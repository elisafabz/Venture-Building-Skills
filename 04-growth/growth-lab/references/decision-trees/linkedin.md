# LinkedIn Decision Tree

## Input metrics to query
Impressions, Engagement Rate (Likes+Comments+Shares / Impressions), Profile visits, Link Clicks, Follower growth, Post format

## Decision logic (Organic)

### Pre-check
- Fewer than five posts in the last month? → "Not enough data. Post at least twice a week for three weeks, then evaluate."

### Diagnosis

**1. Reach problem?**
- Impressions < 500 per post
- DIAGNOSIS: content reaches too few people
- ACTION: test posting time (Tue-Thu, 8-9 or 17-18 local time)
- ACTION: change the format (carousel and document posts often get more reach)
- CHECK: are you posting regularly? The algorithm penalises irregularity.

**2. Hook problem?**
- Impressions > 1000 BUT Engagement Rate < 2%
- DIAGNOSIS: people see the post but do not engage. The hook (first two lines) is not working.
- ACTION: change the hook completely - different category (see hook-categories.md)
- TIP: hooks that work on LinkedIn: a blunt insight, a surprising number, a counterintuitive statement
- DO NOT: write longer text or add more hashtags

**3. Content good, CTA weak?**
- Engagement Rate > 4% BUT Link Clicks < 1%
- DIAGNOSIS: the content resonates but nobody clicks the link
- ACTION: test CTA wording, CTA position (middle vs. end vs. first comment)
- TIP: putting the link in the first comment can help (the algorithm penalises external links in the post)

**4. Winning format found?**
- Engagement Rate > 5%
- DIAGNOSIS: format/topic performs above average
- ACTION: create variations of this format and topic. Do not reinvent the wheel.

## Decision logic (Ads)

For LinkedIn Ads the order is DIFFERENT from Meta — audience first:

**1. Test the audience** (the biggest performance swing on LinkedIn)
- Company size + industry vs. job title + seniority vs. skills vs. groups
- Ideal audience size: 10,000-20,000 for tests
- Minimum: EUR 50-100/day, otherwise too little data

**2. Test creative** (after audience winner)
- Sponsored Content: single image vs. carousel vs. video
- Lead Gen Forms vs. website conversion

**3. Test copy**
- Headline + description variations
