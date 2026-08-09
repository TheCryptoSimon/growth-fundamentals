# Schema and Technical Wiring

The machine-readable layer: structured data, canonicals, metadata, sitemaps, robots, `llms.txt`, and
the registry pattern that stops them drifting apart. Read while building or auditing pages, after the
content decisions in [SEO fundamentals](./11-seo-fundamentals.md) and [GEO](./12-geo-ai-search.md).
Everything here is copy-and-adapt; replace every `PLACEHOLDER`.

---

## 0. What this layer buys you

| Consumer | What it reads | What you get |
|---|---|---|
| Search engines | JSON-LD, canonicals, sitemap, robots | Rich results, correct indexing, no duplicate-content confusion |
| AI answer engines | Clean HTML, JSON-LD, `speakable`, `llms.txt` | Unambiguous facts to extract and attribute to you |
| Social platforms | Open Graph, Twitter cards | A share card that looks deliberate rather than broken |
| Your own tooling | The page registry | Sitemap, links, metadata and `llms.txt` generated, not hand-maintained |

**The rule that governs all of it:** structured data describes what is *on the page*. It is a
translation layer, never an addition. A fact not visible to a human reading the page does not belong
in the markup.

## 1. One connected graph per page

**What it is.** Every page emits one `<script type="application/ld+json">` containing a `@graph`
whose nodes reference each other by `@id` — and every page points at the *same* Organization `@id`.

**Mechanism.** Unlinked snippets read as unrelated assertions. A connected graph tells a parser
"this article, on this site, published by this organization, whose profiles are these" in one pass —
the entity-consolidation problem from [GEO §5](./12-geo-ai-search.md).

**The `@id` convention** — URL fragments on your canonical domain, never changed:
`https://example.com/#organization` · `/#website` · `/path/#webpage` · `/path/#primaryimage` ·
`/about/#person-firstname` · `/pricing/#product`.

**Rules.** One script block per page. Define Organization and WebSite once in the site layout and
reference them by `@id` everywhere else. Every page carries a `WebPage` node with `isPartOf` →
WebSite and `publisher`/`about` → Organization. Never emit the same `@id` with different content on
two pages.

## 2. Page type → JSON-LD cookbook

| Page type | Primary node | Also emit | Required | Recommended |
|---|---|---|---|---|
| Homepage | `Organization` + `WebSite` | `WebPage`, `FAQPage` if shown | name, url, logo | description, sameAs, contactPoint, SearchAction |
| Product / commercial | `Product` or `SoftwareApplication` | `WebPage`, `BreadcrumbList`, `FAQPage` | name, description, offers (price, currency, availability) | brand, image, applicationCategory, operatingSystem |
| Article / blog post | `Article` / `BlogPosting` | `WebPage`, `BreadcrumbList` | headline, image, datePublished, author, publisher | dateModified, articleSection, mainEntityOfPage |
| Service page | `Service` | `WebPage`, `BreadcrumbList`, `FAQPage` | name, provider, serviceType, areaServed | description, offers, audience |
| Glossary term | `DefinedTerm` | `WebPage`, `BreadcrumbList` | name, description, inDefinedTermSet | url, termCode |
| Glossary index | `DefinedTermSet` | `WebPage`, `BreadcrumbList` | name, url | hasDefinedTerm[], description |
| FAQ page or section | `FAQPage` | `WebPage` | mainEntity[] of Question → acceptedAnswer | — |
| How-to / tutorial | `HowTo` | `Article`, `WebPage`, `BreadcrumbList` | name, step[] (HowToStep: name + text) | totalTime, supply, tool, per-step image |
| Video | `VideoObject` | in its host page's graph | name, description, thumbnailUrl, uploadDate | duration, embedUrl, transcript |
| Event | `Event` | `WebPage`, `BreadcrumbList` | name, startDate, location, eventAttendanceMode | endDate, offers, organizer |
| Person / author bio | `Person` | `WebPage`, `BreadcrumbList` | name | jobTitle, worksFor (→ Org `@id`), sameAs, knowsAbout |
| Local business | `LocalBusiness` or a subtype | `WebPage`, `BreadcrumbList` | name, address, telephone | openingHoursSpecification, geo, priceRange |
| Every non-home page | `BreadcrumbList` | — | itemListElement[]: position, name, item | — |

**Choosing the commercial type:** software with a licence or subscription → `SoftwareApplication`
(optionally also `Product`); physical goods → `Product`; a delivered human service → `Service`. Do
not stack all three hoping one sticks.

## 3. Ready-to-adapt snippets

Replace every placeholder. **Delete any property you cannot fill honestly** — an absent property is
fine, a guessed one is not. Assemble them as one page graph:

```html
<script type="application/ld+json">
{ "@context": "https://schema.org", "@graph": [
  Organization, WebSite, WebPage, BreadcrumbList,
  <the page-type node: Article | Product | Service | DefinedTerm | ...>,
  FAQPage (only if the page shows FAQs)
] }
</script>
```

### 3.1 Organization — site-wide, defined once

```json
{
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "PLACEHOLDER Brand",
  "alternateName": "PLACEHOLDER",
  "url": "https://example.com/",
  "description": "PLACEHOLDER Brand is a CATEGORY for AUDIENCE. It MECHANISM, and DIFFERENTIATOR.",
  "foundingDate": "2026",
  "logo": { "@type": "ImageObject", "@id": "https://example.com/#logo", "url": "https://example.com/img/logo-512.png", "width": 512, "height": 512 },
  "image": { "@id": "https://example.com/#logo" },
  "contactPoint": { "@type": "ContactPoint", "contactType": "customer support", "email": "support@example.com", "availableLanguage": ["en"] },
  "sameAs": ["https://www.linkedin.com/company/PLACEHOLDER", "https://github.com/PLACEHOLDER"]
}
```

`description` is the exact entity paragraph from [GEO §5](./12-geo-ai-search.md). `sameAs` lists only
profiles you control and that link back.

### 3.2 WebSite with SearchAction

Include `potentialAction` **only if** that URL pattern really performs a site search.

```json
{
  "@type": "WebSite",
  "@id": "https://example.com/#website",
  "url": "https://example.com/",
  "name": "PLACEHOLDER Brand",
  "description": "PLACEHOLDER one-line descriptor.",
  "publisher": { "@id": "https://example.com/#organization" },
  "inLanguage": "en",
  "potentialAction": {
    "@type": "SearchAction",
    "target": { "@type": "EntryPoint", "urlTemplate": "https://example.com/search?q={search_term_string}" },
    "query-input": "required name=search_term_string"
  }
}
```

### 3.3 WebPage with speakable

`speakable` points at the direct-answer block; the selector must exist in the rendered HTML.

```json
{
  "@type": "WebPage",
  "@id": "https://example.com/how-it-works/#webpage",
  "url": "https://example.com/how-it-works/",
  "name": "PLACEHOLDER page title",
  "description": "PLACEHOLDER meta description — the same string as the meta tag.",
  "isPartOf": { "@id": "https://example.com/#website" },
  "about": { "@id": "https://example.com/#organization" },
  "datePublished": "2026-01-15T09:00:00+00:00",
  "dateModified": "2026-03-02T11:30:00+00:00",
  "inLanguage": "en",
  "breadcrumb": { "@id": "https://example.com/how-it-works/#breadcrumb" },
  "speakable": { "@type": "SpeakableSpecification", "cssSelector": [".direct-answer"] }
}
```

### 3.4 BreadcrumbList

Positions start at 1 and match the visible breadcrumb; the last item has no `item` — it is the
current page.

```json
{
  "@type": "BreadcrumbList",
  "@id": "https://example.com/guides/onboarding/#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Guides", "item": "https://example.com/guides/" },
    { "@type": "ListItem", "position": 3, "name": "Onboarding" }
  ]
}
```

### 3.5 Article — `author` must be a real named `Person` or the `Organization`; never invent a byline

```json
{
  "@type": "Article",
  "@id": "https://example.com/blog/POST-SLUG/#article",
  "headline": "PLACEHOLDER headline under 110 characters",
  "description": "PLACEHOLDER standfirst, one sentence.",
  "image": ["https://example.com/img/POST-SLUG-1200x630.jpg"],
  "datePublished": "2026-02-10T08:00:00+00:00",
  "dateModified": "2026-02-18T14:20:00+00:00",
  "author": { "@id": "https://example.com/about/#person-alex" },
  "publisher": { "@id": "https://example.com/#organization" },
  "mainEntityOfPage": { "@id": "https://example.com/blog/POST-SLUG/#webpage" },
  "articleSection": "PLACEHOLDER pillar",
  "inLanguage": "en"
}
```

### 3.6 Product / SoftwareApplication with a real Offer

```json
{
  "@type": ["SoftwareApplication", "Product"],
  "@id": "https://example.com/pricing/#product",
  "name": "PLACEHOLDER Brand",
  "description": "PLACEHOLDER what it does, for whom.",
  "url": "https://example.com/pricing/",
  "image": "https://example.com/img/product-1200x630.jpg",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "brand": { "@id": "https://example.com/#organization" },
  "offers": { "@type": "Offer", "price": "29.00", "priceCurrency": "EUR", "availability": "https://schema.org/InStock", "url": "https://example.com/pricing/" }
}
```

**No `aggregateRating` and no `review` unless real, verifiable, user-submitted reviews exist on that
page.** A product with real offers and no rating validates cleanly; the "no rating" notice in testing
tools is expected and honest. For a tier lineup use `AggregateOffer`
(`lowPrice`/`highPrice`/`offerCount`) or several `Offer` objects.

### 3.7 FAQPage — generated from the same array that renders the visible FAQ

```json
{
  "@type": "FAQPage",
  "@id": "https://example.com/pricing/#faq",
  "mainEntity": [
    { "@type": "Question",
      "name": "PLACEHOLDER question exactly as a person would ask it?",
      "acceptedAnswer": { "@type": "Answer", "text": "PLACEHOLDER 40-80 word self-contained answer, identical to the visible text." } },
    { "@type": "Question",
      "name": "PLACEHOLDER second, genuinely different question?",
      "acceptedAnswer": { "@type": "Answer", "text": "PLACEHOLDER answer." } }
  ]
}
```

### 3.8 DefinedTerm, DefinedTermSet and Person

Give each named framework a `DefinedTerm` too, so the coined name carries a machine-readable
definition attached to your entity.

```json
{
  "@type": "DefinedTerm",
  "@id": "https://example.com/glossary/TERM-SLUG/#term",
  "name": "PLACEHOLDER Term",
  "description": "PLACEHOLDER 40-70 word standalone definition, identical to the on-page paragraph.",
  "url": "https://example.com/glossary/TERM-SLUG/",
  "inDefinedTermSet": { "@id": "https://example.com/glossary/#termset" }
}
```

```json
{
  "@type": "DefinedTermSet",
  "@id": "https://example.com/glossary/#termset",
  "name": "PLACEHOLDER Brand Glossary",
  "url": "https://example.com/glossary/",
  "hasDefinedTerm": [ { "@id": "https://example.com/glossary/TERM-SLUG/#term" }, { "@id": "https://example.com/glossary/OTHER-TERM/#term" } ]
}
```

```json
{
  "@type": "Person",
  "@id": "https://example.com/about/#person-alex",
  "name": "PLACEHOLDER Full Name",
  "jobTitle": "PLACEHOLDER role",
  "worksFor": { "@id": "https://example.com/#organization" },
  "url": "https://example.com/about/",
  "knowsAbout": ["PLACEHOLDER topic", "PLACEHOLDER topic"],
  "sameAs": ["https://www.linkedin.com/in/PLACEHOLDER"]
}
```

## 4. Honesty rules for structured data

| Rule | Why |
|---|---|
| Every marked-up fact is visible on the page | Hidden structured data is a guideline violation and grounds for losing rich results entirely |
| Never invent `aggregateRating`, `reviewCount` or `review` | The most heavily policed structured-data fraud — and self-defeating, since an assistant may repeat your fake rating as fact |
| Never mark up a price you do not charge, or an `Offer` for something unavailable | A violation, and a refund dispute waiting to happen |
| Never invent an author | A byline is an accountability claim |
| Never mark up FAQs, events or products that exist only in the markup | See rule 1 |
| `dateModified` changes only when content changes | A bumped date with unchanged content is a fabricated freshness signal |

**The line:** translating true page content into a machine format is technical work. Asserting to a
machine something you would not print on the page is deception — the kind that gets a domain flagged
rather than merely deranked.

## 5. Validation workflow

Run on every new page type once, and after every template change.

1. **Parse check** — paste the JSON into any linter. A trailing comma kills the block silently.
2. **Rich results test** — confirm detected types match intent. Test the **live URL**, not pasted
   code, so you also catch render and robots problems.
3. **Schema validator** (schema.org's) — catches type and property errors the rich-results tool
   ignores because they carry no rich result.
4. **Search Console → Enhancements**, days after launch — the only place you see errors at scale.
5. **Rendered-HTML check** — fetch raw HTML or disable JavaScript; confirm the JSON-LD is in the
   source, not injected later.

**Safe to ignore:** missing `aggregateRating`/`review` (correct when you have none); missing
`priceValidUntil` on an open-ended subscription; optional fields you genuinely lack (`sku`, `gtin`,
`brand` on a service). **Must fix:** unparseable blocks, missing required properties, `@id`
collisions, URLs that 404, non-ISO-8601 dates, markup describing content the page does not contain.

## 6. Canonical URLs

| Rule | Detail |
|---|---|
| Self-referencing canonical on every page | Including the homepage |
| Absolute URLs only | `https://example.com/path/`, never `/path/` |
| One host form, enforced | www or non-www, the other 301-redirected. HTTPS only |
| One trailing-slash convention | The other form redirects, not merely canonicalises |
| No tracking parameters | The canonical never carries `utm_*`, session ids, or sort/filter params |
| Paginated series | Each page self-canonicals; never canonical page 2 to page 1 |
| Syndicated copies | The copy canonicals to your original |
| Canonical = sitemap entry = internal links = `og:url` | Any mismatch splits the signal |

## 7. Metadata, Open Graph and cards

Emit these from one helper so a page cannot ship missing them.

```html
<title>PLACEHOLDER primary keyword — PLACEHOLDER Brand</title>
<meta name="description" content="PLACEHOLDER 140-155 characters: one benefit, one specific, one reason to click.">
<link rel="canonical" href="https://example.com/path/">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:site_name" content="PLACEHOLDER Brand">
<meta property="og:title" content="PLACEHOLDER share title">
<meta property="og:description" content="PLACEHOLDER share description.">
<meta property="og:url" content="https://example.com/path/">
<meta property="og:image" content="https://example.com/og/path.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="PLACEHOLDER description of the image content.">
<meta property="og:locale" content="en_GB">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="PLACEHOLDER share title">
<meta name="twitter:description" content="PLACEHOLDER share description.">
<meta name="twitter:image" content="https://example.com/og/path.png">
```

| Element | Rule |
|---|---|
| `<title>` | ~50-60 characters, one primary keyword per URL, brand at the end or omitted when long |
| `description` | ~140-155 characters. Not a ranking factor — it is ad copy for the result |
| `og:type` | `website` for pages, `article` for posts (then add `article:published_time`) |
| `og:image` | 1200×630, absolute URL, under ~1 MB, readable at thumbnail size |
| `og:image:alt` | Required for accessibility; describe the image, not the page |
| `robots` meta | `noindex,follow` on thank-you pages, internal search results, thin tag archives |
| Locale | Set it. Add `hreflang` only if you genuinely run multiple locales |

**Per-page social images.** Generate them from a template — fixed background, logo, page title as
large text, category label — rather than designing each one, and ship one branded fallback. Never let
a page render a card with no image; platforms show a grey box and it reads as broken.

## 8. Sitemaps

**In it:** every canonical, indexable, 200-status URL you want in search.

**Never in it:** private, authenticated, account, checkout or admin routes; anything `noindex`,
redirected or 404; non-canonical variants and parameterised URLs; staging hostnames (a sitemap built
on staging and shipped to production is a classic leak); drafts and scheduled content.

Generate it from the registry (§12), never by hand. Make `<lastmod>` truthful — a sitemap where every
URL changed today is ignored. Split into a sitemap index past a few thousand URLs. Reference it from
`robots.txt` with the **live** absolute domain, submit it in Google Search Console and Bing Webmaster
Tools, then watch discovered-vs-indexed counts weekly for the first month.

## 9. robots.txt

Allow the crawlers you want, disallow what must stay private, point at the sitemap. Fillable version:
[robots.txt.example](../templates/robots.txt.example).

```
# Search + AI answer crawlers
User-agent: Googlebot
User-agent: Bingbot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: PerplexityBot
User-agent: ClaudeBot
User-agent: Google-Extended
Allow: /

# Training-corpus crawlers — decide via the trade-off in 12-geo-ai-search.md §9
User-agent: GPTBot
User-agent: CCBot
Allow: /

# Everyone else
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /account/
Disallow: /checkout/
Disallow: /api/

Sitemap: https://example.com/sitemap.xml
```

| Rule | Detail |
|---|---|
| Agent names change | Re-check published agent lists a few times a year |
| `robots.txt` is not security | It hides nothing. Anything genuinely private needs authentication |
| Never `Disallow` a page you want deindexed | Blocking the crawl prevents it seeing your `noindex`. Allow the crawl, serve `noindex` |
| Never block CSS or JS | Rendering-based evaluation needs them |
| Verify the `Sitemap:` line | Live domain, not a host or staging URL |
| Test after every deploy | A blanket `Disallow: /` shipped from a staging config is the most expensive one-line mistake here |

## 10. `llms.txt` layout

A short markdown brief at `https://example.com/llms.txt`, generated from the registry rather than
typed. Fillable version: [llms.txt.example](../templates/llms.txt.example).

```markdown
# PLACEHOLDER Brand
> PLACEHOLDER one-line descriptor: what it is, for whom.

PLACEHOLDER canonical entity paragraph, 40-60 words, identical to the Organization schema
description, the About page, and every third-party profile.

## What this is not
- Not PLACEHOLDER common misconception
- Not PLACEHOLDER adjacent category people confuse it with

## Best pages
- [What it does](https://example.com/product/): PLACEHOLDER one line
- [Pricing](https://example.com/pricing/): PLACEHOLDER one line
- [Glossary](https://example.com/glossary/): definitions of the core terms

## Key concepts
- **PLACEHOLDER Framework Name**: PLACEHOLDER one-line definition, verbatim across the site.

## Contact
General: hello@example.com | Press: press@example.com | Last updated: 2026-03-02
```

## 11. IndexNow

A ping protocol telling participating engines a URL changed, instead of waiting for a recrawl.
Generate a long hex key, host it as plain text at `https://example.com/<key>.txt` containing only the
key, then POST on publish or update:

```json
{
  "host": "example.com",
  "key": "PLACEHOLDER_KEY",
  "keyLocation": "https://example.com/PLACEHOLDER_KEY.txt",
  "urlList": ["https://example.com/new-page/", "https://example.com/updated-page/"]
}
```

Ping real changes only — spamming unchanged URLs is ignored at best. It does not cover every engine,
so keep submitting the sitemap in Search Console regardless.

## 12. Derive everything from one registry

**What it is.** A single machine-readable list of pages — slug, title, description, type, primary
keyword, dates, and an "include in `llms.txt`" flag — from which sitemap, metadata, JSON-LD,
breadcrumbs, internal links and `llms.txt` are all generated.

**Mechanism.** Every one of those artefacts encodes the same facts. Maintained separately they drift
within weeks: a page in the sitemap but not the nav, an `llms.txt` link to a moved URL, a canonical
pointing at an old slug. Derived from one source, drift is structurally impossible.

| Artefact | Derived how |
|---|---|
| `sitemap.xml` | Map the registry, filtering out `noindex` entries |
| Page metadata | One `buildMetadata(entry)` returning title, description, canonical, OG, Twitter |
| JSON-LD graph | One builder per node type, selected by the entry's `type` field |
| Breadcrumbs | Computed from the slug's path segments plus registry titles |
| Internal links / footer columns | Filter the registry by section or tag |
| `llms.txt` | Filter the registry to flagged highlights |

**Acceptance test:** adding a page is one edit — add the entry, write the content. If it also
requires touching the sitemap, the footer and `llms.txt` by hand, the pattern is not in place.

### 12.1 Execution note — code repo (Next.js, Astro, SvelteKit or similar)

- One `lib/seo.*` holding `SITE_URL`, `SITE_NAME`, the entity paragraph, `absoluteUrl(path)` and
  `buildMetadata()`. Every page's tags come from that helper — no page writes its own.
- One `lib/schema.*` with a pure function per node type (`organization()`, `website()`, `webPage()`,
  `article()`, `product()`, `faqPage()`, `breadcrumb()`, `definedTerm()`, `person()`) plus a
  `<JsonLd graph={[...]}/>` component, all referencing one Organization `@id` constant.
- Content is typed data, not hand-written markup: a page object with `slug`, `metaTitle`,
  `metaDescription`, `h1`, `directAnswer`, `sections[]`, `faq[]`, `related[]`, `schemaKind`, rendered
  by one template. `faq[]` feeds both the visible accordion and `FAQPage` schema.
- Framework-native sitemap and robots routes read the registry directly; per-page social images come
  from a shared image template at route level.
- CI check: fail the build if an entry lacks a title, description or canonical, or if `llms.txt`
  references a slug that no longer exists.

### 12.2 Execution note — WordPress

- Titles, meta descriptions, canonicals, OG/Twitter tags, `Organization`, `WebSite`, `WebPage` and
  `BreadcrumbList` come from an SEO plugin. Configure the site-wide entity fields once — that is your
  Organization node.
- Add the nodes the plugin omits (`FAQPage`, `Service`, `DefinedTerm`, `Product`/
  `SoftwareApplication`, `Person`) via a code-snippet plugin or child theme hooked on `wp_head`, and
  reference the plugin's existing Organization `@id` so you keep **one** graph rather than two
  competing ones. Read the emitted `@id` out of the page source before hardcoding it.
- The registry equivalent is the post/page list plus custom fields for "primary keyword" and "include
  in llms.txt". WordPress does not serve arbitrary root files by default: drop `llms.txt` at the web
  root over SFTP, or add a rewrite that serves it from a generated template.
- `robots.txt` is virtual by default. Override it via the SEO plugin's file editor or a `robots_txt`
  filter to add the crawler allowlist and fix the `Sitemap:` line — it frequently points at a host or
  staging domain.
- Use a glossary custom post type for `DefinedTerm` entries so the archive can generate the
  `DefinedTermSet`.
- **Verify logged out.** Caching and optimisation plugins are bypassed for logged-in administrators,
  so a page can look perfect to you and ship broken to visitors. Check every template change in a
  private window or with a plain HTTP fetch.

## Apply it

- [ ] Every page emits exactly one JSON-LD block containing one `@graph`, and every graph references the same Organization `@id`
- [ ] The Organization `description` is the canonical entity paragraph, identical to About, `llms.txt` and every off-site profile
- [ ] Each page uses the cookbook node for its type, with all required properties filled from real data
- [ ] `speakable` on every important page points at the selector that actually wraps the direct-answer block
- [ ] No rating, review, price, author, event or FAQ exists in markup that is not true and visible on the page
- [ ] Every page has a self-referencing absolute canonical; host form, protocol and trailing-slash convention are enforced by redirect
- [ ] Canonical, sitemap entry, internal links and `og:url` are the same string for every page
- [ ] Title, description, canonical, OG and Twitter tags come from one helper, and every page has a social image with alt text
- [ ] The sitemap is generated, free of private/redirected/`noindex` URLs and staging hostnames, and submitted to Google and Bing
- [ ] `robots.txt` names search and AI crawlers explicitly, disallows private routes, blocks no CSS or JS, and points at the live sitemap
- [ ] `llms.txt` is generated and carries the entity paragraph, the "what this is not" list, best pages and framework definitions
- [ ] IndexNow key is hosted and pinged on real content changes only
- [ ] Sitemap, metadata, internal links, breadcrumbs and `llms.txt` all derive from one registry — adding a page is a single edit
- [ ] Every page type passed the rich results test and the schema validator on the live URL, with only known-safe warnings left

## Related

- [SEO fundamentals](./11-seo-fundamentals.md) — the keyword map and architecture this wires up
- [GEO and AI search](./12-geo-ai-search.md) — direct-answer blocks, entity consistency, the crawler trade-off
- [Positioning and category](../brand/01-positioning-and-category.md) — the category claim your Organization description states
- [Voice, messaging and copywriting](../brand/03-voice-messaging-and-copywriting.md) — titles and descriptions that read as human
- [Page architecture and section recipes](../build/08-page-architecture-and-section-recipes.md) — the page shapes these types map onto
- [Design system and tokens](../build/09-design-system-and-tokens.md) — the social-image template and brand assets
- [Conversion audit checklist](../build/10-conversion-audit-checklist.md) — the pre-ship gate that includes this checklist
- [Measurement and experimentation](../ops/14-measurement-and-experimentation.md) — Search Console and analytics wiring
- [Launch checklist and build order](../ops/15-launch-checklist-and-build-order.md) — when in the build this ships
- [Prompt pack](../ops/16-prompt-pack.md) — prompts for generating schema and metadata from a page brief
- [Page brief template](../templates/page-brief.md) — where a page's type, keyword and FAQ are specified
- [llms.txt example](../templates/llms.txt.example) — fillable version of §10
- [robots.txt example](../templates/robots.txt.example) — fillable version of §9
