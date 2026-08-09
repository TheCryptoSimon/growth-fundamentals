# GEO — Getting Named and Cited by AI Answer Engines

How to become the source an AI assistant quotes when someone asks about your topic. Read this
alongside [SEO fundamentals](./11-seo-fundamentals.md) — same content, second surface, different
win condition. Assumes you already know your category, your named audience, and your one
differentiator. Nothing here works without them.

---

## 0. The shift: from a list of links to a single answer

Classic search hands the user ten options and lets them choose. An answer engine composes one
response and names a handful of sources — sometimes with links, sometimes with nothing but a brand
name in the prose. That collapses the funnel and changes the goal.

| | Classic search | Answer engine |
|---|---|---|
| Output | A ranked list | One synthesised answer |
| Slots available | ~10 on page one | Often 3–6 sources, sometimes 1 |
| What wins | Relevance + authority + links | Extractability + consistency + corroboration |
| Your unit of competition | The page | The **passage** |
| The click | The point | Optional — you can win the answer and lose the visit |
| Position measure | Rank for a keyword | Whether you are named at all, and how |

**The operating goal:** be the most *extractable*, most *consistent*, most *quotable* source on your
topic. Not merely crawlable — crawlable is table stakes. You want a machine that has read ten pages
to find that yours is the one with a clean, self-contained, checkable sentence it can lift.

**Accept the trade.** Some GEO wins produce zero sessions: the assistant answers, names you, and the
user never clicks. That is still worth having — being the named source shapes what the user believes
before they ever land on you, and it compounds with every repetition. Judge GEO on *presence in
answers*, and treat the click as a bonus. If your entire business case depends on the click, you
need the commercial pages of [SEO fundamentals](./11-seo-fundamentals.md) doing the heavy lifting,
not this document.

## 0.1 The dial for GEO

The mechanics below — direct-answer blocks, chunking, entity consistency, schema — are dial-neutral.
They apply the same to a calm/premium brand and to an energetic/playful one. What flips is the
**register of the extractable copy**.

| | **Calm / premium / trust end** | **Energetic / urgent / playful end** |
|---|---|---|
| Direct-answer wording | Declarative, specific, plain | Still declarative, specific, plain |
| Personality | Lives in the body sections | Lives in the body sections |
| Superlatives ("best", "#1", "revolutionary") | Never | Never |
| Urgency language in extractable blocks | Never | Never |
| Framework names | Sober and descriptive | Vivid and memorable, still literal |
| Voice elsewhere on the page | Reserved | Loud, allowed |

**Rule:** the answer block and the definitions are the *neutral zone* of your site. Hype does not
extract — a machine summarising "the fastest, most powerful platform ever built" gets no facts and
tends to skip the passage in favour of one that states something checkable. The inverse for an
energetic brand is not "add energy to the answer block"; it is "spend your energy on the hero, the
CTA, and the body voice, and keep the answer block clinical." See
[voice and messaging](../brand/03-voice-messaging-and-copywriting.md).

## 1. The retrieval reality — three doors, three strategies

An assistant's answer can come from any mix of three sources. You cannot tell which one fired, so
you must supply all three.

| Door | How it works | Lag | What it rewards | Your move |
|---|---|---|---|---|
| **Live retrieval** | The model issues a search at question time and reads the top results now | Minutes to days | Being retrievable *and* extractable in the fetched page | Classic SEO to get fetched; direct answers to get quoted |
| **Indexed / grounded corpus** | A pre-built index the assistant searches, or a cached crawl | Days to weeks | Clean, server-rendered, structured pages | Server render everything public; schema; sitemap; freshness |
| **Training memory** | Facts absorbed during model training, no lookup | Months to years | Repetition across many independent sources | Off-site corroboration; identical entity description everywhere |

Three consequences worth internalising:

1. **Live retrieval is the door you can move this month.** It rides on classic search, so SEO is not
   optional for GEO — it is the delivery mechanism.
2. **Training memory is the door you cannot rush.** It is bought with consistency over time and with
   third-party mentions, not with on-site edits. Start early; expect nothing for months.
3. **A model with no live access will answer anyway**, from memory, possibly wrongly. The defence is
   that every off-site profile carries the same description as your site, so the memory it forms is
   the one you wrote.

## 2. The direct-answer block — the single highest-value element

**What it is.** A self-contained, one-paragraph answer to the page's core question, placed inside
roughly the first 100 words, written so it still makes sense when it is copied out of the page and
pasted somewhere else with no surrounding context.

**Mechanism.** A retrieval system splits pages into passages and scores each passage against the
question. A passage that answers the question completely, names its subject, and depends on nothing
above it scores well and survives the copy. A passage full of "we", "this", "as mentioned above"
resolves to nothing once lifted, so it either gets skipped or gets quoted without your name attached.

**How to apply — the specification:**

| Attribute | Rule |
|---|---|
| Position | First content block after the H1; before any image, video, or long hero copy |
| Length | 40–80 words. One paragraph. Never a bullet list |
| Opening | Restate the question as a statement, then answer it in the same sentence |
| Naming | Name the brand and the category once, in full, in the first sentence |
| Pronouns | No "we", "our", "this", "it" pointing at anything outside the block |
| Specificity | At least one checkable specific: what it does, who it is for, what it costs, how long it takes |
| Claims | No superlatives, no urgency, nothing you cannot support |
| Markup | Wrap it in a stable element with a stable class or id so `speakable` can target it — see [schema and wiring](./13-schema-and-technical-wiring.md) |

**The out-of-context test.** Copy the paragraph into a blank document. If a stranger reading only
that paragraph cannot say *what the thing is, who it is for, and who makes it*, rewrite it.

**Generic worked example** (invented B2B scheduling tool):

> Weak: "We built this because scheduling is broken. Our platform fixes it — and it's the fastest
> way to book anything."
>
> Strong: "Placeholder Scheduling is an appointment-booking tool for small clinics and studios. It
> replaces phone-and-spreadsheet booking with a shared calendar, automated reminders, and online
> self-booking, and is designed for practices with one to twenty practitioners. Plans start at a
> flat monthly fee per practitioner with no per-booking charge."

The strong version names the entity, the category, the audience, the mechanism, and the pricing
model. Every one of those is a fact an assistant can reuse.

**One per page.** The homepage answers "what is [brand]". A service page answers "what is [service]
and who is it for". A glossary entry answers "what is [term]". Two answer blocks on one page split
the signal.

## 3. Chunk-level writing — every section stands alone

Retrieval works on fragments, so write fragments that survive being torn out.

| Practice | Rule | Why |
|---|---|---|
| **Headings as questions** | Phrase H2/H3 as the question a person would type or ask | The heading becomes the passage's label; question-shaped headings match question-shaped prompts |
| **Section independence** | Each section opens by restating its subject in full | A section beginning "It also handles…" is orphaned when lifted |
| **Answer-first sections** | First sentence answers the heading; the rest supports it | Machines and skim-readers both take the first sentence |
| **Sentence shape** | Subject → verb → object. One idea per sentence. Under ~25 words | Long compound sentences fragment badly and lose their subject |
| **Attribution inside the sentence** | Say who says it: "Placeholder Clinic recommends…" not "It is recommended…" | Passive claims get quoted without your name |
| **Tables** | Any comparison, spec set, or option set becomes a table | Tables extract almost perfectly; a header row labels every cell |
| **Ordered lists** | Any process becomes a numbered list with an imperative verb per step | Steps map straight onto "how do I…" prompts |
| **Section length** | 80–250 words per H2 chunk | Shorter than 80 rarely says enough; longer than ~300 gets truncated mid-idea |
| **Definitions inline** | Define a term the first time it appears on the page, even if it has a glossary entry | A lifted passage carries its own dictionary |

**Anti-pattern:** the long flowing essay with a beautiful narrative arc. It reads well to a human
who starts at the top and it extracts terribly. Write in blocks that can be shuffled.

## 4. Named frameworks as citation bait

**What it is.** Coining a labelled model for something you actually do — a loop, a stack, a ladder,
a five-step method — and repeating that exact label everywhere you appear.

**Mechanism.** A proper noun is easier for a retrieval system to attach to an entity than a generic
description is. "Three-stage onboarding" belongs to nobody. "The Placeholder Onboarding Ladder"
belongs to one entity, and any mention of it drags your name along. Named things also give
journalists, podcasters and forum posters a handle to reference, which feeds the training-memory
door in §1.

**How to apply:**

1. Find the thing you genuinely do differently — a sequence, a diagnostic, a scoring method, a
   decision rule. It must be real and describable in one paragraph.
2. Name it literally, not cleverly. The name should half-explain itself. Two to four words.
3. Write a canonical definition: one paragraph, plus a numbered breakdown of its parts.
4. Give it a **dedicated URL** with its own direct-answer block and `DefinedTerm` markup.
5. Repeat it **verbatim** — identical wording — on the pages that use it, in `llms.txt`, in your
   press boilerplate, in bios, in talks, in social profiles. Paraphrase is the enemy here.
6. Aim for three to seven named frameworks total. Twenty named things is a taxonomy nobody repeats.

**The honesty limit.** Naming a real method is legitimate branding — this is standard practice in
consultancy and in the work of writers like Aaker on brand assets. Naming something to imply
research you did not conduct is not. Never call a repackaged commonplace a "discovery", never
present a framework as validated unless you ran and can describe the validation, and never invent a
study to support it. A framework is a *lens you offer*, not evidence.

## 5. Entity consistency — one name, one paragraph, everywhere

**What it is.** A single canonical brand name and a single one-paragraph description, reproduced
character-for-character on your site and on every third-party surface.

**Mechanism.** Systems that assemble knowledge about an entity reconcile many mentions into one
record. Consistent, repeated phrasing across independent sources raises confidence and produces a
crisp stored fact. Variation produces either a hedged answer or, worse, two half-entities that each
look small.

**How to apply — the entity block.** Write it once, store it in the [brand brief](../templates/brand-brief.md),
and never let anyone improvise a new one.

| Field | Rule |
|---|---|
| Canonical name | Exact casing, exact spacing, no tagline attached. Decide about "Ltd/Inc" once |
| Alternate name | Register the common short form once, deliberately, rather than letting it drift |
| One-line descriptor | "[Name] is a [category] for [audience]." Under 15 words |
| One-paragraph description | 40–60 words: category, audience, mechanism, differentiator. This is the string you paste everywhere |
| Founding year, location | Stated identically on-site and off |
| Logo URL | One canonical file, square and wide variants |
| `sameAs` set | Every profile you control, listed on-site in schema, each linking back |

**Where it must be identical:** homepage, about page, footer, `Organization` schema, `llms.txt`,
press boilerplate, every social bio, every directory listing, every marketplace or app-store
listing, every conference speaker bio, every podcast show-notes blurb you supply.

**Drift symptoms and fixes:**

| Symptom | Cause | Fix |
|---|---|---|
| Assistant describes you as the wrong category | Different descriptors on different profiles | Re-paste the entity paragraph everywhere; audit quarterly |
| Assistant hedges: "appears to be a…" | Too few corroborating sources agree | Increase off-site presence (§10) with identical copy |
| Assistant merges you with a similarly named company | Weak disambiguation | Add location, founding year, and `sameAs` links; use the full legal name in schema |
| Assistant cites an outdated fact | Old profile never updated | Keep a list of every profile URL; update all on any material change |

## 6. Definitions and a glossary

**What it is.** A page per important term in your domain, each answering "what is X" in a
self-contained paragraph, plus an index page linking them.

**Mechanism.** Definitional prompts ("what is X", "what does X mean") are enormously common and
generic. A page that is *only* the definition, with the term as the H1 and the definition as the
first paragraph, is the cleanest possible extraction target — and it lets your commercial pages stop
trying to be dictionaries.

**How to apply:**

- One URL per term. H1 is the term alone. First paragraph is a 40–60 word standalone definition.
- Then: how it works, a worked example, common misunderstanding, related terms.
- Mark up with `DefinedTerm` inside a `DefinedTermSet`; see [schema and wiring](./13-schema-and-technical-wiring.md).
- Cover: the category terms, your named frameworks, the jargon your buyers use wrongly, and the
  terms your competitors coined that you must explain neutrally.
- Link each term up to the commercial page it supports, and sideways to two or three sibling terms.
- Start with 8–15 terms. A thin glossary of 60 stubs is worse than 10 real ones.

## 7. FAQs from one source

**What it is.** A single list of question/answer pairs per page that renders on-page **and** feeds
the structured data, generated from the same data object.

**Mechanism.** Two copies drift. Structured data that contradicts the visible page is a quality
problem for search engines and a confusion source for assistants. One array, two consumers.

**How to apply:**

- Questions come from real inputs: support tickets, sales calls, search suggest, forum threads. Not
  from a keyword tool's question list.
- Phrase them exactly as a person asks them, including the awkward phrasing.
- Answer in 40–80 words, answer-first, self-contained, no cross-references.
- 4–8 per page. Beyond that it stops being an FAQ and becomes an article.
- Every FAQ answer must be visible on the page. Hidden-only structured data is a violation and a
  reason to lose rich results entirely.
- Never repeat a keyword across questions to "cover variants" — see §12.

## 8. Freshness and dates

Assistants and their retrieval layers both prefer content that looks current, and users often ask
time-bounded questions ("in 2026", "latest", "current").

| Rule | Detail |
|---|---|
| Publish and modify dates | Visible on the page *and* in schema, and they must agree |
| Never fake a modification | Bumping the date without changing content is detectable and corrosive |
| Real review cadence | Evergreen pages: review every 6 months, change something true, then update the date |
| Say what changed | A one-line "Updated [month]: [what changed]" note is a genuine quality signal |
| Volatile facts | Prices, limits, integrations, availability: single-source them so one edit updates every page |
| Year-bound copy | Avoid "in 2026" in evergreen body copy unless the page is genuinely annual |

## 9. Crawler access

If a machine cannot fetch and parse the page, nothing above matters.

- **Server-render all public content.** Content that only exists after client-side JavaScript runs
  is unreliable for many crawlers and for most assistant fetchers. Test with JavaScript disabled: if
  the direct-answer block is missing, it does not exist.
- **No paywall, interstitial, or cookie wall over the answer block.** A consent overlay that blocks
  the first screen for a bot is a self-inflicted wound.
- **Fast, stable HTML.** Timeouts read as absence.
- **Allowlist crawlers explicitly in `robots.txt`.** Exact syntax and a full agent list are in
  [schema and wiring](./13-schema-and-technical-wiring.md) and
  [robots.txt.example](../templates/robots.txt.example).

**The training-crawler trade-off — decide it deliberately.** Two rough classes of agent exist:
those that fetch pages to answer a live question, and those that collect content for model
training. Blocking the second class does not protect you from the first, and it does not remove
content already collected.

| Choice | You gain | You give up |
|---|---|---|
| Allow both | Maximum chance of being in training memory and in live answers | Your content contributes to models with no attribution or payment |
| Allow live-answer agents, block training agents | Live citations while limiting bulk ingestion | The long-run memory door in §1 narrows |
| Block everything | Content stays out of AI surfaces | You are invisible in answers — competitors fill the slot |

**Recommendation for a new brand with no traffic:** allow both. You have nothing to protect and
everything to gain from being known. Revisit once you own proprietary data or original research
worth gating. Whatever you choose, choose it in a documented decision, not by leaving a default.

## 10. `llms.txt` — a plain-language brief for machines

**What it is.** A short markdown file at your site root that tells an AI system, in plain language,
what your brand is, what it is not, which pages matter, and what your key concepts are. It is a
convention, not a standard with guaranteed support — cheap to maintain, occasionally read, and never
a substitute for the on-page work.

**What belongs in it:**

1. Brand name, one-line descriptor, and the canonical entity paragraph from §5 — verbatim.
2. What the product **is not** (this prevents the most common category mistakes).
3. A curated list of your best pages with a one-line description each — the pages you would want
   quoted, not every URL you own.
4. Your named frameworks (§4) with their one-line definitions.
5. Your glossary index.
6. Contact and press contact.
7. A last-updated date.

**What does not belong:** every URL (that is the sitemap's job), keyword lists, marketing copy,
private or gated pages, anything untrue.

**Keeping it in sync.** Generate it from the same page registry that generates the sitemap and the
footer links — see the registry pattern in [schema and wiring](./13-schema-and-technical-wiring.md).
A hand-maintained `llms.txt` is stale within two months. Layout and a fillable version:
[llms.txt.example](../templates/llms.txt.example).

## 11. Off-site presence — the corroboration layer

Answer engines lean heavily on what *other* sources say about you. A site that praises itself and is
mentioned nowhere else reads as unverified.

| Source type | What it contributes | Effort | Honesty limit |
|---|---|---|---|
| Owned profiles (business directories, professional networks, app or plugin listings, code repositories) | Consistent entity facts, `sameAs` targets | Low, do first | Complete them honestly; no fake employee counts or founding dates |
| Review platforms | Third-party sentiment, the one place a rating can legitimately exist | Medium | **Never** solicit fake reviews, incentivise only positive ones, or write your own |
| Community answers (Q&A sites, forums, subreddits) | Natural-language mentions in the exact phrasing people use | High, ongoing | Disclose your affiliation every time. Undisclosed self-promotion is deceptive and gets punished by the community and the platform |
| Podcasts, interviews, guest articles | Long-form association of your name with your topic; repeats your frameworks | Medium | Say only what you can support |
| Original data — a survey, a benchmark, an index you actually run | The strongest citation magnet: unique facts nobody else has | High | Publish the method and sample size. If you did not run it, you do not have it |
| Digital PR / press coverage | Independent corroboration, high-trust domains | High | No fabricated milestones or invented statistics in a release |

**Original data is the highest-leverage item on that list** and the hardest. A small, honest,
repeatable annual survey with a stated method beats a hundred opinion posts, because it makes you
the only possible source for a fact.

**The line:** creating genuine mentions is marketing; manufacturing the appearance of independent
consensus — sockpuppets, undisclosed paid reviews, invented awards, self-issued "top 10" lists on
sites you secretly own — is fraud. It is also the single fastest way to have your entity flagged.

## 12. Measuring GEO

Rank tracking does not transfer. Answers are non-deterministic, personalised, and unranked. Measure
presence and share instead.

### 12.1 The prompt panel — your primary instrument

**What it is.** A fixed set of prompts, run on a schedule, across the assistants you care about,
with the results logged.

**How to build it:**

1. Write 25–40 prompts covering: category questions ("what is the best tool for X"), problem
   questions ("how do I stop X"), comparison prompts ("X vs Y"), definitional prompts ("what is
   [your framework]"), and brand prompts ("what is [brand]", "is [brand] any good").
2. Freeze the wording. Changing a prompt resets its history.
3. Run monthly at first — weekly once you are actively shipping content. Same day, fresh session,
   no personalisation, logged out where possible.
4. Log per prompt, per engine, per run:

| Field | Values |
|---|---|
| Brand named? | yes / no |
| Cited with a link? | yes / no |
| Position in the answer | first mention / middle / passing mention |
| Framing | correct category? correct audience? |
| Accuracy | any wrong facts stated about you? |
| Competitors named | which, and how many |
| Source pages cited | which URLs of yours, if any |

5. **Share of answer** = prompts where you are named ÷ total prompts, per engine. That single number
   is your GEO headline metric. Track the trend, never the absolute.
6. **Accuracy rate** = prompts where every stated fact about you was correct. A high share of answer
   with wrong facts is an emergency, not a win.

Automate it if you can; a scheduled script and a spreadsheet is enough. Manual runs of 30 prompts
take under an hour and are perfectly acceptable at the start.

### 12.2 The supporting instruments

| Instrument | What it tells you | Caveat |
|---|---|---|
| Referral traffic from AI hosts | Actual sessions from assistant surfaces | Undercounts badly — many assistants send no referrer, and answered-without-click is invisible |
| Landing pages of that traffic | Which pages are being surfaced | Small numbers; read directionally |
| Brand-mention monitoring (alerts on your name and framework names) | New off-site mentions, and misinformation about you | Set alerts on framework names too — those are your fingerprints |
| Search Console impressions on question queries | Whether question-shaped pages are being fetched at all | Proxy only; AI surfaces report inconsistently |
| Direct + branded-search volume | The real long-run outcome of being named in answers | Slow, noisy, but it is what actually pays |

**What not to do:** do not report a single lucky answer as a result, do not average across engines
into one meaningless score, and do not chase a number by asking an assistant leading questions
("tell me why [brand] is the best X") — that measures nothing.

## 13. Failure modes

| Failure | What it looks like | Why it backfires | Fix |
|---|---|---|---|
| **Thin answer-bait pages** | 40 pages, 200 words each, one question per page, no substance | Reads as low-value at scale; can drag the whole domain down | Consolidate into fewer deep pages with many well-chunked sections |
| **Keyword-stuffed FAQ blocks** | Eight questions that are the same question with rotated phrasing | Extracts as redundant noise; risks structured-data penalties | 4–8 genuinely distinct questions from real user input |
| **Contradicting yourself across surfaces** | Site says "for clinics", app-store listing says "for anyone" | Lowers confidence; produces hedged or wrong answers | The entity block in §5, pasted everywhere, audited quarterly |
| **Invented facts** | A made-up statistic, an unearned award, a fabricated study | A model repeats it confidently, third parties re-publish it, and it becomes near-impossible to retract. This is the worst failure in this document | Every number on the site has a source you can produce on demand |
| **Hype in the answer block** | "The world's most advanced platform" | Contains no extractable fact; passage gets skipped | Facts in the answer block, personality in the body |
| **JavaScript-only content** | Beautiful page, empty HTML source | Invisible to a meaningful share of fetchers | Server-render; test with JS disabled |
| **Hidden structured data** | FAQ schema for questions not on the page | Guideline violation; loses rich results | One source array, rendered and marked up |
| **Framework inflation** | Twenty named "frameworks", none used twice | Dilutes every one of them | Three to seven, repeated verbatim |
| **Chasing the click only** | Gating the answer to force a visit | You lose the citation *and* the visit | Give the answer; earn the visit with depth |
| **Set-and-forget** | Everything built, never measured | You cannot tell a win from a coincidence | The prompt panel in §12, on a schedule |

## Apply it

- [ ] Every important page has a 40–80 word direct-answer block in the first 100 words that passes the out-of-context test
- [ ] That block is wrapped in a stable selector and referenced by `speakable` in the page's structured data
- [ ] Every H2 is a question a real person asks, each section's first sentence answers it, and no section depends on the one above it — subjects restated in full, comparisons as tables, processes as numbered lists
- [ ] Three to seven named frameworks exist, each with a dedicated URL, a canonical definition, and verbatim repetition on-site and off
- [ ] One canonical entity paragraph is written down and pasted identically on-site, in schema, in `llms.txt`, and on every third-party profile
- [ ] A glossary of 8–15 real terms exists, each a standalone definition page marked up as `DefinedTerm`
- [ ] FAQs are generated from one source array that feeds both the visible page and the structured data
- [ ] Publish and modified dates are visible, accurate, and never bumped without a real change
- [ ] All public content is server-rendered and verified with JavaScript disabled
- [ ] `robots.txt` states an explicit crawler decision, and the training-crawler trade-off was decided deliberately and documented
- [ ] `llms.txt` exists, is generated from the page registry, and carries the entity paragraph, best pages, and framework definitions
- [ ] At least three off-site profiles carry the identical entity description and link back
- [ ] A frozen 25–40 prompt panel is scheduled, logged, and reports share of answer plus accuracy rate per engine
- [ ] No statistic, award, rating, or study appears anywhere that cannot be sourced on demand

## Related

- [SEO fundamentals](./11-seo-fundamentals.md) — keyword-to-URL mapping and the architecture GEO rides on
- [Schema and technical wiring](./13-schema-and-technical-wiring.md) — the markup, robots, sitemap and `llms.txt` mechanics
- [Positioning and category](../brand/01-positioning-and-category.md) — the category claim your entity description states
- [Identity, archetype and naming](../brand/02-identity-archetype-and-naming.md) — choosing a canonical name that disambiguates
- [Voice, messaging and copywriting](../brand/03-voice-messaging-and-copywriting.md) — writing claims with mechanism and proof
- [Page architecture and section recipes](../build/08-page-architecture-and-section-recipes.md) — where the answer block sits in a page
- [Conversion audit checklist](../build/10-conversion-audit-checklist.md) — the pre-ship gate this feeds into
- [Measurement and experimentation](../ops/14-measurement-and-experimentation.md) — running the prompt panel alongside your analytics
- [Launch checklist and build order](../ops/15-launch-checklist-and-build-order.md) — when in the build this work happens
- [Prompt pack](../ops/16-prompt-pack.md) — prompts for drafting answer blocks and framework definitions
- [Page brief template](../templates/page-brief.md) — where a page's direct answer and FAQ are specified
- [llms.txt example](../templates/llms.txt.example) — a fillable layout
- [robots.txt example](../templates/robots.txt.example) — the crawler allowlist
