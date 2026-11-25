---
name: pricing-strategy
description: Pricing strategy and structure — models (subscription, freemium, usage-based), tier design, anchoring, discount marketing (LTD, BFCM, referral codes), redeem codes. Run /pricing-strategy to design or optimize pricing.
model: opus
effort: high
---

## Step 0: Load marketing context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# Pricing Strategy - Models, Tiers, Discounts

Pricing skill: models, tier design, anchoring, discount strategies (lifetime deals, Black Friday, referral), redeem codes.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Step 1: Intake Questions

Ask the user ALL of the following before doing anything else. Wait for all answers.

```
Ask the user:
1. Do you have pricing already, or are you starting from zero?
2. What is your product type? (SaaS / Marketplace / One-time / Service)
3. What is your biggest pricing problem?
   - Too few conversions
   - High churn
   - No idea what to charge
   - Competitors are cheaper
```

Wait for all answers before proceeding.

---

## Step 2: Project context

Before you start:
- Read any existing venture notes for context and audience
- Read the project's `CLAUDE.md` and `README.md`
- Ask: what is the product? Who pays? What is the competition?

---

## Phase 1: Pricing Model Selection

Ask the user: "Shall we pick the right pricing model (subscription, freemium, usage-based, hybrid)? Yes / no / later"

**If YES:**

**Check the go-to-market motion first** (Revenue Architecture, Jacco van der Kooij): price and sales route must match — self-service, transactional and enterprise each need their own processes, cost structures and teams; one motion for all deal sizes does not work. Rule of thumb: a price too low for the sales effort kills the margin; a price too high for self-service kills conversion. For subscription models, also check where the revenue actually comes from: retention and expansion (NRR) compound harder than the price paid by new customers.

### Pricing models

| Model | When | Examples |
|--------|------|-----------|
| **Subscription** | Recurring, monthly or annual; the SaaS standard | Spotify, Notion, Slack |
| **Freemium** | A free tier plus paid; adoption first, then conversion | Dropbox, Canva, Figma |
| **Usage-Based** | Pay per use; API, credits, consumption | AWS, OpenAI, Twilio |
| **One-Time** | One-off purchase; some tools | Lifetime Deals |
| **Hybrid** | Base + usage; tiers + overage | Vercel, Supabase |

**Variable-cost products** (compute, API, AI): when per-user costs vary a lot (heavy users cost 10x or more than light users), a flat subscription often does not work. Use usage-based pricing, credits or usage tiers.

**[ ] Phase 1 Checklist:**
- [ ] Pricing model chosen (Subscription, Freemium, Usage, Hybrid)
- [ ] Variable cost per user analysed (if relevant)
- [ ] The model fits the product type and the audience

**If NO:** Skip to Phase 2.

---

## Phase 2: Tier Design

Ask the user: "Shall we design the tier structure (how many tiers, what goes in each)? Yes / no / later"

**If YES:**

### Tier-Design Principles

- **2-4 tiers** is typical; no more than that (decision paralysis)
- **Clear differentiation:** every tier has a "best for"
- **Value metric:** tie price to value (seats, projects, API calls)
- **Feature gates:** what is included in which tier?

### Tier structure (template)

| Tier | Target audience | Pricing | Features |
|------|-----------|---------|----------|
| **Free / starter** | Individuals, people trying it out | 0 | Basic features; a usage limit |
| **Pro** | Power users, small teams | €X/mo | All features; higher limit |
| **Team / Business** | Teams, SMBs | €Y/mo | Collaboration, Admin, Priority Support |
| **Enterprise** | Large enterprises | On request | Custom, SSO, SLA, Dedicated Support |

### Packaging vs. Pricing

- **Packaging** = what's in each tier (features, limits, support level)
- **Pricing** = what each tier costs
- Design packaging FIRST, then price. Most teams do it backwards.
- Each tier should have a clear "who is this for" answer.

### Pricing mistakes to avoid

| Mistake | Better |
|--------|--------|
| Too many tiers (5+) | 2-4 tiers; clear differentiation |
| Priced too low | Better to start higher and discount from there |
| No annual discount | Offer 15-25% for annual plans |
| Unclear feature gating | Use a clear table: what is included where |
| LTD without an exit strategy | Time-limit it; set tier limits |
| Never revisiting pricing | Review regularly; markets change |

Alongside this, use the **four monetisation failures** as a diagnostic grid (Monetizing Innovation, Ramanujam/Tacke): *feature shock* (too much crammed in — confusing and diluted), *minivation* (charging too little — value given away), *hidden gem* (a real gem that never gets seriously monetised), *undead* (a product nobody ever wanted, living on as a zombie).

**[ ] Phase 2 Checklist:**
- [ ] 2-4 tiers defined with a clear "best for"
- [ ] Packaging defined first (what sits in which tier)
- [ ] Then set pricing
- [ ] Feature gate table created (what is included where)
- [ ] Annual discount (15-25%) planned

**If NO:** Skip to Phase 3.

---

## Phase 3: Value Metrics

Ask the user: "Shall we define the right pricing axis (the value metric) — what you actually bill against? Yes / no / later"

**If YES:**

### Value Metrics Framework

The right pricing axis is the unit of value your customer receives.

**How to Choose:**
1. **List what customers value** (seats, projects, API calls, storage, revenue managed)
2. **Pick the metric that scales with customer success**
3. **Ensure it's predictable** (customers should be able to estimate their bill)
4. **Make it measurable** (you need to track it technically)

### Common Value Metrics by Product Type

| Product Type | Good Metric | Bad Metric |
|-------------|-------------|------------|
| SaaS tool | Active users, projects | Features unlocked |
| API service | API calls, data volume | Time-based access |
| Marketplace | GMV, transactions | Listings |
| Content platform | Content created, views | Storage |

**[ ] Phase 3 Checklist:**
- [ ] Value metric identified (seats, usage, features, etc.)
- [ ] Metric scales with customer success
- [ ] The metric is predictable for customers
- [ ] The metric is technically trackable

**If NO:** Skip to Phase 4.

---

## Phase 4: Pricing Research

Ask the user: "Shall we run pricing research (Van Westendorp, competitor analysis)? Yes / no / later"

**If YES:**

**Have the willingness-to-pay conversation BEFORE building** (Monetizing Innovation, Ramanujam/Tacke): the price is validated before the product ("design the product around the price"), not after. Talk to target customers about what they would pay early; **segment by willingness to pay, not by demographics**; decide the monetisation MODEL (subscription, usage, freemium) before the price POINT; features without validated WTP come off the roadmap.

### Van Westendorp Price Sensitivity Meter

Ask 4 questions (survey or customer interviews):
1. At what price would this be so cheap you'd doubt quality?
2. At what price is this a bargain - great value?
3. At what price is this getting expensive but you'd still consider?
4. At what price is this too expensive - you'd never buy?

Plot the curves - intersections reveal optimal price range.

### Competitor Analysis

Ask the user: "Who are our competitors? Please name 2-3."

Then analyze:
- What pricing model do they use?
- What tiers and price points?
- What value metric?
- Where is the gap we can position against?

**[ ] Phase 4 Checklist:**
- [ ] Van Westendorp questions asked to 5-10 customers/prospects
- [ ] Price thresholds identified (Too cheap / Bargain / Expensive / Too expensive)
- [ ] Competitor pricing analysed (2-3 competitors)
- [ ] Positioning gap identified

**If NO:** Skip to Phase 5.

---

## Phase 5: Psychology & Presentation

Ask the user: "Shall we set up anchoring, decoy pricing and charm pricing? Yes / no / later"

**If YES:**

### Anchoring & Presentation

| Technique | Details |
|---------|---------|
| **Annual Discount** | 15-25% for annual prepayment; improves cash flow |
| **Decoy Pricing** | A higher tier makes the middle one more attractive |
| **"Most Popular"** | Highlight the recommended plan |
| **Price display** | Monthly vs. annual; show the savings |
| **Order** | Cheapest on left or right? Test it. Typical: cheap -> expensive (left to right) |

### Pricing psychology

| Principle | Application |
|---------|-----------|
| **Charm pricing** | 9.99 rather than 10 for consumer products; for B2B, round numbers are often better |
| **Price Anchoring** | Show the most expensive plan first; the middle one looks cheaper |
| **Decoy effect** | Plan C exists only to make plan B look better |
| **Loss Aversion** | "Save €240/year" instead of "€20/month discount" |
| **Social proof** | "2,400 teams use the pro plan" |
| **Free Trial** | 7-14 days; reduces risk; increases conversion |

**[ ] Phase 5 Checklist:**
- [ ] The annual discount is visible on the pricing page
- [ ] "Most Popular" plan highlighted
- [ ] Decoy plan planned (if 3+ tiers)
- [ ] Loss aversion wording chosen ("Save €X")
- [ ] Social proof on the pricing page (a testimonial or a user count)
- [ ] Free trial or freemium tier in place

**If NO:** Skip to Phase 6.

---

## Phase 6: Discount Strategy

Ask the user: "Shall we develop a discount strategy (lifetime deals, Black Friday, referral)? Yes / no / later"

**If YES:**

### Discount types

| Type | Range | When |
|-----|-------|------|
| **Annual Commitment** | 15-25% | Improve cash flow; reduce churn |
| **Volume / Enterprise** | 10-40% | Larger deals; seat-based |
| **New customers** | 15-30% | Overcome hesitation; 3-12 months; <15% rarely moves people, >30% attracts price-sensitive buyers |
| **Lifetime Deal (LTD)** | One-off; heavily reduced | Cold start; fast cash; AppSumo |
| **BFCM** | 10-25% | Seasonal; November |
| **Referral** | 10-30% of the price | For both the referrer and the referred |

### Lifetime Deals (LTD)

**When it makes sense:**
- Cold start; zero traction; need fast revenue
- Validate PMF; price-sensitive early adopters
- Platform: AppSumo (500K+ users, 2K+ affiliates)

**Risks:**
- Revenue cannibalisation (subscribers switch to the LTD)
- Support load (lifetime deal buyers are often demanding)
- Price perception (the product comes across as "cheap")

**Mitigation:** Tiered LTD (different levels); upsell to premium; limit scope.

### Redeem Codes / Coupons

| Type | When |
|-----|------|
| **Percentage discount** | Feels more valuable at higher price points |
| **Fixed amount** | Better for smaller baskets |
| **Product-specific** | Promote certain tiers or features |
| **Free Shipping** | E-commerce; with/without minimum order value |

**Best Practices:**
- Unique codes per channel (for tracking!)
- Time-limited (real scarcity, no fake)
- Placement: top banner (30-50% more redemptions), popup, email
- Cart abandonment runs at roughly 70% — a coupon can reduce it

### Black Friday / Cyber Monday (BFCM)

| Phase | Details |
|-------|---------|
| **Planning** | Start in October |
| **Launch** | Early November (e.g. Nov 7) |
| **Peak** | The Monday before Thanksgiving; more than 40% of emails carry a discount |
| **Strategy** | 10-25% is often enough; quality over lowest prices |
| **Anchoring** | Several options: a nominal first month OR 50% off the annual plan |
| **Post-Holiday** | Retargeting; segmentation; adjust messaging |

**[ ] Phase 6 Checklist:**
- [ ] Discount strategy defined (new customers, referral, seasonal)
- [ ] LTV:CAC of at least 3:1 checked for discounted offers
- [ ] Unique codes per channel created
- [ ] BFCM timing planned (if relevant)
- [ ] LTD exit strategy defined (if LTD planned)

**If NO:** Proceed to Summary.

---

## Summary: Recommended Pricing Structure

After all phases, always deliver this summary:

**Ask the user:** "Shall I now work out a concrete pricing recommendation?"

Then provide:

1. **Recommended pricing model** with justification
2. **Tier structure** - name, price, "best for", key features per tier
3. **Value metric** chosen and why
4. **Anchor price** and "Most Popular" designation
5. **First discount** to implement (quick win)
6. **Pricing page copy** outline

**[ ] Final Implementation Checklist:**
- [ ] Pricing model chosen (Subscription, Freemium, Usage, Hybrid)
- [ ] 2-4 tiers defined with a clear "best for"
- [ ] Value metric identified (seats, usage, features)
- [ ] Annual discount (15-25%) planned
- [ ] Anchoring and decoy in place on the pricing page
- [ ] "Most Popular" plan highlighted
- [ ] Free trial or freemium tier in place
- [ ] Discount strategy defined (new customers, referral, seasonal)
- [ ] LTV:CAC of at least 3:1 on discounted offers
- [ ] Pricing page copy outline created
- [ ] A/B test plan for pricing page defined

---

## Related Skills
- `/product-marketing-context` - Positioning informs pricing
- `/cro-audit` - Optimize pricing page conversion
- `/churn-prevention` - Pricing's impact on retention
- `/paywall-upgrade-cro` - Free-to-paid conversion
- `/competitor-profiling` - Competitive pricing analysis
- `/marketing-psychology` - Pricing psychology principles

## References

- [Patrick Campbell / ProfitWell: Pricing Strategy](https://www.profitwell.com/recur/all/pricing-strategy-guide)
- [OpenView: SaaS Pricing](https://openviewpartners.com/blog/saas-pricing/)
