# Page Architecture & Section Recipes

Which pages a new brand actually needs, what job each does, and a section-by-section build recipe for the ones
that carry the money. Read this after the design system exists and before anyone writes markup. Each recipe
names its **purpose**, the **lever** it pulls, what it **must contain**, and how it **fails**. Companion to
[10-conversion-audit-checklist.md](10-conversion-audit-checklist.md), the gate you run once a page is built.

## 0. Two things to settle first

**The dial.** Every recipe below has an energy setting: calm/premium/trust-first, or
energetic/urgent/playful. Decide once and hold it site-wide — mixed cues read as an unstable brand, and
instability is expensive in exactly the categories where trust is the product. Direction-dependent recipes carry
a `> Dial.` line stating both ends. **The brief:** no page gets built without a filled
[../templates/page-brief.md](../templates/page-brief.md) — most scope creep is an under-specified brief. Three
words recur below: a **primary action** is the one thing a page exists to make happen; an **assurance line** is
microcopy under a button that pre-answers the cost or risk of clicking; a **mechanism** is the concrete reason
a promise is true — a claim without one is decoration.

## 1. The one-job-per-page rule

**What it is.** Each page has one job and one primary action. Secondary paths exist but stay visually quiet.

**Mechanism.** Choice cost is real: two options at equal weight turn the decision into work, and a
meaningful share of people resolve that work by leaving. People also infer importance from their own attention —
if the eye keeps landing on one element, that element reads as "the point." Two equal buttons destroy the
inference.

**How to apply.**
- Write the job as one sentence before designing: *"This page makes a self-serve buyer start a trial."*
- One solid button style per viewport; at most one ghost or text secondary beside it.
- A page needing two jobs is two pages; a page serving two audiences converts neither — split it, or build the self-selection block (§3.9).
- Nav, footer, and consent banners count as competing actions. Audit the whole viewport.

## 2. The site map for a new brand

Rows 1–4 are the launch set; the rest can land over following weeks without blocking a launch.

| Page | Job (one sentence) | Primary action | Phase |
|---|---|---|---|
| **Home** | Tell a stranger what this is, who it's for, why it's believable, what to do next. | Main conversion | 1 |
| **Product / How it works** | Turn interest into understanding — mechanism, steps, boundaries. | Main conversion | 1 |
| **Pricing** | Let someone self-qualify on cost and pick a tier without contacting you. | Start chosen tier | 1 |
| **Contact / Legal** | Be reachable and lawful: terms, privacy, a real contact route. | Send a message | 1 |
| **Proof / About** | Establish who is behind this and why they're credible on *this* problem. | Continue to product | 2 |
| **Problem pages** | Answer one specific pain in the reader's own words, then bridge to the product. | Read the product page | 2 |
| **Comparison pages** | Serve the "X vs Y" searcher honestly, before a competitor frames you. | Trial or pricing | 3 |
| **Glossary** | Own the category's vocabulary; win definition-shaped queries and AI citations. | Read a problem page | 3 |
| **Blog / Insights** | Publish ongoing evidence that the brand knows this domain. | Subscribe / pillar page | 3 |
| **Changelog / Status** | Prove the thing is alive and maintained (software only). | None — trust artefact | 3 |

**Page-count discipline.** Seven to twelve URLs at launch. More than that before you have traffic means thin pages competing with each other and nothing ranking — depth first, breadth later.

**The four awkward ones.**
- **Problem pages** are the highest-leverage type most new brands skip. One page per named pain, titled the
  way the reader would say it aloud. A dental clinic writes *"Why does a crown feel sensitive to cold?"*, not
  *"Restorative dentistry."*
- **Comparison pages** must be fair to be useful — state where the alternative genuinely wins. A page that
  only flatters you reads as an ad, and a reader who catches one unfair line discounts the whole thing.
- **Glossary entries** are short by design: a one-paragraph direct answer, then context, then a link into
  the relevant product or problem page. [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) explains
  why answer-first is the shape engines lift.

URL and hierarchy rules live in [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md). Keep the
folder shape shallow and stable — a URL you change later is a ranking you pay for twice.

## 3. Section recipes

### 3.1 Hero

**Purpose.** Answer three questions above the fold: *what is this*, *why you*, *what do I do next*.

**Lever.** Expectation-matching and processing fluency — a visitor who understands the page in a second or
two attributes that ease to the product. Confusion at first paint is attributed the same way.

**Must contain.**
- One headline carrying the actual takeaway, not a mood. If it could sit unchanged on a competitor's site, it says nothing.
- One subhead adding the *who* and the *mechanism*, in a lighter weight than the headline.
- Exactly one primary CTA labelled with the outcome or destination ("See the live demo"), never the mechanic ("Submit").
- An assurance line directly under the button: what happens next, whether a card is needed, how long it takes. Proximity matters — words near a button fuse into the imagined act of clicking it.
- Optional trust strip: three short, literally true, concrete proofs. Facts, not adjectives.
- **Legibility over imagery, always.** If text sits on an image, the scrim must keep the *entire* text column at WCAG AA contrast, not just the headline. A subhead unreadable at one breakpoint has deleted a third of your argument.
- **LCP discipline.** The hero visual is almost always the Largest Contentful Paint element: preload it, serve it at rendered size in a modern format, set explicit width and height so nothing shifts, put a flat placeholder tint behind it, and never lazy-load it.

**Fails when.** Two solid buttons compete, so neither reads as the point. A large face hoards attention and
the CTA loses — faces attract gaze powerfully, so use gaze direction or an arrow to *point at* the CTA, not a
rival focal element beside it. The headline is a slogan and the reader still cannot say what the product does. A
carousel rotates the message before it is read. The fold is big type and no information.

> **Dial.** Calm end: one saturated accent on the CTA and nothing else, generous space, at most one gentle
> reveal on load. Energetic end: stack contrast channels — colour, size, motion — and put the offer in the headline.

### 3.2 Navigation and header

**Purpose.** Let people find the few things that matter, and act from anywhere.

**Lever.** Choice load. People apprehend a small set at a glance; past roughly four items a group starts to
feel like "a lot" and gets skipped rather than read. Grouping restores the feeling of ease even when the total
link count is higher.

**Must contain.**
- Three to five primary links. Need more? Group into ≤4 sections and reveal on demand.
- One persistent CTA in a fixed position — same place, words, and style on every page. Repetition makes it findable without thought; a redesigned button per page reads as a different offer each time.
- Descriptive labels ("Pricing" beats "Plans & Options"); a visible current-page state; a logo linking home.

**Fails when.** A mega-menu appears before there are enough pages to justify one; the sticky header eats a
quarter of a phone screen; the header CTA and the hero CTA say different things.

### 3.3 The credibility / origin band

**Purpose.** Establish standing *before* the pitch, so everything after is read by someone who has already
decided you are plausible.

**Lever.** Order effects and the credibility halo — an early "these people are legitimate" judgement colours
every later claim, including the price. The reverse holds too: a pitch delivered before any standing exists is
read defensively, and the reader spends the rest of the page hunting for the catch.

**Must contain** one of these, whichever is *honestly* available: named provenance (who built this, out of
what experience); a real checkable credential or affiliation; a verifiable usage fact stated without inflation;
client or press logos where permission exists. One compact row under the hero — a handshake, not a section.

**Fails when** it is invented. A logo strip of non-customers, a made-up user count, or a badge nobody issued
is the fastest way to lose the exact reader you wanted — and it is where persuasion becomes fraud. With no proof
yet, say what you *do* have: "Built by two clinicians who ran this by hand for four years" beats a fake number.

### 3.4 Problem articulation

**Purpose.** Describe the reader's pain more precisely than they could describe it themselves.

**Lever.** Self-reference. A specific named situation triggers "that's me," and self-generated recognition
persuades harder than any claim you make about yourself. It also earns the right to sell: a reader who feels
understood reads the pitch as help.

**Must contain.**
- Two to four concrete scenarios in the reader's vocabulary, at the level of a specific moment, not a category. *"The invoice you re-typed for the third time this month"* beats *"inefficient workflows."*
- The cost of the status quo in the reader's terms — hours, rework, risk, embarrassment.
- No solution yet. The bridge is one line at the end.

**Fails when** it becomes fear-farming. The line sits at truth plus proportion: describe consequences the
reader actually faces, at the size they are. Inflating an annoyance into catastrophe loses the customer.

> **Dial.** Calm end: understated and clinical — the precision is the persuasion. Energetic end: sharper,
> shorter, more emotional. Neither end justifies invented consequences.

### 3.5 How it works — three steps

**Purpose.** Convert interest into a believable mental model of using the thing.

**Lever.** Mental simulation: desire is roughly *imagined outcome minus imagined effort*. Make the outcome
vivid and the process feel light. Three steps is the ceiling at which a process still feels like one motion; at
five it reads as a project.

**Must contain.** Exactly three steps, each with a verb-led label, one line of what happens, and what the
reader gets at the end. Honest time or effort per step ("about two minutes"). A first step the reader could
imagine doing today with what they already have. One quiet CTA closing the sequence.

**Fails when.** The steps describe *your* internal process instead of the reader's actions; icons are
abstract and carry no meaning; the honest process is eight steps and you hid four, so onboarding contradicts the
page and trust breaks at the worst possible moment.

### 3.6 The capability / feature grid

**Purpose.** Show the scope of what the product does without becoming a spec sheet.

**Lever.** Grouping and fluency. Equal-height cards on a consistent rhythm read as a designed system; ragged
cards read as an unfinished one, and that judgement transfers to the product.

**Must contain.**
- Three, four, or six cards — never five or seven, which never balance in a grid.
- Equal heights enforced by the layout, not by copy that happens to match.
- Per card: a concrete verb-led title, one sentence of outcome, and a mechanism clause only where it earns its place. Vivid outcome, light process.
- Consistent icon treatment, or none at all. Mixed icon styles are worse than no icons.

**Fails when.** Titles are nouns ("Analytics") instead of outcomes ("See which pages lose people"); every card
is the same length of grey text so the eye has nowhere to land; or twelve features appear because the team
could not choose — twelve presented equally communicate none, so pick the four that decide the sale.

### 3.7 The interactive element or open loop

**Purpose.** Let the reader experience a fragment of the value now, and leave the resolution in the product.

**Lever.** The unresolved-task effect: an opened loop stays mentally active and pulls toward closing. A
calculator returning a personalised number, a two-question mini-assessment, a live preview — each starts
something the product finishes.

**Must contain.** A response in under a second with no signup; a result genuinely derived from the input,
not a canned output; one obvious next action at the moment of the result, when interest peaks; graceful
degradation, so a static equivalent still communicates the idea if the script fails.

**Fails when.** The interaction costs more effort than the payoff is worth (nine fields for a generic number);
the result is fake; or the widget is the page's heaviest asset and delays first paint for everyone, including
the majority who never touch it — load it after the fold.

> **Dial.** Calm end: one quiet, useful instrument — a calculator, a preview, a checker. Energetic end:
> quizzes, spinners, playful reveals. The rail is identical at both ends: the output must be real.

### 3.8 Objection handling — before the ask

**Purpose.** Answer the reasons a reader will not buy, *before* they see a price.

**Lever.** Objections raised in the reader's head but never addressed do not disappear; they harden.
Answering them first also produces a credibility halo that the pricing section inherits. And because reason-why
arguments land far better than bare assertions, every promise here needs its mechanism.

**Must contain** a row per objection, in three parts:

| Part | Shape |
|---|---|
| **The objection** | In the reader's blunt words, not softened |
| **The promise** | What is true instead |
| **The mechanism** | *Because* — the concrete reason it is true |

- Four to six real objections, taken from sales calls, support tickets, or the closest proxy you have — never from a brainstorm.
- No promise without its mechanism. "We take security seriously" is noise; "your files are encrypted before they leave your device, so we could not read them if asked" is an argument.
- Expandable rows are fine here — the one place hiding detail helps, because the reader with the objection opens it and everyone else is spared the wall.

**Fails when.** The objections are strawmen the product happens to beat; a promise is made that support
cannot keep; or the section sits after pricing, arriving too late to matter.

### 3.9 "For you if / not for you if"

**Purpose.** Let the right reader select in — and the wrong one leave without a refund request later.

**Lever.** Two-sided argument. Volunteering a genuine limitation raises the credibility of everything else
you claim, because it shows you are not simply selling. It also turns a vague "maybe" into a decision.

**Must contain.** Two columns, three to five lines each, at the *same* visual weight — the "not for you"
side must not be a token whisper. Real exclusions with teeth: a team size, a budget floor, a workflow you
genuinely do not support, a case where a competitor or a free tool is the better answer. Placed immediately
before pricing.

**Fails when** the exclusions are humblebrags ("not for you if you don't want results"). That inverts the
effect — the reader notices the dodge and discounts the rest of the page.

### 3.10 Social proof

**Purpose.** Show that people like the reader already made this decision and were fine.

**Lever.** Social validation is strongest under uncertainty and strongest from a *similar* other. A quote
from someone the reader recognises as themselves outperforms a more impressive one from someone they don't.

| Usable testimonial | Decorative testimonial |
|---|---|
| Names a specific situation and a specific change | "Great service, highly recommend" |
| Attributable — real name, role, company or city | Initials, or nothing |
| Mentions a hesitation that was overcome | Uniform praise |
| Sounds like a person wrote it | Sounds like marketing wrote it |
| Sits next to the claim it supports | Parked in a carousel nobody scrolls |

**How to apply.** Place each quote adjacent to the claim it proves, not in one undifferentiated wall. Three
specific quotes beat twelve generic ones. Collect for specificity: *"What were you doing before?"*, *"What
almost stopped you?"*, *"What changed?"* Show ratings only if a real, checkable platform issued them, and link
out. With none yet, say what you have — a pilot, a waitlist, a founder's track record — and never fabricate;
invented proof is the fastest way to make a trust-first brand unsalvageable.

**Fails when.** It auto-rotates (each quote gets a fraction of a read); the photos are obviously stock; or
every quote praises the same thing, which reads as coached.

### 3.11 The pricing section

**Purpose.** Let a qualified reader choose a tier and start, unaided.

**Placement.** After the product has been *felt* — post problem, post how-it-works, post objections. On a
dedicated pricing page, invert this: prices must be visible on load, because that is what the visitor came for,
and making them scroll violates the expectation they arrived with.

**Must contain.** Three tiers at most for self-serve; past four, comparison becomes work. The intended tier
centre-stage and visually isolated with an honest label ("Most teams start here"). One CTA per card, only the
intended tier's button solid. Every difference visible without a click, identical rows collapsed into an
"included in every plan" strip. Billing period, currency, and what happens after a trial, stated plainly.
Number formatting, anchoring, and tier naming belong to
[../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md).

**Fails when.** "Contact us" is the only option for a self-serve product; a mandatory fee appears at
checkout; or a countdown or "3 seats left" badge appears that isn't true. Manufactured scarcity is a lie about
the world, and it is the tactic most likely to be caught.

### 3.12 The FAQ that doubles as structured data

**Purpose.** Clear the last practical blockers and, in the same markup, hand search and answer engines a
clean question-and-answer pair.

**Lever.** Questions in the reader's own phrasing are fluent to process and easy for a machine to lift
verbatim. Question-shaped headings also sit close to how people actually query.

**Must contain.** Six to ten real questions phrased as a person would type them. The direct answer in the
first sentence, then detail — never preamble first. Answers complete on their own, without the surrounding page
for context. The same content in the DOM as in the structured data — mismatched markup is a policy violation,
not a clever trick; wiring is in [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md).
All items rendered in HTML even when visually collapsed.

**Fails when.** It's a second sales pitch in question form; it dodges the question everyone actually asks
(refunds, cancellation, what it doesn't do); or the accordion loads by script, so crawlers see empty panels.

### 3.13 The final CTA

**Purpose.** Convert at the moment of peak understanding.

**Lever.** People judge an experience heavily by its most intense moment and by its ending. The last section
*is* the ending, so it restates the strongest single idea rather than introducing a new one. Pair it with a
freedom-to-choose line: explicitly acknowledging the reader is free to decline reduces the resistance a hard
close provokes.

**Must contain.** One sentence restating the core outcome — the hero's promise in different words. The same
primary action, same label as the header CTA. The assurance line repeated ("Two minutes. No card. Cancel any
time."). A freedom-to-choose clause ("no commitment," "leave whenever"). Nothing else: no new features, no
last-minute offer, no second button.

**Fails when** it introduces a new idea, stacks three actions, or applies pressure you cannot back up.

> **Dial.** Calm end: quiet restatement, generous space, gentle language. Energetic end: bolder line, larger
> button, and deadline framing *only* where a real deadline exists.

### 3.14 The footer

**Purpose.** Catch the reader who scrolled past the ask, and carry the obligations. **Must contain:** grouped
navigation repeat (≤4 per group), a contact route, legal links, any required disclaimer stated plainly rather
than buried, and the copyright line. One quiet CTA is fine; a loud one is not.

**Fails when.** It's a link farm built for crawlers; the disclaimer is set in unreadably small grey type, which
reads as concealment; or it's noisier than the final CTA above it.

## 4. Forms and input design

Forms are where motivated people quit. The interface does the thinking; every field is necessary or gone.

| Principle | The rule |
|---|---|
| **Field-count discipline** | Every field must justify itself against a drop in completion. If nobody uses the data this week, delete the field. |
| **One column** | Single-column layouts are scanned faster and misread less. Exception: genuinely paired fields (city/postcode, expiry/CVC). |
| **Label placement** | Labels above fields, always visible. Placeholder-as-label vanishes exactly when it's needed and destroys review-before-submit. |
| **Minimise memory** | Never make someone hold a value from a previous step in their head. Show it. |
| **Minimise calculation** | Compute totals, dates, durations, conversions for them. Show "3 days ago", not a date they must subtract from today. |
| **Forgiving formats** | Accept spaces, dashes, brackets, mixed case in phone numbers, cards, postcodes. Normalise silently server-side. |
| **Sensible defaults** | Pre-fill country, currency, timezone, and the most common option — each trivially changeable. |
| **Prevent, don't scold** | Offer only valid inputs: disable unavailable dates, disable the button after first click, enable dependent fields only when relevant. |
| **Inline validation** | Validate on blur, not every keystroke. Confirm success as visibly as you flag failure. Show password rules as they are met, not after submitting. |
| **Error copy** | Say what to do next and drop the "you" — *"Enter an email address"*, not *"You forgot your email."* Preserve everything already typed. |
| **Required vs optional** | Mark whichever set is smaller, consistently. |
| **Tap targets** | At least ~44×44 CSS pixels, with generous spacing between adjacent controls. |
| **Grouping** | Labels close to their fields; related fields grouped by proximity; more than ~6 fields gets a subheading. |
| **Progress** | Multi-step forms show which step this is and how many remain. Never surprise someone with step 5. |
| **Escape routes** | Offer undo; skip confirmation on easily reversible actions; require deliberate confirmation only for genuinely irreversible ones. |

**Field-count reality check.** Every field is a small tax. For a first contact the right count is almost always
email alone, or email plus one qualifier — progressive profiling beats a long form that filters out people who
would have converted.

> **Dial.** This barely moves. Calm brands swap alarm-red validation for a calmer caution colour plus an
> icon; energetic brands can be louder. Everything else is universal.

## 5. Mobile-first ordering

Design the small screen first; treat the large screen as the enhanced case. What actually changes:

- **The fold is roughly a third the size.** Headline, subhead, CTA, assurance line. Everything else waits.
- **Columns become a stack, and stacking changes the argument's order.** Set the mobile order explicitly rather than accepting whatever the grid emits. A row reading left-to-right on desktop must still make sense read top-to-bottom.
- **Focal-point count multiplies** — one focal element on desktop becomes three after stacking. Re-audit.
- **A sticky bottom CTA bar is usually worth its screen cost** — but only one, and it must never cover form fields or the footer's legal links.
- **Collapse peripheral detail** into accordions, provided the content is in the HTML.
- **Hover does not exist.** Anything revealed on hover needs a tap equivalent, and pages with click-delay scripts must still respond to the very first tap.
- **Tables and wide media scroll inside their own container** — the page body never scrolls sideways. Test at a real small width (~360–390 px) with a device profile, not a narrowed desktop window.

## 6. Speed is a conversion and a trust variable

**What it is, and why.** Load performance is not an engineering vanity metric: slow pages lose people before
the argument starts, and a sluggish interface is read as evidence of a sloppy product. Waiting costs attention
and raises irritation, and irritation gets misattributed to whatever is on screen — while the same fluency
effect that makes clear copy feel truer makes a fast interface feel competent.

**Targets** — Google's published Core Web Vitals thresholds, on real devices at the 75th percentile:

| Metric | Target | Practically |
|---|---|---|
| **LCP** — largest contentful paint | ≤ 2.5 s | Usually the hero image or headline. Preload it; never lazy-load it. |
| **INP** — interaction to next paint | ≤ 200 ms | The first tap must feel instant. Heavy main-thread scripts break this. |
| **CLS** — cumulative layout shift | ≤ 0.1 | Reserve space for images, embeds, banners, and late-loading fonts. |

**Practical rules.** Serve images at rendered size, in a modern format, with explicit dimensions. Self-host
and subset fonts, limit to two families and few weights, use `font-display: swap` with a metric-matched fallback
so swapping doesn't shift layout. Third-party scripts are the usual culprit — every tag needs a named owner and
a reason, audited quarterly. Defer everything below the fold (chat, video, maps, toys), and honour
`prefers-reduced-motion`. Where a wait is unavoidable, use skeleton placeholders rather than a spinner, and
never start a progress indicator at zero.

## 7. Assembly order — calm versus energetic homepage

Same sections, different sequence and weighting. Pick the column matching your dial.

| # | Calm / premium / trust-first | Energetic / urgent / playful |
|---|---|---|
| 1 | Hero — clear claim, one CTA, assurance line | Hero — offer in the headline, bold CTA |
| 2 | Credibility / origin band | Social proof volume (logos, counts — if true) |
| 3 | Problem articulation | The offer detail and what's included |
| 4 | How it works, three steps | Capability grid, benefit-led |
| 5 | Capability grid | How it works, three steps |
| 6 | Interactive element / open loop | Interactive element / quiz |
| 7 | Social proof beside the claims it supports | Pricing with anchor and comparison |
| 8 | Objection handling with mechanisms | Objection handling, condensed |
| 9 | For you if / not for you if | Testimonials, dense |
| 10 | Pricing | FAQ |
| 11 | FAQ | Final CTA, with a real deadline if one exists |
| 12 | Final CTA — peak-end, freedom to choose | Footer |
| 13 | Footer | — |

**What actually differs.** The calm build spends its first three sections earning the right to pitch and delays
price until the product has been felt; the energetic build leads with the offer and repeats it, because its
visitor arrived with intent and a short window. Both carry objection handling before the ask, both carry an
honest FAQ, and neither invents proof or urgency — those three are not dial-dependent.

## 8. Skeletons for the secondary pages

| Page | Section order |
|---|---|
| **Problem page** | Question-shaped H1 → direct answer in the first paragraph → why it happens → what to do → where the product fits (one honest paragraph) → related problems → quiet CTA |
| **Comparison page** | Who each option suits → honest at-a-glance table → where the alternative genuinely wins → where you win, with mechanisms → a decision rule → FAQ → CTA |
| **Glossary entry** | Term as H1 → one-paragraph definition a stranger could quote → context and common confusion → a worked example → links to related terms and the product page |
| **Blog post** | Takeaway-carrying title → what the reader gets, in one line → scannable body with meaningful subheads → summary → one relevant CTA, not a generic one |
| **About** | Why this problem, for this team → what you actually do → who is behind it, named → how you work → contact |
| **Pricing page** | Prices visible on load → tier comparison → included-in-everything strip → objection rows → FAQ → CTA |

## Apply it

- [ ] Each page has one written job sentence and exactly one primary action.
- [ ] The site map is 7–12 URLs at launch, with growth pages scheduled rather than crammed in.
- [ ] The hero answers what / why you / what next, and the entire text column passes AA contrast.
- [ ] The LCP element is preloaded and sized; the page hits LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1 on mobile.
- [ ] Navigation is 3–5 primary links with one persistent CTA in a fixed position on every page.
- [ ] A credibility band appears before the pitch, and every element in it is literally true.
- [ ] Every promise on the page is followed by its mechanism ("because…").
- [ ] Objection handling and the "not for you if" block both sit *before* pricing.
- [ ] Every testimonial names a situation and is attributable; nothing on the page is invented.
- [ ] The FAQ answers the awkward questions, is in the DOM when collapsed, and matches its schema.
- [ ] The final CTA restates the core outcome, repeats the assurance line, and gives freedom to choose.
- [ ] Forms are single-column with visible labels, sensible defaults, forgiving formats, inline validation, and no field failing the "who uses this data this week" test.
- [ ] The mobile stacking order was set deliberately and re-audited for focal-point count at ~375 px.
- [ ] The assembly order matches the chosen dial, and no urgency or scarcity claim exists that isn't true.

## Related

- [09-design-system-and-tokens.md](09-design-system-and-tokens.md) — build the tokens before the pages
- [10-conversion-audit-checklist.md](10-conversion-audit-checklist.md) — the pass/fail gate for everything above
- [../psychology/04-persuasion-core.md](../psychology/04-persuasion-core.md) — the levers each recipe pulls
- [../psychology/05-visual-attention-and-layout.md](../psychology/05-visual-attention-and-layout.md) — focal points, salience, scanning
- [../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md) — the materials these sections use
- [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md) — how to set and present the number
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — the words that fill these slots
- [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md) — URL structure, internal linking, page mapping
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — why answer-first sections get cited
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — FAQ and page structured data
- [../templates/page-brief.md](../templates/page-brief.md) — the spec to fill before building any page
- [../ops/15-launch-checklist-and-build-order.md](../ops/15-launch-checklist-and-build-order.md) — the order to build it all in
