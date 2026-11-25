---
name: legal-model-decoder
description: Use when you need to figure out how a competitor or your own venture in a REGULATED market (health/telemedicine, legal, financial, insurance) is legally structured — who contracts, who bills, who is liable — or when asking "is this allowed / how do they get away with this / what's the grey zone / how can we do X compliantly". Particularly useful for health ventures, where professional-conduct law and VAT treatment interact.
model: opus
effort: high
---

# Legal Model Decoder

## Core principle

**The grey zone is never in the marketing — it lives in the legal artifacts.** Do not ask "is this
allowed?" from first principles. **Reverse-engineer the real construction from primary artifacts**
(terms and conditions, legal notice, trade register, and above all the invoice). One invoice
reveals more than ten marketing pages.

This finds the grey zone *fast*, so you walk into the lawyer meeting already knowing the
construction. It does **not** replace legal advice — it makes you lawyer-ready.

## Jurisdiction note

The method below is jurisdiction-independent, and one of its sharpest tells — the VAT treatment of
medical care — is harmonised EU-wide by the VAT Directive 2006/112/EC. Everything else
(professional-conduct law, trade licensing, fee-splitting bans, the name and contents of the
business register) is **national**. Establish which country the entity operates from before you
start, and look up the local equivalent of each artifact and each rule.

## When to use

- "How does competitor X make money / how is X structured / how do they get away with this?"
- "Is our planned model allowed? Where is the grey zone?"
- "How can we do [uniform pricing / revenue share / bundling] compliantly?"
- Any regulated-market business model design (health, telemedicine, legal, fintech, insurance).

**Not for:** pure product or UX questions, or unregulated B2C SaaS with no professional-conduct
law.

## The 3-axis decomposition (always run all three, SEPARATELY)

The construction hides in where these three come *apart*:

1. **Who is the contract partner?** — who legally closes the core regulated contract (e.g. the
   treatment contract)? The platform or the professional?
2. **Who bills, and where does the money flow?** — follow the money *independently* of axis 1. Who
   issues the invoice, and who keeps what.
3. **Who is liable?** — who carries the professional and legal risk.

**When these split apart (e.g. the platform sells and bills, but the professional contracts and is
liable) → that split IS the construction.** That is the grey zone.

## Artifacts to pull — in priority order

| Priority | Artifact | Why |
|---|---|---|
| 1 | **The invoice** | The hardest proof. Shows who sells, what the line item is, and the **tax rate** (the killer tell). |
| 2 | **Terms and conditions** | "The contract is concluded with…", liability clauses, "we are not a provider" |
| 3 | **Legal notice plus the trade and commercial register** (the national equivalents; Northdata and similar aggregators help) | Entity, jurisdiction, the registered scope of the trade licence |
| 4 | Pricing funnel and FAQ | What is stated as included versus not included (what is fiscally split out) |

## The tell dictionary — signals that expose the true structure

| Signal | What it reveals |
|---|---|
| **The VAT rate on the invoice** | Medical care is **VAT-exempt across the EU** (Art. 132(1)(b) and (c), VAT Directive 2006/112/EC). Charging the standard VAT rate means the service is deliberately sold as a *non-medical, commercial* service (support, subscription, platform access). The single sharpest tell. |
| **Whoever issues the invoice is not whoever performs the service** | A principal/seller split — the platform sells, the professional performs |
| **The wording of the trade licence** in the business register | Phrasing that explicitly excludes acting in one's own name and on one's own account signals a deliberately pure intermediary role |
| **"The contract is concluded with [the professional]"** in the terms | Who the *legal* service provider is (not necessarily who you pay) |
| **Entity form and country in the legal notice** | Cross-border arbitrage (an entity in one member state serving another to sidestep local professional law) |
| **What is bundled versus excluded** (medication is almost always excluded) | Shows which layer is kept fiscally and legally separate |
| **Whether the fee is fixed, per consultation, or a percentage of the professional's fee** | A fixed platform fee is safer; a percentage of the regulated fee or a per-referral payment is the forbidden zone in most jurisdictions — many member states prohibit fee-splitting or commission on medical fees. Look up the national rule. |

## Workflow

1. Name the entity, its jurisdiction and the market it serves (legal notice, register).
2. Pull the artifacts above. **Get an invoice if at all possible** — ask the user, or sign up for a
   test.
3. Run the 3-axis decomposition; note where the axes split.
4. Read the tells — especially the **VAT rate**.
5. Locate the grey zone: the exact clause or mechanism that makes it work, and the law it balances
   against. Name whether that law is EU-level or national.
6. Produce the output below and hand it to a lawyer.

To go fast, fan out: dispatch parallel subagents to read the terms, the legal notice and register,
the invoice and the pricing simultaneously, then synthesise.

Run these subagents on `sonnet` / low (pass `model` and `effort` explicitly); keep the synthesis in the main session.

## Output format

- **Verdict:** pure intermediary | principal seller | hybrid | cross-border arbitrage
- **The construction in one line** (how the three axes split)
- **The load-bearing tell** (usually the VAT treatment or the contract clause in the terms)
- **The law it balances against** — and whether that law is EU-level or national
- **Open questions for the lawyer** (what is untested or fragile)

## Common mistakes

- **Reading the marketing, not the invoice.** Marketing says "consultation included"; the invoice
  may show only a taxable subscription — meaning the medical act is a separate legal layer.
- **Merging money and liability.** They are different axes. Ask about them separately.
- **Concluding "compliant" instead of "here is the construction, and here is what a lawyer must
  confirm".** Never certify legality.
- **Ignoring the tax line.** VAT status often settles "is this legally a medical service or not"
  instantly.
- **Assuming one country's rule applies everywhere.** The VAT exemption is EU-wide; the
  professional-conduct rules around it are not.

## Worked example (compressed)

*Provider X, a telemedicine platform selling a GLP-1 programme:* the marketing bundles the doctor's
consultation into a fixed monthly price, so it looks as though Provider X sells the medicine.
**Invoice tell:** a single line item, "Provider X subscription", plus the standard VAT rate. Since
medical care is VAT-exempt across the EU, charging standard-rate VAT proves that Provider X is
selling a *taxable non-medical support subscription*, not the medical act itself.

**Construction:** the platform, registered as an intermediary, sells its own taxable support
subscription (axis 2 plus its own contract), while the doctor keeps the VAT-exempt treatment
contract and the liability (axes 1 and 3). That split is how a pure intermediary can advertise an
all-in fixed price.

**Grey zone for the lawyer:** does the platform's margin risk being treated as a cut of the medical
fee under the national fee-splitting rules? How exactly is the doctor paid — fixed fee, or per
patient?
