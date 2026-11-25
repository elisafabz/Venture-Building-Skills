---
name: venture-learnings
description: Use when a venture is being shut down or paused and the user wants a structured learnings document for future ventures. Triggered by requests like "create learnings", "what did we learn", "shut down the venture", "kill the venture", "post-mortem", "shutdown learnings".
model: sonnet
effort: medium
---

# Venture Learnings

Generate a branded PDF documenting what worked, what didn't, market insights, technical learnings, and recommendations for future ventures. Pulls real data from all available sources.

## Prerequisites

- **Supabase:** Project must have an admin dashboard with a `dashboard-stats` Edge Function
- **Meta Marketing API** (optional): `META_ACCESS_TOKEN` + `META_AD_ACCOUNT_ID` in `~/.claude/.env`
- **Google Analytics** (optional): Accessible via browser
- **Google Ads** (optional): Accessible via browser
- **PostHog** (optional): Accessible via browser
- **Fonts:** Symlinked from `<skill-dir>/fonts/`
- **Python:** `reportlab` package installed

## Workflow

### Phase 1: Context & Configuration

1. **Read CLAUDE.md** from the current project to extract:
   - Venture name, URL, hosting, backend
   - Brand colors (CSS custom properties)
   - Tech stack details
   - Any funnel/survey structure

2. **Ask the user 3-4 questions:**
   - "Which time period?" (default: entire runtime)
   - "Which data sources are available?" (Supabase, Meta, GA4, Google Ads, PostHog)
   - "Why is it being shut down?" (one short sentence — it goes into the core insight)
   - "Are there specific learnings you want recorded?"

3. **Classify the fail type** (Failbook, VNTR/PostFinance — makes learnings comparable across ventures). Pick exactly one primary category, based on the data:
   - **No-need fail:** no genuine customer or market need (the most common cause)
   - **Happy Failure:** the team/idea originators themselves relieved that it's ending
   - **Failure by following management:** failed on internal resistance or missing support
   - **Epic Fail:** unexpected collapse despite a solid concept (partner, regulation, platform)
   Include the category prominently in the document. Also note that failures are not final — record under which changed conditions the idea would become interesting again.

4. **Avoid "resulting"** (Thinking in Bets, Annie Duke): Judge decision quality separately from outcome quality — good decisions can fail through bad luck, bad ones can succeed through good luck. For each key decision in the learnings doc, note: was the decision sound given what was knowable at the time? Only decision-quality lessons transfer to future ventures; outcome-only lessons teach superstition.

3. **Determine venture name** for campaign filtering:
   - Extract from CLAUDE.md or project directory
   - Meta campaign convention: `yymm_venture` or `yymm_venture_#nr details`

### Phase 2: Data Collection (automated, parallel where possible)

#### Supabase Data (required)
1. Open admin dashboard in browser (browser automation)
2. Get JWT from localStorage (`sb-{ref}-auth-token`)
3. Call `dashboard-stats` Edge Function via JavaScript
4. Extract: sessions, surveys, completions, signups, carts, checkouts, survey responses, session analytics

#### Meta Marketing API (if configured)
1. Read credentials from `~/.claude/.env`
2. Fetch campaigns filtered by venture name:
   ```
   GET /v21.0/act_{id}/campaigns?fields=name,status,objective
   ```
3. For matching campaigns, fetch ad-level insights:
   ```
   GET /v21.0/{campaign_id}/insights?level=ad&fields=ad_name,impressions,reach,clicks,spend,actions,cost_per_action_type,frequency&date_preset=maximum
   ```
4. Extract: LPV, CPR, Impressions, Reach, Spend per ad

#### Google Analytics (if available)
1. Open GA4 property in browser
2. Extract via JavaScript or page scraping:
   - Traffic sources breakdown
   - Channel groupings with session counts
   - Geo distribution
   - Bounce rate / engagement rate
   - Top landing pages

#### Google Ads (if available)
1. Open Google Ads dashboard in browser
2. Extract:
   - Campaign performance (clicks, impressions, CPC, conversions, ROAS)
   - Ad group level data
   - Search terms report (if Search campaigns)

#### PostHog (if available)
1. Open PostHog dashboard in browser
2. Extract:
   - Event counts and trends
   - Funnel conversion rates
   - Retention cohorts
   - Feature flag usage
   - Session recordings summary (count, avg duration)

### Phase 3: Analysis & Interpretation

Before generating the PDF, analyze ALL collected data and produce:

1. **Core insight:** one sentence that captures the fundamental learning (e.g. "there was interest, but no willingness to pay")
2. **What worked:** Identify 3-5 things that worked well, with data to back them up
3. **What did not work:** identify 3-5 things that failed, with specific numbers showing where and why
4. **Market insights:** Aggregate survey/user data into actionable market understanding
5. **Technical learnings:** Stack evaluation, what to keep, what to change
6. **Recommendations:** Prioritized by timeline (Quick Wins / Medium-term / Strategic)
7. **Benchmarks:** Key metrics as reference for future ventures

### Phase 4: PDF Generation

1. **Map brand colors** from CLAUDE.md to Terracotta Precision palette:
   - `bg`: warm off-white `#f4f1ec`
   - `fg`: project's primary/dark color
   - `accent`: project's signal/accent color
   - `muted`: warm gray derived from fg
   - `border`: `#dbd6ce`
   - `clay`: `#ece7df`

2. **Build JSON data file** with all sections (see generate_learnings.py for schema)

3. **Run generate_learnings.py:**
   ```bash
   python3 <skill-dir>/generate_learnings.py \
     /tmp/{venture}_learnings_data.json \
     <output folder>/{venture}_venture_learnings.pdf
   ```

4. **Open the PDF** for the user.

### JSON Data Schema

```json
{
  "venture": "venture-name",
  "date": "YYYY-MM-DD",
  "period": "Month YYYY – Month YYYY",
  "colors": { "bg", "fg", "accent", "muted", "border", "clay" },
  "title": "Venture Learnings",
  "subtitle": "One-line venture description",
  "summary_line": "~N months live · ~X ad spend · Y sessions · Z purchases",
  "sections": [
    {
      "num": 1,
      "title": "Section Title",
      "blocks": [
        {
          "subtitle": "Block Title",
          "callout": "Optional highlighted text",
          "bullets": ["bullet 1", "bullet 2"],
          "takeaway": "Optional → takeaway text",
          "table_headers": ["Col1", "Col2"],
          "table_rows": [["val1", "val2"]]
        }
      ]
    }
  ]
}
```

### Standard Sections

Always include these sections (adapt content based on available data):

| # | Section | Content |
|---|---------|---------|
| 1 | What worked | 3-5 successes with data, each with takeaway for next venture |
| 2 | What did not work | 3-5 failures with specific drop-off numbers, each with a takeaway |
| 3 | Market insights | Survey aggregations, user demographics, demand signals |
| 4 | Technical learnings | Stack evaluation table, what to keep/change |
| 5 | Recommendations for the next venture | Domain-specific plus general learnings plus benchmarks |
| 6 | Data assets that remain | What data, code and insights carry forward |

Omit Section 3 if no survey/user data exists. All other sections are always included.

## Important Notes

- **Read-only:** Never modify data in any source system
- **Language:** Report content in the language of the venture's market, code/technical terms in English
- **Tone:** Factual, analytical, action-oriented — no hype, no blame
- **Privacy:** Never include raw email addresses or personal data
- **Numbers:** Double-check all percentages against raw data before generating PDF
- **Venture filtering:** For Meta campaigns, filter case-insensitively by venture name using your naming convention (`yymm_venture`)
- **Design:** Follow Terracotta Precision philosophy — see `references/report-philosophy.md`
