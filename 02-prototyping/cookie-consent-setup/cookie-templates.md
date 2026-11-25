# Cookie Templates — GDPR-Compliant Text Blocks

Reference file for the `cookie-consent-setup` skill. Contains the legal text blocks for the
cookie banner and the cookie section of a privacy policy.

**Applicable law:** GDPR (Regulation 2016/679) and Art. 5(3) of the ePrivacy Directive
2002/58/EC, as implemented in national law.

> GDPR applies directly and identically across the EU, so the article references below are
> accurate everywhere. The consent requirement for cookies comes from the ePrivacy *Directive*,
> which each member state implements in its own act — replace the directive reference with the
> national provision before publishing, and note that some authorities apply stricter guidance
> than others (for example on the wording of "reject" buttons or on cookie walls).

**Placeholders used throughout:**

| Placeholder | Description | Example |
|---|---|---|
| `{{brandName}}` | Product/brand name | ExampleBrand |
| `{{companyLegalName}}` | Legal entity name | Example Ltd |
| `{{companyAddress}}` | Full postal address | 1 Example Street, 12345 Example City |
| `{{contactEmail}}` | Contact email | hello@example.com |
| `{{websiteUrl}}` | Full website URL | https://example.com |

---

## 1. Cookie Banner Texts

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

## 2. Privacy Policy — Cookie Section

### 2.1 What are cookies

```text
Our website uses cookies. Cookies are small text files stored on your device by your browser.
Most of the cookies we use are so-called session cookies, which are deleted automatically at the
end of your visit. Other cookies remain on your device until you delete them.

We distinguish between the following cookie categories:

- Essential cookies: these are required for the basic functions of the website and cannot be
  disabled. They are generally set only in response to actions you take, for example setting your
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

### 2.2 Withdrawing consent and browser settings

```text
You can change your cookie settings at any time by clicking the "Cookie settings" link in the
footer of our website. There you can enable or disable individual cookie categories.

You can also configure your browser to notify you when cookies are set, to allow cookies only in
individual cases, to exclude the acceptance of cookies for certain cases or in general, and to
enable the automatic deletion of cookies when the browser is closed. Disabling cookies may limit
the functionality of this website.
```

---

## 3. Tool-Specific GDPR Texts

### 3.1 Google Tag Manager

```text
Google Tag Manager

We use Google Tag Manager, provided by Google Ireland Limited, Gordon House, Barrow Street,
Dublin 4, Ireland. Google Tag Manager is a solution that lets us manage website tags through a
single interface. Tag Manager itself sets no cookies and collects no personal data. The service
triggers other tags, which may in turn collect data. Google Tag Manager does not access that
data.

Data processed: Tag Manager itself processes no personal data. It only triggers the execution of
the tags embedded through it.

Legal basis: Art. 6(1)(f) GDPR (legitimate interest in managing website tags efficiently)

Further information: https://policies.google.com/privacy
```

### 3.2 Google Analytics / GA4

```text
Google Analytics

We use Google Analytics, a web analytics service provided by Google Ireland Limited, Gordon
House, Barrow Street, Dublin 4, Ireland. Google Analytics uses cookies and similar technologies
to collect and analyse information about the use of our website.

We use Google Analytics with the IP anonymisation extension. As a result, your IP address is
truncated within member states of the European Union or in other states party to the Agreement
on the European Economic Area.

Data processed: IP address (anonymised), browser type and version, operating system, referrer
URL, pages visited, time on site, interactions, device type, screen resolution

Legal basis: Art. 6(1)(a) GDPR (consent)

Google is certified under the EU-US Data Privacy Framework.

Further information: https://policies.google.com/privacy

You can prevent collection by Google Analytics by installing Google's browser add-on:
https://tools.google.com/dlpage/gaoptout
```

### 3.3 Google Ads

```text
Google Ads (conversion tracking and remarketing)

Our website uses the online advertising programme Google Ads, including conversion tracking and
remarketing features. The provider is Google Ireland Limited, Gordon House, Barrow Street,
Dublin 4, Ireland.

When you click an ad served by Google, a conversion tracking cookie is placed on your device.
These cookies expire after 30 days and are not used to identify you personally.

Data processed: cookie data, usage data, click behaviour, conversion data, IP address
(anonymised)

Legal basis: Art. 6(1)(a) GDPR (consent)

Google is certified under the EU-US Data Privacy Framework.

Further information: https://policies.google.com/privacy

You can deactivate ad personalisation in your Google account settings:
https://adssettings.google.com
```

### 3.4 Meta Pixel

```text
Meta Pixel (Facebook)

Our website uses the Meta Pixel provided by Meta Platforms Ireland Limited, 4 Grand Canal Square,
Grand Canal Harbour, Dublin 2, Ireland. The Meta Pixel allows us to measure the effectiveness of
Facebook advertising and to optimise ads for statistical and market research purposes.

When you visit our website, the Meta Pixel establishes a direct connection to Meta's servers.
This transmits to the Meta server that you have visited our website. Meta associates this
information with your personal Facebook account, if you have one.

Data processed: cookie data, usage data, click behaviour, IP address, device information,
browser type

Legal basis: Art. 6(1)(a) GDPR (consent)

Meta is certified under the EU-US Data Privacy Framework.

Further information: https://www.facebook.com/privacy/policy/
```

### 3.5 PostHog

```text
PostHog

We use PostHog, a web analytics service provided by PostHog Inc., 2261 Market Street #4008, San
Francisco, CA 94114, USA. PostHog helps us analyse user behaviour on our website and make
improvements based on it.

Pseudonymised data about the use of our website may be processed, such as buttons clicked, time
on site, devices used or navigation paths.

When using the EU cloud version, data is processed on European servers.

Data processed: IP address (pseudonymised), browser type, operating system, pages visited, click
behaviour, time on site, referrer URL, device type

Legal basis: Art. 6(1)(f) GDPR (legitimate interest in analysing user behaviour) when used
without personal profiles; Art. 6(1)(a) GDPR (consent) for extended tracking

Further information: https://posthog.com/privacy
```

### 3.6 Hotjar

```text
Hotjar

We use Hotjar, an analytics service provided by Hotjar Ltd, Dragonara Business Centre, 5th Floor,
Dragonara Road, Paceville St Julian's STJ 3141, Malta. Hotjar helps us better understand our
users' needs and optimise what we offer on our website.

Hotjar uses cookies and other technologies to collect data about our users' behaviour and their
devices. This includes in particular recording mouse movements, scrolling and clicks (heatmaps)
as well as capturing session recordings.

Data processed: IP address (anonymised), device type, browser type, screen size, geographic
location (country only), preferred language, mouse movements, clicks, scrolling behaviour

Legal basis: Art. 6(1)(a) GDPR (consent)

Hotjar processes data within the EU.

Further information: https://www.hotjar.com/privacy/
```

### 3.7 Cloudflare (Turnstile)

```text
Cloudflare (CDN and security)

We use services provided by Cloudflare Inc., 101 Townsend St., San Francisco, CA 94107, USA, as
a content delivery network (CDN) and to protect our website against attacks. All requests to our
website are routed through Cloudflare's network.

Cloudflare may also deploy security technologies such as Turnstile (a CAPTCHA alternative) to
detect automated access and protect our website.

Data processed: IP address, date and time of access, volume of data transferred, browser type
and version, requested URL, HTTP status code

Legal basis: Art. 6(1)(f) GDPR (legitimate interest in protecting our website and delivering it
with good performance)

Cloudflare is certified under the EU-US Data Privacy Framework.

Further information: https://www.cloudflare.com/privacypolicy/
```

---

## 4. Cookie Table Template

Use this format in the privacy policy to list all cookies:

```text
Cookies in use

| Cookie/tool | Provider | Purpose | Category | Storage period | Legal basis |
|---|---|---|---|---|---|
| cookie-consent | {{brandName}} | Stores cookie preferences | Essential | 1 year | Art. 6(1)(f) GDPR |
| _ga, _ga_* | Google | Web analytics (GA4) | Statistics | 2 years | Art. 6(1)(a) GDPR |
| _gid | Google | Web analytics (GA4) | Statistics | 24 hours | Art. 6(1)(a) GDPR |
| _fbp | Meta | Ad tracking (Pixel) | Marketing | 90 days | Art. 6(1)(a) GDPR |
| _fbc | Meta | Click tracking (Pixel) | Marketing | 90 days | Art. 6(1)(a) GDPR |
| ph_* | PostHog | Product analytics | Statistics | Session | Art. 6(1)(f) GDPR |
```

Include only rows for tools actually detected in the project.

---

## Usage Notes

- All text uses a formal, neutral register suitable for legal pages
- Legal references point to EU-level instruments. GDPR references apply directly EU-wide; the
  ePrivacy consent requirement must be swapped for the implementing national provision before
  publishing
- Each tool section is self-contained and can be included or excluded independently
- Replace all `{{placeholders}}` with project-specific values
- This file is a reference — the skill generates JSX/TSX components using these text blocks, not
  Markdown output
- **No company data is hardcoded** — all company info comes from user input
- These templates are a starting point and do not constitute legal advice
