#!/usr/bin/env python3
"""Pull Meta Ad campaign insights for performance review.

Usage:
  python3 pull_insights.py --days 7
  python3 pull_insights.py --campaign-id 123456789 --days 14
  python3 pull_insights.py --all --days 30

Requires: META_ACCESS_TOKEN and META_AD_ACCOUNT_ID in ~/.claude/.env
"""

import argparse, json, os, sys
from datetime import datetime, timedelta
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from urllib.parse import urlencode

try:
    from dotenv import load_dotenv
    env_path = os.path.expanduser("~/.claude/.env")
    if os.path.exists(env_path):
        load_dotenv(env_path)
except ImportError:
    pass

API_VERSION = "v20.0"
BASE_URL = f"https://graph.facebook.com/{API_VERSION}"


def api_get(endpoint, params):
    """Make a GET request to the Meta Marketing API."""
    url = f"{BASE_URL}/{endpoint}?{urlencode(params)}"
    try:
        req = Request(url)
        with urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except HTTPError as e:
        error_body = e.read().decode()
        print(f"API Error {e.code}: {error_body}", file=sys.stderr)
        sys.exit(1)


def pull_campaign_insights(account_id, token, days, campaign_id=None):
    """Pull insights for campaigns in the given date range."""
    since = (datetime.now() - timedelta(days=days)).strftime("%Y-%m-%d")
    until = datetime.now().strftime("%Y-%m-%d")

    params = {
        "access_token": token,
        "fields": "campaign_name,impressions,clicks,ctr,cpc,cpm,spend,"
                  "actions,cost_per_action_type,frequency",
        "time_range": json.dumps({"since": since, "until": until}),
        "level": "campaign",
        "limit": 100,
    }

    if campaign_id:
        endpoint = f"{campaign_id}/insights"
    else:
        endpoint = f"{account_id}/insights"

    data = api_get(endpoint, params)
    return data.get("data", [])


def format_report(insights, days):
    """Format insights into a readable markdown report."""
    lines = [
        f"# Meta Ads Performance Report",
        f"_Period: last {days} days | As of: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n",
        "| Campaign | Impressions | Clicks | CTR | CPC | CPM | Spend | Frequency |",
        "|----------|------------|--------|-----|-----|-----|-------|-----------|",
    ]

    total_spend = 0
    total_clicks = 0
    total_impressions = 0

    for row in insights:
        name = row.get("campaign_name", "?")
        imp = int(row.get("impressions", 0))
        clicks = int(row.get("clicks", 0))
        ctr = row.get("ctr", "0")
        cpc = row.get("cpc", "0")
        cpm = row.get("cpm", "0")
        spend = float(row.get("spend", 0))
        freq = row.get("frequency", "0")

        total_spend += spend
        total_clicks += clicks
        total_impressions += imp

        lines.append(
            f"| {name} | {imp:,} | {clicks:,} | {float(ctr):.2f}% "
            f"| {float(cpc):.2f} EUR | {float(cpm):.2f} EUR "
            f"| {spend:.2f} EUR | {float(freq):.1f} |"
        )

    lines.append(f"| **TOTAL** | **{total_impressions:,}** | **{total_clicks:,}** "
                 f"| | | | **{total_spend:.2f} EUR** | |")

    # Conversion actions summary
    lines.append("\n## Conversions\n")
    for row in insights:
        actions = row.get("actions", [])
        costs = row.get("cost_per_action_type", [])
        if actions:
            lines.append(f"### {row.get('campaign_name', '?')}")
            lines.append("| Event | Count | Cost per Event |")
            lines.append("|-------|-------|---------------|")
            cost_map = {c["action_type"]: c["value"] for c in costs} if costs else {}
            for a in actions:
                atype = a["action_type"]
                acount = a["value"]
                acost = cost_map.get(atype, "-")
                if acost != "-":
                    acost = f"{float(acost):.2f} EUR"
                lines.append(f"| {atype} | {acount} | {acost} |")

    return "\n".join(lines)


def main():
    p = argparse.ArgumentParser(description="Pull Meta Ad insights")
    p.add_argument("--days", type=int, default=7, help="Number of days to look back")
    p.add_argument("--campaign-id", default=None, help="Specific campaign ID")
    p.add_argument("--output", default=None, help="Save report to file (default: print)")
    args = p.parse_args()

    token = os.environ.get("META_ACCESS_TOKEN")
    account_id = os.environ.get("META_AD_ACCOUNT_ID")

    if not token:
        print("ERROR: META_ACCESS_TOKEN not found in environment", file=sys.stderr)
        sys.exit(1)
    if not account_id:
        print("ERROR: META_AD_ACCOUNT_ID not found in environment", file=sys.stderr)
        sys.exit(1)

    print(f"Pulling insights for last {args.days} days...")
    insights = pull_campaign_insights(account_id, token, args.days, args.campaign_id)

    if not insights:
        print("No data found for the specified period.")
        return

    report = format_report(insights, args.days)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"Report saved to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
