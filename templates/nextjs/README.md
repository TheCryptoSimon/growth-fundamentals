# Next.js execution templates

The App Router version of the machine-readable layer: one registry that every other file
derives from, so the sitemap, `llms.txt`, `robots.txt` and per-page metadata cannot drift
apart. Read [../../search/13-schema-and-technical-wiring.md](../../search/13-schema-and-technical-wiring.md)
first for the method; this folder is only the Next.js mechanics.

| File | Goes at | What it is |
|---|---|---|
| [registry.ts.example](registry.ts.example) | `lib/registry.ts` | The single source of truth: one entry per page with its primary keyword, title, description, real modified date, and whether it belongs in `llms.txt`. Includes a cannibalisation guard you can run as a test |
| [sitemap.ts.example](sitemap.ts.example) | `app/sitemap.ts` | Generates `/sitemap.xml` from the registry, plus the companion `app/robots.ts` and the post-deploy verification commands |
| [llms.txt-route.ts.example](llms.txt-route.ts.example) | `app/llms.txt/route.ts` | Generates `/llms.txt` from the same registry, statically at build time |

The blank, stack-agnostic versions live one level up: [../llms.txt.example](../llms.txt.example)
and [../robots.txt.example](../robots.txt.example). The WordPress equivalents are in
[../wordpress/](../wordpress/README.md).

## Why a registry, and not three files you keep in sync

Every drift bug has the same shape: the sitemap lists a URL your canonical points away from,
or `llms.txt` recommends a page you set to noindex last month. Both are invisible until a
crawler acts on them. One typed array with derived views makes those states unrepresentable —
you cannot forget to update a file that does not exist.

The rule: **nothing outside `lib/registry.ts` filters the page list by hand.** If you need a
new view, add a derived function there.

## The rest of the metadata layer

**One metadata helper, so canonical and OG can never be forgotten.**

```ts
// lib/seo.ts
import type { Metadata } from 'next'
import { SITE_NAME, SITE_URL, absoluteUrl } from '@/lib/registry'

export function buildMetadata(path: string, title: string, description: string): Metadata {
  return {
    metadataBase: new URL(SITE_URL),
    title,
    description,
    alternates: { canonical: path },          // relative — metadataBase makes it absolute
    openGraph: { title, description, url: absoluteUrl(path), siteName: SITE_NAME, type: 'website' },
    twitter: { card: 'summary_large_image', title, description },
  }
}
```

Then every page is three lines, and reads its own registry entry rather than repeating
strings:

```ts
// app/nervous-patients/page.tsx
import { PAGES } from '@/lib/registry'
import { buildMetadata } from '@/lib/seo'

const entry = PAGES.find((p) => p.path === '/nervous-patients')!
export const metadata = buildMetadata(entry.path, entry.title, entry.description)
```

**JSON-LD** goes in the page or layout as a script tag, built by a pure function per type and
rendered as one connected graph sharing a single Organization `@id`:

```tsx
<script
  type="application/ld+json"
  dangerouslySetInnerHTML={{ __html: JSON.stringify(graph) }}
/>
```

**Per-page OG images** come from `opengraph-image.tsx` in a route segment using `ImageResponse`
from `next/og`. A segment's image is inherited by its children, so one file covers a hub and
all of its `[slug]` pages.

## The four Next.js traps

**1. A file in `public/` silently beats your route.** `public/llms.txt` is served before
`app/llms.txt/route.ts` ever runs, and `public/sitemap.xml` beats `app/sitemap.ts`. If edits
appear to do nothing, look in `public/` first.

**2. `'use client'` on a page kills its metadata.** The `metadata` export and
`generateMetadata` only work in server components. A page that became a client component to
get a `useState` will silently ship with no title, no canonical and no OG tags. Push the
interactive part into a child component and keep the page itself a server component.

**3. Content behind `useEffect` may never be ingested.** Answer engines and some crawlers
read the server-rendered HTML. Anything fetched client-side after hydration — including a
direct-answer block rendered from state — can be invisible to them. Check what actually
ships:

```bash
curl -s https://example.com/nervous-patients | grep -i "sedation"
```

If your key content is not in that output, it is not in the index either.

**4. `metadataBase` unset produces relative OG URLs.** Social and answer-engine previews need
absolute URLs. Set it once in the root layout or in the shared helper above, and Next resolves
everything else for you.

## Apply it

- [ ] `lib/registry.ts` exists and every public page has exactly one entry.
- [ ] Nothing outside the registry filters the page list by hand.
- [ ] `assertNoCannibalisation()` runs in the test suite and passes.
- [ ] `app/sitemap.ts` and `app/llms.txt/route.ts` both read the registry; neither has its own list.
- [ ] There is no `public/sitemap.xml` and no `public/llms.txt` shadowing the routes.
- [ ] Every page's metadata comes from the one `buildMetadata` helper, with `metadataBase` set.
- [ ] Every page that ships metadata is a server component — no `'use client'` at the page level.
- [ ] The direct-answer block and the key body copy appear in `curl` output, not just in the browser.
- [ ] `robots.ts` disallows API, app, account and thank-you routes, and the AI-crawler decision is written down.
- [ ] Every URL in the sitemap returns 200 and is self-canonical (the loop in `sitemap.ts.example` checks it).
- [ ] The sitemap is submitted to Search Console and Bing, and IndexNow re-pings on each content deploy.

## Related

- [../../search/13-schema-and-technical-wiring.md](../../search/13-schema-and-technical-wiring.md) — the method these files execute
- [../../search/12-geo-ai-search.md](../../search/12-geo-ai-search.md) — why `llms.txt`, entity consistency and server rendering matter
- [../../search/11-seo-fundamentals.md](../../search/11-seo-fundamentals.md) — keyword architecture and cannibalisation
- [../wordpress/README.md](../wordpress/README.md) — the same layer on WordPress
- [../llms.txt.example](../llms.txt.example) · [../robots.txt.example](../robots.txt.example) — the blank, stack-agnostic versions
- [../page-brief.md](../page-brief.md) — the per-page spec that fills a registry entry
- [../../skills/growth-search.skill.md](../../skills/growth-search.skill.md) — the agent procedure that enforces all of this
