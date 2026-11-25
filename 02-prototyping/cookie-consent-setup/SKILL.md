---
name: cookie-consent-setup
description: End-to-end cookie consent setup — GDPR-compliant banner component, Consent Mode v2, GTM integration, privacy-policy cookie section, and compliance audit. Vendor-neutral (no hardcoded company data).
model: sonnet
effort: medium
---

# Cookie Consent Setup — End-to-End

Unified skill for setting up GDPR-compliant cookie consent. Covers:
1. Cookie Banner component (UI + logic)
2. Google Consent Mode v2 (region-specific defaults)
3. GTM integration (consent-gated tags)
4. Cookie section for the privacy policy (legal text)
5. Compliance audit (verify nothing fires before consent)

No arguments needed. Just run `/cookie-consent-setup`.

**Vendor-neutral:** This skill does NOT hardcode any company data. All company/brand info is collected from the user or from `CLAUDE.md`.

---

## Step 0: Gather project info

### 0a. ASK FIRST — Consent scope (this decides how consent is stored)

**Before anything else, ask the user which consent scope they need.** This choice determines the storage mechanism used throughout the skill (Step 3a storage, Step 4b inline restore, re-open logic):

```
How should consent be shared across your surfaces?

A) SINGLE surface / single origin (default)
   Just one site, OR landing page + app on the SAME domain and path
   (e.g. example.com and example.com/app).
   → Consent stored in localStorage. Simplest. Nothing extra needed.

B) SHARED across SUBDOMAINS
   Landing page + app on different subdomains of the same domain
   (e.g. example.com + app.example.com). User consents once → applies to both.
   → Consent stored in a cookie on the PARENT domain (.example.com),
     because localStorage is per-origin and does NOT carry across subdomains.

C) SEPARATE domains
   Surfaces on entirely different domains (e.g. example.com + other-app.com).
   → No shared browser storage exists. True cross-domain consent needs a
     shared CMP iframe or consent-passing on hand-off. Flag this is complex;
     a certified CMP (e.g. Cookiebot) is genuinely easier for this case.
     Otherwise implement per-domain consent (each domain asks separately).
```

Wait for the answer. Call the result the **consent mode** (`A` / `B` / `C`).

- **Mode A** → use the default localStorage flow as written in Step 3a / Step 4b.
- **Mode B** → use the shared-subdomain cookie flow (Step 3a "Shared across subdomains" subsection + Step 4b cookie variant). Also ask for the `parentDomain`.
- **Mode C** → warn about complexity, recommend per-domain separate consent, and note a certified CMP may be the pragmatic choice.

### 0b. Gather company/brand info

Read `CLAUDE.md` and `README.md` to determine:

| Variable | Source | Example |
|---|---|---|
| `brandName` | CLAUDE.md | "ExampleBrand", "MediMatch" |
| `contactEmail` | CLAUDE.md | "hello@example.com" |
| `websiteUrl` | CLAUDE.md | "https://example.com" |
| `companyName` | Ask user | "Example Ltd" |
| `companyAddress` | Ask user | "1 Example Street, 12345 Example City" |
| `companyRegisterNr` | Ask user (optional) | "12345678" |
| `companyVatId` | Ask user (optional) | "IE1234567X" |
| `companyDirector` | Ask user (optional) | "Alex Example" |
| `parentDomain` | Ask user (**mode B only**) | ".example.com" (leading dot) |

If any required variable is missing, **ask the user** before proceeding. Do not assume or hardcode.

---

## Step 1: Scan for integrated tools

Search the codebase for third-party tools that set cookies or process personal data:

| Tool | Search patterns |
|---|---|
| Google Analytics | `gtag`, `GA_MEASUREMENT_ID` |
| Google Tag Manager | `GTM-`, `googletagmanager` |
| Google Ads | `google_ads`, `AW-` |
| PostHog | `posthog`, `POSTHOG_` |
| Hotjar | `hotjar`, `HOTJAR_` |
| Meta Pixel | `fbq`, `facebook`, `META_PIXEL` |
| Supabase | `supabase`, `SUPABASE_` |
| Stripe | `stripe`, `STRIPE_` |
| Google Fonts | `fonts.googleapis.com`, `fonts.gstatic.com` |
| YouTube embeds | `youtube.com/embed`, `youtube-nocookie.com` |
| Vercel | `vercel` |
| Netlify | `netlify` |
| Cloudflare | `cloudflare`, `turnstile` |

Search in all source files, `.env*` files, and config files.

**MUST confirm with user before proceeding:**

```
Detected tools:
- Google Tag Manager
- Google Analytics (GA4)
- PostHog (EU Cloud)
- Meta Pixel

Are these correct? Anything missing or wrong?
```

Wait for confirmation. Do NOT proceed until the tool list is confirmed.

---

## Step 2: Check existing project patterns

Before generating anything, scan the project for:

### Cookie consent
- Does a cookie consent component already exist? Search for `CookieConsent`, `CookieBanner`, `consent`, `cookie-consent`.
- If one exists: audit and fix it (skip to Step 3b audit mode).
- If none exists: create one (Step 3a).

### Component patterns
- Does a `LegalPageWrapper` or similar layout component exist?
- What heading/text styles does the project use?
- What design system (Tailwind, shadcn, etc.)?

### Routing
- Which router? (React Router, TanStack, Next.js, etc.)
- Where are routes defined?

### Existing legal pages
- Does a privacy policy page exist? (We'll add the cookie section to it.)

---

## Step 3a: Create Cookie Banner Component

Create a cookie consent banner with these requirements:

### Categories
- **Essential** (always on, not toggleable)
- **Statistics** (opt-in) — for analytics tools (GA4, PostHog with cookies, Hotjar)
- **Marketing** (opt-in) — for ad tracking (Meta Pixel, Google Ads, TikTok)

### UI Requirements
- "Accept all" and "Essential only" buttons with **equal visual prominence** (no dark patterns)
- Expandable detail view with individual toggles per category
- Each category shows: name, description, which tools are included
- Modal/overlay with backdrop, `z-index: 9999+`
- Match the project's existing design system (Tailwind classes, colors, spacing)
- Responsive: works on mobile and desktop
- Link to the privacy policy inside the banner

### WCAG Accessibility
- `role="dialog"`, `aria-modal="true"`, `aria-label="Cookie settings"`
- Focus trap inside modal when open
- Escape key = "Nur essenzielle" (reject non-essential)
- Tab navigation through all interactive elements
- Sufficient color contrast on all buttons

### Consent Storage

Store consent with version + timestamp for auditability:
```json
{
  "essential": true,
  "analytics": false,
  "marketing": false,
  "timestamp": "2026-05-19T10:30:00Z",
  "version": "1.0"
}
```

Key name: `cookie-consent` (or match existing project convention).

If the privacy policy version changes (bump `version`), show the banner again to returning visitors.

#### Mode A (single origin) — localStorage
Use `localStorage.setItem('cookie-consent', JSON.stringify(prefs))` and `localStorage.getItem('cookie-consent')`. This is the default. Nothing else needed.

#### Mode B (shared across subdomains) — parent-domain cookie
localStorage is **per-origin**, so it does NOT carry across subdomains (`example.com` and `app.example.com` have separate storage). To share one consent decision across subdomains, store it in a cookie scoped to the **parent domain** (`parentDomain`, e.g. `.example.com`) — every subdomain can then read the same cookie.

Use these helpers in BOTH repos (landing page + app), with the SAME cookie name and `parentDomain`:

```js
const CONSENT_COOKIE = 'cookie-consent';
const PARENT_DOMAIN = '.example.com'; // = parentDomain (leading dot!)

function setConsentCookie(prefs) {
  const value = encodeURIComponent(JSON.stringify(prefs));
  const maxAge = 60 * 60 * 24 * 180; // 6 months
  document.cookie =
    `${CONSENT_COOKIE}=${value}; domain=${PARENT_DOMAIN}; path=/; max-age=${maxAge}; SameSite=Lax; Secure`;
}

function getConsentCookie() {
  const m = document.cookie.match(new RegExp('(?:^|;\\s*)' + CONSENT_COOKIE + '=([^;]+)'));
  if (!m) return null;
  try { return JSON.parse(decodeURIComponent(m[1])); } catch { return null; }
}
```

On load (identical on LP and app): read the cookie, and if it exists and the `version` matches, apply the saved consent via `gtag('consent', 'update', ...)` and do NOT show the banner. If the user first accepts on the LP, the app finds the cookie on open and does not ask again.

Notes for Mode B:
- The `domain=.example.com` (leading dot) is what makes the cookie readable across all subdomains.
- `SameSite=Lax; Secure` — requires HTTPS; fine because subdomains are same-site.
- The consent cookie itself is an **essential** cookie (it stores the decision) → allowed without prior consent.
- Withdrawal: the "Cookie settings" re-open button on either surface simply overwrites the same cookie.
- **Requirement:** both surfaces must be real subdomains of the same registrable domain. Two entirely different domains = Mode C (this cookie approach will NOT work).

### Consent Logic

On **page load**:
1. Check localStorage for existing consent
2. If consent exists and version matches: apply saved preferences via `gtag('consent', 'update', ...)`
3. If no consent or version mismatch: show banner

On **user choice** (accept all / reject / custom):
1. Save preferences to localStorage (with timestamp + version)
2. Call consent update:
```typescript
window.dataLayer = window.dataLayer || [];
function gtag(...args: unknown[]) {
  window.dataLayer!.push(args);
}
gtag('consent', 'update', {
  'analytics_storage': prefs.analytics ? 'granted' : 'denied',
  'ad_storage': prefs.marketing ? 'granted' : 'denied',
  'ad_user_data': prefs.marketing ? 'granted' : 'denied',
  'ad_personalization': prefs.marketing ? 'granted' : 'denied',
});

// Fire custom event so GTM trigger fires
window.dataLayer.push({
  event: 'consent_update',
  analytics_consent: prefs.analytics,
  marketing_consent: prefs.marketing,
});
```

### Re-open mechanism
- Footer link "Cookie settings" that reopens the banner
- AND/OR a floating cookie icon button (bottom-left, small, unobtrusive) that appears after consent is given

### Script Blocking
The banner itself does NOT load/block scripts. That's handled by Consent Mode v2 + GTM (Step 4). The banner's job is to:
1. Collect user preference
2. Store it
3. Communicate it to GTM via `gtag('consent', 'update', ...)`

### Where to render
Render globally — typically in `App.tsx`, root layout, or `_app.tsx`. NOT as a route.

---

## Step 3b: Audit Existing Cookie Banner

If a cookie banner already exists, verify:

| Check | Requirement | Severity |
|---|---|---|
| Equal button prominence | "Reject" same size/colour as "Accept" | 🔴 Critical (dark pattern = GDPR violation) |
| Granular categories | Separate toggles for statistics + marketing | 🔴 Critical |
| No pre-checked boxes | Non-essential categories OFF by default | 🔴 Critical |
| Consent before tracking | No scripts fire before consent given | 🔴 Critical |
| Consent stored | localStorage with timestamp + version | 🟠 Major |
| Re-open mechanism | Footer link or floating button to change settings | 🟠 Major |
| gtag consent update | Calls `gtag('consent', 'update', ...)` correctly | 🔴 Critical |
| Event name matches GTM | `dataLayer.push({ event: 'consent_update' })` | 🔴 Critical |
| WCAG accessible | Focus trap, Escape, aria attributes | 🟡 Minor |
| Privacy link | Links to the privacy policy | 🟠 Major |

Fix all issues found. Report what was fixed.

---

## Step 4: Consent Mode v2 in `index.html`

**CRITICAL: Consent defaults MUST be set BEFORE the GTM script loads.**

Add to `<head>`, right after `<meta name="viewport">`:

### 4a: Region-specific consent defaults

```html
<!-- Consent Mode v2 — region-specific defaults (before GTM) -->
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}

// Default: grant all for non-EEA regions
gtag('consent', 'default', {
  'analytics_storage': 'granted',
  'ad_storage': 'granted',
  'ad_user_data': 'granted',
  'ad_personalization': 'granted',
  'functionality_storage': 'granted',
  'security_storage': 'granted',
});

// EEA + UK + CH: deny until the user consents (GDPR)
gtag('consent', 'default', {
  'analytics_storage': 'denied',
  'ad_storage': 'denied',
  'ad_user_data': 'denied',
  'ad_personalization': 'denied',
  'functionality_storage': 'denied',
  'region': ['AT', 'BE', 'BG', 'CY', 'CZ', 'DE', 'DK', 'EE', 'ES', 'FI',
    'FR', 'GR', 'HR', 'HU', 'IE', 'IT', 'LT', 'LU', 'LV', 'MT', 'NL',
    'PL', 'PT', 'RO', 'SE', 'SI', 'SK', 'IS', 'LI', 'NO', 'GB', 'CH'],
  'wait_for_update': 500,
});
</script>
```

### 4b: Inline consent restore (returning visitors)

Place AFTER consent defaults, BEFORE GTM script:

**Mode A (single origin) — read from localStorage:**
```html
<script>
// Restore saved consent before GTM loads (returning visitors)
try {
  var saved = localStorage.getItem('cookie-consent');
  if (saved) {
    var p = JSON.parse(saved);
    gtag('consent', 'update', {
      'analytics_storage': p.analytics ? 'granted' : 'denied',
      'ad_storage': p.marketing ? 'granted' : 'denied',
      'ad_user_data': p.marketing ? 'granted' : 'denied',
      'ad_personalization': p.marketing ? 'granted' : 'denied',
    });
  }
} catch(e) {}
</script>
```

Adapt `'cookie-consent'` key to match the project's actual localStorage key.

**Mode B (shared across subdomains) — read from the parent-domain cookie instead.** This is REQUIRED for shared consent: if the app still reads localStorage, the consent given on the LP won't apply in time before GTM loads. Add this in BOTH the LP and the app `index.html`:
```html
<script>
// Restore shared consent (parent-domain cookie) before GTM loads
try {
  var m = document.cookie.match(/(?:^|;\s*)cookie-consent=([^;]+)/);
  if (m) {
    var p = JSON.parse(decodeURIComponent(m[1]));
    gtag('consent', 'update', {
      'analytics_storage': p.analytics ? 'granted' : 'denied',
      'ad_storage': p.marketing ? 'granted' : 'denied',
      'ad_user_data': p.marketing ? 'granted' : 'denied',
      'ad_personalization': p.marketing ? 'granted' : 'denied',
    });
  }
} catch(e) {}
</script>
```

### 4c: GTM snippet (env-variable guarded)

**NEVER hardcode the GTM Container ID.** Use env variable:

```html
<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){if(!i||i.indexOf('VITE_')===0)return;w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','%VITE_GTM_ID%');</script>
```

Right after `<body>`:
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%VITE_GTM_ID%"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
```

Add to `.env` and `.env.example`:
```
VITE_GTM_ID=GTM-XXXXXXX
```

**Adapt for framework:** For Next.js, use `NEXT_PUBLIC_GTM_ID`. For other frameworks, use the appropriate env variable prefix.

**Why env variable?** Hardcoded IDs cause E2E tests and CI to pollute production analytics with fake events.

---

## Step 5: Consent per tool type (GTM settings)

After import, these consent settings MUST be configured in GTM UI (cannot be set via JSON import):

| Tool | Consent Setting in GTM |
|---|---|
| **PostHog** (with `person_profiles: 'identified_only'`) | "No additional consent required" — GDPR-safe without consent |
| **GA4** | No changes needed — built-in Consent Mode handling |
| **Meta Pixel** | "Require additional consent → `ad_storage`" |
| **Google Ads** | "Require additional consent → `ad_storage`" |
| **Hotjar / Clarity** | "Require additional consent → `analytics_storage`" |

**IMPORTANT:** Do NOT create "Consent Mode - Default" or "Consent Mode - Update" tags in GTM. Defaults are in `index.html`. Updates come from the cookie banner. A GTM tag that hardcodes `'granted'` overrides the user's choice = GDPR violation.

---

## Step 6: Cookie documentation for the privacy policy

If a privacy policy page exists, add or update the cookie section. If not, create the section content for later integration.

Reference `cookie-templates.md` (in this skill directory) for all legal text blocks. Replace `{{placeholders}}` with values from Step 0.

### Required sections:
1. **Cookies and tracking** — general explanation of cookie categories
2. **Per-tool sections** — one section per detected tool (from Step 1), each with: name, provider, purpose, data processed, legal basis, retention, opt-out link
3. **Managing cookie settings** — explain how to change consent (footer link / floating button)

### Cookie table format (for each detected tool):

```
| Cookie/tool | Provider | Purpose | Category | Storage period | Legal basis |
|---|---|---|---|---|---|
| _ga, _ga_* | Google | Web analytics | Statistics | 2 years | Art. 6(1)(a) GDPR |
| _fbp | Meta | Ad tracking | Marketing | 90 days | Art. 6(1)(a) GDPR |
```

---

## Step 7: Third-Party Script Audit

Verify that NO tracking/analytics scripts load before consent:

### Check in code:
- [ ] Google Analytics / GA4 — loads only via GTM after consent?
- [ ] Meta Pixel — loads only via GTM after consent?
- [ ] PostHog — loads via GTM (consent-free with `person_profiles: 'identified_only'`)?
- [ ] Hotjar / Clarity — loads only via GTM after consent?
- [ ] Google Fonts — loaded from Google servers? (self-host to avoid transfer without consent)
- [ ] YouTube / Vimeo embeds — use click-to-load facade?
- [ ] No direct `<script src="...">` tags for analytics tools in `index.html`
- [ ] No npm-imported analytics SDKs that auto-initialize

### Check in browser (recommend to user):
```
Test steps:
1. Open site in incognito mode
2. Open DevTools → Application → Cookies
3. Before interacting with banner: should see ZERO non-essential cookies
4. Click "Nur essenzielle" → still zero non-essential cookies
5. Reopen settings → enable statistics → appropriate analytics cookies appear
6. Reopen settings → enable Marketing → ad cookies appear
```

Fix any violations found.

---

## Step 8: SPA Pageview Tracking (if applicable)

If the project is a Single Page Application (React, Vue, Svelte), client-side route changes are invisible to GTM's "All Pages" trigger. Add a page view tracker:

### React (react-router v6+)
```tsx
const PageViewTracker = () => {
  const location = useLocation();
  useEffect(() => {
    const id = requestAnimationFrame(() => {
      window.dataLayer = window.dataLayer || [];
      window.dataLayer.push({
        event: "page_view",
        page_path: location.pathname + location.search,
        page_location: window.location.href,
        page_title: document.title,
      });
    });
    return () => cancelAnimationFrame(id);
  }, [location.pathname, location.search]);
  return null;
};
```

Place inside `<BrowserRouter>`, before `<Routes>`.

**Why `requestAnimationFrame`?** Lazy-loaded routes set `document.title` in their own `useEffect`. Without the frame delay, the tracker fires before the title is updated.

---

## Step 9: Content-Security-Policy Check

If the project has a CSP (in `_headers`, `vercel.json`, `netlify.toml`, `next.config.js`, or `<meta>` tag), verify these domains are allowed:

- `script-src`: `https://www.googletagmanager.com`, `https://connect.facebook.net`, `https://eu.i.posthog.com`
- `connect-src`: `https://www.google-analytics.com`, `https://region1.google-analytics.com`, `https://eu.i.posthog.com`
- `frame-src`: `https://www.googletagmanager.com`

Add missing domains. Otherwise tracking scripts are silently blocked.

---

## Step 10: Footer Links

Ensure the footer contains:
- **Privacy policy** → `/privacy`
- **Cookie settings** → reopens the cookie banner (onClick handler, not a route)

Use the project's existing footer link style.

---

## Step 11: Summary

```
Cookie Consent Setup Complete

✅ Cookie banner component created/audited
✅ Consent Mode v2 defaults in index.html (region-specific)
✅ Inline consent restore for returning visitors
✅ GTM snippet (env-variable guarded)
✅ Cookie section for the privacy policy
✅ Third-party script audit passed
✅ Footer links added
[SPA only:] ✅ SPA pageview tracker wired

Consent flow:
- Non-EEA visitors: all consent granted by default → full tracking
- EEA/UK/CH visitors: all consent denied → tracking only after banner acceptance
- Returning visitors: saved consent restored before GTM loads

Manual steps after GTM container import:
1. PostHog tags → "No additional consent required"
2. Meta Pixel tags → "Require additional consent → ad_storage"
3. GA4 tags → no changes needed
4. Test in GTM Preview Mode
5. Test cookie flow in incognito (see Step 7 checklist)

⚠️ Legal disclaimer: this implementation is based on technical best practices and
does not replace legal advice. Please have it reviewed by a lawyer in your
jurisdiction before going live.
```

---

## Rules

- **Ask consent scope FIRST (Step 0a)** — single origin (A), shared across subdomains (B), or separate domains (C). Mode B uses a parent-domain cookie instead of localStorage; Mode C needs a CMP or per-domain consent. Never assume — this changes the storage mechanism everywhere.
- **EU law baseline** — reference GDPR (Regulation 2016/679) and Art. 5(3) of the ePrivacy Directive 2002/58/EC. Flag that the ePrivacy consent rule is implemented differently in each member state and must be checked nationally before go-live.
- **No hardcoded company data** — all company info comes from user input or CLAUDE.md. Never assume any specific company.
- **Always scan tools first** (Step 1) — never generate cookie documentation without knowing which tools are integrated.
- **Always confirm tools with user** — show detected list and ask for confirmation.
- **Match project patterns** — use existing components, router, styles. Never introduce new dependencies.
- **German content, English code** — legal text in German, component/variable names in English.
- **No dark patterns** — reject and accept buttons must have equal visual prominence.
- **Consent before tracking** — no non-essential scripts may fire before explicit opt-in.
- **Do NOT create Consent Mode tags in GTM** — defaults in `index.html`, updates from banner.
- **Event name `consent_update`** — must match between banner and GTM trigger exactly.
- **Use env variable for GTM ID** — never hardcode in `index.html`.
- **PostHog with `person_profiles: 'identified_only'` needs no consent** — set to "No additional consent required" in GTM.
- **Include only detected tools** — no boilerplate for tools not in the project.
- **Recommend legal review** — always end with disclaimer.

## Known Pitfalls (from production incidents)

### Consent Race Condition
**Symptom:** PostHog/Meta `undefined` on live site. **Cause:** GTM Consent Mode v2 silently blocks Custom HTML tags when consent is `denied`. Combined with `wait_for_update: 500`, React hydration can't deliver consent in time. **Fix:** Inline consent restore in `index.html` (Step 4b) + correct consent settings per tool in GTM UI (Step 5).

### 0% Consent Rate
**Symptom:** GTM shows 0% consent even outside EEA. **Cause:** "Consent Mode - Default" tag inside GTM that sets all consent to `denied` globally. **Fix:** Remove any consent default/update tags from GTM. Set defaults only in `index.html`.

### Consent Update Tag Overrides User Choice
**Symptom:** Users who click "Nur essenzielle" are still fully tracked. **Cause:** A "Consent Mode - Update" tag in GTM that hardcodes `'granted'`. **Fix:** No consent tags in GTM container. Banner handles updates directly.

### Hardcoded GTM ID Pollutes Analytics
**Symptom:** Thousands of false pageviews from CI/tests. **Cause:** GTM ID hardcoded in HTML. **Fix:** Use `%VITE_GTM_ID%` with guard.

### SPA Subpages Invisible
**Symptom:** Only landing page shows in analytics. **Cause:** SPA route changes don't trigger GTM "All Pages". **Fix:** SPA pageview tracker (Step 8).
