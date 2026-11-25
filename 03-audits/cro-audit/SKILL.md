---
name: cro-audit
description: Audit conversion rate optimization — messaging clarity, trust placement, funnel flow, persuasion structure, copy effectiveness, signup flows, onboarding, forms, popups, paywalls, psychology principles, and A/B testing
model: sonnet
effort: medium
---

## Intake

Before starting the audit, ask the user:

1. **What page or flow should I audit?**
   - Homepage
   - Landing Page
   - Signup Flow
   - Pricing Page
   - Full Site

2. **What is your current conversion rate (if known)?**
   (If unknown, note that baseline is needed for measuring improvements.)

3. **What is the primary conversion goal?**
   - Signup
   - Purchase
   - Demo Request
   - Email Capture

Then proceed with Step 0.

---

## Step 0: Marketing Context laden

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# CRO Audit — Conversion Rate Optimization

This skill audits a project's conversion effectiveness — messaging clarity, persuasion structure, trust placement, funnel narrative, and copy quality. It identifies what's blocking conversions and fixes issues directly in the codebase.

No arguments needed. Just run `/cro-audit` and the skill scans the project automatically.

### How it differs from other audits
- **UX audit** = does the flow work? (behavioral outcomes, cognitive load)
- **UI audit** = does it look right? (visual polish, spacing, consistency)
- **CRO audit** = does it convert? (messaging, trust placement, funnel narrative, copy)

Reference sources:
- Joanna Wiebe / Copyhackers: conversion copywriting
- CXL Institute: evidence-based CRO
- Cialdini's Principles of Persuasion
- Schwartz's Levels of Awareness (Eugene Schwartz, Breakthrough Advertising)

---

## Step 0: Understand the project

Before auditing, read:
- `CLAUDE.md` / `README.md` for project context
- All page components (understand the page narrative)
- CTAs — copy, placement, frequency, visual weight
- Trust signals — testimonials, badges, guarantees, numbers
- Forms and conversion points
- Above-the-fold content (hero section)
- Post-conversion experience (confirmation, next steps)

Identify:
- **Primary conversion goal** (what's the one thing the visitor should do?)
- **Target audience awareness level** (unaware -> problem-aware -> solution-aware -> product-aware -> most aware)
- **Page narrative arc** (what story does the scroll tell?)
- **Trust stack** (what proof exists and where is it placed?)

---

## Step 1: Audit against CRO principles

Go through **each category** below. For every issue found, note the file, the specific principle violated, and the recommended fix. Rate severity as:
- **🔴 Critical** — likely killing conversions
- **🟠 Major** — measurably reducing conversion rate
- **🟡 Minor** — optimization opportunity

---

### Category 1: Value Proposition & Messaging

#### Above-the-Fold Clarity (5-Second Test)
> A stranger should understand what you offer, who it's for, and what to do next within 5 seconds.

**Check for:**
- Headline that's vague, clever, or jargon-heavy instead of clear
- Missing or buried subheadline that explains the benefit
- No clear CTA visible without scrolling
- Hero section that prioritizes aesthetics over clarity
- Headline that could belong to any competitor (not specific enough)

**Fix pattern:** Headline = clear benefit. Subheadline = how/for whom. CTA = obvious next step. All three visible above the fold.

---

#### Benefit-Over-Feature Framing
> Users care about outcomes, not capabilities. Features tell, benefits sell.

**Check for:**
- Feature lists without "so that..." outcomes
- Technical capabilities described without user impact
- "What it does" without "what it means for you"
- Product-centric language instead of user-centric language

**Fix pattern:** For every feature, ask "so what?" — rewrite it as the outcome the user gets. "AI-powered analysis" → "Understand what is really going on"

---

#### Specificity & Proof
> Concrete numbers beat vague claims. Specificity signals credibility.

**Check for:**
- Vague claims ("many customers", "improved results", "fast progress")
- Round numbers that feel made up vs. specific numbers that feel real
- Claims without supporting evidence or source
- Superlatives without proof ("the best", "unique")

**Fix pattern:** Replace vague claims with specific numbers, timeframes, or cited research. "Many customers" -> "2,400+ customers since 2024". If you can't prove it, soften it or remove it.

---

#### Objection Pre-emption
> Address the top 3-5 objections before they become reasons not to convert.

**Check for:**
- Common objections unaddressed (price, time, privacy, "does it work?", "is it for us?")
- FAQ buried at the bottom instead of addressing objections inline where they arise
- Missing "who this is for / not for" clarity
- No risk reversal near conversion points

**Fix pattern:** Identify top objections for the target audience. Address each one near the point in the page where it naturally arises — not just in the FAQ.

---

#### Headline "So What?" Test
> Read every headline. Ask "so what?" — if you can't answer with a concrete benefit, rewrite.

**Check for:**
- Section headlines that describe the section ("Unsere Funktionen") instead of stating a benefit
- Headlines that are labels, not value propositions
- Headlines that don't create curiosity or communicate a promise
- H2s that work as internal navigation but don't sell

**Fix pattern:** Every section headline should answer "why should I keep reading?" — turn labels into promises. "Funktionen" -> "Alles, was ihr braucht — an einem Ort"

---

### Category 2: Trust & Credibility at Decision Points

#### Trust Signal Placement
> Trust signals must appear BEFORE the conversion point, not after. Users need confidence before they commit.

**Check for:**
- Testimonials, badges, or guarantees placed after the main CTA or form
- Trust signals only at the bottom of the page (most users never scroll there)
- No trust signals near the primary conversion point
- Social proof section far from any CTA

**Fix pattern:** Place at least one trust signal within 200px (visually) of every CTA. Testimonials before the pricing section. Guarantees next to the form.

---

#### Social Proof Quality
> Not all social proof is equal. Specific, relatable, outcome-focused testimonials convert best.

**Check for:**
- Generic testimonials ("Toll!", "Super App!", "Hat uns geholfen")
- Testimonials without specific outcomes or transformations
- Anonymous quotes with no name/initials (feels fake)
- All testimonials saying the same thing (no variety of benefits)
- Missing context (relationship stage, how long they've used it)

**Fix pattern:** Each testimonial should contain: (1) the before state, (2) what they did, (3) the specific outcome. Different testimonials should address different objections/benefits.

---

#### Authority Signals
> Research citations, expert endorsements, and methodology references build credibility.

**Check for:**
- Claims about effectiveness without citing research
- No mention of methodology or scientific basis
- Missing "as seen in" / press mentions / expert endorsements
- No credentials or authority markers for the team/product

**Fix pattern:** Cite specific research (author, year). Mention the methodology. Add expert endorsements where available. "Based on the Gottman method" beats no citation.

---

#### Risk Reversal
> Reduce perceived risk at the moment of conversion. Guarantees, free trials, and "no commitment" language reduce friction.

**Check for:**
- No guarantee or risk reversal near CTA/form
- Missing reassurance such as "free", "no commitment", "cancel any time" near conversion points
- Price presented without value anchoring or risk mitigation
- No free tier or trial mentioned

**Fix pattern:** Add risk-reversal copy directly next to the CTA. "Start free — no credit card needed" is more effective than a standalone CTA.

---

#### Proof Hierarchy
> Numbers > Named testimonials > Logos > Generic claims. Use the strongest proof available.

**Check for:**
- Generic claims used where specific numbers exist
- Testimonials used where quantitative results could be shown
- Missing the strongest available proof type
- Proof elements not escalating in strength down the page

**Fix pattern:** Lead with the strongest proof. Use numbers where possible, named testimonials where not, and save generic claims for supporting roles only.

---

### Category 3: Conversion Funnel & Page Flow

#### Content Narrative Arc
> The page should tell a story: Problem -> Agitation -> Solution -> Proof -> CTA.

**Check for:**
- Page that jumps straight to features without establishing the problem
- Missing "agitation" — not connecting with the pain/desire emotionally
- Solution presented before the problem is felt
- Proof and CTA disconnected from the narrative
- Sections in an order that doesn't build persuasion momentum

**Fix pattern:** Restructure page flow: (1) Hook — connect with the desire/problem, (2) Agitate — deepen the emotional resonance, (3) Solution — present your answer, (4) Proof — back it up, (5) CTA — make the next step clear and easy.

---

#### CTA Cadence
> A CTA should follow every persuasion block. Don't make users scroll back to convert.

**Check for:**
- CTA only in hero and footer (nothing in between)
- Long persuasion sections (features, testimonials, approach) without a CTA following them
- User must scroll up to find how to convert
- More than 2 full screen heights between CTAs

**Fix pattern:** Add a CTA (or at least a text link) after every major persuasion section. Vary the format: primary button, text link, inline CTA, sticky bar.

---

#### CTA Copy
> CTA text should be action-oriented, benefit-loaded, and ideally first-person.

**Check for:**
- Generic CTA text ("Submit", "Send", "Next", "Learn more")
- CTA that describes the action but not the benefit
- All CTAs identical regardless of context
- CTA that creates uncertainty about what happens next

**Fix pattern:** CTA = action + benefit or outcome. "Start your free trial" > "Submit". "See your results" > "Continue". The best CTAs answer "what do I get when I click this?"

---

#### Friction Audit
> Every field, click, and decision point is a potential drop-off. Minimize friction ruthlessly.

**Check for:**
- Forms with too many required fields
- Fields that ask for info not needed at this stage
- No progressive disclosure (showing everything at once)
- Required account creation before value delivery
- Multi-step forms without progress indication
- Form fields without clear labels or placeholder guidance

**Fix pattern:** Remove every field that isn't strictly necessary. Use progressive disclosure. Delay account creation until after value delivery. Show progress in multi-step flows.

---

#### Exit / Soft Conversion
> Not everyone is ready to convert. Offer a smaller commitment for those not ready for the primary CTA.

**Check for:**
- Only one conversion option (all or nothing)
- No newsletter signup, lead magnet, or "follow us" as fallback
- Missing micro-conversions for visitors not ready for the main CTA
- No email capture for retargeting

**Fix pattern:** Offer a soft conversion alongside the primary CTA. Newsletter signup, free resource, "remind me later", or social follow. Capture the interest of non-converters.

---

#### Post-Conversion Experience
> What happens after someone converts? Confirmation delight reduces buyer's remorse and increases referrals.

**Check for:**
- A bland confirmation page or message ("Thanks for signing up.")
- No next steps after conversion
- No social sharing prompt after conversion
- Missing "what happens now" clarity
- No referral hook or viral loop

**Fix pattern:** Post-conversion should (1) confirm and celebrate, (2) set expectations ("you will hear from us within 24 hours"), and (3) suggest a next step (share, explore, invite).

---

### Category 4: Persuasion Psychology

#### Commitment Escalation (Foot-in-the-Door)
> Small yeses lead to big yeses. Start with micro-commitments before asking for the main conversion.

**Check for:**
- First ask is too big (registration, purchase, long form)
- No micro-commitments before the main conversion point
- Survey/quiz not used as engagement before conversion
- No interactive elements that create investment before the ask

**Fix pattern:** Build a ladder of small yeses: read -> interact -> micro-commit -> convert. Quiz, survey, calculator, free preview — anything that creates engagement before the ask.

---

#### Reciprocity
> Give value before asking. People feel compelled to return favors.

**Check for:**
- Asking for email/data without offering value first
- No free content, preview, or tool before the conversion ask
- Gated content that gates too early (before any value is delivered)
- Value proposition only described, never demonstrated

**Fix pattern:** Lead with value. Free content, useful preview, actionable tip, or interactive tool before the ask. "Here's something useful for free — and here's how we can help further."

---

#### Anchoring
> The first number or reference point shapes all subsequent judgments. Use this for pricing and value perception.

**Check for:**
- Price presented without context or comparison
- No "value of" framing before price reveal
- Missing price anchoring (comparable alternatives, cost of the problem)
- No "per day" or "per week" reframing of monthly/annual prices

**Fix pattern:** Before showing the price, establish what the alternative costs. Frame the price as an investment, not a cost. "Less than a coffee a day."

---

#### Loss Aversion Framing
> People are more motivated by what they might lose than what they might gain.

**Check for:**
- All messaging focused on gains, none on what they'd miss
- No "without this..." or "imagine if..." counter-framing
- Missing urgency (authentic, not manufactured)
- No FOMO elements for genuinely limited offers

**Fix pattern:** Balance gain framing with loss framing. "What if you had had this a year ago?" But NEVER use manipulative dark patterns or fake scarcity.

---

#### Paradox of Choice
> More options = more decision paralysis. Fewer, clearer options convert better.

**Check for:**
- More than 3 pricing tiers
- Feature comparison tables with too many rows
- Multiple CTAs competing for attention on the same screen
- No recommended / highlighted option among choices
- Decision points without a clear default or recommendation

**Fix pattern:** Limit to 2-3 options. Highlight the recommended one visually. Use "Most popular" or "Empfohlen" badges. Make the best choice obvious.

---

## Step 2: Report findings

Present findings grouped by severity:

```
## CRO Audit Results

### 🔴 Critical — likely killing conversions
| Issue | CRO Principle | File | Recommended Fix |
|-------|--------------|------|-----------------|
| ... | ... | ... | ... |

### 🟠 Major — measurably reducing conversion rate
| Issue | CRO Principle | File | Recommended Fix |
|-------|--------------|------|-----------------|
| ... | ... | ... | ... |

### 🟡 Minor — optimization opportunity
| Issue | CRO Principle | File | Recommended Fix |
|-------|--------------|------|-----------------|
| ... | ... | ... | ... |

### ✅ Well done
- [list what the project already does well for conversions]
```

Ask the user: **"Shall I fix the issues? All of them, or only the critical ones?"**

---

## Step 3: Fix issues

Apply fixes directly in the codebase. For each fix:
- Reference which CRO principle it addresses in a brief code comment (only if non-obvious)
- Prioritize fixes on the primary conversion funnel
- Never break existing functionality
- Follow the project's existing code style and design system
- Respect brand voice and tone — no dark patterns, no hype, no cringe

---

## Step 4: Summary

```
CRO Audit Complete!

✅ [N] issues fixed
⚠️ [N] issues flagged for manual review

Principles applied:
- [list which CRO principles were most relevant]

Top 3 highest-impact changes:
1. [change] — [which principle, expected impact]
2. [change] — [which principle, expected impact]
3. [change] — [which principle, expected impact]

Recommended next steps:
- A/B test headline variations (current vs. benefit-focused)
- Heatmap analysis on CTA placement (PostHog/Hotjar)
- User testing: 5-second test on hero section with strangers
- Track micro-conversion funnel (scroll depth -> CTA clicks -> form starts -> form completions)
```

---

## Rules

- **Audit the conversion path**, not just aesthetics or usability
- Focus on the **primary conversion goal** first
- Reference specific CRO principles by name — this creates shared vocabulary with marketing
- Respect the project's brand voice — CRO improvements should feel native, not bolted on
- **Never add dark patterns** — no fake urgency, no manipulative scarcity, no confirm-shaming, no hidden costs
- Copy recommendations should match the project's tone and language
- German UI text for German-language projects
- Fixes should be practical and implementable, not theoretical
- Follow the project's existing code style and component patterns
- Every recommendation should have a clear "why" tied to conversion psychology

---

## Specialized CRO Areas

### Signup Flow Optimization

**When to use:** Signup completion below 40%, drop-off at registration step, multi-step signup needs optimization.

Use this section for the registration step only. For what happens AFTER signup, see Onboarding Optimization below.

#### Core Principle

**Every field you add reduces completion by 5-10%.** Ask for the MINIMUM required to get started. Get everything else later.

#### Field Reduction Rules

**Keep at signup (absolute minimum):**
- Email address
- Password (or passwordless/social login)
- That's it for most products

**Move to onboarding (collect after first login):**
- Name, company name, role/job title, team size, use case or goals, phone number, profile photo

**Remove entirely:**
- Address (unless payment required at signup)
- "How did you hear about us" (use analytics instead)
- Preferences that can be inferred from behavior

**Common field reduction wins:**

| Field | Why it's usually unnecessary at signup |
|-------|---------------------------------------|
| First name + Last name as separate fields | Combine into one "Name" field |
| Phone number | 22% of users abandon over phone field |
| Password confirmation | Use show/hide password toggle instead |
| Date of birth | Only collect if legally required |

#### Social Login vs. Email Decision

Not a binary choice - offer both.

| Product type | Primary | Secondary |
|-------------|---------|-----------|
| Consumer B2C | Google / Apple | Email |
| B2B SaaS | Email | Google (work accounts) |
| Healthcare | Email | None (trust/privacy) |
| Community | Email | None (trust/age-appropriate) |

Always offer "Continue with Google" AND "Use email instead" - never force one path.

#### Progressive Profiling Framework

Spread data collection across the first week:

- **Session 0 - Signup (30 seconds max):** Email + password or social login
- **Session 1 - First login (2-3 minutes):** Name + primary role to personalize
- **Session 2-3 - In-app prompts (5-10 seconds each):** Context-triggered data (company size when they try team features)
- **Week 1 - Email sequence:** "Complete your profile" with incentive

**Rules:** Never block core functionality for missing profile data. Show value BEFORE asking for more information. Max 2 questions per in-app prompt.

#### Signup Friction Audit Checklist

**Speed:**
- [ ] Can a user complete signup in under 60 seconds?
- [ ] Fewer than 4 required fields?
- [ ] "Sign in with Google/Apple" offered?
- [ ] Page loads under 2 seconds?

**Clarity:**
- [ ] Value proposition visible on the signup page itself?
- [ ] CTA button specific ("Create free account" vs "Sign up")?
- [ ] Password policy visible BEFORE they type?
- [ ] Error messages specific and helpful?

**Trust:**
- [ ] Page on your own domain (not a third-party auth page)?
- [ ] Security/privacy reassurance near the form?
- [ ] "No credit card required" visible if true?

**Technical UX:**
- [ ] Inline validation enabled (on blur for email, on keypress for password strength)?
- [ ] Form preserves data on error? (Never clear the form on failed submit)
- [ ] Email field type="email" (triggers right keyboard on mobile)?

#### Error Handling UX

- Show errors INLINE next to the specific field, not as a banner at the top
- Error message format: "[Field] [what's wrong]. [How to fix it]."
  - Good: "Email is already registered. Sign in instead or reset your password."
  - Bad: "Invalid input"
- Validate EMAIL on blur, PASSWORD on keypress, REQUIRED FIELDS only on submit
- Show green checkmark when a field is successfully filled
- **Never clear the form on error** - losing all their work is the #1 cause of permanent abandonment

#### Signup Benchmark Metrics

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Signup completion rate | <25% | 40-50% | 60-70% | >75% |
| Time to complete signup | >3 min | 90 sec | 60 sec | <45 sec |
| Email verification rate | <50% | 65% | 80% | >90% |
| Social login adoption | <10% | 20-30% | 40% | >50% |

---

### Onboarding Optimization

**When to use:** Activation rate below 30%, high churn in first 7-14 days, users sign up but never complete first key action.

This section starts the moment the user logs in for the first time.

#### Core Concept: Time-to-Value

Users decide in their first session whether your product is worth their time. Get them to the aha moment fast.

| Product type | Target time-to-value |
|-------------|---------------------|
| Simple consumer app | Under 2 minutes |
| B2B SaaS (simple) | Under 5 minutes |
| B2B SaaS (complex) | Under 15 minutes |
| Enterprise software | Under 30 minutes first session |

#### Finding Your Aha Moment

The aha moment is the specific action that correlates most strongly with long-term retention.

**Method 1 - Retention analysis:** Pull data on users still active after 30 days. Look at what those users all did in their first session. The common action = your aha moment candidate.

**Method 2 - Interview power users:** Ask "What was the moment you realized this product was for you?"

**Method 3 - Funnel analysis:** Find the action with highest correlation to 7-day and 30-day retention.

**Write it as:** "User has completed [specific action] for the first time."

**Aha moment examples:**

| Product | Aha Moment |
|---------|------------|
| Slack | Team sends 2000+ messages |
| Dropbox | User puts a file in the Dropbox folder |
| Newsletter tool | Sending first email to at least 10 subscribers |
| CRM | Adding first 5 contacts and logging first activity |

#### Activation Metrics Framework

| Milestone | Action | Target completion | Target timeframe |
|-----------|--------|------------------|-----------------|
| Setup complete | Profile/account configured | 80% of signups | Day 0 |
| First value | Core aha moment action done | 50% of signups | Day 1 |
| Habit seed | Core action done 3x | 30% of signups | Week 1 |
| Retained | Active in second week | 25% of signups | Week 2 |

**Activation benchmarks:**

| Metric | Poor | Average | Good | Excellent |
|--------|------|---------|------|-----------|
| Day 1 activation | <15% | 25-35% | 45-55% | >60% |
| Week 1 retention | <20% | 30-40% | 50-60% | >65% |
| Month 1 retention | <10% | 20-30% | 40-50% | >55% |

#### Onboarding Patterns

**Pattern 1: Checklist / Progress Bar** - Best for complex products with required setup steps.
- 4-6 steps max, each under 2 minutes
- First step completable in 30 seconds (builds momentum)
- Don't gate the product behind the checklist
- Step naming: use action verbs + specific outcome ("Connect your calendar" not "Setup")

**Pattern 2: Empty State Design** - Best for content-creation or data-display products.
- Use sample/demo data to illustrate value
- Single, prominent CTA: "Create your first [thing]"
- Formula: "Here's where your [things] will appear. [Value description]. [CTA button]"

**Pattern 3: Guided Tooltip Tour** - Best for products with familiar UI where users need orientation.
- 3-5 tooltips max, each tooltip one idea, max 15 words
- Allow skip at any point, show progress ("2 of 5")

**Pattern 4: Welcome Video** - Best for visual products or complex workflows.
- Under 90 seconds (60 is better)
- Show the OUTCOME, not every click
- Always optional with a clear "skip"

**Pattern 5: Interactive Demo** - Best for high learning-curve products.
- The demo action should be the aha moment action
- Must end with clear onward path to real use

#### Email Onboarding Sequence (7-Day)

- **Email 1 - Immediate (0-5 min):** Welcome + ONE CTA to complete first step
- **Email 2 - Day 1 (if not activated):** Reminder + specific benefit they're missing
- **Email 3 - Day 3:** Social proof + one power feature highlight
- **Email 4 - Day 5 (if not activated):** Offer help, remove obstacles
- **Email 5 - Day 7:** Weekly summary + tip they haven't tried

Segment by activation status. Users who ARE activated should get value emails, not "complete setup" emails.

#### Retention Habit Formation

**The Habit Loop (Hooked Model):** Trigger -> Action -> Variable Reward -> Investment

**Designing for habit:**
1. Identify the correct frequency (daily / weekly / on-demand)
2. Build external triggers into onboarding (notifications, integrations)
3. Reduce friction for repeat use
4. Create investment early (import data, invite teammates, create first content)

Investment creates switching cost and increases future value.

---

### Form Optimization

**When to use:** Lead capture forms, contact forms, demo requests, checkout, any form with low completion rates.

Core rule: **Every field reduces completion by 5-10%.** Start with the minimum. Add fields only when the business case is clear.

#### Field Audit

For every field, ask:
1. Do I NEED this to proceed?
2. Can I get this later?
3. Can I infer it? (from email domain, IP, browser, or account data)
4. Is this for the user or for us?

**Fields almost always worth removing:**
- Phone number (unless calling is the next step)
- "How did you hear about us?" (track UTMs instead)
- Job title (unless B2B with very specific targeting)
- Date of birth (unless legally required)
- Confirm email / confirm password (use show/hide toggle instead)
- Separate first name + last name (use full name unless needed separately)

**Minimum viable forms:**

| Form Type | Minimum Fields |
|---|---|
| Newsletter signup | Email only |
| Lead capture | Name + Email |
| Demo request | Name + Email + (optional) Company |
| Waitlist | Email only |
| Contact form | Name + Email + Message |
| Account creation | Email + Password |

#### Layout Best Practices

- **Single column always** - never place fields side by side on mobile
- **Minimum input height:** 44px (mobile touch target requirement)
- **Labels above fields** - never inside as placeholder text only (placeholder disappears on typing)
- **Field order:** Start easy (name, email), end hard (budget, payment)
- **Required fields:** mark with asterisk (*); better yet, mark optional ones as "(optional)"

#### Submit Button Copy

The submit button is the most important text on the form.

| Form Type | Bad | Better |
|---|---|---|
| Newsletter | Submit | Join the newsletter |
| Lead gen | Send | Get my free guide |
| Demo | Submit | Book my 20-min demo |
| Signup | Register | Start my free trial |
| Waitlist | Join | Reserve my spot |

Add a one-line trust signal directly below the submit button: "No credit card required" / "Cancel anytime" / "Takes less than 2 minutes"

#### Multi-Step Forms

Use multi-step when a form has more than 5-6 fields.

- 2-4 steps is the sweet spot; 5+ starts feeling like work
- Always show a progress bar or step counter ("Step 2 of 3")
- Step 1: lowest friction (email, name)
- Last step: payment or detailed requirements
- Back button must work and restore entered data
- Never lose data if user navigates away (warn them)

#### Validation UX

- Validate each field when user LEAVES it (on blur), not on submit
- Show green checkmark for valid fields
- Error messages: specific ("Enter a valid email address"), helpful, human, positioned below the field
- Password strength indicator as they type
- **Never clear the form on submit error**
- Never show all errors only after submit

#### Smart Defaults

- Country from IP geolocation
- Phone country code from IP
- Email from URL parameter (personalized links)
- Plan/tier from pricing page selection

**Dropdown vs. Radio vs. Text:**

| Option count | Best input type |
|---|---|
| 2 options | Radio buttons |
| 3-5 options | Radio buttons |
| 6-12 options | Dropdown select |
| 13+ options | Searchable dropdown (combobox) |

#### Mobile-Specific

- Use correct `type` attribute: `type="email"`, `type="tel"`, `type="number"`
- Use `autocomplete` attributes to enable autofill
- Sticky footer CTA on long forms

---

### Popup & Overlay Optimization

**When to use:** Designing or auditing popups, modals, exit-intent overlays, banners.

#### When Popups Work vs. Fail

**Work when:** User has consumed value first, offer is relevant to what they were doing, popup appears once not on every visit.

**Fail when:** They appear immediately on page load, block mobile content, appear on every visit, offer is generic.

**Google penalty warning:** Popups that cover content on mobile on first load are penalized in mobile search rankings. Never use full-screen overlays on mobile - use banners instead.

#### Popup Trigger Types

| Trigger | When to Use | Benchmark Conversion |
|---------|-------------|---------------------|
| Exit intent | Last-chance capture when mouse moves to close/back | 2-5% of triggers |
| Scroll-triggered (50-75% depth) | User is engaged with content | 1-3% of impressions |
| Time-delayed (15 sec min, 30 sec better) | Supplement to exit intent | 1-2% of impressions |
| Click-triggered (modal) | User actively chose to engage | 10-40% (user initiated) |
| Sticky bar | Persistent, non-blocking promotions | 0.5-2% but cumulative |

**Mobile note:** Exit intent does not work on mobile. Use scroll-triggered or time-delayed instead.

#### UX Rules (Non-Negotiable)

1. **Always easy to close:** Visible X button, clicking outside dismisses, ESC key closes
2. **Never show same popup twice in one session**
3. **Frequency cap:** Max 1 popup per page visit
4. **Mobile:** Never full-screen overlay. Use bottom banner or slide-in instead
5. **Never block content before user has engaged**
6. **Respect close signals:** Suppress for at least 7 days after close (30 days better)
7. **No dark patterns:** No shame-based dismiss text ("No, I don't want more sales")

#### Popup Copy Structure

Popup copy must be extremely concise. Users decide in under 2 seconds.

1. **Headline (1 line, benefit-focused):** What they get, not what you want
2. **Subline (1 sentence max, optional):** Specificity or urgency
3. **CTA button (2-4 words):** Action verb + the thing ("Get the Checklist", "Claim Discount")
4. **Dismiss text:** "No thanks" or "Maybe later" - neutral, no shaming

**Headline formulas:**
- "Get [Specific Thing] for Free"
- "Don't Leave Without Your [Resource]"
- "One Quick Question Before You Go"

**CTA button copy - what works:** "Get the Free Template" / "Claim My Discount" / "Send Me the Guide"
**CTA button copy - what does not work:** "Submit" / "Click Here" / "Subscribe"

#### A/B Test Priorities for Popups

| Priority | Variable | What to Test |
|----------|----------|-------------|
| 1 | Offer | Discount vs. lead magnet vs. free trial |
| 2 | Timing | 15s vs. 30s vs. exit intent |
| 3 | Headline | Benefit framing vs. curiosity vs. urgency |
| 4 | CTA text | Action-verb variations |
| 5 | Design | Minimal vs. image-heavy |

At least 200 conversions per variant before declaring a winner.

---

### Upgrade & Paywall Optimization

**When to use:** Optimizing free-to-paid conversion, feature gates, trial expiry flows, in-app upgrade prompts.

#### Core Principle

**Show the upgrade prompt when the user has just experienced value - not when they are frustrated by a wall.**

Wrong: User tries to do something, gets blocked, feels annoyed, leaves.
Right: User just achieved something, sees what more they could do, upgrades.

#### Trigger Types

| Trigger | Best Practice | Expected Conversion |
|---------|--------------|-------------------|
| Feature gate | Show preview/blur of locked feature. Copy focus: what it does for them | Medium |
| Usage limit (at 80%) | "You've used 4 of your 5 free exports. Upgrade to get unlimited." | High |
| Usage limit (at 100%) | "You've reached your free limit. Continue with [Plan Name]." Never cut off mid-task. | Medium |
| Trial - day 7 of 14 | Frame around value already gotten. "You've [done X] in your first 7 days." | Medium |
| Trial - day 12 | Warning + value framing | High |
| Trial - day 14 | Final reminder + what they'll lose | High |
| Value milestone (best) | Celebrate first, then show what's next. Highest conversion because user is in positive state. | Highest |
| Onboarding completion | Only if product has strong free tier AND upgrade is genuinely relevant. Usually wait. | Low-Medium |

#### Messaging Framework

Structure every upgrade prompt:

1. **Acknowledge what they've done:** "You've created 12 projects this month."
2. **Show the gap:** "Upgrade to keep going with unlimited projects."
3. **Make it specific:** "Unlimited exports, custom branding, and team sharing." (Not "All Pro features")
4. **Social proof (optional):** "Join 2,300+ teams who upgraded."
5. **Clear CTA:** "Upgrade Now - plans from EUR X/month" / "Keep Going with Pro"
6. **Secondary option:** "Or continue on Free (limited to X)"

#### Pricing Page Structure

1. Header: Value promise (not just "Pricing")
2. Toggle: Monthly / Annual (show annual savings - "Save 20%")
3. Tiers: Maximum 3. Mark one as "Most Popular"
4. Feature comparison: Table format, max 10-12 features, use lock icon or dash (not X) for locked features
5. FAQ: Answer 5 most common objections
6. Trust signals: Money-back guarantee, cancelation policy
7. CTA at bottom: Repeat primary CTA after FAQ

**Tier naming:** Verb-based (Starter/Grow/Scale) or Persona-based (Solo/Team/Business). Avoid Bronze/Silver/Gold or "Basic."

**Annual vs. monthly:** Always offer annual with 15-20% discount. Show monthly equivalent clearly.

#### Anti-Patterns to Avoid

- **Nagging:** Showing upgrade prompts more than once per session for the same trigger
- **Blocking critical workflow:** Never prevent users from accessing data they already created
- **Removing features used in trial:** Let them keep it read-only - never take away what they built
- **Upgrade prompts during onboarding:** Too early, user hasn't experienced value
- **Dark patterns:** Pre-checked annual plans, hidden cancellation, "gotcha" trial-end charges
- **Generic prompts:** "You've reached your limit. Please upgrade." - no context, no value framing

#### In-App Upgrade UX Patterns

- **Modal:** For feature gates and milestones. Medium size, easy to dismiss.
- **Inline banner:** For usage limits approaching. Soft color, non-blocking, top of relevant feature view.
- **Sidebar countdown:** For trial period. Subtle, always visible during trial, remove immediately on upgrade.
- **Full upgrade page:** For expired trials. Show value summary of what they accomplished.

#### Upgrade Metrics to Track

| Metric | What It Tells You |
|--------|-----------------|
| Feature gate click-to-upgrade rate | Effectiveness of gate messaging |
| Trial-to-paid conversion rate | Overall trial health |
| Usage limit upgrade rate | How well limit prompts convert |
| Upgrade by trigger type | Which moments convert best |
| Upgrade page conversion rate | Pricing page effectiveness |
| Plan mix (% on each tier) | Whether tier positioning is right |

---

## Persuasion Psychology

### Jobs-to-be-Done (JTBD)

People do not buy products. They hire products to do a job for them.

**The JTBD Formula:** "When [situation], I want to [motivation], so I can [desired outcome]."

**Three types of jobs:**
- **Functional:** the practical task (send invoices quickly, get paid faster)
- **Emotional:** how the user wants to feel (feel like a professional)
- **Social:** how the user wants to be perceived (clients see me as organized)

**Application:** Write hero copy that speaks to the job, not the feature. Use the customer's own language from interviews/reviews.

Bad: "Automated Invoice Generation with Custom Templates"
Good: "Send Your First Invoice in 2 Minutes. Look Like You've Been Doing This for Years."

---

### Cialdini's 6 Principles of Influence

#### 1. Reciprocity
People feel obligated to return favors. Give value first.

- Free tools (calculators, templates) before asking for signup
- Free content lightly gated or not at all
- Personalized free audits or reviews

Warning: Cheap lead magnets trigger skepticism, not reciprocity.

#### 2. Commitment and Consistency
Small yeses lead to bigger yeses. Once people commit, they stay consistent.

- Foot-in-the-door: newsletter -> free trial -> paid
- Progress bars ("You're 60% done setting up your account")
- Quiz flows that build toward a personalized recommendation
- Waitlists (commitment signals intent, increases launch conversion)

The first commitment must be low-cost and immediately valuable. Asking for credit card before delivering value violates this principle.

#### 3. Social Proof
People look to others to determine correct behavior, especially in uncertain situations.

| Type | When most powerful | Example |
|------|-------------------|---------|
| Numbers | When volume is impressive | "12,000+ teams use this" |
| Testimonials | When specificity matches visitor's situation | Quote from same role/problem |
| Logos | B2B / enterprise trust building | "Trusted by Spotify, Notion" |
| Ratings | High-consideration purchases | "4.8/5 from 2,400 reviews" |
| Case studies | Long sales cycles | "How [Company] reduced churn by 34%" |
| "Most popular" badges | Pricing pages | Highlighted recommended plan |
| Real-time activity | E-commerce, booking | "47 people viewing this now" |

Placement rules: Put social proof at decision points. Match proof to visitor's stage. Testimonials must be specific - "Great product!" is worthless.

#### 4. Authority
People defer to experts. Credentials and recognition lower skepticism.

- Founder credentials relevant to the problem
- Press logos ("As seen in TechCrunch, Forbes")
- Certifications and compliance badges (SOC 2, GDPR)
- Data citations ("Based on analysis of 2.4M data points")

Warning: "Industry-leading" and "best-in-class" are empty phrases that damage credibility. Show, don't tell.

#### 5. Liking
People say yes to those they like. Likability comes from similarity, familiarity, and genuine warmth.

- Show real team photos (not stock photos)
- Use conversational, human copy tone
- Mirror the customer's exact language from interviews
- Founder-led content performs differently than brand creatives

#### 6. Scarcity
People value what is rare or becoming unavailable.

- Quantity scarcity: "Only 3 spots left at this price"
- Time scarcity: "Offer ends Friday at midnight"
- Access scarcity: "Founding member pricing - never available again"

**WARNING - Fake Scarcity:** Countdown timers that reset, "Only 2 left" for digital products, "Price goes up tomorrow" that never does. This permanently destroys trust. Only use genuine scarcity.

---

### Cognitive Biases in Decision-Making

#### Loss Aversion
People feel losses ~2x as intensely as equivalent gains.

- Frame benefits as preventing loss, not acquiring gain
- "Stop losing $800/month to manual processes" > "Save $800/month"
- Free trial: frame end of trial as losing access

Copy patterns:
- "Every day without [product] costs you [X]."
- "You're already paying for this problem - just not with money."

#### Anchoring
The first number seen sets the reference point for all subsequent numbers.

- Show most expensive plan first on pricing page
- Show original price crossed out before discounted price
- Compare to more expensive alternatives
- ROI calculator before showing price
- Pricing page order: Premium (left/top) -> Standard -> Basic

#### Paradox of Choice
Too many options cause decision paralysis.

- Maximum 3-4 pricing tiers
- One clearly recommended option
- Default selections in multi-step forms
- If 4+ pricing tiers, test removing lowest or highest

#### Endowment Effect
People value things more once they own them or have invested in them.

- Free trials: let users actually set up and use the product (investment = attachment)
- Let users create real value before hitting the paywall
- Let users personalize before asking to upgrade

#### Peak-End Rule
People judge experiences by their peak moment and their final moment - not the average.

- Design one clear "aha moment" - the peak where the product delivers undeniable value
- End every interaction on a positive note (success state, encouragement, next step)
- Cancellation flow: end with hope ("Your data is saved. Come back anytime.")

---

### Application Matrix: Which Principles for Which Channel

| Principle | Landing Page | Ads | Email | Pricing Page | Signup Flow |
|-----------|-------------|-----|-------|-------------|-------------|
| Reciprocity | Free tool/resource | Lead magnet offer | Valuable content before ask | Free tier | Free trial |
| Commitment | Progress indicators | Sequential retargeting | Nurture series | Annual commitment | Step-by-step |
| Social Proof | Testimonials + logos | Social proof in copy | Case studies | Review counts | "X users like you" |
| Authority | Press logos, credentials | Founder/expert in ad | Expert byline | Compliance badges | Data reassurance |
| Liking | Founder story | Human face creative | Personal tone | Team photo | Friendly copy |
| Scarcity | Limited offer banner | Countdown in ad | Deadline reminder | Founding price | Last spots |
| Loss Aversion | Problem framing hero | "Don't miss" hook | Re-engagement | Cost of inaction | Trial expiry |
| Anchoring | Price comparison | Competitor price ref | Before/after value | Tier order | ROI preview |
| Paradox of Choice | Clear single CTA | One offer per ad | One ask per email | 3 tiers max | One step at a time |

---

### Psychology Quick Audit Checklist

**Landing Page:**
- [ ] Does hero speak to a job, not a feature?
- [ ] Is social proof placed at the decision point (just before CTA)?
- [ ] Is there one clear CTA (not 3-4 competing)?
- [ ] Is the first price shown the anchor (most expensive or full price before discount)?
- [ ] Does the copy use "you lose" framing where appropriate?

**Pricing Page:**
- [ ] Are tiers ordered from most to least expensive?
- [ ] Is there one clearly recommended tier?
- [ ] Is annual pricing shown with daily/monthly breakdown?

**Email:**
- [ ] Does the first email deliver value before asking for anything?
- [ ] Is there one clear CTA per email?
- [ ] Does urgency copy reference a real deadline?

**Ads:**
- [ ] Does the hook trigger loss aversion or curiosity?
- [ ] Is social proof in the first 3 seconds (video) or headline (static)?
- [ ] Is there one offer per ad?

---

## A/B Testing

### Phase 1: Experiment Design

#### The Hypothesis Formula

Every test must start with a structured hypothesis. No hypothesis = no test.

```
"If we [specific change], then [primary metric] will [increase/decrease] by [X%]
because [reason based on data or research]."
```

Examples:
- "If we change the CTA from 'Start Free Trial' to 'Try It Free - No Credit Card', then signup rate will increase by 15% because the current CTA creates friction by implying payment is required."
- "If we add a social proof counter below the hero headline, then trial signups will increase by 10% because visitors lack trust signals at the decision point."

**Hypothesis checklist - before running any test:**
- [ ] One variable changed (not multiple)
- [ ] Primary metric clearly defined and measurable
- [ ] Expected direction of change stated
- [ ] Minimum detectable effect defined
- [ ] Reason based on data or documented research - not a gut feeling

---

### Phase 2: Metric Selection

**Primary metric (one only):** The single metric the test is designed to move.

Common primary metrics:
- Landing page: Signup rate, Trial start rate
- Pricing page: Plan selection rate, Checkout start rate
- Onboarding: Completion rate, Feature activation rate
- Email: Click-through rate, Reply rate

**Guardrail metrics:** Metrics you track to ensure the primary improvement does not cause unintended damage.

Example: Testing shorter signup form -> primary = signup rate, guardrail = trial-to-paid conversion (shorter form may attract lower-quality leads)

**Do NOT track as primary:** Revenue (too noisy), LTV (months of lag), NPS (not sensitive enough)

---

### Phase 3: Sample Size and Duration

**Minimum Detectable Effect (MDE):**
- High-traffic pages (10k+ visitors/week): MDE of 5-10% is achievable
- Medium-traffic pages (1k-10k/week): MDE of 15-20% is realistic
- Low-traffic pages (<1k/week): Testing may not be feasible - use qualitative research instead

**Quick reference (baseline 5%, 80% power, 95% confidence):**
- Detect 1% absolute change (20% relative): ~19,000 per variant
- Detect 2% absolute change (40% relative): ~5,000 per variant
- Detect 3% absolute change (60% relative): ~2,300 per variant

**Test duration:**
- Minimum: 2 weeks (captures full weekly cycles)
- Maximum: 4 weeks (novelty effect distorts results after)
- **Never stop early because "it looks good" - this is p-hacking**

Duration formula: Required sample size / (weekly visitors / number of variants)

---

### Phase 4: Test Prioritization (ICE Framework)

| Criterion | Description | Scale |
|-----------|-------------|-------|
| Impact | How much will this move the needle if it works? | 1-10 |
| Confidence | How confident based on data/research? | 1-10 |
| Ease | How easy to implement? | 1-10 |

ICE Score = (Impact + Confidence + Ease) / 3

**RICE variant (adds Reach):** RICE Score = (Reach x Impact x Confidence) / Effort. Use when reach varies significantly between test ideas.

---

### Phase 5: Implementation Patterns

| Scenario | Recommended Approach |
|----------|---------------------|
| Quick copy test | Client-side JS |
| Pricing page test | Server-side / Feature flag |
| Full page redesign | URL split test |
| Personalization | Server-side |
| Low-traffic site | Qualitative research instead |

**Client-side (JS-based):** Quick iteration, no backend changes. Downside: flicker effect, affects Core Web Vitals, not suitable for SEO-critical pages.

**Server-side (feature flags):** User sees correct variant from first render. Use for pricing changes, checkout flows, performance-sensitive pages.

**URL split tests:** Route % of traffic to /page-v2 at CDN/reverse proxy level. Use for complete page redesigns. Requires canonical tags for SEO.

---

### Phase 6: Common Mistakes

1. **Stopping too early (p-hacking):** A test that "hits significance" on day 3 with 300 visitors is almost certainly noise. Commit to the calculated duration before starting.

2. **Testing too many variants:** A/B/C/D testing requires 3-4x more traffic. Unless you have 100k+ monthly visitors, stick to A/B.

3. **Not enough traffic:** If test needs 12 weeks to reach sample size, do qualitative research instead, make changes based on best practices, and measure before/after directionally.

4. **Changing tests mid-run:** Any change after a test starts invalidates the data. No new deployments, no parameter changes, no new traffic sources mid-test.

5. **Ignoring novelty effect:** Users click new things just because they're new. Run at least 2 full weeks and check if effect diminishes in week 2 vs. week 1.

6. **Multiple comparison problem:** 10 concurrent tests -> false positives by chance alone. Use Bonferroni correction or adjust significance threshold.

7. **Not segmenting results:** A test that shows no overall effect may show a strong effect for mobile users, new visitors, or paid traffic. Always break down results by key segments.

---

### Phase 7: Statistical Significance

**What p<0.05 actually means:** "If there were no real difference between A and B, we would see results this extreme by random chance only 5% of the time." It does NOT mean 95% proven.

**Always report confidence intervals:** "Variant B increased signups by 12% (95% CI: 3%-21%)" is useful. "Variant B increased signups by 12%" is incomplete.

**Use two-tailed tests by default** unless you have a strong prior reason to test only one direction.

---

### Phase 8: Result Reporting Template

```markdown
## A/B Test Report: [Test Name]

**Test ID:** [internal ID]
**Dates:** [start date] to [end date] ([X] days)
**Page / Feature:** [what was tested]

### Hypothesis
If we [change], then [metric] will [direction] by [X%] because [reason].

### Variants
- Control (A): [description]
- Variant (B): [description]

### Results

| Metric | Control (A) | Variant (B) | Change | Significance |
|--------|-------------|-------------|--------|--------------|
| [Primary metric] | X% | Y% | +Z% | p=0.03 (significant) |
| [Guardrail metric] | X% | Y% | +Z% | p=0.40 (not significant) |

**Sample size:** [N per variant]
**Confidence level:** 95%
**Statistical power:** 80%

### Confidence Interval
Primary metric: [point estimate]% (95% CI: [lower]% to [upper]%)

### Segment Breakdown
- Desktop: [result]
- Mobile: [result]
- New visitors: [result]
- Returning visitors: [result]

### Recommendation
[ ] Ship variant B - statistically significant improvement, no guardrail violations
[ ] Do not ship - no significant difference detected
[ ] Do not ship - variant B hurt guardrail metrics
[ ] Run follow-up test - interesting signal but inconclusive

### Learnings
[What did we learn about our users from this test, regardless of outcome?]
```

---

### A/B Test Quick Start Checklist

- [ ] Hypothesis written in full formula format
- [ ] Primary metric defined and tracked
- [ ] Guardrail metrics identified
- [ ] Sample size calculated
- [ ] Required duration calculated and committed to
- [ ] ICE score assigned
- [ ] Implementation approach chosen (client-side / server-side / URL split)
- [ ] Test end date locked in calendar - DO NOT check results before this date
- [ ] Analytics event tracking confirmed working for both variants
- [ ] QA: both variants render correctly on desktop + mobile

---

## Related Skills

- `/product-marketing-context` - Messaging and positioning context
- `/analytics-tracking` - Measure conversion improvements
- `/pricing-strategy` - Pricing models and tier design
- `/churn-prevention` - Reduce churn when onboarding fails
- `/email-marketing` - Full email strategy beyond onboarding sequences
- `/lead-magnets` - Lead magnet strategy for popup and soft conversion offers
- `/posthog-dashboard` - Set up activation funnel tracking
