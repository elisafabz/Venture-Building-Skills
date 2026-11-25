# Email Decision Tree

## Input metrics to query
Sends, Opens, Open Rate, Clicks, Click Rate, Click-to-Open Rate, Unsubscribes, Unsubscribe Rate

## Decision logic

### Pre-check
- Fewer than 100 recipients? → "The list is too small for statistically meaningful tests. Focus on list growth."
- Only one email sent? → "Send at least 3-5 emails before patterns become visible."

### Diagnosis

**1. Subject line problem?**
- Open Rate < 15%
- DIAGNOSIS: emails are not being opened. The subject line is not working.
- ACTION: test subject lines:
  - Shorter vs. longer (under 50 characters often better)
  - Personalisation ("[First name], ...")
  - Curiosity gap ("the one thing that...")
  - Numbers/data ("87% make this mistake")
  - An emoji in the subject — test whether it works for your audience
- CHECK: deliverability ok? (SPF/DKIM/DMARC configured?)

**2. Content/CTA problem?**
- Open Rate > 25% BUT Click Rate < 2%
- DIAGNOSIS: emails are opened but nobody clicks. The content or the CTA is not convincing.
- ACTION:
  - Make the CTA more prominent (higher up, larger button)
  - Shorten the content (less scrolling to reach the CTA)
  - One clear CTA instead of several (Paradox of Choice)
  - CTA text: benefit instead of action ("Claim free offer" instead of "Click here")

**3. Frequency/relevance problem?**
- Unsubscribe Rate > 1%
- DIAGNOSIS: too many emails, or the wrong content for this audience
- ACTION:
  - Reduce frequency
  - Improve segmentation (not everyone gets everything)
  - Raise the value of the content: what does the reader get here that they cannot get elsewhere?

**4. Does it work?**
- Click Rate > 3% AND Unsubscribe Rate < 0.3%
- DIAGNOSIS: format/template works
- ACTION: make this format the standard. Test variations rather than changing it wholesale.

### A/B test setup for email

- At least 1,000 recipients per variant
- 50/50 split or 20/20/60 (20% test A, 20% test B, 60% winner)
- Only ONE variable per test (subject line OR CTA, not both)
- Wait 24-48 hours before evaluation
