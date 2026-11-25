# ICE Scoring

Every proposed experiment gets an ICE score for prioritisation.

## Formula

**Score = (Impact + Confidence + Ease) / 3**

Each factor is rated from 1 to 10.

## Impact (1-10)

How large is the expected effect on the primary metric?

| Score | Meaning |
|---|---|
| 9-10 | Current performance far below benchmark. Big lever. |
| 7-8 | Clear gap to benchmark. Clear room for improvement. |
| 5-6 | Moderate potential. Performance is okay but not good. |
| 3-4 | Performance already within benchmark range. Marginal improvement expected. |
| 1-2 | Performance already good/elite. Diminishing returns. |

## Confidence (1-10)

How confident are we in the hypothesis?

| Score | Meaning |
|---|---|
| 9-10 | Best practice with strong evidence + own experience confirms it |
| 7-8 | Best practice or our own data supports the hypothesis |
| 5-6 | Logically plausible, but no direct evidence |
| 3-4 | Intuition or a single anecdote |
| 1-2 | Pure speculation, counter-intuitive |

## Ease (1-10)

How fast and cheap is the test to run?

| Score | Meaning | Example |
|---|---|---|
| 9-10 | Under 1 hour, no budget | Change hook text, email subject line |
| 7-8 | 1-3 hours, minimal budget | Create new static ad, change CTA |
| 5-6 | Half a day, moderate budget | Shoot video ad, rebuild LP section |
| 3-4 | 1-2 days, significant budget | LP redesign, new campaign structure |
| 1-2 | More than 2 days, high budget | New channel, entirely new strategy |

## Auto-calculation

If possible, calculate ICE automatically:

- **Impact:** compare current metrics against benchmarks. The bigger the gap, the higher the score.
- **Confidence:** check the experiment history. Has this type of test worked before? Weight best practice on top.
- **Ease:** based on the element type (see the ease column in testing-hierarchy.md).

Where data is missing, estimate conservatively and mark it as an estimate.
