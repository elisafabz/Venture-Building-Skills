# /growth-lab review - Weekly experiment review

## Workflow

1. **Load data:**
   - If `--venture <name>`: only the experiments.json of this venture
   - Without --venture: search ALL experiments.json files across ventures
   - Time window: last 7 days (by start_date or end_date)

2. **Generate summary:**

```
## Growth Lab Weekly Review - CW [XX]

### Overview
- **Experiments started:** X
- **Experiments completed:** Y
- **Winners (hypothesis confirmed):** Z
- **Killed:** W
- **Win rate:** Z/Y = XX%
- **Still running:** N

### Results by channel
| Channel | Tests | Winners | Killed | Running |
|---|---|---|---|---|
| Meta Ads | X | Y | Z | W |
| Landing Page | ... | ... | ... | ... |
| ... | ... | ... | ... | ... |

### Top learnings of the week
1. [learning 1 — across ventures where relevant]
2. [Learning 2]
3. [Learning 3]

### Pattern detection
[Are there patterns across multiple ventures?]
- e.g. "curiosity-gap hooks outperform pain-point hooks across all ventures targeting older audiences"
- e.g. "video ads never reached a CTR above 1% on any venture — static seems to work better"

### Recommendation for next week
[Based on the results: what should be tested next week?]
```

3. **Weekly update integration:**
   - Ask: "Shall I use this summary for the weekly update?"
   - If yes: provide output in weekly update format

4. **Track hypothesis accuracy:**
   - Over time: are the hypotheses getting more accurate?
   - If the win rate is below 20%: "Your hypotheses rarely hold. More research before the next test?"
   - If win rate > 50%: "Strong hit rate! You understand your audience well."
