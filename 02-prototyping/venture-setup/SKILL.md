---
name: venture-setup
description: Interactive checklist for setting up a new project — scaffolding, DB, tracking, legal, SEO, tests. Orchestrates all technical skills in the right order. Run /venture-setup when starting a new venture's codebase.
model: sonnet
effort: low
---

# Venture Setup — Technical Project Checklist

Interactive step-by-step setup for a new project. Asks before each phase, skips what's already done, runs the right skill at each step.

## How It Works

1. Ask which venture and confirm the working directory
2. Walk through each phase in order
3. At each phase: check if it's already done, ask if the user wants to run it, invoke the skill
4. Track progress with TodoWrite tasks
5. At the end: summary of what was set up and what's still open

## Phase Checklist

Run phases in this order. Each phase lists the skill to invoke and what it produces.

### Phase 0: Scaffolding
**Default:** Use your boilerplate, e.g. (Vite 7 / React 19 / Supabase / Tailwind v4 / shadcn / Netlify).
**Check:** Does `package.json` exist?
**If not:** Clone from boilerplate repo, run `npm install`, set up `.env` from `.env.example`.
**If yes:** Skip — project already scaffolded.
**Reference:** See your boilerplate docs for details (Edge Function pattern, security headers, folder structure).

### Phase 1: Product Marketing Context
**Skill:** `/product-marketing-context`
**Check:** Does `.agents/product-marketing-context.md` exist?
**Creates:** Central context doc that all marketing skills reference (positioning, personas, competitive landscape, brand voice).
**Why first:** Every subsequent skill (brand, copy, ads, SEO) reads this file.

### Phase 2: Brand Identity _(skippable)_
**Skill:** `/brand-identity`
**Check:** Do design tokens / brand colors exist in `tailwind.config.ts` or `src/lib/design-tokens`?
**Creates:** Color palette, typography, brand personality, visual direction.
**Depends on:** Phase 1 (product-marketing-context)
**Skip if:** User designs in Claude Design (claude.ai artifacts) or Figma instead. Ask: "Brand in Claude Code or external (Claude Design / Figma)?" If external, skip and move on.

### Phase 3: Frontend Design _(skippable)_
**Skill:** any landing-page or frontend design skill you use
**Check:** Does a landing page exist at `src/pages/Index.tsx`?
**Creates:** Landing page with hero, problem, solution, pricing, CTA, FAQ, footer.
**Depends on:** Phase 2 (brand identity for colors/fonts)
**Skip if:** User builds the LP in Claude Design or Figma and pastes/exports the code manually. Ask: "Build the LP here, or have you already designed it externally?" If external, skip.

### Phase 4: Database Setup
**Skill:** `/db-setup`
**Check:** Do `supabase/migrations/*sessions*` and `src/hooks/useSession.ts` exist?
**Creates:** user_sessions + user_events tables, Edge Functions (track-session, track-event), frontend hooks (useSession, useTrackEvent, sessionId), tracking.ts.
**Important:** This skill now also defines funnel events and integrates them in components (Steps 8-9 in db-setup). Events fire without consent (first-party data). Test mode is auto-disabled (`import.meta.env.MODE === 'test'`).
**Depends on:** Phase 3 (needs components to attach events to) — but if Phase 3 was skipped, run after LP code is in place.

### Phase 5: Cookie Consent
**Skill:** `/cookie-consent-setup`
**Check:** Does `src/components/CookieConsent.tsx` exist?
**Creates:** GDPR-compliant cookie banner, Consent Mode v2 defaults, GTM integration.
**Depends on:** Phase 4 (consent gates third-party tracking, not Supabase events)

### Phase 6: GTM + Analytics
**Skill:** `/setup-gtm`
**Check:** Is `VITE_GTM_ID` in `.env` and GTM script in `index.html`?
**Creates:** GTM container config with GA4, Meta Pixel, PostHog, Consent Mode v2, custom events matching the Supabase event names from Phase 4.
**Then run:** `/analytics-tracking` for UTM conventions and conversion tracking plan.
**Important:** GTM ID must come from env var (`%VITE_GTM_ID%`), NEVER hardcoded. This prevents E2E tests from polluting analytics.
**Depends on:** Phase 5 (consent must be set up before GTM fires)

### Phase 7: Legal Pages
**Skill:** `/legal-pages`
**Check:** Do `src/pages/Datenschutz.tsx`, `src/pages/legal notice.tsx`, `src/pages/AGB.tsx` exist?
**Creates:** local GDPR-compliant legal pages with auto-detected third-party tools.
**Then run:** `/legal-audit` to verify compliance.
**Depends on:** Phase 6 (needs to know which tracking tools are used for Datenschutz page)

### Phase 8: SEO Basics
**Skill:** `/seo`
**Check:** Does `index.html` have meta title/description? Does `public/sitemap.xml` exist?
**Creates:** Meta tags, OG tags, sitemap, robots.txt, structured data, canonical URLs.
**Then run:** `/social-sharing` for OG images and favicons.
**Depends on:** Phase 7 (legal pages need to be indexed too)

### Phase 9: Admin Dashboard
**Skill:** `/admin-dashboard`
**Check:** Do `src/pages/AdminDashboard.tsx` and `supabase/functions/dashboard-data/` exist?
**Creates:** Login page at `/admin`, KPI dashboard at `/admin/dashboard`, Edge Function for data aggregation, auth guard.
**Important:** Dashboard filters production only + the target market only. Kill-switch ampel with configurable targets. Admin email via `VITE_ADMIN_EMAIL` env var + Supabase secret.
**Depends on:** Phase 4 (needs DB tables to query)

### Phase 10: E2E Tests
**Skill:** `/e2e-tests`
**Check:** Does `playwright.config.ts` exist and are there tests in `tests/e2e/`?
**Creates:** Playwright infrastructure + tests for the landing page and main user flow (LP to lead/signup).
**Important:** Tests run in `--mode test` which auto-disables all tracking (Supabase, PostHog, GTM). Verify `.env.test` has NO `VITE_GTM_ID`.
**Depends on:** Phase 8 (test the final state of the site)

### Phase 11: Pre-Deploy Check
**Skill:** `/pre-deploy`
**Check:** N/A (always run before first deploy)
**Verifies:** TypeScript builds, no secrets in code, RLS policies active, env vars set, security scan clean.
**Depends on:** All previous phases

## Quick Reference Card

```
/venture-setup        Full interactive walkthrough (this skill)

Individual phases:
/product-marketing-context   Phase 1 — Positioning + personas
/brand-identity              Phase 2 — Colors, fonts, personality (skippable)
(your frontend design skill)  Phase 3 — Landing page (skippable)
/db-setup                    Phase 4 — Supabase + tracking + events
/cookie-consent-setup        Phase 5 — GDPR cookie banner
/setup-gtm                   Phase 6a — GTM container
/analytics-tracking          Phase 6b — Event plan + UTMs
/legal-pages                 Phase 7a — Datenschutz, legal notice, AGB
/legal-audit                 Phase 7b — Compliance check
/seo                         Phase 8a — Meta, sitemap, structured data
/social-sharing              Phase 8b — OG images, favicon
/admin-dashboard             Phase 9 — Admin KPI dashboard
/e2e-tests                   Phase 10 — Playwright tests
/pre-deploy                  Phase 11 — Final safety check
```

## Rules

- **Ask before each phase.** Never auto-run a phase without confirmation.
- **Check first.** If a phase is already done (files exist), say so and ask if the user wants to re-run or skip.
- **One phase at a time.** Complete each phase before moving to the next.
- **Track progress.** Use TodoWrite to create a task per phase so the user can see progress.
- **Skip gracefully.** If the user says "skip", move to the next phase. Don't nag.
- **Boilerplate is default.** Don't ask "boilerplate or fresh?" — always use the boilerplate unless the user explicitly says otherwise.
- **Respect external design.** If the user designs in Claude Design or Figma, skip Phase 2+3 without judgment. Just make sure the code is in the repo before Phase 4.
- **Project journal.** At the end, offer to add an entry to the project journal documenting what was set up.
- **CHANGELOG.** Don't add setup steps to CHANGELOG (that's for user-facing changes only).
