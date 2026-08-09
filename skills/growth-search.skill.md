---
name: growth-search
description: "Make a site rank in classic search AND get cited by AI answer engines — keyword architecture, on-page, structured data, llms.txt, indexing and measurement. Use for any SEO, GEO, schema, sitemap, robots or 'get us cited by ChatGPT' work on any stack."
user-invocable: true
triggers:
  - "SEO"
  - "GEO"
  - "rank for"
  - "schema"
  - "structured data"
  - "JSON-LD"
  - "llms.txt"
  - "sitemap"
  - "get indexed"
  - "AI search"
  - "cited by ChatGPT"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - WebFetch
---

# Growth search (SEO + GEO)

Win two surfaces at once: classic search and AI answer engines. The GEO win is being the clearest, most
quotable, most consistent machine-readable source on a topic. Stack-agnostic.

## Knowledge base

Set `$GF` to the pack root (default: `~/Projects/growth-fundamentals`).

1. `$GF/search/11-seo-fundamentals.md` — intent, keyword architecture, on-page, technical, indexing, links
2. `$GF/search/12-geo-ai-search.md` — direct answers, chunk-level writing, named frameworks, entity
   consistency, llms.txt, measurement
3. `$GF/search/13-schema-and-technical-wiring.md` — the JSON-LD cookbook, canonical/OG, sitemap, robots,
   IndexNow, the single-registry pattern
4. `$GF/ops/14-measurement-and-experimentation.md` — what to instrument and how to read it
5. The project's own page brief (`templates/page-brief.md` filled in) before writing any page

## Step 0 — detect the stack first

It decides the whole execution. `curl -s <site>` and look for framework markers; check `/robots.txt`,
`/sitemap.xml`, `/llms.txt`, and whether JSON-LD is already present. Then confirm the edit channel: a code
repo, a CMS REST API, a CMS UI, or "the human applies the spec". Branch accordingly — the method is
identical, only the mechanics change.

## The one rule that drives every page

**Capture the keyword, reframe the category.** Title, meta, H1 and schema capture the literal term people
actually search; the body holds the brand frame and never parrots the keyword. **One primary keyword per
URL** — decide it before writing a word.

## Procedure

1. **Audit** — pull the live sitemap, robots, llms.txt and a few rendered pages. Map URL → primary
   keyword. List the gaps before building anything.
2. **Architecture** — commercial + pain/problem + audience + comparison + glossary + an informational blog
   that links *up* to the commercial pages. No two pages compete for the same term.
3. **GEO layer on every important page** — a self-contained, quotable direct answer in the first ~100
   words; named original frameworks repeated verbatim across site, llms.txt and PR; a FAQ that feeds
   FAQPage schema from one source; definitions in a glossary.
4. **Schema** — one connected graph per page via a single Organization `@id`. Real data only; never invent
   ratings or reviews.
5. **Wiring** — sitemap + llms.txt + robots (AI-crawler allowlist, private routes disallowed) + canonical
   + OG/Twitter + per-page social image. Derive all of it from one registry so nothing drifts.
6. **Index** — submit the sitemap in Search Console and Bing, request indexing on the priority URLs, wire
   IndexNow, re-ping on every content deploy.
7. **Measure** — first-party analytics, Search Console, plus a scheduled prompt panel for AI answer
   share-of-voice. Classic rank tracking does not measure GEO.
8. **Verify before claiming done** (below).

## Safety rails

No invented metrics, reviews, ratings, testimonials or urgency. One primary keyword per URL; the body
reads for humans. Comparison pages stay fair and factual. Never put private/app/account/API routes in the
sitemap. Structured data must reflect what is actually on the page. For regulated categories (finance,
health, legal), add the required disclaimers and use only real, sourced numbers.

## Verification (the gate)

Each page owns exactly one primary keyword in title/meta/H1 with the brand frame in the body; has a
quotable direct answer in the first 100 words; its JSON-LD validates clean with the correct type and no
invented ratings; canonical + OG + breadcrumbs present; it is server-rendered; it is in the sitemap and (if
important) llms.txt; and it links to the right neighbours. Site-level: one source drives sitemap and
llms.txt, robots allows the AI crawlers, and Search Console / Bing / IndexNow all have the sitemap.

## Apply it

- [ ] `$GF` points at a readable copy of the pack, and the stack was detected before anything was edited.
- [ ] The edit channel is confirmed: repo, CMS API, CMS UI, or a spec a human applies.
- [ ] Every URL maps to exactly one primary keyword, decided before a word was written.
- [ ] Title, meta, H1 and schema capture the literal term; the body holds the brand frame without parroting it.
- [ ] Every important page opens with a self-contained, quotable direct answer in the first ~100 words.
- [ ] Named frameworks are used verbatim and identically across site, llms.txt, and schema.
- [ ] JSON-LD forms one connected graph per page through a single Organization `@id`, with real data only.
- [ ] Sitemap, llms.txt, robots, canonicals and OG images all derive from one registry, so none can drift.
- [ ] No private, app, account, or API route appears in the sitemap or llms.txt.
- [ ] The sitemap is submitted, priority URLs are requested, IndexNow re-pings on deploy.
- [ ] Measurement covers both surfaces — Search Console for classic, a prompt panel for AI share-of-voice.
- [ ] Every item in the verification gate above passes before anything is called done.

## Related

- [README.md](README.md) — installing this skill and its sibling
- [../00-START-HERE.md](../00-START-HERE.md) — the decisions and honesty rails this skill inherits
- [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md) — intent, architecture, on-page, indexing
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — direct answers, named frameworks, entity consistency
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — the JSON-LD cookbook and wiring
- [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md) — what to instrument
- [../templates/page-brief.md](../templates/page-brief.md) — the per-page spec to fill before writing
- [../templates/llms.txt.example](../templates/llms.txt.example) · [../templates/robots.txt.example](../templates/robots.txt.example) — the two files to ship
- [brand-web-design.skill.md](brand-web-design.skill.md) — the design and conversion counterpart
