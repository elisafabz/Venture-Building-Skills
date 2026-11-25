# PostHog Archive Procedure (before project deletion)

Complete, proven procedure to snapshot a PostHog project before deleting it.
Proven procedure. Run via
`scripts/posthog-export.py`.

## Prerequisites

1. `POSTHOG_API_KEY` + `POSTHOG_HOST` in `~/.claude/.env` (EU cloud: `https://eu.posthog.com`)
2. Key scopes: `project:read`, `insight:read+write`, `dashboard:read+write`,
   `query:read`, **`export:write`** (NOT default! User must add it at
   https://eu.posthog.com/settings/user-api-keys - error otherwise:
   `API key missing required scope 'export:write'`)
3. Verify the key against the target project before use (rule:
   always verify API tokens - `GET /api/projects/<id>/` must return 200
   and the expected project name.

## Steps

1. **Find project ID** - MCP `projects-get` (or `GET /api/projects/`), then
   MCP `switch-project` if querying via MCP.
2. **Inventory first** - count everything so nothing is missed:
   - Events: `SELECT count(), min(timestamp), max(timestamp), count(DISTINCT person_id) FROM events WHERE timestamp >= '<launch>'`
   - Event types: `SELECT event, count() FROM events ... GROUP BY event`
   - Entities — count ALL of them, projects differ: `system.insights/dashboards/cohorts/feature_flags/actions/annotations/surveys/experiments/notebooks/early_access_features/session_recordings/session_recording_playlists/hog_functions/batch_exports/data_warehouse_sources/integrations` + `groups`. Export any non-zero entity as JSON (one project had a hog function plus recording playlists that the standard script does not cover)
   - Persons: `SELECT count() FROM persons` (0 is normal for anonymous-only tracking)
3. **Create export folder**: `<venture archive folder>/posthog-export/`
   (a folder outside the git repo, NEVER the repo itself)
4. **Run the script**:
   ```bash
   source ~/.claude/.env && export POSTHOG_API_KEY
   python3 <skill-dir>/scripts/posthog-export.py \
       <project_id> "<export_dir>" <date_from>
   ```
   `date_from` = first day of the month the venture launched (covers everything).
   The script exports (in this order):
   - JSON: events (full properties), sessions, persons, insights, dashboards,
     cohorts, project settings, event/property definitions
   - Patches ALL dashboards + insights to the full date range
     (original definitions are already saved as JSON before patching)
   - Renders every dashboard + every insight as PNG, dashboards also as PDF
5. **Visually verify PNGs** (Read tool on the images):
   - Every tile/insight header must show the full range (e.g. "LAST 68 DAYS"),
     NOT "LAST 7 DAYS" / "LAST 30 DAYS"
   - Empty tiles can be legitimate - check before re-exporting (see gotchas)
6. **Write README.md** into the export folder: project ID, export date, data
   range, kill context, file list, event overview table, note which entity
   types were empty.
7. **Delete the project** - ONLY after explicit user confirmation that the
   export is complete. UI: Project Settings > Danger Zone. This is the ONE
   exception to the "never delete" rule, and only because the full snapshot
   exists locally.

## Gotchas (all hit on 2026-07-08)

| Problem | Fix |
|---|---|
| `application/pdf` export -> "not supported for insights" | Export `image/png`, convert locally: `sips -s format pdf in.png --out out.pdf` |
| Download of `/exports/<id>/content` fails 400/403 | Endpoint 302-redirects to object storage; Authorization header must NOT be forwarded (script handles it; with curl use `-L`, it strips auth cross-host) |
| Insight PNGs empty ("no matching events") | Insights render with their SAVED range (Last 7/30 days) - dead venture has no recent data. Patch `query.source.dateRange` (new format) or `filters.date_from` (legacy) first |
| Dashboard tiles still on old range | Dashboard-level filter overrides tiles: PATCH dashboard `filters: {date_from, date_to: null}` |
| `SELECT *`-style sessions query -> HTTP 500 | One column has type Unknown; use the curated column list in the script |
| `countIf(is_identified)` -> Illegal type Int8 | Use `countIf(is_identified = 1)` |
| persons export = 0 items | Normal for anonymous-only tracking; the unique `person_id`s are in events.json. Note it in README, not a data loss |
| Tile empty even with full range | Can be real: event never instrumented (e.g. widget-load never tracked), or insight type needs identified persons (lifecycle/growth accounting). Explain in README |
| Query API result cap: **50000 rows hard**, regardless of LIMIT | Script paginates with timestamp cursor + uuid dedupe. ALWAYS verify exported count == inventory count! (in one case the first run silently returned 50,000 of 51,010) |
| WHERE with ISO timestamp `'...T11:41:38.632000Z'` -> ClickHouse 500 | Date-only strings work; for full timestamps wrap in `parseDateTimeBestEffort('...')` (`parseDateTime64BestEffort` is NOT supported in HogQL) |
| REST endpoints | Paginate via `next` link |
| Dashboard PNG cut off at exactly 10000 px height | PostHog renderer height limit. Build a multi-page "_FULL.pdf" instead: page 1 = dashboard PNG, then each tile's individual insight PNG as its own page (PIL: `pages[0].save(pdf, save_all=True, append_images=pages[1:])`, tile order from `GET /dashboards/<id>/` -> `tiles`) |
| Dashboard tiles render gray/empty on large projects | Screenshot worker captures before queries finish. Re-trigger the export once (query cache is then warm) and/or rely on individual insight PNGs |
| events.json `properties` saved as JSON string | Query API returns properties as string - parse with `json.loads` before saving (script does this since 2026-07-08) |

## Verification checklist

- [ ] events.json count == inventory count
- [ ] Every insight PNG shows full-range header
- [ ] Both/all dashboard PNGs+PDFs show full-range tiles
- [ ] Empty tiles explained in README
- [ ] README.md complete
- [ ] User explicitly confirmed deletion (or project intentionally kept)
