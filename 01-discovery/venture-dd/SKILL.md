---
name: venture-dd
description: >
  Use when the user asks for venture due diligence, market validation, or startup idea evaluation.
  Triggered by /venture-dd or phrases like "run a due diligence", "validate this idea",
  "evaluate this venture", "is this idea any good?", "market validation".
disable-model-invocation: true
model: sonnet
effort: medium
---

# Venture Due Diligence

> **Heavy skill.** Runs extensive web research across five hypotheses plus competitor and market sizing. A single run can consume a large number of tokens. It only runs when you invoke `/venture-dd` explicitly.

> **Requires:** web search.

Structured due diligence for venture ideas. Tests five critical hypotheses through web research,
analyses the competition and sizes the market.

## Critical rules

1. **No speculative early-stage KPIs.** NEVER calculate or present CAC, LTV, LTV:CAC ratio,
   payback period or break-even for ventures at idea or pre-revenue stage. These are pure fiction
   without years of real data. Skip the unit economics section entirely unless the venture has
   actual customer data.
2. **No scoping assumptions without explicit user approval.** NEVER lock into a target segment
   (e.g. "mid-market only"), a geography, a firm size or a beachhead vertical unless the user
   explicitly said so. If a scope decision is needed, ASK first. If the user gives a broad idea,
   keep the analysis broad.
3. **Match research to the actual business context.** When researching a vertical, make sure the
   analysis matches the use case. If the platform serves B2B advisory firms, research B2B cases —
   do not default to B2C data just because it is more available.

## Checklist

Complete these steps in order:

- [ ] Phase 1: gather the venture input
- [ ] Phase 2: identify and prioritise five hypotheses
- [ ] Phase 3: test the hypotheses through web research
- [ ] Phase 4a: competitor deep dive
- [ ] Phase 4b: calculate TAM/SAM/SOM
- [ ] Phase 4c: check unit economics (ONLY if the venture has real customer data — skip for
      idea stage)
- [ ] Phase 4d: pre-mortem and failure grid (derive kill criteria)
- [ ] Phase 5: generate the report from the template

## Phase 1: Gather input

Ask the user for the following. One question per message, never all at once:

1. **Value proposition** — what exactly does the venture solve?
2. **Target audience** — for whom exactly?
3. **Business model** — how does it make money?
4. **Market and region** — where? (country, region, global?)

If the user has already given a detailed description, do not ask follow-up questions — go
straight to phase 2.

## Phase 2: Identify hypotheses

Select five critical hypotheses from `references/hypothesis-patterns.md`. Adapt the wording to
the specific venture.

**Prioritisation (always in this order):**
1. Criticality — would failure kill the venture?
2. Uncertainty — how much do we NOT know?
3. Cost to test — cheap desk research first

Present the five hypotheses to the user before starting the research.

## Phase 3: Web research and hypothesis testing

Test each hypothesis individually via WebSearch. Use several search terms per hypothesis.

**Search strategy:**
- Non-English-speaking markets: search terms in the local language plus English technical terms
- English-speaking or international markets: English search terms
- Always search for failed predecessors as well
- Statista, Crunchbase and LinkedIn for market data

**Format per hypothesis:**

| Field | Content |
|---|---|
| **Hypothesis** | The full text |
| **Test method** | How it was tested |
| **Result** | What was found |
| **Source** | URL or source reference |
| **Status** | ✅ confirmed / ❌ refuted / ⚠️ unclear |
| **Evidence level** | 1-6 on the confidence meter (see below) |

**Confidence meter** (Evidence Guided, Itamar Gilad) — confidence is the strength of the
EVIDENCE, not the strength of the gut feeling:

1. Your own conviction or plausibility
2. Other people's opinions, thematic fit
3. Market data and competitor signals
4. User evidence (interviews, surveys)
5. Test results (fake door, prototype, concierge)
6. Launch data

Desk research alone reaches level 3 at most. Hypotheses at level 1-2 are opinion, not knowledge —
mark them as such in the report and propose them first for real tests (levels 4-5).

Every claim needs a source. No source means marking it as an estimate.

## Phase 4a: Competitor deep dive

Research the top five competitors (direct and indirect):

- Name, type (direct/indirect), strengths, weaknesses, funding and size
- Differentiation: how exactly does the venture stand apart?
- **Moat test** (7 Powers, Hamilton Helmer): "why does this keep winning?" must be answerable
  with one of the seven powers (scale economies, network economies, **counter-positioning** — the
  classic startup power, where the incumbent CANNOT copy without cannibalising its existing
  business — switching costs, branding, cornered resource, process power). Every power needs a
  benefit AND a barrier; "we are faster, better, cheaper" is not a power. Check which power is
  even achievable in the current phase.
- **Failed predecessors:** which similar ventures failed, and why? This is often the most
  important information.

Search Crunchbase, LinkedIn, app stores, G2 and Capterra, and the trade press.

## Phase 4b: Calculate TAM/SAM/SOM

Always do two calculations:

**Top-down:** total market × relevant share × price point
- Sources: the national statistics office of each target market, Eurostat, Statista, industry
  associations

**Bottom-up:** number of potential customers × expected ARPU × penetration
- Realistic assumptions, no fantasy numbers

Compare the two results. Large discrepancies mean the assumptions need checking.

## Phase 4c: Check unit economics

**⚠️ ONLY if the venture has real customer or revenue data.** For idea-stage ventures, SKIP this
section entirely. Speculative CAC, LTV and payback calculations for pre-revenue ventures are
fiction and must not be included.

If real data exists, assess:

| Metric | What |
|---|---|
| ARPU | Average revenue per user (monthly) — from real data |
| Gross margin | Gross margin (%) — from real data or a strong comparable |
| Revenue model viability | Does the pricing model make directional sense given comparable tools? |

Do NOT calculate CAC, LTV, LTV:CAC ratio, payback period or break-even unless they are based on
actual customer acquisition data. Benchmarks from comparables are fine for context, but never
fabricate venture-specific numbers.

## Phase 4d: Pre-mortem and failure grid

**Pre-mortem** (the inversion principle, Poor Charlie's Almanack, Munger: "invert, always
invert"): instead of asking "how does this succeed?", ask **"it is 12 months later and the
venture is dead — what killed it?"** List the three to five most likely causes of death,
concretely and grounded in the research. Derive a measurable kill criterion from each one (metric
plus threshold plus date).

**Failure grid** (Failbook, VNTR/PostFinance — four categories as a diagnostic lens): check which
failure type is most likely to threaten this venture.

| Failure type | Question | Frequency |
|---|---|---|
| **No-need fail** | Is there really a need — or just polite interest? | The most common cause |
| **Happy failure** | Would we ourselves be relieved if it ended? (a motivation check) | |
| **Failure by following management** | Does the venture depend on internal support that could evaporate? | |
| **Epic fail** | Which external dependency (partner, regulation, platform) can topple everything despite a good concept? | The most painful type |

The result of both analyses feeds into the report (risk section plus kill criteria).

## Phase 5: Generate the report

Use the template in `references/report-template.md` for the final report.

**Assign a risk score:**
- 🟢 **Green (fundable)** — strong signals, no fundamental blockers
- 🟡 **Yellow (needs work)** — potential is there, but open risks must be addressed
- 🔴 **Red (major blocker)** — fundamental problems identified, pivot or stop recommended

**Closing:** the top three recommendations (concrete, actionable) plus next steps as a checklist.

## Additional resources

### Reference files
- **`references/hypothesis-patterns.md`** — ready-made hypotheses by category (desirability,
  market, competition, business model, legal) with sub-patterns for B2B, B2C, marketplace, SaaS
  and regulated markets
- **`references/report-template.md`** — the complete Markdown template for the DD report

