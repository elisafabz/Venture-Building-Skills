---
name: admin-dashboard
description: Scaffold a complete admin KPI dashboard with Supabase Auth, Edge Function, and React frontend for any project
model: opus
effort: medium
---

# Admin KPI Dashboard

Scaffold a complete admin dashboard with login, live KPI cards, and data tables for any Supabase-backed venture.

## When to use

When the user says: "admin dashboard", "KPI dashboard bauen", "dashboard erstellen", "admin board"

## What it builds

1. **Login page** at `/admin` (Supabase Auth, email + password)
2. **Dashboard page** at `/admin/dashboard` (auth-guarded)
3. **Edge Function** `dashboard-data` (aggregates all metrics server-side)
4. **Dark glassmorphism UI** with a modern dark look

## Steps

### Step 1: Ask the user

Ask these questions one at a time:

1. **Which tables** should the dashboard pull from? (e.g. `event_signups`, `leads`, `orders`)
2. **Which KPIs** matter? (e.g. total signups, revenue, conversion rate, target group fit)
3. **Any status/ampel logic?** (e.g. kill-switch with green/yellow/red thresholds)
4. **Admin email** for the auth guard

### Step 2: Create the Edge Function

Create `supabase/functions/dashboard-data/index.ts`:

```typescript
import { serve } from "https://deno.land/std@0.168.0/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";

const ALLOWED_ORIGINS = [
  Deno.env.get("SITE_URL") || "https://VENTURE.at",
  "http://localhost:8080",
  "http://localhost:8081",
  "http://localhost:5173",
];
const ADMIN_EMAIL = Deno.env.get("ADMIN_EMAIL") || "";

function getCorsHeaders(req: Request) {
  const origin = req.headers.get("origin") || "";
  const allowed = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0];
  return {
    "Access-Control-Allow-Origin": allowed,
    "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  };
}

function jsonResponse(data: unknown, status = 200, req?: Request) {
  const cors = req ? getCorsHeaders(req) : { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type" };
  return new Response(JSON.stringify(data), {
    status,
    headers: { ...cors, "Content-Type": "application/json" },
  });
}

serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: getCorsHeaders(req) });
  }

  const authHeader = req.headers.get("authorization");
  if (!authHeader?.startsWith("Bearer ")) {
    return jsonResponse({ error: "Missing authorization" }, 401, req);
  }

  const supabaseAuth = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_ANON_KEY")!
  );

  const { data: { user }, error: authError } = await supabaseAuth.auth.getUser(
    authHeader.replace("Bearer ", "")
  );

  if (authError || !user || user.email !== ADMIN_EMAIL) {
    return jsonResponse({ error: "Unauthorized" }, 403, req);
  }

  const supabase = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
  );

  try {
    // CUSTOMIZE: Add your queries here
    // const { data, error } = await supabase.from("TABLE").select("*");

    return jsonResponse({
      // CUSTOMIZE: Return your KPI data here
    }, 200, req);
  } catch (err) {
    console.error("Dashboard data error:", err);
    return jsonResponse({ error: "Internal server error" }, 500, req);
  }
});
```

**Deploy with:** `npx supabase functions deploy dashboard-data --no-verify-jwt`

The `--no-verify-jwt` flag is required because Supabase Gateway rejects ES256 JWTs from newer projects. Auth verification happens in our code.

### Step 3: Create the auth hook

Create `src/lib/useAdminAuth.ts`:

```typescript
import { useState, useEffect, useCallback } from "react";
import { supabase } from "@/integrations/supabase/client";
import type { User, Session } from "@supabase/supabase-js";

const ADMIN_EMAIL = import.meta.env.VITE_ADMIN_EMAIL || "";

interface AdminAuthState {
  user: User | null;
  session: Session | null;
  isAdmin: boolean;
  isLoading: boolean;
}

export function useAdminAuth() {
  const [state, setState] = useState<AdminAuthState>({
    user: null, session: null, isAdmin: false, isLoading: true,
  });

  useEffect(() => {
    supabase.auth.getSession().then(({ data: { session } }) => {
      const user = session?.user ?? null;
      setState({ user, session, isAdmin: user?.email === ADMIN_EMAIL, isLoading: false });
    });

    const { data: { subscription } } = supabase.auth.onAuthStateChange((_event, session) => {
      const user = session?.user ?? null;
      setState({ user, session, isAdmin: user?.email === ADMIN_EMAIL, isLoading: false });
    });

    return () => subscription.unsubscribe();
  }, []);

  const login = useCallback(async (email: string, password: string) => {
    const { error } = await supabase.auth.signInWithPassword({ email, password });
    if (error) throw error;
  }, []);

  const logout = useCallback(async () => {
    await supabase.auth.signOut();
  }, []);

  return { ...state, login, logout };
}
```

### Step 4: Create the data hook

Create `src/lib/useDashboardData.ts` — uses React Query, fetches from the Edge Function, auto-refreshes every 60s. Only fetches when session exists (`enabled: !!session`).

### Step 5: Create pages

**AdminLogin** (`src/pages/AdminLogin.tsx`):
- Dark background, centered white card
- Email + password form
- useEffect for redirect when already logged in (NOT render-time navigate)
- No admin email in placeholder (security)
- German labels

**AdminDashboard** (`src/pages/AdminDashboard.tsx`):
- Dark gradient background (`from-[#1a1f2e] to-[#222f30]`)
- Sticky header with title, refresh, logout
- KPI cards in responsive grid
- Optional status ampel banner
- Data tables for detail views

### Step 6: Add routes

In `App.tsx`, add lazy-loaded routes:
```tsx
const AdminLogin = lazy(() => import("./pages/AdminLogin"));
const AdminDashboard = lazy(() => import("./pages/AdminDashboard"));

// Inside <Routes>:
<Route path="/admin" element={<AdminLogin />} />
<Route path="/admin/dashboard" element={<AdminDashboard />} />
```

### Step 7: Components

Reusable components in `src/components/admin/`:

- **KpiCard** — glassmorphism card with title, big number, optional color coding, optional progress bar
- **StatusBanner** — full-width colored banner (green/yellow/red) with status label and criteria indicators
- **DataTable** — dark-themed table with tab switching

### Step 8: Environment

```bash
# .env (local)
VITE_ADMIN_EMAIL=admin@venture.com

# Supabase secrets
npx supabase secrets set ADMIN_EMAIL=admin@venture.com

# Netlify env var
VITE_ADMIN_EMAIL=admin@venture.com
```

### Step 9: Supabase Auth user

The admin user must exist in Supabase Auth. Create via dashboard or CLI. Email must be confirmed.

## Data filtering rules

- **Production only:** Always filter `user_sessions` by `environment = 'production'`. Never show test/dev data.
- **the target market only:** Filter sessions by country (`AT`, `DE`, `CH`). Include rows where country is null (geo not yet set up).
- **No PII in edge function responses** except email (admin-guarded). Never return full IP, user agent, or birth dates.

## Design rules

- All text in German (local), code in English
- Dark glassmorphism: `bg-white/[0.04]`, `border-white/[0.06]`, `backdrop-blur-sm`
- Use opaque text colors for WCAG AA contrast (`text-gray-400` not `text-white/40`)
- Brand purple: `#9b40ea`
- Status colors: emerald for good, amber for warning, red for bad
- No manual input fields — dashboard shows only live data from Supabase
- Button `type="button"` on all non-submit buttons
- No admin email exposed in UI
