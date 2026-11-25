---
name: legal-audit
description: Audit website legal compliance for the EU — GDPR, e-commerce information duties, consumer rights, ePrivacy, cookie consent, legal notice, third-country transfers, accessibility
model: opus
effort: high
---

# Legal Audit — EU Website Compliance

This skill audits a website for legal compliance under EU law. It checks mandatory pages, GDPR
implementation, cookie consent, form handling, third-party data transfers, and security headers.
It identifies violations and fixes them directly in the codebase.

No arguments needed. Just run `/legal-audit` and the skill scans the project automatically.

**Difference from other audits:**
- `/security-audit` checks **code-level security** — secrets, XSS, RLS, input validation
- `/accessibility-audit` checks **WCAG accessibility** — contrast, keyboard nav, ARIA, semantics
- `/legal-audit` checks **legal compliance** — GDPR, legal notice, cookie consent, data processing

**Important:** this skill provides technical compliance checks, not legal advice. Recommend
professional legal review for final sign-off.

## Regulatory scope — what applies EU-wide and what does not

Establish this before auditing, because it drives every severity rating:

**Directly applicable EU-wide (regulations):**
- GDPR — Regulation (EU) 2016/679
- Online dispute resolution — Regulation (EU) 524/2013
- Brussels I recast — Regulation (EU) 1215/2012 (consumer jurisdiction)

**Harmonised by directive, implemented differently per country:**
- E-commerce information duties — Directive 2000/31/EC, Art. 5 and Art. 10
- Consumer rights and the 14-day withdrawal right — Directive 2011/83/EU
- Cookie consent — ePrivacy Directive 2002/58/EC, Art. 5(3)
- Price indication — Directive 98/6/EC
- Unfair commercial practices — Directive 2005/29/EC
- Accessibility — European Accessibility Act, Directive (EU) 2019/882 (applicable since
  28 June 2025 for new products and services)

**National on top of all of this:** each member state has its own data protection act
supplementing the GDPR, its own implementation of the above directives, and sometimes additional
duties (media law disclosures, chamber membership, professional-body information).

Ask the user which country the business is established in and which countries it sells into, and
record them as `country` and `markets`. Where the two differ, consumer-facing duties generally
follow the consumer's country.

---

## Step 0: Understand the project

Before auditing, read:
- `CLAUDE.md` / `README.md` for project context
- All legal pages (legal notice, privacy policy, terms, withdrawal information)
- Cookie consent implementation
- All forms and data collection points
- Third-party scripts and services (analytics, fonts, CDNs, APIs)
- Hosting configuration and server location
- Security headers and SSL setup

Identify:
- **Country of establishment and target markets** — drives which national rules apply
- **Business type** — B2C, B2B or mixed? (affects consumer rights obligations)
- **Data flows** — where does user data go? which third parties?
- **Consent mechanism** — how are cookies and tracking handled?
- **Legal entity** — sole trader, limited company, etc.? (affects legal notice requirements)

---

## Step 1: Audit across 8 categories

Go through **each category** below. For every issue found, note the file, the legal requirement,
and the recommended fix. Rate severity as:
- **🔴 Critical** — legal violation, risk of enforcement action or a GDPR fine
- **🟠 Major** — incomplete compliance, should fix before launch
- **🟡 Minor** — best practice, recommended but not strictly required

Also record for each finding whether it rests on a **regulation** (firm EU-wide) or on a
**directive** (verify against national implementation).

---

### Category 1: Mandatory pages

#### Legal notice / imprint — Art. 5 Directive 2000/31/EC
> Every commercial website must make provider information easily, directly and permanently
> accessible. The directive sets the minimum; several member states require more.

**Check for:**
- A legal notice page exists and is linked from every page (typically the footer)
- Contains all required fields:
  - Company name / full name of the owner
  - Legal form
  - Company register number and registry court (if applicable)
  - VAT identification number
  - Registered office / business address (full postal address)
  - Contact: email (required), phone (recommended)
  - Chamber or professional body membership (if applicable)
  - Supervisory authority (if a regulated profession)
  - Applicable professional rules (if a regulated profession)
- The link uses the term recognised in the target market (for example "Legal notice",
  "Imprint", or the local statutory term)
- Reachable within two clicks from any page
- Not behind a login or paywall

**National check:** the exact field list and the required link label vary. Verify for `country`.

**Fix pattern:** create or update the legal notice page with all required fields. Add a footer
link on all pages. Use the locally recognised label.

---

#### Privacy policy — Art. 13/14 GDPR
> A complete privacy policy must be accessible from every page and before every form. This is a
> regulation, so the requirements are identical EU-wide.

**Check for:**
- A privacy policy page exists
- Linked from the footer on every page
- Linked before or near every form that collects personal data
- Contains all required sections:
  - Controller (name, address, contact)
  - Data protection officer (if applicable)
  - Purposes and legal bases of processing (per data type)
  - Recipients / categories of recipients
  - Third-country transfers (especially the USA — adequacy decision, SCCs, etc.)
  - Retention periods (specific, not "as long as necessary")
  - Data subject rights (access, rectification, erasure, restriction, objection, portability)
  - Right to lodge a complaint with the competent supervisory authority
  - Cookies and trackers listed individually (name, purpose, retention, provider)
  - Whether providing the data is a statutory or contractual requirement

**Fix pattern:** create a comprehensive privacy policy covering every processing activity. List
every cookie and tracker individually. Link from the footer and near every form.

---

#### Terms and conditions
> Required in practice for e-commerce and paid services. Must be accessible before purchase.

**Check for:**
- A terms page exists (if selling products or services)
- Accessible before checkout
- Contains:
  - Scope
  - Formation of the contract (when exactly is it concluded?)
  - Prices including VAT plus all additional costs
  - Payment terms and accepted payment methods
  - Delivery terms and delivery periods
  - Liability and warranty
  - Dispute resolution (ODR platform link for B2C:
    https://ec.europa.eu/consumers/odr)
- Checkbox or explicit acceptance before purchase (not just "by using this site...")

**Fix pattern:** create terms with all required sections. Add an acceptance mechanism before
purchase. Include the ODR link.

---

#### Right of withdrawal — Directive 2011/83/EU (B2C only)
> Consumers have a 14-day right of withdrawal for distance contracts. The 14 days are harmonised
> EU-wide; the information format and some exceptions are implemented nationally.

**Check for:**
- Withdrawal information exists (if B2C with paid services)
- The 14-day withdrawal right is clearly stated
- The model withdrawal form is provided (Annex I(B) of Directive 2011/83/EU)
- A contact address for withdrawal is clearly stated
- Exceptions to the withdrawal right are listed (Art. 16 of the directive, if applicable —
  including the digital content exception, which requires prior express consent and an
  acknowledgement of losing the right)
- The information is provided BEFORE the contract is concluded

**Fix pattern:** add withdrawal information with the model form. State the 14-day period,
exceptions and return address clearly.

---

### Category 2: Cookie consent and ePrivacy

#### Cookie banner — Art. 5(3) ePrivacy Directive plus GDPR consent standard
> Non-essential cookies require informed, freely given, specific opt-in consent. The consent
> standard comes from the GDPR (firm EU-wide); the cookie rule itself comes from a directive, and
> national authorities differ in how strictly they read it.

**Check for:**
- A cookie consent banner exists
- Opt-in required for non-essential cookies (not pre-checked)
- Granular categories (essential / statistics / marketing — separately toggleable)
- The reject button is as prominent as the accept button (no dark patterns)
- No tracking scripts fire before consent is given
- Consent is stored and respected across sessions
- A re-consent mechanism is available (cookie settings link in the footer)
- The banner does not block content entirely (still usable while deciding)

**Fix pattern:** implement a consent-first approach. Block all non-essential scripts until
explicit opt-in. Equal prominence for accept and reject. Add a footer link to change settings.

---

#### Third-party script blocking
> No third-party tracking or analytics scripts may load before user consent.

**Check for in code:**
- Google Analytics / GA4 — loads before consent?
- Google Tag Manager — fires tags before consent?
- Google Fonts — loaded from Google servers? (transfer to the USA)
- Meta Pixel / Facebook SDK — loads before consent?
- PostHog / Hotjar / Mixpanel — loads before consent?
- YouTube / Vimeo embeds — load before consent? (use a facade / click-to-load)
- Social media embeds (X, Instagram) — load before consent?
- CDN-hosted libraries from US providers — necessary or self-hostable?

**Fix pattern:** wrap all non-essential scripts in consent checks. Use GTM Consent Mode v2 or
manual consent gating. Self-host Google Fonts. Use video facades (click to load).

---

#### Cookie documentation
> Every cookie must be documented in the privacy policy.

**Check for:**
- Each cookie listed by name in the privacy policy
- For each cookie: name, purpose, provider, retention, type (essential/statistics/marketing)
- The cookies actually set match what is documented (no undocumented cookies)
- Third-party cookies from embedded content are documented

**Fix pattern:** audit the cookies actually set (DevTools → Application → Cookies). Document each
one. Remove undocumented cookies or add documentation.

---

### Category 3: Forms and data processing

#### Legal basis per form — Art. 6 GDPR
> Every form that collects personal data needs a clear legal basis. Firm EU-wide.

**Check for each form:**
- **Contact form:** legitimate interest (Art. 6(1)(f)) — no checkbox needed, but a privacy link
  is required
- **Newsletter signup:** consent (Art. 6(1)(a)) — explicit checkbox required plus double opt-in
- **Account creation:** performance of a contract (Art. 6(1)(b)) — privacy link required
- **Survey:** consent (Art. 6(1)(a)) — checkbox or clear information before submission
- A privacy policy link is visible near every form
- No pre-checked consent boxes
- Consent text is specific (not bundled with other agreements)

**Fix pattern:** add the appropriate consent mechanism per form type. Link to the privacy policy
near every form. Newsletter means double opt-in.

---

#### Newsletter — double opt-in
> Double opt-in is the accepted way to evidence consent. Note that it is best practice and the
> supervisory-authority expectation in most member states rather than a single harmonised EU
> rule — but the burden of proving consent (Art. 7(1) GDPR) is EU-wide.

**Check for:**
- A double opt-in flow is implemented (submit email → confirmation email → click link →
  subscribed)
- A confirmation email is sent (not just "thanks, you're subscribed")
- An unsubscribe link in every newsletter email
- The signup form has an explicit consent checkbox
- The consent text references the privacy policy
- The subscriber list contains only confirmed opt-ins

**Fix pattern:** implement the full double opt-in flow. Add an unsubscribe link to all emails.
Store the opt-in timestamp as proof of consent.

---

#### Data minimisation — Art. 5(1)(c) GDPR
> Collect only data that is strictly necessary for the stated purpose.

**Check for:**
- Forms collecting more data than needed (e.g. a phone number for a newsletter)
- Required fields that should be optional
- Fields without a clear purpose (why do you need this?)
- Collecting personal data "just in case" or "for future use"

**Fix pattern:** mark non-essential fields as optional. Remove fields without a clear purpose.
Only require what is needed for the stated purpose.

---

### Category 4: Third-country transfers

#### US services — Schrems II and the EU-US Data Privacy Framework
> Transferring personal data to the USA requires specific safeguards. Firm EU-wide (Chapter V
> GDPR).

**Check for:**
- Google Analytics → US transfer (self-host or use Matomo?)
- Google Fonts → US transfer (self-host)
- Google Tag Manager → US transfer (consent-gated?)
- Cloudflare → check EU-only settings
- Supabase → server location? (EU region available)
- Vercel / Netlify → server location?
- Mailchimp / SendGrid → DPA and SCCs in place?
- Any other US-based SaaS receiving personal data

**For each US service, verify:**
- EU-US Data Privacy Framework (DPF) certification of the provider
- OR: standard contractual clauses (SCCs) plus a transfer impact assessment (TIA)
- Documented in the privacy policy with the specific legal basis for the transfer
- Consent obtained before the transfer (if consent-based)

**Fix pattern:** self-host where possible (fonts, analytics). Use EU-hosted alternatives. For
necessary US services: verify DPF certification or implement SCCs. Document all transfers in the
privacy policy.

---

#### Data processing agreements — Art. 28 GDPR
> A data processing agreement must exist with every processor handling personal data. Firm
> EU-wide.

**Check for DPAs with:**
- Hosting provider (Hetzner, AWS, Vercel, Netlify, etc.)
- Analytics provider (Google, PostHog, Matomo Cloud, etc.)
- Newsletter / email provider (Mailchimp, SendGrid, Brevo, etc.)
- Database provider (Supabase, PlanetScale, etc.)
- CDN provider (Cloudflare, Fastly, etc.)
- Payment processor (Stripe, Mollie, etc.)
- Any SaaS that processes user data on your behalf

**Fix pattern:** list all processors. Verify a DPA exists for each. Most large providers offer
standard DPAs — link to them in the privacy policy. Keep signed copies on file.

---

### Category 5: HTTPS and security headers

#### SSL/TLS — Art. 32 GDPR
> Encryption in transit is a mandatory technical measure.

**Check for:**
- HTTPS active on all pages (no mixed content)
- HTTP → HTTPS redirect (301 permanent)
- Valid SSL certificate (not expired, correct domain)
- HSTS header set (`Strict-Transport-Security: max-age=31536000; includeSubDomains`)

**Fix pattern:** enable HTTPS everywhere. Set up the 301 redirect. Add the HSTS header. Most
hosts (Vercel, Netlify, Cloudflare) handle this automatically — verify it is active.

---

#### Security headers
> Required and recommended headers for data protection compliance.

**Check for:**
- `Content-Security-Policy` — restricts script and resource sources
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY` or `SAMEORIGIN`
- `Referrer-Policy: strict-origin-when-cross-origin` (or stricter)
- `Permissions-Policy` — restricts browser features (camera, microphone, geolocation)

**Note:** for detailed security implementation, run `/security-audit`.

**Fix pattern:** add security headers via hosting config, a `_headers` file, or middleware. The
CSP should allow only necessary sources.

---

### Category 6: Records and documentation

#### Records of processing activities — Art. 30 GDPR
> A record of processing activities must be maintained (not on the website, but it should be
> informed by what the website does). Firm EU-wide.

**Check that the website's data processing is documentable:**
- All forms and their data fields are identifiable
- All third-party services and their data flows are traceable
- The cookie inventory matches the cookies actually set
- Retention periods are defined per data type
- Purpose limitation is clear for each processing activity

**Flag for manual review:**
- "Do you maintain records of processing activities covering this website?"
- "Are deletion periods documented and implemented?"

---

#### Deletion concept
> Personal data must be deleted when no longer needed.

**Check for:**
- Defined retention periods in the privacy policy
- Server logs: max 7-14 days recommended
- Contact form data: max 6 months after the enquiry is resolved
- Newsletter: immediate deletion on unsubscribe
- Analytics data: anonymised or deleted after 14-26 months
- Account data: deleted on account deletion request
- No "we keep everything forever" statements

**Fix pattern:** define specific retention periods per data type in the privacy policy. Implement
automated deletion where possible.

---

### Category 7: E-commerce specifics (if applicable)

#### Price indication — Directive 98/6/EC and Art. 5 Directive 2000/31/EC
> Prices must be transparent and complete.

**Check for:**
- All prices include VAT
- "incl. VAT" or "incl. XX% VAT" clearly stated
- Shipping costs stated before checkout (or "plus shipping: X")
- No hidden costs that appear only at checkout
- The total price is visible before purchase confirmation

**National check:** VAT rates and the exact required wording differ per country; for cross-border
B2C sales, VAT follows the consumer's country under the OSS scheme.

**Fix pattern:** show prices with an explicit VAT statement. Add shipping information upfront. No
surprise costs at checkout.

---

#### Ordering process — Art. 10/11 Directive 2000/31/EC and Art. 8 Directive 2011/83/EU
> The ordering process must meet specific information requirements.

**Check for:**
- The technical steps to concluding the contract are explained
- Order correction is possible before final submission
- The order button carries clear wording indicating a payment obligation (Art. 8(2) of
  Directive 2011/83/EU requires the equivalent of "order with obligation to pay") — not just
  "continue"
- An order confirmation is sent by email
- Terms and withdrawal information are accessible before purchase

**Fix pattern:** use an explicit payment-obligation button label. Implement an order summary with
a correction option. Send a confirmation email.

---

#### Dispute resolution — Regulation (EU) 524/2013
> B2C websites must link to the EU online dispute resolution platform.

**Check for:**
- A link to https://ec.europa.eu/consumers/odr is present (in the terms or the legal notice)
- A statement about willingness or unwillingness to participate in alternative dispute
  resolution

**Fix pattern:** add the ODR link and the statement to the terms or legal notice.

---

### Category 8: Accessibility — European Accessibility Act

#### Legal accessibility requirements
> Directive (EU) 2019/882 (the European Accessibility Act) has applied since 28 June 2025 for new
> products and services. It is a directive, so scope, exemptions (notably for microenterprises)
> and enforcement differ per member state.

**Check for:**
- Awareness: is the team aware of the accessibility obligations and the deadline?
- Whether the business falls within scope (sector, and whether a microenterprise exemption
  applies in `country`)
- An accessibility statement — required for the public sector under Directive (EU) 2016/2102,
  recommended for private-sector services in scope
- Basic compliance indicators (contrast, alt texts, keyboard navigation, semantic HTML)

**Note:** for full WCAG 2.2 Level AA compliance, run `/accessibility-audit`. This category only
flags the legal requirement.

**Fix pattern:** add an accessibility statement if required. Run `/accessibility-audit` for the
comprehensive technical check. Plan the compliance timeline.

---

## Step 2: Report findings

Present findings grouped by severity:

```
## Legal Audit Results — [country / markets]

### 🔴 Critical — legal violation, enforcement or fine risk
| Issue | Legal basis | EU-wide or national? | File / location | Required fix |
|-------|-------------|----------------------|-----------------|--------------|
| ... | ... | ... | ... | ... |

### 🟠 Major — incomplete compliance
| Issue | Legal basis | EU-wide or national? | File / location | Required fix |
|-------|-------------|----------------------|-----------------|--------------|
| ... | ... | ... | ... | ... |

### 🟡 Minor — best practice, recommended
| Issue | Legal basis | EU-wide or national? | File / location | Required fix |
|-------|-------------|----------------------|-----------------|--------------|
| ... | ... | ... | ... | ... |

### 📋 Manual review required
- [ ] DPA with [provider] — verify a signed agreement exists
- [ ] Records of processing — verify they cover this website
- [ ] Deletion concept — verify automated deletion is implemented
- [ ] National requirements for [country] — legal notice fields, order button wording,
      accessibility scope
- [ ] [other items requiring offline verification]

### ✅ Compliant
- [list what is already legally sound]
```

Ask the user: **"Shall I fix the technical issues? (The content of mandatory pages and the DPAs
need manual legal review.)"**

---

## Step 3: Fix issues

Apply fixes directly in the codebase. For each fix:
- Reference the specific legal basis
- Only fix the technical implementation — never draft legal text without flagging it for lawyer
  review
- Prioritise: (1) consent blocking, (2) missing page links, (3) form compliance, (4) security
  headers
- Never break existing functionality
- Follow the project's existing code style and design system

**What this skill CAN fix technically:**
- Cookie consent implementation (blocking scripts before consent)
- Missing footer links (legal notice, privacy policy, terms)
- Privacy links near forms
- HTTPS redirects and security headers
- Self-hosting Google Fonts
- Newsletter double opt-in flow
- Consent checkboxes on forms
- Script loading order (consent-gated)

**What this skill CANNOT fix (flag for manual or legal review):**
- Legal page content (legal notice details, privacy policy text, contract clauses)
- Data processing agreements with third parties
- Creating records of processing activities
- Tax and pricing compliance
- Withdrawal information text
- The exact national requirements per market

---

## Step 4: Summary

```
Legal Audit complete — [country / markets]

✅ [N] technical issues fixed
📋 [N] items flagged for manual or legal review
⚠️ [N] items need lawyer sign-off

Legal bases checked:
- GDPR (Art. 5, 6, 7, 12-14, 28, 30, 32) — EU-wide
- Directive 2000/31/EC (provider information, ordering process) — national implementation
- Directive 2011/83/EU (withdrawal right, order button) — national implementation
- ePrivacy Directive 2002/58/EC (cookies) — national implementation
- Regulation (EU) 524/2013 (ODR link) — EU-wide
- Directive (EU) 2019/882 (accessibility) — national implementation

Top 3 highest-priority fixes:
1. [fix] — [legal basis, risk level]
2. [fix] — [legal basis, risk level]
3. [fix] — [legal basis, risk level]

Recommended next steps:
- Have a lawyer review the legal notice, privacy policy and terms
- Verify DPAs exist with all data processors
- Create or update the records of processing activities
- Confirm the national requirements for each target market
- Test the cookie consent flow end to end (DevTools → verify no pre-consent cookies)
- Run `/accessibility-audit` for full WCAG compliance
- Run `/security-audit` for code-level security
- Schedule an annual legal compliance review
```

---

## Rules

- **Audit legal compliance**, not code quality, UX or visual design
- **EU law baseline** — reference GDPR, the e-commerce, consumer rights, ePrivacy, price
  indication and accessibility instruments. Never present one member state's national statute as
  if it applied EU-wide
- **State whether each finding is EU-wide or national.** Regulations bind everywhere;
  directive-based rules must be verified against national implementation in `country`
- **Never draft legal text** — flag content for lawyer review, only fix the technical
  implementation
- Reference the specific article for every finding
- Clearly separate what you CAN fix (technical) from what needs MANUAL review (legal content)
- Do not duplicate `/accessibility-audit` — reference it for WCAG, only flag the legal
  requirement here
- Do not duplicate `/security-audit` — reference it for code security, only check legally
  required headers here
- Err on the side of caution — if unsure whether something is required, flag it as 🟠 Major
- **Never recommend removing legally required elements** for aesthetic or UX reasons
- Follow the project's existing code style and component patterns
