---
name: competitor-research
description: Research and analyze competitors - structured profiles, website analysis, SEO data, feature comparison, positioning maps, and SEO-optimized comparison pages ("[Product] vs [Competitor]", "Best Alternatives"). Uses Firecrawl for scraping. Run /competitor-research to analyze competitors.
model: sonnet
effort: medium
---

# Competitor Profiling Skill

> **Requires:** web fetch; Firecrawl optional.

You are a competitive intelligence analyst. Create structured, actionable competitor profiles by combining website analysis, pricing research, feature mapping, and positioning analysis. Use Firecrawl for scraping when available. Output clean, comparable profiles across all competitors.

## Step 0: Marketing Context laden

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

---

## Phase 1: Identify Competitors to Profile

Ask the user to confirm or provide:
1. List of direct competitors (same product category, same audience)
2. List of indirect competitors (different approach, same problem)
3. List of alternative solutions (how the target audience currently solves the problem without a dedicated tool)

**Why this matters:** Direct competitors are who you fight for same-intent users. Indirect competitors shape how users think about the problem. Alternatives show what you are actually being compared to in buying decisions.

Start with 3-5 direct competitors. Add indirect and alternatives only after direct profiles are complete.

---

## Phase 2: Research Process (Per Competitor)

### Step 1: Homepage and Positioning

If Firecrawl is available, use `/firecrawl` to scrape:
- Homepage (`/`)
- Pricing page (`/pricing`)
- About page (`/about` or `/company`)
- Blog homepage (to understand content strategy and audience)

If Firecrawl is not available, ask the user to paste the homepage copy, or use WebFetch.

Extract from homepage:
- Hero headline and subheadline (this is their positioning statement)
- Primary CTA copy
- How they describe their target customer
- Key benefit claims
- Trust signals used (logos, numbers, testimonials)

---

### Step 2: Pricing Research

Scrape or manually record:
- Number of pricing tiers
- Tier names
- Monthly price per tier
- Annual price per tier (and discount %)
- What is included in each tier
- What is locked behind paid tiers
- Free trial? Freemium? Demo? No self-serve?
- Payment required to start?

**Note:** If pricing is not public ("Contact us"), that is itself a data point - signals enterprise-first motion or high ACV (Annual Contract Value - the amount one customer pays per year).

---

### Step 3: Feature Research

Sources:
- Features page or product tour on their website
- G2 / Capterra reviews (read reviews to understand features customers mention)
- Changelog / release notes (shows what they are building now)
- Job postings (what engineering roles they hire for reveals product direction)

---

### Step 4: Marketing and Traffic Estimation

Check:
- Social media presence (LinkedIn, Twitter/X, Instagram) - followers and recent post engagement
- Content marketing: do they have a blog? How often do they publish? What topics?
- SEO visibility: use Semrush/Ahrefs estimates if available, or check organic presence manually
- Paid advertising: search their brand name in Google - are they running ads? Check Meta Ad Library for their Facebook/Instagram ads.
- Community presence: are they active in Reddit, Slack communities, Discord?

---

### Step 5: Company Intelligence

From Crunchbase, LinkedIn, and their website:
- Founded year
- Funding raised (amount + latest round)
- Team size (approximate, from LinkedIn)
- Headquarters location
- Key investors (signals strategic direction and resources)

---

## Phase 3: Competitor Profile Template

Complete one profile per competitor. Store output as markdown.

```markdown
# Competitor Profile: [Company Name]

**URL:** [website]
**Founded:** [year]
**Headquarters:** [city, country]
**Team size:** [approximate]
**Funding:** [total raised, latest round, year]
**Key investors:** [if notable]

---

## Positioning

**Hero headline:** "[exact quote from homepage]"
**Subheadline:** "[exact quote]"
**Target audience (as they describe it):** [quote or paraphrase]
**Positioning statement (summarized):** [1-2 sentence synthesis]

---

## Pricing

| Tier | Monthly | Annual | Key Limits |
|------|---------|--------|------------|
| [Tier name] | €/$ | €/$ | [users, projects, etc.] |
| [Tier name] | €/$ | €/$ | |
| [Tier name] | €/$ | €/$ | |

**Free trial:** [Yes/No + duration]
**Freemium:** [Yes/No + what is free]
**Credit card required to start:** [Yes/No]

---

## Core Features

- [Feature 1]
- [Feature 2]
- [Feature 3]
- [...]

**Notable differentiators (features only they have):**
- [Unique feature 1]
- [Unique feature 2]

**Notable gaps (features users complain about missing):**
- [Gap 1 - from G2/Capterra reviews]
- [Gap 2]

---

## Marketing Channels

| Channel | Active? | Notes |
|---------|---------|-------|
| SEO / Content | [Yes/No] | [estimated traffic, publishing frequency] |
| Paid Search | [Yes/No] | [branded? non-branded?] |
| Paid Social | [Yes/No] | [platform, estimated spend level] |
| LinkedIn | [Yes/No] | [followers, engagement level] |
| Community | [Yes/No] | [which communities] |
| Product Hunt | [Yes/No] | [launch date, upvotes] |
| Partnerships | [Yes/No] | [known integrations or partners] |

---

## Trust Signals Used

- [Social proof type + example]
- [Authority signal]
- [Numbers/stats they display]

---

## Customer Reviews Summary

**G2 rating:** [X.X/5] from [N] reviews
**Capterra rating:** [X.X/5] from [N] reviews

**What customers love:**
- [Theme 1]
- [Theme 2]

**What customers complain about:**
- [Complaint 1]
- [Complaint 2]

---

## SWOT (from our perspective)

**Strengths:** [what they do well that we need to respect]
**Weaknesses:** [where they are vulnerable]
**Opportunities:** [gaps we can exploit]
**Threats:** [how they could hurt us]

**Counter-Positioning check** (7 Powers, Hamilton Helmer): [Which business model could this competitor NOT copy without cannibalizing their existing revenue or channel? "Better features" they can always match — a conflicting business model they cannot. If such a model exists, it is our strongest strategic angle; if none exists, our differentiation must come from another of the 7 Powers.]

---

## Profile last updated: [date]
```

---

## Phase 4: Feature Comparison Matrix

After profiling all competitors, create a comparison matrix.

```markdown
# Feature Comparison Matrix

| Feature | [Our Product] | [Competitor A] | [Competitor B] | [Competitor C] |
|---------|--------------|----------------|----------------|----------------|
| [Feature 1] | ✓ | ✓ | ✓ | - |
| [Feature 2] | ✓ | - | ✓ | - |
| [Feature 3] | ✓ | - | - | - |
| [Feature 4] | - | ✓ | ✓ | ✓ |
| [Feature 5] | Partial | ✓ | - | ✓ |

Legend: ✓ = full support / Partial = limited support / - = not available
```

**How to use this matrix:**
- Rows where only we have ✓ = our unique differentiators (use in marketing)
- Rows where we have - and everyone else has ✓ = gaps to address or acknowledge
- Rows where everyone has ✓ = table stakes, do not over-emphasize

---

## Phase 5: Positioning Map (2x2)

Choose the two dimensions most meaningful in your market. Plot all competitors on a 2x2 grid.

**Common dimension pairs:**
- Price (low/high) vs. Feature breadth (narrow/broad)
- Ease of use (simple/complex) vs. Power (limited/advanced)
- Self-serve (DIY) vs. Service (full-service)
- SMB-focused vs. Enterprise-focused
- Specialist vs. Generalist

**How to present as text:**
```
High Price / High Feature breadth: [Competitor A], [Competitor B]
High Price / Low Feature breadth: [Competitor C]
Low Price / High Feature breadth: [Our Product], [Competitor D]
Low Price / Low Feature breadth: [Competitor E]
```

**The white space:** Look for a quadrant no one occupies. That is your potential positioning opportunity — strongest when occupying it would force incumbents to cannibalize their own model to follow (Counter-Positioning; 7 Powers, Helmer). But verify it is empty because incumbents CAN'T go there, not because nobody wants it (No-Need-Fail, Failbook/VNTR).

---

## Phase 6: Intelligence Sources Quick Reference

| Source | What you get | Cost |
|--------|-------------|------|
| Competitor website | Positioning, features, pricing | Free |
| G2.com | Reviews, ratings, competitor comparison | Free (some behind paywall) |
| Capterra.com | Reviews, ratings | Free |
| Crunchbase | Funding, team size, investors | Free (basic) |
| LinkedIn company page | Team size, hiring activity, content | Free |
| Meta Ad Library | Active Facebook/Instagram ads | Free |
| Google search (brand name) | Paid search ads they run | Free |
| Product Hunt | Launch history, upvotes, comments | Free |
| Changelog / blog | Product direction, release velocity | Free |
| Job postings | Strategic direction, tech stack | Free |
| SimilarWeb / Semrush | Traffic estimates, keyword data | Paid |
| Firecrawl | Automated scraping of pages | Paid (use /firecrawl skill) |

---

## Phase 7 Gate: Comparison Pages

Before proceeding to maintenance, ask:

**"Shall I also create SEO-optimized comparison pages ([Product] vs [Competitor])? Yes/No"**

If YES: Continue to the "Comparison & Alternatives Pages" section below.
If NO: Skip to the Summary.

---

### Summary (if skipping Comparison Pages)

Deliver:
1. Individual markdown profiles per competitor (saved to `.agents/competitors/[competitor-name].md`)
2. Feature comparison matrix (saved to `.agents/competitors/comparison-matrix.md`)
3. Positioning map summary (saved to `.agents/competitors/positioning-map.md`)
4. 3-5 strategic takeaways for the user

Then stop here.

---

## Phase 8: Competitive Intelligence Maintenance

A competitor profile is out of date the moment it is written. Build a lightweight refresh process:

**Monthly (15 min):**
- Check competitor pricing pages for changes
- Scan their changelog or blog for new features
- Check job postings for shifts in hiring direction

**Quarterly (1 hour):**
- Full profile refresh
- Read new G2/Capterra reviews
- Update feature comparison matrix
- Check funding news (Crunchbase)

**Trigger-based (immediate):**
- Competitor raises a funding round - update immediately
- Competitor launches a new major feature - assess impact
- You lose a deal to a specific competitor - interview the customer who chose them

---

## Output Format

Deliver:
1. Individual markdown profile per competitor (saved to `.agents/competitors/[competitor-name].md`)
2. Feature comparison matrix (saved to `.agents/competitors/comparison-matrix.md`)
3. Positioning map summary (saved to `.agents/competitors/positioning-map.md`)
4. Competitive summary with 3-5 strategic takeaways for the user

---

---

## Comparison & Alternatives Pages

After profiling competitors, use this research to build high-intent SEO pages. People searching "[Competitor] alternative" or "[Product A] vs [Product B]" are buying, not browsing - conversion rates are 10-20x typical blog posts.

### Page Types and When to Use Each

**Type 1: "[Our Product] vs [Competitor]" - 1v1 Comparison**
Use when: head-to-head competition, clear differentiation, competitor has meaningful search volume.
Target audience: people who know both products and are deciding between them.

**Type 2: "[Competitor] Alternatives" - Targeted at Competitor's Audience**
Use when: competitor has significant market share, their users have documented frustrations.
Target audience: competitor's customers who are unhappy and searching for options.
Important: this page type mentions multiple alternatives - you present as one option (ideally best for your segment).

**Type 3: "Best [Category] Software" - Listicle**
Use when: category has good search volume, you can credibly compete for the keyword.
Target audience: early-stage buyers just starting to research options.

**Type 4: "Switching from [Competitor]" - Migration Guide**
Use when: you have a migration tool or clear process, competitor is larger than you.
Target audience: competitor's dissatisfied customers ready to switch but fearing the effort.

### The Fairness Principle

Honest comparisons outperform biased ones:
1. Readers already know the competitor's strengths - if you pretend the competitor is terrible, they distrust your entire page
2. Fair comparisons rank better in Google - they match search intent more accurately
3. Fair comparisons convert better - readers who see honest trade-offs and still choose you are higher-quality leads

**What honesty looks like:**
- Acknowledge where the competitor is genuinely stronger
- Use real feature data, not vague claims
- Neutral language in comparison table (checkmarks/X, not "amazing"/"terrible")
- State your honest recommendation: "Choose [Competitor] if X. Choose [Us] if Y."

### Page Structure: "[Product] vs [Competitor]"

**Section 1: Hero**
- Headline: "[Our Product] vs [Competitor]: Which is right for you?"
- Subheadline: 1-2 sentences stating what each product is best for
- Do NOT write "Why [Our Product] is better" - signals bias immediately

**Section 2: Quick Summary Table**
```
| | [Our Product] | [Competitor] |
|---|---|---|
| Best for | [ideal customer] | [ideal customer] |
| Pricing starts at | EUR X/month | EUR X/month |
| Free trial | 14 days | 7 days |
| [Key feature 1] | yes | yes |
| [Key feature 2] | yes | - |
| [Key feature 3] | - | yes |
```

**Section 3: Detailed Feature Breakdown**
Go deeper on 4-6 key decision areas. For each: explain what it is and why it matters, describe how each product handles it (factually), state which product wins on this dimension (should NOT always be you).

**Section 4: Pricing Comparison**
Full pricing breakdown for both products including: all tiers and prices, annual vs. monthly, hidden costs (seats, storage, add-ons), total cost of ownership for a typical customer.

**Section 5: Who Should Choose Each**
```
Choose [Our Product] if:
- You are [specific situation]
- You need [specific feature]

Choose [Competitor] if:
- You need [their strength]
- You are [their target customer]
```

**Section 6: CTA**
- Primary: "Start free trial"
- Secondary: "See all features" or "Compare pricing"
- Optional: live chat trigger for undecided visitors

### Page Structure: "[Competitor] Alternatives"

**Section 1: Hero**
- Headline: "Best [Competitor] Alternatives in [Year]"
- Subheadline: acknowledge why someone might be looking (their key weakness from reviews)

**Section 2: Quick Summary Table**
```
| Tool | Best for | Starting price | Free trial? |
|------|----------|---------------|------------|
| [Our Product] | [use case] | EUR X/mo | Yes |
| [Alternative 2] | [use case] | EUR X/mo | Yes |
```

**Section 3: Detailed Reviews (one per alternative)**
For each: what it is, top strengths, limitations/who it is NOT for, pricing. Add CTA only for your own product.

**Section 4: How to Choose**
"If you need [criteria] -> [product]"

**Section 5: FAQ (3-5 questions)**
"Is [Competitor] worth the cost?" / "What is the cheapest [Competitor] alternative?" / "Can I migrate my data?"

### SEO On-Page Optimization for Comparison Pages

**URL structure:**
- `/vs/[competitor-slug]` or `/compare/[our-product]-vs-[competitor]`
- `/alternatives/[competitor-slug]`

**Title tag:**
- "[Our Product] vs [Competitor]: Honest Comparison [Year]"
- "Best [Competitor] Alternatives in [Year] (Free & Paid)"
Include year - signals freshness, users prefer recent comparisons.

**Meta description (155 chars):**
Include: both product names, key differentiator, CTA.

**Internal linking:**
- Link from comparison page to relevant feature pages
- Link from blog posts about related topics to comparison pages
- Link from homepage or pricing page to key comparisons

**Update frequency:** At minimum annually (update year in title). Update whenever competitor changes pricing or features.

### Keyword Strategy for Comparison Pages

**Direct comparison queries:**
- "[Our product] vs [Competitor]"
- "[Competitor] alternative" / "[Competitor] alternatives"

**Category queries:**
- "Best [category] software"
- "[Category] software comparison"

**Switching queries:**
- "How to migrate from [Competitor] to [Our product]"
- "[Competitor] pricing too high"

**Prioritization:** Build pages for competitors where search volume is meaningful AND you have a credible differentiation story. Do NOT build comparison pages for competitors in a completely different market segment - it confuses your positioning.

### Content Quality Checklist

**Accuracy:**
- [ ] Competitor pricing verified on their website today
- [ ] Feature claims verified (not from memory or old data)
- [ ] No outdated screenshots
- [ ] All links working

**Fairness:**
- [ ] Competitor's genuine strengths acknowledged
- [ ] "Choose [Competitor] if" section is honest
- [ ] Language in comparison table is neutral
- [ ] No misleading feature cherry-picking

**SEO:**
- [ ] Primary keyword in title tag, H1, first 100 words
- [ ] Year in title tag
- [ ] Meta description written
- [ ] Internal links to feature/pricing pages
- [ ] FAQPage schema for FAQ section

**Conversion:**
- [ ] CTA visible without scrolling (above the fold)
- [ ] CTA repeated at bottom
- [ ] Trust signals near CTA (trial terms, "no credit card", etc.)
- [ ] Mobile rendering checked

---

## Related Skills

- `/product-marketing-context` - baseline positioning to compare competitors against
- `/seo` - use competitor keyword gaps from this research and technical SEO for comparison pages
- `/target-group` - competitor audiences inform our own targeting
