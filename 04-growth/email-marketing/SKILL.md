---
name: email-marketing
description: Email marketing strategy — EDM vs Newsletter, onboarding sequences, campaigns, deliverability (SPF/DKIM/DMARC), content mix, SEO synergy via article delivery. Run /email-marketing to plan email strategy.
model: sonnet
effort: medium
---

## Step 0: Load Marketing Context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# Email Marketing - Strategy & Setup

Email marketing skill: EDM versus newsletter, five content types, onboarding sequences, deliverability, SEO synergy. Email ROI is roughly 36 for every 1 invested.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Step 1: Intake Questions

Ask the user ALL of the following before doing anything else. Wait for all answers.

```
Ask the user:
1. What do you need?
   A: Strategy from scratch
   B: Specific email sequence (Onboarding / Win-back / Campaign / Newsletter)
   C: Deliverability setup (SPF/DKIM/DMARC)
   D: Improve existing emails
2. Do you have an email tool? (Mailchimp / Resend / Loops / other?)
3. How many subscribers or users do you have?
```

Wait for all answers before proceeding.

---

## Step 2: Route Based on Answer

**If Mode A (Strategy from scratch):** go to Mode A below.

**If Mode B (Specific sequence):** go to Mode B below.

**If Mode C (Deliverability):** go to Mode C below.

**If Mode D (Improve existing emails):** go to Mode D below.

---

## Project Context

Before you start:
- Read any existing brand notes for the brand identity, audience and tone of voice
- Read the project's `CLAUDE.md` and `README.md`
- Identify existing email infrastructure (Mailchimp, Resend, Loops, etc.)

---

# MODE A: Strategy from Scratch

## A1: EDM vs. Newsletter

Ask the user: "Do you need marketing emails (EDM), a newsletter, or both?"

| Type | Purpose | When |
|-----|---------|------|
| **EDM** (Direct Marketing) | Conversion-focused; sales/promotion | Promotions, campaigns, announcements |
| **Newsletter** | Relationship building; long-term value | Industry insights, curated articles, regularly |

**Combine both:** EDM for push; newsletter for nurture. Different goals, different frequency.

## A2: Content Types

Walk the user through all 5 content types and ask which ones are relevant:

| Type | Purpose | Details |
|-----|---------|---------|
| **Onboarding** | Welcome plus first steps | 5-7 emails over 5-7 days; behaviour-triggered; lead to the aha moment |
| **Campaign** | Promotions, time-limited | Conversion or participation; clear CTA |
| **Announcement** | Product launch, major update | One-off; important news |
| **Feature update** | New features, improvements | Drive adoption; show what is new |
| **Blog/Newsletter** | Curated articles, insights | Regular contact; deliver value |

## A3: Frequency & Segmentation

Ask the user: "Which segments does your list have? (New users / Active / Inactive / Power users)"

| Segment | Strategy |
|---------|-----------|
| **New users** | A tight onboarding sequence that leads to the aha moment |
| **Active users** | Feature updates; newsletter; community |
| **Inactive users** | Re-engagement series; "We miss you" |
| **Power users** | Exclusive insights; beta access; referral incentives |

**Frequency recommendation:**

| Guideline | Details |
|------------|---------|
| **Baseline** | One high-quality email per week for most brands |
| **Best times** | Tue-Thu, 8-11 a.m. or 2-4 p.m. (recipient's local time zone) |
| **Segmentation** | New vs. loyal users need different frequency |
| **Quality > quantity** | Relevant, behaviour-triggered emails > calendar volume |

**Data:** ~36% send 1-3x/month; ~30% weekly; daily risks a high unsubscribe rate.

**[ ] Mode A Checklist:**
- [ ] EDM vs. newsletter strategy decided
- [ ] Relevant content types defined
- [ ] Segments identified
- [ ] Frequency per segment set
- [ ] Email tool selected and configured

---

# MODE B: Specific Sequence

Ask the user: "Which sequence do you need? (Onboarding / Win-back / Campaign / Newsletter)"

## B1: Onboarding Sequence

**If Onboarding:**

The most important email series. The goal: lead users to their first success.

| Email | Timing | Content |
|-------|--------|--------|
| **Welcome** | Immediately after signup | Thanks, what to expect, first step |
| **Quick win** | Day 1 | One concrete action that delivers value immediately |
| **Feature highlight** | Days 2-3 | Show the core feature that solves the problem |
| **Social Proof** | Day 3-4 | Testimonial or use case |
| **Nudge** | Days 5-7 | If they are not active: "do you need help?" |

**Trigger-based beats calendar-based.** If a user has already done action X, skip the corresponding email.

### Trigger-Based Flows (not just time-based)
- **Behavioral triggers**: page visited, feature used, cart abandoned, plan limit reached
- **Engagement triggers**: email opened, link clicked, video watched
- **Lifecycle triggers**: trial expiring, subscription anniversary, usage milestone

### Conditional Branching
```
IF opened email 1 AND clicked CTA
  -> Send case study email (Day 3)
ELSE IF opened email 1 but NO click
  -> Send social proof email (Day 3)
ELSE (no open)
  -> Resend with new subject line (Day 3)
```

**[ ] Onboarding Checklist:**
- [ ] Welcome email written (trigger: immediately after signup)
- [ ] Quick win email defined (what is the fastest value?)
- [ ] Feature highlight email planned (core feature)
- [ ] Social proof email prepared
- [ ] Nudge email for inactive users
- [ ] Trigger logic set up (behavioural, not just time-based)
- [ ] Conditional branching defined

## B2: Win-back Sequence

**If Win-back:**

### Essential Flows Beyond Onboarding
1. **Win-back flow**: 30/60/90 days inactive -> re-engagement series
2. **Upgrade flow**: Free user hits limit -> value demonstration -> upgrade CTA
3. **Churn prevention**: Cancel intent signal -> save offer sequence
4. **Re-engagement**: Newsletter non-opener -> "Still interested?" -> prune or win back

**[ ] Win-back Checklist:**
- [ ] Trigger defined (30d / 60d / 90d inactive)
- [ ] Re-engagement email 1: "We miss you" + concrete value
- [ ] Re-engagement email 2: what is new since the last login
- [ ] Re-engagement email 3: last attempt + opt-out offer
- [ ] Pruning logic: anyone still inactive after the series is removed from the active list

## B3: Campaign Sequence

**If Campaign:**

Ask the user: "How long is the campaign? When is the launch date?"

Then design a campaign structure:
- Teaser email (1-2 weeks before launch)
- Launch email (Day 0)
- Follow-up for non-openers (Day 3)
- Last chance email (if there is a deadline)
- Post-campaign thank you / next steps

**[ ] Campaign Checklist:**
- [ ] Campaign goal clear (what should happen?)
- [ ] Timing plan defined
- [ ] All emails written and checked
- [ ] Segmentation: who gets which email?
- [ ] UTM tracking set up

## B4: Newsletter

**If Newsletter:**

Ask the user: "What frequency? (weekly / fortnightly / monthly)"

**Newsletter structure template:**
1. Subject line (curiosity or clear benefit)
2. Preview text (complements the subject, does not repeat it)
3. Short personal intro (1-3 sentences)
4. Main content (1-3 topics)
5. One primary CTA
6. Optional: curated links

**[ ] Newsletter Checklist:**
- [ ] Editorial plan for the next 4 issues
- [ ] Consistent structure defined
- [ ] Subject line formula chosen
- [ ] Frequency agreed and communicated

---

# MODE C: Deliverability Setup

## C1: Domain Setup

Ask the user: "Have you already set up SPF, DKIM and DMARC? Yes / no / not sure"

### Use a subdomain (mandatory!)

Send marketing emails from a subdomain (e.g. `mail.example.com`). Keep transactional emails (confirmations, password resets) on the main domain. This isolates the risk.

### SPF, DKIM, DMARC

| Protocol | Purpose | Order |
|-----------|-------|-------------|
| **SPF** (sender policy framework) | Authorises mail servers for the domain | Step 1 |
| **DKIM** (DomainKeys Identified Mail) | Cryptographic signature; verifies the sender | Step 2 |
| **DMARC** (domain-based message authentication) | Policy for unauthenticated mail | Step 3 |

**Setup order:** SPF -> DKIM -> DMARC.

**DMARC policy, step by step:**
1. `p=none` (monitor only, 2-4 weeks)
2. `p=quarantine` (suspicious mail to spam, 4-8 weeks)
3. `p=reject` (block, after 60-90 days)

**Mandatory at Gmail and Yahoo since February 2024:** all three protocols are required for bulk senders (5,000+ per day).

**[ ] Deliverability Checklist:**
- [ ] Marketing subdomain set up (e.g. mail.example.com)
- [ ] SPF record configured and tested
- [ ] DKIM configured and tested
- [ ] DMARC set to p=none (monitoring phase)
- [ ] DMARC reports reviewed (2-4 weeks)
- [ ] Raise DMARC to p=quarantine (after 4-8 weeks)
- [ ] Raise DMARC to p=reject (after 60-90 days)
- [ ] One-click unsubscribe set up (required by Gmail/Yahoo)

---

# MODE D: Improve Existing Emails

Ask the user: "Please send me 1-3 emails you want to improve (subject line plus body)."

Then audit each email against best practices:

## D1: Subject Line Audit

### Subject Line Formulas

| Formula | Example |
|--------|----------|
| Question | "Do you know why 73% of couples...?" |
| Number + benefit | "3 ways to save time this week" |
| Curiosity | "Here is what we learned this week" |
| Direct | "New feature: [Name]" |
| Personal | "[Name], your weekly check-in" |

## D2: Content Best Practices Audit

| Rule | Details |
|-------|---------|
| **Subject line** | One clear topic; not pure promotion; spark curiosity |
| **Preview text** | Complements the subject line; does not repeat it |
| **Value first** | Useful information BEFORE promotion |
| **One CTA** | One primary call-to-action per email |
| **Mobile** | More than 50% read on mobile; responsive layout, tappable links |
| **Length** | Keep it short; respect the reader's time |

## D3: Metrics Benchmark

| Metric | Target |
|--------|--------|
| **Open rate** | >20% (B2C), >25% (B2B niche) |
| **Click rate** | >2.5% |
| **Unsubscribe rate** | <0.5% per send |
| **Complaint rate** | <0.3% (mandatory!) |
| **Bounce rate** | <2% (list hygiene!) |

**[ ] Improve Checklist:**
- [ ] Subject line checked against formulas
- [ ] Preview text complements the subject line (does not repeat it)
- [ ] Value first: useful content comes before promotion
- [ ] Only one primary CTA per email
- [ ] Mobile preview checked
- [ ] Metrics compared with benchmarks

---

## Rules (all modes)

1. **GDPR requirement:** double opt-in for all marketing emails. Document consent.
2. **No purchased lists** — only organically built subscribers
3. **Value first** — every email must deliver value to the recipient
4. **Frequency: respect it** — better less often with quality than daily with noise
5. **Segment** — not everyone gets everything
6. **Test** — A/B test subject lines, send times, content types
7. **List hygiene** — clean out bounces and inactive addresses regularly

## Unsubscribe (mandatory!)

- **One-click unsubscribe** is mandatory (a Gmail and Yahoo requirement)
- Process it within 48 hours
- Clearly visible in the footer
- Optional: preference center instead of a hard unsubscribe ("fewer emails" option)

## SEO Synergy: Articles by Email

Email can support SEO by distributing blog articles through the newsletter:

| Article type | Purpose |
|-------------|---------|
| **Retention** | Deep content for existing users; improve retention |
| **ToFu** | Top of funnel; awareness (trends, concepts, problem framing) |
| **MoFu** | Middle of funnel; consideration (comparisons, best practices) |

**Double value:** (1) better email engagement (opens, clicks) and (2) traffic to article pages from a non-search channel, which signals to Google that the content is valuable.

**Measure:** GA4 email-source traffic to article pages; rank and click changes in Search Console.

---

## Summary: Checklist before the first send

- [ ] SPF, DKIM, DMARC configured correctly
- [ ] Marketing subdomain set up
- [ ] Unsubscribe link works (one-click)
- [ ] Mobile preview checked
- [ ] Subject line + preview text written
- [ ] One clear CTA per email
- [ ] Tracking (UTM parameters) set up
- [ ] GDPR-compliant: double opt-in, consent documented
- [ ] Test email sent to yourself

---

## Related Skills
- `/product-marketing-context` - Brand voice for email copy
- `/content-marketing` - Content strategy for newsletters
- `/growth-strategy` - Email as retention channel
- `/churn-prevention` - Churn-related email flows
- `/ab-test-setup` - Test subject lines and CTAs

## References

- [Mailchimp Email Marketing Benchmarks](https://mailchimp.com/resources/email-marketing-benchmarks/)
- [Gmail Sender Guidelines](https://support.google.com/mail/answer/81126)
