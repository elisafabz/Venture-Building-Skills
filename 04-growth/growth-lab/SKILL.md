---
name: growth-lab
description: Plan, log, and review marketing growth experiments (Meta/Google/LinkedIn ads, landing page, email) with ICE scoring, testing hierarchy, kill/scale rules, and experiments.json tracking. Triggered by /growth-lab, "what should I test", "which test next", "plan a growth experiment", "log/evaluate test results", "experiment review". NOT for PostHog feature-flag A/B experiments (use posthog skills) and NOT for choosing which channel/strategy to pursue at all (use growth-strategy first).
model: sonnet
effort: medium
---

# Growth Lab - Experiment Framework

> **Requires:** web search optional (live benchmarks).

A channel-agnostic growth experiment framework. It tells you what to test, why and how — based on best practices from Reforge, Hormozi, Demand Curve and CXL.

## Subcommands

Parse $ARGUMENTS to pick the right workflow:

- `/growth-lab <venture> <channel>` -> Plan mode (default)
- `/growth-lab results` -> Log results
- `/growth-lab review` -> Weekly review

If there are no arguments, ask for the venture and the channel.

---

## Plan mode: `/growth-lab <venture> <channel>`

Channels: `meta-ads`, `google-ads`, `landing-page`, `linkedin`, `email`

### Phase 1: Context Pull (automatic)

1. **Load venture context:**
   - Read any existing venture notes
   - Read the project's strategy document if one exists
   - Load existing experiments: `<venture-folder>/experiments.json` (if present)

2. **If context is missing - ASK, NEVER ASSUME:**
   - No audience found? → "Who is the target audience for [venture]? (age, pain point, segment)"
   - No existing record of the venture? → "Is this a new venture? Tell me briefly: what is the product and who is it for?"
   - No value proposition? → "What is the core value proposition of [venture]?"
   - Stage unclear? → "What stage is [venture] at? (idea / prototype / pilot)"
   - Running experiments found? → "You have [N] experiments running. Shall I evaluate those first, or propose new ones?"

3. **Research benchmarks (priority order):**
   a. **Your own data first:** check whether similar ventures or channels already have data. Ask: "Do you already have benchmarks from comparable ventures?"
   b. **Experiment history:** check past experiments.json files across ventures for the same channel — your own results are the best benchmarks
   c. **Online research:** Current benchmarks via WebSearch/Firecrawl for channel + industry + country + year. ONLY reputable sources (see `references/benchmark-sources.md`)
   d. **Fallback:** the built-in values in `references/benchmarks.md` — ALWAYS mark these as "fallback, not verified for this venture"

### Phase 2: Gap Analysis

0. **Funnel maths FIRST** (Growth Levers, Matt Lerner): before choosing experiments, write the funnel down as a numeric model (impressions → clicks → landing page views → conversions → activation, with current values or benchmarks) and work out **at which stage a 2x lever is even possible**. Only test there. A stage already close to the benchmark ceiling is not a lever, however easy the test would be. For subscription products, model the full bowtie (see rule 7).

1. Read `references/testing-hierarchy.md` for the chosen channel
2. Check against experiment history: what has already been tested?
3. Identify the next test according to the hierarchy:
   - Meta Ads: Hook -> Creative Format -> Copy -> CTA -> Audience
   - Google Ads: Keywords -> Headlines -> Descriptions -> Bidding
   - Landing Page: Headline -> Social Proof -> CTA -> Layout -> Form
   - LinkedIn: Hook -> Format -> Content Angle -> Hashtags -> Posting Time
   - Email: Subject Line -> Preview Text -> CTA -> Send Time -> Content

4. If current performance data is known, use the decision tree in `references/decision-trees/<channel>.md`

### Phase 3: Plan Output

For each proposed experiment (top 3, sorted by ICE):

```
## Experiment #1: [Title]
ICE Score: [X.X] (Impact: X | Confidence: X | Ease: X)

**Hypothesis:** if [change], then [expected result], because [rationale].

**Primary metric:** [Metric] | Target: [Threshold]
**Benchmark:** [Current industry value] (Source: [Source])

**Setup:**
- Channel: [Channel]
- Element: [what is being tested]
- Variants: [A vs. B description]
- Budget: [EUR X] | Duration: [X days]
- Optimisation goal: [e.g. landing page views on a budget under 100 per day]

**Kill rule:** [When to stop - e.g. "CTR < 0.5% after 48h"]
**Scale rule:** [When to scale up - e.g. "CPA in target range with 10+ conversions"]

**Next step if it wins:** [what follows logically]
**Next step if it loses:** [what follows logically]
```

After the plan, ask: "Shall I record one of these experiments in experiments.json?"

### ICE Score Calculation

Read `references/ice-scoring.md` for details. Summary:
- **Impact** (1-10): the gap between current performance and the benchmark. Bigger gap means higher score. It must match the funnel maths from phase 2 (where is 2x possible?).
- **Confidence** (1-10): the strength of the EVIDENCE, not the gut feeling (confidence meter, Evidence Guided / Gilad): your own conviction (1-2) < best practices and market data (3-5) < your own past test results on this or a similar venture (6-9) < launch data (10).
- **Ease** (1-10): Changing a hook = 10, landing page redesign = 3, new channel = 2.
- **Score** = (I + C + E) / 3

---

## Results mode: `/growth-lab results`

Read `skills/results.md` for the full workflow.

Summary:
1. Load `experiments.json` - show running experiments
2. User selects an experiment
3. Ask for channel-specific metrics
4. Apply the decision tree (`references/decision-trees/<channel>.md`)
5. Generate verdict + learnings + next recommendation
6. Update `experiments.json`
7. Ask: "Shall I update the project journal?"

---

## Review mode: `/growth-lab review`

Read `skills/review.md` for the full workflow.

Summary:
1. Load all `experiments.json` files (across ventures if no --venture is given)
2. Show: X tests run, Y winners, Z killed
3. Calculate win rate
4. Pattern detection: what works across ventures?
5. The top learnings of the week
6. Output in weekly update format

---

## Experiment data storage

File: `<venture-folder>/experiments.json`

If experiments.json does not exist, create it with an empty array.
If the venture folder is unclear: ask.

Schema: see `templates/experiment-schema.json`

---

## Interplay with other skills

**Upstream skill:**
- **`/growth-strategy`** — if you do not yet know WHICH channel to use, start there. growth-strategy answers "where do we play?", growth-lab answers "how do we play there?"

**Downstream skills (for execution):**

| growth-lab says | Then use |
|---|---|
| "Test a new hook on Meta" | `/meta-ads` for copy and creative |
| "Test LP headline" | your frontend tooling for implementation |
| "Test email subject line" | `/email-marketing` for sequence |
| "Test LinkedIn hook" | `/linkedin-content-writer` for post |
| Weekly review | `/weekly-update` for weekly report |
| CRO/conversion problem diagnosed | `/cro-audit` for deeper analysis |

---

## Rules

1. **NEVER assume data.** If info is missing: ask. No estimated audiences, budgets, or metrics.
2. **ALWAYS write hypotheses in this format:** "if [X], then [Y], because [Z]."
3. **Respect the testing hierarchy.** Hook before creative before copy before audience (Meta). Do not skip.
4. **Kill rules are binding.** When a kill criterion is met, recommend killing it — not "let it run a bit longer".
5. **Benchmarks with a source.** If it comes from web research, cite it. If it is a fallback, mark it as a "fallback benchmark".
6. **Use cross-venture learnings.** If a hook type worked on venture A, mention it on venture B.
7. **Bowtie rather than funnel for subscription products** (Revenue Architecture, Jacco van der Kooij): the funnel does not end at the close — onboarding, adoption/impact and expansion are experiment categories in their own right. Improvements on the right of the bowtie (churn, expansion) often compound harder than more top-of-funnel. For every plan, ask: does the next test belong on the right-hand side (activation email, time-to-impact, winback) rather than in the ads?
