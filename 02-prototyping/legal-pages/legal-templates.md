# Legal Templates — EU Legal Page Text Blocks

Reference file for the `legal-pages` skill. Contains GDPR-compliant text blocks and page
section templates for legal pages of EU-based websites.

**Company:** {{companyLegalName}}
**Applicable law:** GDPR (Regulation 2016/679), ePrivacy Directive 2002/58/EC, E-Commerce
Directive 2000/31/EC, Consumer Rights Directive 2011/83/EU — plus the national laws
implementing those directives in {{country}}.

> **Important — regulations vs. directives.** GDPR is a *regulation*: it applies directly and
> identically across the EU, so the article references below are accurate everywhere. The
> e-commerce, consumer rights and ePrivacy rules are *directives*: each member state implements
> them in its own national law, with different names, thresholds and sometimes stricter
> requirements. Wherever a template cites a directive, replace it with the corresponding national
> act before publishing, and have the result checked by a lawyer in your jurisdiction. These
> templates are a starting point, not legal advice.

**Placeholders used throughout:**

| Placeholder | Description | Example |
|---|---|---|
| `{{brandName}}` | Product/brand name | ExampleBrand, ExampleApp |
| `{{contactEmail}}` | Project contact email | hello@example.com |
| `{{websiteUrl}}` | Full website URL | https://example.com |
| `{{currentDate}}` | Date of page generation | 2026-03-03 |
| `{{country}}` | Country of establishment | Ireland, Germany, Spain |
| `{{supervisoryAuthority}}` | National data protection authority (name, address, contact) | see Section 1.12 |
| `{{governingLaw}}` | Governing law of the contract | the laws of Ireland |
| `{{jurisdiction}}` | Competent court | the courts of Dublin |

---

## 1. Privacy Policy — Section Templates

### 1.1 Controller

```text
The controller responsible for data processing on {{websiteUrl}} is:

{{companyLegalName}}
{{companyAddress}}
Company register number: {{companyRegisterNr}}
VAT identification number: {{vatId}}
Registry court: {{commercialCourt}}
Managing director: {{managingDirector}}
Email: {{contactEmail}}

For any questions about data protection, you can reach us at any time at {{contactEmail}}.
```

### 1.2 Overview of processing activities

```text
We process personal data only to the extent necessary to provide a functional website together
with our content and services. Personal data is generally processed only with the consent of the
data subject. An exception applies where obtaining prior consent is not possible for practical
reasons and the processing is permitted by law.

The following categories of data are processed:
- Master data (e.g. name, email address)
- Usage data (e.g. pages visited, time on site, access times)
- Technical data (e.g. IP address, browser type, operating system)
- Communication data (e.g. email address when contacting us or subscribing to a newsletter)

Processing takes place for the following purposes:
- Providing and operating the website {{websiteUrl}}
- Responding to enquiries
- Analysing and improving our offering
- Sending information and newsletters (where consent has been given)
- Processing payments (where applicable)
- Meeting legal obligations
```

### 1.3 Legal bases

```text
Your personal data is processed on the following legal bases under the GDPR:

- Consent (Art. 6(1)(a) GDPR): you have given consent to the processing of your personal data
  for one or more specific purposes. This applies in particular to non-essential cookies,
  newsletter distribution and optional analytics services.

- Performance of a contract (Art. 6(1)(b) GDPR): processing is necessary for the performance of
  a contract to which you are party, or to take steps at your request prior to entering into a
  contract. This applies in particular to the use of our services, registering a user account
  and processing payments.

- Legal obligation (Art. 6(1)(c) GDPR): processing is necessary for compliance with a legal
  obligation to which we are subject. This applies in particular to tax and commercial record
  retention obligations.

- Legitimate interests (Art. 6(1)(f) GDPR): processing is necessary for the purposes of the
  legitimate interests pursued by us or by a third party, except where your interests or
  fundamental rights and freedoms override those interests. This applies in particular to
  analysing website usage in order to improve our offering, protecting against misuse, and
  technical security measures.
```

### 1.4 Security measures

```text
In accordance with Art. 32 GDPR, and taking into account the state of the art, the costs of
implementation and the nature, scope, context and purposes of processing as well as the varying
likelihood and severity of the risk to the rights and freedoms of natural persons, we implement
appropriate technical and organisational measures to ensure a level of security appropriate to
the risk.

These measures include in particular:
- Encryption of data transmission via SSL/TLS (HTTPS)
- Regular review and updating of security measures
- Restricting access to personal data to authorised persons
- Pseudonymisation and anonymisation of data where possible
- Regular backups
```

### 1.5 Transfers to third countries

```text
Where we process data in a third country (i.e. outside the European Union or the European
Economic Area), or where this occurs in the context of using third-party services or disclosing
or transferring data to other persons, bodies or companies, this is done only in accordance with
the applicable legal requirements.

Where the European Commission has adopted an adequacy decision (Art. 45 GDPR), transfers are
made on that basis. In the case of the United States we rely on the EU-US Data Privacy Framework
(DPF), provided the relevant recipient holds a valid DPF certification.

Otherwise, transfers are made on the basis of the European Commission's standard contractual
clauses (Art. 46(2)(c) GDPR) or on the basis of your explicit consent (Art. 49(1)(a) GDPR).
```

### 1.6 Cookies and tracking

```text
Our website uses cookies. Cookies are small text files stored on your device by your browser.
Most of the cookies we use are so-called session cookies, which are deleted automatically at the
end of your visit. Other cookies remain on your device until you delete them.

We distinguish between the following cookie categories:

- Essential cookies: these are required for the basic functions of the website and cannot be
  disabled. They are generally set only in response to actions you take, such as setting your
  privacy preferences or filling in forms.

- Statistics cookies: these allow us to analyse the use of the website and measure its
  performance. They help us understand which pages are most popular and how visitors move around
  the site. Legal basis: Art. 6(1)(a) GDPR (consent).

- Marketing cookies: these are used to make advertising more relevant to you. They serve to
  control the display of advertising and to measure the effectiveness of advertising campaigns.
  Legal basis: Art. 6(1)(a) GDPR (consent).

Non-essential cookies are stored only with your consent, in accordance with Art. 6(1)(a) GDPR in
conjunction with Art. 5(3) of the ePrivacy Directive 2002/58/EC as implemented in national law.
You can withdraw your consent at any time through our cookie settings.
```

### 1.7 Hosting — general template

```text
[HOSTING_PROVIDER_SECTION]
```

(See Section 2 for provider-specific texts: Vercel, Netlify, Cloudflare.)

### 1.8 Web analytics — general template

```text
[ANALYTICS_PROVIDER_SECTION]
```

(See Section 2 for provider-specific texts: Google Analytics, PostHog, Hotjar.)

### 1.9 Payment providers — general template

```text
[PAYMENT_PROVIDER_SECTION]
```

(See Section 2 for provider-specific text: Stripe.)

### 1.10 Email delivery — general template

```text
[EMAIL_PROVIDER_SECTION]
```

(See Section 2 for provider-specific text: Brevo.)

### 1.11 Data subject rights

```text
You have the following rights regarding your personal data:

Right of access (Art. 15 GDPR)
You have the right to obtain confirmation as to whether we process personal data concerning you.
Where that is the case, you have a right of access to that personal data and to the information
listed in Art. 15 GDPR.

Right to rectification (Art. 16 GDPR)
You have the right to obtain without undue delay the rectification of inaccurate personal data
and, where applicable, to have incomplete data completed.

Right to erasure (Art. 17 GDPR)
You have the right to obtain the erasure of your personal data without undue delay where one of
the grounds set out in Art. 17 GDPR applies, for example where the data is no longer necessary
for the purposes for which it was collected.

Right to restriction of processing (Art. 18 GDPR)
You have the right to obtain restriction of processing where one of the conditions in Art. 18
GDPR is met, for example where you contest the accuracy of the data.

Right to data portability (Art. 20 GDPR)
You have the right to receive the personal data concerning you which you have provided to us in
a structured, commonly used and machine-readable format. You also have the right to transmit
that data to another controller.

Right to object (Art. 21 GDPR)
You have the right to object at any time, on grounds relating to your particular situation, to
processing of your personal data based on Art. 6(1)(e) or (f) GDPR. We will then no longer
process the personal data unless we can demonstrate compelling legitimate grounds for the
processing.

Right to withdraw consent (Art. 7(3) GDPR)
You have the right to withdraw consent at any time. Withdrawal does not affect the lawfulness of
processing carried out on the basis of consent before its withdrawal.

To exercise your rights, you can contact us at any time: {{contactEmail}}
```

### 1.12 Right to lodge a complaint

```text
Under Art. 77 GDPR you have the right to lodge a complaint with a supervisory authority if you
consider that the processing of your personal data infringes the GDPR.

You may lodge a complaint with the supervisory authority of the member state of your habitual
residence, place of work, or the place of the alleged infringement. The authority competent for
us is:

{{supervisoryAuthority}}
```

> Fill `{{supervisoryAuthority}}` with the name, address, phone number, email and website of the
> national data protection authority where the controller is established. The European Data
> Protection Board maintains the current list of all national authorities:
> https://www.edpb.europa.eu/about-edpb/about-edpb/members_en

### 1.13 Health data (conditional: hasHealthData)

```text
In the course of our services, special categories of personal data within the meaning of
Art. 9(1) GDPR may be processed, in particular health data.

This data is processed exclusively on the basis of your explicit consent under Art. 9(2)(a)
GDPR. You may withdraw your consent at any time with effect for the future.

We apply specific safeguards to the processing of health data, including:
- Encrypted storage and transmission
- Strict access restrictions
- Pseudonymisation where possible
- Regular review of security measures

Your health data is processed solely to provide the {{brandName}} features you use and is not
used for advertising purposes.
```

> Note: several member states impose additional national requirements on health data under
> Art. 9(4) GDPR. Check the national rules in {{country}} before processing health data.

---

## 2. Tool-specific texts

Not included. For each third-party tool, fill the general templates in Sections 1.5 and 1.7 to
1.10 with the provider's legal entity, address, processing purpose and transfer mechanism, taken
from the provider's own privacy notice and data processing agreement. Verify every detail
before publishing.

---

## 3. Imprint / Legal Notice — Section Templates

> Art. 5 of the E-Commerce Directive 2000/31/EC requires information society service providers to
> make certain information easily, directly and permanently accessible. Each member state
> implements this in its own law, and several go beyond the directive's minimum (for example
> additional media-law disclosures for editorial content). Check the national requirements in
> {{country}} and add whatever it demands on top of the block below.

### 3.1 Provider information

```text
Provider information pursuant to Art. 5 of Directive 2000/31/EC on electronic commerce, as
implemented in {{country}}

{{brandName}} is a service provided by:

{{companyLegalName}}
{{companyStreet}}
{{companyZipCity}}

Company register number: {{companyRegisterNr}}
VAT identification number: {{vatId}}
Registry court: {{commercialCourt}}
Managing director: {{managingDirector}}

Business activity: digital services and software development
Supervisory authority / chamber membership (where applicable): {{supervisoryBody}}
```

### 3.2 Contact

```text
Contact

Email: {{contactEmail}}
Website: {{websiteUrl}}
```

### 3.3 Online dispute resolution

```text
Online dispute resolution

The European Commission provides a platform for online dispute resolution (ODR):
https://ec.europa.eu/consumers/odr

Our email address can be found above in this legal notice.

We are neither willing nor obliged to participate in dispute resolution proceedings before a
consumer arbitration board.
```

> Check the national rules in {{country}}: some member states require traders to state whether
> they participate in alternative dispute resolution, and a few make participation mandatory for
> certain sectors.

### 3.4 Liability for content

```text
Liability for content

The content of our pages has been created with the greatest care. However, we cannot guarantee
that it is accurate, complete or up to date.

As a service provider we are responsible for our own content on these pages under general law.
Under Articles 12 to 15 of Directive 2000/31/EC, as implemented in national law, we are not
obliged to monitor transmitted or stored third-party information, or to investigate
circumstances that indicate illegal activity.

Obligations to remove or block the use of information under general law remain unaffected.
Liability in this respect is, however, only possible from the point at which we become aware of
a specific infringement. If we become aware of such infringements, we will remove the content
concerned without delay.
```

### 3.5 Liability for links

```text
Liability for links

Our website contains links to external third-party websites over whose content we have no
control. We therefore cannot accept any liability for that third-party content. The respective
provider or operator of the linked pages is always responsible for their content.

The linked pages were checked for possible legal infringements at the time of linking. No
unlawful content was apparent at that time. However, permanent monitoring of the content of
linked pages is not reasonable without specific indications of an infringement. If we become
aware of any infringements, we will remove such links without delay.
```

---

## 4. Terms and Conditions — Section Templates

### 4.1 Scope

```text
Scope

These terms and conditions govern the use of the website {{websiteUrl}} and the associated
services of {{brandName}} (the "Service" or "Platform").

By using the Service you agree to these terms. If you do not agree with them, please do not use
the Service.

The version of these terms in force at the time of use applies.
```

### 4.2 Contracting party

```text
Contracting party

The contracting party for the use of {{brandName}} is:

{{companyLegalName}}
{{companyStreet}}
{{companyZipCity}}
Company register number: {{companyRegisterNr}}
VAT identification number: {{vatId}}
Email: {{contactEmail}}

(the "Provider", "we" or "us")
```

### 4.3 Subject matter

```text
Subject matter of the contract

The subject matter of the contract is the provision and use of the online service {{brandName}}
via the website {{websiteUrl}}.

The precise scope of services follows from the description of the Service on the website at the
time of registration or conclusion of the contract. We reserve the right to further develop,
improve and adapt the Service, provided this is reasonable for the user.
```

### 4.4 Registration and user account

```text
Registration and user account

Using certain features of {{brandName}} requires registration and the creation of a user
account.

The information provided on registration must be truthful and complete. Any changes to that
information must be updated without delay.

You are required to keep your access credentials confidential and to protect them against access
by third parties. If you become aware of any misuse of your account, you must inform us without
delay.

We reserve the right to suspend or delete user accounts in the event of breaches of these terms.
```

### 4.5 Prices and payment (conditional: hasPaidFeatures)

```text
Prices and payment

The prices currently applicable to paid features of {{brandName}} are shown on the website
{{websiteUrl}}. All prices stated include statutory VAT.

Payment is processed through the payment service provider Stripe. The following payment methods
are available:
- Credit card (Visa, Mastercard)
- Other payment methods available through Stripe

For subscriptions, payment is collected automatically on each due date. You may cancel your
subscription at any time with effect from the end of the current billing period.

In the event of late payment we are entitled to suspend access to paid features until the
outstanding payment has been received.
```

### 4.6 Right of withdrawal (conditional: hasPaidFeatures)

```text
Right of withdrawal

If you are a consumer, you have a statutory right of withdrawal under Directive 2011/83/EU on
consumer rights, as implemented in {{country}}.

Withdrawal instructions:

You have the right to withdraw from this contract within fourteen days without giving any
reason.

The withdrawal period expires fourteen days from the day of the conclusion of the contract.

To exercise the right of withdrawal, you must inform us

{{companyLegalName}}
{{companyAddress}}
Email: {{contactEmail}}

of your decision to withdraw from this contract by an unequivocal statement (for example a
letter sent by email).

To meet the withdrawal deadline, it is sufficient for you to send your communication concerning
your exercise of the right of withdrawal before the withdrawal period has expired.

Effects of withdrawal:

If you withdraw from this contract, we shall reimburse to you all payments received from you
without undue delay and in any event not later than fourteen days from the day on which we are
informed about your decision to withdraw. We will carry out such reimbursement using the same
means of payment as you used for the initial transaction, unless you have expressly agreed
otherwise.

Model withdrawal form:

(If you wish to withdraw from the contract, please complete and return this form.)

To:
{{companyLegalName}}
{{companyAddress}}
Email: {{contactEmail}}

I/we (*) hereby give notice that I/we (*) withdraw from my/our (*) contract for the provision of
the following service:

Ordered on (*) / received on (*):
Name of consumer(s):
Address of consumer(s):
Date:
Signature of consumer(s) (only if this form is notified on paper):

(*) Delete as appropriate
```

> Note: for digital content and services, Art. 16(m) of Directive 2011/83/EU allows the right of
> withdrawal to lapse where the consumer has given prior express consent to immediate performance
> and acknowledged the loss of the right. If you rely on this, add the corresponding consent step
> in the purchase flow and reflect it here.

### 4.7 Warranty and liability

```text
Warranty and liability

We endeavour to make the {{brandName}} Service available without errors or interruption. Given
the nature of software and the internet, however, we cannot guarantee uninterrupted
availability.

We are liable for damages only in cases of intent and gross negligence. In cases of slight
negligence we are liable only for breach of material contractual obligations, and in such cases
liability is limited to the foreseeable damage typical for this type of contract.

The above limitations of liability do not apply to damage arising from injury to life, body or
health, nor to liability under Directive 85/374/EEC on liability for defective products as
implemented in national law.

Towards business customers, warranty is limited to the statutory provisions applicable under
{{governingLaw}}.

{{brandName}} does not constitute medical, therapeutic, legal or financial advice. The content
provided serves general information purposes only.
```

> Note: limitations of liability towards consumers are restricted by national law, and several
> member states treat broad exclusions as unfair terms under Directive 93/13/EEC. Have this
> clause reviewed for {{country}}.

### 4.8 Data protection

```text
Data protection

Information on the processing of your personal data can be found in our privacy policy at
{{websiteUrl}}/privacy.
```

### 4.9 Final provisions

```text
Final provisions

These terms are governed by {{governingLaw}}, excluding the UN Convention on Contracts for the
International Sale of Goods and the conflict-of-law rules of private international law.

For disputes arising from this contractual relationship, {{jurisdiction}} shall have
jurisdiction to the extent permitted by law. Where the user is a consumer, the statutory rules on
jurisdiction apply and remain unaffected.

Should individual provisions of these terms be or become invalid, the validity of the remaining
provisions shall remain unaffected. The invalid provision shall be replaced by a valid provision
that comes closest to the economic purpose of the invalid provision.

We may amend these terms at any time. Registered users will be informed of material changes by
email. Continued use of the Service after the amended terms take effect constitutes acceptance.
```

> Note: under Regulation (EU) 1215/2012 (Brussels I recast), consumers may generally only be sued
> in the courts of their own domicile, and choice-of-law clauses cannot deprive a consumer of the
> protection of their home country's mandatory rules (Rome I, Art. 6). Keep the consumer carve-out
> in this clause.

---

## 5. Cookie Notice Texts

### Banner

```text
Headline: We use cookies
Description: We use cookies and similar technologies to give you the best possible experience on
our website. Some cookies are required to operate the site; others help us improve the site and
show you personalised content.
```

### Cookie categories

```text
Essential:
Name: Essential cookies
Description: These cookies are required to operate the website and cannot be disabled. They are
generally set only in response to actions you take, such as setting your privacy preferences or
filling in forms.

Statistics:
Name: Statistics cookies
Description: These cookies allow us to count visits and traffic sources so we can measure and
improve the performance of our site. They help us understand which pages are most popular and
how visitors move around the site.

Marketing:
Name: Marketing cookies
Description: These cookies are used to make advertising more relevant to you. They are used to
control the display of advertising and to measure the effectiveness of advertising campaigns.
```

### Button labels

```text
Accept all: Accept all
Essential only: Essential only
Confirm selection: Confirm selection
Cookie settings: Cookie settings
```

### Detail toggle labels

```text
Show details: Show details
Hide details: Hide details
Always active: Always active
```

---

## Usage Notes

- All text uses a formal, neutral register suitable for legal pages
- Legal references point to EU-level instruments (GDPR, ePrivacy, E-Commerce, Consumer Rights,
  Product Liability). GDPR references are directly applicable EU-wide; directive references must
  be swapped for the implementing national act before publishing
- Fill `{{supervisoryAuthority}}`, `{{governingLaw}}`, `{{jurisdiction}}` and `{{country}}` with
  the values for the country of establishment
- Each tool section (Section 2) is self-contained and can be included or excluded independently
- Replace all `{{placeholders}}` with project-specific values before generating pages
- Conditional sections (health data, payment, right of withdrawal) are only included when the
  respective flag is true
- This file is a reference — the skill generates JSX/TSX pages using these text blocks, not
  Markdown output
- These templates are a starting point and do not constitute legal advice. Have the generated
  pages reviewed by a lawyer qualified in the relevant jurisdiction before publishing
