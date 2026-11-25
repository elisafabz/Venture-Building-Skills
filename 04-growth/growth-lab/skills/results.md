# /growth-lab results - Log results

## Workflow

1. **Load experiment:** Read `experiments.json` in the venture folder. Show all experiments with status "running".
   - If there are no running experiments: "No running experiments found. Would you like to create one? (/growth-lab <venture> <channel>)"

2. **User selects experiment** (by ID or title)

3. **Query metrics** (channel-specific):
   - Read the channel from the experiment
   - Ask for the relevant metrics (see decision-trees/<channel>.md for the input metrics)
   - ALSO ask for the run time and the spend

4. **Research benchmarks:**
   - ALWAYS research current benchmarks online for the specific channel, industry and country
   - Compare results against researched benchmarks

5. **Apply decision tree:**
   - Read `references/decision-trees/<channel>.md`
   - Apply the logic to the metrics provided
   - Give a clear diagnosis + recommendation

6. **Generate output:**

```
## Experiment result: [Title]

**Hypothesis:** [Original hypothesis]
**Result:** [Metrics summarised]
**Benchmark comparison:** [Current vs. industry value (source)]

**Verdict:** Confirmed / Rejected / Inconclusive
**Reasoning:** [Why this verdict]

**Learning:** [What did we learn?]

**Recommended next test:**
[Based on the decision tree — what follows logically]
```

7. **Update experiments.json:**
   - Status: "running" -> "completed" or "killed"
   - Enter result metrics
   - Enter verdict + learnings
   - Enter next_action

8. **Ask:**
   - "Shall I update the project journal?"
   - "Shall I create the recommended next test as an experiment right away?"
