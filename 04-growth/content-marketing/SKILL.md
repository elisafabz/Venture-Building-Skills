---
name: content-marketing
description: Content marketing strategy — content types, formats, distribution channels, repurposing matrix, funnel mapping, editorial calendar, lead magnet planning, and LinkedIn organic posting strategy. Run /content-marketing to plan content strategy.
model: sonnet
effort: medium
---

## Step 0: Load marketing context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# Content Marketing - Strategy & Editorial Plan

Content marketing skill: content types, formats, distribution, repurposing, funnel mapping, editorial calendar.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Step 1: Intake Questions

Ask the user ALL of the following before doing anything else. Wait for all answers.

```
Ask the user:
1. What do you need? (Content Strategy / Editorial Calendar / Specific Content Piece / LinkedIn Posts / Lead Magnet)
2. What resources do you have? (Just me / Small team / Agency)
3. Do you already publish content regularly? (Yes / No)
```

Wait for all answers before proceeding.

---

## Step 2: Project context

Before you start:
- Read any existing brand notes for the brand identity and tone of voice
- Read the project's `CLAUDE.md` and `README.md`
- Ask: what is the goal? Which channels? What capacity is available?

---

## Phase 1: Content Strategy

Ask the user: "Shall we work out a content strategy (topic clusters, buyer stage mapping)? Yes / no / later"

**If YES:**

### Content types (what to create?)

| Type | Purpose | Funnel stage |
|-----|---------|-------------|
| **How-to Guides** | Educate; informational intent | Awareness |
| **Comparisons** | "X vs Y"; commercial intent | Consideration |
| **Listicles** | "Top 10", "Best X" | Consideration |
| **Case Studies** | Proof; customer success | Consideration -> Decision |
| **Product Updates** | Feature launches, release notes | Decision -> Retention |
| **Glossary** | Definitions; internal link hub | Awareness |
| **Tools / Calculators** | Linkable assets; engagement | Consideration |
| **News / Trending** | Industry news, hot topics | Awareness |
| **Onboarding** | Welcome, first steps | Retention |
| **Newsletter** | Curated insights; nurture | Retention |

### Topic Cluster Model

- **Pillar Page**: Comprehensive guide on a broad topic (2000-5000 words)
- **Cluster Pages**: Focused articles on subtopics (800-1500 words each)
- **Internal Links**: Every cluster page links to the pillar, pillar links to all clusters

Example:
Pillar: "Complete Guide to [Product Category]"
Clusters: "How to [specific use case]", "[Product] vs [Alternative]", "[Product] for [Segment]", "Best practices for [specific feature]"

Benefits:
- Establishes topical authority for SEO
- Creates natural internal linking structure
- Guides content production priorities
- Maps directly to buyer journey stages

### Buyer Stage Content Mapping

| Stage | Goal | Content Types | KPIs |
|-------|------|--------------|------|
| Awareness | Educate, attract | Blog posts, social, infographics, videos | Traffic, impressions, shares |
| Consideration | Compare, evaluate | Comparison pages, case studies, webinars, guides | Time on page, downloads, email signups |
| Decision | Convert | Product demos, free trials, testimonials, pricing pages | Signups, trials, purchases |
| Retention | Retain, expand | Help docs, newsletters, feature updates, community | NPS, churn rate, expansion revenue |

### Funnel mapping

| Stage | Content focus | Channels |
|-------|--------------|----------|
| **Awareness** | Education, thought leadership, glossary, how-tos | Blog, SEO, Social, PR |
| **Consideration** | Comparisons, case studies, demos, features | Blog, Email, Landing Pages |
| **Decision** | Pricing, testimonials, product pages | Website, Email, Sales |
| **Retention** | Onboarding, newsletter, product updates, changelog | Email, In-App, Blog |

**[ ] Phase 1 Checklist:**
- [ ] Goal defined (traffic, leads, brand, retention)
- [ ] Content types chosen (matched to the funnel)
- [ ] Topic cluster structure defined (1 pillar + 4-6 cluster pages)
- [ ] Buyer stage mapping created

**If NO:** Skip to Phase 2.

---

## Phase 2: Editorial Calendar

Ask the user: "Shall we build an editorial calendar with frequency and channel mix? Yes / no / later"

**If YES:**

### Content formats (how to deliver?)

| Format | When | Related skills |
|--------|------|-----------------|
| **Pages** | Homepage, About, Features, Pricing, Landing | `/new-page` |
| **Articles** | Blog posts, guides, listicles | `/seo` |
| **Email** | EDM, newsletter, sequences | `/email-marketing` |
| **Social posts** | LinkedIn, X, Reddit | `/linkedin-organic` |
| **Video** | Short-form, long-form, webinar | - |
| **Infographics** | Visual summaries | `/canvas-design` |
| **Slides / PDF** | Decks, whitepapers, eBooks | `/slides` |

### Frequency recommendation

| Capacity | Blog | Social | Email |
|------------|------|--------|-------|
| **Minimal** (1 person) | 2x/month | 2x/week | 2x/month |
| **Medium** (small team) | 1x/week | 3-5x/week | 1x/week |
| **Full** (dedicated team) | 2-3x/week | Daily | 2x/week |

### Editorial plan (template)

| Week | Type | Topic/Keyword | Format | Channel | Owner | Status |
|-------|-----|--------------|--------|---------|-------|--------|
| KW 16 | How-to | "SEO for SaaS" | Article + LinkedIn post | Blog, LinkedIn | [Name] | Draft |
| KW 17 | Case Study | Customer X success | Article + video | Blog, Email, YouTube | [Name] | Planned |
| KW 18 | Product Update | Feature Y | Email + social | Email, X, LinkedIn | [Name] | - |
| KW 19 | Newsletter | Curated | Email | Email | [Name] | - |

**[ ] Phase 2 Checklist:**
- [ ] Channels identified (where is the audience?)
- [ ] Frequency per channel agreed (based on capacity)
- [ ] Editorial calendar created with deadlines and owners
- [ ] Keyword research for SEO content (see `/seo`)

**If NO:** Skip to Phase 3.

---

## Phase 3: Content Prioritization

Ask the user: "Shall we prioritise the content ideas by impact versus effort? Yes / no / later"

**If YES:**

### Content prioritization (impact x effort)

Score each content idea on two axes (1-5):
- **Impact**: SEO potential + conversion potential + brand value
- **Effort**: Research time + production time + design needs

Priority order: High Impact/Low Effort > High/High > Low/Low > Low/High

### Evergreen vs. Timely

| Type | Share | Details |
|-----|-------|---------|
| **Evergreen** | 70-75% | Pillar guides, how-tos, comparisons, glossary; long-term traffic; refresh every 6-12 months |
| **Timely** | 25-30% | Seasonal, trending, news; quick spikes; often one-off |

### Article types by intent

| Intent | SEO priority | Examples |
|-------------|----------------|-----------|
| **Guides / How-to** | High | Tutorials, step-by-step, best practices |
| **Evergreen** | High | Pillar guides, glossary, comparisons |
| **News / Trending** | Medium | Industry news, hot topics; short shelf life |
| **Product Updates** | Low-Medium | Feature launches, release notes |
| **Funding / PR** | Low | Funding rounds, hires; little search volume |

**SEO-driven** (how-to, listicles, comparisons) -> target keywords, fully optimise.
**Non-SEO-driven** (funding, updates) -> clarity, shareability, internal links to SEO content.

### Content audit (existing content)

Before creating new content, review what already exists:

1. **Inventory:** list all existing pages/articles
2. **Performance:** traffic, rankings, engagement per piece
3. **Gaps:** which topics/keywords are missing?
4. **Update candidates:** what is outdated but still has potential?
5. **Delete:** what brings zero traffic and has no value?

**[ ] Phase 3 Checklist:**
- [ ] Content ideas scored by impact x effort
- [ ] Evergreen/timely mix planned (70/30)
- [ ] Existing content audited (if any)
- [ ] Repurposing plan created (1 core piece -> multiple formats)

**If NO:** Skip to Phase 4.

---

## Phase 4: Lead Magnet Planning

Ask the user: "Shall we develop a lead magnet strategy? Yes / no / later"

**If YES:**

### What Makes a Good Lead Magnet

A lead magnet works when it:
- Solves ONE specific problem (not "everything about topic X")
- Delivers a quick win (usable in under 10 minutes)
- Is genuinely valuable (the user would pay for it if it wasn't free)
- Relates to your paid product (the problem it solves is adjacent to what you sell)
- Has a specific, benefit-driven title

A lead magnet fails when it:
- Is vague ("Marketing Guide 2024")
- Requires too much time investment to get value
- Has no connection to your product (attracts wrong audience)
- Is just a product brochure in disguise

### Types by Buyer Stage

| Stage | Buyer Mindset | Best Lead Magnet Types | Email List Value |
|-------|--------------|----------------------|-----------------|
| **Awareness** | "I have a problem but don't know solutions" | Checklist, infographic, quiz | Lower - top of funnel |
| **Consideration** | "I'm researching options" | Template, toolkit, comparison guide | Medium |
| **Decision** | "I'm ready to buy, just choosing who" | Case study, ROI calculator, free trial | High - hot leads |
| **Retention** | Existing customer | Advanced guide, certification, insider tips | Increases LTV |

**Rule:** One lead magnet per stage. Start with one that serves your most common buyer stage, then expand.

### Lead Magnet Types and When to Use Each

**Checklist**
- Best for: Awareness stage, process-heavy topics
- Format: 1-2 pages, PDF or web page
- Title pattern: "The [Number]-Step Checklist for [Specific Task]"
- Conversion potential: High (fast to consume, easy to understand value)

**Template**
- Best for: Consideration stage, tasks people do repeatedly
- Format: Google Doc, Notion page, spreadsheet, Figma file
- Title pattern: "[Role/Industry] [Task] Template (Copy-Paste Ready)"
- Conversion potential: High (immediate utility)

**Ebook / Guide**
- Best for: Consideration stage, complex topics needing explanation
- Format: PDF, 10-30 pages
- Title pattern: "The Complete Guide to [Goal] for [Audience]"
- Conversion potential: Medium (high perceived value, lower immediate utility)
- Warning: Only do this if you can write genuinely useful content. Generic ebooks hurt trust.

**Mini-course / Email course**
- Best for: Consideration to Decision stage
- Format: 5-7 emails over 5-7 days, each one teaching one thing
- Title pattern: "[Number]-Day [Skill] Course (Free)"
- Conversion potential: High (repeated touchpoints build trust, natural upsell at end)

**ROI Calculator / Interactive tool**
- Best for: Decision stage
- Format: Web-based calculator or spreadsheet
- Title pattern: "Calculate How Much [Your Category] Could Save You"
- Conversion potential: Very high (creates personalized value, shows your solution's impact)

**Case study / Success story**
- Best for: Decision stage
- Format: PDF, 2-4 pages, or web page
- Title pattern: "How [Company Type] Achieved [Result] with [Your Category]"
- Conversion potential: Very high (proof-based, high intent signal)

**Webinar / Workshop**
- Best for: Consideration to Decision stage
- Format: Live or recorded, 45-60 minutes
- Conversion potential: High (highest engagement, easiest direct ask at end)
- Cost: High effort to produce

**Quiz**
- Best for: Awareness stage, high-traffic content
- Format: Interactive, 5-10 questions, personalized result at end
- Title pattern: "What Type of [X] Are You?" or "How Mature Is Your [Process]?"
- Conversion potential: High for list growth, lower purchase intent

### Title Formulas That Work

- "The [Number]-Point [Topic] Checklist for [Audience]"
- "[Number] [Format]s for [Specific Goal]"
- "How to [Achieve Result] in [Short Timeframe] (Without [Common Obstacle])"
- "The [Audience] [Topic] Toolkit: [Number] Ready-to-Use [Resources]"
- "Free [Calculator/Audit/Assessment]: [Specific Benefit]"
- "The [Year] [Industry] [Topic] Guide (Updated [Month])"

**Bad title examples (too vague):**
- "Marketing Ebook"
- "Complete Business Guide"
- "Free Resources"

### Delivery Mechanics

**Immediate delivery (required):**
- Show download link on the thank-you page immediately after form submit
- Do NOT say "check your email" - users may not open it
- Also send via email (for tracking and re-access)

**Email nurture sequence after signup:**
- Email 1 (immediate): Delivery + welcome + what to expect
- Email 2 (day 2): One quick-win tip related to the lead magnet topic
- Email 3 (day 4): Deepen the topic + soft mention of your product
- Email 4 (day 7): Case study or social proof
- Email 5 (day 10): Direct offer (free trial, demo, or paid product)

**Segmentation:**
- Tag subscribers by which lead magnet they downloaded
- Use different nurture sequences per lead magnet (stage-appropriate)
- Score leads higher if they download a decision-stage magnet

### Landing Page and Form Optimization

**Landing page structure:**
1. Headline: Specific benefit, who it's for
2. Visual: Show a preview (cover page, screenshot of template)
3. Bullet points: 3-5 specific things they'll get
4. Social proof: "[Number]+ downloads" or "[Person] said [quote]"
5. Form: Email only (name optional). Never ask for phone number on a free magnet.
6. CTA button: "Get the [specific thing]" not "Submit"

**Conversion benchmarks:**
- Generic landing page: 10-20% conversion
- Strong lead magnet landing page: 30-50%
- If below 15%, test: headline, visual preview, or offer relevance

**A/B test priority:**
1. Headline (biggest impact)
2. Visual (show more of the content)
3. Bullet copy (benefits vs. features)
4. CTA button text

### Lead Magnet Roadmap

| Priority | Stage | Type | Timeline |
|----------|-------|------|----------|
| 1 | Most common buyer stage | Fastest to produce (checklist or template) | Week 1-2 |
| 2 | Adjacent stage | Second highest impact type | Month 1 |
| 3 | Decision stage | ROI calculator or case study | Month 2-3 |

**[ ] Phase 4 Checklist:**
- [ ] Buyer stage analysis done (where most leads are today)
- [ ] 3 lead magnet concepts defined (type, title, format)
- [ ] Priority recommendation clear (which to build first)
- [ ] Title options for top-priority magnet (3-5 variations)
- [ ] Landing page copy outline created
- [ ] Email nurture sequence structure planned (5 emails)
- [ ] Distribution plan defined (where to promote each magnet)

**If NO:** Skip to Phase 5.

---

## Phase 5: LinkedIn Organic Strategy

Ask the user: "Shall we develop a LinkedIn posting strategy? Yes / no / later"

**If YES:**

### Character Limits

| Element | Limit | Note |
|---------|-------|------|
| **Post total** | 3,000 characters | Optimal: 1,300-1,600 |
| **First line (critical!)** | 210-235 characters | Visible before "see more"; 60-80% decide here |
| **Short posts** | 100-200 characters | Polls, announcements, quotes |

### Optimal length by content type

| Type | Characters | When |
|-----|------|-----|
| **Short** | 100-200 | Polls, announcements, quotes |
| **Medium** | 300-1,200 | Case studies, tips, behind the scenes |
| **Long** | 1,200-2,000 | Thought leadership, analysis |
| **Sweet spot** | 1,300-1,600 | Highest engagement |
| **Avoid** | >2,000 | ~35% engagement drop |

### Hook formulas (first line = everything)

The first 140 characters decide whether anyone taps "see more".

| Formula | Example |
|--------|----------|
| **A concrete result** | "We raised our conversion rate by 340%. Here is how we did it:" |
| **Pain point** | "The biggest problem in B2B SaaS? Nobody understands your pricing." |
| **Bold claim** | "90% of landing pages make the same mistake." |
| **A surprising statistic** | "Only 3% of Product Hunt launches lead to real customers." |
| **A personal story** | "Six months ago we had zero users. Today we have 2,400." |
| **Contrarian** | "Content marketing is not dead. Your content is just boring." |

**What NOT to use as a hook:**
- Vague teasers: "I have something to tell you..."
- Hashtag-first: "#startup #growth"
- Generic greetings: "Good morning LinkedIn community!"
- Self-praise: "I am so proud..."

### Post formats by reach ranking

| Format | Reach | When |
|--------|-------|------|
| **Polls** | Highest reach | Opinions, quick engagement |
| **Document/Carousel** | Very high | Tutorials, frameworks, step-by-step |
| **Single image** | High | Statements, infographics, screenshots |
| **Text-only** | Good | Personal stories, hot takes |
| **Video** | Medium | Behind the scenes, demos |
| **Link post** | Lowest reach | LinkedIn penalises external links; workaround: link in first comment |

**Workaround for links:** publish the post without a link and put the link in the first comment. The LinkedIn algorithm favours posts that keep users on the platform.

### Image specs

| Format | Size | When |
|--------|------|------|
| **Single image** | 1200x627 (1.91:1) | Feed; link previews |
| **Square** | 1200x1200 | Single image |
| **Carousel** | Up to 20 images | Multi-image posts; PDFs |
| **File size** | Max 10 MB; JPG/PNG | Native uploads perform better |
| **Vertical** | Preferred | 88% browse on mobile |

### Content pillars (template)

Choose three to five content pillars and rotate through them:

| Pillar | Example | Frequency |
|--------|----------|----------|
| **Behind the Scenes** | Day-to-day work, learnings, mistakes | 1x/week |
| **Industry Insights** | Trends, data, opinions | 1x/week |
| **How-to / tips** | Practical tips from your field | Once a week |
| **Social Proof** | Customer wins, testimonials, milestones | 1-2x/month |
| **Personal Story** | Founder journey, reflections | 1-2x/month |

### Hashtags

- **3-5 hashtags** at the end of the post (not in the body)
- Mix broad tags (#startup, #saas) with niche ones (#b2bmarketing, plus a local or sector tag your audience follows)
- No more than 5 - otherwise it looks spammy

### Posting frequency and timing

| Aspect | Recommendation |
|-----------|-----------|
| **Minimum** | 2-3x/week (Company Page); 3-5x/week (Personal) |
| **Best days** | Tuesday to Thursday |
| **Best times** | 7-9 am, 12 pm, 5-6 pm (audience time zone) |
| **Consistency** | Regular > sporadic bursts |

### Engagement tactics

| Tactic | Details |
|--------|---------|
| **Reply to comments** | Within 1-2 hours; the algorithm rewards it |
| **Ask questions** | At the end of the post, to prompt discussion |
| **Tag others** | Only where relevant; do not spam-tag |
| **Engage before and after posting** | Comment on other posts for 15 minutes before and after yours |
| **Alt text** | Add for images (accessibility + SEO) |

### LinkedIn rules

1. **The hook is everything** — the first line decides 80% of the outcome
2. **No external links in the post** - link in first comment
3. **Mobile first** — 88% are on mobile; short paragraphs, plenty of white space
4. **Authentic > polished** - LinkedIn rewards real stories
5. **Consistency > perfection** - better regularly good-enough than rarely perfect
6. **No corporate speak** — write like a human, not like a press release

### LinkedIn output format

When generating a LinkedIn post, deliver:
1. **First line** (max 210 characters; hook)
2. **Full post** with character count
3. **Hashtags** (3-5; at the end)
4. **Recommended format** (text, image, carousel, poll)
5. **Image specs** (if visual)

**[ ] Phase 5 Checklist:**
- [ ] 3-5 content pillars defined
- [ ] Posting frequency set
- [ ] Hook formula chosen for each post type
- [ ] Engagement routine defined (reply, comment before/after posting)

**If NO:** Skip to Phase 6.

---

## Phase 6: Content Repurposing Plan

Ask the user: "Shall we create a repurposing plan (1 content piece -> multiple formats)? Yes / no / later"

**If YES:**

### Repurposing Matrix

**Principle:** one core piece -> multiple formats -> multiple channels. Maximise ROI.

| Core content | -> Formats | -> Channels |
|-------------|-----------|-----------|
| **Case Study** | Article, video, infographic, slides | Blog, Email, LinkedIn, YouTube, Sales Deck |
| **How-to Guide** | Article, video, checklist, PDF | Blog, Email, YouTube, Docs |
| **Product Update** | Article, email, social post, video | Blog, Email, X, LinkedIn, Changelog |
| **Industry Insight** | Article, podcast, post, newsletter | Blog, Spotify, X, Email |

**Example:** one customer success story → an article (blog) + a video (YouTube) + an infographic (LinkedIn) + slides (sales) = four channels from one piece of work.

### Content Repurposing Matrix (LinkedIn)

| Source Content | LinkedIn Format | Effort |
|---------------|----------------|--------|
| Blog post | Text post (key insight) | Low |
| Blog post | Carousel (step-by-step) | Medium |
| Webinar | Video clip (best 60s) | Medium |
| Case study | Before/after story post | Low |
| Data report | Chart + insight post | Low |
| Podcast episode | Quote graphic + thread | Medium |
| Customer interview | Testimonial story | Low |

**Cross-Platform Workflow:**
1. Create core content (blog, video, podcast)
2. Extract 3-5 key insights
3. Format each insight for LinkedIn (text, carousel, or image)
4. Schedule across 1-2 weeks
5. Repurpose top performers to other platforms

**[ ] Phase 6 Checklist:**
- [ ] A repurposing plan created for the first three pieces of content
- [ ] Each content piece adapted into at least 2 formats
- [ ] Cross-platform workflow defined

**If NO:** Proceed to Summary.

---

## Summary: Next 3 Content Pieces

After all phases, always deliver this summary:

**Ask the user:** "Which three pieces of content should we create first?"

Then provide:

1. **Content Piece 1** - Type, title, format, channel, owner, deadline
2. **Content Piece 2** - Type, title, format, channel, owner, deadline
3. **Content Piece 3** - Type, title, format, channel, owner, deadline

Plus a mini editorial calendar for the next 4 weeks.

**[ ] Final Checklist:**
- [ ] Goal defined (traffic, leads, brand, retention)
- [ ] Content types chosen (matched to the funnel)
- [ ] Channels identified (where is the audience?)
- [ ] Repurposing plan created (1 core piece -> multiple formats)
- [ ] Evergreen/timely mix planned (70/30)
- [ ] Editorial calendar with deadlines and owners
- [ ] Existing content audited
- [ ] Keyword research for SEO content (see `/seo`)

---

## Related Skills
- `/product-marketing-context` - Positioning and audience foundation
- `/seo` - SEO optimization for content
- `/ai-seo` - Optimize for AI search engines
- `/email-marketing` - Distribute content via email
- `/popup-cro` - Optimize lead magnet capture forms

## References

- [Content Marketing Institute](https://contentmarketinginstitute.com/)
- [LinkedIn Marketing Solutions](https://business.linkedin.com/marketing-solutions)
