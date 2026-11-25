---
name: analytics-tracking
description: Set up analytics tracking - GA4 event architecture, GTM best practices, UTM conventions, conversion tracking, event naming, GDPR-compliant tracking with Consent Mode v2. Run /analytics-tracking to plan or implement tracking.
model: sonnet
effort: medium
---

# Analytics Tracking Skill

## Step 0: Marketing Context laden

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

---

## Intake

Before doing anything, ask the user these three questions:

**Question 1:** What do you need?
- A) New tracking setup (starting from scratch or adding to a new project)
- B) Audit existing tracking (check what's working, what's missing)
- C) Just UTM conventions (no code changes, just the naming system)
- D) GDPR compliance check (consent mode, cookie banner)

**Question 2:** What tools do you currently use or plan to use?
- GA4 (Google Analytics 4)?
- GTM (Google Tag Manager - the container that fires tags without code changes)?
- PostHog (product analytics)?
- None yet?

**Question 3:** What type of product is this?
- Website (marketing/content site)
- Web App (logged-in product)
- Landing Page (single conversion page)

Based on answers, proceed to the matching mode below.

---

## Overview

This skill helps you plan and implement a complete analytics tracking setup. The goal is not to track everything - it is to track what drives decisions. Start lean, add only when there is a clear reason.

---

## Mode A: New Setup

Use when: user chose "New tracking setup" (Answer A to Question 1).

### Phase 1: Tool Selection

Is this relevant? "Shall I help you choose the right analytics tools for your product? Yes / no"

If YES:
- [ ] Decision: GA4 only vs. GA4 + PostHog vs. PostHog only
- [ ] Decision: Use GTM (recommended for flexibility) vs. hardcode tags
- [ ] If no GTM yet: run `/setup-gtm` first
- [ ] Tools confirmed and accounts created

**Recommendation rule:** For marketing sites: GA4 + GTM. For web apps: GA4 + PostHog + GTM. For landing pages: GA4 only (GTM optional).

### Phase 2: Event Architecture

Is this relevant? "Shall I plan the event architecture (which events get tracked)? Yes / no"

If YES, define events per funnel stage:

**Macro Conversions (primary goals - must always track):**
- [ ] Account signup / registration completed
- [ ] First purchase / subscription activated
- [ ] Demo booked / lead form submitted
- [ ] Paid plan upgraded

**Micro Conversions (leading indicators - track to understand funnel):**
- [ ] Email newsletter signup
- [ ] Pricing page visited
- [ ] Demo video watched >50%
- [ ] Feature page clicked
- [ ] Return visit within 7 days

**Custom Events (add only for decisions you actually make):**

| Event name (snake_case) | Trigger | Why we track it |
|------------------------|---------|-----------------|
| `click_cta_hero` | Hero CTA button click | |
| `submit_form_contact` | Contact form success | |
| `view_pricing` | Pricing page load | |
| `start_trial` | Trial start button click | |
| `complete_onboarding` | Onboarding flow complete | |

**Custom Event Naming Convention:**
- Format: `snake_case` only - no spaces, no camelCase, no hyphens
- Max 40 characters
- Pattern: `verb_noun` (what happened - to what)

**Event Parameters to include:**
```javascript
gtag('event', 'click_cta_hero', {
  'button_text': 'Start Free Trial',
  'button_location': 'hero',
  'page_path': window.location.pathname,
  'user_type': 'anonymous' // or 'logged_in'
});
```

### Phase 3: UTM Convention Setup

Is this relevant? "Shall I define the UTM conventions for your venture? Yes / no"

If YES - see UTM table below (Mode C content applies here too).

### Phase 4: GDPR / Consent Mode v2

Is this relevant? "Shall I plan a GDPR-compliant tracking setup (Consent Mode v2, cookie banner)? Yes / no"

If YES - see GDPR section below (Mode D content applies here too).

### Phase 5: Go-Live Checklist

- [ ] GA4 property created and Measurement ID added to site
- [ ] GTM container installed on all pages (including thank-you pages)
- [ ] Consent Mode v2 configured
- [ ] Cookie banner live and tested (reject = no tracking fires)
- [ ] All macro conversions firing correctly (test in GTM Preview mode)
- [ ] UTM parameters being captured in GA4
- [ ] Referral exclusion list set (exclude your own domains)
- [ ] Internal traffic filter set (exclude your own IP)
- [ ] Cross-domain tracking set up if multiple domains
- [ ] GA4 linked to Google Ads (for conversion import)
- [ ] Events visible in GA4 Realtime within 24h of launch

---

## Mode B: Audit Existing Tracking

Use when: user chose "Audit existing tracking" (Answer B to Question 1).

- [ ] Read current GTM container setup (or code-based tags)
- [ ] List all events currently firing
- [ ] Check: are all macro conversions tracked?
- [ ] Check: is Consent Mode v2 configured?
- [ ] Check: are UTMs being captured?
- [ ] Check: internal traffic filtered?
- [ ] Check: referral exclusions set?
- [ ] Report gaps with priority: Critical / Warning / OK

Ask after the report: "Shall I close the gaps right away? Yes / no"

---

## Mode C: Just UTMs

Use when: user chose "Just UTM conventions" (Answer C to Question 1).

Always use UTM parameters on links from external sources. Never use UTMs on internal links.

### Standard Format
```
?utm_source=meta&utm_medium=paid_social&utm_campaign=launch-2026&utm_content=variant-a&utm_term=keyword
```

### Parameter Definitions

**utm_source** - Where the traffic comes from (platform/publisher):
- `meta` - Facebook/Instagram ads
- `google` - Google Ads
- `linkedin` - LinkedIn ads or organic
- `newsletter` - Email newsletter
- `partner` - Partner referral
- `organic` - Organic social (use with utm_medium=social)

**utm_medium** - Type of channel:
- `paid_social` - Paid social ads
- `paid_search` - Google Search Ads
- `email` - All email campaigns
- `social` - Organic social posts
- `referral` - Referral from another site
- `affiliate` - Affiliate links
- `display` - Display/banner ads

**utm_campaign** - Campaign name (use hyphens, no spaces, lowercase):
- `launch-2026`
- `spring-sale`
- `q1-brand-awareness`
- `retargeting-warm`

**utm_content** - Creative variant or link identifier:
- `variant-a` / `variant-b` - for A/B testing
- `cta-hero` / `cta-footer` - for link position testing
- `image-lifestyle` / `image-product` - for creative testing

**utm_term** - Keyword (paid search only):
- The actual search keyword

### UTM Builder Workflow
1. Create a shared UTM spreadsheet (Google Sheets)
2. One row per link
3. Auto-generate UTM string with a CONCATENATE formula
4. Copy-paste into ad platforms - never type manually

---

## Mode D: GDPR Compliance Check

Use when: user chose "GDPR compliance check" (Answer D to Question 1).

### Consent Mode v2 (required for EU users since March 2024)

Google requires Consent Mode v2 for all EU-targeting. This is not optional.

**Two modes:**
1. **Basic Consent Mode** - No data sent until user consents. Simpler, less data, recommended for smaller products.
2. **Advanced Consent Mode** - Cookieless pings sent before consent, modeled data fills the gap. More data, more complex setup. Recommended when traffic volume is high.

**GDPR Compliance Checklist:**
- [ ] Consent banner appears BEFORE any tracking fires
- [ ] Reject button is as prominent as accept button
- [ ] No pre-ticked boxes
- [ ] Partial consent supported (analytics yes, marketing no)
- [ ] Consent is easily reversible
- [ ] Consent Mode v2 configured in GTM (consent initialization tag)
- [ ] All GTM tags set to "Wait for consent"
- [ ] Test: consent denied = no GA/Meta calls fire
- [ ] Test: consent granted = all calls fire correctly
- [ ] Cookie policy page exists and is linked from banner

**What you CAN track without consent:**
- Basic server-side analytics (no cookies, no fingerprinting)
- Aggregate page view counts
- Technical performance metrics

**What you CANNOT track without consent:**
- Google Analytics cookies
- Meta Pixel cookies
- Any cross-site tracking
- User-linked events

### Implementation Order
1. Install cookie consent tool (e.g., Cookiebot, Usercentrics, or cookie-consent-js)
2. Configure Consent Mode v2 in GTM (consent initialization tag)
3. Set all tags to "Wait for consent" in GTM
4. Test with consent denied - verify no GA/Meta calls fire
5. Test with consent granted - verify all calls fire correctly

---

## GA4 Standard Events Reference

These are pre-defined by Google and auto-reported in GA4:

| Event | When to fire |
|---|---|
| `page_view` | Every page load (automatic in GA4) |
| `scroll` | User scrolls 90% of page |
| `click` | Outbound link clicks |
| `sign_up` | User creates an account |
| `login` | User logs in |
| `purchase` | Completed transaction |
| `begin_checkout` | Checkout started |
| `add_to_cart` | Item added to cart |
| `search` | Internal site search |
| `share` | Content shared |
| `file_download` | File downloaded |

---

## Dashboard Design Principles

Only build dashboards around decisions you actually make.

### Max 5-7 Metrics Per Dashboard

**Acquisition Dashboard**
- Sessions by channel (source/medium)
- New users
- Bounce rate
- UTM campaign performance

**Activation Dashboard**
- Signup rate (sessions to signups)
- Form completion rate
- Time to first key action

**Revenue Dashboard**
- Conversion rate (trial to paid)
- MRR (from your billing tool)
- CAC by channel

**Retention Dashboard**
- Day 1 / Day 7 / Day 30 retention
- Churn rate
- Return visit rate

---

## Common Mistakes to Avoid

- Tracking everything "just in case" - leads to data overload and nothing actionable
- Firing events on button clicks instead of actual completions (track form submit success, not button click)
- Forgetting to filter internal traffic (your own team inflates numbers)
- UTM parameters on internal links (breaks session attribution)
- Not testing in GTM Preview mode before publishing
- Missing the thank-you page / success state for conversion events

---

## Related Skills

- `product-marketing-context` - Foundation for all marketing work
- `setup-gtm` - Full GTM container setup with GA4, Meta, PostHog, Consent Mode
- `ab-test-setup` - Structured A/B test design and event tracking
- `cro-audit` - Conversion rate audit that relies on tracking data
- `posthog-dashboard` - Product analytics dashboards in PostHog
- `growth-strategy` - AARRR funnel strategy that tracking supports
