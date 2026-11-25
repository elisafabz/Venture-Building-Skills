---
name: posthog-dashboard
description: Create or update PostHog dashboards and insights via API for any project. Use when building analytics dashboards, funnels, trend charts, or cohorts in PostHog.
model: sonnet
effort: low
---

# PostHog Dashboard Builder

> **Requires:** PostHog MCP or a PostHog API key.

Create and manage PostHog dashboards, insights, cohorts, and annotations via the PostHog API. Venture-agnostisch — works for any project.

## Prerequisites

- `POSTHOG_API_KEY` (phx_... Personal API Key) in `~/.claude/.env`
- `POSTHOG_HOST` (https://eu.posthog.com) in `~/.claude/.env`
- API Key needs write scopes: `cohort:write`, `dashboard:write`, `insight:write`, `annotation:write`, `action:write`

## Project IDs


To discover project IDs: `GET /api/projects/`

---

## Session Replay — ALWAYS ON

**Session Replay MUST always be enabled** for every project. Watch recordings of how users interact with your web app to diagnose issues and understand user behavior.

### Activation checklist (verify for every project)

1. **PostHog Project Settings → Session Replay → Enable**: Must be ON
2. **posthog-js config**: `session_recording: { maskAllInputs: true }` (GDPR — mask inputs by default)
3. **URL Blocklist**: Set `session_recording_url_blocklist_config` to exclude `/admin` pages (see below)
4. **Verify in PostHog UI**: Go to Replay tab, confirm recordings appear
5. **Standard dashboard**: Always include a "Session Replay" link/note so the team knows recordings are available

If Session Replay is not active for a venture, flag it immediately and help activate it.

---

## Project-Level Test Account Filter — ALWAYS SET AUTOMATICALLY

**Every time this skill touches a PostHog project** (dashboard, insight, cohort, settings), verify and — if missing — set the project-level `test_account_filters` WITHOUT asking. This is the central filter that "Filter out internal and test users" applies everywhere.

Required entries (APPEND to existing filters, never remove existing ones like cohort filters):

```json
{
  "id": PROJECT_ID,
  "test_account_filters": [
    ...existing filters...,
    {"key": "$host", "type": "event", "value": ["gtm-msr.appspot.com"], "operator": "is_not"},
    {"key": "$geoip_country_code", "type": "event", "value": ["AT", "DE", "CH"], "operator": "exact"}
  ],
  "test_account_filters_default_checked": true
}
```

Set via MCP tool `project-settings-update` (or `PATCH /api/projects/{id}/`).

Why:
- `gtm-msr.appspot.com` is the **Google Tag Manager scanner bot**: it renders the GTM container server-side and fires ALL tags (fake pageviews, cta_clicks, even conversion events). Discovered in production: dozens of fake cta_click and email_submit events.
- Geo-filtering to your target market is a sensible default (bots often come from US data centers). AT-only only if the user explicitly asks.
- `test_account_filters_default_checked: true` makes every NEW insight apply the filter by default.

In insights created by this skill, set `"filterTestAccounts": true` so the project filter is applied.

### URL Blocklist — Standard for all ventures

Every venture MUST block `/admin` from session recordings. Admin pages are internal-only and clutter the replay list.

Set via MCP tool `project-settings-update`:
```json
{
  "id": PROJECT_ID,
  "session_recording_url_blocklist_config": [
    {"url": "/admin", "matching": "regex"}
  ]
}
```

This blocks recordings on any URL containing `/admin` (e.g. `/admin`, `/admin/dashboard`, `/admin/users`). Existing recordings are not affected.

---

## CRITICAL RULES (learned the hard way)

### 1. InsightVizNode Wrapper — MANDATORY

**All insights MUST use the `InsightVizNode` wrapper.** Without it, the API accepts the insight but the PostHog UI renders empty/blank charts. No error, just blank tiles.

WRONG (charts won't render):
```json
{"query": {"kind": "TrendsQuery", "series": [...]}}
```

CORRECT (charts render):
```json
{
  "query": {
    "kind": "InsightVizNode",
    "source": {
      "kind": "TrendsQuery",
      "series": [...],
      "interval": "day",
      "dateRange": {"date_from": "-30d", "explicitDate": false},
      "properties": [],
      "trendsFilter": {"display": "ActionsLineGraph", "showLegend": false, "showValuesOnSeries": false, "smoothingIntervals": 1},
      "filterTestAccounts": true
    }
  }
}
```

### 2. Operator Names — NOT what you'd expect

Inside InsightVizNode, the operator `"is"` does NOT work. Use:
- `"operator": "exact"` = equals / is
- `"operator": "is_not"` = not equals
- `"operator": "icontains"` = contains (case insensitive)
- `"operator": "not_icontains"` = does not contain (case insensitive)

### 3. Geo Properties — Events only, NOT Persons

- `$geoip_country_code`, `$geoip_city_name` etc. exist on **events**, NOT on persons
- Person-level cohorts with geo filters will always return 0 persons
- Always put geo filters in the `properties` array on each `EventsNode` in the series

### 4. Properties go on SERIES level, not top level

Put filter properties on each EventsNode inside `series[].properties`, not on `source.properties`. The top-level `properties` should be `[]`.

---

## Standard Filter: the target market + Clean Traffic

The standard filter set for "echte User" is:

```json
[
  {"key": "$geoip_country_code", "type": "event", "value": ["AT", "DE", "CH"], "operator": "exact"},
  {"key": "$host", "type": "event", "value": ["gtm-msr.appspot.com"], "operator": "is_not"},
  {"key": "$current_url", "type": "event", "value": "gtm_debug", "operator": "not_icontains"},
  {"key": "$current_url", "type": "event", "value": "localhost", "operator": "not_icontains"},
  {"key": "$current_url", "type": "event", "value": "127.0.0.1", "operator": "not_icontains"},
  {"key": "$current_url", "type": "event", "value": "lovable", "operator": "not_icontains"},
  {"key": "$current_url", "type": "event", "value": "netlify", "operator": "not_icontains"},
  {"key": "$referring_domain", "type": "event", "value": "tagassistant.google.com", "operator": "is_not"}
]
```

### What this filters out and why

| Filter | Reason |
|--------|--------|
| Country != the target market | Team in Italy/Estonia, bots in US data centers (The Dalles, Boardman, Council Bluffs = Google/AWS/Meta), random global crawlers |
| `gtm-msr.appspot.com` host | GTM scanner bot renders the container and fires ALL tags (fake pageviews, clicks, conversions) |
| `gtm_debug` in URL | Google Tag Manager preview/debug sessions |
| `localhost` in URL | Local development server |
| `127.0.0.1` in URL | Local development server (alternative) |
| `lovable` in URL | Lovable.dev preview deployments |
| `netlify` in URL | Netlify staging/preview deployments |
| `tagassistant.google.com` referrer | GTM Tag Assistant debug tool |

**Default is the target market — apply automatically without asking.** Use AT-only only if the user explicitly requests it.

---

## Display Types

| Display Value | Chart Type | Best for |
|--------------|------------|----------|
| `ActionsLineGraph` | Line chart | Trends over time (default) |
| `ActionsBarValue` | Horizontal bar | Breakdowns, comparisons |
| `ActionsBar` | Vertical bar | Time-based comparisons |
| `ActionsPie` | Pie chart | Proportions |
| `ActionsTable` | Table | Detailed data |
| `WorldMap` | World map | Geographic distribution |
| `BoldNumber` | Single big number | KPI headlines |

## Math Types

| Math | Description |
|------|-------------|
| `total` | Total event count (default) |
| `dau` | Unique users per day |
| `weekly_active` | Weekly active users |
| `monthly_active` | Monthly active users |
| `unique_group` | Unique groups |
| `avg_count_per_actor` | Average events per user |

---

## API Patterns

### Load env
```bash
source ~/.claude/.env
```

### List projects
```bash
curl -s -H "Authorization: Bearer $POSTHOG_API_KEY" "$POSTHOG_HOST/api/projects/" | python3 -c "
import json, sys
for p in json.load(sys.stdin)['results']:
    print(f'ID: {p[\"id\"]} | {p[\"name\"]} | Events: {p[\"ingested_event\"]}')"
```

### Create dashboard
```bash
curl -s -X POST -H "Authorization: Bearer $POSTHOG_API_KEY" -H "Content-Type: application/json" \
  "$POSTHOG_HOST/api/projects/{PROJECT_ID}/dashboards/" \
  -d '{"name": "Dashboard Name", "description": "...", "tags": ["venture-name"]}'
```

### Create Trends insight
```bash
curl -s -X POST -H "Authorization: Bearer $POSTHOG_API_KEY" -H "Content-Type: application/json" \
  "$POSTHOG_HOST/api/projects/{PROJECT_ID}/insights/" \
  -d '{
    "name": "Insight Name",
    "saved": true,
    "dashboards": [DASHBOARD_ID],
    "query": {
      "kind": "InsightVizNode",
      "source": {
        "kind": "TrendsQuery",
        "series": [
          {"kind": "EventsNode", "event": "$pageview", "name": "$pageview", "math": "dau",
           "properties": [STANDARD_FILTER_HERE]}
        ],
        "interval": "day",
        "dateRange": {"date_from": "-30d", "explicitDate": false},
        "properties": [],
        "trendsFilter": {"display": "ActionsLineGraph", "showLegend": true},
        "filterTestAccounts": true
      }
    }
  }'
```

### Create Funnel insight
```bash
curl -s -X POST ... -d '{
    "query": {
      "kind": "InsightVizNode",
      "source": {
        "kind": "FunnelsQuery",
        "series": [
          {"kind": "EventsNode", "event": "$pageview", "name": "$pageview", "custom_name": "Step 1",
           "properties": [STANDARD_FILTER_HERE]},
          {"kind": "EventsNode", "event": "signup", "name": "signup", "custom_name": "Step 2",
           "properties": [STANDARD_FILTER_HERE]}
        ],
        "dateRange": {"date_from": "-30d", "explicitDate": false},
        "properties": [],
        "funnelsFilter": {"funnelVizType": "steps"},
        "filterTestAccounts": true
      }
    }
  }'
```

### Create Lifecycle insight (new vs returning users)
```bash
curl -s -X POST ... -d '{
    "query": {
      "kind": "InsightVizNode",
      "source": {
        "kind": "LifecycleQuery",
        "series": [
          {"kind": "EventsNode", "event": "$pageview", "name": "$pageview",
           "properties": [STANDARD_FILTER_HERE]}
        ],
        "interval": "week",
        "dateRange": {"date_from": "-30d", "explicitDate": false},
        "properties": [],
        "lifecycleFilter": {"showLegend": false},
        "filterTestAccounts": true
      }
    }
  }'
```

### Breakdown by UTM content (ad creative comparison)
Add to TrendsQuery source:
```json
"breakdownFilter": {"breakdowns": [{"property": "utm_content", "type": "event"}]}
```

### HogQL query (for ad-hoc analysis, not saved insights)
```bash
curl -s -H "Authorization: Bearer $POSTHOG_API_KEY" -X POST "$POSTHOG_HOST/api/projects/{PROJECT_ID}/query/" \
  -H "Content-Type: application/json" \
  -d '{
    "query": {
      "kind": "HogQLQuery",
      "query": "SELECT event, count() FROM events WHERE timestamp > now() - interval 30 day GROUP BY event ORDER BY count() DESC"
    }
  }'
```

### Update insight
```bash
curl -s -X PATCH -H "Authorization: Bearer $POSTHOG_API_KEY" -H "Content-Type: application/json" \
  "$POSTHOG_HOST/api/projects/{PROJECT_ID}/insights/{INSIGHT_ID}/" \
  -d '{"query": {...}}'
```

### Delete insight (soft delete)
```bash
curl -s -X PATCH ... -d '{"deleted": true}'
```

### Create cohort
```bash
curl -s -X POST -H "Authorization: Bearer $POSTHOG_API_KEY" -H "Content-Type: application/json" \
  "$POSTHOG_HOST/api/projects/{PROJECT_ID}/cohorts/" \
  -d '{"name": "...", "description": "...", "is_static": false,
       "filters": {"properties": {"type": "AND", "values": [...]}}}'
```

Note: Cohorts with geo filters on person properties won't work (persons have no geo data). Use behavioral cohorts or event-level filters in insights instead.

---

## Standard Dashboard Template

When creating a new venture dashboard, include these insights:

1. **Pageviews & Key Events (Trend)** — Line chart, daily, math=dau, all key events as separate series
2. **Conversion Funnel** — Steps: Pageview > CTA Click > Signup > Payment (adapt per venture)
3. **Traffic sources** — Bar chart, breakdown by `$referring_domain`
4. **Geo-Verteilung** — Bar chart, breakdown by `$geoip_city_name`
5. **Geraete & Browser** — Bar chart, breakdown by `$device_type`

Optional but recommended:
6. **UTM campaign performance** — Breakdown by `utm_content` (compares ad creatives)
7. **Paid vs. Organic** — Breakdown by `utm_source` (meta vs direct vs google)
8. **Lifecycle** — LifecycleQuery (new vs returning vs resurrected vs dormant)
9. **Rageclicks** — Trend of `$rageclick` events (UX frustration signal)
10. **Tageszeit-Heatmap** — HogQL: traffic by hour (helps with ad scheduling)

---

## Workflow

1. Verify project-level `test_account_filters` (GTM scanner + the target market, see section above) — set automatically if missing. the target market is the default; only ask if the user mentioned AT-only.
2. Identify project ID from table above
3. Create dashboard with tags
4. Build PROPS variable with standard filter (the target market or AT + test traffic exclusions)
5. Create insights with `InsightVizNode` wrapper + `"saved": true` + `"dashboards": [ID]`
6. Put PROPS on every EventsNode in series, keep top-level `properties: []`
7. Verify in UI — charts should render immediately after page load
8. If charts are blank: check InsightVizNode wrapper is present
9. If cohort shows 0 persons: geo filters don't work on persons, use event-level filters

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| Charts blank/empty | Missing `InsightVizNode` wrapper | Wrap query in `{"kind": "InsightVizNode", "source": {...}}` |
| Charts blank/empty | Ad blocker in browser | Disable ad blocker for eu.posthog.com |
| Validation error with `is` | Wrong operator name | Use `exact` instead of `is` |
| Cohort shows 0 persons | Geo filter on person level | Persons have no geo props, use event-level |
| 792 validation errors | `is` operator in InsightVizNode | Replace `is` with `exact` |
| API accepts but UI empty | Query format mismatch | Compare with working dashboard's query format |
