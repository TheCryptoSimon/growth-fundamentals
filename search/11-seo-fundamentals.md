# SEO Fundamentals

How a brand-new site earns search traffic: intent mapping, keyword-to-URL architecture, on-page
anatomy, the technical baseline, indexing, and links. Stack-agnostic — nothing here assumes a CMS.
Read it before you name a single page or write a single title tag; re-read §5 whenever two of your
pages start ranking for the same thing.

---

## 0. The mental model: search is demand capture

Advertising interrupts someone and creates a want. Search does the opposite: the want already
exists, someone typed it, and your only job is to be the best available match at that moment.

1. **You are matching an intent, not a string.** The engine does not hand the page to whoever
   repeated the phrase most; it infers what the searcher wanted. Different words, same intent →
   near-identical results. Overlapping words, different intents → completely different results.
2. **The SERP is the spec.** What already ranks is the engine stating in public what it believes
   satisfies that query. If page one is nine comparison listicles, that query does not want your
   product page — no amount of optimisation fixes a format mismatch.
3. **You cannot out-optimise a missing audience.** Search rewards you for showing up where demand
   already flows; it does not create the flow. Demand creation is positioning, PR and paid — see
   [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md).

**Test every planned page:** write the exact query a real person would type, then ask "would this
page end their search?" If the honest answer is "no, they'd go back and click something else," it
will not hold a ranking even if it gets one.

## 1. The four intents, and the page type that serves each

Classify every target query into exactly one before deciding what to build. Getting this wrong is
the most common reason a well-written page never ranks.

| Intent | What they are doing | Query shape | Page type that wins | What kills it |
|---|---|---|---|---|
| **Informational** | Learning, diagnosing | "what is X", "how to X", "why does X happen" | Guide, tutorial, glossary entry, post | A sales pitch where an explanation was wanted |
| **Commercial investigation** | Comparing before buying | "best X", "X alternatives", "X vs Y", "X reviews" | Comparison, alternatives, buyer's guide | A one-sided page listing only your product |
| **Transactional** | Ready to act now | "buy X", "X pricing", "X free trial", "book X near me" | Product, pricing, booking, category | A blog post between them and the button |
| **Navigational** | Going somewhere specific | "<brand> login", "<brand> support", "<brand> pricing" | Your own real page, where they expect it | Making them hunt; a third party outranking you for your own name |

- One page, one intent. A page that explains, compares and sells equally ranks for none of the three.
- Never point a transactional query at a blog post, or an informational query at a pricing page.
- Own your navigational queries early — brand, brand + login, brand + pricing, brand + reviews.
  Cheapest to win, best converting.
- **Mixed SERPs:** when results blend formats, build the *dominant* one and satisfy the secondary
  intent inside it (a comparison page with a short "what it actually is" opener).

**Read the SERP as a spec** for every term (two minutes each): which format dominates; how deep and
old the top results are; which extra blocks appear (People Also Ask, images, video, map pack,
shopping), since each is a format you could produce; and which PAA questions expose sub-intents you
have not covered — free outline material.

## 2. Name the dial: where SEO is direction-dependent

Most of SEO is direction-neutral — a canonical tag does not care about your brand's temperature.
But everything a human *reads* sits on the dial, and search results are read by humans.

| Element | Trust pole (calm / premium / considered) | Urgency pole (energetic / promotional / impulse) |
|---|---|---|
| Title tag | Specific and plain: term + concrete deliverable | Term + a benefit or number hook; still literal |
| Meta description | What the page contains and who it is for | Adds a light action prompt and a differentiator |
| Content cadence | Fewer, deeper, maintained pages | More frequent, shorter, timelier pages |
| Comparison pages | Neutral, tabular, concedes where rivals win | Confident, sharper framing — still factually fair |
| Internal anchor text | Descriptive and dry | Descriptive with a benefit word |
| Freshness | Update dates only when content really changed | Publish cadence is itself the signal |

**Invert, do not soften.** At the trust pole, do not write a slightly-tamed clickbait title — drop
the hook and win the click with specificity ("Fee schedule for every plan, updated quarterly" beats
"You won't believe our pricing"). At the urgency pole, do not publish four sober essays a year and
call it a strategy; cadence is the point. **Fixed at both poles:** never manufacture urgency in a
title tag ("Only 2 left!" on an evergreen page), and never promise in the SERP what the page does
not deliver — an overpromise buys one click and loses the ranking on the bounce. Pole definitions:
[../psychology/04-persuasion-core.md](../psychology/04-persuasion-core.md).

## 3. Keyword research from zero

### 3.1 With no budget (this is enough to launch)

1. **Seed list.** 10-20 terms from three sources: what you call the product; what a customer called
   it in their own words (mine support tickets, sales calls, onboarding forms); the problem phrased
   as a complaint ("my X keeps Y-ing").
2. **Autocomplete harvesting.** Type each seed into the search box, record every suggestion, then
   repeat with modifiers: "seed for", "how to seed", "best seed for", "seed vs", "why seed", "seed
   without", "cheap seed", "seed near me". Suggestions come from real queries — the highest-signal
   free source that exists.
3. **Related searches and People Also Ask.** Harvest the bottom-of-page block and expand several PAA
   questions (expanding one usually spawns more). This maps the question space.
4. **Competitor gap, manually.** List 5-8 sites already ranking for your seeds; read their sitemaps
   (`/sitemap.xml`) and navigation. Every URL they have and you do not is a candidate — you are
   reading their intent map for free, not copying their pages.
5. **Question mining in the wild.** Forums, Q&A sites, review sections, the support pages of
   adjacent products. Real phrasing beats keyword-tool phrasing every time.
6. **Your own site search + Search Console.** The moment you have traffic, the queries report is the
   truest keyword tool you will own — it is your actual demand.

### 3.2 With paid tools

They accelerate steps 1-4; they do not replace judgement. Use them to pull a competitor's whole
ranking-keyword list at once, cluster thousands of variants into topics, spot terms where a weak
site currently ranks (an opening), and track movement over time. Treat every volume and difficulty
figure as a modelled estimate with wide error bars: directional, not factual.

### 3.3 Search volume is not demand

The most expensive research mistake is optimising for the biggest number in the spreadsheet.

- **Volume is a modelled estimate**, usually a rounded annual average. It hides seasonality,
  undercounts long-tail variants, and is unreliable at small numbers.
- **Zero-volume terms convert.** Tools round small numbers to zero. A handful of searches from people
  describing your exact problem in their own words can beat a head term with no purchase intent.
- **Volume ≠ available clicks.** Ads, answer boxes, video carousels and the map pack eat the top of
  the page; a query answered in full on the results page sends far fewer clicks than its number
  implies.
- **The unit is the topic, not the keyword.** One page can rank for dozens of phrasings of one
  intent. Plan clusters, then decide which cluster earns a URL.

**The judgement question:** what happens *right after the click*? Searchers three steps from buying
are worth more per visit than searchers ten steps away — but the far term is usually far easier to
win. Build both, and label them honestly in the plan.

### 3.4 Judging difficulty honestly on a new domain

Ignore the difficulty score for a moment and read page one directly.

| What page one looks like | Reading |
|---|---|
| All large, established, topically-dedicated sites | Not winnable in year one — skip, or attack a sub-slice |
| Forums, Q&A threads, thin aggregators present | Winnable; a genuinely good page displaces these |
| Top results shallow, outdated, or clearly not written by a practitioner | Winnable and worth doing well |
| One giant marketplace or platform dominating | Not winnable directly; target modifier variants |
| An obvious sub-intent nobody serves ("for beginners", "without X", "for small teams") | Your opening — that variant is the page to build |

**New-domain reality:** with no history and no links you compete on relevance and quality, not
authority. Your realistic starting field is **specific, lower-competition, longer queries**; you
climb toward head terms as trust accrues. A plan whose first ten pages all target head terms is a
plan to rank for nothing for a year. Allocate the first ~20 pages as a few head/commercial pages you
must own regardless of difficulty (they serve navigational and paid traffic too), plus a majority of
specific, winnable, intent-clear pages that rank quickly and link upward.

## 4. The load-bearing rule: capture the keyword, reframe the category

The rule most brand-led teams break and most SEO-led teams overcorrect on.

> **The metadata captures the term people actually search. The body carries the brand frame.**

| Slot | What goes in it | Why |
|---|---|---|
| Title tag | The literal searched term, naturally phrased | What the engine matches and the human scans |
| Meta description | The term plus what the page delivers | Not a ranking factor; a click factor |
| H1 | The term, or a close natural variant, once | Confirms the subject to reader and crawler |
| URL slug | A short readable form of the term | Stable, legible, shareable |
| Structured data | The literal name and description | Machine-readable confirmation ([13](13-schema-and-technical-wiring.md)) |
| **Body copy** | **Your positioning, your language, your frame** | What makes someone choose you over the other nine results |

**The failure this prevents.** A team invents an evocative internal name for its category and puts
it in every title tag. Nobody searches it, so the page matches nothing — while the term people *do*
type appears nowhere in the metadata. The page is invisible and the positioning reaches no one. A
distinctive positioning phrase is an asset in the body, on the About page and in PR; it is a
liability in a title tag until people search it.

**The opposite failure.** Repeating the keyword through the body until the copy reads like a crawler
wrote it. Engines resolve synonyms and concepts; the repetition buys nothing and costs you the
human. Rule of thumb: **the keyword appears where it is matched and where it aids comprehension —
nowhere else.**

## 5. One primary keyword per URL, and how cannibalisation happens

Every URL owns exactly one primary intent and one primary term. Record it in the page brief
([../templates/page-brief.md](../templates/page-brief.md)) before writing the page.

**Cannibalisation** is two or more of your own URLs competing for the same query. Not a penalty — a
dilution. **Symptoms:** the same query lands on different URLs on different days in Search Console;
a page's position oscillates with no edits; neither page ranks as well as one merged page obviously
would; internal links on that topic point at two destinations depending on who wrote them.

| Cause on a young site | Example |
|---|---|
| A post written on the same topic as a commercial page | "What is a project tracker" post vs the "Project tracker" product page |
| A category and subcategory with near-identical scope | `/tools/` and `/tools/all/` |
| Audience pages built by find-and-replace | "for dentists", "for clinics", "for practices" — one page, three URLs |
| Tag, archive, filter, sort or pagination URLs | `/blog/tag/pricing/` vs `/blog/category/pricing/` |
| A term drifting after an edit | Someone adds the money page's term to the guide's H1 |

**Fixes, in order of preference:** merge into the stronger URL and redirect the weaker one; re-scope
the weaker page to a genuinely different sub-intent and re-point its internal links; canonicalise
the duplicate; only last, `noindex` it. Prevention beats all four — keep a **keyword-to-URL map** as
a real file, and make "which URL owns this term?" a required question in every content brief.

## 6. Site architecture: the tiers

Build the map before the pages. Each tier serves a different intent and links to the others in a
defined direction.

| Tier | What it is | Intent served | Typical count at launch |
|---|---|---|---|
| **1. Commercial head** | Homepage, product/service pages, pricing | Transactional + navigational | 3-6 |
| **2. Pain / problem** | "How to stop X", "why X keeps happening", "fixing X" | Informational → commercial | 4-8 |
| **3. Audience / segment** | One page per genuinely distinct customer type | Commercial investigation | 2-5 |
| **4. Comparison / alternatives** | "X vs Y", "best X for Z", "X alternatives" | Commercial investigation | 3-8 |
| **5. Glossary** | One short page per term, owning definitional intent | Informational (definitional) | 8-15 |
| **6. Informational blog** | Everything else long-tail, linking up | Informational | Ongoing |

- **Pain pages are usually the strongest converters** on a young site: high intent, lower competition
  than head terms, natural bridge to the product.
- **Audience pages must be genuinely written for that audience.** A find-and-replace clone set
  creates a doorway-page problem and a cannibalisation problem at once.
- **Comparison pages must be fair and factual.** Concede where a rival is genuinely better; a page
  that only flatters you fails the reader's real question and is trivially spotted. Never invent
  feature claims about a competitor — credibility risk and legal risk.
- **The glossary is load-bearing.** It absorbs "what is X" intent so commercial pages need not open
  with a definition, and it is disproportionately useful to AI answer engines ([12](12-geo-ai-search.md)).
- **The blog never competes with the money pages.** It catches long-tail informational demand and
  passes relevance and readers upward.

### URL structure

- Lowercase, hyphens between words, no underscores, no spaces, no capitals.
- Short, readable, guessable from the title. Keep the term, drop the filler:
  `/project-tracker-for-agencies/`, not
  `/the-best-project-tracker-software-for-small-creative-agencies-2026/`.
- **No dates in evergreen URLs** — a year in a slug forces an annual redirect or a stale URL.
- Folder depth is not a ranking lever but it *is* a clarity lever: one level of grouping where it
  aids comprehension (`/glossary/term/`, `/compare/x-vs-y/`), no more.
- **Decide the pattern at day zero** — trailing slash or not, `www` or not, folder scheme. Every
  later change costs a redirect and some equity.
- Keep private, account, checkout, admin and API routes outside the public content tree entirely.

### Internal linking

The strongest ranking lever you fully control, and it is free.

- **Hub and spoke.** Each tier-1/tier-2 page is a hub; the informational pages around it are spokes.
  Every spoke links to its hub, the hub links to its main spokes, spokes link sideways only when
  genuinely relevant.
- **Link up, from informational to commercial.** Every guide, glossary entry and post carries at
  least one contextual link to the commercial or pain page it supports. This is how a young site
  channels relevance earned on easy terms into the pages that make money.
- **Descriptive anchors** that describe the destination: "our project tracker pricing", not "click
  here", not a bare URL, and not the same exact-match phrase on every link. Vary across a few true
  variants; identical anchors site-wide look engineered.
- **Every page reachable in ~3 clicks from the homepage.** Reachable only from the sitemap file =
  orphaned.
- **Link a new page the day it publishes**, from at least two existing pages. URLs are discovered
  through links, not by waiting.
- Keep navigation to real destinations; never stuff the footer to manufacture link volume. Section
  structure: [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md).

## 7. On-page anatomy

**Title tag.** The highest-leverage string on the page: a ranking input *and* the headline of your
listing. Plan for roughly 50-60 characters (the real limit is pixel width, so wide capitals truncate
earlier). Primary term near the front, phrased naturally, then one differentiator — the deliverable,
the audience, the format or the brand. A trailing brand name is optional: drop it on long titles,
keep it on short ones and on navigational pages. Unique on every URL; duplicate titles are a
cannibalisation tell.

| Page type | Pattern | Generic example |
|---|---|---|
| Product / commercial | `<Term> — <core benefit or audience> \| <Brand>` | `Job scheduling software — for field service teams \| Northwind` |
| Pricing | `<Product> pricing — <what's included>` | `Job scheduling pricing — plans, limits and setup fees` |
| Pain / problem | `<Problem as searched> — <what the page gives>` | `Why technicians miss appointments — 6 causes and fixes` |
| Comparison | `<A> vs <B>: <axis of comparison>` | `Northwind vs Ridgeline: features, pricing and fit` |
| Glossary | `<Term>: definition and example` | `Dispatch window: definition and example` |
| Guide / blog | `<How-to as searched> (<qualifier>)` | `How to plan a route for 40 daily stops (step by step)` |
| Local | `<Service> in <place> \| <Brand>` | `Emergency dental care in Riverton \| Ash Lane Dental` |

**Meta description.** Not a ranking factor but a click factor — and engines rewrite it when it fails
to match the query, itself a signal it was not answering the search. Roughly 140-155 characters,
unique per page, never auto-generated on important pages. Say what the page contains and who it is
for, with the term phrased naturally (matched words are bolded in the listing, which aids scanning).
One concrete specific beats one adjective: "plans, limits and setup fees" beats "great value". Close
with an action prompt at the urgency pole, with the deliverable at the trust pole.

**Headings.** Exactly one H1, matching the page's subject and containing the primary term or a close
variant — the logo is not the H1. H2s are the outline in the order a reader needs them; H3s nest
only inside an H2; never skip a level for styling, since size is CSS's job. Write headings as
answers or labels a scanner can use, not clever fragments, and mirror the questions the SERP showed
you — most readers scan headings and read only the section they need.

**The first 100 words.** Answer the target query immediately, in a self-contained paragraph a
stranger could quote without the rest of the page. This serves the impatient human, snippet
selection, and AI answer engines at once — [12-geo-ai-search.md](12-geo-ai-search.md) covers how to
construct and reuse that block. Include the primary term once, naturally. Never open with the origin
story, a definition of the industry, or "In today's fast-paced world".

**Images.** Descriptive filenames before upload (`route-planner-map-view.png`, not `IMG_4821.png`).
Alt text describes the image for someone who cannot see it — accessibility first, SEO second;
decorative images get `alt=""`, never a keyword. "Screenshot of the weekly schedule view" is correct;
a string of product keywords is spam. Compress, serve modern formats, set explicit width and height
(prevents layout shift), and lazy-load below-the-fold images only — never the largest above-the-fold
image. Caption the useful ones; captions get read more than body copy.

**Body links.** 3-6 contextual internal links on a substantial page, placed where a reader would want
the detour, not clustered at the bottom. External links to real sources are a quality signal, not a
leak — cite the standard, the study, the spec. Mark paid, sponsored or user-generated links
appropriately; selling a followed link is a policy violation with real consequences.

## 8. Quality signals in practice

Public quality guidance emphasises experience, expertise, authoritativeness and trustworthiness
(E-E-A-T). It is not a score you can inspect — it describes what human raters are asked to look for.
Translate it into things you literally put on a page.

| Signal | What actually goes on the page |
|---|---|
| **Experience** | First-hand detail only a practitioner would have: what went wrong, the edge case, the photo you took, a number from your own work. A summary of other people's articles reads as exactly that. |
| **Expertise** | A named author with a real, verifiable credential or track record, linked to an author page. "Admin" and "The Team" are anti-signals on anything consequential. |
| **Authoritativeness** | Being cited elsewhere; one consistent entity description everywhere you appear; being the site people link to for a specific thing. |
| **Trustworthiness** | Contact details, a real registered address if you have one, an About page naming humans, transparent pricing, clear policies, HTTPS, working forms, no dark patterns. |

- [ ] Author byline on every article, linking to an author page with a real bio and credentials.
- [ ] Published date, and a "last updated" date only when genuinely revised. Never fake a refresh.
- [ ] Sources cited and linked for factual claims; state how you know what you claim.
- [ ] An About page naming real people and stating what the company is and is not.
- [ ] Contact details reachable in one click from every page.
- [ ] An editorial or review policy if the topic touches money, health, safety or legal matters.
- [ ] Reviews and testimonials only if real and attributable. Fabricating them is fraud, and marking
      up invented ratings in structured data is a manual-action risk.

**The higher the stakes, the higher the bar.** Content that could affect someone's money, health,
safety or legal position is held to a stricter standard by raters and readers alike. In those
categories credentials and sourcing are not decoration — they are the requirement.

## 9. Technical baseline

Ship all of this before anything clever. Code-level wiring:
[13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md).

| Item | The rule | Common failure |
|---|---|---|
| **Crawlability** | Every public page reachable by link and allowed in `robots.txt` | A staging block on a directory that nobody removed |
| **Rendering** | Public content present in the served HTML | Client-only rendering leaving crawlers an empty shell |
| **Indexability** | No stray `noindex` on pages you want ranked | A site-wide `noindex` surviving launch — check this first, always |
| **HTTPS + one canonical host** | Enforced everywhere; pick `www` or bare; everything else 301s once | Both hosts serving 200 and splitting signals; http→www→https chains |
| **Canonical tags** | Self-referencing on every indexable page; pointing to the original on true duplicates | Canonicals pointing at the homepage site-wide |
| **XML sitemap** | Only canonical, indexable, 200-status URLs, generated from one source | A stale sitemap listing deleted or private URLs |
| **robots.txt** | Disallow private/admin/checkout/API; `Sitemap:` on the live domain | A staging hostname left in the `Sitemap:` line |
| **Redirects** | 301 for permanent moves, one hop, to the closest equivalent page | Chains, loops, everything dumped on the homepage |
| **404s** | A real 404 status with a helpful page | Soft 404s returning 200 on a not-found page |
| **Pagination** | Every page crawlable via real links, unique titles; do not canonicalise page 2+ to page 1 | Infinite scroll with no crawlable links behind it |
| **Faceted / filter URLs** | Decide which combinations are indexable; block or canonicalise the rest | Millions of permutations eating crawl budget |
| **Mobile** | The mobile rendering is the one that counts; content parity with desktop | Hiding content on mobile that exists on desktop |
| **Core Web Vitals** | Fast largest paint, negligible layout shift, responsive to input | A hero image and font stack that push the largest paint late |
| **hreflang** (multi-language only) | Reciprocal annotations across all variants, plus `x-default` | One-way tags; using it for near-identical same-language pages |
| **Structured data** | Reflects what is actually on the page; validates cleanly | Marking up content the visitor cannot see |

**Performance is a means, not an end.** Speed is a modest ranking input and a large conversion input.
Chase fixes a real user would feel — image weight, font loading, blocking scripts, layout shift —
and stop optimising the score once the page feels instant. Keeping the front end light by
construction: [../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md).

## 10. Getting indexed

Ranking is downstream of indexing, and indexing is not automatic. **Day one of launch:**

1. Verify in Google Search Console — DNS TXT verification is the most durable, surviving redesigns
   and platform moves.
2. Add the site to Bing Webmaster Tools (it can import the Search Console setup).
3. Submit the XML sitemap in both.
4. URL-Inspect and request indexing on priority URLs — homepage plus the handful of commercial
   pages. It is rate-limited; the sitemap covers the rest.
5. Wire **IndexNow** (a key file plus a POST on publish) so Bing and Yandex learn about new and
   changed URLs immediately, and re-ping on every content deploy that adds or changes URLs.

**When a page will not index, check in this order:**

- [ ] Does it return 200 to an anonymous request? Test logged out — a logged-in session hides access
      and cache problems.
- [ ] Is it blocked in `robots.txt`, or carrying `noindex`?
- [ ] Does its canonical point somewhere else?
- [ ] Is it in the sitemap, and is the sitemap actually being read (check the report)?
- [ ] Does any internal link point to it? Orphans get found slowly or never.
- [ ] Does the served HTML contain the content, or only a JavaScript shell?
- [ ] Is it a near-duplicate of a page you already have?
- [ ] Is it thin — genuinely low-value, boilerplate, or auto-generated?

"Discovered – currently not indexed" and "Crawled – currently not indexed" usually mean the engine
looked and did not think the page earned a slot. The fix is nearly always **make it substantially
better or merge it**, not resubmit repeatedly.

## 11. Off-page: why links still matter, and which ones you can get

Links remain one of the clearest signals that someone outside your own site thinks you are worth
referencing. On a brand-new domain with none, the first genuine ones matter disproportionately.

| Legitimate source | What it takes | Why it works |
|---|---|---|
| **Original data** | A survey, your own anonymised aggregate data, a benchmark nobody has run — with the methodology published | People must cite a number's source; you become the source |
| **Digital PR** | A genuine story, a real expert, a reporter's actual beat, a fast response when a relevant story breaks | Editorial links from real publications |
| **Being genuinely quotable** | A named framework, a clear definition, a strong opinion with the reasoning shown | Writers link to the clearest explanation they can find |
| **Partnerships and integrations** | Partner directories, case studies, co-authored material, integration pages on both sides | Real relationships produce real pages |
| **Community and expert contribution** | Answering well where your buyers already ask; podcasts, panels, guest pieces with real substance | Slow, but the audience is exactly right |
| **Your own footprint** | Industry directories, professional bodies, supplier and customer listings | Entity consistency matters more than the link itself |
| **Being the resource** | A free tool, calculator, template, dataset or reference table people bookmark | Tools attract links for years |

**Avoid:** bought links, private blog networks, mass guest-post spam, comment and forum drops, link
exchanges, paid directory farms, anything sold by volume. They violate the guidelines, are
detectable at scale, and the downside — a manual action or a quiet devaluation — lands on the domain
you are building. One editorial link from a genuinely relevant, respected site beats a hundred from
anywhere that takes anyone. And links are a *lagging* signal of doing something worth linking to: if
you cannot earn any, the honest question is "what have we published that a stranger would cite?"

## 12. Local SEO, if the brand has a place

Only relevant when you serve customers at a location or within a service area.

- [ ] Claim and fully complete the business profile on the major map platforms — categories, hours,
      service list, real photos.
- [ ] **NAP consistency**: name, address, phone written identically on your site, every profile and
      every directory. Inconsistency is the most common local ranking problem.
- [ ] The same details in the footer and on a contact page, with `LocalBusiness` structured data
      ([13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md)).
- [ ] One page per location with genuinely local content — parking, transit, neighbourhood, the team
      at that site. Not a template with the town name swapped.
- [ ] One page per core service, plus service-and-place pages where demand justifies them.
- [ ] Ask real customers for reviews through a compliant, non-incentivised process, and reply. Never
      write, buy or filter reviews — it is fraud, and platforms remove businesses for it.
- [ ] Get listed in genuinely local sources: chambers of commerce, local press, sponsorships, trade
      bodies. Track the map pack separately; it behaves differently from classic results.

## 13. A realistic 0-6 month timeline

A **planning framework, not a forecast**. Pace depends on competition, category, publishing rate,
and whether the brand already has an audience. Nothing here is a guarantee, and any source quoting
exact percentages for a generic new site is guessing.

| Window | What you do | What to expect | The trap |
|---|---|---|---|
| **Weeks 0-2** | Technical baseline, verify in Search Console and Bing, submit the sitemap, publish the core commercial pages | Indexing begins on the homepage and a few key URLs; effectively no traffic | Concluding "SEO doesn't work" from a fortnight |
| **Weeks 2-6** | Publish the pain and glossary tiers, internal-link everything, earn the first genuine mentions | More pages indexed; impressions appear for brand and very long-tail terms; clicks near zero | Rewriting pages weekly out of impatience — it destroys your own measurement |
| **Months 2-3** | Keep publishing to the map, start comparison pages, begin real link work | First rankings on specific low-competition queries; positions volatile, which is normal for new URLs | Chasing daily rank fluctuations |
| **Months 3-4** | Read the Search Console queries report and let it retarget you; fix pages with impressions but no clicks | Long-tail traffic becomes measurable and repeatable; first conversions from search | Ignoring the queries report, now better data than any keyword tool |
| **Months 4-6** | Consolidate cannibalisation, deepen the winning cluster, push internal links to the money pages | A compounding curve rather than a flat line; mid-competition terms come into reach | Starting a new cluster before the first one is finished |
| **Beyond 6 months** | Head terms become realistic as authority accrues | — | Assuming the curve continues without continued work |

**Leading indicators move first** — pages indexed, impressions, distinct queries you appear for,
average position on the target cluster, referring domains. If those climb, traffic follows. If they
are flat after two months of publishing, something structural is wrong: start with indexing (§10)
and intent match (§1). Instrumentation:
[../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md).

## 14. The black-hat list: not worth the risk

Each item below either violates search guidelines outright or degrades the site for humans. On a new
domain the asymmetry is brutal: a small temporary gain against the only asset you are building.

- Buying or selling links that pass ranking signals; private blog networks; link farms.
- Hidden text and hidden links (invisible colour, off-screen positioning, zero-size fonts).
- Keyword stuffing anywhere — body, alt text, meta keywords, footer term lists.
- Cloaking: serving crawlers different content from users, including "SEO-only" text blocks.
- Doorway pages: near-identical location or keyword pages funnelling to one destination.
- Scraped, spun or auto-translated content published without human review or added value.
- Bulk AI-generated pages published at scale with no editing, sourcing or first-hand substance.
  AI-assisted writing is fine; unreviewed mass publication is the problem.
- Expired-domain purchases repurposed to inherit unrelated authority.
- Fake reviews, invented ratings, and structured data describing things not on the page.
- Sneaky redirects sending users somewhere other than what they clicked.
- Manufactured urgency and countdowns that reset — a conversion and trust problem too, see
  [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md).
- Negative SEO attempts against competitors.

**The line to hold:** if a tactic only works because the engine has not noticed yet, or because the
user has not noticed yet, it is not a strategy — it is a debt with an unknown due date.

## Apply it

- [ ] Every planned URL has one primary keyword and one intent class in its page brief before writing.
- [ ] A keyword-to-URL map exists as a real file, checked before any new page is briefed.
- [ ] Every target term's SERP has been read, and the page format matches what is ranking.
- [ ] Titles, metas, H1s and schema capture the searched term; the body carries the brand frame.
- [ ] The architecture covers all six tiers, and every informational page links up to the commercial
      page it supports.
- [ ] Every page answers its query in a self-contained paragraph within the first 100 words.
- [ ] Exactly one H1 per page; headings form the real outline; no level skipped for styling.
- [ ] Images have descriptive filenames, honest alt text, explicit dimensions and modern formats.
- [ ] Authors are named with real credentials; dates, sources, About and contact details are true.
- [ ] The §9 technical baseline is green, verified on a logged-out request, before launch.
- [ ] Search Console and Bing verified, sitemap submitted, IndexNow wired, priority URLs inspected.
- [ ] The link plan uses only legitimate sources; nothing from §14 appears anywhere on the site.
- [ ] Leading indicators are reviewed monthly, not daily.
- [ ] The 0-6 month expectation is stated to whoever funds this, so month two does not trigger a
      panic rewrite.

## Related

- [12-geo-ai-search.md](12-geo-ai-search.md) — making the same pages quotable by AI answer engines
- [13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md) — structured data, canonicals, sitemap, robots, IndexNow
- [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md) — the frame the body copy carries
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — how the on-page copy actually reads
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — the section structure behind each page type
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — what to check once the traffic arrives
- [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md) — instrumenting and reading the results
- [../ops/15-launch-checklist-and-build-order.md](../ops/15-launch-checklist-and-build-order.md) — where search work sits in the build order
- [../templates/page-brief.md](../templates/page-brief.md) — the per-page brief that records the primary keyword
- [../templates/robots.txt.example](../templates/robots.txt.example) — a starting robots file
