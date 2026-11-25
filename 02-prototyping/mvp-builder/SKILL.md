---
name: mvp-builder
description: Use when deciding how to validate a venture idea with the least buildable thing — choosing between fake door, concierge, Wizard-of-Oz, no-code, or a coded MVP, or scoping what NOT to build yet. Triggers - "MVP", "validation experiment", "fake door", "what is the fastest way to test this", "what do we build first". NOT for scaffolding a new codebase (use venture-setup), writing/designing landing pages (use your frontend design and copywriting tools), or planning ad experiments (use growth-lab).
model: sonnet
effort: medium
---

# MVP Builder

Pick the cheapest experiment that answers the riskiest open question. Speed is a feature; building is the last resort, not the first.

## Core Rule

Every feature, page, and line of code must map to a hypothesis. If you cannot state what you will learn from building it, do not build it yet.

## The Speed Hierarchy

Always start at level 1 and justify each step down:

1. **No build** — conversations, mockups, manual processes (see customer-discovery)
2. **Landing page** — waitlist, fake door, signup form (multi-pillar fake-door pattern)
3. **No-code** — Typeform, Tally, Airtable, Zapier
4. **Coded MVP** — smallest functional version on the project boilerplate

## Choosing the Experiment

| Experiment | Validates | Don't use when |
|---|---|---|
| Fake door (button → waitlist) | Demand for a feature/product | B2B pilots where trust is the product — a fake door can burn the relationship |
| Concierge (deliver outcome by hand) | People want the outcome | Outcome requires regulated expertise (medical advice → legal-model-decoder first) |
| Wizard of Oz (UI real, backend manual) | UX + value prop | Response-time expectations you can't fake manually |

**Evidenz-Leiter** (Design A Better Business, van der Pijl et al.): opinions < interviews < behavioural data < **payments**. Every experiment should move the hypothesis up at least one rung; where possible, bring in paying customers as early as possible — without a revenue source even a strong product dies (Failbook, VNTR).

**Do not get attached to your own prototype** (Failbook, VNTR): the prototype is a disposable measuring instrument, not a baby. If the experiment refutes the hypothesis, the prototype gets buried — you do not move the goalposts.

## Stack (non-negotiable)

Use the project boilerplate: Vite 7 + React 19 + Tailwind v4 + shadcn + Supabase (Edge Functions for all business logic), deployed on Netlify. Do NOT introduce Next.js, Vercel, or new services for an MVP — the boilerplate already covers auth, DB, tracking, and legal pages. Scaffold via venture-setup.

Even for MVPs, the security rules hold: no secrets in code, no direct DB writes from frontend, `service_role` only in Edge Functions.

## Edge Cases That Bite

- **Email collection = GDPR scope.** Any fake door or waitlist that collects emails needs Datenschutz + legal notice (legal-pages) and consent handling (cookie-consent-setup) BEFORE the first ad click lands.
- **Health ventures:** no efficacy claims on test landing pages without health-claims-audit. A fake door promising "reduces symptoms" is a legal risk, not a growth hack.
- **PII products** (anything handling sensitive personal data): synthetic data only in demos, screenshots, and seeded DBs.
- **Paid traffic on a fake door:** define the kill/scale threshold in writing before spending (growth-lab logs the experiment).

## Definition of Done

- Happy path works; one Playwright test covers it (e2e-tests)
- Professional enough to be taken seriously
- Captures signups/emails/feedback
- Shareable via URL, shipped this week
- pre-deploy checklist passed before the URL goes into an ad

## Prioritization

ICE score (Impact × Confidence × Ease, each 1–10) per candidate feature; build the top item only. Ask "if the product could do ONE thing, what would it be?" — build that, ship, re-ask.
