---
name: seo
description: Comprehensive SEO audit and optimization — on-page (title, description, headings, schema, OG, Twitter Cards, URLs, internal links, images, video), technical (sitemap, robots, canonical, Core Web Vitals, crawlability, indexing, IndexNow, mobile, rendering), content (keyword research, content strategy, content optimization, E-E-A-T, competitor research), off-page (link building, backlink analysis), local SEO, entity SEO, programmatic SEO, parasite SEO, and AI SEO (GEO - optimizing for ChatGPT, Perplexity, Google AI Overviews, Claude citations). Run /seo to audit and optimize. Based on kostja94/marketing-skills.
model: sonnet
effort: medium
---

## Step 0: Load Marketing Context

Before working with this skill:

1. **Check if `.agents/product-marketing-context.md` exists** in the current project
2. If YES: Read the file and use positioning, personas, voice, and pain points as foundation for your work
3. If NO: Ask the user if they want to run `/product-marketing-context` first, or proceed without it (with a warning that results may be less targeted)

# SEO — Interactive Checklist

This skill walks you step by step through every SEO topic. For each phase you are asked whether it is relevant — skip what does not apply.

Based on [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT License).

---

## Intake: understand first, then work

Ask the user these 3 questions before doing anything else:

**Ask the user:**

1. What do you need? (Full audit / specific area / optimise a new page)
2. Do you have an existing website to audit, or are you planning a new one?
3. What is the priority? (Quick wins / comprehensive / solve a technical problem)

Wait for the user's answers. Then adapt which phases to run:
- "Quick Wins" -> Start with Phase 1 (On-Page) and Phase 2 (Technical), focus on checklist items only
- "New page" -> Start with Phase 1, skip Phase 2 crawlability sections
- "Full audit" -> Walk through all phases in order
- "Specific area" -> Jump to the relevant phase

---

## Phase 1: On-Page SEO

Ask the user: **"Shall we check / optimise On-Page SEO? (Yes/No/Later)"**

If YES: Work through the following checklist and knowledge base with the user.
If NO: Skip to Phase 2.

### On-Page Audit Checklist

Run through these for each page:

- [ ] Title tag: unique, keyword front-loaded, 50-60 chars
- [ ] Meta description: unique, CTA included, 150-160 chars
- [ ] H1: exactly one per page, contains primary keyword
- [ ] Heading hierarchy: logical H1 -> H2 -> H3 (no skipped levels)
- [ ] Schema markup: appropriate type, valid JSON-LD
- [ ] Open Graph tags: og:title, og:description, og:image present
- [ ] Twitter Card tags present
- [ ] Image alt text: descriptive, keyword-natural, max 125 chars
- [ ] Image format: WebP/AVIF preferred, width/height dimensions set
- [ ] Internal links: 3-5+ per page, descriptive anchor text
- [ ] URL structure: short, descriptive, lowercase, hyphens

### 1.1 Title Tag

- One unique title per page
- Length: 50-60 chars (Latin), ~600px pixel width
- Front-load primary keyword
- Brand at end (optional)
- Match search intent; avoid keyword stuffing
- Numbers, power words, questions can boost CTR ~36%
- H1 should align with title tag

**Bad:** "SEO Tips for Small Business" -> **Better:** "11 SEO Tips That Actually Work (2026)"

### 1.2 Meta Description

- Length: 150-160 chars (Latin), ~920px desktop
- Unique per page; no duplicates
- Include clear CTA ("Learn how...", "Discover...")
- Naturally include target keyword
- Does not affect ranking directly; well-written descriptions improve CTR 5-10%

### 1.3 Heading Structure (H1-H6)

- **One H1 per page** with primary keyword
- Logical hierarchy: H1 -> H2 -> H3 (don't skip levels)
- Each heading = one topic, scannable
- Use keyword variations in subheadings

```
H1 (page title)
  -> H2 (section 1)
    -> H3 (subsection)
  -> H2 (section 2)
    -> H3
```

**Common issues:** Multiple H1s, skipped levels, generic headings ("Introduction"), keyword stuffing.

### 1.4 Schema / Structured Data (JSON-LD)

Schema.org markup for rich results, AI search visibility, and machine-readable content. JSON-LD is the preferred format.

**Core types (use on most sites):**

| Type | Use case |
|------|----------|
| Organization | Site-wide; company info, logo, sameAs |
| WebSite | Site-wide; search action, site name |
| Article / BlogPosting | Blog posts, news, tool intros |
| BreadcrumbList | Breadcrumb navigation |
| FAQPage | FAQ sections |
| Person | Author info |

**Exclusive types (match to content):**

| Website type | Schema |
|-------------|--------|
| E-commerce | Product + Offer + AggregateRating |
| Job board | JobPosting |
| Events | Event |
| SaaS / App | SoftwareApplication |
| Local business | LocalBusiness |
| Recipe site | Recipe |
| Tutorial | HowTo |

**Placement:**
- Organization + WebSite -> homepage or root layout (site-wide)
- Article/BlogPosting -> each blog post
- BreadcrumbList -> every page with breadcrumbs

**Article type selection:**
- BlogPosting: informal blog posts
- Article: formal, evergreen content
- NewsArticle: time-sensitive news

**Required properties (Article):** headline (max 110 chars), image (min 1200px wide), datePublished (ISO 8601), author (Person/Organization), publisher (Organization with logo).

**Date display tip:** Show only one date on page. If both datePublished and dateModified visible, Google may pick the wrong one (~22% CTR drop).

**Schema <-> SERP Features mapping:**

| Schema | SERP Feature |
|--------|-------------|
| FAQPage | PAA, Featured Snippet |
| BreadcrumbList | Breadcrumbs |
| AggregateRating / Review | Star ratings |
| HowTo | Step-based snippet |
| VideoObject | Video thumbnail |
| Product + Offer | Shopping results |
| WebSite + SearchAction | Sitelinks searchbox |
| Organization / Person | Knowledge Panel |

**Validation:** [Rich Results Test](https://search.google.com/test/rich-results), [Schema Markup Validator](https://validator.schema.org/)

### JSON-LD Templates

**Product:**
```json
{"@context": "https://schema.org", "@type": "Product", "name": "", "description": "", "offers": {"@type": "Offer", "price": "", "priceCurrency": "EUR"}}
```

**FAQ:**
```json
{"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "", "acceptedAnswer": {"@type": "Answer", "text": ""}}]}
```

**Organization:**
```json
{"@context": "https://schema.org", "@type": "Organization", "name": "", "url": "", "logo": "", "sameAs": []}
```

### Schema Testing Workflow
1. Implement JSON-LD in page head
2. Test with Google Rich Results Test
3. Validate with Schema.org validator
4. Monitor in Google Search Console > Enhancements

**Next.js example:**
```tsx
export const metadata = {
  other: {
    'script:ld+json': JSON.stringify({
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": "...",
      "description": "...",
      "inLanguage": "en-US",
      "image": "https://example.com/image.jpg",
      "datePublished": "2024-01-01T00:00:00Z",
      "author": { "@type": "Person", "name": "..." },
      "publisher": { "@type": "Organization", "name": "...", "logo": { "@type": "ImageObject", "url": "..." } }
    }),
  },
};
```

### 1.5 Open Graph (og: tags)

For Facebook, LinkedIn, WhatsApp, Slack link previews.

| Tag | Guideline |
|-----|-----------|
| og:title | 40-60 chars; can differ from title tag |
| og:description | 80-110 chars; CTA-focused |
| og:image | 1200x630px; <8MB; absolute URL |
| og:url | Canonical URL |
| og:type | website (homepage), article (blog) |
| og:site_name | Brand name |
| og:locale | `{{locale}}` (language_TERRITORY, matching the page language) |

**Testing:** Facebook Sharing Debugger, LinkedIn Post Inspector

### 1.6 Twitter Cards

| Tag | Guideline |
|-----|-----------|
| twitter:card | summary_large_image (recommended) or summary |
| twitter:title | 50-60 chars |
| twitter:description | 100-130 chars |
| twitter:image | 1200x628px (large), 400x400px (summary) |
| twitter:site | @handle |

### 1.7 URL Structure

- Short, descriptive, lowercase, hyphens (not underscores)
- Include primary keyword
- No file extensions, no special characters
- Flat hierarchy: max 3-4 levels deep
- Multi-language: `/{{lang1}}/page`, `/{{lang2}}/page`
- HTTPS always
- Avoid URL parameter-based content for SEO pages

### 1.8 Internal Links

- Use descriptive anchor text (not "click here")
- Link from high-authority pages to important pages
- 3-5 internal links per page minimum
- Fix orphan pages (pages with no internal links)
- Use breadcrumbs for hierarchical linking
- Hub-and-spoke model: pillar page -> cluster articles -> back to pillar

### 1.9 Image Optimization

| Item | Guideline |
|------|-----------|
| Format | WebP preferred; AVIF for modern browsers; JPEG fallback |
| Alt text | Descriptive, include keyword naturally; 125 chars max |
| File name | Descriptive, hyphenated (e.g. `seo-checklist-2026.webp`) |
| Dimensions | Specify width/height to prevent CLS |
| Lazy loading | `loading="lazy"` for below-fold images |
| Srcset | Responsive images with multiple sizes |

### 1.10 Video Optimization

- Use VideoObject schema (name, description, thumbnailUrl, uploadDate, duration, contentUrl)
- Create video sitemap
- Custom thumbnail (1280x720px minimum)
- Add key moments / timestamps for clip markup
- Host on YouTube for maximum reach; embed on site for engagement

### 1.11 Featured Snippets

- Target question-based queries
- Answer-first format: direct answer in first 40-60 words after H2
- Structure for snippet types: paragraph (40-60 words), list (5-8 items), table (3+ rows/columns)
- Use H2 as the question, answer immediately below
- Schema (FAQPage, HowTo) supports extraction

### 1.12 SERP Features

**Rich results** = schema-powered (stars, breadcrumbs, FAQ dropdowns). **Featured snippets** = Google-extracted answer boxes at position zero (no schema required).

Zero-click rate: ~65% of searches. Strategy: optimize for brand visibility even without clicks.

**Phase 1 complete. Continue to Phase 2? (Yes/No)**

---

## Phase 2: Technical SEO

Ask the user: **"Shall we check Technical SEO? (Yes/No/Later)"**

If YES: Work through the following checklist and knowledge base.
If NO: Skip to Phase 3.

### Technical Audit Checklist

- [ ] Sitemap.xml: exists, valid, submitted to Search Console
- [ ] Robots.txt: proper blocks, sitemap reference included
- [ ] Canonical tags: self-referencing, correct, one per page
- [ ] HTTPS: all pages, no mixed content
- [ ] Core Web Vitals: LCP <=2.5s, INP <=200ms, CLS <=0.1
- [ ] Mobile-friendly: responsive design, viewport tag present
- [ ] No broken links (404s)
- [ ] No redirect chains (max 1 hop)
- [ ] hreflang correctly implemented (if multi-language)
- [ ] Rendering strategy: SSG/SSR for SEO-critical pages
- [ ] noindex applied to correct pages (thank-you, login, search results)
- [ ] IndexNow configured (for Bing, Yandex)

### 2.1 Sitemap (XML)

- Max 50,000 URLs or 50MB per sitemap; use sitemap index for larger sites
- Include only canonical, indexable URLs (200 status, not noindex)
- Set `lastmod` only when content meaningfully changes
- Multi-language: add `xhtml:link` with hreflang in sitemap
- Submit via robots.txt: `Sitemap: https://example.com/sitemap.xml`
- Auto-generate from CMS/framework (Next.js: `app/sitemap.ts`)

### 2.2 Robots.txt

- Place at domain root: `https://example.com/robots.txt`
- Block: admin, API, auth, search results, staging, private
- Allow: all public content, CSS/JS (needed for rendering)
- Always include: `Sitemap: https://example.com/sitemap.xml`
- robots.txt = crawl control only; does NOT prevent indexing (use noindex for that)

**AI crawlers strategy:**
- Allow: Googlebot, Bingbot, GPTBot (if you want AI visibility)
- Consider blocking: CCBot, anthropic-ai, if you don't want training data usage
- Default: allow all unless specific reason to block

### 2.3 Canonical Tags

- Every indexable page needs a self-referencing canonical
- Use absolute URLs with https://
- Only one canonical per page
- Canonical + hreflang must align for multi-language
- HTTP -> HTTPS, www -> non-www redirects must match canonical

### 2.4 Core Web Vitals

| Metric | Good | Needs Work | Poor |
|--------|------|------------|------|
| **LCP** (Largest Contentful Paint) | <=2.5s | <=4.0s | >4.0s |
| **INP** (Interaction to Next Paint) | <=200ms | <=500ms | >500ms |
| **CLS** (Cumulative Layout Shift) | <=0.1 | <=0.25 | >0.25 |

**LCP fixes:** Optimize hero image (preload, WebP, srcset), reduce server response time, minimize render-blocking CSS/JS.
**INP fixes:** Reduce JS execution, break long tasks, use `requestIdleCallback`.
**CLS fixes:** Set explicit dimensions on images/embeds, avoid dynamic content insertion above fold, use `font-display: swap`.

**Tools:** PageSpeed Insights, Chrome DevTools, Search Console Core Web Vitals report, web-vitals JS library.

### 2.5 Crawlability

- Fix redirect chains (max 1 redirect hop)
- Fix broken links (404s) -- redirect or remove
- Flat site architecture: every page reachable in <=3 clicks from homepage
- Use pagination with rel="next"/rel="prev" or load-more (not infinite scroll for SEO)
- Crawl budget: relevant for sites with 10,000+ pages

### 2.6 Indexing

**Pages that should be noindex:**
- Thank you / confirmation pages
- Internal search results
- Tag/filter pages with thin content
- Login/signup/account pages
- Staging/preview/draft pages
- Legal pages (sometimes -- depends on strategy)

**Google Indexing API:** Use for JobPosting and BroadcastEvent types for faster indexing. For other content types, use IndexNow.

**Soft 404:** Pages that return 200 but have no meaningful content. Fix: return proper 404 or add content.

### 2.7 IndexNow

- Instant indexing notification for Bing, Yandex, Seznam (not Google)
- Generate API key, host at root, submit URL on publish/update
- Integrate into CI/CD: auto-submit on deploy
- Supported engines: Bing, Yandex, Seznam, Naver

### 2.8 Mobile-Friendly

- Google uses mobile-first indexing (mobile version is primary)
- Responsive design required; same content on mobile and desktop
- Viewport meta tag: `<meta name="viewport" content="width=device-width, initial-scale=1">`
- Touch targets: minimum 48x48px with 8px spacing
- No horizontal scrolling; readable font sizes (16px+ base)

### 2.9 Rendering Strategies

| Strategy | SEO | When to use |
|----------|-----|-------------|
| **SSG** | Best | Static content, blogs, docs |
| **SSR** | Great | Dynamic content, personalized pages |
| **ISR** | Great | Frequently updated content |
| **CSR** | Poor | App-like interfaces (not SEO-critical) |

For SPAs (React, Vue): use SSR/SSG for SEO-critical pages. Googlebot can render JS but with delays and issues.

### 2.10 Page Metadata (hreflang, robots, viewport)

**hreflang (multi-language):**
- Self-referencing tags required
- Symmetric annotations (every version lists ALL others)
- Include x-default for fallback
- Canonical must match regional version

```html
<link rel="alternate" hreflang="{{lang1}}" href="https://example.com/{{lang1}}/page" />
<link rel="alternate" hreflang="{{lang2}}" href="https://example.com/{{lang2}}/page" />
<link rel="alternate" hreflang="x-default" href="https://example.com/{{lang1}}/page" />
```

**Meta robots:**
- `noindex` = exclude from search results
- `nofollow` = don't pass link equity (does NOT prevent indexing)
- `noindex,follow` = most common for thank-you, legal pages

**Phase 2 complete. Continue to Phase 3? (Yes/No)**

---

## Phase 3: Content SEO

Ask the user: **"Shall we tackle content SEO and keyword strategy? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 4.

### Content Checklist

- [ ] Primary keyword defined for each page
- [ ] Content matches search intent (informational / commercial / transactional)
- [ ] E-E-A-T signals present: author info, credentials, sources
- [ ] Content freshness: dates updated where relevant
- [ ] No thin or duplicate content
- [ ] Topic clusters planned: pillar page + supporting articles
- [ ] Keyword cannibalization checked (no two pages targeting same keyword)

### 3.1 Keyword Research

**Discovery methods:**
1. Google Autocomplete + "People Also Ask"
2. Competitor analysis (what they rank for)
3. Customer language (reviews, support tickets, forums)
4. Seed keyword -> long-tail expansion

**Search intent types:**
- Informational: "how to...", "what is..."
- Navigational: brand searches
- Commercial: "best...", "vs", "review"
- Transactional: "buy...", "price...", "discount"

**Clustering:** Group keywords by topic/intent -> map to pages. One primary keyword per page + related secondary keywords.

**Topical map:** Build clusters around core topics. Pillar page (broad) -> cluster articles (specific) -> internal linking between them.

### 3.2 Content Strategy

**Topic cluster model:**
- **Pillar page**: Comprehensive guide (2000-4000 words) targeting broad keyword
- **Cluster articles**: Specific subtopics (800-1500 words) linking back to pillar
- **Internal linking**: Hub-and-spoke; every cluster links to pillar and vice versa

**Content types by funnel stage:**
- TOFU (awareness): Blog posts, guides, infographics
- MOFU (consideration): Case studies, comparisons, webinars
- BOFU (decision): Product pages, free trials, demos, testimonials

### 3.3 Content Optimization

| Factor | Guideline |
|--------|-----------|
| Word count | Match top-ranking competitors; quality > length |
| H2 keywords | Include keyword variations in H2 headings |
| Keyword density | 1-2% natural; never stuff |
| Multimedia | Images, videos, infographics break up text |
| Tables & lists | Improve scannability; help featured snippets |
| Freshness | Update content regularly; add dateModified |

### 3.4 E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness)

| Signal | Implementation |
|--------|---------------|
| **Experience** | First-hand accounts, original data, case studies |
| **Expertise** | Author bios with credentials, author schema |
| **Authoritativeness** | Backlinks, citations, brand mentions |
| **Trustworthiness** | HTTPS, privacy policy, accurate info, editorial standards |

**YMYL (Your Money Your Life):** Health, finance, legal, safety content requires highest E-E-A-T. Extra scrutiny from Google.

**Author pages:** Create dedicated author pages with bio, credentials, social links, published articles. Link from articles via author schema.

### 3.5 Competitor Research

1. Identify top 3-5 competitors in search results
2. Analyze: keywords they rank for, content gaps, backlink sources
3. Find content gaps: topics competitors cover that you don't
4. Analyze their top-performing content: format, length, structure
5. Check their schema markup and SERP features

**Phase 3 complete. Continue to Phase 4? (Yes/No)**

---

## Phase 4: Off-Page SEO / Link Building

Ask the user: **"Shall we discuss off-page SEO and link building? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 5.

### Off-Page Checklist

- [ ] Backlink profile reviewed: quality, diversity, no spam
- [ ] Brand presence: consistent social profiles, sameAs in schema
- [ ] Link building strategy selected (see options below)
- [ ] Anchor text distribution checked (not over-optimized)

### 4.1 Link Building

**Quality over quantity.** One authoritative link > 100 low-quality links.

**Strategies:**
- Create link-worthy content (original research, tools, data)
- Guest posting on relevant, authoritative sites
- HARO / journalist queries
- Broken link building (find broken links -> offer replacement)
- Resource page outreach
- Digital PR and press coverage

**Avoid:** Link farms, PBNs, paid links (Google penalty risk), reciprocal link schemes.

### 4.2 Backlink Analysis

**Key metrics:** Domain Authority/Rating, referring domains count, anchor text distribution, link velocity.

**Quality signals:** Relevant niche, editorial placement, followed link, diverse anchor text.

**Risk signals:** Sudden link spikes, exact-match anchor text overuse, links from unrelated sites, PBN patterns.

**Disavow:** Only if clear penalty/manual action. Google is good at ignoring bad links automatically.

**Phase 4 complete. Continue to Phase 5? (Yes/No)**

---

## Phase 5: AI SEO / GEO

Ask the user: **"Should your content be optimised for AI search (ChatGPT, Perplexity, Google AI Overviews)? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 6.

### AI SEO Checklist

**Content structure:**
- [ ] Page has a clear, question-based or topic-clear headline
- [ ] TL;DR or summary near the top
- [ ] H2/H3 headings written as questions or clear topics
- [ ] Each section front-loads its answer
- [ ] FAQ-style Q&A blocks present
- [ ] Tables, lists, or structured data elements present

**Entity signals:**
- [ ] Company/product name used consistently across all content
- [ ] Entity hub page (About/company page) exists
- [ ] Organization schema on About/company page
- [ ] Product pages using SoftwareApplication or Product schema

**E-E-A-T:**
- [ ] Articles have a named author with credentials
- [ ] Statistics cited with source and date
- [ ] Clear publication/update date on all content

**Monitoring:**
- [ ] Weekly AI mention check scheduled
- [ ] Tracking spreadsheet created

### How AI Search Differs from Traditional Search

| Traditional Google | AI Search |
|-------------------|-----------|
| Ranks pages by authority + relevance | Cites sources in synthesized answers |
| Goal: be on page 1 | Goal: be the source AI references |
| Keyword density matters | Entity clarity and structure matters |
| Backlinks = authority | Citations + clear definitions = authority |
| User clicks to your page | AI may answer without a click |
| Optimized for algorithms | Optimized for LLM comprehension |

**The shift:** Google ranks pages. AI systems choose SOURCES. Being cited by AI is the new "ranking #1" for many queries.

### Content Patterns that Earn AI Citations

**1. Clear Definitions First**

AI systems extract definitions. Structure every key concept as a clear, standalone definition.

Pattern:
```
[Term] is [clear definition in one sentence]. [Expand with 1-2 sentences of context].
```

**2. FAQ-Style Question and Answer Blocks**

Write Q&A pairs exactly as someone would type them into ChatGPT or Perplexity. AI systems lift these verbatim.

```markdown
## [Common question users ask]

[Direct answer in 1-2 sentences]. [Supporting detail in 2-3 sentences].
```

**3. Comparison Content**

"[X] vs [Y]" pages get cited heavily. Structure: summary table at top, clear winner per use case, specific factual differences, pros/cons.

**4. Original Data and Statistics**

AI systems cite original data. Always include: sample size, date of collection, methodology, clear attribution.

**5. Structured Lists and Tables**

AI parses structured content more easily than prose. Prefer: numbered lists for processes, bullet lists for features, tables for comparisons, definition lists for glossaries.

**6. Expert Quotes and Named Sources**

Include first + last name, title and company, direct quote in quotation marks.

**7. Concise, Complete Answers**

Each section should answer one question completely. AI systems prefer self-contained paragraphs that answer a specific question without requiring surrounding context.

### Entity Optimization

Traditional SEO optimizes for keywords. Entity optimization makes sure AI systems understand WHAT you are, WHO you serve, and HOW you relate to other concepts.

**Entity Building Checklist:**

1. **Consistent naming across all properties** - company name always the same spelling, product name never abbreviated unless established, social profiles same name everywhere

2. **Create an entity hub page** - About page or dedicated company page with: full company name, what you do, who you serve, where you operate, when founded, key products. Add Organization schema.

3. **Build entity relationships** - Create content that explicitly connects:
   - Product -> Problem it solves -> Who has that problem
   - Company -> Industry -> Competitors -> Differentiators
   - Feature -> Use case -> Persona -> Outcome

4. **Wikipedia/Wikidata presence** - For larger ventures: one of the strongest entity signals for AI systems

5. **Schema.org markup** - JSON-LD for: Organization, Product, SoftwareApplication, FAQPage, HowTo, Article

### Content Structure for AI Readability

**Page-Level Structure:**
```
[Page title - should be the question/topic]
[TL;DR or summary - 2-3 sentences]
[Table of contents for long pages]

[H2 - First main topic]
[Direct answer to this section's implicit question]
[Supporting details]
```

**Heading Best Practices:**
- Write H2/H3 headings as questions or clear topic statements
- Good: "How does progressive profiling work?"
- Good: "Progressive Profiling: Definition and Best Practices"
- Bad: "Overview" / "Introduction" / "More information"

**Front-Load Every Section:**

Bad: "In order to understand how our pricing works, you first need to know that..."

Good: "Our pricing has three tiers: Starter ($29/mo), Growth ($79/mo), Enterprise (custom). Each tier is designed for different team sizes:"

### Platform-Specific Optimization

| Platform | What it prefers | Key tactic |
|----------|----------------|------------|
| ChatGPT | Authoritative, well-structured content | Be the definitive source on your topic |
| Perplexity | Recent content with citations | Keep content fresh, add publication dates |
| Google AI Overviews | Schema-rich, E-E-A-T content | Structured data + author credentials |
| Claude | Well-reasoned, nuanced, honest content | Depth and accuracy over promotional tone |
| Bing Copilot | Web content with clear authorship | Author markup + fresh content |

### Monitoring Protocol

**Weekly (manual, 15 min):** Check brand and product in ChatGPT, Perplexity, and Google AI Overviews:
- "[Your product name]"
- "Best [your category] tools"
- "[Your product] vs [competitor]"
- "How does [your product] work?"

**Monthly deeper audit:**
- Search product category + "best", "top", "alternative", "vs", "review"
- Check if you appear in "best [X] for [use case]" queries
- Check competitor names - are they cited more than you?
- Verify accuracy: when AI mentions you, is the description correct?

**If miscited or misrepresented:**
1. Identify what the AI says (specific claims)
2. Find the source content that trained this
3. Update the source content to correct the record
4. Add a clear, definitive statement about correct information
5. Wait 4-8 weeks for AI systems to re-index

**Tracking template:** Spreadsheet with: Date, Platform, Query, Brand mentioned (Y/N), Accurate (Y/N/Partial), Competitors mentioned, Action needed.

### Structured Data for AI Visibility

**For SaaS/Product pages:**
```json
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "Product Name",
  "applicationCategory": "BusinessApplication",
  "description": "One sentence description",
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "EUR"
  }
}
```

**For FAQ sections:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "How does X work?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "Direct answer here."
    }
  }]
}
```

**For How-To content:**
```json
{
  "@context": "https://schema.org",
  "@type": "HowTo",
  "name": "How to [task]",
  "step": [{
    "@type": "HowToStep",
    "text": "Step description"
  }]
}
```

### Tools
- Schema.org validator for structured data
- Google Rich Results Test
- Perplexity.ai for citation checking
- ChatGPT for brand mention testing

**Phase 5 complete. Continue to Phase 6? (Yes/No)**

---

## Phase 6: Site Architecture

Ask the user: **"Shall we optimise the site architecture and internal linking? (Yes / no / later)"**

If YES: Work through the following.
If NO: Skip to Phase 7.

### Site Architecture Checklist

- [ ] URL hierarchy planned: max 3 levels deep
- [ ] Every important page reachable within 3 clicks from homepage
- [ ] Main nav reflects top keyword categories
- [ ] Breadcrumbs on all pages (with BreadcrumbList schema)
- [ ] Footer links to key pages and categories
- [ ] XML sitemap submitted to Google Search Console
- [ ] Low-value pages blocked in robots.txt
- [ ] Crawl errors checked in Search Console

### Page Hierarchy & URL Structure
- Plan URL patterns: `/category/subcategory/page-slug`
- Keep URLs short, descriptive, keyword-rich
- Avoid deep nesting (max 3 levels)

### Internal Linking Strategy
- Hub & Spoke model: pillar pages link to cluster content
- Every important page should be reachable within 3 clicks from homepage
- Use descriptive anchor text (not "click here")
- Build topic clusters: 1 pillar page + 5-15 supporting pages

### Navigation for SEO
- Main nav should reflect top keyword categories
- Breadcrumbs on all pages (with BreadcrumbList schema)
- Footer links to key pages and categories

### Crawl Budget
- Submit XML sitemap to Google Search Console
- Use robots.txt to block low-value pages (admin, staging, duplicates)
- Fix crawl errors promptly
- Monitor crawl stats in Search Console

**Phase 6 complete. Continue to Phase 7? (Yes/No)**

---

## Phase 7: Local / Entity / Programmatic SEO

Ask the user: **"Is Local SEO, Entity SEO or Programmatic SEO relevant for you? (Yes/No/Later)"**

If YES: Ask which sub-topics apply and show relevant sections.
If NO: Skip to Phase 8.

### 7a. Local SEO

Ask: **"Do you have a physical location? (Yes/No)"**

If YES:

- [ ] Google Business Profile: all fields completed, photos added
- [ ] NAP (Name, Address, Phone) consistent across all platforms
- [ ] Reviews: responding to all reviews
- [ ] Google Posts used for updates
- [ ] Primary category correct
- [ ] Citations on relevant directories (Yelp, industry-specific)

**NAP consistency:** Name, Address, Phone must be identical across all platforms.

**Google Business Profile:**
- Complete all fields; add photos regularly
- Respond to all reviews
- Use Google Posts for updates
- Choose correct primary category

**Citations:** List business on relevant directories. Audit regularly for consistency.

If NO: Skip 7a.

### 7b. Entity SEO

Ask: **"Do you want to establish your brand as an entity for search engines and AI? (Yes / no)"**

If YES:

- [ ] Organization schema with @id and sameAs (social profiles, Wikipedia, Wikidata)
- [ ] Consistent brand information across web
- [ ] Author entities: Person schema, consistent bylines

Making your brand/people/products recognizable as entities to search engines and AI.

**Entity signals:**
- Organization schema with @id, sameAs (social profiles, Wikipedia, Wikidata)
- Consistent brand information across web
- Knowledge Panel: requires Wikipedia page or strong web presence
- Author entities: Person schema, Google Scholar, consistent bylines

**For AI/GEO:** Structured data makes content machine-readable. AI engines (Google AI Overviews, Perplexity, ChatGPT) extract and cite more accurately from well-structured content.

If NO: Skip 7b.

### 7c. Programmatic SEO

Ask: **"Do you want to generate pages automatically from data (e.g. city pages, product comparisons)? (Yes / no)"**

If YES:

- [ ] Data source defined (database, API, public data)
- [ ] Page template created (consistent layout with dynamic content)
- [ ] Unique value defined per page (not just raw data)
- [ ] Thin content check: each page has genuine unique content

Generating pages at scale from structured data.

**Three-part framework:**
1. **Data source** (database, API, public data)
2. **Page template** (consistent layout with dynamic content)
3. **Unique value** (aggregation, comparison, visualization - not just raw data)

**Use cases:** City/location pages, product comparisons, tool directories, job boards, glossaries.

**Critical:** Each page must have unique, valuable content. Thin/duplicate pages trigger quality penalties.

### 7d. Parasite SEO

Ask: **"Do you want to publish content on third-party platforms to rank for competitive keywords? (Yes / no)"**

If YES:

**Platform tiers:**
- Tier 1 (highest authority): Medium, LinkedIn, GitHub, Reddit, YouTube
- Tier 2: Quora, dev.to, Hashnode, industry forums

**Strategy:** Publish optimized content on these platforms -> link back to your site. Works for competitive keywords where your domain can't rank directly (yet).

**Risks:** Platform can remove content; you don't control the domain; Google's 2024 site reputation abuse policy may penalize some tactics.

**Phase 7 complete. Continue to Phase 8? (Yes/No)**

---

## Phase 8: Audit Report + Priority Actions

After completing relevant phases, compile findings and present to the user:

### Findings Summary

Present a traffic-light summary:

| Area | Status | Critical issues | Quick wins |
|---------|--------|-----------------|------------|
| On-Page | 🟢/🟡/🔴 | ... | ... |
| Technical | 🟢/🟡/🔴 | ... | ... |
| Content | 🟢/🟡/🔴 | ... | ... |
| Off-Page | 🟢/🟡/🔴 | ... | ... |

### Output Format

Present:
1. **Score summary** - traffic-light per category (on-page, technical, content, off-page)
2. **Critical issues** - things that block SEO performance (fix immediately)
3. **Improvements** - things that would boost performance (prioritized)
4. **Quick wins** - easy fixes with high impact
5. **Implementation** - fix issues directly in the codebase where possible

### The top three actions for the next two weeks

Based on all phases completed, identify and present the 3 highest-impact actions:

1. **[Action 1]** - [Rationale / expected impact]
2. **[Action 2]** - [Rationale / expected impact]
3. **[Action 3]** - [Rationale / expected impact]

---

## References

- [Google Search Central](https://developers.google.com/search)
- [Schema.org](https://schema.org/)
- [Google Rich Results Test](https://search.google.com/test/rich-results)
- [PageSpeed Insights](https://pagespeed.web.dev/)
- [Search Console](https://search.google.com/search-console)
- Source: [kostja94/marketing-skills](https://github.com/kostja94/marketing-skills) (MIT)

## Related Skills
- `/product-marketing-context` - Marketing context as foundation
- `/content-marketing` - Content strategy
- `/competitor-profiling` - Competitor keyword gaps and comparison pages
- `/google-ads` - Paid search as complement to organic
- `/analytics-tracking` - Track SEO performance
