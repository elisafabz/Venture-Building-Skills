# Agent briefs (templates)

Replace {PLACEHOLDERS}. Always write the shared rules into one file (e.g. `/tmp/<project>/brief.md`) and point agents to it, so each prompt stays short. All agents: do not write to Figma or other tools, only to the directory you name.

## Brief A: problem tree per category

Task: build a problem tree for the category "{CATEGORY}" ({MARKET}, examples: {EXAMPLES}) in the same structure as the anchor tree. Focus: the interface to the anchor "{ANCHOR}" (e.g. commissioning, documentation, payment, liability, digitalisation).

Structure (reference = anchor tree, concise):
- Core: 1 sentence (<= 110 characters)
- 3 top effects (<= 55)
- 5 direct effects, each assigned to one top effect (<= 70)
- 6 causes (<= 55)
- 13 to 15 sub-causes, 2 to 3 per cause (<= 130 including source)
Direction: sub-cause -> cause -> core -> direct effect -> top effect.

Rules: every number with a source `[source year]`, otherwise `[N]`; primary sources with a real URL; write from the category's point of view as a business (their pain), so product opportunities become visible.

Output JSON: `{"category","core","top_effects":[3],"effects":[{"text","top":0}x5],"causes":[6],"subcauses":[{"text","cause":0}x13-15],"sources":[{"claim","url"}],"overlap_notes":"max 120 words: what is identical with which sibling category, recommendation own tree or merge"}`. Reply to the lead in max 100 words.

## Brief B: startup scouting (match x region)

The shared brief file contains: context, matches M1..Mn with problem (demand pain, supply pain) and search terms per match, method, output.

Method: grounded web research (fallback: web search); verify every company (fetch its homepage), check active/shut down/acquired; every number with a source; 4 to 8 startups, quality over quantity; partial solutions count; adjacent markets count if the mechanism transfers (note it).

Output JSON: `{"match","continent","startups":[{"name","url","country","founded","status":"active|acquired|shut down|unverified","covers":"full|partial","what_it_does":"<=30 words","which_part_of_match":"<=25","traction":"with source or empty","transferable_to_home_market":"yes|partial|no + reason","verified":"how"}],"coverage_note":"<=60 words: how crowded is the match there, gaps","queries_used":[]}`.

Task per agent: "Match {Mn}, region {REGION}. File: {PATH}". Regions: Europe, North America (incl. Central America/Caribbean), South America, Asia (incl. Middle East), Africa, Oceania.

### Brief B2: home market deep dive (one agent per match)
Additions: up to 12 entries; also incumbents/suites with type `startup|scaleup|incumbent`; extra fields `home_markets` (which countries of the home market it serves, with source), `law_specific` (yes/no/partial), `home_law_fit` (<=20 words), `segment`; search in the local language; re-verify companies already found and look for more; acquisitions, shutdowns and funding of the last 3 years; `coverage_note` answers: how crowded is the match, what is NOT solved, which gap is specific to the home market.

## Brief C: funding per chunk

Input: JSON list (name, url, country, status, matches, traction = lead from an earlier pass). `traction` is a lead, not truth.

Method: max ~3 searches per venture; rounds (pre-seed, seed, Series A/B/C, debt, grant, accelerator, revenue-based loan); keep equity, debt and grants separate; acquisition: acquirer, date, price; prefer company/investor announcements and trade press; Crunchbase/Tracxn/PitchBook only as `secondary`.

Output JSON per venture: `{"name","funding_status":"raised|bootstrapped|undisclosed|not_found","total_raised":{"amount","currency","text"},"rounds":[{"date","type","amount","currency","investors","source"}],"acquisition":{"acquirer","date","price"}|null,"confidence":"primary|secondary|unverified","conflict_with_earlier_pass":"<=20 words","note":"<=25"}`. Amounts as full numbers. "not_found" does not mean "no funding".

## Brief D: legal check per topic (optional, phase 7)
Check statements from an AI text one by one: verdict `confirmed|partly correct|incorrect|unverifiable`, correct version (<=60 words), who bears the duty (owner, manager, operator, contractor), sources with section and URL (primary law), reading level (primary text read / secondary). Mark paywalled standards as not read.
