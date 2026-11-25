---
name: db-setup
description: Use when starting a new project and need the full database setup — user_sessions, user_events tables, track-session and track-event Edge Functions, frontend hooks (useSession, useTrackEvent), sessionId utility, and tracking.ts integration. Scaffolds everything for GDPR-compliant session and event tracking.
model: haiku
effort: low
---

# Database Setup — Session & Event Tracking

Scaffold the complete session tracking system for a project. Creates DB tables, Edge Functions, and frontend hooks in one go.

## What Gets Created

| Layer | Files | Purpose |
|-------|-------|---------|
| **Migration** | `supabase/migrations/{ts}_create_user_sessions_and_events.sql` | `user_sessions` + `user_events` tables with RLS, indexes, triggers |
| **Edge Functions** | `supabase/functions/track-session/index.ts` | Session create (with IP truncation, Cloudflare geo) + update (session_end) |
| | `supabase/functions/track-event/index.ts` | Event tracking with Zod validation, rate limiting, customData size cap |
| **Frontend** | `src/lib/sessionId.ts` | `getOrCreateSessionId()` via `crypto.randomUUID()` + sessionStorage |
| | `src/hooks/useSession.ts` | Auto-create session on page load, session_end on unload (pagehide + visibilitychange + beforeunload) |
| | `src/hooks/useTrackEvent.ts` | Hook for component-level event tracking + GTM dataLayer |
| | `src/lib/tracking.ts` | Extend existing `trackEvent()` to send to both GTM and Supabase |
| **App integration** | `src/App.tsx` | `SessionTracker` component + `PageViewTracker` with Supabase events |

## Steps

1. **Read existing project** — check `supabase/migrations/`, `src/App.tsx`, `src/lib/tracking.ts` for existing patterns
2. **Create migration** — `user_sessions` (browser, device, location, UTM, environment) + `user_events` (event_type, page_url, custom_data)
3. **Create Edge Functions** — `track-session` (create/update with IP truncation) + `track-event` (with customData validation)
4. **Create frontend utilities** — `sessionId.ts`, `useSession.ts`, `useTrackEvent.ts`
5. **Extend tracking.ts** — add Supabase sending to existing `trackEvent()`, with `skipDataLayer` option and 3s retry for early events
6. **Integrate in App.tsx** — add `SessionTracker` + extend `PageViewTracker`
7. **Add session_id to existing signup tables** — migration + Edge Function updates + frontend `api.ts`
8. **Define funnel events** — ask user for pages/flows, create event plan (see "Event Definition" section below)
9. **Integrate events in components** — add `trackEvent()` calls at every CTA, flow start/step/complete/abandon

## Migration Template

```sql
-- Helper: auto-update updated_at
CREATE OR REPLACE FUNCTION public.update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = now();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Helper: protect session_id immutability
CREATE OR REPLACE FUNCTION public.protect_immutable_cols()
RETURNS TRIGGER AS $$
BEGIN
  IF NEW.session_id IS DISTINCT FROM OLD.session_id THEN
    RAISE EXCEPTION 'session_id is immutable';
  END IF;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- user_sessions (central table)
CREATE TABLE IF NOT EXISTS public.user_sessions (
  session_id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  browser_name     TEXT,
  browser_version  TEXT,
  user_agent       TEXT,
  os_name          TEXT,
  device_type      TEXT,
  screen_resolution TEXT,
  ip_prefix        TEXT,   -- truncated: last octet zeroed (GDPR)
  country          TEXT,
  city             TEXT,
  language         TEXT,
  timezone         TEXT,
  referrer         TEXT,
  utm_source       TEXT,
  utm_medium       TEXT,
  utm_campaign     TEXT,
  environment      TEXT DEFAULT 'production',
  is_test_user     BOOLEAN DEFAULT FALSE,
  session_start    TIMESTAMPTZ NOT NULL DEFAULT now(),
  session_end      TIMESTAMPTZ,
  created_at       TIMESTAMPTZ NOT NULL DEFAULT now(),
  updated_at       TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- user_events
CREATE TABLE IF NOT EXISTS public.user_events (
  id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  session_id    UUID NOT NULL REFERENCES public.user_sessions(session_id) ON DELETE CASCADE,
  event_type    TEXT NOT NULL,
  page_url      TEXT NOT NULL,
  element_id    TEXT,
  element_text  TEXT,
  custom_data   JSONB,
  timestamp     TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Indexes
CREATE INDEX IF NOT EXISTS idx_user_events_session ON public.user_events (session_id);
CREATE INDEX IF NOT EXISTS idx_sessions_created_at ON public.user_sessions (created_at);
CREATE INDEX IF NOT EXISTS idx_sessions_environment ON public.user_sessions (environment);
CREATE INDEX IF NOT EXISTS idx_sessions_utm_source ON public.user_sessions (utm_source);
CREATE INDEX IF NOT EXISTS idx_user_events_type ON public.user_events (event_type);
CREATE INDEX IF NOT EXISTS idx_user_events_timestamp ON public.user_events (timestamp);

-- RLS (no policies = only service_role can write)
ALTER TABLE public.user_sessions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_events   ENABLE ROW LEVEL SECURITY;

-- Triggers
CREATE TRIGGER trg_sessions_updated_at
  BEFORE UPDATE ON public.user_sessions
  FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_column();

CREATE TRIGGER trg_sessions_protect_immutable
  BEFORE UPDATE ON public.user_sessions
  FOR EACH ROW EXECUTE FUNCTION public.protect_immutable_cols();

CREATE TRIGGER trg_user_events_protect_immutable
  BEFORE UPDATE ON public.user_events
  FOR EACH ROW EXECUTE FUNCTION public.protect_immutable_cols();
```

## Key Design Decisions

| Decision | Why |
|----------|-----|
| **IP truncation** (last octet zeroed) | GDPR: `192.168.1.47` becomes `192.168.1.0`. Column is `ip_prefix`, not `ip_address` |
| **Cloudflare geo headers** (`cf-ipcountry`, `cf-ipcity`) | No external API call needed, no IP sent to third party |
| **`ignoreDuplicates: true`** on session upsert | Preserve first-touch acquisition data on page reloads |
| **`--no-verify-jwt`** on Edge Functions | Analytics endpoints are public (like GA/PostHog). Rate limiting + Zod + RLS is sufficient |
| **`pagehide` + `visibilitychange`** for session_end | `beforeunload` is unreliable on mobile (<50%). `pagehide` has 91% coverage |
| **`fetch` with `keepalive: true`** (not sendBeacon) | sendBeacon cannot set custom headers, Supabase would reject with 401 |
| **3s retry for early events** | Page view events can fire before session is created (FK constraint) |
| **`customData` restricted to primitives + 5KB** | Prevents storage bombing via `z.record(z.any())` |
| **No FK on signup tables** to `user_sessions` | Signups must work even if session tracking fails |
| **Test mode kills all tracking** | `import.meta.env.MODE === 'test'` skips Supabase events, sessions, and PostHog. E2E tests must never pollute analytics. GTM is already handled by not setting `VITE_GTM_ID` in `.env.test` |

## OS Detection Order

**IMPORTANT:** Detect in this order to avoid Android being classified as Linux:
```
iOS → Android → macOS → Windows → Linux
```

## After Creating

1. `supabase db reset` — test migration locally
2. `npm run build` — verify TypeScript compiles
3. `supabase db push` — apply to production
4. `supabase functions deploy track-session track-event --no-verify-jwt` — deploy Edge Functions
5. Push frontend code — Vercel/Netlify auto-deploys
6. Verify in Supabase dashboard that `user_sessions` fills on page visit

## Event Definition (REQUIRED)

After creating the tracking infrastructure, you MUST define and integrate the project's funnel events. Do NOT leave `trackEvent()` unused — the infrastructure alone is worthless without actual events firing.

### Step 8: Define Funnel Events

Ask the user which pages/flows exist, then define the event plan. Use this template as a starting point and adapt to the project:

| Event | Where | elementId | customData |
|-------|-------|-----------|------------|
| `cta_click` | Every CTA button that leads to signup/onboarding | Which CTA (e.g. `hero-cta`, `header-cta`) | — |
| `page_view` | `App.tsx` PageViewTracker (already created in Step 6) | — | — |
| `onboarding_start` | First step of any multi-step flow | — | — |
| `onboarding_step_viewed` | Each step change in multi-step flows | — | `{ step, step_name }` |
| `onboarding_abandoned` | Close/back-to-home from multi-step flow | — | `{ step, step_name }` |
| `onboarding_complete` | Final submission success | — | — |
| `email_signup` | Email captured (waitlist, newsletter, lead) | — | — |
| `signup_complete` | Account created / event registered | — | — |

### Step 9: Integrate Events in Components

For each event defined above:
1. Import `trackEvent` from `@/lib/tracking`
2. Add `trackEvent()` call alongside existing `dataLayer.push()` / `posthog.capture()` calls
3. If no GTM/PostHog exists yet, add a `dataLayer.push()` too — run `/analytics-tracking` or `/setup-gtm` to set up the GTM side

### Consent Rules

- **Sessions (`useSession`)**: Always fire. Sessions are a technical requirement for linking data, not analytics.
- **Supabase events (`trackEvent`)**: Always fire. These are first-party funnel data without PII (IP already truncated, no email/name). Comparable to server logs.
- **PostHog / Meta Pixel / GA4**: Consent-dependent (Statistik/Marketing). These are third-party tracking tools. Managed via GTM Consent Mode v2.

This means `tracking.ts` must NOT check for cookie consent before sending to Supabase. The consent check should only gate third-party tools (PostHog, Meta Pixel) — not your own database.

### Cross-reference

- For GTM container setup + Consent Mode v2 + GA4/Meta Pixel: run `/setup-gtm`
- For event naming conventions + UTM strategy + conversion tracking: run `/analytics-tracking`
- Events should use the same `event` names in both Supabase and GTM dataLayer for consistency

## Existing Signup Tables

For each signup table (`event_signups`, `info_event_signups`, etc.):
1. Add `session_id UUID` column via migration (nullable, no FK)
2. Add `sessionId` to Edge Function validation + insert
3. Add `sessionId: getOrCreateSessionId()` to frontend API call

## Reference Implementation

Reference structure of a complete working implementation:
- Migration: `supabase/migrations/20260414210000_create_user_sessions_and_events.sql`
- Edge Functions: `supabase/functions/track-session/index.ts`, `track-event/index.ts`
- Frontend: `src/hooks/useSession.ts`, `src/hooks/useTrackEvent.ts`, `src/lib/tracking.ts`
