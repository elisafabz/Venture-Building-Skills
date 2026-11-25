---
name: google-ads
description: Google Ads campaign setup and optimization — Search, Display, Performance Max, YouTube. PMF testing mode ($47-500) and conversion-driven mode. Keyword strategy, Quality Score, bidding, retargeting, competitor brand bidding. Run /google-ads to plan or optimize campaigns.
model: sonnet
effort: medium
---

## Step 0: Load Marketing Context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# Google Ads — Interactive Checklist

This skill walks you step by step through Google Ads setup and optimisation. For each phase you are asked whether it is relevant.

Set up campaigns in the language of the target market.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Intake: understand first, then work

Ask the user these 3 questions before doing anything else:

**Ask the user:**

1. What is the goal? (PMF testing / lead generation / e-commerce sales / brand awareness)
2. What is the monthly budget? (under 500 / 500-2,000 / 2,000+)
3. Have you run Google Ads before? (Yes / No / Tried it but stopped)

Wait for the user's answers. Then adapt the approach:
- PMF Testing / no budget -> Focus on PMF Testing Mode, minimal setup
- Lead Gen / medium budget -> Search campaigns + Tracking setup
- E-Commerce / large budget -> Full funnel: Search + PMax + Retargeting
- "Stopped before" -> Ask what went wrong first, diagnose before building

---

## Phase 1: Campaign Type Selection

Ask the user: **"Which campaign types are relevant? I can explain the options. (Yes / no / later)"**

If YES: Walk the user through the decision below.
If NO: Skip to Phase 2.

### Two Modes: PMF Testing vs. Conversion-Driven

| Mode | When | Budget | Landing Page | KPIs |
|------|------|--------|-------------|------|
| **PMF testing** | Pre-PMF; validate the idea before building | Start small | A simple landing page: headline, benefits, CTA ("join waitlist") | CTR, signup rate, bounce rate |
| **Conversion-Driven** | PMF validated; scaling | Scaled; ROAS target | Full funnel; ad-to-page alignment | ROAS, CAC, Conversion Rate |

**PMF testing:** no finished product needed. Build a landing page, run ads on relevant search terms, measure clicks and signups. Test messaging ("the fastest app for freelancers" versus "the simplest time tracker for teams"), price points and audiences. Allow 4-6 weeks for the Performance Max learning phase.

### Campaign Types

| Type | When to use |
|-----|-------------|
| **Search** | High-intent queries; users actively search for a solution |
| **Display** | Awareness; retargeting; broader reach |
| **YouTube** | Video; awareness; consideration |
| **Performance Max (PMax)** | Automated; cross-channel; feed + search + display |

Ask the user: **"Which mode and which campaign types fit your venture?"**

Document the decision and proceed with the selected approach.

### Recommended Campaign Structure

Once the user has chosen, show the relevant structure:

```
Account
├── Campaign: Brand (Search)           <- protect your own brand terms
├── Campaign: Non-Brand (Search)       <- generic keywords
├── Campaign: Competitor (Search)      <- optional: "[Competitor] alternative"
├── Campaign: Retargeting (Display)    <- win back website visitors
└── Campaign: Performance Max          <- automated, cross-channel
```

**Naming Convention:** `GOOG_[Goal]_[Audience]_[Offer]_[Date]`
Example: `GOOG_Search_Brand_FreeTrial_2604`

**Phase 1 complete. Continue to Phase 2? (Yes/No)**

---

## Phase 2: Keyword Strategy

Ask the user: **"Shall we build the keyword strategy? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 3.

### Keyword Checklist

- [ ] Seed keywords identified (core terms your audience searches for)
- [ ] Match types decided per campaign (see below)
- [ ] Negative keyword list started
- [ ] Brand terms in separate campaign
- [ ] Competitor keywords considered (separate campaign)
- [ ] Search Terms Report review scheduled (weekly)

### Match Types

| Type | When |
|-----|------|
| **Broad** | Discovery phase; find new keywords |
| **Phrase** | Balanced approach |
| **Exact** | Maximum control; proven keywords |

### Negative Keywords (mandatory!)

Build up weekly. Exclude:
- Support terms: "login", "forum", "pricing", "help" (existing customers, not prospects)
- Irrelevant queries from the search terms report
- Exclude your own brand from non-brand campaigns

### Competitor Brand Keywords

- Bid on "[Competitor] alternative", "[Competitor] vs [Us]"
- Google allows competitor keywords, but NOT their names in ad copy
- Use a **dedicated comparison landing page** (not a blog article)
- Separate campaign; Exact/Phrase Match
- Expect a lower Quality Score and higher CPC

**Phase 2 complete. Continue to Phase 3? (Yes/No)**

---

## Phase 3: Ad Copy

Ask the user: **"Shall we create ad copy? (Yes/No/later)"**

If YES: Work through the following.
If NO: Skip to Phase 4.

### Ad Copy Checklist

- [ ] At least 3 ad variants per Ad Group
- [ ] 8-10 headlines per RSA
- [ ] 3-4 descriptions per RSA
- [ ] Headlines cover: Benefit, Feature, Social Proof, CTA, Keyword
- [ ] Ad-to-Page Alignment checked (promise in ad = visible on LP)
- [ ] No dark patterns (no fake scarcity, no clickbait)

### Ad Copy Frameworks

| Framework | Structure |
|-----------|----------|
| **PAS** | Problem -> Intensify pain -> Solution -> CTA |
| **BAB** | Painful present -> Desired future -> Your product as the bridge |
| **Social Proof** | Impressive number/testimonial -> What you do -> CTA |

### Responsive Search Ads (RSA)

- At least 8-10 headlines, 3-4 descriptions
- Vary headlines: Benefit, Feature, Social Proof, CTA, Keyword
- Pin only when necessary (it constrains the algorithm)

### Quality Score

| Factor | Action |
|--------|--------|
| **Expected CTR** | Improve ad relevance; test headlines |
| **Ad Relevance** | Align ad copy with keyword intent |
| **Landing Page** | Ad-to-page alignment; fast load time; mobile-friendly |

**Target:** a quality score of 6 or higher. Going from 5 to 7 can cut CPC by 30-50%.

**Phase 3 complete. Continue to Phase 4? (Yes/No)**

---

## Phase 4: Bidding & Budget

Ask the user: **"Shall we set the bidding strategy and budget? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 5.

### Bidding Checklist

- [ ] Conversion volume estimated (determines which strategy to use)
- [ ] Bidding strategy selected (see table below)
- [ ] Daily budget set per campaign
- [ ] Budget cap confirmed: max 25 EUR per campaign without explicit approval

### Bidding Strategy

| Conversions/Month | Strategy |
|-------------------|-----------|
| <30 | Manual CPC (Smart Bidding needs volume) |
| 30-50 | Target CPA; minimum for effective Smart Bidding |
| 50-100 | Target CPA |
| 100+ | Target ROAS |

**Smart Bidding** needs at least 30 conversions in 30 days. Below that: Manual CPC.

### Performance Max (PMax) - Additional Rules

| Rule | Details |
|-------|---------|
| **Learning Phase** | Let it run for at least 6 weeks |
| **Asset groups** | Organise by audience intent, not by product category |
| **Assets per group** | At least 5 images (including 1200x1200), 5 texts (4 headlines, 5 descriptions), video if possible |
| **Signals** | Add Remarketing Lists + Customer Match for faster learning |
| **Weekly check** | Brand terms above 30% of conversions? Unexpected geographic conversions? Any placement above 15% of spend? |

**Performance Max complements search, it does not replace it.**

**Phase 4 complete. Continue to Phase 5? (Yes/No)**

---

## Phase 5: Tracking Setup

Ask the user: **"Is conversion tracking set up? (Yes / No / Not sure)"**

If NO or "Not sure": Work through the following.
If YES: Quick-check with the checklist and skip to Phase 6.

### Tracking Checklist

- [ ] Conversion Tracking configured in Google Ads
- [ ] Conversion event tested with a real conversion
- [ ] Enhanced Conversions activated
- [ ] UTM parameters consistent for GA4 cross-check
- [ ] Offline Conversion Import set up (if B2B with CRM)

### Tracking Components

| Component | Purpose |
|------------|-------|
| **Enhanced Conversions** | Server-side signals for better attribution |
| **Offline Conversion Imports** | B2B: CRM -> Google Ads |
| **UTM parameters** | Consistent for GA4 cross-check |

**Test the conversion event before the campaign goes live!**

### Retargeting Setup

Ask: **"Do you want to set up retargeting (Display)? (Yes/No)"**

If YES:

- [ ] Remarketing audiences defined
- [ ] Exclusions set (existing customers, recent converters, bouncers)

| Audience | Window | Message |
|----------|---------|-----------|
| Blog readers, video viewers | 30-90 days | Educational, social proof |
| Pricing/feature visitors | 14-30 days | Case studies, demos |
| Cart abandoners, trial users | 7-14 days | Urgency, objection handling |

**Exclusions:** existing customers; recent converters (7-14 days); bounced visitors (<10s).

**Phase 5 complete. Continue to Phase 6? (Yes/No)**

---

## Phase 6: Launch Checklist

Ask the user: **"Ready to launch? Shall we go through the final checklist? (Yes / no)"**

If YES: Go through each item explicitly with the user.

### Checklist Before Launch

- [ ] Conversion Tracking tested with a real conversion
- [ ] Landing page loads in <3s; mobile-friendly
- [ ] UTM parameters work
- [ ] Negative keyword list built
- [ ] Budget set; targeting matches the audience
- [ ] Ad-to-page alignment checked (the promise in the ad is visible on the landing page)
- [ ] At least 3 ad variants per Ad Group
- [ ] Budget cap confirmed: max 25 EUR per campaign

### Dual-Channel Note: Google + Meta

Google and Meta are **complementary**, not competing:
- **Google** captures high-intent search (users actively searching)
- **Meta** creates and shapes demand (the user discovers)

Use consistent KPIs (profit > volume). See `/meta-ads` for Meta setup.

### Paid-Organic Cannibalisation

If you rank organically (position 4 or better) for a keyword AND run PPC, paid ads can absorb clicks that would otherwise have come organically.

**Audit:** compare organic rankings in Search Console with the search terms report. Where you rank well organically, test pausing PPC for those terms and move the budget to higher-impact keywords.

**Phase 6 complete. Continue to Phase 7? (Yes/No)**

---

## Phase 7: Weekly Optimisation Checklist

Ask the user: **"Shall we set up a weekly optimisation routine? (Yes / no / later)"**

If YES: Show the following and help the user schedule it.
If NO: Skip to Summary.

### Weekly Optimisation

| Check | Action |
|-------|--------|
| **Creative fatigue** | Refresh when CTR or conversion rate falls |
| **Learning Phase** | Ensure sufficient volume (30+ conversions/30d for Smart Bidding) |
| **Brand term share** | If brand terms exceed 30% of conversions, move budget to non-brand |
| **Placement check** | Flag any placement above 15% of total spend |
| **Search Terms** | Review weekly; add irrelevant queries as negatives |

### Weekly Checklist

- [ ] Search Terms Report reviewed, new negatives added
- [ ] CTR and Conversion Rate per campaign checked
- [ ] Budget utilization checked (not over- or under-spending)
- [ ] Quality Scores reviewed
- [ ] Any placement consuming >15% of spend flagged
- [ ] PMax: Brand Terms share checked

---

## Summary: the top three actions for the next two weeks

After completing relevant phases, present the user with the 3 highest-impact next steps:

1. **[Action 1]** - [Rationale / expected impact]
2. **[Action 2]** - [Rationale / expected impact]
3. **[Action 3]** - [Rationale / expected impact]

---

## Rules (always apply)

1. **Budget cap: max 25 EUR per campaign** -- NEVER more without explicit confirmation
2. **PMF first** — no large paid scaling before PMF is validated
3. **Quality Score > Budget** -- a poor QS is expensive regardless of how much budget you have
4. **Ad-to-page alignment** — what the ad promises must be immediately visible on the landing page
5. **No dark patterns** -- no fake scarcity, no clickbait
6. **Respect the algorithm** — no significant changes during the learning phase
7. **Measure before scaling** — prove it works first, then raise the budget

---

## Related Skills
- `/product-marketing-context` - Venture context
- `/meta-ads` - Dual-channel strategy
- `/seo` - Organic + paid synergy
- `/analytics-tracking` - Conversion tracking setup
- `/ab-test-setup` - Test ad variations

---

## References

- [Google Ads Help Center](https://support.google.com/google-ads/)
- [Google Ads Best Practices](https://ads.google.com/intl/en/home/resources/)
