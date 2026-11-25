---
name: product-marketing-context
description: Create and maintain a central product marketing context document for any venture. All marketing skills reference this as their foundation. Generates .agents/product-marketing-context.md with positioning, personas, competitive landscape, and brand voice. Run /product-marketing-context to create or update.
model: sonnet
effort: medium
---

# Product Marketing Context Skill

## Purpose

This is the **foundation skill** for all marketing work. It creates and maintains `.agents/product-marketing-context.md` — a single source of truth for product marketing intelligence that all other marketing skills read as their first step.

Without this document, marketing skills work blind. With it, they produce output that is grounded in actual product reality, customer language, and competitive positioning.

## When to Run

- First marketing engagement for a venture (before any ad copy, SEO, content)
- After a pivot or major strategy change
- When another skill reports "no context found" or "product-marketing-context.md missing"
- When the user says something like "update our marketing context" or "refresh the positioning"

## Output File

**Path:** `.agents/product-marketing-context.md` in the project root

Create the `.agents/` directory if it does not exist. This directory holds all agent-generated context files that are shared across skills but not shipped to production.

If `.agents/product-marketing-context.md` already exists: show a diff summary of what changed and ask for confirmation before overwriting.

---

## Workflow

### Step 1: Identify Venture and Phase

Ask the user:
1. Which venture? (or confirm from project context)
2. What phase? Venture Opportunity / Prototype / Pilot
3. Is there an existing product-marketing-context.md? (check `.agents/` directory)

### Step 2: Collect Data

Pull information from these sources in priority order:

1. **Existing `/target-group` analysis** - If `.agents/target-group.md` exists, read it. Sections 2, 3, 4, and 9 of the output document draw heavily from this.
2. **The strategy document** — wherever the single source of truth for strategy, positioning, current goals and KPIs lives.
3. **The project journal** — look for customer discovery entries, user interview notes, pivot decisions and data points from real users.
4. **Landing Page / Webapp copy** - Read the actual product copy. This reveals how the product currently presents itself and what language it uses.
5. **Direct conversation with user** - Fill gaps through targeted questions. Do not ask for information you can already infer.

### Step 3: Determine Depth by Phase

| Phase | Required Sections | Notes |
|-------|------------------|-------|
| Venture Opportunity | 1-6 mandatory, 7-12 optional | Hypothesis-based, mark assumptions clearly |
| Prototype | All 12 sections | Mix of hypotheses + early data |
| Pilot | All 12 sections | Data-backed wherever possible |

### Step 4: Draft Section by Section

Draft each section and **ask the user to validate** before moving to the next. Do not batch all sections and dump them at once - the user needs to catch errors early.

Say something like: "Here's Section 1 (Produktuebersicht) - does this match your understanding? Any corrections before I continue?"

### Step 5: Write Output File

Once all sections are validated, write the complete `.agents/product-marketing-context.md` using the template below.

---

## Company-Specific Adaptations

- **The strategy document is the single source of truth** for strategy and current goals. Always cross-reference it.
- **The project journal is the historical record.** Mine it for customer quotes, discovery insights and pivot reasoning.
- **Phase-awareness is mandatory**. A Venture Opportunity context is hypothesis-heavy. A Pilot context has real data. Mark the difference clearly.
- **target market is the default** unless the venture explicitly targets other markets.
- **Document language: German** for all section headers and user-facing content. English marketing terms (USP, ICP, CAC, etc.) are fine inline.
- **Never use em-dashes (-)** - always short hyphens (-).
- **PII rule**: Never include real user names, emails, or identifying information. Use synthetic or anonymized examples only.

---

## Output Document Template

When writing `.agents/product-marketing-context.md`, use this exact template:

```markdown
# Product Marketing Context: [Venture Name]

> Generated: [YYYY-MM-DD] | Stage: [Opportunity / Prototype / Pilot] | Last updated: [YYYY-MM-DD]
>
> This document is the central marketing context for [Venture Name]. Every marketing skill reads it as its first step.

---

## 1. Product overview

<!-- What the product is, the core value proposition, how it works. 3-5 sentences. -->

**Product:** [name and category]

**Core value proposition:** [one sentence: for whom, which problem, how it is solved, compared to what]

**How it works:** [short description of the mechanism: step 1, step 2, step 3]

**Price:** [pricing model and entry price]

**Status:** [in development / live / beta / etc.]

---

## 2. Target audience

<!-- Primary and secondary audience. Demographics plus psychographics. -->
<!-- For a deep ICP analysis, run /target-group. -->

### Primary audience

- **Who:** [short description]
- **Age:** [range]
- **Geography:** [primary markets]
- **Occupation / life situation:** [relevant contexts]
- **Digital behaviour:** [where they are online, how they search, which platforms]
- **Decision patterns:** [how they make buying decisions]

### Secondary audience (if any)

- **Who:** [short description]
- **Difference from the primary group:** [what is different]

### ICP (ideal customer profile)

The perfect customer is: [2-3 sentences, very concrete. Not "people with problem X" but "a 45-year-old woman in a mid-sized city who has experienced X and Y and already tried Z"]

---

## 3. Personas

<!-- 2-3 concrete persona profiles. They should feel like real people, not marketing templates. -->
<!-- Prefer real quotes from discovery calls or phrasing from your project journal. -->

### Persona 1: [first name, age]

**In one sentence:** [who this is in one sentence]

**Situation:** [their current life or work situation]

**Frustration:** [what genuinely annoys them — concrete, not abstract]

**What they have already tried:** [previous attempts at a solution]

**Typical quote:** "[how they would describe the problem in their own words]"

**Why they convert:** [what has to happen for them to buy or sign up]

---

### Persona 2: [first name, age]

**In one sentence:** [who this is in one sentence]

**Situation:** [their current life or work situation]

**Frustration:** [what genuinely annoys them — concrete, not abstract]

**What they have already tried:** [previous attempts at a solution]

**Typical quote:** "[how they would describe the problem in their own words]"

**Why they convert:** [what has to happen for them to buy or sign up]

---

### Persona 3 (optional): [first name, age]

[Same structure as above]

---

## 4. Problems and pain points

<!-- Top 3-5 problems. For each: severity, current workarounds, emotional impact. -->

| # | Problem | Severity (1-5) | Current workaround | Emotional impact |
|---|---------|----------------|--------------------|------------------|
| 1 | [problem] | [1-5] | [what they do instead] | [how it feels] |
| 2 | [problem] | [1-5] | [what they do instead] | [how it feels] |
| 3 | [problem] | [1-5] | [what they do instead] | [how it feels] |

### Jobs to be done

What does the audience "hire" the product for?

- **Functional:** [concrete job, e.g. "find an appointment quickly without waiting"]
- **Emotional:** [emotional job, e.g. "feel that I am doing something active for my health"]
- **Social:** [social job, e.g. "be seen as a modern, proactive person"]

---

## 5. Competitive landscape

<!-- Direct and indirect competitors. Positioning map. Who we lose to and why. -->

### Direct competitors

| Competitor | Strengths | Weaknesses | Price | Why we sometimes lose |
|------------|-----------|------------|-------|------------------------|
| [name] | [what they do well] | [gaps] | [price] | [when users choose them over us] |
| [name] | [what they do well] | [gaps] | [price] | [when users choose them over us] |

### Indirect competitors and alternatives

<!-- What do users do instead of using our product? -->

- [alternative 1]: [why it is an option for them]
- [alternative 2]: [why it is an option for them]
- [status quo / doing nothing]: [why some users simply carry on as before]

### Positioning (Obviously Awesome, April Dunford)

Work through the 5(+1) components IN THIS ORDER — positioning is context setting, not a slogan:

1. **Competitive alternatives:** what would best-fit customers do WITHOUT us? (often: a spreadsheet, an intern, nothing — not the obvious competitor)
2. **Unique attributes:** capabilities only we have (relative to those alternatives)
3. **Value (with evidence):** what provable customer value do those attributes enable?
4. **Best-fit segment:** who cares INTENSELY about exactly that value? Cut it narrower.
5. **Market category:** the category that makes the value immediately understandable
6. *(optional)* **Relevant trends:** only if they strengthen the story — a trend is not a category

Style choice: head-to-head (only with clear superiority), **big fish in a small pond** (the standard route for startups), or create a new game (expensive, only when nothing else fits). The test: if customers mis-categorise the product ("ah, something like X"), the positioning is broken — not the product.

### Positioning map

```
                    [Y axis top - e.g. "premium / expensive"]
                              |
    [X left]  _______________+_______________ [X right]
               |              |              |
               |     US       |              |
               |    (x,y)     |              |
               |______________|______________|
                              |
                    [Y axis bottom - e.g. "budget / cheap"]
```

Axes: [description of the X axis] versus [description of the Y axis]

Our position: [short explanation of why we sit there]

---

## 6. Differentiation

<!-- Why us and not the others? USPs, unfair advantages, moats. -->

### Our USPs

1. **[USP 1]:** [explanation — what this concretely does for the user]
2. **[USP 2]:** [explanation — what this concretely does for the user]
3. **[USP 3]:** [explanation — what this concretely does for the user]

### Unfair advantages and moats

<!-- What can competitors not simply copy? -->

- [advantage 1]: [why it is hard to replicate]
- [advantage 2]: [why it is hard to replicate]

### Core positioning statement

For [primary audience] who [have problem], [product] is the [category] that delivers [benefit], because [reason / evidence].

---

## 7. Objections and anti-personas

<!-- Common objections with responses. Who is NOT the target audience. -->

### Typical objections

| Objection | Response |
|-----------|----------|
| "[typical objection]" | [how we answer — concrete, not generic] |
| "[typical objection]" | [how we answer — concrete, not generic] |
| "[typical objection]" | [how we answer — concrete, not generic] |

### Anti-personas

<!-- Who is explicitly NOT our customer? This saves ad budget and reduces churn. -->

- **[anti-persona type]:** [why they do not fit — what they need, we cannot deliver]
- **[anti-persona type]:** [why they do not fit — what they need, we cannot deliver]

---

## 8. Switching dynamics

<!-- What do users switch from? Switching barriers? Triggers for the switch? -->

### What do users switch from?

- **Main origin 1:** [product/method] — because [reason for switching]
- **Main origin 2:** [product/method] — because [reason for switching]
- **New to the category (no switch):** [share and context]

### Switching barriers

What stops users from switching to us?

- [barrier 1]: [e.g. data migration, trust, habit, price]
- [barrier 2]: [e.g. an existing contract with the incumbent]

### Switching triggers

What finally makes someone switch?

- [trigger 1]: [a concrete event or situation]
- [trigger 2]: [a concrete event or situation]

---

## 9. Customer language

<!-- The exact words and phrases customers use themselves. Directly usable in copy. -->
<!-- From discovery calls, reviews, forums, your project journal. Do not invent phrasing. -->

### How they describe the problem

- "[direct quote or typical phrasing]"
- "[direct quote or typical phrasing]"
- "[direct quote or typical phrasing]"

### How they describe the ideal solution

- "[direct quote or typical phrasing]"
- "[direct quote or typical phrasing]"

### Terms they use (and we should use in copy)

[term 1], [term 2], [term 3], [term 4], [term 5]

### Terms we should NOT use

[internal term or jargon users do not know], [another term]

---

## 10. Brand voice

<!-- Tone, style, do's and don'ts. For detailed brand work, run /brand-identity. -->

### Tone

- **In one word:** [e.g. "direct" / "warm" / "matter-of-fact"]
- **Like a friend who...:** [analogy, e.g. "works as a doctor and tells you honestly what's going on"]

### Do's

- [what we do in our communication]
- [what we do in our communication]
- [what we do in our communication]

### Don'ts

- [what we avoid]
- [what we avoid]
- [what we avoid]

### Reference points

- Brands with a similar tone: [name], [name]
- Brands whose tone we do NOT want: [name], [name]

---

## 11. Proof points

<!-- Social proof, testimonials, numbers, case studies, trust signals. -->

### Numbers and facts

- [number / fact 1, e.g. "X users in beta", "Y% completion rate"]
- [number / fact 2]
- [number / fact 3]

### Testimonials

<!-- Only with permission. No real names without consent. Anonymous or synthetic. -->

> "[quote]"
> - [first name, age, context — anonymised if needed]

### Trust signals

- [signal 1, e.g. "GDPR-compliant data protection", "clinically supervised", "independently audited"]
- [signal 2]
- [signal 3]

### What we are still missing (honest assessment)

- [gap 1 — e.g. "no public testimonials yet"]
- [gap 2]

---

## 12. Current goals

<!-- Current marketing goals, KPIs, venture stage. -->
<!-- Keep the single source of truth wherever your strategy lives — summarise here, do not duplicate. -->

### Venture stage

[Opportunity / Prototype / Pilot]

### Current marketing focus

[The main focus in this stage — e.g. "validate PMF with the first paying user" or "prove CAC below the target"]

### Key marketing KPIs

| KPI | Target | Current | Source |
|-----|--------|---------|--------|
| [KPI 1] | [target value] | [current value or "n/a"] | [where the number comes from] |
| [KPI 2] | [target value] | [current value or "n/a"] | [where the number comes from] |

### Next milestones

- [milestone 1, with a date if known]
- [milestone 2]

**For the full strategy and kill-switch criteria:** see your strategy source of truth.

---

## Recent changes

| Date | Section | What changed |
|------|---------|--------------|
| [YYYY-MM-DD] | [section] | [short description] |
```

---

## How Other Skills Should Use This Document

When building a skill that needs marketing context, include this instruction at the top of its workflow:

```
### Step 0: Load Marketing Context

Before starting, check if `.agents/product-marketing-context.md` exists in the project root.

- If YES: Read it. Use it to ground all output in actual product positioning, customer language, and competitive reality.
- If NO: inform the user — "I could not find product-marketing-context.md. For the best results I recommend running /product-marketing-context first. I can also start right away and ask for the relevant information as we go."
```

---

## Related Skills

- `/target-group` - Deep ICP analysis (feeds into Section 2+3)
- `/brand` - Detailed brand identity work (feeds into Section 10)
- `/customer-discovery` - Interview methodology (feeds into Section 4+9)
- `/competitor-profiling` - Structured competitor analysis (feeds into Section 5)
- `/meta-ads` - Reads product-marketing-context.md as first step
- `/google-ads` - Reads product-marketing-context.md as first step
- `/seo` - Reads product-marketing-context.md as first step
- `/content-marketing` - Reads product-marketing-context.md as first step
- `/linkedin-ads` - Reads product-marketing-context.md as first step
