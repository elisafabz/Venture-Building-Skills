---
name: exit-intent-survey
description: Generate an exit intent survey — detection hook, UI component, edge function, and DB migration — adapted to the project's design system and context
model: sonnet
effort: medium
---

# Exit Intent Survey

This skill is fully interactive — no arguments needed. Just run `/exit-intent-survey` and follow the prompts.

It generates 4 artifacts:
1. **Detection hook** (`useExitIntent`) — always identical across projects
2. **UI component** (`ExitIntentSurvey`) — styled to match the project's design system
3. **Edge function** or direct insert — backend persistence
4. **SQL migration** — `exit_intent_responses` table with RLS + indexes

---

## Step 0: Read project context (silent)

Before asking any questions, silently:

1. **Read the design system** — find CSS custom properties, Tailwind config, color tokens, typography classes. Check:
   - `src/index.css` or similar for CSS variables
   - `tailwind.config.*` for theme extensions
   - Any `constants/` or `tokens/` files
2. **Find the session ID utility** — search for `sessionId`, `getOrCreateSessionId`, `useSessionId`, or similar. Note the import path.
3. **Find the Supabase client** — search for `createClient`, `supabase/client`, or similar. Note the import path.
4. **Check for existing exit intent code** — search for `exitIntent`, `exit-intent`, `useExitIntent`. If found, inform the user and ask whether to replace or skip.

Store all findings internally — use them to generate code that matches the project perfectly.

---

## Step 1: Ask 3 setup questions (one at a time)

### Question 1: Page context

```
Where should the exit intent survey be added?

1. Survey flow (e.g. multi-step survey)
2. Checkout (e.g. purchase flow)
3. Landing page (e.g. product landing page)
4. Product page (e.g. detail page)

And what is your conversion goal? (e.g. completing a survey, a purchase, a waitlist signup)
```

Wait for the user's answer before continuing.

### Question 2: Context variable

Based on the page context, suggest the most useful context variable:

- **Survey flow:** `currentScreen` (number) — which step they left on
- **Checkout:** `cartValue` (number) or `productName` (text)
- **Landing page:** nothing extra (just page URL)
- **Product page:** `productName` (text) or `productId` (text)

```
Which context variable should be logged alongside?

For [context type] I recommend: [suggestion] — that shows you [why it's useful].

Does that work, or do you want to track something else?
```

Wait for the user's answer before continuing.

### Question 3: Persistence method

```
How should the feedback be stored?

1. Edge Function (empfohlen) — Zod-Validierung + Rate Limiting serverseitig
2. A direct Supabase insert — faster to set up, but no server-side validation

For most projects I recommend option 1.
```

Wait for the user's answer before continuing.

---

## Step 2: Define exit reasons

Based on the page context from Step 1, suggest 6 default reasons:

### Survey Flow
```typescript
const EXIT_REASONS = [
  { id: "price", label: "Too expensive" },
  { id: "not_ready", label: "Too early for me, I'll come back later" },
  { id: "unclear_value", label: "The benefit isn't clear enough" },
  { id: "too_personal", label: "Too personal a topic for an app" },
  { id: "just_looking", label: "Just browsing" },
  { id: "other", label: "Other" },
] as const;
```

### Checkout
```typescript
const EXIT_REASONS = [
  { id: "price", label: "Price too high" },
  { id: "unclear_value", label: "The benefit isn't clear enough" },
  { id: "not_right", label: "Not right for me" },
  { id: "looking_elsewhere", label: "Looking for something else" },
  { id: "tech_doubts", label: "Technical doubts" },
  { id: "other", label: "Other" },
] as const;
```

### Landing Page
```typescript
const EXIT_REASONS = [
  { id: "not_relevant", label: "Not relevant to me" },
  { id: "not_understood", label: "Not quite understood" },
  { id: "not_now", label: "Not now, maybe later" },
  { id: "trust", label: "Not sure it's trustworthy" },
  { id: "just_looking", label: "Just browsing" },
  { id: "other", label: "Other" },
] as const;
```

### Product page
```typescript
const EXIT_REASONS = [
  { id: "price", label: "Price too high" },
  { id: "not_right", label: "Doesn't fit my needs" },
  { id: "comparison", label: "Comparing other options" },
  { id: "unclear_info", label: "Not enough information" },
  { id: "not_now", label: "Not now, maybe later" },
  { id: "other", label: "Other" },
] as const;
```

Present the matching defaults and ask:

```
Here are the default reasons for [context type]:

[list reasons]

Do these work, or do you want to adjust any? (max six; the last one should always be "Other")
```

Wait for confirmation or customization before continuing.

---

## Step 3: Generate detection hook

Create `src/hooks/useExitIntent.ts` — this is **always identical** regardless of project:

```typescript
import { useState, useEffect, useCallback, useRef } from "react";

const ACTIVATION_DELAY_MS = 5000;

interface UseExitIntentOptions {
  /** Don't trigger when already completed */
  enabled: boolean;
}

export function useExitIntent({ enabled }: UseExitIntentOptions) {
  const [isVisible, setIsVisible] = useState(false);
  const hasShownRef = useRef(false);
  const isActiveRef = useRef(false);

  const showPopup = useCallback(() => {
    if (hasShownRef.current || !isActiveRef.current || !enabled) return;
    hasShownRef.current = true;
    sessionStorage.setItem("exit_intent_shown", "true");
    setIsVisible(true);
  }, [enabled]);

  // Activation delay + session check
  useEffect(() => {
    if (!enabled) return;
    const shown = sessionStorage.getItem("exit_intent_shown");
    if (shown) {
      hasShownRef.current = true;
      return;
    }
    const timer = setTimeout(() => {
      isActiveRef.current = true;
    }, ACTIVATION_DELAY_MS);
    return () => clearTimeout(timer);
  }, [enabled]);

  // Desktop: mouse leaves viewport top edge
  useEffect(() => {
    if (!enabled) return;
    const isMobile = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    if (isMobile) return;

    const handleMouseLeave = (e: MouseEvent) => {
      if (e.clientY <= 5) showPopup();
    };

    document.addEventListener("mouseleave", handleMouseLeave);
    return () => document.removeEventListener("mouseleave", handleMouseLeave);
  }, [enabled, showPopup]);

  // Mobile: tab switch (visibilitychange) + repeated scroll-up
  useEffect(() => {
    if (!enabled) return;
    const isMobile = "ontouchstart" in window || navigator.maxTouchPoints > 0;
    if (!isMobile) return;

    const handleVisibilityChange = () => {
      if (document.visibilityState === "hidden") showPopup();
    };

    let lastScrollY = window.scrollY;
    let scrollUpCount = 0;

    const handleScroll = () => {
      const currentScrollY = window.scrollY;
      const diff = lastScrollY - currentScrollY;
      if (diff > 60) {
        scrollUpCount++;
        if (scrollUpCount >= 2) showPopup();
      } else if (diff < -30) {
        scrollUpCount = 0;
      }
      lastScrollY = currentScrollY;
    };

    document.addEventListener("visibilitychange", handleVisibilityChange);
    window.addEventListener("scroll", handleScroll, { passive: true });

    return () => {
      document.removeEventListener("visibilitychange", handleVisibilityChange);
      window.removeEventListener("scroll", handleScroll);
    };
  }, [enabled, showPopup]);

  const dismiss = useCallback(() => setIsVisible(false), []);

  return { isVisible, dismiss };
}
```

---

## Step 4: Generate UI component

Create the component in the appropriate location:
- If `src/components/survey/` exists → `src/components/survey/ExitIntentSurvey.tsx`
- Otherwise → `src/components/ExitIntentSurvey.tsx`

**CRITICAL: Use the project's actual design tokens** found in Step 0. Do NOT hardcode colors — use CSS variables, Tailwind classes, or whatever the project uses.

### Component structure

```
┌─────────────────────────────┐
│ [X close]                   │
│                             │
│ Before you go               │  ← title
│ What wasn't right?          │  ← subtitle
│                             │
│ ○ Reason 1                  │
│ ○ Reason 2                  │  ← single-select radio buttons
│ ● Reason 3 (selected)       │
│ ○ Reason 4                  │
│ ○ Reason 5                  │
│ ○ Other                     │
│                             │
│ [ Send feedback ]           │  ← submit button (disabled until selection)
│     Skip                        │  ← dismiss link
└─────────────────────────────┘
```

After submit → success state:
```
┌─────────────────────────────┐
│                             │
│        ✓ (checkmark)        │
│  Thanks for the feedback!   │
│                             │
└─────────────────────────────┘
```

### Requirements

- **Layout:** bottom-sheet on mobile (slides up from bottom, rounded top corners), centered modal on desktop (rounded all corners)
- **Backdrop:** semi-transparent overlay (`bg-black/40` or equivalent)
- **z-index:** `10001` (above cookie banners which typically use 9999–10000)
- **Animation:** slide-in from bottom on mobile, zoom-in on desktop (use CSS animations or Tailwind `animate-in` if available)
- **Accessibility:** `role="dialog"`, `aria-modal="true"`, `aria-labelledby` on title, `aria-label="Close"` on the close button, Escape key dismisses
- **Submit flow:** select reason → click "Send feedback" → loading state ("Sending...") → success checkmark → auto-dismiss after 1500ms
- **Best-effort:** wrap API call in try/catch, never block user on failure
- **Icons:** only `X` from `lucide-react` (close button), inline SVG for checkmark

### Props interface

Adapt based on context variable from Step 1:

```typescript
// Survey flow
interface ExitIntentSurveyProps {
  currentScreen: number;
  onDismiss: () => void;
}

// Checkout
interface ExitIntentSurveyProps {
  productName?: string;
  cartValue?: number;
  onDismiss: () => void;
}

// Landing page
interface ExitIntentSurveyProps {
  onDismiss: () => void;
}
```

### API call

**If Edge Function (recommended):**
```typescript
await supabase.functions.invoke("save-exit-intent", {
  body: {
    sessionId: getOrCreateSessionId(),
    reason: selectedReason,
    reasonLabel: EXIT_REASONS.find((r) => r.id === selectedReason)?.label,
    [contextField]: contextValue, // e.g. currentScreen, productName
    pageUrl: window.location.href,
  },
});
```

**If direct insert:**
```typescript
await supabase.from("exit_intent_responses").insert({
  session_id: getOrCreateSessionId(),
  reason: selectedReason,
  reason_label: EXIT_REASONS.find((r) => r.id === selectedReason)?.label,
  [contextColumn]: contextValue,
  page_url: window.location.href,
});
```

Use the **actual Supabase client import path** and **session ID utility** found in Step 0.

---

## Step 5: Generate backend

### Option A: Edge Function (recommended)

Create `supabase/functions/save-exit-intent/index.ts`:

```typescript
import { createClient } from 'https://esm.sh/@supabase/supabase-js@2'
import { z } from 'https://deno.land/x/zod/mod.ts'

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

// Adapt schema based on context variable
const exitIntentSchema = z.object({
  sessionId: z.string().uuid(),
  reason: z.string().max(50),
  reasonLabel: z.string().max(200).optional(),
  // Context field — adapt per project:
  // currentScreen: z.number().int().min(1).max(20),    // survey
  // productName: z.string().max(200).optional(),        // checkout/product
  pageUrl: z.string().max(500).optional(),
})

// Rate limiting — 3 per session per minute
const rateLimitStore = new Map<string, { count: number; resetTime: number }>()

function checkRateLimit(sessionId: string): boolean {
  const now = Date.now()
  const record = rateLimitStore.get(sessionId)
  if (!record || now > record.resetTime) {
    rateLimitStore.set(sessionId, { count: 1, resetTime: now + 60000 })
    return true
  }
  if (record.count >= 3) return false
  record.count++
  return true
}

Deno.serve(async (req) => {
  if (req.method === 'OPTIONS') {
    return new Response(null, { headers: corsHeaders })
  }

  try {
    const supabase = createClient(
      Deno.env.get('SUPABASE_URL') ?? '',
      Deno.env.get('SUPABASE_SERVICE_ROLE_KEY') ?? '',
      { auth: { autoRefreshToken: false, persistSession: false } }
    )

    const rawBody = await req.json()
    const parsed = exitIntentSchema.safeParse(rawBody)

    if (!parsed.success) {
      return new Response(
        JSON.stringify({ error: 'Validation failed', details: parsed.error.format() }),
        { status: 400, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
      )
    }

    const { sessionId, reason, reasonLabel, pageUrl, ...contextFields } = parsed.data

    if (!checkRateLimit(sessionId)) {
      return new Response(
        JSON.stringify({ error: 'Rate limit exceeded' }),
        { status: 429, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
      )
    }

    const { error } = await supabase
      .from('exit_intent_responses')
      .insert({
        session_id: sessionId,
        reason,
        reason_label: reasonLabel,
        page_url: pageUrl,
        ...contextFields, // spread context column(s)
      })

    if (error) {
      console.error('Error saving exit intent:', error)
      throw error
    }

    return new Response(
      JSON.stringify({ success: true }),
      { headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )
  } catch (error) {
    console.error('Exit intent error:', error)
    return new Response(
      JSON.stringify({ error: 'Internal server error' }),
      { status: 500, headers: { ...corsHeaders, 'Content-Type': 'application/json' } }
    )
  }
})
```

### Option B: Direct insert

Skip edge function creation. Note the tradeoff to the user:
```
⚠️ Direct Supabase insert: no server-side validation or rate limiting.
Anyone with the anon key could in theory insert data.
Fine for low-traffic sites; for production I recommend the edge function.
```

---

## Step 6: Generate SQL migration

Create a migration file at `supabase/migrations/[timestamp]_create_exit_intent_responses.sql`.

Adapt the context column based on Step 1:

```sql
-- Exit intent survey responses
CREATE TABLE IF NOT EXISTS exit_intent_responses (
  id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
  session_id UUID NOT NULL,
  reason TEXT NOT NULL,
  reason_label TEXT,
  -- Context column (adapt per project):
  -- current_screen INTEGER,           -- survey flow
  -- product_name TEXT,                 -- checkout / product page
  -- cart_value NUMERIC(10,2),          -- checkout
  page_url TEXT,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Indexes
CREATE INDEX idx_exit_intent_session ON exit_intent_responses (session_id);
CREATE INDEX idx_exit_intent_reason ON exit_intent_responses (reason);
CREATE INDEX idx_exit_intent_created ON exit_intent_responses (created_at DESC);

-- RLS: no direct access from client (edge function uses service_role)
ALTER TABLE exit_intent_responses ENABLE ROW LEVEL SECURITY;

-- If using direct insert instead of edge function, add this policy:
-- CREATE POLICY "Allow anonymous inserts" ON exit_intent_responses
--   FOR INSERT TO anon WITH CHECK (true);
```

If the user chose direct insert in Step 1, uncomment the RLS policy for anonymous inserts.

---

## Step 7: Wire into target component

Show the exact integration code for the user's specific file. Find the target component from Step 1 context and provide a snippet like:

```typescript
// In the target component (e.g. SurveyWizard.tsx, CheckoutPage.tsx, etc.)

import { useExitIntent } from "@/hooks/useExitIntent";
import ExitIntentSurvey from "@/components/survey/ExitIntentSurvey";

// Inside the component:
const { isVisible: showExitIntent, dismiss: dismissExitIntent } = useExitIntent({
  enabled: !isCompleted, // adapt condition: e.g. !isPurchased, true for landing pages
});

// In the JSX return:
{showExitIntent && (
  <ExitIntentSurvey
    currentScreen={currentScreen} // or productName, or nothing — depends on context
    onDismiss={dismissExitIntent}
  />
)}
```

Point to the **exact file and location** where this should be added.

---

## Step 8: Summary

After all files are generated, show:

```
Done! Exit Intent Survey set up:

✅ src/hooks/useExitIntent.ts — Detection (Desktop top-edge + Mobile scroll-up/tab-switch)
✅ src/components/[path]/ExitIntentSurvey.tsx — UI (bottom-sheet mobile / modal desktop)
✅ supabase/functions/save-exit-intent/index.ts — Edge Function with Zod + rate limiting
   (or: direct Supabase insert)
✅ supabase/migrations/[timestamp]_create_exit_intent_responses.sql — Tabelle + RLS + Indexes
✅ Integration in [target component] gezeigt

Next steps:
1. Apply migration: supabase db push (or supabase migration up)
2. Edge Function deployen: supabase functions deploy save-exit-intent
3. Test it: open the page → wait 5s → move the mouse past the top edge of the viewport
4. Verify: a row appears in exit_intent_responses
```

---

## Rules

- **Always read the design system first** — never hardcode colors. Use the project's CSS variables, Tailwind classes, or design tokens.
- **Max 6 reasons** — always end with "Other"
- **Write the copy in the language of the site** — e.g. "Before you go" / "What wasn't right?" / "Send feedback" / "Skip"
- **5s activation delay**, once per session (sessionStorage), desktop top-edge detection only (clientY ≤ 5)
- **Mobile detection:** visibilitychange + 2× scroll-up > 60px
- **Hook separate from UI** — `useExitIntent` returns `{ isVisible, dismiss }`, component is stateless regarding detection
- **Best-effort submission** — try/catch, never block the user or show error states
- **No npm packages** — only `lucide-react` for the X icon, inline SVG for checkmark
- **Edge function:** always include Zod validation + rate limiting (3/session/min)
- **Direct insert:** always warn about missing server-side validation
- **z-index: 10001** — above cookie banners
- **Accessibility:** `role="dialog"`, `aria-modal="true"`, Escape closes, `aria-label` on close button
- **Auto-dismiss:** 1500ms after successful submission
