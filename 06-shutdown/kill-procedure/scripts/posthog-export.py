#!/usr/bin/env python3
"""Full PostHog project archive before deletion.

Exports raw data, entity definitions, and rendered PNGs/PDFs of all
dashboards and insights (forced to the full time range).

Usage:
    source ~/.claude/.env && export POSTHOG_API_KEY
    python3 posthog-export.py <project_id> <output_dir> <date_from>

Example:
    python3 posthog-export.py 175234 \
        "$HOME/exports/posthog-export" \
        2026-05-01

Requirements:
  - POSTHOG_API_KEY env var (personal API key, EU cloud)
  - Scopes: project:read, insight:read+write, dashboard:read+write,
    query:read, export:write  <-- export:write is NOT default, add it
    at https://eu.posthog.com/settings/user-api-keys
  - macOS `sips` for PNG->PDF conversion (skipped if unavailable)

Known gotchas (learned in production):
  - export_format "application/pdf" is NOT supported -> use image/png,
    then convert locally with sips.
  - The /exports/<id>/content endpoint 302-redirects to object storage.
    The Authorization header MUST NOT be forwarded to the redirect
    target (else 400/403) -> NoAuthRedirect handler below.
  - Insights render with their SAVED date range (e.g. "Last 7 days").
    A dead venture has no recent data -> "no matching events". This
    script PATCHes every insight + dashboard to date_from before
    rendering. Original definitions are saved to JSON first.
  - sessions: SELECT of ALL columns 500s (column with type Unknown).
    Use the curated column list below.
  - persons can legitimately be 0 (anonymous-only tracking).
"""
import json
import os
import subprocess
import sys
import time
import urllib.request

HOST = os.environ.get("POSTHOG_HOST", "https://eu.posthog.com")

SESSION_COLS = [
    "session_id", "distinct_id", "$start_timestamp", "$end_timestamp",
    "duration", "$is_bounce", "$pageview_count", "$autocapture_count",
    "$num_uniq_urls", "$urls", "$entry_current_url", "$entry_pathname",
    "$exit_current_url", "$exit_pathname", "$entry_referring_domain",
    "$channel_type", "$entry_utm_source", "$entry_utm_campaign",
    "$entry_utm_medium", "$entry_utm_content", "$last_external_click_url",
    "$vitals_lcp",
]


class NoAuthRedirect(urllib.request.HTTPRedirectHandler):
    """Strip Authorization header when following redirects to object storage."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        new = super().redirect_request(req, fp, code, msg, headers, newurl)
        if new is not None:
            new.headers.pop("Authorization", None)
        return new


OPENER = urllib.request.build_opener(NoAuthRedirect)


def main():
    if len(sys.argv) != 4:
        print(__doc__)
        sys.exit(1)
    pid, outdir, date_from = sys.argv[1], sys.argv[2], sys.argv[3]
    key = os.environ["POSTHOG_API_KEY"]
    os.makedirs(os.path.join(outdir, "insights_png"), exist_ok=True)

    def api(path, method="GET", body=None, raw=False):
        req = urllib.request.Request(f"{HOST}{path}", method=method)
        req.add_header("Authorization", f"Bearer {key}")
        data = None
        if body is not None:
            req.add_header("Content-Type", "application/json")
            data = json.dumps(body).encode()
        with OPENER.open(req, data) as r:
            return r.read() if raw else json.load(r)

    def paginate(path):
        results, url = [], path
        while url:
            d = api(url.replace(HOST, ""))
            results.extend(d.get("results", []))
            url = d.get("next")
        return results

    def hogql(query):
        d = api(f"/api/environments/{pid}/query/", "POST",
                {"query": {"kind": "HogQLQuery", "query": query}})
        return [dict(zip(d["columns"], row)) for row in d["results"]]

    def save(name, data):
        p = os.path.join(outdir, name)
        with open(p, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        n = len(data) if isinstance(data, list) else "ok"
        print(f"  {name}: {n} items, {os.path.getsize(p) / 1024:.0f} KB")

    def render_png(export_body, out_path, label):
        """Trigger a PNG export, poll until rendered, download."""
        exp = api(f"/api/projects/{pid}/exports/", "POST",
                  {"export_format": "image/png", **export_body})
        for _ in range(40):
            status = api(f"/api/projects/{pid}/exports/{exp['id']}/")
            if status.get("has_content"):
                content = api(
                    f"/api/projects/{pid}/exports/{exp['id']}/content?download=true",
                    raw=True)
                with open(out_path, "wb") as f:
                    f.write(content)
                print(f"  OK {label} ({len(content) / 1024:.0f} KB)")
                return True
            if status.get("exception"):
                print(f"  FAILED {label}: {status['exception']}")
                return False
            time.sleep(3)
        print(f"  TIMEOUT {label}")
        return False

    def safe_name(s):
        return "".join(c if c.isalnum() or c in " -_" else "_"
                       for c in s)[:60].strip()

    def png_to_pdf(png_path):
        pdf_path = png_path.rsplit(".", 1)[0] + ".pdf"
        try:
            subprocess.run(["sips", "-s", "format", "pdf", png_path,
                            "--out", pdf_path], capture_output=True, check=True)
        except (FileNotFoundError, subprocess.CalledProcessError):
            print(f"  (sips unavailable/failed, no PDF for {png_path})")

    # ---- 1. Raw JSON exports (ORIGINAL definitions, before any patching) ----
    print("== JSON exports ==")
    # The query API hard-caps results at 50000 rows regardless of LIMIT.
    # Paginate with a timestamp cursor + uuid dedupe until exhausted.
    # NOTE: ISO timestamps with 'T...Z' in a WHERE literal 500 in ClickHouse;
    # wrap the cursor in parseDateTimeBestEffort() (the 64-variant is
    # unsupported in HogQL).
    events, seen = [], set()
    cursor = f"'{date_from}'"
    while True:
        batch = hogql(
            "SELECT uuid, event, timestamp, distinct_id, person_id, properties "
            f"FROM events WHERE timestamp >= {cursor} "
            "ORDER BY timestamp ASC LIMIT 50000")
        new = [e for e in batch if e["uuid"] not in seen]
        if not new:
            break
        for e in new:  # query API returns properties as JSON string -> parse
            if isinstance(e.get("properties"), str):
                try:
                    e["properties"] = json.loads(e["properties"])
                except ValueError:
                    pass
            seen.add(e["uuid"])
        events.extend(new)
        if len(batch) < 50000:
            break
        cursor = f"parseDateTimeBestEffort('{max(e['timestamp'] for e in batch)}')"
    events.sort(key=lambda e: e["timestamp"])
    save("events.json", events)
    save("sessions.json", hogql(
        f"SELECT {', '.join(SESSION_COLS)} FROM sessions "
        f"WHERE $start_timestamp >= '{date_from}' "
        "ORDER BY $start_timestamp ASC LIMIT 10000"))
    save("persons.json", paginate(f"/api/projects/{pid}/persons/?limit=100"))
    insights = paginate(f"/api/projects/{pid}/insights/?limit=100")
    save("insights.json", insights)
    dashboards = paginate(f"/api/projects/{pid}/dashboards/?limit=100")
    save("dashboards.json", dashboards)
    save("cohorts.json", paginate(f"/api/projects/{pid}/cohorts/?limit=100"))
    save("project_settings.json", api(f"/api/projects/{pid}/"))
    save("event_definitions.json",
         paginate(f"/api/projects/{pid}/event_definitions/?limit=500"))
    save("property_definitions.json",
         paginate(f"/api/projects/{pid}/property_definitions/?limit=500"))

    # ---- 2. Force full time range on dashboards + insights ----
    print("== Set full time range ==")
    for d in dashboards:
        api(f"/api/projects/{pid}/dashboards/{d['id']}/", "PATCH",
            {"filters": {"date_from": date_from, "date_to": None}})
        print(f"  dashboard {d['id']} ({d.get('name')}) -> from {date_from}")
    for ins in insights:
        current = api(f"/api/projects/{pid}/insights/{ins['id']}/")
        q = current.get("query")
        if q and isinstance(q, dict) and "source" in q:
            q["source"]["dateRange"] = {"date_from": date_from, "date_to": None}
            api(f"/api/projects/{pid}/insights/{ins['id']}/", "PATCH",
                {"query": q})
        elif current.get("filters"):
            f2 = current["filters"]
            f2["date_from"], f2["date_to"] = date_from, None
            api(f"/api/projects/{pid}/insights/{ins['id']}/", "PATCH",
                {"filters": f2})
        print(f"  insight {ins['id']} ({ins.get('name') or ins.get('derived_name')}) -> from {date_from}")

    # ---- 3. Render dashboards + insights as PNG, convert to PDF ----
    print("== Dashboard PNGs ==")
    for d in dashboards:
        fname = f"dashboard_{safe_name(d.get('name') or str(d['id'])).lower().replace(' ', '_')}.png"
        p = os.path.join(outdir, fname)
        if render_png({"dashboard": d["id"]}, p, fname):
            png_to_pdf(p)
    print("== Insight PNGs ==")
    for ins in insights:
        name = ins.get("name") or ins.get("derived_name") or str(ins["id"])
        fname = f"insights_png/{ins['id']}_{safe_name(name)}.png"
        render_png({"insight": ins["id"]}, os.path.join(outdir, fname), fname)

    print("Done. Remember: write README.md, visually verify PNGs, "
          "then delete the project ONLY after explicit user confirmation.")


if __name__ == "__main__":
    main()
