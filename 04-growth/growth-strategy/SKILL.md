---
name: growth-strategy
description: Interactive growth strategy checklist - walks through AARRR funnel, PMF validation, GTM, cold start, retention, churn prevention, referral programs, free tools, Product Hunt, directory submissions, and 139 marketing tactics. Asks step-by-step what's relevant. Run /growth-strategy to diagnose bottlenecks or plan growth.
model: sonnet
effort: medium
---

## Step 0: Load marketing context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without

# Growth Strategy - Interactive Checklist

This skill walks you through every growth topic step by step. For each topic you are asked whether it is relevant — skip what does not apply.

## Workflow: How to use this skill

```
START: determine the venture stage
  |
  v
Phase 1: diagnosis — where are you? What is the bottleneck?
  |
  v
Phase 2: strategy — which levers fit your stage?
  |
  v
Phase 3: tactics — concrete marketing ideas by budget and stage
  |
  v
Phase 4: retention — keeping users (if you already have some)
  |
  v
Phase 5: summary — the top three actions for the next two weeks
```

---

## Phase 1: Diagnose

### Question 1: what stage is the venture at?

Ask the user and respond accordingly:

| Phase | Typical situation | Focus |
|-------|-------------------|-------|
| **Pre-Build / Idea** | No product yet | Validate PMF, landing page test, customer discovery |
| **Built, no users** | The product exists, 0-10 users | Cold start: find the first users |
| **First users, unsure about PMF** | 10-100 users, unclear whether it works | Test PMF, measure retention |
| **PMF confirmed, want to grow** | Retention is good, needs more users | Choose GTM mode, build channels |
| **Growth stalled** | Was good, now plateaued | AARRR diagnosis, find the bottleneck |

### Question 2: what is the biggest bottleneck?

Use the AARRR funnel (Dave McClure) to diagnose:

| Stage | Question | If weak... |
|-------|----------|-----------|
| **Acquisition** | Do people find you? | → SEO, Ads, Content, Directories (Phase 3) |
| **Activation** | Do they reach the aha moment? | → onboarding, CRO (see `/cro-audit`) |
| **Retention** | Do they come back? | → Phase 4 (Retention & Churn) |
| **Referral** | Do they refer others? | → Referral Program (Phase 4) |
| **Revenue** | Do they pay? | → Pricing (see `/pricing-strategy`) |

**Principle:** fix the stage with the biggest drop-off first. Do not pour more in at the top while the middle leaks.

### Question 3: what is the budget?

| Budget | Available tactics |
|--------|-------------------|
| **No budget** | Content, SEO, community, social, comment marketing |
| **Small (under 500 per month)** | + targeted ads, sponsorships, free tools |
| **Medium (500-2,000)** | + events, partnerships, PR |
| **Large (over 2,000)** | + brand campaigns, conferences, influencers |

---

## Phase 2: Strategy

### Do you need PMF validation? (yes/no)

If YES — ask the user whether they want to validate PMF:

**Sean Ellis 40% Test:**
Ask active users: "How would you feel if you could no longer use [product]?"

| Score (% "very disappointed") | Meaning |
|-------------------------------|---------|
| Under 25% | Significant changes needed |
| 25-39% | Close to PMF, keep iterating |
| 40%+ | PMF reached |

Best practice: survey 40-50 active users (two or more sessions in the last 14 days).

**Vitamin vs. Painkiller Check:**
- **Painkiller** = solves an urgent problem → fast adoption, high retention
- **Vitamin** = nice to have → slow adoption, expensive marketing
- Around 99% of failures solve vitamin problems instead of real pain

**PMF-Indikatoren:**
- [ ] High retention, low churn?
- [ ] Is CAC falling relative to CLTV?
- [ ] Organic growth and word of mouth?
- [ ] High NPS, enthusiastic recommendations?

### Do you need a go-to-market strategy? (yes/no)

If YES:

**Which GTM mode fits?**

| Mode | When | ACV | Buyer |
|------|------|-----|-------|
| **Product-Led (PLG)** | Value in minutes, self-serve | <€10K | End user = buyer |
| **Sales-Led (SLG)** | Multi-stakeholder, complex | >€25K | Enterprise |
| **Marketing-Led (MLG)** | Content/SEO/paid drive awareness | Variable | Demand gen |
| **Hybrid** | PLG for acquisition, sales for expansion | Common | Self-serve → Sales |

**Goal:** LTV:CAC >= 3:1; CAC payback <12 months.

**The motion must match the deal size** (Revenue Architecture, Jacco van der Kooij): every motion has its own processes, cost structure and team requirements — one motion for all deal sizes does not work. And with recurring revenue the go-to-market does not end at the close: onboarding and adoption are revenue work (the bowtie), measured by time-to-impact.

**90-day GTM framework:**
- [ ] Weeks 1-3: market analysis (demand, competition, TAM)
- [ ] Weeks 4-6: strategy (ICP, positioning, pricing, GTM mode)
- [ ] Weeks 7-9: execution (messaging, content, tech stack)
- [ ] Weeks 10-12: launch & iterate

### Do you need a cold start plan? (yes/no)

If YES — for products with network effects, apply the three principles from The Cold Start Problem (Andrew Chen) first: (1) **atomic network** — do not launch "the market", ignite the smallest network that works on its own (one company, one city, one campus); (2) **hard side first** — serve the difficult side (suppliers, creators, doctors) disproportionately well, with hand curation and subsidies if needed; (3) **"come for the tool, stay for the network"** — start with a single-player benefit that works without a network. Big-bang launches without atomic networks fall apart (many signups, empty rooms).

Channels for the first 100 users:

| Channel | Conversion | Timeline | Effort |
|---------|-----------|----------|---------|
| **Product Hunt** | ~3% | Launch day | High (30 days of prep) |
| **Reddit** | Variable | 5+ months | Medium |
| **Indie Hackers** | ~23% | 4-6 months | Medium |
| **Hacker News** | Variable | Luck + timing | Low |
| **Directories** | Variable | 2-4 weeks | Low |
| **Founder-led Outbound** | High | Immediate | High |
| **Community** | Variable | 45-90 days | Medium |

**Demand-Signal Outreach:**
- Search Twitter/X, LinkedIn and Reddit for "[looking for a tool for X]"
- Reply to posts where users express a need
- Template: "Hi, I'm building something similar. If you want to try it: [link]. Feedback welcome."

**What does NOT work early:**
- Hiring SDRs before the founder has personally closed 10 customers
- Large paid budgets before PMF
- "Spray and Pray" targeting

---

## Phase 3: Tactics - Marketing Idea Library

**Bullseye discipline** (Traction, Weinberg/Mares): do not default to the channels you already know. (1) Brainstorm at least one idea for ALL categories, (2) test the three most promising with cheap experiments (cost per customer? enough customers in the channel? the right ones?), (3) pick ONE winning channel — then put all energy there until it is exhausted. Plus the 50% rule: from day one, half your time goes into traction, not only after the product is done. The undervalued channels are the ones competitors are currently ignoring.

Ask the user for EVERY category: "Is this relevant for you? Yes / no / later"

If YES: suggest concrete ideas with how-to-start steps.
If NO: skip.
If LATER: note it for later.

### Category 1: Content & SEO (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 1 | **Easy keyword ranking** — find and target long-tail keywords with little competition | Free | Medium |
| 2 | **Programmatic SEO** — generate template-based pages at scale (locations, comparisons) | Free | Medium |
| 3 | **Glossary / knowledge base** — definitions and explanations as SEO content | Free | Long |
| 4 | **Content repurposing** — one article → LinkedIn post → carousel → newsletter → video | Free | Short |
| 5 | **Comparison pages** — "[our product] vs [competitor]" SEO pages (see `/competitor-research`) | Free | Medium |
| 6 | **Guest blogging** — guest articles on relevant blogs for backlinks and reach | Free | Medium |
| 7 | **Answer sites** — Quora, Stack Overflow and Reddit answers that mention the product | Free | Short |
| 8 | **Roundup posts** — "top 10 tools for X" articles that include you | Free | Medium |
| 9 | **Original research** — publish your own studies or surveys (strong backlinks) | Small | Long |
| 10 | **AI SEO** — optimise content for ChatGPT, Perplexity and Claude (see `/seo`) | Free | Long |

### Category 2: Free Tools & Lead Magnets (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 11 | **ROI / savings calculator** — shows the concrete benefit of your product | Small | Short |
| 12 | **Free checker / auditor** — tests something and shows room for improvement | Small | Short |
| 13 | **Template library** — templates that showcase your product | Free | Medium |
| 14 | **Chrome extension** — a small tool that complements your product | Medium | Medium |
| 15 | **Free tier** — a limited free version (freemium) | Free | Medium |
| 16 | **Email course** — a 5-7 day email series that demonstrates expertise | Free | Short |

### Category 3: Paid Ads (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 17 | **Google search ads** — buy high-intent keywords (see `/google-ads`) | Small+ | Short |
| 18 | **Meta / Instagram ads** — awareness and retargeting (see `/meta-ads`) | Small+ | Short |
| 19 | **LinkedIn ads** — B2B targeting by job title and company (see `/linkedin-ads`) | Medium+ | Short |
| 20 | **Retargeting** — reach website visitors again | Small | Short |
| 21 | **Competitor keyword bidding** — bid on competitor brand names | Small | Short |
| 22 | **Podcast / newsletter sponsorship** — reach niche audiences directly | Medium | Short |

### Category 4: Social & Community (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 23 | **LinkedIn content** — post regularly, thought leadership (see `/content-marketing`) | Free | Medium |
| 24 | **X presence** — daily posts, engagement, thread marketing | Free | Medium |
| 25 | **Reddit marketing** — genuine help in subreddits, no spam | Free | Long |
| 26 | **Build a community** — Discord, Slack or a forum for your audience | Free | Long |
| 27 | **Short-form video** — TikTok, Reels and Shorts with product demos or tips | Free | Short |
| 28 | **Comment marketing** — reply to relevant posts with something useful | Free | Short |

### Category 5: Partnerships & Events (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 29 | **Integration marketing** — integrate with complementary tools and co-promote | Free | Medium |
| 30 | **Newsletter swap** — mutual mentions in each other's newsletters | Free | Short |
| 31 | **Affiliate programme** — others earn commission for referrals | Small | Medium |
| 32 | **Webinars** — live demos or educational sessions | Free | Short |
| 33 | **Conference speaking** — speak as an expert at events | Free | Long |
| 34 | **Podcast tour** — guest on podcasts your audience listens to | Free | Medium |

### Category 6: Launch & PR (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 35 | **Product Hunt launch** — visibility and credibility (details below) | Free | Short |
| 36 | **Lifetime deal** — AppSumo or similar for fast revenue and feedback | Small | Short |
| 37 | **Giveaway / contest** — give the product away in exchange for social shares | Small | Short |
| 38 | **Press coverage** — contact journalists and bloggers | Free | Medium |
| 39 | **Awards** — enter industry awards (credibility and backlinks) | Small | Long |

### Category 7: Product-Led (yes/no?)

| # | Idea | Budget | Time horizon |
|---|------|--------|-------------|
| 40 | **Viral loops** — users invite others as part of the product experience | Free | Medium |
| 41 | **Powered-by badge** — "built with [product]" on user outputs | Free | Long |
| 42 | **Free migrations** — offer free migration from competitors | Small | Short |
| 43 | **In-app upsells** — upgrade prompts at the right moments | Free | Short |
| 44 | **Referral Program** - Users refer others for a reward (details below) | Small | Medium |

### Give a recommendation

After going through all categories, summarise the top three to five ideas that best fit the stage, budget and situation. For each one:

- **Idea:** name plus a short description
- **Why it fits:** the connection to the current situation
- **First steps:** 2-3 concrete actions for the next two weeks
- **Expected result:** what success looks like
- **Effort:** time, budget, skills

---

## Phase 4: Retention and churn (yes/no?)

Ask: "Do you already have active users you want to keep?"

If YES, work through this checklist:

### Understanding churn

| Churn type | Share | Cause | Fix |
|------------|-------|-------|-----|
| **Voluntary** | 60-80% | Pricing, missing features, poor onboarding | Cancel flow plus save offers |
| **Involuntary** | 20-40% | Payment failures, expired cards | Dunning management |

**Most churn is predictable 30-90 days in advance** from behavioural signals.

### Checklist: what do you already have? (yes/no per item)

- [ ] **Dunning management?** — automatic retries on failed payments plus an email sequence
  - Retry on days 1, 3, 7, 10 and 14
  - Emails: "Payment failed" → "Action needed" → "Account at risk" → "Account paused"
  - Proactive: warn customers 30 days before their card expires (reduces involuntary churn by 15-30%)

- [ ] **Cancel flow?** — not just a "cancel" button, but:
  1. Ask for the reason (radio buttons: too expensive, not using it, missing feature, switching tools, etc.)
  2. A targeted save offer based on the reason:
     - Too expensive → downgrade or discount
     - Not using it → pause (1-3 months)
     - Missing feature → show the roadmap
     - Switching → show a comparison
  3. A clean confirmation (no guilt-tripping)

- [ ] **Engagement scoring?** — spot at-risk users early:
  - Logging in less than once a week for two weeks = at risk
  - Core feature unused for 14 days = at risk
  - Emails no longer opened = at risk
  - Trigger: an automatic "we miss you" email plus an in-app nudge

- [ ] **Win-back campaigns?** — after cancellation:
  - Day 0: a clean confirmation, no guilt
  - Day 30: "we have something new" plus a concrete feature
  - Day 60: a comeback offer (one month free)
  - Day 90: "Here's how [product] has changed" + 14-day trial
  - After that: newsletter only

- [ ] **Referral Program?** - Existing users as a growth driver:
  - Double-sided rewards (both sides get something)
  - Product credit > cash > discount (effectiveness)
  - Timing: promote after the aha moment, NEVER during onboarding
  - Anti-gaming: reward only after purchase, IP deduplication, rate limits
  - Tools: Rewardful, Tolt, or custom with Supabase

### Retention metrics (which ones do you track?)

- [ ] **Monthly churn rate** = cancellations / active customers
- [ ] **Net Revenue Retention (NRR)** = (Start MRR + Expansion - Churn - Downgrade) / Start MRR. NRR >100% = good, >120% = excellent
- [ ] **Cohort retention** = % of each monthly cohort still active after 1/3/6/12 months
- [ ] **Save rate** = users who accepted the save offer / users who entered the cancel flow. Target: 15-30%

---

## Phase 5: Launch playbooks (yes/no?)

### Product Hunt launch checklist

Question: "Do you want to run a Product Hunt launch?"

If YES:

**Who Product Hunt works for:** SaaS, dev tools, AI, productivity, Chrome extensions.
**Bad for:** physical products, services, local businesses.
**Expectation:** only around 10% of submissions get featured. Product Hunt is a credibility boost, not a primary acquisition channel.

**30-day checklist:**
- [ ] Weeks 4-3: set up a "notify me" page on Product Hunt and engage in the community
- [ ] Weeks 3-2: build 200+ supporters, reach out personally
- [ ] Weeks 2-1: tagline (max 60 characters), gallery (1270x760px), video (<2 min), write first comment
- [ ] Launch day: Tuesday-Thursday, 00:01 Pacific time, 16h of engagement

**First comment structure:**
1. Who are you? (1-2 sentences)
2. Why did you build it? (personal motivation)
3. What does it do? (short, no feature dump)
4. What's next? (roadmap teaser)
5. CTA: "Would love your feedback!"

**Realistic results:**
- 50-100 upvotes = weak
- 200-400 = average (top 10)
- 500-800 = good (top 5)
- 800+ = Product of the Day
- Conversion: around 3% of Product Hunt visitors become users

### Directory submissions checklist

Question: "Do you want to get listed in directories?"

If YES:

**Why:** Backlinks (SEO), AI Citations (AI training data), Discovery, Credibility.

**Checklist - in this order:**

- [ ] **Tier 1 (first):**
  - [ ] Product Hunt (DR 90) - see above
  - [ ] G2 (DR 92) - needs real user reviews
  - [ ] Capterra (DR 91) - like G2
  - [ ] AlternativeTo (DR 82) - list as an alternative to competitors

- [ ] **Tier 2 (next):**
  - [ ] BetaList (DR 70) - good for pre-launch
  - [ ] SaaSHub (DR 65)
  - [ ] There's An AI For That (DR 72) — AI tools only
  - [ ] Indie Hackers (DR 80) - needs a real story post

- [ ] **Tier 3 (if there is time):**
  - [ ] GetApp (DR 82), Software Advice (DR 80), ToolPilot.ai (DR 50), SaaSworthy (DR 55)

**Prepare asset pack:**
- [ ] Product name (consistent everywhere)
- [ ] Tagline (max 60 characters)
- [ ] Description short (150 characters) + long (300-500 words)
- [ ] Logo (512x512, PNG, transparent)
- [ ] Screenshots (min. 3, 1280x800)
- [ ] UTM links per directory

### Free tool strategy checklist

Ask: "Do you want to build a free mini tool as a lead magnet?"

If YES:

**Selection criteria (all 4 must hold):**
- [ ] It relates to your product (a natural upsell path)
- [ ] Solves a real standalone problem
- [ ] Buildable in 1-2 weeks
- [ ] Useful enough that people share it

**Tool types:**
| Type | Examples |
|-----|----------|
| Calculator | ROI calculator, savings calculator, price comparison |
| Generator | Name generator, tagline generator, template generator |
| Checker | SEO audit, accessibility check, speed test |
| Converter | Format converter, unit converter |

**Monetisation: which variant?**
- [ ] Email gate (email for results - highest conversion)
- [ ] Ungated with CTA (results free, "Want more?" - lowest friction)
- [ ] Premium (basic free, detailed analysis with signup)
- [ ] Follow-up sequence (email → nurture → convert)

---

## Phase 6: Summary

At the end of every growth strategy session:

1. Agree the **top three actions** for the next two weeks
2. Define **metrics** for each action (how do we measure success?)
3. Name the **non-goals** clearly (what we deliberately will NOT do)
4. Document it in the project journal
5. Create tasks in your task tracker

---

## Related Skills
- **`/growth-lab`** — **the next step after this strategy.** Once you know WHICH channel you are using, growth-lab tells you WHAT exactly to test, with decision trees, benchmarks and experiment tracking.
- `/product-marketing-context` — positioning and messaging foundation
- `/seo` - Organic Traffic + AI SEO
- `/meta-ads` - Paid Acquisition Meta/Instagram
- `/google-ads` - Paid Search
- `/linkedin-ads` - B2B Paid
- `/email-marketing` - Email as a growth channel
- `/cro-audit` - Conversion Optimization + Onboarding + A/B Tests
- `/pricing-strategy` - Monetisation + tier design
- `/analytics-tracking` - Metrics + tracking
- `/competitor-research` - Competitor analysis + comparison pages
- `/content-marketing` - Content strategy + lead magnets + LinkedIn

## References
- Dave McClure: AARRR Pirate Metrics
- Marc Andreessen: Product-Market Fit
- Sean Ellis: 40% Test
- Corey Haines: Marketing Ideas Library (139 Tactics)
- Source: [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT)
