---
name: analyst-report
description: Generate a structured PDF analyst report (User Behavior Analysis) for any project — pulls data from Supabase dashboard + Meta Marketing API, analyzes traffic, campaigns, funnel, user profiles, and generates actionable recommendations.
model: sonnet
effort: medium
---

# Analyst Report — User Behavior Analysis

> **Requires:** Supabase access; Meta Marketing API (MCP or REST) for ad data.

Generate a professional, data-driven PDF report for any venture. Pulls real data from Supabase and Meta Marketing API, analyzes it, and produces a branded PDF with interpretation and recommendations.

## Prerequisites

- **Supabase:** Project must have an admin dashboard with a `dashboard-stats` Edge Function
- **Meta Marketing API:** Token + Ad Account ID configured in `~/.claude/.env`
  - `META_ACCESS_TOKEN` — System User Token with `ads_read` permission
  - `META_AD_ACCOUNT_ID` — Format: `act_123456789`
- **Fonts:** Cormorant Garamond + Inter in `<skill-dir>/fonts/`
- **Python:** `reportlab` package installed (`pip3 install reportlab`)

## Workflow

### Phase 1: Context & Configuration (ask user)

1. **Read CLAUDE.md** from the current project to extract:
   - Project/venture name
   - Brand colors (CSS custom properties)
   - Font families
   - Any survey structure or funnel info

2. **Ask the user 2-3 questions:**
   - "Which time period?" (default: last 30 days)
   - "Focus?" (full analysis / traffic only / funnel only / ads only)
   - "Include Meta Ads?" (yes/no — default: yes)

3. **Determine venture name** for Meta campaign filtering:
   - Extract from project directory name or CLAUDE.md
   - Campaign naming convention: `yymm_venture` or `yymm_venture_#nr details`
   - Filter campaigns case-insensitively by venture name in campaign name

### Phase 2: Data Collection (automated)

#### Single-source-of-truth rule: the Supabase admin dashboard is the primary data source

**CRITICAL:** the Supabase admin dashboard (the dashboard-stats edge function) is the SINGLE SOURCE OF TRUTH for all visitor, funnel and lead figures. NEVER use PostHog data for these metrics — PostHog filters test accounts and counts differently, which produces incorrect (lower) numbers.

- **Visitors, sessions, devices, countries, traffic sources** → ONLY from the Supabase admin dashboard
- **Funnel (CTA clicks, onboarding starts, completions, signups)** → ONLY from the Supabase admin dashboard
- **Step-by-step onboarding drop-off** → ONLY from the Supabase admin dashboard
- **Survey responses and age distribution** → ONLY from the Supabase admin dashboard
- **Meta Ads Performance** → Meta Marketing API (MCP or REST)
- PostHog may ONLY be used as a supplement (e.g. bounce rate, session duration) where the admin dashboard does not provide that metric

#### Supabase Data (SSOT)
1. Ask the user for a screenshot or for the figures from the admin dashboard
2. ALTERNATIV: Open the admin dashboard in the browser (browser automation)
3. Get the authenticated user's JWT from localStorage
4. Call the `dashboard-stats` Edge Function via JavaScript
5. Extract the full JSON response containing:
   - Stats (sessions, surveys, completions, signups)
   - Session analytics (by date, country, device, browser, UTM source)
   - Survey responses (raw data for aggregation)
   - Funnel data (screen-by-screen conversion)
   - Event counts
   - Exit intent data
6. **Plausibility check:** if two metrics contradict each other (e.g. more signups than completions), ask the user IMMEDIATELY rather than assuming

#### Meta Marketing API Data
1. Read credentials from `~/.claude/.env`
2. Fetch campaigns filtered by venture name using the **full lifetime** time range (not just the last 30 days, unless explicitly requested otherwise):
   ```
   GET /v21.0/act_{id}/campaigns?fields=name,status,objective
   ```
3. For matching campaigns, fetch insights with time_range from campaign start:
   ```
   GET /v21.0/{campaign_id}/insights?level=ad&fields=ad_name,impressions,reach,clicks,spend,actions,cost_per_action_type,frequency&time_range={"since":"YYYY-MM-DD","until":"YYYY-MM-DD"}
   ```
4. Extract key metrics per ad:
   - Ad name, status
   - Landing Page Views (LPV) from `actions` where `action_type=landing_page_view`
   - Cost per Result (CPR) from `cost_per_action_type`
   - Impressions, Reach, Frequency, Unique Link Clicks, Spend
5. **Include ONLY campaigns under the current venture name** (no predecessor names such as "oldbrand" for "newbrand", unless explicitly requested)

### Phase 3: Analysis & Interpretation

Before generating the PDF, analyze the data and produce insights:

1. **Traffic analysis:** Trends, peaks, channel mix, geo distribution, device split
2. **Campaign analysis:** Best/worst performing ads, CPR comparison, creative patterns
3. **Funnel analysis:** Drop-off points, conversion rates per step, critical leaks
4. **User profile:** Demographics aggregation, behavioral patterns
5. **Recommendations:** Prioritized by impact (Quick Wins → Medium-term → Strategic)

### Phase 4: PDF Generation

1. **Read brand tokens** from CLAUDE.md:
   - Map CSS custom properties to PDF colors
   - Identify heading font (typically serif) and body font (typically sans-serif)
   - Fall back to Cormorant Garamond + Inter if not specified

2. **Run generate_report.py** with the collected data:
   - Pass data as JSON via stdin or temp file
   - Brand colors, fonts, venture name as arguments
   - Output path: `<output folder>/{venture}_user_behaviour_analysis_{date}.pdf`

3. **Report sections** (include/exclude based on available data):

   | Section | Condition |
   |---------|-----------|
   | Executive Summary | Always |
   | Traffic & Akquise | Always (from Supabase sessions) |
   | Meta Campaign Performance | Only if Meta ads data available |
   | Survey Funnel | Only if survey responses exist |
   | User Profile | Only if survey demographics exist |
   | Needs and motivation | Only if survey desire or trigger data exists |
   | Interpretation | Always |
   | Handlungsempfehlungen | Always |

4. **Open the PDF** for the user after generation.

## Report Design Philosophy

Follow the "Terracotta Precision" design philosophy from `references/report-philosophy.md`:
- Clean, data-driven layout with generous white space
- Brand colors used sparingly — accent color for section numbers, KPIs, chart bars
- Cormorant Garamond (or project serif) for headings, Inter (or project sans) for body
- Tables: thin hairlines, no alternating row fills, right-aligned numbers
- Callout boxes for key insights (clay background + accent left bar)
- Funnel visualization as horizontal bars with drop-off indicators

## Important Notes

- **Read-only:** This skill never modifies data in Supabase or Meta
- **Campaign filtering:** Always filter by venture name using the naming convention (`yymm_venture`)
- **Language:** Report content in German (local), code discussion in English
- **Tone:** Sachlich, analytisch, handlungsorientiert — no hype, no fluff
- **Privacy:** Never include raw email addresses or personal data in reports
- **No pricing screens:** Only include survey screens that actually exist in the project
