---
name: kill-procedure
description: Systematic venture shutdown procedure - documents, deactivates services, archives data, and updates all systems. Interactive checklist that asks before each step.
model: sonnet
effort: medium
---

# Kill Procedure - Venture Shutdown

> **Requires:** PostHog MCP or a PostHog API key for the data export.

A systematic wind-down of a venture. An interactive process — every step is agreed before it happens.

## Trigger

Aktiviert durch: "kill venture", "venture einstellen", "shutdown", "kill-procedure", "venture killen", "abwickeln"

## Prerequisites

Before starting, confirm with user:
1. Which venture? (check cwd and CLAUDE.md)
2. Is this a final kill or a pause?
3. Any special considerations?

## Checklist (in order)

### Phase 1: Documentation (automated, ask before each)

- [ ] **Project journal** — a kill entry with KPIs, reasoning and a data snapshot
  - Ask: "Shall I write the kill entry into the project journal?"
  - Include: What, Why, Result, Key Data table, Impact on strategy
  - Pull data from: Admin dashboard, Meta Ads, project journal history

- [ ] **Changelog** - No entry needed (kill is not a user-facing product change)

- [ ] **Project notes** - Record the project as killed
  - Ask: "Shall I mark this as killed in the project notes?"

- [ ] **PDF Analyst Report** - Final report with all data
  - Ask: "Shall I create a PDF final report?"
  - Use /analyst-report skill
  - Save to: <venture archive folder>/

### Phase 2: strategy document updates (automated, ask before each)

- [ ] **Project status** — set to "cancelled"
  - Ask: "Shall I set the project status to cancelled?"

- [ ] **Kill notice** — add a kill notice at the top of the page
  - Ask: "Shall I add a kill notice at the top of the page?"

- [ ] **Recommendation** — fill out the recommendation section
  - Ask: "Shall I fill out the recommendation section? (concept or prototype phase: stop)"
  - Content: Stop recommendation, next steps, reasoning (data-backed), strategic risks/challenges, future recommendations
  - IMPORTANT: English, strategic risks (not operational), correct phase (Concept vs Prototype)

- [ ] **Dashboard conclusions** — fill in "which conclusion can we draw"
  - Ask: "Shall I fill in the dashboard conclusions?"
  - Data-driven analysis of what the metrics tell us

- [ ] **Wrap-up / post-mortem** — a comprehensive wrap-up
  - Ask: "Shall I write a full post-mortem into the strategy document?"
  - Sections: Executive Summary, Hypothesis Tested, User Data, Market Data, Campaign Data, Funnel Analysis, What Worked/Didn't, Key Learnings, Future Recommendations, Financial Summary

### Phase 3: Service Deactivation (mixed - some automated, some manual)

- [ ] **Meta Ads** - Check if all campaigns are paused
  - Automated: Check campaign status via Meta API
  - Ask: "Shall I check the Meta campaigns? If any are active, shall I pause them?"
  - Use ad account from env/config

- [ ] **Netlify/Vercel** - Disable project (NOT delete)
  - Semi-automated: Navigate to hosting dashboard, find project
  - Ask: "Shall I deactivate the hosting project? (It will NOT be deleted, only taken offline)"
  - If browser automation fails: "Please deactivate the project manually: [URL]"

- [ ] **Supabase** - Data backup
  - Manual step: "Please export the Supabase data manually in the dashboard (table editor > export CSV for each table)"
  - Reason: RLS policies block API access with anon key
  - Alternative: User provides service_role key for automated export
  - Save to: <venture archive folder>/supabase-backup/

- [ ] **PostHog** - Full project archive, then optional deletion
  - Ask: "Shall I archive the PostHog project completely (events, sessions, insights and dashboards as JSON plus PNG/PDF)?"
  - Follow posthog-archive.md in this skill folder (proven 1:1 procedure)
  - Run: `python3 <skill-dir>/scripts/posthog-export.py <project_id> "<export_dir>" <date_from>`
  - Requires POSTHOG_API_KEY with `export:write` scope (user must add manually)
  - Save to: <venture archive folder>/posthog-export/
  - Visually verify PNGs show FULL time range (not "Last 7/30 days")
  - Deletion of the PostHog project ONLY after explicit user confirmation

- [ ] **GTM** - Deactivate container if needed
  - Ask: "Shall the GTM container be deactivated?"

- [ ] **Domain** - Check renewal status
  - Ask: "Should the domain be kept or allowed to lapse?"

### Phase 4: Cleanup

- [ ] **Todos** - Mark related todos as done
  - Ask: "Shall I mark open todos as done?"

- [ ] **Archive Folder** - Ensure all assets are in the right place
  - Check: <venture archive folder>/ exists and has all exports

## Important Rules

- **Always ask before each step** - never just execute
- **Consistent wiki language** - keep all wiki content in one language
- **Strategic risks, not operational** - Recommendation risks should be about the venture/market, not about "don't forget to turn off ads"
- **Correct phase** - Check if venture was Concept or Prototype before writing Recommendation
- **Data-driven** - Every claim backed by actual numbers from dashboard/ads
- **Assets in the archive folder** - All exports, PDFs, backups go to the venture archive folder, never to git repo
- **Classify the failure type** — during the learnings step, categorise the kill against the four failure types (no-need / happy failure / following management / epic fail; Failbook, VNTR) and record under which changed conditions the idea would become interesting again. Failures are not final; some later turn into successes.
- **Never delete** - Deactivate/disable/pause, but never delete services or data
  - Exception: PostHog project MAY be deleted after full archive (posthog-archive.md) + explicit user confirmation
- **Pull live data** - Always check admin dashboard and Meta API for current numbers, don't rely on recollection alone
