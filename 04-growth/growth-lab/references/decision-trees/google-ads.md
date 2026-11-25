# Google Ads Decision Tree

## Input metrics to query
Impressions, Clicks, CTR, CPC, Conversions, CPA, Quality Score, Search Terms (Top 5)

## Decision logic

### Pre-check
- Fewer than 100 clicks? -> "Too early. Wait until at least 100 clicks."
- Runtime < 14 days? -> "Google Ads experiments need at least 2 weeks."

### Diagnosis

**1. Relevance problem?**
- Quality Score < 5
- DIAGNOSIS: a keyword-ad-landing page mismatch. Google does not consider your ad relevant to the query.
- ACTION: align the ad copy more closely with the keyword; the landing page headline must contain the keyword
- CHECK: Search Terms report - are irrelevant queries getting through? Add negatives.

**2. Headline problem?**
- CTR below 2% (search) with a quality score of 5 or higher
- DIAGNOSIS: the ad is shown but not clicked. The headlines are not compelling enough.
- ACTION: test new headlines (benefit-focused, with keyword, numbers/data)
- TIP: provide 6-10 unique headlines, use pinning sparingly

**3. LP problem or wrong intent?**
- CTR > 5% BUT CVR < 2%
- DIAGNOSIS: people click but do not convert.
- CHECK: is the keyword transactional or informational?
  - Informational (e.g. "what is X") → the keyword does not match the conversion goal
  - Transactional (e.g. "buy X") -> LP problem, test headline/CTA/form

**4. Does it work?**
- CPA in target range with 10+ conversions
- DIAGNOSIS: scale
- ACTION: increase budget, add similar keywords, test Broad Match
- Moving from "Poor" to "Excellent" Ad Strength = on average +15% clicks

**5. Too expensive?**
- CPA >50% above target after 2x CPA spend
- DIAGNOSIS: kill these keywords/ads
- ACTION: pause, test other keywords or angles
