---
name: linkedin-ads
description: LinkedIn Ads setup and optimization — B2B targeting (Job Title, Company, Seniority), Sponsored Content, Lead Gen Forms, Message Ads. Run /linkedin-ads to plan or optimize B2B ad campaigns. Based on kostja94/marketing-skills.
model: sonnet
effort: medium
---

## Step 0: Load Marketing Context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# LinkedIn Ads — Interactive Checklist

This skill walks you step by step through LinkedIn Ads setup. For each phase you are asked whether it is relevant.

Set up campaigns in the language of the target market.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Intake: understand first, then work

Ask the user these 3 questions before doing anything else:

**Ask the user:**

1. Is your product B2B? (If not, LinkedIn Ads is probably the wrong channel — suggest alternatives)
2. What is the goal? (Lead generation / brand awareness / event promotion)
3. What is the monthly budget? (LinkedIn Ads are expensive — at least 1,000 per month is recommended)

Wait for the user's answers. Then:
- If B2C -> Warn that LinkedIn is likely wrong channel. Suggest Meta Ads or Google Ads instead. Ask if user still wants to proceed.
- If budget <500 EUR per month -> Warn that LinkedIn CPCs are 5-15 EUR, budget will run out very fast. Suggest Google Ads as more cost-effective alternative.
- If B2B + adequate budget -> Proceed with Phase 0 (Suitability Check).

---

## Phase 0: Suitability Check — is LinkedIn the right channel?

Before building campaigns, always verify LinkedIn is worth it.

Ask the user: **"Let's quickly check whether LinkedIn makes sense for your venture. (Yes / no — skip if it is already clear)"**

If YES: Walk through the decision table.

### When to use LinkedIn Ads?

| Situation | LinkedIn | Instead |
|-----------|----------|-------------|
| B2B, reaching decision-makers | Yes | - |
| Job title / company targeting important | Yes | - |
| Higher ACV (>5K) | Yes | - |
| B2C, broad audience | No | Meta Ads |
| Low budget, performance-focused | No | Google Ads |

**LinkedIn is expensive** (a CPC of 5-15 is typical). It only makes sense when the customer lifetime value justifies it.

If LinkedIn is NOT right for the venture: Explain why and recommend the better alternative. Stop here.
If LinkedIn IS right: Proceed to Phase 1.

**Phase 0 complete. Continue to Phase 1? (Yes/No)**

---

## Phase 1: Targeting Setup

Ask the user: **"Shall we define the targeting? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 2.

### Targeting Checklist

- [ ] Target Job Titles defined (e.g. CTO, Head of Marketing, VP Sales)
- [ ] Target Company Size defined (SMB vs. Enterprise)
- [ ] Target Industries defined
- [ ] Seniority levels defined (C-Level, Director, Manager)
- [ ] Decision to use ABM targeting (specific companies list) made
- [ ] Lookalike audience planned (based on existing customer list)

### Targeting Options (LinkedIn's strength)

| Signal | When to use |
|--------|-------------|
| **Job Title** | Reach decision-makers directly (CTO, Head of Marketing, etc.) |
| **Company** | ABM (Account-Based Marketing); specific companies |
| **Seniority** | Filter for C-Level, Director, Manager |
| **Company Size** | Distinguish Enterprise vs. SMB |
| **Industry** | Industry-specific targeting |
| **Skills** | Technical audiences (e.g. "Machine Learning") |
| **Lookalike** | Based on a contact list or on engagement |

**Principle:** target narrowly on high-intent segments. Broad targeting on LinkedIn burns money.

**Phase 1 complete. Continue to Phase 2? (Yes/No)**

---

## Phase 2: Ad Format Selection

Ask the user: **"Which ad formats are relevant for your goal? (Yes / no / later)"**

If YES: Walk through the options based on the user's stated goal from Intake.
If NO: Skip to Phase 3.

### Ad Format Checklist

- [ ] Primary ad format selected (see table below)
- [ ] Image dimensions confirmed (1200x627px for Feed)
- [ ] Video specs confirmed if using video (15-30 sec, subtitles, hook in 3s)
- [ ] Lead Gen Form fields minimized (if using Lead Gen Forms)
- [ ] Document prepared if using Document Ads

### Ad Formats

| Format | When | Details |
|--------|------|---------|
| **Sponsored Content** | Standard; feed ads | Single Image, Video, Carousel, Document |
| **Lead Gen Forms** | Lead generation without a landing page | Native forms; higher conversion than LP |
| **Message Ads** | Direct outreach | InMail; personal; lead gen |
| **Text Ads** | Awareness; cheaper | Right column; lower cost |
| **Document Ads** | Thought leadership | PDFs, whitepapers in the feed |

**Recommendation by goal:**
- Lead Generation -> Lead Gen Forms (best conversion, no landing page effort)
- Brand Awareness -> Sponsored Content with a strong creative
- Event Promotion -> Sponsored Content + Message Ads

### Creative Best Practices

| Rule | Details |
|-------|---------|
| **Professional tone** | LinkedIn is not Facebook; respect the business context |
| **Headlines** | Clear benefit; problem-solution format |
| **Images** | 1200x627px (Feed); real people > stock |
| **Safe zones** | Keep critical content at least 60px from the edge (LinkedIn crops on mobile). Use the central 80%. No text or UI elements in the outer 10% |
| **Never reuse one image across all ads** | Every ad needs its own visual — otherwise you get ad fatigue and no clean A/B test |
| **Video** | 15-30 seconds; subtitles mandatory; hook in 3s |
| **Document Ads** | PDFs for thought leadership; carousel effect |
| **Lead gen forms** | As short as possible; essential fields only |

**Phase 2 complete. Continue to Phase 3? (Yes/No)**

---

## Phase 3: Campaign Structure

Ask the user: **"Shall we build the campaign structure? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 4.

### Campaign Structure Checklist

- [ ] Campaign Groups named after venture
- [ ] Awareness campaign defined (if needed)
- [ ] Lead Gen campaign defined
- [ ] Retargeting campaign planned
- [ ] Naming convention applied to all campaigns

### Recommended Structure

```
Account
├── Campaign Group: [Venture Name]
│   ├── Campaign: Awareness (Sponsored Content)
│   │   └── Audience: Decision Makers in [Industry]
│   ├── Campaign: Lead Gen (Lead Gen Forms)
│   │   └── Audience: [Job Titles] at [Company Size]
│   └── Campaign: Retargeting
│       └── Audience: Website Visitors + Engagers
```

**Naming Convention:** `LI_[Goal]_[Audience]_[Offer]_[Date]`
Example: `LI_LeadGen_CTOs-SaaS_Whitepaper_2604`

**Phase 3 complete. Continue to Phase 4? (Yes/No)**

---

## Phase 4: Budget & Bidding

Ask the user: **"Shall we set the budget and bidding strategy? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 5.

### Budget & Bidding Checklist

- [ ] Realistic budget confirmed (minimum ~300 EUR per month total recommended)
- [ ] Daily budget set per campaign (~10 per day minimum)
- [ ] Bidding strategy selected (start Manual CPC)
- [ ] Expected lead volume estimated based on budget and target CPC
- [ ] Budget cap confirmed: max 25 EUR per campaign

### Budget & Bidding Details

| Aspect | Details |
|--------|---------|
| **CPC** | Typically 5-15 (well above Meta/Google) |
| **Minimum budget** | ~10/day per campaign |
| **Bidding at the start** | Manual CPC; switch to automated once conversion data exists |
| **Expectation** | Fewer clicks, but higher lead quality than other platforms |

**Phase 4 complete. Continue to Phase 5? (Yes/No)**

---

## Phase 5: Launch Checklist

Ask the user: **"Ready to launch? Shall we go through the final checklist? (Yes / no)"**

If YES: Go through each item explicitly.

### Tracking Setup

| Component | Purpose |
|------------|-------|
| **Insight Tag** | Website tracking; retargeting; conversion measurement |
| **Offline conversions** | CRM integration where available |
| **Lead Gen Forms** | Native tracking; no pixel needed |
| **UTM parameters** | Attribution in GA4 |

### Checklist Before Launch

- [ ] Insight tag installed and verified
- [ ] Audience defined (Job Title, Company, Seniority)
- [ ] Creative fits the professional context
- [ ] Lead gen form fields minimised (if used)
- [ ] Budget realistic for LinkedIn CPCs
- [ ] UTM parameters set up
- [ ] Retargeting audience defined
- [ ] Budget cap confirmed: max 25 EUR per campaign

---

## Summary: the top three actions for the next two weeks

After completing relevant phases, present the user with the 3 highest-impact next steps:

1. **[Action 1]** - [Rationale / expected impact]
2. **[Action 2]** - [Rationale / expected impact]
3. **[Action 3]** - [Rationale / expected impact]

---

## Rules (always apply)

1. **Agree a per-campaign budget cap with the user** — as with every paid channel
2. **Target narrowly** — LinkedIn is too expensive for broad targeting
3. **Lead quality beats volume** — fewer leads that convert beats many unqualified ones
4. **Professional tone** — no Facebook-speak on LinkedIn
5. **Prefer Lead Gen Forms** -- higher conversion than external landing pages

---

## Related Skills
- `/product-marketing-context` - Venture context for B2B messaging
- `/target-group` - ICP definition for targeting
- `/linkedin-organic` - Complement paid with organic
- `/sales-outreach` - Follow up on leads from ads

---

## References

- [LinkedIn Campaign Manager](https://www.linkedin.com/campaignmanager/)
- [LinkedIn Marketing Solutions](https://business.linkedin.com/marketing-solutions)
- Source: [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT)
