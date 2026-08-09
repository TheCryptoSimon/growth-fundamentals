# Schema and Technical Wiring

The machine-readable layer: structured data, canonicals, metadata, sitemaps, robots, `llms.txt`, and
the registry pattern that stops them drifting apart. Read this when you are building or auditing
pages, after the content decisions in [SEO fundamentals](./11-seo-fundamentals.md) and
[GEO](./12-geo-ai-search.md). Everything here is copy-and-adapt; replace every `PLACEHOLDER`.

---

## 0. What this layer buys you

| Consumer | What it reads | What you get |
|---|---|---|
| Search engines | JSON-LD, canonicals, sitemap, robots | Rich results, correct indexing, no duplicate-content confusion |
| AI answer engines | Clean HTML, JSON-LD, `speakable`, `llms.txt` | Unambiguous facts to extract and attribute to you |
| Social platforms | Open Graph, Twitter cards | A share card that looks deliberate rather than broken |
| Your own tooling | The page registry | Sitemap, internal links, metadata, and `llms.txt` generated, not hand-maintained |

**The rule that governs all of it:** structured data describes what is *on the page*. It is a
translation layer, never an addition. If a fact is not visible to a human reading the page, it does
not belong in the markup.

## 1. One connected graph per page

**What it is.** Every page emits a single `<script type="application/ld+json">` containing a
`@graph` array whose nodes cross-reference each other by `@id`, and every page's graph points at the
*same* Organization `@id`.

**Mechanism.** Independent, unlinked snippets read as unrelated assertions. A connected graph tells
a parser "this article, on this website, published by this organization, whose profiles are these"
in one pass — which is exactly the entity-consolidation problem described in
[GEO §5](./12-geo-ai-search.md).

**The `@id` convention.** Use URL fragments on your canonical domain, and never change them:

| Node | `@id` |
|---|---|
| Organization | `https://example.com/#organization` |
| WebSite | `https://example.com/#website` |
| A page | `https://example.com/path/#webpage` |
| A page's primary image | `https://example.com/path/#primaryimage` |
| A person | `https://example.com/about/#person-firstname` |
| A product | `https://example.com/product/#product` |

**Rules:**

1. One `<script>` block per page containing one `@graph`. Not five separate blocks.
2. Define Organization and WebSite once in a site-wide layout; reference them by `@id` elsewhere.
3. Every page has a `WebPage` node with `isPartOf` → WebSite and `about`/`publisher` → Organization.
4. Anything with a `mainEntityOfPage` points it at the page's `@id`.
5. Never emit the same `@id` with different content on different pages.

## 2. Page type → JSON-LD cookbook

| Page type | Primary node | Also emit | Required properties | Recommended |
|---|---|---|---|---|
| Homepage | `Organization` + `WebSite` | `WebPage`, `FAQPage` if FAQs shown | name, url, logo | description, sameAs, contactPoint, potentialAction (SearchAction) |
| Product / commercial | `Product` or `SoftwareApplication` | `WebPage`, `BreadcrumbList`, `FAQPage` | name, description, offers (price, currency, availability) | brand, image, applicationCategory, operatingSystem |
| Article / blog post | `Article` (or `BlogPosting`) | `WebPage`, `BreadcrumbList` | headline, image, datePublished, author, publisher | dateModified, articleSection, wordCount, mainEntityOfPage |
| Service page | `Service` | `WebPage`, `BreadcrumbList`, `FAQPage` | name, provider, serviceType, areaServed | description, offers, audience |
| Glossary term | `DefinedTerm` | `WebPage`, `BreadcrumbList` | name, description, inDefinedTermSet | termCode, url |
| Glossary index | `DefinedTermSet` | `WebPage`, `BreadcrumbList` | name, url | hasDefinedTerm[], description |
| FAQ page or section | `FAQPage` | `WebPage` | mainEntity[] with Question → acceptedAnswer | — |
| How-to / tutorial | `HowTo` | `Article`, `WebPage`, `BreadcrumbList` | name, step[] (HowToStep with name + text) | totalTime, supply, tool, image per step |
| Video | `VideoObject` | on its host page's graph | name, description, thumbnailUrl, uploadDate | duration, contentUrl or embedUrl, transcript |
| Event | `Event` | `WebPage`, `BreadcrumbList` | name, startDate, location, eventAttendanceMode | endDate, offers, performer, organizer |
| Person / author bio | `Person` | `WebPage`, `BreadcrumbList` | name | jobTitle, worksFor (→ Org `@id`), sameAs, image, knowsAbout |
| Local business | `LocalBusiness` (or a subtype) | `WebPage`, `BreadcrumbList` | name, address, telephone | openingHoursSpecification, geo, priceRange, hasMap |
| Any non-home page | `BreadcrumbList` | — | itemListElement[] with position, name, item | — |

**Choosing between `Product` and `SoftwareApplication`:** software with a licence or subscription →
`SoftwareApplication` (optionally also typed as `Product`). Physical goods → `Product`. A delivered
human service → `Service`. Do not stack all three hoping one sticks.

## 3. Ready-to-adapt snippets

Replace `example.com`, `PLACEHOLDER Brand`, dates, and prices with real values. Delete any property
you cannot fill honestly — an absent property is fine, a guessed one is not.

### 3.1 Organization (site-wide, define once)

```json
{
  "@type": "Organization",
  "@id": "https://example.com/#organization",
  "name": "PLACEHOLDER Brand",
  "alternateName": "PLACEHOLDER",
  "url": "https://example.com/",
  "logo": {
    "@type": "ImageObject",
    "@id": "https://example.com/#logo",
    "url": "https://example.com/img/logo-512.png",
    "width": 512,
    "height": 512,
    "caption": "PLACEHOLDER Brand"
  },
  "image": { "@id": "https://example.com/#logo" },
  "description": "PLACEHOLDER Brand is a CATEGORY for AUDIENCE. It MECHANISM, and DIFFERENTIATOR.",
  "foundingDate": "2026",
  "email": "hello@example.com",
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "customer support",
    "email": "support@example.com",
    "availableLanguage": ["en"]
  },
  "sameAs": [
    "https://www.linkedin.com/company/PLACEHOLDER",
    "https://github.com/PLACEHOLDER",
    "https://x.com/PLACEHOLDER"
  ]
}
```

`description` must be the exact entity paragraph from [GEO §5](./12-geo-ai-search.md). `sameAs`
lists only profiles you control and that link back.

### 3.2 WebSite with SearchAction

Include `potentialAction` **only if** the URL pattern really performs a site search.

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
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "https://example.com/search?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  }
}
```

### 3.3 WebPage with speakable

`speakable` points at the direct-answer block. Use a CSS selector that exists in the rendered HTML.

```json
{
  "@type": "WebPage",
  "@id": "https://example.com/how-it-works/#webpage",
  "url": "https://example.com/how-it-works/",
  "name": "PLACEHOLDER page title",
  "description": "PLACEHOLDER meta description, same string as the meta tag.",
  "isPartOf": { "@id": "https://example.com/#website" },
  "about": { "@id": "https://example.com/#organization" },
  "primaryImageOfPage": { "@id": "https://example.com/how-it-works/#primaryimage" },
  "datePublished": "2026-01-15T09:00:00+00:00",
  "dateModified": "2026-03-02T11:30:00+00:00",
  "inLanguage": "en",
  "breadcrumb": { "@id": "https://example.com/how-it-works/#breadcrumb" },
  "speakable": {
    "@type": "SpeakableSpecification",
    "cssSelector": [".direct-answer"]
  }
}
```

### 3.4 BreadcrumbList

Positions start at 1. The trail must match the visible breadcrumb and the URL hierarchy.

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

The last item carries no `item` — it is the current page.

### 3.5 Article

```json
{
  "@type": "Article",
  "@id": "https://example.com/blog/POST-SLUG/#article",
  "headline": "PLACEHOLDER headline, under 110 characters",
  "description": "PLACEHOLDER standfirst, one sentence.",
  "image": ["https://example.com/img/POST-SLUG-1200x630.jpg"],
  "datePublished": "2026-02-10T08:00:00+00:00",
  "dateModified": "2026-02-18T14:20:00+00:00",
  "author": { "@id": "https://example.com/about/#person-alex" },
  "publisher": { "@id": "https://example.com/#organization" },
  "mainEntityOfPage": { "@id": "https://example.com/blog/POST-SLUG/#webpage" },
  "isPartOf": { "@id": "https://example.com/#website" },
  "articleSection": "PLACEHOLDER pillar",
  "inLanguage": "en"
}
```

`author` must be a real named `Person` or the `Organization`. Do not invent a byline.

### 3.6 Product / SoftwareApplication with a real Offer

```json
{
  "@type": ["SoftwareApplication", "Product"],
  "@id": "https://example.com/pricing/#product",
  "name": "PLACEHOLDER Brand",
  "description": "PLACEHOLDER what it does, for whom.",
  "applicationCategory": "BusinessApplication",
  "operatingSystem": "Web",
  "url": "https://example.com/pricing/",
  "image": "https://example.com/img/product-1200x630.jpg",
  "brand": { "@id": "https://example.com/#organization" },
  "offers": {
    "@type": "Offer",
    "price": "29.00",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "url": "https://example.com/pricing/",
    "priceValidUntil": "2026-12-31"
  }
}
```

**No `aggregateRating`, no `review`, unless you have real, verifiable, user-submitted reviews on
that page.** A product with real offers and no rating validates cleanly; the "no rating" notice in
testing tools is expected and honest. For multiple tiers use an `AggregateOffer` with
`lowPrice`/`highPrice`/`offerCount`, or list several `Offer` objects.

### 3.7 FAQPage

Generated from the same array that renders the visible FAQ.

```json
{
  "@type": "FAQPage",
  "@id": "https://example.com/pricing/#faq",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "PLACEHOLDER question exactly as a person would ask it?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "PLACEHOLDER 40-80 word self-contained answer, identical to the visible text."
      }
    },
    {
      "@type": "Question",
      "name": "PLACEHOLDER second, genuinely different question?",
      "acceptedAnswer": { "@type": "Answer", "text": "PLACEHOLDER answer." }
    }
  ]
}
```

### 3.8 DefinedTerm and DefinedTermSet

```json
{
  "@type": "DefinedTerm",
  "@id": "https://example.com/glossary/TERM-SLUG/#term",
  "name": "PLACEHOLDER Term",
  "description": "PLACEHOLDER 40-60 word standalone definition, identical to the on-page paragraph.",
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
  "description": "Definitions of the core terms in PLACEHOLDER category.",
  "hasDefinedTerm": [
    { "@id": "https://example.com/glossary/TERM-SLUG/#term" },
    { "@id": "https://example.com/glossary/OTHER-TERM/#term" }
  ]
}
```

Use the same pattern for a named framework: give it a `DefinedTerm` node so the coined name has a
machine-readable definition attached to your entity.

### 3.9 Person

```json
{
  "@type": "Person",
  "@id": "https://example.com/about/#person-alex",
  "name": "PLACEHOLDER Full Name",
  "jobTitle": "PLACEHOLDER role",
  "worksFor": { "@id": "https://example.com/#organization" },
  "url": "https://example.com/about/",
  "image": "https://example.com/img/team-alex.jpg",
  "knowsAbout": ["PLACEHOLDER topic", "PLACEHOLDER topic"],
  "sameAs": ["https://www.linkedin.com/in/PLACEHOLDER"]
}
```

### 3.10 Assembling a page

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { /* Organization — from the site layout */ },
    { /* WebSite */ },
    { /* WebPage with speakable */ },
    { /* BreadcrumbList */ },
    { /* the page-type node: Article | Product | Service | DefinedTerm | ... */ },
    { /* FAQPage, if the page shows FAQs */ }
  ]
}
</script>
```

## 4. The honesty rules for structured data

| Rule | Why |
|---|---|
| Every marked-up fact is visible on the page | Hidden structured data is a guideline violation and grounds for losing rich results entirely |
| Never invent `aggregateRating`, `reviewCount`, or `review` | This is the most common structured-data fraud and the most heavily policed. It is also self-defeating: an assistant may repeat your fake rating as fact |
| Never mark up a price you do not charge | Price mismatch between markup and page is both a violation and a refund dispute |
| Never mark up an `Offer` for something unavailable | `availability` must reflect reality |
| Never invent an author | A byline is an accountability claim |
| Never mark up FAQs that only exist in the markup | See rule 1 |
| Never mark up an `Event` that is not scheduled | Same |
| `dateModified` changes only when content changes | A bumped date with unchanged content is a fabricated freshness signal |

**The line:** translating true page content into a machine format is technical work. Asserting to a
machine something you would not print on the page is deception, and it is the kind that gets a
domain flagged rather than merely deranked.

## 5. Validation workflow

Run this on every new page type once, and on every template change.

1. **Parse check.** Paste the JSON into any JSON linter. A trailing comma kills the whole block
   silently.
2. **Rich results test** (Google's tool). Confirm the eligible types detected match what you
   intended. Test the **live URL**, not just pasted code, so you also catch render and robots
   problems.
3. **Schema validator** (schema.org's validator). Catches type and property errors that the rich
   results tool ignores because they are not tied to a rich result.
4. **Search Console → Enhancements**, a few days after launch. This is the only place you see
   errors at scale across the site.
5. **Rendered-HTML check.** View the page as a bot would — fetch the raw HTML or disable JavaScript
   — and confirm the JSON-LD is present in the source, not injected later.

**Warnings that are safe to ignore:**

- "Missing field `aggregateRating`" / "`review`" — correct and honest when you have no real reviews.
- "Missing field `priceValidUntil`" on an open-ended subscription.
- Optional recommended fields you genuinely do not have (`sku`, `gtin`, `brand` on a service).
- "Missing `logo` dimensions" if the logo URL resolves and is square.

**Errors you must fix:** invalid or missing required properties, an unparseable block, a `@id`
collision, a URL that 404s, a date in the wrong format (use ISO 8601 with a timezone), or
markup describing content the page does not contain.

## 6. Canonical URLs

**What it is.** A `<link rel="canonical">` on every page declaring the single official URL for that
content.

| Rule | Detail |
|---|---|
| Self-referencing canonical on every page | Including the homepage |
| Absolute URLs only | `https://example.com/path/`, never `/path/` |
| Pick one host form and enforce it | www or non-www, and redirect the other with a 301 |
| HTTPS only | Redirect all HTTP |
| Pick one trailing-slash convention | And make the other redirect, not merely canonicalise |
| Strip tracking parameters | The canonical never contains `utm_*`, session ids, or sort/filter params |
| Paginated series | Each page self-canonicals; do not canonical page 2 to page 1 |
| Cross-domain syndication | The syndicated copy canonicals to your original |
| Canonical, sitemap entry, internal links, and OG `url` must be the same string | Any mismatch is a split signal |

## 7. Metadata, Open Graph, and cards

Emit these from one helper so a page cannot ship missing them.

```html
<title>PLACEHOLDER primary keyword — PLACEHOLDER Brand</title>
<meta name="description" content="PLACEHOLDER 140-155 characters, one benefit, one specific, one reason to click.">
<link rel="canonical" href="https://example.com/path/">
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1">

<meta property="og:type" content="website">
<meta property="og:site_name" content="PLACEHOLDER Brand">
<meta property="og:title" content="PLACEHOLDER share title">
<meta property="og:description" content="PLACEHOLDER share description, may differ from meta description.">
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
| `<title>` | ~50–60 characters. One primary keyword per URL. Brand at the end, or omitted on long titles |
| `description` | ~140–155 characters. Not a ranking factor; it is ad copy for the result |
| `og:type` | `website` for pages, `article` for posts (then add `article:published_time`) |
| `og:image` | 1200×630, under ~1 MB, absolute URL, readable at thumbnail size |
| `og:image:alt` | Required for accessibility; describe the image, not the page |
| `robots` meta | `noindex,follow` on thank-you pages, internal search results, and thin tag archives |
| Locale | Set it; add `hreflang` only if you genuinely run multiple locales |

**Per-page social images.** Generate them from a template rather than designing each one: a fixed
background, the logo, the page title as large text, and a category label. Ship one branded fallback
for anything without a generated image. Never let a page render a card with no image — platforms
show a bare grey box and it reads as broken.

## 8. Sitemaps

**What belongs in it:** every canonical, indexable, 200-status URL you want in search.

**What must never be in it:**

- Private, authenticated, account, checkout, or admin routes
- Anything `noindex`, redirected, or 404
- Non-canonical variants, parameterised URLs, or paginated duplicates
- Staging hostnames (a sitemap generated on staging and shipped to production is a classic leak)
- Draft or scheduled content

**Rules:**

- Generate it from the page registry (§12) — never hand-maintain.
- Use `<lastmod>` and make it truthful; a sitemap where every URL changed today is ignored.
- Split into a sitemap index once you pass a few thousand URLs, or to separate posts from pages.
- Reference it from `robots.txt` with the **live** absolute domain.
- Submit it in Google Search Console and Bing Webmaster Tools, then check the "discovered vs
  indexed" counts weekly for the first month.

## 9. robots.txt

Allow the crawlers you want, disallow the routes that must stay private, and point at the sitemap.
A fillable version is at [robots.txt.example](../templates/robots.txt.example).

```
# Search crawlers
User-agent: Googlebot
Allow: /

User-agent: Bingbot
Allow: /

# AI answer / assistant crawlers
User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Google-Extended
Allow: /

# Training-corpus crawlers — see the trade-off in 12-geo-ai-search.md §9
User-agent: GPTBot
Allow: /

User-agent: CCBot
Allow: /

# Everyone else
User-agent: *
Allow: /
Disallow: /admin/
Disallow: /account/
Disallow: /checkout/
Disallow: /api/
Disallow: /*?utm_

Sitemap: https://example.com/sitemap.xml
```

| Rule | Detail |
|---|---|
| Agent names change | Re-check the published agent lists a few times a year and update |
| `robots.txt` is not security | It hides nothing. Anything genuinely private needs authentication |
| Never `Disallow` a page you want deindexed | Blocking it prevents the crawler seeing your `noindex`. Allow the crawl, serve `noindex` |
| Never block CSS or JS | Rendering-based evaluation needs them |
| Verify the `Sitemap:` line | It must be the live domain, not a host or staging URL |
| Test after every deploy | A blanket `Disallow: /` shipped from a staging config is the most expensive one-line mistake in this document |

## 10. `llms.txt` layout

A short markdown brief at `https://example.com/llms.txt`. Generated from the registry, not typed by
hand. Full fillable version: [llms.txt.example](../templates/llms.txt.example).

```markdown
# PLACEHOLDER Brand

> PLACEHOLDER one-line descriptor: what it is, for whom.

PLACEHOLDER canonical entity paragraph — 40-60 words, identical to the Organization
schema description, the About page, and every third-party profile.

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
- General: hello@example.com
- Press: press@example.com

Last updated: 2026-03-02
```

## 11. IndexNow

**What it is.** A ping protocol that tells participating engines a URL changed, instead of waiting
for a recrawl.

1. Generate a key (a long hex string) and host it as plain text at
   `https://example.com/<key>.txt`, containing only the key.
2. On publish or update, POST to the IndexNow endpoint:

```json
{
  "host": "example.com",
  "key": "PLACEHOLDER_KEY",
  "keyLocation": "https://example.com/PLACEHOLDER_KEY.txt",
  "urlList": ["https://example.com/new-page/", "https://example.com/updated-page/"]
}
```

3. Ping only real changes. Spamming it with unchanged URLs gets ignored at best.
4. It does not cover every engine — keep submitting the sitemap in Search Console regardless.

## 12. Derive everything from one registry

**What it is.** A single machine-readable list of pages — slug, title, description, type, primary
keyword, publish/modified dates, whether it belongs in `llms.txt` — from which the sitemap,
metadata, internal-link modules, breadcrumbs, and `llms.txt` are all generated.

**Mechanism.** Every one of those artefacts encodes the same facts. Maintained separately, they
drift within weeks: a page appears in the sitemap but not the nav, `llms.txt` links a URL that moved,
a canonical points at an old slug. Derived from one source, drift is structurally impossible.

**How to apply:**

| Artefact | Derived how |
|---|---|
| `sitemap.xml` | Map the registry, filtering out `noindex` entries |
| Page metadata | One `buildMetadata(entry)` helper returning title, description, canonical, OG, Twitter |
| JSON-LD graph | One builder per schema type, selected by the entry's `type` field |
| Breadcrumbs | Computed from the slug's path segments plus the registry's titles |
| Internal-link modules / footer columns | Filter the registry by section or tag |
| `llms.txt` | Filter the registry to entries flagged as highlights |

**Acceptance test:** adding a page must be one edit — add the entry, write the content. If adding a
page requires touching the sitemap, the footer, and `llms.txt` by hand, the pattern is not in place.

### 12.1 Execution note — code repo (Next.js, Astro, SvelteKit, or similar)

- One `lib/seo.*` holding `SITE_URL`, `SITE_NAME`, the entity paragraph, `absoluteUrl(path)`, and
  `buildMetadata()`. Every page's metadata comes from that helper — no page writes its own tags.
- One `lib/schema.*` with a pure function per node type (`organization()`, `website()`, `webPage()`,
  `article()`, `product()`, `faqPage()`, `breadcrumb()`, `definedTerm()`, `person()`) plus a
  `<JsonLd graph={[...]}/>` component. All of them reference one Organization `@id` constant.
- Content is typed data, not hand-written markup: a page object with `slug`, `metaTitle`,
  `metaDescription`, `h1`, `directAnswer`, `sections[]`, `faq[]`, `related[]`, `schemaKind`, rendered
  by one template. The `faq[]` array feeds both the visible accordion and `FAQPage` schema.
- Framework-native sitemap and robots routes read the registry directly.
- Per-page social images from a shared image template at the route level.
- Add a CI check: fail the build if any registry entry lacks a title, description, or canonical, or
  if `llms.txt` references a slug that no longer exists.

### 12.2 Execution note — WordPress

- Titles, meta descriptions, canonicals, OG/Twitter tags, `Organization`, `WebSite`, `WebPage` and
  `BreadcrumbList` come from an SEO plugin. Configure the site-wide entity fields once — that is
  your Organization node.
- Add the nodes the plugin does not emit (`FAQPage`, `Article` extras, `Service`, `DefinedTerm`,
  `Product`/`SoftwareApplication`, `Person`) with a code-snippet plugin or a child theme, hooked on
  `wp_head`, and reference the plugin's existing Organization `@id` so you keep **one** graph rather
  than two competing ones. Check the emitted `@id` in the page source before hardcoding it.
- The registry equivalent is the post/page list plus a custom field for "include in llms.txt" and
  "primary keyword". Generate `llms.txt` from a scheduled job or a small template rather than typing
  it, since WordPress does not serve arbitrary root files by default — either drop the file at the
  web root over SFTP, or add a rewrite rule that serves it from a template.
- `robots.txt` is virtual by default. Override it via the SEO plugin's file editor or a `robots_txt`
  filter to add the crawler allowlist and correct the `Sitemap:` line — it frequently points at a
  host or staging domain.
- Use a glossary custom post type for `DefinedTerm` entries so the archive can generate the
  `DefinedTermSet`.
- **Verify logged out.** Caching and optimisation plugins are bypassed for logged-in administrators,
  so a page can look perfect to you and ship broken or unstyled to visitors. Check every template
  change in a private window or with a plain HTTP fetch.

## Apply it

- [ ] Every page emits exactly one JSON-LD block containing one `@graph`, and every graph references the same Organization `@id`
- [ ] The Organization `description` is the canonical entity paragraph, identical to About, `llms.txt`, and every off-site profile
- [ ] Each page uses the cookbook type for its page type, with all required properties filled from real data
- [ ] `speakable` on every important page points at the actual selector wrapping the direct-answer block
- [ ] No `aggregateRating`, `review`, price, author, event, or FAQ exists in markup that is not true and visible on the page
- [ ] Every page has a self-referencing absolute canonical; host form, protocol, and trailing-slash convention are enforced by redirect
- [ ] Canonical, sitemap entry, internal links, and `og:url` are the same string for every page
- [ ] Title, description, canonical, OG, and Twitter tags come from one helper, and every page has a social image
- [ ] The sitemap is generated from the registry, contains no private/redirected/`noindex` URLs and no staging hostnames, and is submitted to Google and Bing
- [ ] `robots.txt` names the search and AI crawlers explicitly, disallows private routes, blocks no CSS or JS, and points at the live sitemap URL
- [ ] `llms.txt` exists, is generated, and carries the entity paragraph, the "what this is not" list, best pages, and framework definitions
- [ ] IndexNow key is hosted and pinged on real content changes only
- [ ] Sitemap, metadata, internal links, breadcrumbs and `llms.txt` are all derived from one registry — adding a page is a single edit
- [ ] Every page type passed the rich results test and the schema validator on the live URL, with only known-safe warnings remaining

## Related

- [SEO fundamentals](./11-seo-fundamentals.md) — the keyword map and architecture this wires up
- [GEO and AI search](./12-geo-ai-search.md) — the direct-answer block, entity consistency, and the crawler trade-off
- [Positioning and category](../brand/01-positioning-and-category.md) — the category claim your Organization description states
- [Voice, messaging and copywriting](../brand/03-voice-messaging-and-copywriting.md) — writing titles and descriptions that read as human
- [Page architecture and section recipes](../build/08-page-architecture-and-section-recipes.md) — the page shapes these types map onto
- [Design system and tokens](../build/09-design-system-and-tokens.md) — the social-image template and brand assets
- [Conversion audit checklist](../build/10-conversion-audit-checklist.md) — the pre-ship gate that includes this checklist
- [Measurement and experimentation](../ops/14-measurement-and-experimentation.md) — Search Console and analytics wiring
- [Launch checklist and build order](../ops/15-launch-checklist-and-build-order.md) — when in the build this ships
- [Prompt pack](../ops/16-prompt-pack.md) — prompts for generating schema and metadata from a page brief
- [Page brief template](../templates/page-brief.md) — where a page's type, keyword, and FAQ are specified
- [llms.txt example](../templates/llms.txt.example) — fillable version of §10
- [robots.txt example](../templates/robots.txt.example) — fillable version of §9
