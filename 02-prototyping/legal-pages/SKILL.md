---
name: legal-pages
description: Use when creating or updating legal pages for a website — privacy policy, legal notice/imprint, terms and conditions, cookie notice. Generates GDPR-compliant legal pages for EU-based projects with automatic third-party tool detection.
model: opus
effort: high
---

# Legal Pages — EU Legal Page Generator

This skill generates or updates GDPR-compliant legal pages for web projects: privacy policy,
legal notice (imprint), terms and conditions, and a cookie notice. It scans the codebase for
third-party tools, gathers project-specific variables, and creates or updates legal pages
matching the project's existing patterns.

No arguments needed. Just run `/legal-pages` and the skill handles everything.

**Create or update:** if legal pages already exist, the skill updates them to reflect the current
tool stack and project state (new tools added, old references removed, dates updated). It does
NOT ask whether to create or update — it always scans and produces the correct, current version
automatically.

**Difference from `/legal-audit`:**
- `/legal-audit` **audits** an existing website for legal compliance issues and flags violations
- `/legal-pages` **generates** the legal pages from scratch (or regenerates them) using
  standardised templates

**Important:** this skill generates legal text based on templates, not legal advice. Always
recommend professional legal review for final sign-off.

**Jurisdiction scope:** the templates are built on EU-level law. GDPR applies directly and
identically across the EU. The e-commerce, consumer rights and ePrivacy rules come from
directives that each member state implements differently — the generated pages therefore need a
national check before go-live. Ask the user which country the company is established in and
record it as `country`.

---

## Step 0: Gather project info

Read `CLAUDE.md` and `README.md` to determine:

| Variable | Source | Example |
|---|---|---|
| `brandName` | CLAUDE.md | "ExampleBrand", "ExampleApp" |
| `contactEmail` | CLAUDE.md | "hello@example.com" |
| `websiteUrl` | CLAUDE.md | "https://example.com" |
| `country` | Ask user | Ireland, Germany, Spain |
| `contentLanguage` | Project locale | en, de, fr |
| `hasHealthData` | Ask user if unclear | true/false |
| `hasPaidFeatures` | Ask user if unclear | true/false |

### Company data (fill once per company)

Fill in the company data once (from CLAUDE.md or ask the user):

```
Legal name:              {{companyLegalName}}
Company register number: {{companyRegisterNr}}
VAT identification no.:  {{vatId}}
Address:                 {{companyAddress}}
Registry court:          {{commercialCourt}}
Managing director:       {{managingDirector}}
Supervisory authority:   {{supervisoryAuthority}}
Governing law:           {{governingLaw}}
Jurisdiction:            {{jurisdiction}}
```

If `brandName`, `contactEmail`, `websiteUrl` or `country` cannot be determined from CLAUDE.md,
ask the user before proceeding.

---

## Step 1: Scan for integrated tools

Search the codebase for third-party tools and services. Use Grep to detect each tool by its
search patterns:

| Tool | Search patterns |
|---|---|
| Google Analytics | `gtag`, `GA_MEASUREMENT_ID` |
| Google Tag Manager | `GTM-`, `googletagmanager` |
| Google Ads | `google_ads`, `AW-` |
| PostHog | `posthog`, `POSTHOG_` |
| Hotjar | `hotjar`, `HOTJAR_` |
| Supabase | `supabase`, `SUPABASE_` |
| Stripe | `stripe`, `STRIPE_` |
| Brevo | `brevo`, `sendinblue` |
| Vercel | `vercel` |
| Netlify | `netlify` |
| Cloudflare | `cloudflare`, `turnstile` |
| Make | `make.com`, `integromat` |

Search in all source files, `.env*` files, and config files (`vite.config.*`, `package.json`,
etc.).

**MUST confirm with user before proceeding:**

```
Detected tools:
- Supabase (auth + DB)
- PostHog (analytics)
- Stripe (payments)
- Vercel (hosting)

Are these correct? Anything missing or wrong?
```

Wait for user confirmation. Do NOT generate pages until the tool list is confirmed.

---

## Step 2: Check existing project patterns

Before generating pages, scan the project for:

### Component patterns
- Does a `LegalPageWrapper` component exist? Search for `LegalPageWrapper` in the codebase.
- What layout components are used? (`PageWrapper`, `Container`, `Layout`, etc.)
- What heading and text styles does the project use?

### Routing
- Which router is used? (React Router, TanStack Router, etc.)
- Where are routes defined? (`App.tsx`, `router.tsx`, `routes/` directory)
- Are existing routes lazy-loaded?

### Design system
- Tailwind classes used for content pages
- Existing page structure (headers, spacing, max-width)
- Footer component location and link patterns

### Existing legal pages
- Do any legal pages already exist? Check for `/privacy`, `/legal-notice`, `/imprint`, `/terms`,
  `/legal`, and localised equivalents
- If they exist, note their structure so the new pages match

---

## Step 3: Generate pages

Reference `legal-templates.md` (in this skill directory) for all legal text content. Replace
template variables (`{{brandName}}`, `{{contactEmail}}`, etc.) with the values from Step 0.
Include only sections relevant to the detected tools from Step 1. For each detected tool, fill the
general templates (Sections 1.5 and 1.7 to 1.10) with the provider's legal entity, address,
purpose and transfer mechanism from the provider's own privacy notice, and flag these details
for the user to verify.

### 3a: Privacy policy (`/privacy`)

Generate with these sections:
1. Controller (company data)
2. Overview of processing activities
3. Legal bases (Art. 6 GDPR bases used)
4. Security measures (Art. 32 GDPR)
5. Transfers to third countries (per detected tool)
6. Cookies and tracking (per detected tool, with name/purpose/duration/provider)
7. Hosting (Vercel/Netlify/Cloudflare — whichever is detected)
8. Web analytics (Google Analytics/PostHog/Hotjar — whichever is detected)
9. Payment providers (Stripe — if detected)
10. Email delivery (Brevo — if detected)
11. Data subject rights (Art. 15-21 GDPR — always included)
12. Right to lodge a complaint with the supervisory authority (always included)

Conditional sections:
- Include the health data section (Art. 9 GDPR) only if `hasHealthData === true`
- Include the payment/Stripe section only if Stripe is detected
- Include the email/Brevo section only if Brevo is detected
- Include only the analytics tools that were actually detected

### 3b: Legal notice (`/legal-notice`)

Generate with these sections:
1. Provider information under Art. 5 of Directive 2000/31/EC, as implemented in `country`
   (company data, register number, VAT ID, registry court, managing director)
2. Contact (contactEmail, websiteUrl)
3. Online dispute resolution (link to the ODR platform — always included)
4. Liability for content
5. Liability for links

Flag to the user that several member states require additional disclosures here (for example
media-law information for editorial content, or chamber and professional-body details for
regulated professions).

### 3c: Terms and conditions (`/terms`)

Generate with these sections:
1. Scope
2. Contracting party (company data)
3. Subject matter (adapted to brandName)
4. Registration and user account (if the app has auth)
5. Prices and payment (only if `hasPaidFeatures === true`)
6. Right of withdrawal (Directive 2011/83/EU, only if `hasPaidFeatures === true`)
7. Warranty and liability
8. Data protection (reference to the privacy policy)
9. Final provisions (`governingLaw`, `jurisdiction`, consumer carve-out)

If `hasPaidFeatures === false`, omit sections 5 and 6 and adapt the terms to a free-service
context.

### 3d: Cookie notice component

Generate a cookie banner component:
- Categories: essential (always on), statistics (opt-in), marketing (opt-in)
- "Accept all" and "Essential only" buttons with equal prominence
- Expandable detail view with individual toggles per category
- Stores consent in localStorage
- Footer link "Cookie settings" to reopen the banner
- Blocks non-essential scripts until consent is given
- Match the project's existing Tailwind styles

---

## Step 4: Add routing

Add lazy-loaded routes for all legal pages. Example for React Router:

```tsx
const Privacy = lazy(() => import('./pages/Privacy'));
const LegalNotice = lazy(() => import('./pages/LegalNotice'));
const Terms = lazy(() => import('./pages/Terms'));
```

Routes to add:
- `/privacy` → privacy policy
- `/legal-notice` → legal notice
- `/terms` → terms and conditions

If the project is localised, use the route names that match its locale conventions and keep them
consistent with the rest of the app.

The cookie notice is a component, not a route — it renders globally (typically in `App.tsx` or
the root layout).

Follow the project's existing routing pattern. If routes use a config array, add to the config.
If they use JSX routes, add JSX routes. Match the existing pattern exactly.

---

## Step 5: Add footer links

Add links to the footer component (or create a minimal footer if none exists):

Required footer links:
- Privacy → `/privacy`
- Legal notice → `/legal-notice`
- Terms → `/terms`
- Cookie settings → reopens the cookie banner

Use the same link style and layout pattern as existing footer links. If the footer already has
legal links, update them to point to the new pages.

---

## Layout rules

### If `LegalPageWrapper` exists:
Use it. Wrap all legal page content in `<LegalPageWrapper>`. Do not create a new wrapper.

### If no `LegalPageWrapper` exists:
Use a minimal centred layout matching the project's existing content pages:

```tsx
<div className="mx-auto max-w-3xl px-4 py-16">
  <h1 className="mb-8 text-3xl font-bold">Page Title</h1>
  {/* content */}
</div>
```

Adapt Tailwind classes to match the project's existing spacing, max-width and typography
patterns.

### Text structure for all legal pages:
- `<h1>` for the page title
- `<h2>` for main sections
- `<h3>` for subsections
- `<p>` for body text
- `<ul>` / `<li>` for lists
- Anchor IDs on `<h2>` elements for deep linking (e.g. `id="cookies"`)
- Write the legal text in the language your users contract in (`contentLanguage`); if the service
  is offered in several languages, generate a version per language
- No Markdown rendering — use semantic HTML/JSX directly

---

## Rules

- **EU law baseline** — reference GDPR (Regulation 2016/679), the ePrivacy Directive
  (2002/58/EC), the E-Commerce Directive (2000/31/EC) and the Consumer Rights Directive
  (2011/83/EU). Never mix in one member state's national statutes as if they applied EU-wide.
- **Flag the national gap** — GDPR references are safe everywhere; directive-based sections must
  be checked against the implementing national law in `country`. Say this explicitly in the
  handover.
- **Always scan tools first** (Step 1) — never generate a privacy policy without knowing which
  tools are integrated.
- **Always confirm tools with the user** — do not assume. Show the detected list and ask for
  confirmation.
- **Ask when unsure** — if `country`, `hasHealthData` or `hasPaidFeatures` is ambiguous, ask.
- **Match project patterns** — use existing components, router and styles. Never introduce new
  dependencies.
- **Code in English** — variable names and component names in English, regardless of the language
  of the legal text.
- **Recommend legal review** — always end with: "These pages are based on templates and do not
  replace legal advice. Please have them reviewed by a lawyer in your jurisdiction before going
  live."
- **No invented legal text** — only use text from `legal-templates.md`. Provider-specific facts
  come from the provider's own documentation and must be flagged for verification. Never make up
  legal clauses.
- **Include only detected tools** — do not include boilerplate sections for tools that are not in
  the project.
- **One file per page** — `Privacy.tsx`, `LegalNotice.tsx`, `Terms.tsx`, `CookieBanner.tsx` (or
  matching the project's file naming convention).
