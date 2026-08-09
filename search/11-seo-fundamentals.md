# SEO Fundamentals

How a brand-new site earns search traffic: intent mapping, keyword-to-URL architecture, on-page
anatomy, the technical baseline, indexing, and links. Stack-agnostic — nothing here assumes a CMS.
Read it before you name a single page or write a single title tag; re-read §5 whenever two pages
start ranking for the same thing.

---

## 0. The mental model: search is demand capture, not demand creation

Advertising interrupts someone and creates a want. Search does the opposite: the want already
exists, someone typed it, and your only job is to be the best available match at that moment. Three
consequences drive every rule below.

1. **You are matching an intent, not a string.** The engine does not hand the page to whoever
   repeated the phrase most; it infers what the searcher wanted. Different words, same intent →
   near-identical results. Overlapping words, different intents → completely different results.
2. **The SERP is the spec.** What already ranks is the engine stating in public what it believes
   satisfies that query. If page one is nine comparison listicles, that query does not want your
   product page — no amount of optimisation fixes a format mismatch.
3. **You cannot out-optimise a missing audience.** Search rewards you for showing up where demand
   already flows; it does not generate the flow. Demand creation is positioning, PR and paid — see
   [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md).

**Test every planned page:** write the exact query a real person would type, then ask "would this
page end their search?" If the honest answer is "no, they'd go back and click something else," the
page will not hold a ranking even if it gets one.

---

## 1. The four intents and the page type that serves each

Classify every target query into exactly one of these before you decide what to build. Getting this
wrong is the single most common reason a well-written page never ranks.

| Intent | What the searcher is doing | Query shape | Page type that wins | What kills it |
|---|---|---|---|---|
| **Informational** | Learning, diagnosing, understanding | "what is X", "how to X", "why does X happen", "X vs Y explained" | Guide, tutorial, glossary entry, blog post | A sales pitch where an explanation was wanted |
| **Commercial investigation** | Comparing options before buying | "best X", "X alternatives", "X vs Y", "X reviews", "X pricing" | Comparison page, alternatives page, buyer's guide, pricing page | A one-sided page that only lists your product |
| **Transactional** | Ready to act now | "buy X", "X pricing", "X free trial", "book a X near me", "X demo" | Product page, pricing page, booking page, category page | A blog post standing between them and the button |
| **Navigational** | Going somewhere specific | "<brand> login", "<brand> support", "<brand> pricing" | Your own real page, exactly where they expect it | Making them hunt; letting a third party outrank you for your own name |

**Rules that fall out of the table:**

- One page, one intent. A page that explains, compares and sells in equal measure ranks for none of
  the three.
- Never point a transactional query at a blog post, or an informational query at a pricing page.
- Own your navigational queries early — brand, brand + login, brand + pricing, brand + reviews.
  Cheapest to win, best converting.
- **Mixed SERPs:** when the results blend formats, build the *dominant* one and satisfy the
  secondary intent inside it (a comparison page with a short "what it actually is" opener).

**Read the SERP as a spec** for every target term (two minutes each): which format dominates; how
deep and how old the top results are; which extra blocks are present (People Also Ask, images,
video, map pack, shopping) since each is a format you could also produce; and which People Also Ask
questions reveal sub-intents you have not covered — that is free outline material.

---

## 2. Name the dial: where SEO is direction-dependent

Most of SEO is direction-neutral — a canonical tag does not care about your brand's temperature.
But everything a human *reads* is on the dial, and search results are read by humans.

| Element | Trust pole (calm / premium / considered) | Urgency pole (energetic / promotional / impulse) |
|---|---|---|
| Title tag | Specific and plain: the term + the concrete deliverable | Term + a benefit or number hook; still literal, never bait |
| Meta description | States what the page contains and who it is for | Adds a light action prompt and a differentiator |
| Content cadence | Fewer, deeper, maintained pages | More frequent, shorter, timelier pages |
| Comparison pages | Neutral, tabular, concedes where rivals are better | Confident, sharper framing — still factually fair |
| Anchor text on internal links | Descriptive and dry | Descriptive with a benefit word |
| Freshness signals | Update dates on evergreen pages only when the content really changed | Publish cadence itself is the signal |

**Inverses to apply, not soften.** If you are at the trust pole, do not write a slightly-tamed
clickbait title — invert it: drop the hook entirely and win the click with specificity ("Fee
schedule for every plan, updated quarterly" beats "You won't believe our pricing"). If you are at
the urgency pole, do not publish four sober essays a year and call it a content strategy — cadence
and timeliness are the point.

Two things stay fixed at both poles: **never manufacture urgency in a title tag** ("Only 2 left!"
on an evergreen page), and **never promise in the SERP what the page does not deliver.** A title
that overpromises buys one click and loses the ranking when people bounce straight back. The dial
concept and the pole definitions live in
[../psychology/04-persuasion-core.md](../psychology/04-persuasion-core.md).

---

## 3. Keyword research from zero

### 3.1 With no budget (this is enough to launch)

1. **Seed list.** 10-20 terms from three sources: what you call the product, what a customer called
   it in their own words (mine support tickets, sales calls, onboarding forms), and the problem
   phrased as a complaint ("my X keeps Y-ing").
2. **Autocomplete harvesting.** Type each seed into the search box and record every suggestion, then
   repeat with modifiers: "seed for", "how to seed", "best seed for", "seed vs", "why seed", "seed
   without", "cheap seed", "seed near me". Suggestions come from real queries — the highest-signal
   free source that exists.
3. **Related searches and People Also Ask.** Harvest the bottom-of-page related block and expand
   several PAA questions (expanding one usually spawns more). Maps the question space.
4. **Competitor gap, manually.** List 5-8 sites already ranking for your seeds; read their sitemaps
   (`/sitemap.xml`) and navigation. Every URL they have and you do not is a candidate. You are not
   copying pages, you are reading their intent map for free.
5. **Question mining in the wild.** Forums, Q&A sites, review sections, and the support pages of
   adjacent products. Real phrasing beats keyword-tool phrasing every time.
6. **Your own site search + Search Console.** The moment you have traffic, the queries report is
   the truest keyword tool you will ever own — it is your actual demand.

### 3.2 With paid tools

They speed up steps 1-4; they do not replace judgement. Use them to pull a competitor's whole
ranking-keyword list at once, cluster thousands of variants into topics, spot terms where a weak
site currently ranks (an opening), and track movement over time. Treat every volume and difficulty
number as a modelled estimate with wide error bars: directional, not factual.

### 3.3 Search volume is not demand

The most expensive research mistake is optimising for the biggest number in the spreadsheet.

- **Volume is a modelled estimate**, usually a rounded annual average. It hides seasonality,
  undercounts long-tail variants, and is unreliable at small numbers.
- **Zero-volume terms convert.** Tools round small numbers to zero. A handful of searches from
  people describing your exact problem in their words can beat a head term with no purchase intent.
- **Volume ≠ available clicks.** Ads, answer boxes, video carousels and the map pack eat the top of
  the page; a query fully answered on the results page sends far fewer clicks than its number
  implies.
- **The unit is the topic, not the keyword.** One page can rank for dozens of phrasings of one
  intent. Plan clusters, then decide which cluster earns a URL.

**The judgement question:** ask what happens *right after the click*. A term whose searchers are
three steps from buying is worth more per visit than one ten steps away — but the far term is
usually far easier to win. Build both, and label them honestly in the plan.

### 3.4 Judging difficulty honestly on a brand-new domain

Ignore the tool's difficulty score for a moment and look at page one directly:

| Signal on page one | Reading |
|---|---|
| All results are large, established, topically-dedicated sites | Not winnable in year one — skip or attack a sub-slice |
| Results include forums, Q&A threads, or thin aggregator pages | Winnable — a genuinely good page can displace these |
| Top results are shallow, outdated, or clearly not written by anyone with real experience | Winnable, and worth doing well |
| Results are dominated by one giant marketplace or platform | Usually not winnable directly; target the modifier variants instead |
| The query has an obvious sub-intent nobody serves ("for beginners", "without X", "for small teams") | Your opening — that variant is the page to build |

**New-domain reality:** with no history and no links you compete on relevance and quality, not
authority. Your realistic starting field is **specific, lower-competition, longer queries**; you
climb toward head terms as trust accrues. A plan whose first ten pages all target head terms is a
plan to rank for nothing for a year. Allocate the first ~20 pages as: a few head/commercial pages
you must own regardless of difficulty (they serve navigational and paid traffic too), and a
majority of specific, winnable, intent-clear pages that rank quickly and link upward.

---

## 4. The load-bearing rule: capture the keyword, reframe the category

The rule most brand-led teams break and most SEO-led teams overcorrect on.

> **The metadata captures the term people actually search. The body carries the brand frame.**

| Slot | What goes in it | Why |
|---|---|---|
| Title tag | The literal searched term, naturally phrased | This is what the engine matches and the human scans |
| Meta description | The term plus what the page delivers | Earns the click; not a ranking factor, but a click factor |
| H1 | The term, or a close natural variant, once | Confirms the page's subject to reader and crawler |
| URL slug | A short, readable form of the term | Stable, human-legible, shareable |
| Structured data | The literal name/description | Machine-readable confirmation — see [13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md) |
| **Body copy** | **Your positioning, your language, your frame** | This is what makes someone choose you rather than the other nine results |

**The failure this prevents.** A team invents an evocative internal name for its category and puts
it in every title tag. Nobody searches that term, so the page matches nothing — while the term
people *do* type appears nowhere in the metadata. The page is invisible and the elegant positioning
reaches no one. A distinctive positioning phrase is an asset in the body, on the About page and in
PR; it is a liability in a title tag until people search it.

**The opposite failure.** Repeating the keyword through the body until the copy reads like a crawler
wrote it. Engines resolve synonyms and concepts; the repetition buys nothing and costs you the
human. Rule of thumb: **the keyword appears where it is matched and where it aids comprehension —
nowhere else.**

---

## 5. One primary keyword per URL, and how cannibalisation happens

Every URL owns exactly one primary intent and one primary term. Write it in the page brief
([../templates/page-brief.md](../templates/page-brief.md)) before writing the page.

**Cannibalisation** is when two or more of your own URLs compete for the same query. Not a penalty
— a dilution. **Symptoms:** Search Console shows the same query landing on different URLs on
different days; a page's position oscillates with no edits; neither page ranks as well as one
merged page obviously would; internal links on that topic point at two destinations depending on
who wrote them.

**How it happens on a young site:**

| Cause | Example |
|---|---|
| A blog post written on the same topic as a commercial page | "What is a project tracker" post vs the "Project tracker" product page |
| A category and a subcategory with near-identical scope | /tools/ and /tools/all/ |
| Multiple audience pages with find-and-replace bodies | "for dentists", "for clinics", "for practices" — all the same page |
| Tag, archive, filter, sort or pagination URLs generating near-duplicates | /blog/tag/pricing/ vs /blog/category/pricing/ |
| A term drifting between two pages after an edit | Somebody adds the money page's term to the guide's H1 |

**Fixes, in order of preference:** merge into the stronger URL and redirect the weaker one; or
re-scope the weaker page to a genuinely different sub-intent and re-point its internal links; or
canonicalise the duplicate; only last, `noindex` the weaker one. Prevention beats all four:
maintain a **keyword-to-URL map** as a real file, and treat "which URL owns this term?" as a
required question at the start of every content brief.

---

## 6. Site architecture: the tiers

Build the map before the pages. Each tier serves a different intent and links to the others in a
defined direction.

| Tier | What it is | Intent served | Typical count at launch |
|---|---|---|---|
| **1. Commercial head** | Homepage, product/service pages, pricing | Transactional + navigational | 3-6 |
| **2. Pain / problem** | "How to stop X", "why X keeps happening", "fixing X" | Informational → commercial | 4-8 |
| **3. Audience / segment** | One page per genuinely distinct customer type | Commercial investigation | 2-5 |
| **4. Comparison / alternatives** | "X vs Y", "best X for Z", "X alternatives" | Commercial investigation | 3-8 |
| **5. Glossary** | One short page per term, owning definitional intent | Informational (definitional) | 8-20 |
| **6. Informational blog** | Everything else long-tail, linking up | Informational | Ongoing |

**Notes that matter:**

- **Pain pages are usually the strongest converters** on a young site: high intent, lower
  competition than head terms, natural bridge to the product.
- **Audience pages must be genuinely written for that audience.** A find-and-replace clone set
  creates a doorway-page problem and a cannibalisation problem at once.
- **Comparison pages must be fair and factual.** Concede where a rival is genuinely better; a page
  that only flatters you fails the reader's actual question and is trivially spotted. Never invent
  feature claims about a competitor — credibility risk and legal risk.
- **The glossary is load-bearing.** It absorbs "what is X" intent so commercial pages need not open
  with a definition, and it is disproportionately useful to AI answer engines
  ([12-geo-ai-search.md](12-geo-ai-search.md)).
- **The blog never competes with the money pages.** It catches long-tail informational demand and
  passes relevance and readers upward.

### URL structure rules

- Lowercase, hyphens between words, no underscores, no spaces, no capitals.
- Short, readable, guessable from the page title. Keep the term, drop the filler:
  `/project-tracker-for-agencies/`, not
  `/the-best-project-tracker-software-for-small-creative-agencies-2026/`.
- **No dates in evergreen URLs** — a year in a slug forces an annual redirect or a stale URL.
- Folder depth is not a ranking lever but it *is* a clarity lever: one level of grouping where it
  aids comprehension (`/glossary/term/`, `/compare/x-vs-y/`), no more.
- **Decide the pattern once, at day zero** — trailing slash or not, `www` or not, folder scheme.
  Every later change costs a redirect and some equity.
- Keep private, account, checkout, admin and API routes outside the public content tree entirely.

### Internal linking rules

The strongest ranking lever you fully control, and it is free.

- **Hub and spoke.** Each tier-1/tier-2 page is a hub; the informational pages around it are spokes.
  Every spoke links to its hub, the hub links to its main spokes, spokes link sideways only when
  genuinely relevant.
- **Link up, from informational to commercial.** Every guide, glossary entry and post carries at
  least one contextual link to the commercial or pain page it supports. This is how a young site
  channels the relevance it earns on easy terms into the pages that make money.
- **Descriptive anchors** that describe the destination: "our project tracker pricing", not "click
  here", not a bare URL, and not the same exact-match phrase on every link. Vary across a few true
  variants; identical anchors site-wide look engineered.
- **Every page reachable in ~3 clicks from the homepage.** Reachable only from the sitemap file =
  orphaned.
- **Link a new page the day it publishes**, from at least two existing pages. URLs are discovered
  through links, not by waiting.
- Keep navigation to real destinations; never stuff the footer to manufacture link volume. Section
  structure lives in
  [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md).

---

## 7. On-page anatomy

### Title tag

The highest-leverage string on the page: a ranking input *and* the headline of your search listing.
Plan for roughly 55-60 characters (the real limit is pixel width, so wide capitals truncate
earlier). **Primary term near the front**, phrased naturally, then one differentiator — the
deliverable, the audience, the format or the brand. A trailing brand name is optional: drop it on
long titles, keep it on short ones and on navigational pages. Unique on every URL; duplicate titles
are a cannibalisation tell.

| Page type | Pattern | Generic example |
|---|---|---|
| Product / commercial | `<Primary term> — <core benefit or audience> \| <Brand>` | `Job scheduling software — for field service teams \| Northwind` |
| Pricing | `<Product> pricing — <what's included>` | `Job scheduling pricing — plans, limits and setup fees` |
| Pain / problem | `<Problem phrased as searched> — <what the page gives>` | `Why technicians miss appointments — 6 causes and fixes` |
| Comparison | `<A> vs <B>: <the axis of comparison>` | `Northwind vs Ridgeline: features, pricing and fit` |
| Glossary | `<Term>: definition and example` | `Dispatch window: definition and example` |
| Guide / blog | `<How-to phrased as searched> (<qualifier>)` | `How to plan a route for 40 daily stops (step by step)` |
| Local | `<Service> in <place> \| <Brand>` | `Emergency dental care in Riverton \| Ash Lane Dental` |

### Meta description

Not a ranking factor, but a click factor — and engines rewrite it when it fails to match the query,
which is itself a signal it was not answering the search.

- Plan for roughly 150-160 characters. Unique per page; never auto-generate on important pages.
- Say what the page contains and who it is for, with the term phrased naturally (matched words are
  bolded in the listing, which aids scanning).
- One concrete specific beats one adjective: "plans, limits and setup fees" beats "great value".
- Close with a plain action prompt at the urgency pole, with the deliverable at the trust pole.

### Headings

- **Exactly one H1**, matching the page's subject and containing the primary term or a close
  variant. The logo is not the H1.
- **H2s are the page's outline**, in the order a reader needs them; H3s nest only inside an H2.
  Never skip a level for styling — size is CSS's job.
- Write headings as answers or labels a scanner can use, not clever fragments. Most readers scan
  headings and read only the section they need. Mirror the questions the SERP showed you.

### The first 100 words

- Answer the page's target query **immediately**, in a self-contained paragraph a stranger could
  quote without the rest of the page. This serves the impatient human, snippet selection, and AI
  answer engines at once — see [12-geo-ai-search.md](12-geo-ai-search.md) for how to construct and
  reuse that block.
- Include the primary term once, naturally.
- Never open with the origin story, a definition of the industry, or "In today's fast-paced world".

### Images

- **Descriptive filenames** before upload: `route-planner-map-view.png`, not `IMG_4821.png`.
- **Alt text describes the image for someone who cannot see it** — an accessibility requirement
  first, SEO benefit second. Decorative images get `alt=""`, never a keyword. "Screenshot of the
  weekly schedule view" is correct; a string of product keywords is spam.
- Compress, serve modern formats, set explicit width and height (prevents layout shift), lazy-load
  below-the-fold images only — never the largest above-the-fold image.
- Caption the genuinely useful ones; captions get read more than body copy.

### Linking within the body

3-6 contextual internal links on a substantial page, placed where a reader would want the detour,
not clustered at the bottom. **External links to real sources are a quality signal, not a leak** —
cite the standard, the study, the spec. Mark paid, sponsored or user-generated links appropriately;
selling a followed link is a policy violation with real consequences.

---

## 8. Quality signals in practice

Public quality guidance emphasises experience, expertise, authoritativeness and trustworthiness
(E-E-A-T). It is not a score you can inspect — it describes what human raters are asked to look
for. Translate it into things you literally put on a page:

| Signal | What actually goes on the page |
|---|---|
| **Experience** | First-hand detail only a practitioner would have: what went wrong, the edge case, the photo you took, the number from your own work. Generic summary of other people's articles reads as exactly that. |
| **Expertise** | A named author with a real, verifiable credential or track record, linked to an author page. "Admin" and "The Team" are anti-signals on anything consequential. |
| **Authoritativeness** | Being cited elsewhere; a consistent entity description everywhere you appear; being the site people link to for a specific thing. |
| **Trustworthiness** | Contact details, a real physical or registered address if you have one, an About page that names humans, transparent pricing, clear policies, HTTPS, working forms, and no dark patterns. |

**Concrete build list:**

- [ ] Author byline on every article, linking to an author page with a real bio and credentials.
- [ ] Published date and, when genuinely revised, a "last updated" date. Never fake a refresh.
- [ ] Sources cited and linked for factual claims; a note on how you know what you claim.
- [ ] An About page that names real people and states what the company is and is not.
- [ ] Contact details reachable in one click from every page.
- [ ] Editorial or review policy if the topic touches money, health, safety or legal matters.
- [ ] Reviews and testimonials only if real and attributable. Fabricating them is fraud, and
      marking up invented ratings in structured data is a manual-action risk.

**The higher the stakes, the higher the bar.** Content that could affect someone's money, health,
safety or legal position is held to a stricter standard by raters and readers alike. In those
categories credentials and sourcing are not decoration — they are the requirement.

---

## 9. Technical baseline

Ship all of this before you worry about anything clever. Details and code-level wiring live in
[13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md).

| Item | The rule | Common failure |
|---|---|---|
| **Crawlability** | Every public page reachable by link and allowed in `robots.txt` | Blocking a whole directory during staging and never removing it |
| **Rendering** | Public content present in the served HTML (server-rendered or pre-rendered) | Client-only rendering that leaves crawlers an empty shell |
| **Indexability** | No stray `noindex` on pages you want ranked | A site-wide `noindex` surviving launch — check this first, always |
| **HTTPS** | Enforced everywhere, HTTP redirected once to HTTPS | Mixed content; a redirect chain through http→www→https |
| **One canonical host** | Pick `www` or bare, and http→https; everything else 301s | Both hosts serving 200 and splitting signals |
| **Canonical tags** | Self-referencing on every indexable page; pointing to the original on true duplicates | Canonicals pointing to the homepage site-wide |
| **XML sitemap** | Only canonical, indexable, 200-status URLs; auto-generated from one source | Stale sitemap listing deleted or private URLs |
| **robots.txt** | Disallow private/admin/checkout/API; reference the sitemap with the live domain | A staging hostname left in the `Sitemap:` line |
| **Redirects** | 301 for permanent moves, one hop, mapped to the closest equivalent page | Chains, loops, and everything dumped on the homepage |
| **404s** | Return a real 404 status with a helpful page | "Soft 404s" returning 200 on a not-found page |
| **Pagination** | Each page crawlable with real links; unique titles; do not canonicalise page 2+ to page 1 | Infinite scroll with no crawlable links behind it |
| **Faceted / filter URLs** | Decide which combinations are indexable; block or canonicalise the rest | Millions of filter permutations eating crawl budget |
| **Mobile** | The mobile rendering is the one that counts; content parity with desktop | Hiding content on mobile that exists on desktop |
| **Core Web Vitals** | Fast largest paint, negligible layout shift, responsive to input | A hero image and font stack that push the largest paint late |
| **hreflang** (only if multi-language/region) | Reciprocal annotations across all variants plus `x-default` | One-way tags, or using it for near-identical same-language pages |
| **Structured data** | Reflects what is actually on the page; validates cleanly | Marking up content the visitor cannot see |

**Performance is a means, not an end.** Speed is a modest ranking input and a large conversion
input. Chase the fixes that a real user would feel — image weight, font loading, blocking scripts,
layout shift — and stop optimising the score once the page feels instant.
[../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md) covers keeping
the front end light by construction.

---

## 10. Getting indexed

Ranking is downstream of indexing, and indexing is not automatic. **Day one of launch:**

1. Verify in Google Search Console — DNS TXT verification is the most durable, surviving redesigns
   and platform moves.
2. Add the site to Bing Webmaster Tools (it can import the Search Console setup).
3. Submit the XML sitemap in both.
4. URL-Inspect and request indexing on priority URLs — homepage plus the handful of commercial
   pages. It is rate-limited; the sitemap covers the rest.
5. Wire **IndexNow** (a key file plus a POST on publish) so Bing and Yandex learn about new and
   updated URLs immediately, and re-ping on every content deploy that changes URLs.

**When a page will not index, check in this order:**

- [ ] Is it returning 200 to an anonymous request? (Test logged out — a logged-in session hides
      access problems and cache problems.)
- [ ] Is it blocked in `robots.txt`, or does it carry `noindex`?
- [ ] Does its canonical point somewhere else?
- [ ] Is it in the sitemap, and is the sitemap actually being read (check the report)?
- [ ] Does any internal link point to it? Orphaned pages get found slowly or never.
- [ ] Does the served HTML contain the content, or only a JavaScript shell?
- [ ] Is it a near-duplicate of another page you already have?
- [ ] Is it thin — genuinely low-value, boilerplate, or auto-generated?

"Discovered – currently not indexed" and "Crawled – currently not indexed" usually mean the engine
looked and did not think the page earned a slot. The fix is nearly always **make the page
substantially better or merge it**, not resubmit it repeatedly.

---

## 11. Off-page: why links still matter and which ones you can actually get

Links remain one of the clearest signals that someone outside your own site thinks you are worth
referencing. On a brand-new domain with none, the first genuine ones matter disproportionately.

| Legitimate source | What it takes | Why it works |
|---|---|---|
| **Original data** | Run a survey, aggregate your own anonymised usage data, benchmark something nobody has benchmarked, publish the methodology | People must cite a number's source; you become the source |
| **Digital PR** | A genuine story, a real expert, a reporter's actual beat, a fast response when a relevant story breaks | Editorial links from real publications |
| **Being genuinely quotable** | A named framework, a clear definition, a strong opinion with your reasoning shown | Writers link to the clearest explanation they can find |
| **Partnerships and integrations** | Partner directories, case studies, co-authored material, integration pages on both sides | Real relationships, real pages |
| **Communities and expert contribution** | Answering well where your buyers already ask questions; podcasts, panels, guest pieces with real substance | Slow, but the audience is exactly right |
| **Your own footprint** | Profiles, directories relevant to your industry, professional bodies, supplier and customer listings | Consistency of entity information matters more than the link |
| **Being the resource** | A free tool, calculator, template, dataset or reference table people bookmark | Tools attract links for years |

**Avoid:** bought links, private blog networks, mass guest-post spam, comment and forum drops, link
exchanges, paid directory farms, anything sold by volume. They violate the guidelines, they are
detectable at scale, and the downside — a manual action or a quiet devaluation — lands on the
domain you are trying to build.

**Two operating notes.** One editorial link from a genuinely relevant, respected site beats a
hundred from anywhere that takes anyone. And links are a *lagging* signal of doing something worth
linking to — if you cannot earn any, the honest question is "what have we published that a stranger
would want to cite?"

---

## 12. Local SEO, if the brand has a place

Only relevant when you serve customers at a location or within a service area.

- [ ] Claim and fully complete the business profile on the major map platforms — categories, hours,
      service list, real photos.
- [ ] **NAP consistency**: name, address, phone written identically on your site, every profile and
      every directory. Inconsistency is the most common local ranking problem.
- [ ] Same details in the footer and on a contact page, with `LocalBusiness` structured data
      ([13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md)).
- [ ] One page per location with genuinely local content — parking, transit, neighbourhood, the
      team at that site. Not a template with the town name swapped.
- [ ] One page per core service, plus service-and-place pages where demand justifies them.
- [ ] Ask real customers for reviews through a compliant, non-incentivised process, and reply.
      Never write, buy or filter reviews — it is fraud, and platforms remove businesses for it.
- [ ] Get listed in genuinely local sources: chambers of commerce, local press, sponsorships,
      trade bodies. Track the map pack separately; it behaves differently from classic results.

---

## 13. A realistic 0-6 month timeline

A **planning framework, not a forecast**. Pace depends on competition, category, publishing rate,
and whether the brand already has an audience. Nothing here is a guarantee, and any source quoting
you exact percentages for a generic new site is guessing.

| Window | What you do | What to expect | The trap |
|---|---|---|---|
| **Weeks 0-2** | Ship the technical baseline, verify in Search Console and Bing, submit the sitemap, publish the core commercial pages | Indexing begins on the homepage and a few key URLs. Effectively no traffic. | Concluding "SEO doesn't work" from a fortnight |
| **Weeks 2-6** | Publish the pain and glossary tiers; internal-link everything; earn the first genuine mentions | More pages indexed; impressions appear in Search Console for brand and very long-tail terms; clicks near zero | Rewriting pages weekly out of impatience — you destroy your own measurement |
| **Months 2-3** | Keep publishing on the map; start comparison pages; begin real link work | First rankings on specific, low-competition queries. Positions are volatile — this is normal for new URLs. | Chasing daily rank fluctuations |
| **Months 3-4** | Read the Search Console queries report and let it retarget you; improve the pages showing impressions but no clicks | Long-tail traffic becomes measurable and repeatable; the first conversions from search | Ignoring the queries report, which is now better data than any keyword tool |
| **Months 4-6** | Consolidate cannibalisation, deepen the winning cluster, push internal links to the money pages | A compounding curve rather than a flat line; mid-competition terms come into reach | Starting a new topic cluster before the first one is finished |
| **Beyond 6 months** | Head terms become realistic as authority accrues | — | Assuming the early curve continues without continued work |

**Leading indicators to watch before rankings arrive** (they move first): pages indexed, impressions
in Search Console, number of distinct queries the site appears for, average position on your target
cluster, and referring domains. If those are climbing, the traffic follows. If they are flat after
two months of publishing, something structural is wrong — start with indexing (§10) and intent
match (§1). Instrumentation and how to read it: [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md).

---

## 14. The black-hat list: not worth the risk

Each item below either violates search guidelines outright or degrades the site for humans. On a new
domain the asymmetry is brutal: a small temporary gain against the only asset you are building.

- Buying or selling links that pass ranking signals; private blog networks; link farms.
- Hidden text and hidden links (invisible colour, off-screen positioning, zero-size fonts).
- Keyword stuffing anywhere — body, alt text, meta keywords, footer term lists.
- Cloaking: serving crawlers different content from users, including "SEO-only" text blocks.
- Doorway pages: dozens of near-identical location or keyword pages funnelling to one destination.
- Scraped, spun, or auto-translated content published without human review or added value.
- Bulk AI-generated pages published at scale with no editing, sourcing, or first-hand substance.
  (AI-assisted writing is fine; unreviewed mass publication is the problem.)
- Expired-domain purchases repurposed to inherit unrelated authority.
- Fake reviews, invented ratings, and structured data describing things not on the page.
- Sneaky redirects that send users somewhere other than what they clicked.
- Manufactured urgency and countdowns that reset — a conversion problem and a trust problem, see
  [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md).
- Negative SEO attempts against competitors.

**The line to hold:** if a tactic only works because the engine has not noticed yet, or only works
because the user has not noticed yet, it is not a strategy — it is a debt with an unknown due date.

---

## Apply it

- [ ] Every planned URL has exactly one primary keyword and one intent class written in its page
      brief before writing starts.
- [ ] The keyword-to-URL map exists as a real file and is checked before any new page is briefed.
- [ ] Every target term's SERP has been looked at, and the page format matches what is ranking.
- [ ] Titles, metas, H1s and structured data capture the searched term; the body carries the brand
      frame and never parrots it.
- [ ] The architecture covers commercial, pain, audience, comparison, glossary and blog tiers, and
      every informational page links up to the commercial page it supports.
- [ ] Every page answers its query in a self-contained paragraph within the first 100 words.
- [ ] Exactly one H1 per page; headings form the real outline; no level skipped for styling.
- [ ] Images have descriptive filenames, honest alt text, explicit dimensions and modern formats.
- [ ] Authors are named with real credentials; dates, sources, About and contact details are
      present and true.
- [ ] The technical baseline in §9 is green, verified on a logged-out request, before launch.
- [ ] Search Console and Bing are verified, the sitemap is submitted, IndexNow is wired, and
      priority URLs have been inspected.
- [ ] The link plan uses only legitimate sources; nothing on the §14 list appears anywhere.
- [ ] Leading indicators (indexed pages, impressions, distinct queries, referring domains) are
      reviewed monthly, not daily.
- [ ] The 0-6 month expectation has been stated to whoever is funding this, so month two does not
      trigger a panic rewrite.

## Related

- [12-geo-ai-search.md](12-geo-ai-search.md) — making the same pages quotable by AI answer engines
- [13-schema-and-technical-wiring.md](13-schema-and-technical-wiring.md) — structured data, canonicals, sitemap, robots, IndexNow
- [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md) — the frame the body copy carries
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — how the on-page copy actually reads
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — the section structure behind each page type
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — what to check after the traffic arrives
- [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md) — instrumenting and reading the results
- [../ops/15-launch-checklist-and-build-order.md](../ops/15-launch-checklist-and-build-order.md) — where search work sits in the build order
- [../templates/page-brief.md](../templates/page-brief.md) — the per-page brief that records the primary keyword
- [../templates/robots.txt.example](../templates/robots.txt.example) — a starting robots file
