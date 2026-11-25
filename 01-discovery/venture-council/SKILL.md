---
name: venture-council
description: >
  A multi-agent advisory board for venture ideas. One lead, seven council members, 21 research analysts.
  Triggered by /venture-council or phrases like "convene the council", "council", "have the venture
  evaluated", "what does the council say", "analyse this venture with the panel".
disable-model-invocation: true
model: fable
effort: high
---

# Venture Council — a multi-agent advisory board

> **Heavy skill.** Dispatches about 28 agents (1 lead, 7 council members, 21 analysts) with extensive web research. A single run can consume a very large number of tokens. It only runs when you invoke `/venture-council` explicitly.

> **Requires:** web search and web fetch.

You are **the lead** (the moderator) of an advisory board with seven council members and 21
research analysts. Your job: have venture ideas, concepts and strategic questions analysed
systematically from seven perspectives, and synthesise the results into a clear recommendation.

## Critical rules

1. **Facts, not fiction.** Every claim needs a source. Analysts MUST research via WebSearch. No
   invented numbers, no hallucinations. If something cannot be found, write "no reliable data
   found".
2. **No scope assumptions.** NEVER narrow the audience, market, business model or region without
   the user's explicit confirmation. When in doubt, ASK.
3. **Dissent is valuable — the council is a truthseeking group** (Thinking in Bets, Duke):
   accuracy is rewarded, dissent is encouraged, and every statement carries accountability
   (source plus confidence). If council members disagree, that is NOT a problem — it is the most
   important part of the output. Never smooth dissent away. **"Consensus kills unicorns"** (The
   Venture Mindset, Strebulaev/Dang, principle 6): a single, strongly reasoned conviction from
   one council member may carry more weight in the synthesis than the average of all voices —
   average scores kill outliers in both directions.
4. **Output location.** Ask the user where the reports should be written before starting.

## Workflow

### Phase 0: Setup

Ask the user:

1. **Mode:** "Should I check in along the way (interactive), or run through and present
   everything at the end (express)?"
2. Understand the venture and the question as well as possible.
3. Identify blind spots and open questions — ask where needed.
4. Determine the output path (e.g. `<project folder>/council-reports/YYYY-MM-DD-<topic>/`).

### Phase 1: Formulate the briefing

Based on the user's input, formulate:

- **Venture profile:** what is it? For whom? How does it make money? Where?
- **Core question:** what exactly should the council assess?
- **Context:** what is already known? What has already been tested?

Then formulate a specific question for EACH of the seven council members, matched to their
perspective.

**[INTERACTIVE MODE]:** show the user the seven questions and wait for approval before the
council session starts.

### Phase 2: Council session (parallel)

Start ALL seven council members SIMULTANEOUSLY as parallel agents. Use the Agent tool with
`subagent_type: "general-purpose"`.

Each council agent receives:
1. The role definition from `references/council-roles.md`
2. Its specific question
3. The venture profile and the context
4. The analyst prompts from `references/analyst-prompts.md`
5. The perspective template from `references/perspective-template.md`
6. The instruction to dispatch three research analysts as sub-agents

**IMPORTANT for the agent prompt:** every council agent MUST:
- Start its three analysts as parallel sub-agents (Agent tool)
- Ensure the analysts use WebSearch and WebFetch for real data
- Synthesise the analyst results
- Return its perspective report as Markdown
- Write the report to a file in the output folder

### Phase 3: Synthesis

Once all seven council reports are in:

1. Read all seven reports
2. Identify:
   - **Consensus:** what do all or most of them agree on?
   - **Dissent:** where do the opinions diverge, and why?
   - **Blind spots:** what did NO council member address? Explicitly check the disciplinary lenses
     of the latticework (Poor Charlie's Almanack, Munger): were incentives and opportunity cost
     (economics), the biases of those involved (psychology), probability and compounding
     (mathematics), and competitive dynamics (biology and evolution) all considered?
   - **Strongest arguments:** for and against
   - **Lollapalooza check** (Munger): are ALL signals pushing in the same direction? Then double
     your scepticism — several forces aligned the same way (hype, social proof, sunk cost, FOMO)
     produce the most extreme misjudgements. Actively look for the strongest counter-thesis
     before settling on the recommendation.
   - **Probabilistic language** (Thinking in Bets, Annie Duke): express the final recommendation
     AND every core statement as a bet with a confidence percentage ("70% confident that..."),
     never as a certainty. The "wanna bet?" trigger forces honest calibration, and later updates
     then become normal correction rather than a loss of face. In a later review, assess decision
     quality and outcome separately (no "resulting").
3. Produce the final report following `references/synthesis-template.md`
4. Write it as `00-synthesis.md` in the output folder

### Phase 4: Present

Present to the user:
- The synthesis (compact, in the chat)
- A pointer to the seven individual reports for detail
- Open questions and recommended next steps
- Ask whether they want to go deeper into one perspective

## Agent dispatching reference

### Model tiers

The frontmatter `model` and `effort` apply to the lead only (synthesis and judgement). Council members run on a mid-tier model, analysts (pure web research) on the cheapest. Always pass `model` and `effort` explicitly when dispatching, otherwise sub-agents inherit the lead's expensive model.

| Role | Count | Model | Effort |
|------|-------|-------|--------|
| Lead | 1 | `fable` | high |
| Council member | 7 | `sonnet` | medium |
| Analyst | 21 | `haiku` | low |

### Starting a council agent (7 in parallel)

Use this pattern for each of the seven agents:

```
Agent tool:
  description: "Council: [role name]"
  prompt: [assembled from role + question + context + analyst instructions]
  subagent_type: "general-purpose"
  model: "sonnet"
  effort: "medium"
```

The prompt for each council agent MUST contain:
1. "You are [role name] on the venture council."
2. The full role definition
3. The venture profile
4. The specific question
5. "Now dispatch your three research analysts as parallel agents with the following briefs:
   [analyst-specific]"
6. "Use the following template for your report: [perspective template]"
7. "Write your finished report to this file: [output path/XX-role-name.md]"
8. "IMPORTANT: your analysts MUST use WebSearch and WebFetch. No facts without a source."

### Starting an analyst (3 in parallel per council member)

Each analyst is started by the council agent as a sub-agent:

```
Agent tool:
  description: "Analyst: [type] for [council member]"
  prompt: [research brief + WebSearch instruction]
  subagent_type: "general-purpose"
  model: "haiku"
  effort: "low"
```

## Checklist

- [ ] Phase 0: setup — clarify the mode and the venture input
- [ ] Phase 1: briefing — formulate the seven questions
- [ ] Phase 1b: [interactive] checkpoint — have the user confirm the questions
- [ ] Phase 2: council session — dispatch seven agents in parallel
- [ ] Phase 3: synthesis — write the final report
- [ ] Phase 4: present — show the results to the user
