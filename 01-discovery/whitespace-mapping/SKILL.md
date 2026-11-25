---
name: whitespace-mapping
description: Use when the user wants to find a real whitespace or opportunity in a market by mapping both sides of it (an anchor customer group and its suppliers, partners and service providers), comparing their problems, and checking which startups worldwide already attack them. Triggers - "stakeholder mapping", "problem tree", "demand supply matching", "startup competition research", "find whitespace", "funding research", "cluster by solution", "who already solves this".
disable-model-invocation: true
model: sonnet
effort: high
---

# Whitespace Mapping

> **Heavy skill.** Runs many parallel research agents across both sides of a market. A single run can consume a large number of tokens. It only runs when you invoke `/whitespace-mapping` explicitly.

> **Requires:** Figma MCP (FigJam board); web search for the research agents.

Goal: find problems that hurt **both sides of a market** (an anchor stakeholder and its supply-side partners), then check who already tries to solve them (location, funding, solution approach). Output: a Figma/FigJam board plus a summary in chat.

The process is market-agnostic: anchor, home market and categories are parameters. Example anchor: building managers and their contractors, planners, financiers and utilities.

**Not pressure-tested.** This skill was distilled from a real working session, not validated with a subagent baseline. Note deviations on first use and fold them back in here.

## Hard rules

1. **Every number carries an inline source** `[source, year]`. No verifiable number: state the claim without a number and tag it `[N]`. Never invent figures.
2. **General research through a grounded web research tool**; if it hits a quota, fall back to plain web search and say in the result which claim came from which tool. Legal questions go through a legal research tool for the relevant jurisdiction, scientific questions through a literature search, not a general LLM (invented citations).
3. **Agent results are leads, not facts.** Agents often read only search snippets; "primary" then only means "a search result points to a company announcement". Conflicts between agents (HQ, amount, acquisition) are shown as conflicts on the board, not smoothed over.
4. **Evaluations live in chat only.** Files and boards stay neutral ("not found", not "the gap is huge").
5. **Never set scope silently.** Confirm market/country, target group and categories before phase 1.
6. **Announce the agent count before launching** and run at most 20 agents at once; start the rest as slots free up.

## Flow

| # | Phase | Result |
|---|---|---|
| 0 | Setup | anchor, country, categories, board URL, language confirmed |
| 1 | Stakeholder mapping | supply-side categories around the anchor |
| 2 | Problem trees | one tree per category (one agent each), merge decision |
| 3 | Matching | matches demand <> supply plus a unifying problem statement each |
| 4 | Startup competition | startups per match: worldwide by continent, then home market deep dive |
| 5 | Funding | amount, rounds, investors, source level, table and boxes |
| 6 | Clusters | startups per match grouped by solution approach |
| 7 | Whitespace check | scoring matrix, legal check, market sizing, interviews |

Briefs and schemas: `references/agent-briefs.md`. Board build and pitfalls: `references/figma-build.md`.

### 0 Setup
Ask (one question per message): Which demand anchor? Which country? Which supply categories (otherwise propose them from phase 1)? Target board (URL, page)? Is there already a tree for the anchor? Read an existing tree first and copy its style (colors, structure).

### 1 Stakeholder mapping
The anchor plus 4 to 6 supply categories (e.g. trades, facility services, planners and experts, commercial/legal/financial partners, utilities and authorities). Check whether a tree already exists for a category; focus that category on its interface to the anchor.

### 2 Problem trees
Structure per tree (modelled on the anchor tree): 1 core problem, 3 top effects, 5 direct effects, 6 causes, 13 to 15 sub-causes; causal direction sub-causes -> causes -> core -> effects. One agent per category (brief A). Every agent returns `overlap_notes`.

**Merge decision (lead):** if causes largely overlap (same payer, same mechanism), merge categories and justify the decision to the user. Example: trades and facility services became one tree (same payment and price-pressure chain), so 5 categories became 4 trees. Assign distinct leftovers (e.g. emergency services, network/authority topics) deliberately.

Build the trees in Figma (see `references/figma-build.md`), one section per tree, in the style of the anchor tree.

### 3 Matching
Lay the anchor tree against all supply trees. Match types: **strong** (same problem, several supply trees name it), **chain** (the anchor's pressure lands on the partner), **weak** (same problem without an interface), **no counterpart** (one side only). For each match write **one problem statement that unites both sides**, plus one sentence for each side's view. Result as a board page "Demand <> Supply": left column demand, middle the common denominator, right the supply side per tree.

### 4 Startup competition
1. **Worldwide:** one agent per match per continent (Europe, North America, South America, Asia, Africa, Oceania). One shared brief file; the task per agent is only match + continent (brief B). Each agent returns JSON.
2. **Home market deep dive:** one agent per match, home market only, including incumbents, HQ, markets served, legal fit (brief B2).
3. Dedupe across all files (name aliases); the home market takes precedence. Highlight home-market HQs on the board.
4. Classify: region, status (active, acquired, shut down, unverified), coverage (full, partial), fit in the home market.

### 5 Funding
Collect unique ventures, split by region into chunks (about 25 each) and hand them to agents (brief C). Consolidate: amounts roughly converted to a common currency with **fixed, visibly stated rates**; never silently add equity, debt and grants; mark sums of rounds with "≥"; source level P/S/U; conflicts in the notes column. Merge duplicates (aliases). Presentation: a color-coded box per card, one sorted table, one list of ventures without findings. Figures from aggregators (Tracxn, PitchBook, CB Insights) are secondary only.

### 6 Clusters by solution approach
Per match 4 to 6 clusters by **solution approach** (not by country). A startup may appear in several clusters. Per cluster: a short description of the approach and a line "In home market: ..." (names with country, or "none found"). Above the clusters, the unifying problem statement. Assign every startup; add unassigned ones to a cluster, never drop them.

### 7 Whitespace check (in chat, not on the board)
Candidates: "none in the home market" plus mechanism proven abroad. Score 1 to 5: pain on both sides, willingness to pay, competition in the home market, defensibility, time to revenue. Then: (1) incumbents that could build it in 6 to 12 months; (2) legal check with a legal research tool; (3) bottom-up market sizing with sources; (4) interviews on both sides plus a fake-door test with kill criteria set in advance. Follow up with due-diligence, kill-criteria and benchmark checks.

**Agent models.** The frontmatter model is for the lead only. Pass `model` and `effort` explicitly when dispatching: problem-tree agents (brief A) on `sonnet` / medium; search and extraction agents (briefs B, B2, C) on `haiku` / low. Without it, sub-agents inherit the lead's model.

## Common mistakes

| Mistake | Counter |
|---|---|
| Agent figure taken as fact | Show the source level, mark conflicts |
| Same company under two names | Alias map, merge |
| Grouping by country instead of solution approach | Cluster = approach, country only on the card |
| Evaluative sentences on the board | Neutral on the board, evaluation in chat |
| FigJam moves sections when creating them | Set position again at the end of the script |
| More than 20 agents at once | Batch, start the rest later |
| Legal statement taken from AI text | Verify against primary law (one agent per legal topic) |
