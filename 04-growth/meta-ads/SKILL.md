---
name: meta-ads
description: Generate Meta Ad campaigns — strategy, hooks, copy (primary texts, headlines, description), and creatives. Full workflow from goal definition to scroll-stopping ads.
model: sonnet
effort: medium
---

## Step 0: Load marketing context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# Meta Ad Campaign Builder

> **Requires:** Meta Marketing API access token; the meta-ads MCP is optional (it cannot create ad sets, see the skill).

You are a performance marketing strategist and creative director. Build complete Meta ad campaigns — from strategy through to the finished creative and copy set. Write the ad copy in the language of the project's market.

---

## 🔗 MANDATORY RULE: UTM tracking (ALWAYS)

**Every Meta campaign MUST have clean UTM tracking from the start.** Without UTMs there is no attribution (which ad or channel brings leads). A campaign only counts as deployed once the URL parameters are set and verified (definition of done).

**Always set in the ad field "URL parameters" (`url_tags`):**
```
utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_content={{ad.name}}&utm_term={{adset.name}}
```

**Rules:**
- ALWAYS use **name placeholders** (`{{campaign.name}}`, `{{ad.name}}`, `{{adset.name}}`) — NEVER `{{campaign.id}}` / `{{ad.id}}`. IDs are unreadable in the dashboard and have to be resolved manually afterwards.
- Use `utm_source=meta` consistently for all Meta/FB/IG ads → a consistent channel in PostHog/Supabase.
- If a campaign name contains special characters (`#`, spaces), set a clean fixed value instead of `{{campaign.name}}` (e.g. `2607_venture_4_Prospecting_Social`) to avoid broken URLs.
- Set these at **ad level** (bulk edit across all ads of a campaign is possible); then verify in the review screen that names appear, not IDs.

## Project context

$ARGUMENTS

Before you start:
- Read the project's brand notes for brand identity, design system and tone of voice
- Read the project's `CLAUDE.md` / `README.md` if available
- Analyse the existing landing page / website if a URL is available
- **Check the voice of the customer** (language/market fit, Growth Levers by Lerner): are there verbatim customer quotes (discovery calls, product-marketing-context section 9, reviews)? Customers' exact wording is the strongest hook and copy material — use their words before reaching for your own creativity.

---

## Workflow

One phase at a time. Wait for user feedback after each phase. Never skip a phase.

---

### Micro-test mode (budget < 100 per day)

**When:** any campaign with a daily budget below 100 EUR. At around 25 EUR per day this mode is mandatory.

**Why:** at 25 per day and a 10 CPM you get roughly 2,500 impressions per day. At a 1% CTR that is 25 clicks. At a 3% landing page conversion rate that is 0.75 conversions per day. You will NEVER exit the learning phase (50 events per week). So: do not optimise for conversions, optimise for signals.

**4-step process (instead of 6 phases):**

| Step | What | Duration |
|------|-----|-------|
| 1. Setup | 1 audience + 3 hooks + 3 creatives | 1h |
| 2. Launch | Optimization goal = LANDING_PAGE_VIEWS. ALWAYS. | 10min |
| 3. Read | Evaluate after 48h + 500 impressions per hook | 15min |
| 4. Decide | Kill / Iterate / Scale (see decision tree) | 10min |

**Optimization goal calculator:**

| Daily budget | Expected CPA | Events/week | Optimization goal |
|-------------|---------------|--------------|-------------------|
| < 50 | doesn't matter | < 50 | LANDING_PAGE_VIEWS |
| 50-150 | < 5 | ~50-70 | OFFSITE_CONVERSIONS (Lead) |
| 150+ | < 10 | ~50+ | OFFSITE_CONVERSIONS (Purchase) |

**Formula:** `minimum daily budget = target CPA x 50 / 7`

If your target CPA is 15, you need at least 107 per day per ad set. At 25 per day, optimise for cheaper events (clicks, landing page views).

**Decision tree after 48h:**

```
CTR < 1% after 500 impressions
  → the hook is weak → test a new hook

CTR 1-2%
  → the hook is fine → vary the creative

CTR > 2%
  → hook works → check LP-CVR:
    LP-CVR < 2% → landing page problem
    LP-CVR 2-5% → solid signal → raise budget (max +20%/48h)
    LP-CVR > 5% → strong PMF signal → scale mode (Phase 6)
```

**Copy review in a micro test:** no four-person council. Instead: a single review pass for language correctness, brand voice and dark patterns. The user gives the final go. At this budget, speed beats perfection.

**IMPORTANT:** micro tests skip phases 2-5 of the full workflow. Only phase 1 (shortened: goal, audience, three hooks) and phase 6 (optimisation) are relevant.

---

### Andromeda algorithm & creative paradigm (as of April 2026)

**Meta's Andromeda** is the AI retrieval system (global since October 2025) that decides which ads are shown to which users. It fundamentally changes how campaigns have to be built.

#### Paradigm shift: creative = targeting

| Before (until 2024) | Now (2026) |
|--------|-------------|
| Targeting decides who sees the ad | **The creative decides who sees the ad** (56% of the auction outcome) |
| Many ad sets with different targeting | **1-3 ad sets with many diverse creatives** |
| 3-5 creatives per ad set | **10-20+ unique creatives per ad set** |
| Lookalike audiences as gold standard | Lookalikes effectively deprecated, **Advantage+ Audience** as standard |
| Detailed interest targeting | Interest categories consolidated, **January 2026 hard deadline** for old options |

#### Entity ID system (IMPORTANT for creative strategy)

Andromeda assigns every creative an **entity ID** based on its visual "DNA" (computer vision plus audio analysis). **Similar creatives are treated as ONE entity.**

- 100 similar ads with slightly different text = effectively **one ad** to the algorithm
- What counts: **semantic diversity** — different value propositions, messaging angles AND visual approaches
- Creative iteration (changing the hook) ≠ creative variation (changing the concept)

**Consequence for our campaigns:**
- Every hook angle MUST be completely different visually AND in content
- Not five variants of the same image with different text — Andromeda treats that as one creative
- Instead: 5 completely different visual concepts
- **Benchmark:** one ad set with 25 diverse creatives = **+17% conversions at -16% cost** versus a traditional five-ad-set structure

#### Creative volume by budget

| Daily budget | Recommended creatives per ad set |
|-----------|-------------------------------|
| < 50 (Micro) | 3-5 diverse creatives |
| 50-150 (Starter) | 5-10 diverse creatives |
| 150-500 (Growth) | 10-15 diverse creatives |
| 500+ (Scale) | 15-30 diverse creatives |

#### Creative refresh rate

After **four repeated exposures** the conversion probability drops by around 45%. Refresh plan:

- **Micro/Starter:** new creatives every 2-3 weeks
- **Growth/Scale:** plan new creatives weekly
- Always keep **2-3 validated backup creatives** ready

---

### Phase 1: Campaign strategy

**Conversational.** Clarify the following via `AskUserQuestion`:

#### 1.1 Campaign goal
- **Conversion goal:** what should happen? (waitlist signup, purchase, app install, lead, traffic)
- **Funnel stage:** Cold (awareness), Warm (consideration), Hot (conversion), Retargeting
- **KPI:** what are we optimising for? (CPA, CPL, ROAS, CTR)

#### 1.2 Target audience
- **Demographics:** age, gender, location
- **Psychographics:** values, fears, desires, frustrations
- **Awareness level** (Eugene Schwartz):
  - Unaware → Problem-Aware → Solution-Aware → Product-Aware → Most Aware
- **Existing custom audiences?** (CRM lists, website visitors, app users)

**🔴 Targeting changes 2025/2026:**
- **Lookalike audiences** are effectively deprecated — Meta recommends Advantage+ Audience instead
- **Detailed targeting exclusions** were removed in March 2025
- **Interest categories** were consolidated in June 2025 (e.g. "Jazz Guitar" → "Jazz Music"). **January 2026 hard deadline** for all old interest options
- **Advantage+ Audience** is the new standard: you give "audience suggestions" (age, location, interests) as starting hints, not hard limits. Meta benchmarks: **-32% CPA**, **+11-15% CTR**
- **At least 50 conversions per week** for stable Advantage+ performance. Below 50, use classic detailed targeting with broad interests
- **"Creative is the new targeting"** — creatives decide who sees the ads, not targeting settings (see the Andromeda section)

#### 1.3 Constraints
- **Budget range** (affects the number of variants AND creative volume - see the Andromeda section)
- **Placements:** Feed, Stories, Reels, Threads, or Automatic?
  - **🔴 Instagram Explore removed** (January 2026) — no longer available as a placement
  - **🔴 Post-loop ads on Reels removed** (November 2025) — overlay ads remain
  - **NEW: Threads** as a placement (since January 2026, 400M+ MAU)
  - **NEW: WhatsApp Status ads** announced (since June 2025)
- **Existing assets:** photos, videos, testimonials? (UGC-style outperforms polished brand content in most tests)
- **Competitors:** who advertises in the same space?

#### 1.4 Campaign structure & Advantage+

**Hierarchy:** campaign → ad set → ad (three levels). One objective per campaign. Several campaigns with the same objective split budget and data and slow down the learning phase.

```
Account
├── Campaign: Prospecting (CBO, Advantage+ Audience)
│   └── Ad Set: 10-20 diverse creatives (1-3 ad sets max!)
├── Campaign: Retargeting
│   └── Ad Set: Website visitors / engagers
└── Campaign: Testing (ABO)
    └── Ad Set: Test new creative concepts
```

**IMPORTANT in 2026:** at most 1-3 ad sets per campaign. More ad sets fragment the budget and give Andromeda less data per ad set. One ad set with many diverse creatives beats five ad sets with few creatives.

**Advantage+ automation:**

| Feature | When to use | Note 2026 |
|---------|-------------|-------------|
| **Advantage+ Sales Campaigns (ASC)** | E-commerce, lead gen, app installs | Renamed from "Advantage+ Shopping"; now supports lead gen too |
| **Advantage+ Audience** | Standard for prospecting, replaces lookalikes | You give "suggestions", Meta optimises beyond them |
| **Automatic Placements** | Meta optimises across Feed, Stories, Reels, **Threads** | Threads available as a placement since January 2026 (400M+ MAU) |
| **Catalog ads** | E-commerce with a product catalogue | **23% higher ROAS**, 3.6x more revenue than static ads |

**Recommendation:** Advantage+ works particularly well with diverse creative assets. More variants means better optimisation by the algorithm. Meta recommends **15-50+ active creatives** for optimal ASC performance.

#### 1.5 Retargeting strategy

| Audience | Window | Purpose |
|----------|---------|-------|
| Website visitors | 7-30 days | Win back warm leads |
| Engagers (video, page) | 14-60 days | Strengthen interest |
| Add-to-cart / initiate checkout | 7-14 days | Convert cart abandoners |
| Email/CRM custom audiences | Ongoing | Reactivate existing customers |

**Exclusions (mandatory):** exclude existing customers and recent converters (7-14 days) from prospecting campaigns. Otherwise you waste budget on users who already converted.

Output: a short **strategy brief** (max. 10 lines) as the reference for all following phases.

---

### Phase 2: Hook development & copy (via Gemini)

**The single most important part of the ad.** The hook decides about 80% of performance.

**Brand voice input (mandatory):** a brand voice specification MUST exist before copy generation. Template: `brand_voice_template.md` in this skill directory. If none exists, create it with the user first. The specification is passed to `generate_copy.py` via the `--brand-voice` parameter.

**IMPORTANT: generate copy via the Gemini API** — do not write it yourself. The `generate_copy.py` script in the skill directory generates hooks, primary texts, headlines and descriptions through Gemini using a specialised copywriting prompt.

```bash
# Markdown output (for manual review)
python3 <skill-dir>/generate_copy.py \
  --brand "Brand Name" \
  --product "Short product description" \
  --tone "tone of voice from CLAUDE.md" \
  --audience "target audience with psychographics" \
  --cta "CTA Text" \
  --language "English (UK)" \
  --angles 5 \
  --output copy_output.md

# JSON output (for automatic deployment via deploy_campaign.py)
python3 <skill-dir>/generate_copy.py \
  --brand "Brand Name" \
  --product "Short product description" \
  --tone "tone of voice from CLAUDE.md" \
  --audience "target audience with psychographics" \
  --cta "CTA Text" \
  --language "English (UK)" \
  --angles 5 \
  --format json \
  --output copy_output.json
```

Per hook angle the script returns: two hook variants, four primary texts, five headlines and one description. Use `--format json` for machine-readable output for automated campaign creation.

Then: the user reviews the copy, picks the best hooks, and gives feedback for iteration.

#### End-to-end deployment (recommended)

After the copy review, the entire campaign can be created automatically:

```bash
# 1. Create campaign config (copy template + adjust)
cp <skill-dir>/campaign_config_template.json campaign.json
# → Edit config: page_id, pixel_id, link, budget, angles_to_use

# 2. Dry run — check what will be created
python3 <skill-dir>/deploy_campaign.py --config campaign.json --dry-run

# 3. Deploy (everything PAUSED)
python3 <skill-dir>/deploy_campaign.py --config campaign.json

# 4. MANUAL: assign vertical images (9:16) in Ads Manager (a table is printed)
# 5. MANUAL: set the ad set to ACTIVE
```

The script creates the campaign and ad set, uploads images, creates creatives with `contextual_multi_ads` (alternative headlines and primary texts), and creates the ads — all PAUSED. The only manual step is assigning 9:16 images in Ads Manager (an API limitation with multi-text ads).

#### 2.1 Develop hook angles

Develop **five different hook angles**, each from a different psychological perspective:

| # | Angle type | Mechanism | Example |
|---|-----------|----------|----------|
| 1 | **Pain point** | Name a pain the audience recognises | "You keep talking past each other — and you don't know why" |
| 2 | **Desire / Aspiration** | Paint the desired state | "Imagine understanding each other without words" |
| 3 | **Curiosity gap** | Open a knowledge gap | "The one thing 87% of couples don't know about communication" |
| 4 | **Social proof / authority** | Lead with evidence | "2,400 couples already use it — here's why" |
| 5 | **Contrarian / pattern interrupt** | Break the expectation | "Couples therapy isn't the answer. This is." |

#### 2.2 Hook quality criteria

Every hook MUST:
- **Land within three seconds** — the first sentence decides whether they scroll past
- **Be specific** — no generic statements
- **Resonate emotionally** — feeling before logic
- **Match the awareness stage** — cold audiences need problem hooks, warm audiences need solution hooks
- **Match the brand voice** — respect the project's tone

#### 2.3 Hook formats

Test at least two formats per angle:
- **Question:** "Do you know that feeling when...?"
- **Statement:** "Most couples wait too long."
- **Story opener:** "Last week a friend told me..."
- **Statistic:** "73% of long-term couples say..."
- **Provocation:** "Stop 'working on' your relationship."
- **Before/After:** "Before: fighting over small things. After: ..."

Output: **five hook angles** with two variants each. The user picks the best two or three for phase 3.

---

### Phase 3: Ad copy

Create a full copy set for **each selected hook angle**.

#### 3.1 Primary text (4 variants per hook)

Structure of every primary text: **Hook → Pain/Desire → Bridge → Solution → Proof → CTA**

| Variant | Length | Purpose |
|----------|-------|-------|
| **Short** | 2-3 sentences | Scroll stopper, pure hook plus CTA |
| **Medium** | 4-6 sentences | Hook, pain, solution, CTA |
| **Long (story)** | 8-12 sentences | Storytelling approach with an emotional arc |
| **Long (proof)** | 8-12 sentences | Benefit stack with social proof and authority |

**Copy rules:**
- The first sentence is the hook (shown in the preview; it decides whether they tap "see more")
- Short sentences. Paragraphs. White space.
- No corporate speak, no buzzwords
- Concrete benefits instead of features
- CTA at the end — clear, action-oriented
- Emojis sparingly, and only where they fit the brand
- Speak the audience's language, not the brand's
- **Outcome-focused > feature-focused** ("Clear skin in 30 days" > "Revolutionary skincare system")

**Character limits by placement (IMPORTANT):**

| Field | Feed (recommended) | Reels | Maximum |
|------|-----------------|-------|---------|
| **Primary text** | 80-125 characters (before "See more") | **40-72 characters** | 2,200+ |
| **Headline** | 25-40 characters | 10 characters (overlay) | 255 |
| **Description** | 25-30 characters | not visible | 255 |

**Reels copy rules:** far less text is visible on Reels. Shorten the primary text to **72 characters max**. Headline overlay **10 characters max**. Captions on every frame — 80% of plays are sound-off.

#### 3.2 Headlines (5 variants per hook)

**255 characters max** per headline. Does not appear in all placements.

| Type | Mechanic |
|-----|----------|
| **Benefit headline** | Clear benefit in one sentence |
| **Curiosity headline** | Spark curiosity, motivate the click |
| **Social proof headline** | Number or proof up front |
| **Urgency headline** | Time relevance (NO fake scarcity!) |
| **Question headline** | A question the audience answers with "yes" |

**Headline rules:**
- No clickbait — the headline must deliver what it promises
- Specific beats generic ("Communicate better" is weak; "Understand what's really going on in five minutes" is strong)
- Power words: free, now, new, finally, without, instantly, simple
- Do not repeat the primary text

#### 3.3 Description (1 per hook)

Appears only in some placements. Short, complementary, not redundant.
- 1-2 sentences max
- Adds a benefit or a risk reversal on top of the headline
- Example: "Start free. No credit card needed."

#### 3.4 Output format

Per hook angle as a structured table:

```
## Hook angle: [Name]

### Primary Texts
| # | Type | Text |
|---|-----|------|
| 1 | Short | ... |
| 2 | Medium | ... |
| 3 | Long (Story) | ... |
| 4 | Long (Proof) | ... |

### Headlines
| # | Type | Text | Characters |
|---|-----|------|---------|
| 1 | Benefit | ... | XX/255 |
| 2 | Curiosity | ... | XX/255 |
| 3 | Social Proof | ... | XX/255 |
| 4 | Urgency | ... | XX/255 |
| 5 | Question | ... | XX/255 |

### Description
...
```

---

### Phase 4: Creatives

Matching visual assets for every hook angle.

#### 4.1 Creative strategy

Define for every hook angle:
- **Visual concept:** what does the image or graphic show?
- **Text overlay:** which hook text goes on the visual? (keep it minimal)
- **Formats:** 1:1 (Feed), 4:5 (Feed optimal), 9:16 (Story/Reel)
- **Style:** from the project's brand design system

#### 4.2 Creative types

| Type | When | Tool |
|-----|------|------|
| **Static image ad** | Standard, high reach | `canvas-design` → PNG |
| **Carousel card** | Feature walkthrough or story | `canvas-design` → PNG series |
| **HTML ad mockup** | Interactive, landing page preview | your frontend tooling → HTML |
| **AI-generated image** | Lifestyle, mood, hero | `nano-banana` → `/genimage` |

#### 4.3 Creative formats & safe zones

**Formats and pixel sizes:**

| Format | Aspect ratio | Pixels | Use |
|--------|-------------|-------|-----|
| Feed square | 1:1 | 1080×1080 | Feed standard |
| Feed portrait | 4:5 | 1080×1350 | Optimal for feed (more surface) |
| Stories/Reels | 9:16 | 1080×1920 | Stories, Reels |
| Link ad / landscape | 1.91:1 | 1200×628 | Link ads, carousel |

**🔴 MANDATORY FORMATS:** for EVERY creative, always generate at least these three formats:
1. **1:1** (1080x1080) — Feed standard
2. **9:16** (1080x1920) — Stories/Reels
3. **1.91:1** (1200x628) — Link ads / landscape

4:5 is optional (best for feed, but 1:1 works too). NEVER generate only one format — Meta needs all three for optimal delivery across placements.

**Safe zones (mandatory — otherwise the Meta UI covers your content):**

| Format | Top | Bottom | Sides | Reason |
|--------|------|-------|--------|--------|
| 1:1 | 10% (108px) | 10% (108px) | 10% (108px) | Profile overlay, UI elements |
| 4:5 | 10% (135px) | 10% (135px) | 10% (108px) | Feed UI |
| 9:16 | 14% (250px) | 20% (350px) | 10% (108px) | Story handle at top, send bar at bottom |
| 1.91:1 | 10% (63px) | 10% (63px) | 10% (120px) | Link preview UI |

**Visual rules:**

- **20% rule:** keep critical elements (text, logo, CTA) within the central 80% of the canvas
- **Borders:** if you use a border as a design element, make it 30-50px (never 1-2px — it looks pixelated on mobile)
- **Rule of thirds:** put the focal point on the intersections of the 3×3 grid
- **On brand:** colours, fonts and tone from the design system
- **Mobile first:** 80%+ see the ad on mobile
- **Text rule:** text on no more than 20% of the image area
- **Contrast:** the hook text must be legible on any background
- **Authenticity:** no stock-photo look, no AI aesthetic
- **CTA in the visual is optional:** only if it strengthens the design

#### 4.4 Creative production

Creatives are generated with **Python Pillow** — not with AI image generators — to guarantee brand fonts and exact colours.

For every creative:
1. Load the brand identity (colours, fonts, tone)
2. Find `.ttf` font files in the project (`**/*.ttf`)
3. The Python script generates all formats (1:1, 4:5, 9:16, 1.91:1) with safe zones
4. Add illustrative elements: organic blobs, rings, dot patterns, typographic highlights
5. Export as PNG (quality=95)

**Creative elements for visual interest:**

| Element | When | Example |
|---------|------|----------|
| Overlapping organic blobs | Relationship metaphor | Sage + terracotta circles |
| Constellation dots and rings | Dark mode, tech feel | Dots and lines on a night background |
| Architectural arch | Opening/doorway metaphor | Arch in clay/accent |
| Botanical leaves | Growth, nature | Sage leaves, dot grids |
| Typographic background | Statistic impact | Huge "93%" as background element |

#### 4.5 UGC & video creatives (recommended)

**Reality check:** an authentic selfie video of a real person typically beats any static graphic by 3-5x on CTR, especially with older audiences.

| Creative type | When | Effort |
|-------------|-------------|-----------|
| **Talking head (UGC)** | Best format for trust and authenticity | Medium (needs a real person) |
| **Text-on-screen video** | Good for Reels, hook as animated text | Low (can be generated from statics) |
| **Slideshow** | Quick win: 3-5 statics as a video with transitions | Low |

**Example:** a 15-second video of a real user with a concrete success statement would beat all the generated graphics combined.

**If no UGC is available:** export the statics as a slideshow video (three statics, three seconds each, with fade transitions). That performs better than single statics in Reels placements.

#### 4.6 Reels-specific best practices (2026)

Reels is the fastest-growing format. 9:16 ads outperform every other format.

| Rule | Details |
|-------|---------|
| **Length** | **7-15 seconds** optimal. No longer. |
| **First 3 seconds** | Must be impossible to miss — pattern interrupt needed |
| **Captions** | **Mandatory on every frame** — 80% of plays are sound-off |
| **Native aesthetic** | Use native font styles and text stickers — the algorithm favours ads that look like organic Reels |
| **Person in frame** | Significantly increases CTR |
| **Format** | 9:16 (1080x1920px) is mandatory |
| **Primary text** | Max **40-72 characters** (much less than Feed!) |
| **Overlay headline** | Max **10 characters** |

**Carousels (hot format in 2026):** carousels perform particularly well for product showcases and story sequencing. Minimum three cards, optimal five to seven.

#### 4.7 Creative design rules — research-backed checklist (2026)

All rules are based on Meta benchmarks, eye-tracking studies and A/B tests across millions of impressions. Work through this checklist on every creative build.

##### Typography (on a 1080px canvas)

| Element | Minimum | Recommended | Weight |
|---------|---------|-----------|--------|
| Headline | 60px | 72-80px | Medium/bold (light only from 72px up) |
| Subtitle/Body | 28px | 30-36px | Regular |
| Logo (if used) | 18px | 20px | Medium |

- **5-7 words max** as a headline on the image
- Detailed copy belongs in the primary text, NOT on the image
- If the text is not legible at 300px wide (phone display), it is too small
- **Bold or semi-bold** for anything under 40px — light weights become illegible on mobile

##### Safe zones (pixels on a 1080px canvas)

| Format | Top | Bottom | Sides | Visible zone |
|--------|------|-------|--------|---------------|
| 1:1 Feed (1080x1080) | 100px | 100px | 80px | Central 80% |
| 4:5 Feed (1080x1350) | 120px | 120px | 80px | Central 80% |
| 9:16 Stories (1080x1920) | 250px (14%) | 380px (20%) | 80px | Pixels 250-1540 |
| 9:16 Reels (1080x1920) | 250px (14%) | **670px (35%)** | 80px | **Only pixels 250-1248** |

- **Reels:** only the central 51% is guaranteed visible
- For a 9:16 creative used for BOTH stories and Reels: always apply the stricter Reels zone
- Source: [Meta Safe Zones](https://www.facebook.com/business/help/980593475366490)

##### Colour & contrast

- **Contrast > colour choice:** +32% CTR from high contrast alone (Meta study)
- Warm (red/orange/terracotta): +34% conversion on CTAs, ideal for action
- Cool (blue/green): longer engagement time, ideal for trust
- **NEVER:** low contrast (grey on grey, pastel on pastel, white on cream)
- A/B test baseline: +20-30% CTR for high contrast versus low contrast

##### Whitespace & content density

- **+25% CTR** with a clear focal point versus cluttered designs
- Optimal: **60% whitespace, 40% content**
- Micro whitespace around the CTA area: +15-20% CTR
- Cluttered designs: -50% message retention, +30% bounce rate
- Max 3 visual elements per creative: headline + subtitle + logo if any

##### Logo usage

- **For unknown brands: no logo.** A study across one billion impressions found logos hurt conversion campaigns when the brand is not known
- 45% of all story ads leave the logo out
- Only helpful for established brands (Nike level)
- Source: Confect.io (1B impressions dataset, 13,600 creatives)

##### CTA in the image

- **NO CTA button in the image.** Meta's native CTA button brings +22% CTR, 2.5x lower CPA
- Fake buttons are a policy risk (the ad can be rejected)
- A text overlay as a promotional hook is fine, but no elements that look clickable

##### Amount of text on the image

- 20% rule retired, but less text still performs better
- Optimal: text on **10-15% of the image area**
- Posts under 50 characters: 66% higher engagement
- Primary text: 80-125 characters, with the hook in the first 80

##### Human faces

- Real faces: **+35% conversion** versus no faces
- UGC: **3-5x better ROAS** vs. polished brand content
- Soft/averted gaze works better for intimacy/wellness products
- AI-generated faces: increasingly distrusted (2026 trend)
- **Ranking:** real people > models > illustrations > stock > AI

##### Visual hierarchy (eye tracking)

- **Z-pattern** for ads: top left → top right → diagonal → bottom right
- **One focal point per ad.** Several = -35% CTR
- Users fixate for 2.3 seconds before they scroll
- Headline at top (hot zone), visual in the middle, CTA bottom right

##### Shapes & emotional triggers

- **Rounded shapes** (pill buttons, curves): friendliness, closeness, safety
- **Angular shapes**: competence, seriousness, tech
- **Serif** (Cormorant Garamond): +40% trustworthiness, luxury
- **Sans-serif** (Inter): modern, accessible
- Colour-driven emotions increase purchase intent by 39%

##### Creative fatigue & refresh

- From frequency 2.5: CTR measurably drops, CPA rises
- From 4 impressions: conversion -45%
- Refresh: Micro monthly, Starter every 2-4 weeks, Growth weekly
- **Always keep 2-3 backup creatives** ready
- Warning signs: CTR -30% from peak OR CPM +30% over 2 weeks

##### Mobile thumb zone

- **75% of all interactions** are thumb-driven
- Easy zone = lower third, centred (67% of taps)
- Tap targets: min 44x44px, optimal 48x48px
- Top corners = hard zone
- Spacing between targets: min 8px

##### Pre-creative checklist (MANDATORY)

Go through before every creative build:

- [ ] Headline min 60px, bold/medium weight
- [ ] Subtitle min 28px
- [ ] 5-7 words max on the image
- [ ] No CTA button in the image (Meta adds that)
- [ ] No logo (except established brand)
- [ ] Max 3 visual elements
- [ ] High contrast (text clearly legible against the background)
- [ ] Safe zones respected (Reels: bottom 35% free!)
- [ ] 60%+ whitespace
- [ ] Tested on a real phone screen (300px width)
- [ ] Z-pattern: key message at top, CTA area bottom right
- [ ] Rounded shapes for approachability

---

### Phase 5: Campaign matrix & review

#### 5.1 Test matrix

Overview summary of all variants:

```
## Campaign matrix

| Hook angle | Primary texts | Headlines | Creatives | Combinations |
|------------|--------------|-----------|-----------|---------------|
| [Angle 1] | 4 | 5 | X | ... |
| [Angle 2] | 4 | 5 | X | ... |
| [Angle 3] | 4 | 5 | X | ... |
| **Total** | **X** | **X** | **X** | **X** |
```

#### 5.2 A/B test recommendation

- **Phase 1:** test hook angles against each other (same creative, different hooks)
- **Phase 2:** test the winning hook with different creatives
- **Phase 3:** optimise the winning combination with copy variants
- Budget split: 70% on winners, 30% on new tests

#### 5.3 Pre-launch checklist

- [ ] All headlines ≤ 255 characters
- [ ] Primary texts have the hook in the first sentence (preview line)
- [ ] Creatives in all required formats (1:1, 4:5, 9:16)
- [ ] Text on creatives covers no more than 20% of the image area
- [ ] CTA link correct and the landing page is live
- [ ] Tracking (UTM parameters, pixel, Conversions API) set up
- [ ] No policy violations (Meta Advertising Standards)
- [ ] Brand voice consistent across all variants
- [ ] Audience exclusions set (existing customers, recent converters)
- [ ] At least 3 creative variants per ad set

---

### Phase 6: Optimisation & learning phase

#### 6.1 Learning phase

The learning phase is the period in which Meta's algorithm learns who to show the ad to. Results are unstable during that time.

| Rule | Details |
|-------|---------|
| **Exit criterion** | 50+ conversions per ad set per week |
| **During learning phase** | No significant changes (budget, audience, creative) |
| **Duration** | Typically 3-7 days |
| **Significant change** | >20% budget change, new audience, new creative |

**If an ad never exits the learning phase:** the ad set has too little budget or the audience is too small. Consolidate instead of splitting.

#### 6.2 Budget control & scaling

| Method | When |
|---------|------|
| **ABO** (ad set budget optimisation) | When testing — controlled budget split per ad set |
| **CBO** (campaign budget optimisation) | When scaling with three or more proven ad sets — Meta distributes budget to the best ad sets automatically |

**Scaling rules:**
- Raise budget by at most 20% every 48-72 hours, so the learning phase does not reset
- **72-hour rule:** no changes for at least 72h after a budget adjustment
- Never change more than one variable at a time (budget OR audience OR creative)

#### Bidding strategies (NEW 2026)

| Strategy | Ideal for | Characteristic |
|---|---|---|
| **Lowest cost** (default) | Volume, beginners, micro tests | Automatic, no manual setting needed |
| **Cost cap** | Stable CPA when scaling | Meta targets the average CPA as the goal |
| **Bid cap** | Strict margin control, competitive verticals | Maximum bid per auction — can limit reach |
| **Minimum ROAS** | E-commerce with known margins | Only bids where the ROAS floor is achievable |

**Recommended path:** lowest cost to start → cost cap when scaling → bid cap or minimum ROAS only with a strong data base (at least 50 conversions per week).

**Meta value rules (since June 2025):** raise or lower bids per segment (age, gender, location, device). Example: +20% for a segment that converts better. Only use with a sufficient data base.

#### Budget tiers and what changes

| Tier | Budget/day | What works | What breaks | Action |
|-------|-----------|-----------------|------------|--------|
| **Micro** | < 50 | Signal tests, CTR comparison | No learning phase, no conversion optimisation | Micro-test mode, LPV optimisation |
| **Starter** | 50-150 | Lead optimisation, first real data | Creative fatigue after 1 week, small audiences exhausted | 2x creative volume, expand audience |
| **Growth** | 150-500 | Conversion optimisation, retargeting becomes worthwhile | Frequency rises fast in small geographies (a single city plus a narrow age band can be only ~200K), CAPI becomes mandatory | CAPI setup, weekly creative rotation, widen the geography |
| **Scale** | 500+ | CBO, Advantage+, lookalikes | Needs dedicated ad ops, automated reporting | Automated rules, reporting pipeline, creative pipeline |

**When to scale?**
- The winning ad set has beaten the target ROAS for at least five days
- The learning phase is over ("active" status, not "learning" or "learning limited")
- Frequency below 2.5 on cold audiences

**Audience size check:**
- Cold conversion campaign: at least 500K audience size
- Retargeting: worthwhile from 1,000 website visitors (7 days)
- With a narrow geography and age band (often only 150-300K reachable on Meta): watch the frequency ceiling and widen the geography early

#### 6.3 Frequency & creative fatigue

- Keep **frequency below 3** (how often one user sees the ad)
- If frequency rises + CTR falls → **creative fatigue**
- The fix is a new creative, not a new audience
- **After 4 repeated exposures, conversion probability drops by ~45%**
- Plan fresh creatives every 1-2 weeks (faster than before, because of Andromeda)
- Always keep **2-3 validated backup creatives** ready for immediate swap

#### 6.4 Tracking setup

| Component | Purpose | Priority |
|------------|-------|------------|
| **Meta Pixel** | Client-side tracking (pageviews, events) | Mandatory |
| **Conversions API (CAPI)** | Server-side tracking — complements the pixel, works despite ad blockers and iOS restrictions | Strongly recommended |
| **UTM parameters** | Campaign attribution in analytics | Mandatory |
| **Custom conversions** | Specific events (e.g. waitlist signup) | As needed |

**Conversions API setup:** a server-to-server connection between your backend and Meta. It sends events directly, independent of the browser. Particularly important since iOS 14.5+ (the ATT framework). On Supabase projects, implement it as an edge function.

**Recommended event structure:**
- `PageView` → all pages
- `ViewContent` → product page / landing page
- `Lead` → waitlist signup / form
- `Purchase` → purchase (with value)
- `AddToCart` → shopping cart (e-commerce)

### Phase 6.5: PMF signal analysis

**Purpose:** distinguish whether good ad metrics indicate a strong creative or genuine product-market fit.

#### Signal mapping

| Metric | What it measures | PMF question |
|--------|--------------|-----------|
| CTR (click-through rate) | Message-market fit | Does the problem resonate with the audience? |
| LP-CVR (landing page conversion rate) | Offer-market fit | Is the solution convincing? |
| Payment / signup rate | Willingness to pay | Is there real demand? |
| Retention / repeat | Product-market fit | Does the product actually solve the problem? |

**Each metric answers a DIFFERENT question.** High CTR plus low LP-CVR means a good hook and a bad offer. That is not PMF.

#### False-positive detection

| Signal | Diagnosis | Action |
|--------|----------|--------|
| High CTR plus high bounce rate | Creative bait — the hook promises more than the landing page delivers | Rework the landing page or make the hook more honest |
| High CTR plus low LP-CVR | Messaging and landing page disconnect | Check message match: the hook text must appear above the fold on the landing page |
| High LP-CVR + no payment | Price problem or trust problem | Smoke test: compare "Buy now" vs. "Waitlist" |
| Everything strong on retargeting, weak on cold | Warm audience bias, no genuine cold PMF | Use cold traffic metrics only when assessing PMF |

#### Smoke test patterns

| Pattern | When | What you learn |
|---------|------|---------------|
| Waitlist signup | Pre-launch, no product | Interest level (weak signal) |
| Preorder / deposit | Product announced | Willingness to pay (strong signal) |
| Full purchase | Product live | Real demand (strongest signal) |
| Feature vote | Post-launch | What users really want |

**Rule:** use ONLY cold traffic data when assessing PMF. Retargeting metrics are distorted.

---

### Phase 6.6: CAPI, attribution & UTM

#### CAPI (Conversions API) — mandatory from Growth stage

**What it is:** a server-to-server connection that sends conversion events directly to Meta, independent of the browser.

**Why it is mandatory:** pixel-only setups miss **30-60% of actual conversions** (worse since 2025). CAPI plus pixel together is the minimum standard for 2026. Recommended for any advertiser spending 1,000+ per month on Meta ads.

**Setup on Supabase projects:**

1. **Create edge function** (`supabase/functions/meta-capi/index.ts`)
   - Receives events from the frontend (e.g. Lead, Purchase)
   - Sends them to `graph.facebook.com/v20.0/{PIXEL_ID}/events`
   - Required fields: `event_name`, `event_time`, `action_source`, `user_data` (at least `client_ip_address` + `client_user_agent`)

2. **Event deduplication — MANDATORY**
   - Every event needs an `event_id` (a UUID, for example)
   - Same `event_id` in pixel AND CAPI → Meta deduplicates automatically
   - Without deduplication, events are counted twice

3. **Event Match Quality (EMQ)**
   - Target: a score of 6.0 or higher in Events Manager
   - Sending more user data raises EMQ: `em` (email hash), `ph` (phone hash), `fn` (first name hash)
   - All PII must be SHA-256 hashed BEFORE sending

4. **Test:** Events Manager → Test Events → enter test event code → verify events arrive

**Gate:** do not start a campaign with a daily budget above 150 without a working CAPI setup.

**Alternative: GTM server-side CAPI**

Instead of a custom edge function, CAPI can also run through a Google Tag Manager server-side container. That is the preferred route for projects already using GTM:

1. Create a server-side GTM container (Google Cloud)
2. Connect GA4 to server-side GTM
3. Configure the Meta CAPI tag in the server-side container (Facebook Conversions API tag template)

**Further CAPI setup options (NEW 2025/2026):**

| Option | Description | When to use |
|--------|-------------|-------------|
| **Edge function** (Supabase) | Full control, direct code | Supabase projects, maximum flexibility |
| **GTM server-side** | UI-based, no code | No-code site builders already using GTM |
| **CAPI Gateway** | Semi-automated, hosted on AWS or Google Cloud | When fast setup matters more than full control |
| **Signals Gateway** | Newest option, automates the CAPI process further | For high-traffic accounts, least effort |

All approaches deliver the same data quality. Recommendation: an edge function for Supabase projects, server-side GTM for everything else.

**Offline Conversions API:** discontinued in May 2025 — everything now runs through standard CAPI. Old offline integrations must be migrated.

#### Attribution windows (UPDATED April 2026)

**🔴 BREAKING CHANGE (12 January 2026):** the 7-day view and 28-day view attribution windows were **permanently removed**. Reported conversions dropped by **15-40%** as a result — without anything changing in the campaign.

| Window | When to use | Note |
|--------|-------------|------|
| **7-day click, 1-day view** (new standard) | Default for most campaigns | This is now the maximum |
| 7-day click, 0-day view | More conservative measurement, less view-through | Recommended for internal reports |
| 1-day click, 0-day view | Only for incrementality comparison | Strongest signal for true attribution |

**Further metric changes 2026:**
- **Engaged view:** now requires only **five seconds** (previously ten) or 97% of a short video
- **Engaged view for static images:** completely **removed** (5-15% fewer attributed conversions)
- **10-second video view metric:** **retired** (26 January 2026) — use ThruPlay or 2-second continuous views instead
- **Incremental attribution:** a new metric that counts only conversions that would NOT have happened without the ad

**Tip:** regularly compare 7dc/1dv vs. 7dc/0dv. Large gap = many view-through conversions = potentially overvalued.

#### Aggregated Event Measurement (AEM)

Since iOS 14.5 only eight prioritised conversion events per domain are possible. Configure them in Events Manager:

1. Purchase (highest priority)
2. Lead / CompleteRegistration
3. AddToCart
4. ViewContent
5. PageView (lowest)

**Order matters:** Meta tracks only the highest-priority event per user per 24-hour window.

#### UTM naming convention

MANDATORY for all ads:

```
utm_source=meta
utm_medium=paid-social
utm_campaign={{campaign.name}}
utm_content={{ad.name}}
utm_term={{adset.name}}
```

Meta replaces the `{{...}}` placeholders automatically. Add them to the ad URL.

---

### Phase 6.7: Performance reporting

Review campaign performance regularly:

```bash
# Last 7 days, all campaigns
python3 <skill-dir>/pull_insights.py --days 7

# Specific campaign, last 14 days
python3 <skill-dir>/pull_insights.py --campaign-id 123456 --days 14

# Save report as file
python3 <skill-dir>/pull_insights.py --days 7 --output report.md
```

**Reporting rhythm:**
- **Micro test (< 50):** check once after 48h
- **Starter (50-150):** every 3 days
- **Growth (150-500):** daily
- **Scale (500+):** daily + weekly summary

---

## Ad Creative Systematic Variation

### Headlines x Descriptions x Visuals Matrix
Generate variations systematically:
- 5 headline angles (benefit, curiosity, social proof, urgency, question)
- 3 description styles (short/punchy, story-driven, data-driven)
- 3 visual concepts per angle
= 45 unique combinations to test

### Creative Fatigue Detection
- CTR drops >20% from peak = creative fatigue
- Frequency >3 in awareness campaigns = time to refresh
- Refresh cycle: every 2-4 weeks for active campaigns
- Keep winning elements, change the weakest component first

### Platform-Specific Specs Quick Reference
| Format | Ratio | Resolution | Max Text |
|--------|-------|-----------|----------|
| Feed Image | 1:1 | 1080x1080 | 125 chars primary |
| Feed Video | 4:5 | 1080x1350 | 125 chars primary |
| Stories/Reels | 9:16 | 1080x1920 | Keep text in safe zone |
| Carousel | 1:1 | 1080x1080 | Per card |

## Related Skills
- `/product-marketing-context` - Product/brand context for targeting and messaging
- `/target-group` - ICP and proxy interests for targeting
- `/google-ads` - Dual-channel strategy
- `/cro-audit` - Landing page conversion check
- `/marketing-psychology` - Psychological triggers for ads
- `/ab-test-setup` - Test ad variations systematically

---

## Naming Convention

To keep campaigns organised, use the following naming:

| Level | Format | Example |
|-------|--------|----------|
| **Campaign** (single) | `yymm_venture` | `2604_brand` |
| **Campaign** (several per venture) | `yymm_venture_#nr details` | `2604_brand_#2 retargeting` |
| **Ad Set** | `[Campaign Name]_Ad Set` | `2604_brand_Ad Set` |

- `yy` is the two-digit year, `mm` the month the campaign was created
- With several campaigns per venture: running number plus short description
- Ad sets always carry the campaign name plus `_Ad Set`

---

## Rules

0. **🔴 Budget limit: agree a per-campaign cap with the user before spending** — never raise the budget beyond the agreed cap on your own. If a higher budget is needed, warn explicitly and get confirmation first.
0b. **Micro-test mode is mandatory:** for campaigns below a daily budget of 100, use micro-test mode. NEVER optimise for purchase or conversion when the daily budget is below target CPA x 7.
1. **One phase at a time** — never jump ahead, always wait for user feedback
2. **Respect the brand voice** — keep the project's tone and style
3. **No dark patterns** — no fake scarcity, no clickbait, no confirm-shaming. Additionally prohibited:
   - **Misleading before/after:** promising results that are not typical
   - **Manufactured social proof:** fabricated testimonials or numbers
   - **Emotional manipulation through fear:** "if you don't act NOW, it's too late"
   - **Implied medical or financial claims:** no health or financial promises without evidence
   - **Hidden costs:** the price in the ad must match the price on the landing page
   - **Scarcity verification:** if the ad claims "only X places left", that MUST be factually true. Ask the user to confirm the number for every scarcity claim.
4. **Specific beats generic** — every piece of copy must be unique to the product
5. **Think mobile-first** — 80%+ mobile audience
6. **Data beats opinion** — base recommendations on marketing principles, not on taste
7. **Less is more** — three strong hooks beat ten mediocre ones
8. **Copy and creative must work together** — the hook in the text must match the visual
9. **Respect the awareness level** — cold audiences need a different approach from warm/hot
10. **Always test** — there is no "perfect" ad, only the best version so far

## Reference frameworks

- **AIDA:** Attention → Interest → Desire → Action
- **PAS:** Problem → Agitation → Solution
- **BAB:** Before → After → Bridge
- **4U:** Useful, Urgent, Unique, Ultra-specific
- **Schwartz Awareness Levels:** Unaware → Most Aware
- **Cialdini:** Reciprocity, Commitment, Social Proof, Authority, Liking, Scarcity

---

## Phase 6b: API implementation (Meta Marketing API)

### Credentials

Meta Marketing API credentials are stored in `~/.claude/.env`:
- `META_ACCESS_TOKEN` — Long-lived system user token
- `META_AD_ACCOUNT_ID` — Format: `act_XXXXXXXXX`

### Check before you start

1. **Is the token valid?** `GET /me/adaccounts` — an error means the token has expired
2. **Which ad account?** `GET /me/adaccounts?fields=id,name` — with portfolio accounts (several ventures), make sure the right account is used
3. **Does the Facebook page exist and is it linked?** `GET /{business_id}/owned_pages` — the page must be in Business Manager AND assigned to the system user (Business Settings → System Users → assign assets → pages)
   - **Common mistake:** the page is visible in Business Manager but the system user token has no access. Fix: Business Settings → System Users → [select user] → Assets → Pages → assign the page individually and set `CREATE_CONTENT` and `MANAGE` permissions.
   - **Is Instagram linked?** Story and Reel placements need an IG account connected to the Facebook page. Check with `GET /{page_id}?fields=instagram_business_account`
4. **Pixel active?** `GET /{ad_account_id}/adspixels?fields=id,name,last_fired_time`
5. **Images uploaded?** `POST /{ad_account_id}/adimages` with `-F "filename=@file.png"`

### Naming convention for ads

```
2604_example_K[1-5]_v[0-1]
```
K is the concept number, v the variant. Example: `2604_example_K3_v0`

### What works (tested April 2026)

#### Standard ads with `contextual_multi_ads` ✅
Multiple text options per ad ("Add a text option" in Ads Manager):
```python
creative_data = {
    "name": "...",
    "object_story_spec": json.dumps({
        "page_id": PAGE_ID,
        "link_data": {
            "image_hash": "...",
            "link": "https://...",
            "message": "Primary Text (main version)",
            "name": "Headline (main version)",
            "description": "Description",
            "call_to_action": {"type": "LEARN_MORE", "value": {"link": "https://..."}}
        }
    }),
    "contextual_multi_ads": json.dumps({
        "enroll_status": "OPT_IN",
        "contextual_texts": [
            {"text": "Alt Headline 1", "text_type": "name"},
            {"text": "Alt Headline 2", "text_type": "name"},
            {"text": "Alt Primary Text 1", "text_type": "message"},
            {"text": "Alt Primary Text 2", "text_type": "message"},
            # NO text_type "description" — description allows only one option
        ]
    }),
    "access_token": TOKEN,
}
# POST /{ad_account_id}/adcreatives
```

**Rules for `contextual_multi_ads`:**
- `text_type: "name"` = headline options (max. 4 alternatives + 1 original = 5)
- `text_type: "message"` = primary text options (max. 4 alternatives + 1 original = 5)
- `text_type: "description"` — do NOT use it, description allows only one option
- **CANNOT be combined with `asset_feed_spec`** — one or the other, not both

#### 🔴 Placement images (9:16, 1.9:1) on multi-text ads: a MANUAL step

When `contextual_multi_ads` is used (several text options per ad), placement-specific images (9:16 for stories and Reels, 1.9:1 for link ads) **cannot be assigned via the API**. The API does not allow `asset_feed_spec` and `contextual_multi_ads` at the same time.

**Consequence:** the ads are created with the 1:1 image. Meta crops that image automatically for story and Reel placements, which looks bad (grey bar at the top, cut-off content).

**Mandatory workaround (MANUAL in Ads Manager, ~1 min per ad):**

1. Open ad → **Edit**
2. In the **Media** section you see "Square" (1:1) and "Vertical" (9:16)
3. Click **Replace** on **Vertical**
4. Upload the matching 9:16 image (e.g. `Creatives/9_16/1.0_9_16.png`)
5. Save

**ALWAYS give the user a mapping table:**

```
| Ad       | Square (API)        | Vertical (MANUAL)       |
|----------|---------------------|-------------------------|
| K1_v0    | 1-1/1.0_1_1.png     | 9_16/1.0_9_16.png       |
| K2_v0    | 1-1/2.0_1_1.png     | 9_16/2.0_9_16.png       |
| ...      | ...                 | ...                     |
```

**Never forget or skip this step.** Without a 9:16 image, story and Reel placements either do not deliver or look unprofessional.

#### Create standard ads ✅
```python
ad_data = {
    "name": "...",
    "adset_id": ADSET_ID,
    "creative": json.dumps({"creative_id": CREATIVE_ID}),
    "status": "PAUSED",
    "access_token": TOKEN,
}
# POST /{ad_account_id}/ads
```

#### Update ad creative (swap creative) ✅
```python
update_data = {
    "creative": json.dumps({"creative_id": NEW_CREATIVE_ID}),
    "access_token": TOKEN,
}
# POST /{ad_id}  (updates existing ad, keeps ID/stats)
```

### What does NOT work on some ad accounts (from practice)

**NOTE:** these limitations are specific to individual ad accounts. Other accounts may well have these features. Check before working with any new account.

#### Dynamic creative (asset_feed_spec) with OUTCOME_SALES ❌
```
Error: "Missing Call To Action Type" (error_subcode 1487664)
```
Creatives with `asset_feed_spec` are created, but ads cannot be created from them on OUTCOME_SALES campaigns. The CTA is not passed through correctly. Workaround: use standard ads with `contextual_multi_ads`.

#### `asset_feed_spec` + `contextual_multi_ads` combined ❌
```
Error: "Adcreative Create Failed" (error_subcode 1487390)
```
These two features cannot be used together on one creative. Workaround: use only `contextual_multi_ads` (multi-text) and add asset customisation (different images per placement) manually in Ads Manager.

#### Asset customisation via API + contextual_multi_ads ❌
Placement-specific images (9:16 for stories, 1.9:1 for the right column) cannot be set via the API while `contextual_multi_ads` is active. **Add them manually in Ads Manager.**

#### Advantage+ Creative on some accounts ❌
```
Error: "Ad account ineligible for Advantage plus Creative" (error_subcode 3858023)
```
Some accounts are not enabled for Advantage+ Creative. `degrees_of_freedom_spec` with `text_generation` or `standard_enhancements` does not work. This also affects dynamic creative optimisation.

#### `use_advantage_audience=false` with age_min > 25 ❌ (when not explicitly set)
With Advantage+ Audience, `age_min` is capped at 25. Fix: set `targeting_automation: {advantage_audience: 0}` inside the targeting object, NOT as a separate field.

#### Facebook video feeds placement ❌ (deprecated)
```
Error: "Facebook video feeds placement is deprecated"
```
Remove `video_feeds` from `facebook_positions`. Applies from API v20.0.

### Account-specific notes (example account)

- **Account ID:** `act_XXXXXXXXXXXXXXX`
- **Business ID:** `XXXXXXXXXXXXXXX`
- **All pages must be assigned to the system user INDIVIDUALLY** (Business Settings → System Users → Assets → Pages). A page being in Business Manager does NOT mean the API token has access to it.
- **Instagram subscription blocker:** if an IG account linked to the page has an ad-free subscription, ads cannot be published. Error message: "Ad can't be published due to subscription" (error_subcode 3858226)

#### `is_adset_budget_sharing_enabled` required field (NEW April 2026) ⚠️

From April 2026, `is_adset_budget_sharing_enabled` is a **required field** when creating campaigns without CBO (campaign budget optimisation). Without it the API returns this error:

```
Error: "Must specify True or False in is_adset_budget_sharing_enabled field" (error_subcode 4834011)
```

**Fix:** ALWAYS include when creating the campaign:
```python
"is_adset_budget_sharing_enabled": "false",  # or "true" if ad sets should share 20% of budget
```

**What the field does:** when `true`, ad sets within the campaign can hand up to 20% of their budget to other ad sets in the same campaign to optimise overall performance. With only one ad set it makes no difference — set it to `false`.

#### Account forces `LOWEST_COST_WITH_BID_CAP` (discovered July 2026) ⚠️

Some accounts force `bid_strategy: LOWEST_COST_WITH_BID_CAP` on EVERY campaign — even when no bid strategy is specified. This is an account-level setting that cannot be changed via the API.

**Consequence:** every ad set needs a `bid_amount` (in cents). Without it the API returns:
```
Error: "Bid Amount Required For The Bid Strategy Provided" (error_subcode 1815857)
```

**Fix:** ALWAYS include `bid_amount` when creating the ad set:
```python
"bid_amount": "200",  # 200 cents = 2.00 EUR bid cap per event
```

**Recommended bid_amount values:**
- LANDING_PAGE_VIEWS: 100-300 (1-3 per LPV)
- LINK_CLICKS: 50-200 (0.50-2 per click)
- OFFSITE_CONVERSIONS (lead): 1000-3000 (10-30 per lead)

#### `targeting_automation.advantage_audience` required field (discovered July 2026) ⚠️

From 2026, `targeting_automation: {advantage_audience: 0}` (or `1`) is a **required field** in the targeting object when creating an ad set. Without it:
```
Error: "Advantage Audience Flag Required"
```

**Fix:** ALWAYS include in the targeting object:
```python
"targeting": {
    "geo_locations": {...},
    "targeting_automation": {"advantage_audience": 0}  # 0 = off, 1 = on
}
```

Use `0` when you want exact audience control (for example retargeting with custom audiences).

#### The meta-ads MCP tool (brijr/meta-mcp v1.1.0) CANNOT create ad sets ❌

The `meta-ads-mcp@1.1.0` MCP tool has a known bug (GitHub issue #19): its internal validation blocks valid optimization_goal/billing_event combinations and the promoted_object pass-through. **Creating campaigns works, creating ad sets does not.**

**Workaround:** use `deploy_campaign.py` or a direct API call via Python/curl instead of the MCP tool.

#### Video ads: thumbnail mandatory + chunked upload > 100 MB

- **Thumbnail:** video creatives ALWAYS need an `image_hash` in the `video_data` object. Without it: `"Your ad needs a video thumbnail"` (error_subcode 1443226). Fix: extract a thumbnail with ffmpeg, upload it as an adimage, and pass the image_hash in video_data.
- **Chunked upload:** videos over 100 MB must be uploaded via chunked upload (three phases: start → transfer → finish). A standard upload returns an empty result.

```python
# Extract thumbnail
subprocess.run(['ffmpeg', '-y', '-i', video_path, '-ss', '00:00:02', '-vframes', '1', '-q:v', '2', thumb_path])

# Video creative with thumbnail
"video_data": {
    "video_id": VIDEO_ID,
    "image_hash": THUMBNAIL_HASH,  # REQUIRED!
    "message": "Primary Text",
    "title": "Headline",
    ...
}
```

#### Website custom audiences only in the Ads Manager UI

The Meta Marketing API (both via MCP and directly) cannot create website custom audiences — that only works in the Ads Manager UI. The audience ID can then be referenced via the API:
```python
"custom_audiences": [{"id": "AUDIENCE_ID_FROM_ADS_MANAGER"}]
```

### Check feature eligibility on a new account

When moving to a new ad account, test these features:

1. **Advantage+ Creative:** `GET /{AD_ACCOUNT_ID}?fields=capabilities` — check whether "ADVANTAGE_PLUS_CREATIVE" is in capabilities
2. **Dynamic creative:** create a creative with `asset_feed_spec` (PAUSED). If you get error_subcode 1487664, it is not available
3. **Advantage+ Shopping:** create a campaign with `special_ad_categories=[]` and `buying_type=AUCTION`

Features available on most accounts that may be missing here:
- `asset_feed_spec` with OUTCOME_SALES (normally available)
- Advantage+ Creative / Dynamic Creative (normally available)
- `degrees_of_freedom_spec` with text_generation (normally available)

### Choosing the right optimisation goal

| Situation | Optimisation goal | Rationale |
|---|---|---|
| Pixel has **< 50 purchase events/week** | `LANDING_PAGE_VIEWS` | Meta needs data. LPV gives an immediate signal. |
| The pixel has **50+ purchase events per week** | `OFFSITE_CONVERSIONS` (purchase) | Enough data for conversion optimisation |
| Lead generation (waitlist, email) | `OFFSITE_CONVERSIONS` (lead) | When the lead event fires regularly |
| New campaign, new pixel | `LANDING_PAGE_VIEWS` for the first two weeks | Then switch to conversions |

**NEVER optimise for purchase when the pixel has zero purchase events.** Meta cannot optimise without data.

### Checking pixel events

The events the pixel tracks are configured through GTM. The GTM container config typically lives as `gtm-container.json` in the repo. Check before setting up a campaign:
1. Has `gtm-container.json` actually been imported into GTM AND published?
2. Has the conversion event (e.g. purchase) ever fired? → check Events Manager
3. Custom events must be **confirmed** in Events Manager before they can be used for ads

### Copy review process (mandatory)

Before copy goes into ads, ALWAYS have it reviewed by a panel of at least four specialists:

1. **Performance marketer:** Hook under 125 characters? Price in the text? CTA variation?
2. **Brand manager:** Tone consistent? No teleshopping language?
3. **Comms specialist:** avoid repetition, vary CTA endings, include story hooks
4. **Native-speaker editor:** correct spelling and diacritics for the target language, natural phrasing for the audience, no jargon or loanwords the audience does not know

**Character-set rule:** all ad copy MUST use the correct characters of the target language, including accents and diacritics. Stripping them (writing "Gruender" instead of "Gründer", or "francais" instead of "français") makes the ad look unprofessional.

#### AI-tells detection (mandatory after Gemini generation)

Before copy goes into ads, check it for these AI tells:

| AI tell | Example | Fix |
|---------|----------|-----|
| Parallel sentence structures across all angles | Every angle starts with "You have..." | At least three different sentence openings |
| Identical emotional arcs | Every long variant: statement → question → details → guarantee → CTA | At least two angles with a completely different structure |
| Symmetrical lists | Always three bullets, always the same length | Vary it: two, four, or no bullets at all |
| Overusing "you" at the start of paragraphs | "You have...", "You know...", "You deserve..." | At most 30% of paragraphs may start with "you" |
| No surprise | Not a single line that makes the reader pause | At least one unexpected phrase per angle |
| Generic power-phrase overuse | "finally", "now", "just right" in every text | Max 1 power word per primary text |

#### Tonal divergence (mandatory)

**Rule:** if you read two angles side by side and they feel similar, one of them is wrong. Rewrite it.

Every angle MUST have its own character:

| Angle | Tonal character | Sentence style |
|-------|-------------------|----------|
| Pain point | Direct, slightly uncomfortable | Short. Staccato. Confrontational. |
| Desire | Warm, painterly, calm | Longer sentences, imagery, subjunctive ("Imagine...") |
| Curiosity | Playful, teasing | Questions, cliffhangers, ellipses... |
| Social proof | Factual, matter-of-fact, sober | Numbers up front, short statements, sources |
| Contrarian | Sharp, provocative, bold | Negations, contrasts, short punches |

**Sameness test:** put all five short variants side by side. Would a real person notice these are five different ads? If not, rewrite.

### 🔴 PRE-FLIGHT CHECKLIST (mandatory before the first API call)

Before EVERY campaign setup, work through this checklist completely and present it to the user. No API call before every point is settled.

**1. Verify geo-targeting**
- [ ] Default to a country code, e.g. `"countries": ["<COUNTRY_CODE>"]` (NEVER city keys from memory)
- [ ] Ask the user: "Only the target country, or also neighbouring markets?"
- [ ] If targeting a city plus radius: the city key was verified via `GET /search?type=adgeolocation&q=<CITY>`

**2. Check page access**
- [ ] The Facebook page exists and is in Business Manager
- [ ] The system user has access to the page (test: `GET /PAGE_ID?fields=name`)
- [ ] Instagram account checked: no ad-free subscription active? If unclear: do NOT include IG in placements

**3. Check pixel status**
- [ ] Pixel fires (`last_fired_time` < 24h)
- [ ] Has the conversion event (purchase/lead) ever fired? → check Events Manager
- [ ] If zero events: LANDING_PAGE_VIEWS as optimisation goal, NOT conversions

**4. Campaign + ad set consistency**
- [ ] The campaign objective and the ad set optimisation goal match
- [ ] For OUTCOME_SALES: ALWAYS set `promoted_object` with the pixel ID (even with LPV optimisation)
- [ ] For LPV optimisation inside a sales campaign: `promoted_object` with `custom_event_type: OTHER`

**5. Check placements**
- [ ] Do NOT use `video_feeds` (deprecated from API v20.0)
- [ ] Do NOT use `explore` (Instagram Explore removed as a placement January 2026)
- [ ] `right_hand_column` only if a desktop audience is relevant
- [ ] Instagram only if the IG account is VERIFIED to have no subscription blocker
- [ ] Audience Network and Messenger: default to no
- [ ] Check Threads as a placement (available since January 2026)

**6. Budget & ads ratio**
- [ ] At most one ad per ~4 of daily budget (at 21 per day that is five ads max)
- [ ] Below 50/day: ALWAYS micro-test mode

**7. Copy check**
- [ ] All texts use the correct characters for the target language (accents, diacritics)
- [ ] UTM parameters in all links
- [ ] Price in the copy (when price is a conversion argument)

**8. Show the user a final summary**
- [ ] A table with: objective, geography, age, placements, budget, optimisation goal, number of ads
- [ ] User confirms BEFORE the first API call

---

### Campaign setup step by step

**Recommended: automated setup via `deploy_campaign.py`** — instead of the manual API steps below, `deploy_campaign.py` can perform the whole setup (steps 1-5) automatically. See phase 2 for the workflow. The manual steps remain as a reference for special cases.

1. **Create campaign** (PAUSED, `is_adset_budget_sharing_enabled=false`)
2. **Create the ad set** (PAUSED, with the correct optimisation goal, targeting and budget)
   - **Mandatory on conversion campaigns:** `promoted_object` must be set:
   ```python
   "promoted_object": json.dumps({
       "pixel_id": PIXEL_ID,
       "custom_event_type": "LEAD"  # or "PURCHASE", "COMPLETE_REGISTRATION"
   })
   ```
   - Set `promoted_object` with the pixel ID even for `LANDING_PAGE_VIEWS` optimisation — otherwise Meta cannot switch to conversions later without a new ad set.
3. **Upload images** (`POST /{act}/adimages`, returns an image_hash)
4. **Create creatives** (with `contextual_multi_ads` for multi-text)
5. **Create ads** (PAUSED, references creative)
6. **The user reviews in Ads Manager** (check previews, add placement images manually)
7. **The user goes live** (set the ad set to ACTIVE)

**ALWAYS create everything PAUSED. The user activates it themselves after review.**

### Geo-targeting: MANDATORY RULES

**🔴 NEVER use city keys from memory. ALWAYS use the country-code method:**

```python
# CORRECT: country code
"geo_locations": {"countries": ["US"]}

# CORRECT: country + radius around city
"geo_locations": {"countries": ["US"], "cities": [{"key": "VERIFIED_KEY", "radius": 50, "distance_unit": "kilometer"}]}

# WRONG: a city key from memory (it may be wrong)
"geo_locations": {"cities": [{"key": "1025873"}]}  # DO NOT DO THIS
```

**Never assume a country.** Before EVERY campaign setup, ask:
- "Should the campaign run in neighbouring markets as well, or in one country only?"

**If a city plus radius is wanted:** verify the correct city key via the API FIRST:
```
GET /search?type=adgeolocation&q=<CITY>&location_types=city&access_token=TOKEN
```
Never hardcode keys or use them from memory.
