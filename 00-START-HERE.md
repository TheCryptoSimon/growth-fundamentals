# Start Here — the operating manual

The one file to read before any pixel, any page, or any line of copy exists. It locks the five decisions the
rest of the library depends on, gives you the mental model that predicts most of the tactics in this pack,
and defines what "done" means for a new brand's first site. If you are an AI agent, read this in full and do
not begin building until the five decisions below are answered in writing.

---

## How to use this file

**Founder:** work through the five decisions and write the answers into
[templates/brand-brief.md](templates/brand-brief.md). Nothing downstream is worth doing until they exist.

**AI agent:** treat the brand brief as the only source of truth for brand decisions. If an answer is
missing, stop and ask. You may choose *implementations* (a grid, a component name, a spacing value); you may
not choose *positioning, promise, energy level, or price* — those belong to a human.

**Precedence, when two things in this pack disagree.** Documents in this library overlap deliberately, and
overlapping documents drift. Resolve conflicts in this fixed order, and do not average two rules together:

1. **The honesty rails** ([Part 4](#part-4--non-negotiable-honesty-rails)) beat every tactic, everywhere.
2. **The brand brief** beats any default in the pack — it is the specific case.
3. **The canonical numbers** in [Part 6](#part-6--canonical-numbers-one-value-each) beat any number stated
   loosely elsewhere.
4. **The deep doc beats the summary.** On typography, `psychology/06` outranks a passing mention in
   `build/10`; on pricing, `psychology/07` outranks `build/08`. The document whose subject it is, wins.
5. **Still ambiguous?** Pick the more conservative option, write down which you picked and why, and flag it
   — a silently-resolved contradiction is how a defect gets inherited by every page after it.

---

## Part 1 — The five decisions before any pixel

These five compound. Getting decision 1 wrong makes decisions 2–5 unanswerable, and it will show up months
later as a site that is well-built and does not work.

### Decision 1 — Who exactly is it for

**What it is.** A single primary buyer, described by their situation, not their demographics.

**Method.**
1. Write one sentence in this shape: *"[Role] who [situation], and who is currently [imperfect workaround]."*
2. Apply the **twenty-names test**: could you, this week, list twenty real people or organisations who match?
   If not, the definition is a mood, not a market.
3. Write the **trigger moment** — the specific event that sends someone looking. Nobody wakes up wanting
   your product; they hit a moment. A dental clinic's trigger is a cracked tooth, not "dental health."
4. Name one adjacent audience you are explicitly **not** serving yet. Refusing an audience is what makes the
   copy sound like it was written for someone.

**Fail states.** "Small businesses." "Anyone who wants to grow." "B2B and B2C." Breadth here is not
ambition, it is a postponed decision, and the site pays for it.

**Output artifact.** One primary-buyer sentence, one trigger moment, one excluded audience.
**Deep doc:** [brand/01-positioning-and-category.md](brand/01-positioning-and-category.md).

### Decision 2 — What category you are entering or creating

**What it is.** The mental shelf a first-time visitor puts you on in the first three seconds. They will put
you on one whether you choose it or not.

**Method.**
1. Complete the frame: *"[Brand] is a **[category]** for **[buyer]** that **[differentiator]**."*
2. Choose the strategy, knowing the cost of each:

| Strategy | You get | You pay |
|---|---|---|
| **Enter an existing category** | Instant comprehension, existing search demand, obvious comparisons | You must win on a differentiator, and you inherit the category's price expectations |
| **Create a new category** | You define the criteria and the comparison set | You must teach the category before you can sell in it, and there is no search demand yet |

3. If entering: name the two or three alternatives the buyer is realistically weighing, including "do
   nothing" and "a spreadsheet." Most losses go to inertia, not to a competitor.
4. If creating: write the one-sentence definition and repeat it everywhere — a category you name
   inconsistently is a category nobody learns.

**Rule of thumb.** Create a category only when the existing label actively misleads buyers about what you
do. Otherwise enter the obvious one and win inside it: comprehension is cheaper than education.

**Output artifact.** The completed category frame plus the real alternative set.
**Deep docs:** [brand/01](brand/01-positioning-and-category.md), then
[brand/02](brand/02-identity-archetype-and-naming.md) for the name.

### Decision 3 — The one promise

**What it is.** The single claim the brand stakes itself on. One sentence. Everything else on the site is
evidence for it.

**Method.**
1. Draft it as: *"You get [specific outcome] without [the cost or friction they expect]."*
2. Apply the **inversion test**: could a credible competitor claim the opposite and still sound sane?
   "Fast, reliable support" fails — nobody promises slow, unreliable support. "A named engineer answers,
   not a queue" passes, because "a large team answers whoever is free" is a real, defensible opposite.
3. Attach a **mechanism** — the structural fact that makes it possible. A promise without a reason is a
   slogan, and buyers accept claims far more readily when the causal chain is visible.
4. Apply the **falsifiability test**: could a customer prove you broke it? If nothing could count as a
   breach, it is decoration.

**Worked example (invented, generic).** An online-course business promises "you finish it." Mechanism: one
lesson releases per week alongside a live cohort call, because unfinished self-paced courses are
overwhelmingly an isolation problem. A competitor can genuinely disagree with that, and a customer can tell
whether it held.

**Output artifact.** One promise sentence, one mechanism sentence, one falsification condition.
**Deep doc:** [brand/03-voice-messaging-and-copywriting.md](brand/03-voice-messaging-and-copywriting.md).

### Decision 4 — The energy target on the dial

**What it is.** Where the brand sits on a spectrum from **calm / premium / trust-first** to
**energetic / urgent / playful**. This single setting flips roughly half the tactics in this library.

**Method — score the purchase, not your taste.** Give each a 1–5:

| Question | 1 = calm end | 5 = energetic end |
|---|---|---|
| What does the buyer risk if it goes wrong? | Money, health, reputation, data | Little — small, reversible |
| How long do they consider before deciding? | Weeks, with others involved | Seconds, alone |
| Is the purchase reasoned or impulsive? | Researched, compared | Felt, spontaneous |
| Is the value serious or entertaining? | Consequential | Fun, expressive |
| Who signs off? | A committee or a cautious individual | The buyer, instantly |

Average the five. **1–2.4 → calm end. 2.5–3.4 → middle, lean calm. 3.5–5 → energetic end.**

**Why it matters.** Most published conversion tactics were developed on high-arousal retail — saturated
colour, urgency language, tight layouts, grabbing motion. Those levers raise arousal, and arousal helps an
impulse purchase while actively hurting a considered one. Energy is a setting you choose, not a quality you
maximise.

**The inversion table — read this before applying any tactic in the pack:**

| Lever | Calm / premium / trust-first | Energetic / urgent / playful |
|---|---|---|
| Colour saturation | Muted field; one saturated accent, spent on the primary action | Saturated throughout; multiple bright accents |
| Colour temperature | Cool or warm-neutral | Warm, activating |
| Whitespace | Generous; crowding reads cheap | Tighter; density reads busy and alive |
| Motion | One gentle reveal at most; respect reduced-motion settings | More movement, faster onsets |
| Urgency | None manufactured; only genuine, stated deadlines | Time-boxed offers, if literally true |
| Type weight | Light to medium; bold reserved for one focal element | Heavier, more contrast |
| Price format | Round numbers, calm presentation | Charm endings, deal framing |
| Copy register | Specific, plain, mechanism-led | Punchier, more exclamatory |
| Social proof | Depth: a few detailed, verifiable accounts | Breadth: volume and activity signals |

**Neither end licenses dishonesty.** The energetic column allows urgency only where a deadline is real.

**Output artifact.** A number 1–5 and one sentence explaining it.
**Deep docs:** [psychology/05](psychology/05-visual-attention-and-layout.md),
[psychology/06](psychology/06-color-and-typography.md), [build/09](build/09-design-system-and-tokens.md).

### Decision 5 — Business model and price ladder

**What it is.** How money arrives, and the two or three rungs a buyer can stand on.

**Method.**
1. Pick the **shape**: one-off purchase, subscription, usage-based, service retainer, marketplace take rate,
   or a free tier feeding a paid core. The shape sets the site's job — a subscription site must reduce
   perceived commitment; a one-off purchase site must justify a single decision.
2. Build **three rungs, not seven**: a low-commitment entry, the tier you actually want most people on, and
   a higher tier that gives the middle one context. Name what each is *for*, not what it contains.
3. Set the number by evidence — what buyers pay for the workaround today, tested across a small range, and
   anchored against the **category you want to be compared with**, not a cheaper one that shares nothing
   but a screen.
4. Decide **what is free and why** (free should remove a specific unknown, not just cost less), and write
   the **refund and cancellation policy now** — it is a positioning decision and it changes the copy.

**Output artifact.** Model shape, three named rungs with prices, what is free, refund policy.
**Deep doc:** [psychology/07-pricing-psychology.md](psychology/07-pricing-psychology.md).

### The five decisions at a glance

| # | Decision | Output artifact | Deep doc |
|---|---|---|---|
| 1 | Who exactly | Buyer sentence, trigger moment, excluded audience | [brand/01](brand/01-positioning-and-category.md) |
| 2 | Category | Category frame + real alternative set | [brand/01](brand/01-positioning-and-category.md), [brand/02](brand/02-identity-archetype-and-naming.md) |
| 3 | The one promise | Promise + mechanism + falsification condition | [brand/03](brand/03-voice-messaging-and-copywriting.md) |
| 4 | Energy target | A 1–5 score with one line of reasoning | [psychology/05](psychology/05-visual-attention-and-layout.md), [psychology/06](psychology/06-color-and-typography.md) |
| 5 | Model + ladder | Shape, three rungs, free tier, refund policy | [psychology/07](psychology/07-pricing-psychology.md) |

---

## Part 2 — The three engines everything reduces to

Almost every tactic in this library is a surface expression of one of three underlying mechanisms. Learn
these and you can derive tactics you have never read, and — more useful — spot when a popular tactic will
backfire on your particular brand.

### Engine 1 — Ease of processing

**The mechanism.** When something is easy to perceive and understand, that ease *feels* good, and people
misattribute the good feeling to the thing itself. Easy-to-read claims are judged more believable.
Easy-to-scan layouts are judged more competent. The judgement happens before any conscious evaluation.

**What turns it up.** Legible type at generous size. Familiar page structures. Headlines that carry the
point rather than label the section. One idea per section. Meeting expectations on arrival — a pricing page
that shows prices immediately, a contact page with a form above the fold. Consistent spacing, so the eye
stops re-learning the layout.

**What kills it.** Clever navigation labels. Low-contrast text. Jargon before the plain version. Three
competing calls to action. Animation that delays content. A hero that describes a feeling instead of saying
what the product is.

**The trap.** Ease makes things *feel* true, which is why it must be paired with real substance. A beautiful
page for a weak claim converts once and refunds later.

### Engine 2 — Association spillover

**The mechanism.** Every element on a page drags its existing associations onto the brand. A rounded shape
carries softness. A serif carries tradition and institutional weight. A cool colour carries calm. Stock
photography carries genericness. These transfers are automatic and additive, and the reader has no idea it
is happening — which is why unmanaged spillover is where most amateur sites lose.

**What turns it up.** Choosing every element for the concept you want borrowed rather than for whether you
personally like it, and repeating the same associations across colour, type, imagery, name, and word choice
so they compound. Concrete, domain-specific imagery instead of abstract gradients.

**What kills it.** Contradictory cues — a premium palette in a crowded discount-shop layout, photography
whose setting fights the promise, a playful name over an enterprise-serious product, unrecognised trust
badges that transfer only "someone told them to add badges."

**Use it as a checklist.** For every element, ask: *what does this make the brand seem like to someone who
is not reading carefully?* If the answer is off-brand, change it.

### Engine 3 — Simulated outcome minus simulated effort

**The mechanism.** People decide by running a quick mental film: what will I get, and what will it take? The
felt result is roughly *vividness of the imagined outcome* minus *weight of the imagined effort*. Both halves
are imagined, which means both halves are yours to influence honestly.

**What turns up the outcome half.** Concreteness — specific nouns and observable results, not abstract
benefits. Second person, present tense. A picture of the state *after* the product has worked, and the
product shown in use rather than in isolation.

**What turns down the effort half.** Naming the number of steps. Stating setup time truthfully. Removing
form fields. Answering the friction question right next to the button — the small line under a call to
action that pre-empts *what happens when I click* often does more work than the button label itself.

**Why it predicts so much.** Free trials, demos, three-step diagrams, onboarding checklists, "no card
required," and interactive tours are all one move: raise the imagined outcome, lower the imagined effort.

### The engines as a diagnostic

| Symptom | Likely engine at fault | First fix |
|---|---|---|
| High traffic, high bounce, no scroll | Ease of processing | Rewrite the hero to say plainly what it is and who it is for |
| Visitors read a lot, then leave | Simulated effort too high | Show the steps, cut the friction, answer the cost question near the action |
| "Looks nice, feels generic" | Association spillover | Replace stock elements with domain-specific ones; commit to one personality |
| Clicks the button, abandons the form | Simulated effort | Cut fields, show progress, state what happens next |
| Reads the claim, does not believe it | All three | Add the mechanism, then the evidence, then simplify the sentence |

---

## Part 3 — Order of operations: zero to launched

Each phase has a gate. Do not start the next phase until the gate passes. Skipping a gate does not save
time; it moves the cost to rework.

| Phase | Do | Gate before moving on |
|---|---|---|
| **0. Decide** | The five decisions above | [templates/brand-brief.md](templates/brand-brief.md) is filled in by a human |
| **1. Name & identity** | Name generation, screening, archetype ([brand/02](brand/02-identity-archetype-and-naming.md)) | Name is legally and technically clear; domain and handles are secured |
| **2. Message** | Message hierarchy, headline set, objection list ([brand/03](brand/03-voice-messaging-and-copywriting.md)) | Every claim has a mechanism and a proof source |
| **3. Design system** | Tokens, colour, type, spacing, components ([psychology/06](psychology/06-color-and-typography.md), [build/09](build/09-design-system-and-tokens.md)) | Tokens exist in code; contrast passes AA; energy target is visible in the tokens |
| **4. Architecture** | Page map, one primary keyword per URL ([search/11](search/11-seo-fundamentals.md), [build/08](build/08-page-architecture-and-section-recipes.md)) | No two pages compete for the same query; every page has a job |
| **5. Home + core page** | Build the two pages that carry the promise ([build/08](build/08-page-architecture-and-section-recipes.md)) | [build/10](build/10-conversion-audit-checklist.md) passes on both, desktop and mobile |
| **6. Supporting pages** | Pricing, about, contact, proof, FAQ, legal | Each has a page brief; each passes the audit |
| **7. Search & AI wiring** | Schema graph, sitemap, robots, `llms.txt`, canonicals ([search/13](search/13-schema-and-technical-wiring.md), [search/12](search/12-geo-ai-search.md)) | Structured data validates; no private routes in the sitemap |
| **8. Measurement** | Analytics, events, one primary conversion ([ops/14](ops/14-measurement-and-experimentation.md)) | The primary conversion fires correctly in a real test |
| **9. Pre-launch** | Full audit, performance, accessibility, legal review ([ops/15](ops/15-launch-checklist-and-build-order.md)) | The definition of done below is fully green |
| **10. Launch** | Ship, submit sitemap, request indexing | Live URLs return 200 and render the same content to a logged-out visitor |
| **11. Learn** | Read behaviour, fix the largest leak, repeat | One change at a time, with a measurement window |

**Two ordering rules people break constantly.** Tokens come before pages, or every page invents its own
spacing scale. Keyword-to-URL mapping comes before content, or you write two pages that compete and both
lose.

---

## Part 4 — Non-negotiable honesty rails

These override every tactic in this library. If a technique in any document conflicts with a rail, the rail
wins.

- **No invented numbers** — no percentages, user counts, ratings, or growth figures you cannot source on
  request. A missing number beats a decorative one.
- **No fabricated proof** — no sample testimonials, no placeholder reviews shipped to production, no logos
  of organisations that are not customers, no borrowed credentials.
- **No manufactured scarcity or urgency** — no resetting countdown, no uncounted "seats left," no offer that
  expires forever. Genuine deadlines and genuine limits may be stated plainly.
- **Every promise carries its mechanism.** If you cannot say why it is true, do not claim it.
- **Comparisons must be checkable** — real, current, correctly-described alternatives only.
- **Privacy copy must match the actual data flow.** A site loading third-party trackers does not get to say
  it does not track you.
- **No dark patterns.** Cancelling is as easy as signing up; consent boxes start unchecked; the declining
  option is real and findable, not a guilt-worded link.
- **Generated content still needs a human owner.** If an agent wrote it, a human read it before it shipped.

**Where the line sits.** A technique is legitimate when it helps a well-informed person decide faster and
they would still endorse that decision a month later. It becomes manipulation when it only works while the
person is confused, rushed, or misinformed — when clarifying the situation would reverse the choice.
Practical test: *if I explained this technique to the buyer, would they feel helped or tricked?*

---

## Part 5 — Definition of done for a new brand's first site

A first site is done when all of the following are true. Not "when it looks finished."

**Clarity** — a stranger can say what it is, who it is for, and what to do next within roughly five seconds
of the home page loading; the one promise sits above the fold in the brand's own words; every page has
exactly one primary action and it is the most visually prominent thing on the screen.

**Substance** — every claim has its mechanism stated near it; every number, quote, and credential is real
and sourceable; the pricing page shows prices without interaction and says what happens after purchase;
objections are answered before the ask rather than left for the buyer to raise.

**Craft** — the design system exists as tokens and no page hard-codes a colour or spacing value outside it;
text contrast passes AA including over images; a small viewport is verified rather than assumed, with no
horizontal scroll; motion matches the energy target and respects reduced-motion preferences; the console is
clean on every page.

**Findability** — one primary keyword per URL with no two pages competing; structured data validates and
resolves to one connected entity graph; `sitemap.xml`, `robots.txt`, and `llms.txt` exist, agree with each
other, and exclude private routes; each important page opens with a self-contained, quotable answer to the
question it targets.

**Accountability** — analytics is live, the primary conversion event has fired in a real test, and someone
owns that number; legal pages exist and describe what the site actually does; the
[build/10](build/10-conversion-audit-checklist.md) audit has been run and every failure is either fixed or
written down as a known, accepted gap.

If any of these is false, the site is not done — it is launched, which is a different word.

---

## Part 6 — Canonical numbers: one value each

Several quantities recur across this library, and a pack that states the same number three ways teaches an
agent to pick whichever it saw last. These are the values that win. Where a deep doc gives a range for a
specific case, the range must sit inside these bounds.

| Quantity | Canonical value | Where it is used |
|---|---|---|
| Peer items in one visible, comparable group | **≤ 4** — chunk into labelled groups of ≤4 beyond that | `psychology/04`, `psychology/05`, `build/10` |
| Cards in a scannable feature grid (not a comparison set) | 3, 4 or 6 — never 5 or 7. Above 4, they must be *browsed*, not *compared* | `build/08` |
| Bullets in a list | 3–5 for a persuasive list; up to ~7 for a reference list nobody has to weigh | `brand/03`, `psychology/06` |
| Self-serve pricing tiers | **3**, plus at most one "talk to us" tier | `psychology/07`, `build/08` |
| Direct-answer block | **40–70 words**, one paragraph, inside the first 100 words. A glossary entry's opening definition is one of these | `search/12`, `build/10`, `templates/page-brief` |
| FAQ answer | **40–80 words**, answer-first, self-contained | `search/12`, `search/13`, `ops/16` |
| Canonical entity paragraph | **40–60 words** — it goes in `Organization.description`, so it must stay short | `brand/02`, `search/12`, `templates/brand-brief` |
| Body text minimum | **16px on mobile** (below it, iOS zooms form fields), 16–18px desktop. 14px is a floor for labels and fine print, never body copy | `psychology/06`, `build/09`, `build/10` |
| Space above a heading vs below it | **2× the space below**, up to 3× at a major section break | `psychology/05`, `psychology/06`, `build/09` |
| Contrast | 4.5:1 body · 3:1 large text (~24px+, or ~19px+ bold) and meaningful UI edges | everywhere |
| Tap target | ≥ 44×44 CSS px, ≥ 8px apart | `psychology/05`, `build/09`, `build/10` |
| Core Web Vitals | LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1, at the 75th percentile on a mid-range phone | `build/08`, `build/10`, `ops/15` |
| Named frameworks | 3–7 total | `search/12` |
| Glossary at launch | 8–15 real terms | `search/12` |
| URLs at launch | 7–12 | `build/08` |

Two of these are hard gates rather than defaults: **contrast** and **tap target** come from published
accessibility guidance, and failing them is a defect, not a style. The rest are craft defaults — deviate
when you have a reason, and write the reason down.

---

## Apply it

- [ ] All five decisions are answered in writing in [templates/brand-brief.md](templates/brand-brief.md).
- [ ] The primary buyer passes the twenty-names test, and one adjacent audience is explicitly excluded.
- [ ] The category frame is written, and the real alternative set includes "do nothing."
- [ ] The one promise survives the inversion test and carries a mechanism and a falsification condition.
- [ ] The energy target is a recorded number, and I know which tactics to invert because of it.
- [ ] The price ladder has three rungs, a defined free entry, and a written refund policy.
- [ ] I can explain each of the three engines in one sentence and name which one a given tactic uses.
- [ ] The build follows the phase order, and no phase started before the previous gate passed.
- [ ] Tokens were built before pages; keyword-to-URL mapping was done before content.
- [ ] Every honesty rail has been checked against the live site, not just intended.
- [ ] The definition of done is green, item by item, before anyone calls it finished.
- [ ] Where two documents disagreed, the precedence order in "How to use this file" decided it — and the
      decision was written down rather than averaged.
- [ ] Every recurring number on the site matches the canonical values in Part 6.

## Related

- [README.md](README.md) — what the pack is, the full table of contents, and the three reading paths
- [brand/01-positioning-and-category.md](brand/01-positioning-and-category.md) — decisions 1 and 2 in depth
- [brand/03-voice-messaging-and-copywriting.md](brand/03-voice-messaging-and-copywriting.md) — turning the promise into copy
- [psychology/04-persuasion-core.md](psychology/04-persuasion-core.md) — the influence principles and their limits
- [psychology/07-pricing-psychology.md](psychology/07-pricing-psychology.md) — decision 5 in depth
- [build/09-design-system-and-tokens.md](build/09-design-system-and-tokens.md) — the tokens that encode the energy target
- [build/10-conversion-audit-checklist.md](build/10-conversion-audit-checklist.md) — the pre-ship gate
- [ops/15-launch-checklist-and-build-order.md](ops/15-launch-checklist-and-build-order.md) — the full launch sequence
