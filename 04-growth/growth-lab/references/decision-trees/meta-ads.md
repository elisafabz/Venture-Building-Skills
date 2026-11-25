# Meta Ads Decision Tree

## Input metrics to query
Impressions, CTR, CPC, conversions, CPA, spend, days running, hook rate (video), hold rate (video)

## Decision logic

### Pre-check: Enough data?

- Fewer than 2,000 impressions? → "Too early to decide. Wait until at least 2,000 impressions."
- Runtime < 3 days? -> "Too early. Let it run at least 3 full days (weekday fluctuations)."
- Both checks passed? → continue to the diagnosis.

### Diagnosis (check in this order)

**1. Hook/creative problem?**
- CTR below 0.8% (or a hook rate below 20% on video)
- DIAGNOSIS: the ad does not stop the scroll. A hook problem.
- ACTION: test new hook - use a different category (see hook-categories.md)
- DO NOT CHANGE: landing page, audience, budget
- EXAMPLE HYPOTHESIS: "If we use a [curiosity gap] hook instead of [pain point], CTR will rise, because [reasoning based on the audience]."

**2. Creative is okay but not strong?**
- CTR between 0.8% and 1.5%
- DIAGNOSIS: creative works in principle but has room for optimisation
- ACTION: test hook variations of the existing angle (same category, different execution)
- ALTERNATIVE: switch creative format (static -> video, or test UGC)

**3. The ad works but the landing page does not?**
- CTR > 1.5% BUT CVR < 2% (or Bounce Rate > 60%)
- DIAGNOSIS: people click the ad but do not convert on the landing page. A message mismatch or a landing page problem.
- ACTION: test LP headline, social proof, or form
- DO NOT CHANGE: the ad creative (it is working)
- CHECK: does the ad's message match the landing page?

**4. Funnel works?**
- CTR > 1.5% AND CVR > 3%
- DIAGNOSIS: winner!
- ACTION: SCALE - increase budget by +20% every 3-5 days
- WATCH: frequency (above 3 on a cold audience means creative fatigue is starting)
- WATCH: CPA trend during scaling (CPA rising despite stable frequency = plateau)

**5. Too expensive?**
- CPA >50% above target AFTER spend >= 2x target CPA
- DIAGNOSIS: kill
- ACTION: pause. Start a new experiment.
- DO NOT: "let it run longer" or "reduce budget"

**6. Borderline case?**
- CPA close to target BUT fewer than 10 conversions
- DIAGNOSIS: sample size too small for a decision
- ACTION: let it run until at least 10 conversions
- MAXIMUM: no more than 3x target CPA spend without a clear signal

### Video-specific diagnosis

| Situation | Diagnosis | Action |
|---|---|---|
| Hook Rate > 30%, Hold Rate > 45% | Video works fully | Scale |
| Hook Rate > 30%, Hold Rate < 30% | Hook good, body loses viewers | Rework body (story arc, proof points) |
| Hook Rate < 20%, Hold Rate > 45% | Hook weak, but those who stay like it | Test 3-5 new hook variants, keep body |
| Hook rate below 20%, hold rate below 30% | The video is not working | An entirely new concept |

### Micro-budget rule (<EUR 100/day)

For budgets under EUR 100/day:
- NEVER optimise for conversions (too little data for Meta's learning phase)
- Optimization Goal = LANDING_PAGE_VIEWS
- Judge on CTR and landing page engagement, not on CPA
- Kill rule: no signal after 500 impressions per variant
