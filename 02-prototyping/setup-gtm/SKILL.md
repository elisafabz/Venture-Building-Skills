---
name: setup-gtm
description: Set up Google Tag Manager container with GA4, Meta Pixel, PostHog, Consent Mode v2, and custom events
model: sonnet
effort: medium
---

# Setup GTM Container with GA4 + Meta Pixel + PostHog + Consent Mode v2

This skill is fully interactive — no arguments needed. Just run `/setup-gtm` and follow the prompts.

## Step 1: Collect IDs one by one

Ask the user for each ID individually. For each one, tell them where to find it if they don't have it yet.

**1. GTM Container ID**
```
Do you already have a GTM container? Give me the ID (e.g. GTM-XXXXXXX).

If not: https://tagmanager.google.com → create an account → container → web
```
Wait for the user's answer before continuing.

**2. GA4 Measurement ID**
```
GA4 Measurement ID? (e.g. G-XXXXXXX)

If not: https://analytics.google.com → admin → create property → data stream → web
```
Wait for the user's answer before continuing.

**3. Meta Pixel ID**
```
Meta Pixel ID? (the numeric ID)

If not: https://business.facebook.com → Events Manager → connect data sources → web → Meta Pixel
```
Wait for the user's answer before continuing.

**4. PostHog API Key**
```
PostHog Project API Key? (e.g. phc_xxxxx)

If not: https://eu.posthog.com → settings → project API key
```
Wait for the user's answer before continuing.

**5. Additional tools**
```
Do you want to add any other tools? (e.g. Hotjar, Clarity, TikTok Pixel, LinkedIn Insight Tag, Hubspot, etc.)

If yes: tell me which tool plus its ID or key.
If no: just say "no" and we move on.
```
Wait for the user's answer before continuing.

**6. SPA detection**
```
Is the project a single page app (SPA)?
(e.g. React, Vue, Svelte, Angular with client-side routing)

If yes: I will set up SPA-specific pageview tracking.
Falls nein: Standard-Tracking reicht.
```
Wait for the user's answer before continuing. If unsure, check for `react-router`, `vue-router`, `@angular/router`, or `svelte-routing` in `package.json`. If found, it's an SPA.

If the user wants additional tools, collect each tool name + ID. For each additional tool, create:
- A **Constant variable** for the tool's ID/key
- A **Pageview tag** (Custom HTML) that loads the tool's standard snippet, fires on All Pages, with `analytics_storage = granted` consent requirement
- For each custom event: an additional **Custom HTML tag** that sends the event to that tool (if the tool supports custom events)

Use the tool's official embed snippet. Common patterns:
- **Hotjar:** `(function(h,o,t,j,a,r){...})(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');`
- **Microsoft Clarity:** `(function(c,l,a,r,i,t,y){...})(window,document,"clarity","script","PROJECT_ID");`
- **TikTok Pixel:** `ttq.load('PIXEL_ID'); ttq.page();`
- **LinkedIn Insight Tag:** `_linkedin_partner_id = "PARTNER_ID"; ...`

---

## Step 2: Define custom events BEFORE generating anything

**STOP. Do not generate the container JSON yet.** First, ask the user two questions:

1. **"What is your conversion goal?"** — the one action that matters most (e.g. waitlist signup, purchase, booking, demo request). This becomes the primary conversion event and fires `fbq('track', 'Lead')` (or `'Purchase'`, etc.) on Meta for ad optimization.

2. **"Which 2-4 steps lead there?"** — the key steps in the user journey leading to the conversion (e.g. CTA click, survey start, add to cart). These become the custom events.

### Rules for events:
- **Maximum 5 custom events total** (including the conversion event). Less is more.
- Events should map to meaningful user intent, not UI interactions.
- Name events in `snake_case` (e.g. `cta_click`, `waitlist_signup`, `survey_start`).
- Choose the right Meta standard event for the conversion (Lead, Purchase, CompleteRegistration, etc.) — use `fbq('trackCustom', ...)` for non-standard events.

### Example event discussion:

```
Before I set up GTM, let's define your events.

1. What is your conversion goal?
   (e.g. waitlist signup, purchase, booking, demo request)

2. Which 2-4 steps lead there?
   (e.g. CTA click, survey started, product viewed)
```

Once the user confirms the events, proceed to Step 3.

---

## Step 3: Generate `gtm-container.json`

Create a file `gtm-container.json` in the project root. This is a standard GTM container export (exportFormatVersion 2) that the user imports via **GTM Admin > Import Container**.

Use placeholder values for `accountId`, `containerId`, `containerName`, `fingerprint` — they get overwritten on import.

### Variables

| Variable | Type | Value |
|----------|------|-------|
| GA4 Measurement ID | Constant | (from argument) |
| Meta Pixel ID | Constant | (from argument) |
| PostHog API Key | Constant | (from argument) |
| PostHog Host | Constant | `https://eu.i.posthog.com` |

### Triggers

Always include these base triggers:

| Trigger | Type | Details |
|---------|------|---------|
| All Pages | Page View | Standard pageview trigger |
| Consent Update | Custom Event | Event name: `consent_update` |
| SPA Page View | Custom Event | Event name: `page_view` (**SPA only**) |

The "SPA Page View" trigger is **required for SPA projects**. Without it, only the initial HTML load is tracked — client-side route changes (e.g. navigating from `/` to `/datenschutz`) are invisible to analytics.

Plus one Custom Event trigger per custom event agreed in Step 2 (event name matches the `snake_case` name).

**NOTE:** Do NOT create a "Consent Initialization" trigger or a "Consent Mode - Default" tag in the GTM container. Consent defaults are set in `index.html` before GTM loads (see Step 3). Setting defaults inside GTM causes them to override the region-specific defaults and results in 0% consent rate for non-EEA traffic.

### Tags

**Consent requirements per tool:**
- **PostHog tags:** "No additional consent required" — PostHog with `person_profiles: 'identified_only'` collects no PII and is GDPR-compliant without consent. Set to "No additional consent required" in GTM UI after import.
- **Meta Pixel tags:** Require `ad_storage = granted` — Meta sets cross-site tracking cookies. Set to "Require additional consent → ad_storage" in GTM UI after import.
- **GA4 tags:** Have built-in consent handling (Consent Mode v2). No manual consent settings needed.
- **Other tools (Hotjar, Clarity, etc.):** Require `analytics_storage = granted`.

#### Base tags (always included):

**IMPORTANT: Do NOT create a "Consent Mode - Update" tag in the GTM container.** The cookie consent banner already calls `gtag('consent', 'update', ...)` directly via dataLayer with the user's actual preferences (granted/denied per category). A GTM tag that fires on `consent_update` and hardcodes `'granted'` for all consent types would **override the user's choice** — a GDPR violation. The `consent_update` trigger is kept so other tags can react to the consent event, but no Consent Mode tag should exist in the container.

**1. GTM to Analytics (GA4 Pageview)**
- **Type:** Google Tag (`googtag`)
- **Tag ID:** the GA4 Measurement ID variable
- **Fires on:** All Pages (non-SPA) or **SPA Page View** (SPA projects)
- **Consent required:** GA4 handles this automatically (built-in Consent Mode)
- **SPA note:** Do NOT set `sendPageView: false` — the googtag config tag's automatic pageview is correct behavior. If you suppress it, GA4 receives zero pageviews (there's no separate manual pageview tag).

**2. Meta Pixel — Pageview**
- **Type:** Custom HTML
- **Fires on:** All Pages (non-SPA) or **SPA Page View** (SPA projects)
- **Consent required:** `ad_storage = granted` (Meta sets cross-site tracking cookies)
- **Code (non-SPA):** Standard Meta Pixel init + `fbq('track', 'PageView')` using the Meta Pixel ID variable
- **Code (SPA):** Must include **init guard** to prevent re-initializing the SDK on every route change:
```html
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window, document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
if(!window.__metaPixelInitialized){fbq('init', '{{Meta Pixel ID}}');window.__metaPixelInitialized=true;}
fbq('track', 'PageView');
</script>
```

**3. PostHog — Pageview**
- **Type:** Custom HTML
- **Fires on:** All Pages (non-SPA) or **SPA Page View** (SPA projects)
- **Consent required:** None — PostHog with `person_profiles: 'identified_only'` is GDPR-compliant without consent (no PII, no cross-site cookies). Set to "No additional consent required" in GTM UI.
- **Code (non-SPA):** Standard PostHog snippet using PostHog API Key and PostHog Host variables
- **Code (SPA):** Must include **init guard** + `capture_pageview: false` + manual `posthog.capture('$pageview')`:
```html
<script>
!function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host.replace(".i.posthog.com","-assets.i.posthog.com")+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="init capture register register_once register_for_session unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group identify setPersonProperties setPersonPropertiesForFlags resetPersonPropertiesForFlags setGroupPropertiesForFlags resetGroupPropertiesForFlags resetGroups onFeatureFlags addFeatureFlagsHandler onSessionId getSurveys getActiveMatchingSurveys renderSurvey canRenderSurvey getNextSurveyStep".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
if(!window.__posthogInitialized){posthog.init('{{PostHog API Key}}', { api_host: '{{PostHog Host}}', capture_pageview: false });window.__posthogInitialized=true;}
posthog.capture('$pageview');
</script>
```
**Why init guards?** In an SPA, pageview tags fire on every route change. Without guards, the SDK script gets loaded and `init()` is called multiple times, causing duplicate events and memory leaks. The `if(f.fbq)return` guard in Meta's snippet prevents script reload but NOT double `fbq('init')`. PostHog's `__SV` guard prevents script reload but NOT double `posthog.init()`.

#### Custom event tags (from Step 2):

For each custom event, create **3 tags** (one per platform):

**GA4_{event_name}**
- **Type:** GA4 Event (`gaawe`)
- **Event name:** the event name
- **Measurement ID:** reference to "GTM to Analytics" tag
- **Fires on:** the event's Custom Event trigger
- **Consent required:** GA4 handles this automatically (built-in Consent Mode)

**Meta_{event_name}**
- **Type:** Custom HTML
- **Fires on:** the event's Custom Event trigger
- **Consent required:** `ad_storage = granted` (Meta sets cross-site tracking cookies)
- **Code:** For the primary conversion event, use the appropriate standard Meta event (`fbq('track', 'Lead')`, `fbq('track', 'Purchase')`, etc.). For other events, use `fbq('trackCustom', 'event_name')`.

**PostHog_{event_name}**
- **Type:** Custom HTML
- **Fires on:** the event's Custom Event trigger
- **Consent required:** None — set to "No additional consent required" in GTM UI
- **Code:** `<script>if(typeof posthog!=='undefined'){posthog.capture('event_name');}</script>`

---

## Step 4: Wire up dataLayer in the codebase

Find the project's event tracking hook or utility (e.g. `useTrackEvent`, `trackEvent`, or similar). Add a `window.dataLayer.push({ event: eventType })` call so GTM picks up events fired from the app.

If no tracking utility exists, create a minimal one that pushes to dataLayer.

Make sure each custom event from Step 2 is actually fired somewhere in the codebase. If an event doesn't have a corresponding call yet, add it in the appropriate component.

---

## Step 5: SPA Pageview Tracking (SPA projects only)

**Skip this step for non-SPA projects.** For SPAs (React, Vue, Svelte, Angular), client-side route changes are invisible to GTM's "All Pages" trigger. You must push a `page_view` event to the dataLayer on every route change.

### React (react-router v6+)

Add a `PageViewTracker` component inside `<BrowserRouter>`:

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

// In the App component:
<BrowserRouter>
  <PageViewTracker />
  <Routes>...</Routes>
</BrowserRouter>
```

### Why `requestAnimationFrame`?

Lazy-loaded route components (e.g. `React.lazy()`) set `document.title` in their own `useEffect`. Without `requestAnimationFrame`, the tracker fires **before** the target page's title is set, sending the wrong title to analytics.

### Per-page document.title

Each page component MUST set its own `document.title` via `useEffect`:

```tsx
useEffect(() => { document.title = "Page Name — Brand"; }, []);
```

**Including the index/home page** — otherwise, navigating back from a subpage leaves the old title in the tab and sends wrong data to analytics.

### Vue (vue-router)

```ts
router.afterEach((to) => {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: "page_view",
    page_path: to.fullPath,
    page_location: window.location.origin + to.fullPath,
    page_title: document.title,
  });
});
```

### Svelte (SvelteKit)

```ts
// In +layout.ts or +layout.svelte
afterNavigate(({ to }) => {
  window.dataLayer = window.dataLayer || [];
  window.dataLayer.push({
    event: "page_view",
    page_path: to?.url.pathname,
    page_location: to?.url.href,
    page_title: document.title,
  });
});
```

---

## Step 6: Add Consent Defaults + GTM snippet to `index.html`

**CRITICAL: Consent defaults MUST be set BEFORE the GTM script loads.** This is the Google-recommended approach and prevents the 0% consent rate issue. Do NOT set consent defaults inside the GTM container — that overrides region-specific rules.

**In `<head>`** — add right after `<meta name="viewport">`:

First, the region-specific consent defaults:
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

// EEA + UK + CH: deny until user consents (GDPR/GDPR)
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

Then, immediately after, the GTM container script. **CRITICAL: NEVER hardcode the GTM ID directly. Always use the `VITE_GTM_ID` environment variable** so GTM doesn't load in test/CI environments (see Pitfall: Hardcoded GTM ID below):
```html
<!-- Google Tag Manager (loads only when VITE_GTM_ID is set) -->
<script>(function(w,d,s,l,i){if(!i||i.indexOf('VITE_')===0)return;w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','%VITE_GTM_ID%');</script>
<!-- End Google Tag Manager -->
```

**Right after `<body>`** — add the noscript fallback:
```html
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=%VITE_GTM_ID%"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->
```

**Also add to `.env`:**
```
VITE_GTM_ID=GTM-XXXXXXX
```
Replace `GTM-XXXXXXX` with the actual GTM Container ID.

**Also add to `.env.example`:**
```
# Google Tag Manager (leave empty to disable tracking in dev/test)
VITE_GTM_ID=GTM-XXXXXXXX
```

**Why this order matters:** Google's Consent Mode reads defaults synchronously before any tags fire. If defaults are set inside a GTM tag (even a Consent Initialization tag), they can override the region-specific `region` parameter with a global `denied`, causing 0% consent rate for all non-EEA traffic.

---

## Step 7: Cookie Consent Banner Integration

After generating the GTM container and wiring up dataLayer, check if the project already has a cookie consent banner.

### If a cookie consent banner EXISTS:

Search the codebase for cookie consent components (e.g. `CookieConsent`, `CookieBanner`, `consent`). Verify:

1. **The consent update event name matches the GTM trigger exactly.** The GTM container expects the event `consent_update`. If the banner fires a different event name (e.g. `cookie_consent_update`, `consent_granted`, etc.), fix it to match.

2. **The `gtag('consent', 'update', ...)` call works reliably.** Do NOT rely on `window.gtag` existing — instead push directly to dataLayer:
```typescript
// CORRECT — always works with GTM
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

// ALSO fire the custom event so the GTM "Consent Update" trigger fires
window.dataLayer.push({
  event: 'consent_update',
  analytics_consent: prefs.analytics,
  marketing_consent: prefs.marketing,
});
```

3. **A floating re-open button exists** so users can change their cookie preferences after the initial choice. If not, add one — a small icon button (e.g. cookie icon) fixed to bottom-left with `z-index` below the banner but above page content.

### If NO cookie consent banner exists:

Create one. Requirements:
- Three choices: "Accept all", "Necessary only", "Settings" (with toggles for analytics/marketing)
- On accept/reject: store preferences in `localStorage` (including `timestamp` and `version` — see below), call `gtag('consent', 'update', ...)` via dataLayer push, and fire `window.dataLayer.push({ event: 'consent_update' })`
- On page load: check localStorage — if consent already given, call `gtag('consent', 'update', ...)` with saved preferences
- **Consent record format (recommended):** Store a timestamp and privacy policy version alongside preferences so the consent can be audited later (EDPB recommendation). If the privacy policy version changes, show the banner again:
  ```json
  { "analytics": true, "marketing": false, "timestamp": "2026-04-13T14:32:00Z", "version": "1.0" }
  ```
- Show a floating cookie icon button (bottom-left) after consent is given so users can reopen settings
- Modal backdrop with `z-index: 9999+`
- Must use `<Link>` to privacy policy page
- WCAG: focus management, Escape key closes with "reject all", `aria-modal`, `role="dialog"`

**CRITICAL:** The event name in `dataLayer.push({ event: '...' })` MUST be exactly `consent_update` — this is what the GTM container trigger listens for. A mismatch here means GTM never fires the consent update tag, resulting in 0% consent rate in GTM.

---

## Step 8: Summary

After completing, tell the user:

```
Done! Here's what was set up:

✅ Region-specific Consent Mode v2 defaults in index.html (before GTM)
✅ GTM snippet added to index.html
✅ dataLayer.push() wired into event tracking
✅ Cookie consent banner integrated with Consent Mode v2
✅ gtm-container.json generated with:
   - GA4 pageview + [N] custom events
   - Meta Pixel pageview + [N] custom events
   - PostHog pageview + [N] custom events (EU cloud)
   [SPA only:]
   - SPA Page View trigger for client-side route changes
   - Init guards on Meta Pixel + PostHog (prevent double SDK init)
   - PageViewTracker component wired into router

How consent works:
- Non-EEA visitors: all consent granted by default → full tracking immediately
- EEA/UK/CH visitors: all consent denied → tracking only after cookie banner acceptance

Next steps:
1. Go to https://tagmanager.google.com → your container
2. Admin → Import Container → upload gtm-container.json
3. Choose "Existing workspace" → Merge → Overwrite conflicting tags
4. IMPORTANT: Make sure there is NO "Consent Mode - Default" tag in the container
   (defaults are handled in index.html — a GTM default tag would override them)
5. IMPORTANT: Set consent requirements per tool type (GTM's import format does not support consentSettings — this must be done manually after import):
   - **PostHog tags** (Pageview + all custom events): Tag → Advanced Settings → Consent Settings → "No additional consent required"
   - **Meta Pixel tags** (Pageview + all custom events): Tag → Advanced Settings → Consent Settings → "Require additional consent for tag to fire" → add "ad_storage"
   - **GA4 tags**: No changes needed (built-in Consent Mode handling)
6. Review the imported tags, then click "Submit" → "Publish"
7. Test: check GTM Preview Mode — non-EEA traffic should show consent as granted
```

---

## Rules

- PostHog host is ALWAYS `https://eu.i.posthog.com` (EU cloud) unless the user's snippet explicitly uses a different host (e.g. `https://us.i.posthog.com`)
- **PostHog tags require NO consent** when using `person_profiles: 'identified_only'` (GDPR-safe, no PII, no cross-site cookies). Set to "No additional consent required" in GTM UI.
- **Meta Pixel tags require `ad_storage = granted`** (cross-site tracking cookies). Set to "Require additional consent → ad_storage" in GTM UI.
- **GA4 tags** have built-in Consent Mode handling — no manual consent settings needed.
- **Consent defaults MUST be set in `index.html` before the GTM script, NOT inside GTM** — this enables region-specific defaults. A "Consent Mode - Default" tag inside GTM will override the region parameter and cause 0% consent rate for non-EEA traffic.
- **NEVER hardcode the GTM Container ID in `index.html`** — always use `%VITE_GTM_ID%` (Vite env variable). Hardcoded IDs cause E2E tests and CI pipelines to generate thousands of false analytics events (page views, conversions, etc.), polluting production data. The guard `if(!i||i.indexOf('VITE_')===0)return;` ensures GTM only loads when the env variable is set.
- Do NOT install any npm packages — all tracking loads via GTM
- Follow the project's existing code style in `index.html`
- The generated JSON must be valid GTM export format (exportFormatVersion 2)
- **Maximum 5 custom events** — always clarify events with the user first
- **Always ask about the conversion goal before generating anything**
- **GA4 config tag fires on "All Pages" trigger (non-SPA) or "SPA Page View" trigger (SPA), NOT "Consent Initialization"** — the init trigger fires too early for GA4 to receive valid page data.
- **SPA projects: pageview tags fire on "SPA Page View" trigger, NOT "All Pages"** — the "All Pages" trigger only fires on the initial HTML load, not on client-side route changes. Use the `page_view` custom event trigger instead.
- **SPA projects: always add init guards** on Meta Pixel (`window.__metaPixelInitialized`) and PostHog (`window.__posthogInitialized`) tags. Without them, the SDK re-initializes on every route change.
- **SPA projects: PostHog must use `capture_pageview: false`** in the init config + manual `posthog.capture('$pageview')` per navigation. Otherwise PostHog's auto-capture fires duplicates.
- **SPA projects: always set `document.title` per route** via `useEffect` (React) or equivalent. The PageViewTracker reads `document.title` — if pages don't set it, all pages show the same title in analytics.
- **SPA projects: use `requestAnimationFrame` in the PageViewTracker** to delay the dataLayer push by one frame. This prevents a race condition where the tracker fires before lazy-loaded page components set their `document.title`.
- **Consent update event name must be exactly `consent_update`** — this must match between the cookie banner's `dataLayer.push({ event: '...' })` and the GTM trigger. A mismatch = 0% consent rate.
- **Always push gtag consent updates via dataLayer** — never rely on `window.gtag` existing. Use `window.dataLayer.push(arguments)` pattern instead.
- **Always verify or create a cookie consent banner** as part of this skill — GTM Consent Mode is useless without one
- **Do NOT create any Consent Mode tags in the GTM container** — neither "Default" nor "Update". Consent defaults go in `index.html` (region-specific). Consent updates are handled by the cookie banner calling `gtag('consent', 'update', ...)` via dataLayer with the user's actual preferences. A GTM tag that hardcodes `'granted'` overrides the user's cookie choice (GDPR violation).
- **Each tool (GA4, Meta, PostHog, etc.) is optional** — the user can skip any tool. Only generate variables, tags, and triggers for tools the user actually provides IDs for.
- **Check for Content-Security-Policy (CSP).** After adding tracking scripts, check if the project has a CSP (in `_headers`, `vercel.json`, `netlify.toml`, `next.config.js`, or as a `<meta http-equiv="Content-Security-Policy">` tag). If a CSP exists, these domains must be allowed — otherwise the browser silently blocks the tracking scripts and no data arrives in GA4/Meta/PostHog:
  - `script-src`: `https://www.googletagmanager.com`, `https://connect.facebook.net`, `https://eu.i.posthog.com`, `https://eu-assets.i.posthog.com`
  - `connect-src`: `https://www.google-analytics.com`, `https://region1.google-analytics.com`, `https://eu.i.posthog.com`, `https://www.facebook.com`
  - `frame-src`: `https://www.googletagmanager.com`
  - For additional tools (Hotjar, Clarity, TikTok, LinkedIn), add their respective domains to `script-src` and `connect-src` as well.

## GTM Container JSON Format — Critical Rules (learned from import failures)

These rules are **non-negotiable** for the JSON to import successfully into GTM:

1. **Custom HTML tag type MUST be lowercase `"html"`**, NOT `"HTML"`. GTM rejects uppercase.
   ```json
   "type": "html"    ✅ CORRECT
   "type": "HTML"    ❌ REJECTED — "unknown entity type"
   ```

2. **Do NOT include `consentSettings` in the JSON export.** GTM's import parser does not understand the `consentSettings` object format. The import will fail with "Argument is not an object: analytics_storage". Instead, tell the user to set consent requirements manually per tag in the GTM UI after import (Tag → Advanced Settings → Consent Settings → Require additional consent → `analytics_storage`).

3. **Valid tag types for GTM container JSON:**
   - `"html"` — Custom HTML (lowercase!)
   - `"googtag"` — Google Tag (gtag.js config)
   - `"gaawe"` — GA4 Event
   - `"c"` — Constant variable

4. **Valid trigger types:**
   - `"PAGEVIEW"` — All Pages
   - `"CUSTOM_EVENT"` — Custom Event

5. **Always validate the JSON** before telling the user to import it:
   ```bash
   python3 -c "import json; json.load(open('gtm-container.json')); print('Valid JSON')"
   ```

6. **NEVER include `publicId` in the container object.** If the `publicId` (e.g. `"GTM-XXXXXXX"`) in the JSON doesn't match the target container's ID, GTM rejects the import with "Container to import is incompatible with the current container." Since `publicId` gets overwritten on import anyway, always omit it. The `container` object should only contain `path`, `accountId`, `containerId`, `name`, `usageContext`, and `fingerprint` — never `publicId`.

## Pitfall: Consent Race Condition — Custom HTML tags never fire for EU users (learned in production)

**Symptom:** PostHog and Meta Pixel (`window.posthog` and `window.fbq`) are `undefined` on the live site, even though GTM loads correctly. Only GTM Server-Side Preview traffic appears in PostHog. Zero real user events for weeks.

**Root cause:** GTM Consent Mode v2 **silently blocks all Custom HTML tags** when `analytics_storage` or `ad_storage` is `denied` — even without explicit `consentSettings` on the tag. This is GTM's default behavior since Consent Mode v2. Combined with the `wait_for_update: 500` timeout, React-based cookie consent banners cannot deliver the consent update in time (React hydration takes 800-1200ms).

**Fix (two parts):**

1. **Set correct consent per tool in GTM UI (after import):**
   - PostHog tags → "No additional consent required" (GDPR-safe with `person_profiles: 'identified_only'`)
   - Meta Pixel tags → "Require additional consent → `ad_storage`"
   - GA4 tags → no changes (built-in handling)

2. **Add inline consent restore in `index.html` (before GTM script):** Read saved cookie consent from localStorage synchronously before GTM loads, so returning visitors get their consent applied within the 500ms window:
```html
// Instantly restore saved consent before GTM loads
try {
  var saved = localStorage.getItem('YOUR-CONSENT-KEY');
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
```
Place this AFTER the consent defaults but BEFORE the GTM script tag.

**Why this matters:** Without this fix, ALL EU visitors who haven't previously accepted cookies see zero tracking — PostHog, Meta Pixel, and even GA4 custom events are blocked. The Supabase Edge Functions (server-side) still work, creating a confusing mismatch where signups appear in the database but not in analytics.

---

## Pitfall: 0% Consent Rate (learned from production issue)

**Symptom:** GTM diagnostics shows "0% consent rate detected in some regions" and "100% of consent signals are marked as denied" — even outside the EEA.

**Root cause:** A "Consent Mode - Default" tag inside GTM that sets all consent to `denied` globally (without a `region` parameter). This overrides any region-specific defaults set in `index.html`.

**Fix:** Remove any "Consent Mode - Default" tag from the GTM container. Set consent defaults exclusively in `index.html` before the GTM script, using the `region` parameter to differentiate EEA vs. rest of world. Do NOT create a "Consent Mode - Update" tag in GTM either — the cookie consent banner already calls `gtag('consent', 'update', ...)` directly via dataLayer with the user's actual preferences. A GTM tag that hardcodes `'granted'` would override the user's cookie choice (GDPR violation).

## Pitfall: SPA subpages invisible in analytics (learned in production)

**Symptom:** GA4/Meta/PostHog only shows the landing page in reports. Subpages like `/datenschutz`, `/agb`, `/impressum` show zero traffic — even though users navigate to them.

**Root cause:** The project is a Single Page Application (React/Vue/Svelte). GTM's "All Pages" trigger (type `PAGEVIEW`) only fires on the initial HTML load. Client-side route changes don't trigger a new page load, so GTM never fires the pageview tags again.

**Fix:**
1. Add a "SPA Page View" trigger (Custom Event, event name `page_view`) to the GTM container
2. Switch all pageview tags (GA4, Meta, PostHog) to fire on this trigger instead of "All Pages"
3. Add a `PageViewTracker` component in the app that pushes `{ event: "page_view", page_path, page_location, page_title }` to the dataLayer on every route change
4. Add init guards on Meta Pixel + PostHog tags (see Tags section)
5. Set `document.title` in every page component

**Do NOT** set `sendPageView: false` on the GA4 `googtag` tag. The automatic pageview from the googtag config is the only GA4 pageview mechanism — suppressing it means zero pageviews in GA4.

## Pitfall: Hardcoded GTM ID pollutes analytics with test data (learned in production)

**Symptom:** GA4 and Meta Pixel show thousands of false page views, events, and conversions. Data is unreliable for decision-making.

**Root cause:** The GTM Container ID (e.g. `GTM-XXXXXXX`) was hardcoded directly in `index.html`. This means GTM loads in ALL environments — including E2E tests running on GitHub CI. Every commit triggers Playwright tests that generate dozens of page views and events, all recorded as real production traffic.

**Fix:** Never hardcode the GTM ID. Use Vite's `%VITE_GTM_ID%` env variable placeholder with a guard:
```html
<script>(function(w,d,s,l,i){if(!i||i.indexOf('VITE_')===0)return;w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','%VITE_GTM_ID%');</script>
```

The guard `if(!i||i.indexOf('VITE_')===0)return;` ensures:
- If `VITE_GTM_ID` is not set → `i` is the literal string `%VITE_GTM_ID%` → starts with `VITE_` → GTM doesn't load
- If `VITE_GTM_ID` is set (e.g. in `.env` or Netlify env vars) → `i` is `GTM-XXXXXXX` → GTM loads normally

Add `VITE_GTM_ID=GTM-XXXXXXX` to `.env` (local + production) and `.env.example`. The CI environment has no `.env`, so GTM is automatically disabled in tests.

## Pitfall: Consent Mode Update tag overrides user choice (learned in production)

**Symptom:** CodeRabbit flags GDPR violation — users who click "Nur notwendige" in the cookie banner are still fully tracked.

**Root cause:** A "Consent Mode - Update" Custom HTML tag in the GTM container that hardcodes `'granted'` for all consent types (`analytics_storage`, `ad_storage`, `ad_user_data`, `ad_personalization`). This tag fires on the `consent_update` event — the same event the cookie banner fires. The cookie banner correctly calls `gtag('consent', 'update', ...)` with the user's real preferences (granted/denied), but then the GTM tag immediately overwrites everything to `'granted'`.

**Fix:** Do NOT create any Consent Mode tags (neither "Default" nor "Update") in the GTM container. Consent defaults are set in `index.html` (region-specific, before GTM loads). Consent updates are handled by the cookie banner component, which calls `gtag('consent', 'update', ...)` directly via dataLayer with the user's actual preferences. The GTM container only needs the `consent_update` **trigger** (so other tags can react to consent changes), but no Consent Mode **tag**.
