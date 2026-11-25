---
name: health-claims-audit
description: Audit health and medical product claims against EU regulation — EU MDR, Health Claims Regulation, Cosmetics Regulation, and advertising law for health-related products
model: opus
effort: high
---

# Health Claims Audit — Medical & Health Product Advertising Compliance

This skill audits all health-related claims, medical product advertising, and wellness/health
copy on a website for compliance with EU regulation. It checks for prohibited claims, missing
disclaimers, misleading language, and ensures the correct legal framing for the product category.

No arguments needed. Just run `/health-claims-audit` and the skill scans the project
automatically.

**Difference from other audits:**
- `/legal-audit` checks **general website compliance** — GDPR, legal notice, cookies, e-commerce
- `/health-claims-audit` checks **health-specific advertising law** — what you can and cannot
  claim about health products

**Important:** this skill flags legal risks in health advertising copy. It is NOT legal advice.
All findings should be reviewed by a regulatory affairs specialist or a health advertising lawyer
before publication.

## Regulatory scope — what applies EU-wide and what does not

This distinction drives every severity rating, so establish it before auditing:

**Directly applicable EU-wide (regulations):**
- EU Medical Device Regulation (EU MDR), Regulation (EU) 2017/745 — Art. 7 prohibits misleading
  claims about function, performance and intended purpose
- Health Claims Regulation, Regulation (EC) 1924/2006 — including Art. 12 (no claims referring to
  the prevention, treatment or cure of disease on foods)
- Food Information to Consumers, Regulation (EU) 1169/2011
- Cosmetics Regulation, Regulation (EC) 1223/2009, plus the Common Criteria in Regulation (EU)
  655/2013
- EFSA register of authorised health claims

**Harmonised by directive, implemented differently per country:**
- Advertising of medicinal products: Directive 2001/83/EC, Title VIII (Art. 86-100). Art. 88(1)
  prohibits advertising prescription-only medicines to the general public EU-wide, but the
  mandatory particulars and their formatting are set nationally
- Unfair and misleading advertising: Directive 2005/29/EC (unfair commercial practices) and
  Directive 2006/114/EC (comparative advertising)
- **Advertising of medical devices to consumers is largely national.** The MDR governs the
  product and its claims, but the mandatory wording in consumer advertising (the equivalent of a
  "consult the instructions for use" notice) comes from national law and differs by country

**Practical consequence:** flag findings that rest on a regulation as firm. Flag findings that
rest on national advertising law as "verify against the rules in `country`". Ask the user which
country or countries the product is marketed in and record it as `country`.

---

## Step 0: Understand the project

Before auditing, read:
- `CLAUDE.md` / `README.md` for project context
- All product descriptions and claims
- All landing page copy, hero sections, feature descriptions
- Testimonials and user stories
- FAQ content (often contains implicit health claims)
- Legal pages (terms, privacy policy — may contain product classification info)
- Image and video content descriptions (before/after, body imagery)
- Meta descriptions and ad copy (if present)

---

## Step 1: Business model interview

**STOP. Before auditing anything, ask the user the following questions.** The answers
fundamentally change what is allowed and what is not. Use AskUserQuestion to collect all answers
before proceeding.

Present a brief intro:

> Before I start the audit I need some information about your business model — what you may and
> may not claim depends heavily on how your product is classified in regulatory terms, which
> markets you sell into, and who you work with.

### Question 0: Markets

> Which countries do you market this product in?

Options:
- One EU country only
- Several EU countries
- EU plus UK / Switzerland
- Not sure yet

### Question 1: Product category

> What is your product?

Options:
- Medical device (CE-marked, defined intended purpose)
- Food supplement
- Cosmetic product
- Software / app
- Physical wellness or lifestyle product
- Service (coaching, consulting, course)
- Combination / not sure

### Question 2: Professional collaboration

> Do you work with medical professionals or institutions?

Options:
- Yes, medical director / medical advisory board (named, verifiable)
- Yes, collaboration with doctors or therapists (e.g. content is medically reviewed)
- Yes, accredited laboratory or research institution
- Yes, clinical studies exist (our own or third-party)
- No formal medical collaboration
- Not sure

**Why this matters:** with medical collaboration you may write things like "developed with
doctors" or "medically reviewed" — without it, the same claim would be unlawful. Clinical studies
enable stronger efficacy statements. An accredited laboratory supports "laboratory tested".

### Question 3: Evidence base

> What evidence do you have for your efficacy claims?

Options:
- Our own clinical studies (RCT, peer-reviewed)
- Our own clinical studies (not peer-reviewed)
- Third-party studies supporting the active ingredient or method
- EFSA-authorised health claims (for food supplements)
- Observational data / user experience data
- No formal evidence, only testimonials
- Not sure

**Why this matters:** "clinically proven" is only defensible with your own peer-reviewed studies.
"Studies show" also works with third-party studies. Without evidence, only vague wellbeing claims
remain.

### Question 4: Audience and distribution channel

> Who is your primary audience and how is the product distributed?

Options:
- Consumers (B2C, freely available)
- Professional audience (B2B: doctors, clinics, pharmacies)
- Both (separate areas on the website)
- Consumers, but only via pharmacies or specialist retail
- Consumers, direct online sales

### Question 5: Regulatory status (if medical device or app)

> If this is a medical device or software: what is the regulatory status?

Options:
- CE-marked, class I
- CE-marked, class IIa / IIb / III
- CE process ongoing
- Deliberately NOT a medical device (wellness positioning)
- Not applicable (not a medical device, not an app)

### Question 6: Existing disclaimers / legal advice

> Have you already obtained legal advice on your health claims?

Options:
- Yes, a lawyer or regulatory affairs specialist has cleared the claims
- Yes, but only partially (e.g. only the legal notice, not the claims)
- No legal review yet
- Not sure

---

### Step 1b: Build the audit profile

Based on the answers, build the **audit profile** that governs the entire audit. Present it to
the user before continuing:

```
## Audit profile

| Parameter | Value |
|-----------|-------|
| Product category | [answer Q1] |
| Markets | [answer Q0] |
| Regulatory framework | [derived: EU MDR / Health Claims Regulation / Cosmetics Regulation / unfair commercial practices only] |
| Professional collaboration | [answer Q2] |
| Permitted claim strength | [see matrix below] |
| Audience | [answer Q4] |
| Consumer advertising permitted? | [Yes / No / Restricted] |
| Evidence base | [answer Q3] |
| Existing legal advice | [answer Q6] |
```

### Claim strength matrix

The combination of evidence and professional collaboration determines how strong your claims may
be:

| Evidence \ Collaboration | None | Medical board / review | Accredited lab | Own clinical studies |
|--------------------------|------|------------------------|----------------|----------------------|
| **No formal evidence** | Wellbeing claims only ("may support") | + "medically supervised" | + "laboratory tested" | — |
| **Third-party studies** | "based on scientific findings" | + "recommended by doctors" possible | + "scientifically grounded" | — |
| **Own studies (not peer-reviewed)** | "in observational use we saw..." | + "developed and tested by doctors" | + "laboratory tested" | — |
| **Own studies (peer-reviewed)** | "clinically tested" + source | + "clinically proven" + source | + "clinically and laboratory tested" | Strongest claims permitted (with citation) |
| **EFSA list (supplements only)** | Exact wording of the authorised claim | + claim + "recommended by doctors" | + claim + "laboratory tested" | — |

**Important:** the matrix shows the MAXIMUM claim strength. Every individual claim must still be
checked against the specific prohibitions in the audit categories below.

Ask: **"Does this audit profile look right? Then I'll start the audit."**

Wait for confirmation before proceeding to Step 2.

---

## Step 1c: Product classification (decision tree)

Using the interview answers, classify the product. The rules differ dramatically by category.

### Decision tree:

```
Is it a medical device (CE-marked, defined intended purpose)?
├── Yes → Category A: medical device (EU MDR 2017/745)
│   ├── Prescription-only? → consumer advertising PROHIBITED
│   ├── Only usable by health professionals? → consumer advertising PROHIBITED
│   └── Freely available, self-administered? → consumer advertising PERMITTED (with restrictions,
│       set by national law)
│
├── No → Is it a food supplement?
│   ├── Yes → Category B: supplement (Health Claims Regulation 1924/2006 + FIC 1169/2011)
│   └── No → Is it a cosmetic product?
│       ├── Yes → Category C: cosmetics (Cosmetics Regulation 1223/2009 + Common Criteria 655/2013)
│       └── No → Is it an app or software?
│           ├── Medical purpose (diagnosis, therapy, monitoring)? → Category A: SaMD
│           └── Wellness / lifestyle? → Category D: wellness/lifestyle
│
└── Service (coaching, consulting)?
    ├── Health-related? → unfair commercial practices rules + national rules on regulated
    │   professions (psychotherapy, medicine, physiotherapy)
    └── Lifestyle / wellness? → unfair commercial practices rules only
```

**Flag for manual review** if the classification is unclear or the user answered "not sure".
Misclassification is the number one regulatory risk.

**Adjust severity ratings based on the audit profile:**
- No legal review yet (Q6) → bump borderline 🟡 issues to 🟠
- No formal evidence (Q3) plus strong claims on the site → bump to 🔴
- Formal medical collaboration (Q2) → claims referencing that collaboration are ALLOWED (do not
  flag them)
- Peer-reviewed studies (Q3) → "clinically proven" plus source citation is ALLOWED
- Several markets (Q0) → apply the strictest national rule among them, and say which country
  drives it

---

## Step 2: Audit across 8 categories

**Use the audit profile from Step 1 throughout.** The claim strength matrix determines whether a
specific claim is allowed, borderline or unlawful for THIS project. Do not flag claims as
violations if the business model supports them (e.g. "medically reviewed" is fine if Q2 confirmed
medical collaboration).

Go through **each category** below. For every issue found, note the file, the specific legal
requirement, and the recommended fix. Rate severity as:
- **🔴 Critical** — unlawful claim, risk of enforcement action, fines or product seizure
- **🟠 Major** — legally risky, likely non-compliant, fix before publication
- **🟡 Minor** — borderline, could be challenged, tighten the language

---

### Category 1: Prohibited healing claims

#### Absolute prohibitions — never use
> These claims are unlawful in consumer advertising for all health product categories.

**Scan all copy for:**
- "cures" / "cure" / "cured" — healing claims are prohibited
- "eliminates" / "removes" (a disease or symptom) — healing claim
- "guaranteed" plus a health statement — inadmissible guarantee
- "replaces your doctor" / "no doctor needed" / "instead of therapy" — prohibited
- "miracle cure" / "breakthrough" / "revolution" — exaggeration
- "100% effective" / "works for everyone" — inadmissible absolute claim
- "no side effects" / "completely safe" / "risk-free" (health-related) — misleading
- "clinically proven" without a citation — misleading
- "doctors recommend" without a demonstrable basis — misleading
- "immediate effect" / "instant results" for health claims — exaggerated

**Legal basis:** Art. 7 EU MDR for devices; Art. 12 Regulation 1924/2006 for foods; Art. 6 and 7
of Directive 2005/29/EC for misleading commercial practices generally.

**Fix pattern:** replace absolute claims with evidence-based, qualified wording:
- "cures" → "may support..." / "contributes to..."
- "eliminates pain" → "may help relieve pain"
- "guaranteed" → "in studies we observed..." / "many users report..."
- "replaces your doctor" → "as a complement to medical care"
- "clinically proven" → "in a clinical study with N participants we observed..." plus citation

---

#### "Better than" comparisons
> Comparative advertising against medical treatment or other products is high risk.

**Check for:**
- "better than [medicine/treatment]" — prohibited without solid evidence
- "more effective than" / "superior to" — comparison without a head-to-head study
- "replaces [medicine]" — implies superiority over medical treatment
- "the natural alternative to [medicine]" — implicit efficacy comparison
- "without the side effects of [medicine]" — misleading comparison

**Legal basis:** Directive 2006/114/EC requires comparative advertising to compare like with like
on verifiable, material and representative features.

**Fix pattern:** compare only on your own evidence and never against medical treatment. Instead
of comparing, state your own benefits positively without referring to other products or
therapies.

---

### Category 2: Mandatory particulars (consumer advertising of medical devices)

> **National rule.** The MDR governs the device and its claims, but the mandatory particulars in
> consumer advertising are set by national law and differ per country. Verify the exact
> requirements and the exact required wording for `country` before flagging or fixing.

**Check for presence of:**
- Name of the medical device (trade name)
- Short description of the intended purpose
- Essential information for correct use
- Reference to possible undesirable effects (where applicable)
- Reference to particular safety precautions (where applicable)
- The mandatory advisory notice required in the target market (typically along the lines of
  "read the instructions for use; if in doubt, ask your doctor or pharmacist" — use the exact
  national wording)
- For audio/video: the mandatory notice must be clearly perceptible acoustically

**Fix pattern:** place mandatory particulars as a footer disclaimer on every page carrying
product advertising. On landing pages, put them below the hero section rather than only in the
footer. For video and audio, add a spoken notice at the end.

---

#### Reminder advertising vs. full advertising
> Name plus logo only, with no intended purpose or claims, counts as reminder advertising (fewer
> obligations). As soon as you say what the product is good for, it becomes full advertising with
> the complete set of obligations.

**Check for:**
- Pages that make claims but carry no mandatory particulars
- Social media posts with efficacy statements but no disclaimer
- Banners and ads stating the intended purpose but without the mandatory notice

**Fix pattern:** either reduce to reminder advertising (name, logo, brand only) or add the full
mandatory particulars.

---

### Category 3: Audience separation (public vs. professionals)

#### Consumer advertising vs. professional advertising
> Strict separation is required. Anything aimed at the general public is subject to the strictest
> rules.

**Check for:**
- Prescription-only products → advertising to the general public is prohibited (Art. 88(1)
  Directive 2001/83/EC for medicinal products; equivalent national rules for devices)
- Products intended only for health professionals → consumer advertising prohibited
- Products whose instructions require medical supervision → consumer advertising prohibited
- Technical claims (study details, mechanisms of action) on consumer-facing pages
- No clear separation between the professional and consumer areas of the website

**Fix pattern:**
- Professional area: behind a login, or clearly labelled "for healthcare professionals"
- Consumer area: only permitted claims, mandatory particulars, no detailed technical information
- If the product is prescription-only: no advertising at all in the public area

---

#### Children as an audience
> Advertising aimed primarily or exclusively at children is highly problematic for medical
> devices.

**Check for:**
- Advertising addressed directly to children (language, imagery, tone)
- Cartoon characters or mascots in medical device advertising
- Gamification elements that address children as the audience

**Fix pattern:** address medical device advertising to parents and guardians, not to children
themselves.

---

### Category 4: Imagery and before/after

> **Mixed basis.** Misleading imagery is caught EU-wide by Art. 7 MDR and Directive 2005/29/EC.
> Explicit bans on specific image types (shock imagery, before/after on the body) are national —
> verify for `country`.

**Check for:**
- Before/after images of the body (surgery, wounds, skin conditions)
- Drastic disease imagery used to create fear
- Shock images used to drive motivation
- Images of operations or invasive procedures
- Extreme close-ups of disease symptoms

**Permitted (with restrictions):**
- Factual product images
- Schematic representations (infographics, drawings)
- Lifestyle images showing the product in use
- Restrained before/after for cosmetics (not for medical devices)

**Fix pattern:** replace drastic imagery with factual product shots, schematic representations or
lifestyle photography. No fear triggers.

---

### Category 5: Testimonials and social proof (health context)

#### Testimonials — strict rules
> Recovery testimonials and healing stories are prohibited as advertising material in consumer
> advertising.

**Check for:**
- Testimonials describing a cure: "my [condition] is gone"
- Testimonials that encourage self-diagnosis
- "doctors recommend" without a demonstrable basis
- Testimonials naming specific medical diagnoses
- Recovery narratives used as advertising ("after two weeks my back was pain-free")
- Celebrities or influencers making health claims without disclosure

**Permitted:**
- General satisfaction statements: "I'm happy with the product"
- Usage experience without healing claims: "the product is easy to use"
- Vague improvements in wellbeing: "I feel better"
- Always with a disclaimer: "individual experience, results may vary"

**Fix pattern:** limit testimonials to usage experience and satisfaction. No specific conditions
or recovery narratives. Always add a disclaimer.

---

### Category 6: Food supplements and the Health Claims Regulation

#### Authorised vs. unauthorised health claims
> For foods (including supplements) only health claims authorised on the EU list may be used.
> This is Regulation (EC) 1924/2006 and applies directly in every member state.

**Check for:**
- Health-related statements with no basis in the EU health claims list
- "strengthens the immune system" — only permitted where the ingredient and dose are on the EFSA
  list
- "good for joints" — only permitted with an authorised claim
- "detox" / "detoxification" / "cleansing" — no authorised claims, misleading
- "anti-ageing" for supplements — not an authorised health claim
- Disease-related claims for supplements — entirely prohibited (Art. 12 Regulation 1924/2006)
- "helps with [disease]" — prohibited for foods and supplements
- Missing mandatory particulars in supplement advertising

**Mandatory particulars for supplements** (Regulation 1169/2011 and the food supplements
directive as implemented nationally):
- The product must be clearly identifiable as a food supplement
- Recommended daily dose
- A statement that supplements are not a substitute for a varied diet
- A statement to keep the product out of the reach of children
- A warning not to exceed the recommended daily dose

**Fix pattern:** check every health claim against the EFSA list
(https://ec.europa.eu/food/safety/labelling-and-nutrition/claims/health-claims). Remove
unauthorised claims or replace them with authorised ones. Add the mandatory particulars.

---

### Category 7: Cosmetics claims

#### Cosmetics Regulation 1223/2009 plus the Common Criteria
> A cosmetic product may not promise an effect that goes beyond the surface of the skin. The
> Common Criteria (Regulation (EU) 655/2013) set six principles for cosmetic claims: legal
> compliance, truthfulness, evidential support, honesty, fairness, and informed decision-making.

**Check for:**
- Claims that go beyond cosmetic effect ("cures acne" is a medicinal claim)
- "medically effective" for a cosmetic — prohibited
- "dermatologically tested" without actual testing — misleading
- "hypoallergenic" / "suitable for allergy sufferers" without substantiation
- "100% natural" where synthetic ingredients are present
- "clinically tested" without study details
- Claims about influencing biological processes ("repairs DNA", "regenerates cells")
- Exaggerated before/after results

**Permitted for cosmetics:**
- "cares for the skin" / "provides moisture" — cosmetic effect
- "improves the appearance of the skin" — appearance, not medical
- "dermatologically tested" — where testing actually took place
- Before/after with realistic presentation (no retouching, identical lighting)

**Fix pattern:** limit cosmetic claims to appearance and care. No medical efficacy promises.
Every "tested" claim needs an actual study behind it.

---

### Category 8: Software as a Medical Device (SaMD) and wellness apps

#### Drawing the line for apps and software
> An app that diagnoses, treats or monitors is a medical device under the EU MDR. An app for
> wellness or lifestyle is not a medical device, but advertising law still applies.

**Check whether the app or software is a medical device:**
- Calculates medical diagnoses or risk scores
- Gives therapy recommendations based on health data
- Monitors vital signs for a medical purpose
- Controls or influences a medical device
- Claims such as "diagnoses", "detects [disease]", "monitors your state of health"

**If it is a medical device → all rules from categories 1 to 5 apply.**

**If it is a wellness or lifestyle app:**
- Make no medical claims ("improves your health" is borderline)
- Position it clearly as wellness or lifestyle, not as a medical product
- "may contribute to your wellbeing" instead of "improves your health"
- Do not advertise diagnostic functions
- Unfair commercial practices rules still apply: no misleading advertising

**Grey-zone wording for wellness apps:**

| ❌ Sounds like a medical device | ✅ Stays in wellness territory |
|--------------------------------|-------------------------------|
| "Diagnoses sleep disorders" | "Analyses your sleep patterns" |
| "Treats anxiety" | "Supports you in relaxing" |
| "Monitors your state of health" | "Helps you keep track of your habits" |
| "Detects depression" | "Reflects your mood over time" |
| "Treats back pain" | "Guides you through back exercises" |
| "Medically validated" | "Based on scientific findings" |
| "Replaces your therapist" | "A complement to professional support" |
| "Cures relationship problems" | "Supports you in everyday life" |
| "Psychological treatment" | "Prompts for your relationship" |

**Fix pattern:** clear positioning — wellness is not medicine. For every claim ask: would a
regulator read this as a medical intended purpose? If yes, rewrite it.

---

## Step 3: Report findings

Present findings grouped by severity. **Always include the audit profile at the top** so the
reader understands the basis for the severity ratings.

```
## Health Claims Audit Results

### Audit profile (basis for the assessment)
| Parameter | Value |
|-----------|-------|
| Product category | [from Q1] |
| Markets | [from Q0] |
| Professional collaboration | [from Q2 — critical for claim strength] |
| Evidence base | [from Q3] |
| Permitted claim strength | [from matrix] |
| Audience | [from Q4] |
| Consumer advertising permitted? | [Yes / No / Restricted] |
| Regulatory framework | [EU MDR / Health Claims Regulation / Cosmetics Regulation / UCPD] |
| Legal advice obtained? | [from Q6] |

### 🔴 Critical — unlawful claim, enforcement and fine risk
| Issue | Legal basis | EU-wide or national? | File:Line | Current text | Recommended fix |
|-------|-------------|----------------------|-----------|--------------|-----------------|
| ... | ... | ... | ... | ... | ... |

### 🟠 Major — legally risky, fix before publication
| Issue | Legal basis | EU-wide or national? | File:Line | Current text | Recommended fix |
|-------|-------------|----------------------|-----------|--------------|-----------------|
| ... | ... | ... | ... | ... | ... |

### 🟡 Minor — borderline, tighten the wording
| Issue | Legal basis | EU-wide or national? | File:Line | Current text | Recommended fix |
|-------|-------------|----------------------|-----------|--------------|-----------------|
| ... | ... | ... | ... | ... | ... |

### 📋 Manual review required
- [ ] Confirm product classification with regulatory affairs
- [ ] Check health claims against the EFSA list (if a supplement)
- [ ] Review intended purpose / IFU (if a medical device)
- [ ] Check testimonials for recovery narratives
- [ ] Review imagery for before/after compliance
- [ ] Verify national advertising requirements for each market in Q0
- [ ] [further items]

### ✅ Compliant
- [list what is already legally sound]
```

Ask the user: **"Shall I fix the copy issues? (Product classification and evidence claims need
manual regulatory review.)"**

---

## Step 4: Fix issues

Apply fixes directly in the codebase. For each fix:
- Show before → after for every changed text
- Reference the specific legal basis (article, regulation or national act)
- Only technical text changes — no regulatory assessment
- Add mandatory notices where required
- Always choose the safer wording (when in doubt, soften)

**What this skill CAN fix:**
- Replace prohibited wording ("cures" → "may support")
- Add mandatory notices (instructions-for-use notice, doctor notice)
- Soften exaggerated claims
- Defuse testimonials
- Add disclaimer text
- Rewrite grey-zone wording into safe wording

**What this skill CANNOT fix (flag for regulatory or legal review):**
- Product classification (medical device: yes or no?)
- Evidence assessment (is the claim supported by studies?)
- CE marking and conformity assessment
- Drawing the line between medical device and medicinal product
- Detailed compliance of professional advertising
- The exact national wording of mandatory particulars per market

---

## Step 5: Summary

```
Health Claims Audit complete

Product category: [category]
Markets: [countries]
Regulatory framework: [instruments]

✅ [N] claims fixed
📋 [N] claims flagged for regulatory review
⚠️ [N] mandatory notices added

Highest risks:
1. [claim] — [legal basis, risk]
2. [claim] — [legal basis, risk]
3. [claim] — [legal basis, risk]

Recommended next steps:
- Have regulatory affairs or legal review all 🔴 claims
- Formally confirm the product classification
- Reconcile health claims against the EFSA list / the IFU
- Review imagery (before/after, disease imagery)
- Legal review of testimonials
- Verify national advertising requirements in each target market
- Schedule an annual compliance review
```

---

## Rules

- **Audit health-related advertising claims**, not general copy quality or UX
- **When in doubt, be more restrictive** — a softened statement beats an enforcement notice
- Reference the specific legal instrument (Art. 7 EU MDR, Art. 12 Regulation 1924/2006, Art. 88
  Directive 2001/83/EC) for every finding
- **State whether a finding is EU-wide or national.** Regulations bind everywhere; directive-based
  rules must be verified against national implementation
- **Product classification is the most important first step** — everything else depends on it
- Clearly separate what you CAN fix (wording) from what needs REGULATORY review (classification,
  evidence)
- Never draft claims that go beyond the product's intended purpose / IFU
- **No healing claims** — not even subtle or implicit ones
- Legal text: formal register, clear and unambiguous
- Follow the project's existing code style and component patterns
- This is NOT legal advice — always recommend professional regulatory review
- **Precautionary principle:** if it is unclear whether a claim is permitted, flag it as 🟠 Major
