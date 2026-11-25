# Landing Page Decision Tree

## Input metrics to query
Visitors, bounce rate, scroll depth (% reaching 50%), CTA clicks, CTA click rate, conversions, CVR, page load time

## Decision logic

### Pre-check
- Fewer than 300 visitors? -> "Too early. At least 300 visitors for reliable conclusions."
- Page load time > 3 seconds? -> "Technical problem. Fix page speed before testing content."

### Diagnosis

**1. First-impression problem?**
- Bounce Rate > 60%
- DIAGNOSIS: the hero section does not resonate. Visitors leave immediately.
- ACTION: test headline
  - Benefit-focused vs. feature-focused vs. social proof
  - Clarity beats cleverness: "what am I selling?" must be immediately obvious
  - The Julian Shapiro rule: the header must describe COMPLETELY what is being sold
- CHECK: is the traffic coming from the right source? (ad-message match)

**2. The content does not hold them?**
- Bounce Rate < 50% BUT Scroll Depth < 30%
- DIAGNOSIS: visitors stay briefly, but the content after the hero does not convince
- ACTION: test section order, add visual breaks
- TIP: move the social proof closer to the hero

**3. CTA problem?**
- Scroll Depth > 50% BUT CTA Click Rate < 3%
- DIAGNOSIS: visitors read the content but do not act
- ACTION: test CTA text (action-oriented instead of "Submit"), colour, position, count
- TIP: personalised CTAs convert 202% better than generic ones
- TIP: a single CTA converts better than 2-4 links

**4. Form friction?**
- CTA Click Rate > 3% BUT form conversion < 20%
- DIAGNOSIS: visitors want to act, but the form blocks them
- ACTION: reduce fields (up to +120% uplift!), test multi-step
- RULE: every additional field reduces conversions

**5. Does it work?**
- CVR > 7%
- DIAGNOSIS: LP works well
- ACTION: increase traffic instead of optimising further. Look for other levers.
- DO NOT: keep tinkering with the landing page (diminishing returns)

### Smoke test / fake door evaluation

If the landing page is a smoke test for a new idea:
- CTA click rate above 3-5%? → a positive demand signal
- At least 300 cold visitors (not existing customers)
- Define the success criteria BEFOREHAND, do not bend them afterwards
