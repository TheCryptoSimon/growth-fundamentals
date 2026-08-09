# Prompt Pack

Twelve reusable prompts for driving an AI agent through this pack, from a blank brand to a monthly review.
Copy a prompt verbatim, fill the `{{PLACEHOLDERS}}`, and paste. Read this when you are about to ask an agent
for something and want a specification instead of a vibe.

---

## 0. How to use these

**The path convention.** Every prompt tells the agent which document to load first. Replace `{{PACK}}` with
the path to this library from the agent's working directory — if you cloned the pack as a sibling of the
project, that is `../growth-fundamentals`. Loading the right doc is what makes the output usable; an agent
without the context will produce a plausible average of the internet.

**Four rules that apply to every prompt here.**

1. **Ground before generating.** Name the file to read. Never assume the model remembers this pack.
2. **Constrain the output shape.** Say how many, in what format, and what must not appear. Unbounded prompts
   produce unbounded, unusable output.
3. **Force the honesty rails into the prompt itself.** Every generative prompt below repeats the ban on
   invented numbers, testimonials, and urgency, because a model asked for "compelling copy" will otherwise
   helpfully manufacture evidence.
4. **Ask for the uncertainty.** A prompt that ends "list what you had to assume" converts silent fabrication
   into a visible question.

**Chaining them.** P1 → P2 → P3 → P5 produces the brand brief. P6 → P7 → P8 produces and hardens a page.
P9 → P10 → P11 wires it for search. P12 closes the loop each month.

---

## P1 — Brand discovery interview

**Purpose.** The agent interviews the founder and produces the raw material for the brand brief. Use before
anything else exists.
**Load first.** `{{PACK}}/00-START-HERE.md`, `{{PACK}}/brand/01-positioning-and-category.md`

```text
Read {{PACK}}/00-START-HERE.md and {{PACK}}/brand/01-positioning-and-category.md in full.

You are interviewing me to fill in {{PACK}}/templates/brand-brief.md. Do not write the
brief yet.

Ask me ONE question at a time and wait for my answer. Start with the audience and the
trigger moment, then the category and real alternatives, then the promise and its
mechanism, then the energy target on the calm-to-urgent dial, then the price ladder.

Rules:
- If an answer is vague, abstract, or could be said by a competitor, say so plainly and
  ask a sharper follow-up. Do not accept "small businesses" or "we're the best at X".
- Push for concrete nouns, specific situations, and evidence I already have.
- Never suggest an answer before I have given mine; you may offer options only after I
  have tried and failed twice.
- Track which of the five decisions are still unanswered and tell me the count each turn.

After no more than 25 questions, stop and produce:
1) A draft brand brief filled from my answers only.
2) A list of everything you had to leave blank or guess, marked GAP or ASSUMPTION.
3) The three answers you consider weakest, and why.
```

**Good output looks like.** One question per turn with visible pushback on vague answers, then a brief whose
gaps are explicitly marked rather than smoothed over. If the agent filled every field confidently after eight
questions, it invented most of them.

---

## P2 — Positioning statement generator

**Purpose.** Turn interview material into three competing positioning statements, not one.
**Load first.** `{{PACK}}/brand/01-positioning-and-category.md`

```text
Read {{PACK}}/brand/01-positioning-and-category.md.

Using only the facts in the brand brief below, write THREE distinct positioning
statements in this shape:
  "For [specific buyer] who [trigger situation], {{BRAND}} is the [category] that
   [differentiator], because [mechanism]."

The three must differ in strategy, not in wording: one that enters the obvious existing
category, one that competes on a different dimension inside it, and one that names a new
category. For each, add:
- the alternative it is fighting (including "do nothing")
- what you must be able to prove for it to be credible
- what it forces the brand to give up

Rules: no invented facts, no numbers I did not give you, no superlatives. If a statement
needs a fact I have not supplied, write [NEEDS PROOF: ...] instead of inventing it.

BRAND BRIEF:
{{PASTE BRIEF}}
```

**Good output looks like.** Three genuinely different strategic bets with explicit costs, and bracketed proof
gaps. Three rephrasings of the same sentence means the agent optimised for wording; re-run with the
differences named more forcefully.

---

## P3 — Positioning critic (run against P2's output)

**Purpose.** An adversarial second pass. Generation and criticism must be separate calls, because a model
grading its own output grades gently.
**Load first.** `{{PACK}}/brand/01-positioning-and-category.md`, `{{PACK}}/00-START-HERE.md`

```text
Read {{PACK}}/brand/01-positioning-and-category.md and the honesty rails in
{{PACK}}/00-START-HERE.md.

You are a sceptical strategist who thinks each of these statements is probably weak.
For EACH statement below, run these tests and answer each with a verdict and one line of
reasoning:

1. INVERSION: could a credible competitor claim the opposite and still sound sane? If
   no, the claim is empty table stakes.
2. TWENTY NAMES: could someone list twenty real buyers matching this audience this week?
3. MECHANISM: is there a structural reason it is true, or only an assertion?
4. FALSIFIABILITY: could a customer prove we broke this promise?
5. SUBSTITUTION: replace the brand name with a competitor's. Does it still read as true?
   If yes, it is not positioning.
6. COMPREHENSION: would a first-time reader know what the product physically is?

Then: rank the three, name the single strongest sentence across all of them, and write
one improved statement that fixes the worst failure. Be blunt. Do not soften.

STATEMENTS:
{{PASTE P2 OUTPUT}}
```

**Good output looks like.** Failed verdicts, in plain words, on at least one test per statement. Six passes
across the board means the critic role did not take.

---

## P4 — Name generator, constrained by the phonetics rules

**Purpose.** Candidate names that already survive the screening criteria.
**Load first.** `{{PACK}}/brand/02-identity-archetype-and-naming.md`

```text
Read {{PACK}}/brand/02-identity-archetype-and-naming.md, especially the sound-symbolism,
fluency, and screening sections.

Generate 30 name candidates for: {{ONE-LINE DESCRIPTION}}, aimed at {{AUDIENCE}}, with an
energy target of {{CALM|MIDDLE|ENERGETIC}} on the calm-to-urgent dial and the personality
traits {{TRAIT, TRAIT, TRAIT}}.

Constraints, all mandatory:
- Sound must match the energy target as described in the doc; state which sound choices
  you used for each name.
- Two to four syllables. Pronounceable on a first read by a non-native speaker.
- Passes the bad-phone-line test: spellable correctly after hearing it once.
- No numbers, no deliberate misspellings of common words, no doubled letters that invite
  typos, no hyphens.
- Avoid unintended meanings in English, Spanish, German, and French; flag any you spot.

Group the 30 into the name types from the doc (descriptive, suggestive, abstract,
compound, founder, metaphor) with at least three per type. For each name give: the type,
the association you are borrowing, and the single biggest risk.

Do NOT check domain availability or trademarks — you cannot verify these. Instead output
a checklist of what I must verify before adopting any name.
```

**Good output looks like.** Type-grouped candidates each carrying a stated association and a risk, plus an
explicit refusal to claim domain or trademark availability. Any agent that asserts a domain is free is
guessing.

---

## P5 — Voice extractor from sample writing

**Purpose.** Derive a usable voice specification from writing the founder already produced, rather than
picking adjectives from a list.
**Load first.** `{{PACK}}/brand/03-voice-messaging-and-copywriting.md`

```text
Read {{PACK}}/brand/03-voice-messaging-and-copywriting.md.

Below are {{N}} samples of my writing that sound like the brand should sound. Analyse
them and produce a voice specification:

1. Three to five voice traits. For each: a "we do" line and a "we never" line, each with a
   short example lifted from the samples.
2. Sentence patterns: typical length, rhythm, how often questions appear, how contractions
   and first/second person are used.
3. Vocabulary: fifteen words and phrases characteristic of these samples.
4. A banned-words list of at least twelve items: filler, hype, and category clichés that
   appear in competitors' writing but never in mine.
5. Punctuation and formatting rules that are actually observable in the samples.
6. Two rewritten paragraphs: a generic marketing paragraph about {{TOPIC}}, first in the
   wrong voice, then corrected — with the specific lever named for each change.

Describe only what is present in the samples. If a trait is not evidenced, say so rather
than inventing a personality.

SAMPLES:
{{PASTE 3-5 SAMPLES}}
```

**Good output looks like.** Traits that quote the samples, a banned list you recognise as the things you hate,
and a before/after where each edit names its lever.

---

## P6 — Homepage wireframe and copy

**Purpose.** Turn a completed brand brief into a section-by-section home page with real copy.
**Load first.** `{{PACK}}/build/08-page-architecture-and-section-recipes.md`,
`{{PACK}}/brand/03-voice-messaging-and-copywriting.md`, `{{PACK}}/psychology/05-visual-attention-and-layout.md`

```text
Read {{PACK}}/build/08-page-architecture-and-section-recipes.md,
{{PACK}}/brand/03-voice-messaging-and-copywriting.md and
{{PACK}}/psychology/05-visual-attention-and-layout.md.

Using the brand brief below as the ONLY source of brand facts, produce a home page as a
section-by-section wireframe plus finished copy.

For each section give:
- Section name and its single job in one line
- Layout sketch in text (what sits where, and the visual hierarchy)
- Finished copy: heading, subheading, body, and any labels — written in the brand voice
- Whether a CTA appears here, and if so its exact label and the microcopy under it
- Which objection or which of the three pillars this section is discharging

Hard constraints:
- Exactly ONE primary CTA style across the page; secondaries must be visually quiet.
- The energy target is {{DIAL}}: apply the inversion table in {{PACK}}/00-START-HERE.md
  and tell me which tactics you inverted because of it.
- Every claim states its mechanism next to it.
- No statistics, testimonials, logos, ratings, countdowns, or scarcity unless they appear
  verbatim in the brief. Where proof is needed and absent, output [PROOF NEEDED: what].
- Second person, present tense, concrete nouns.

Finish with: the five-second test answers a stranger should give after seeing the first
screen (what is it / who is it for / what do I do next).

BRAND BRIEF:
{{PASTE BRIEF}}
```

**Good output looks like.** Six to nine sections, each discharging a named job, with `[PROOF NEEDED: ...]`
markers where evidence is missing and an explicit list of tactics inverted for the dial.

---

## P7 — Section-copy rewriter

**Purpose.** Harden existing copy for concreteness, second person, and mechanism.
**Load first.** `{{PACK}}/brand/03-voice-messaging-and-copywriting.md`

```text
Read {{PACK}}/brand/03-voice-messaging-and-copywriting.md.

Rewrite the copy below. Produce a table with three columns: ORIGINAL, REWRITE, LEVER
(the specific principle you applied), one row per sentence or clause you changed.

Apply, in this order:
1. Replace abstractions with concrete nouns and observable outcomes.
2. Convert to second person, present tense.
3. Attach a mechanism to every claim ("because ..."), using only facts supplied below. If
   the mechanism is unknown, write [MECHANISM NEEDED] — never invent one.
4. Cut hedges, filler, and any word on the banned list.
5. Shorten: no sentence over about 25 words; one idea per sentence.
6. Keep the energy at {{DIAL}} — do not add urgency, exclamation, or intensifiers unless
   the dial is at the energetic end AND the urgency is literally true.

Do not add new claims, numbers, or proof. Preserve every factual constraint.

Then state: the single weakest remaining sentence and why.

FACTS AVAILABLE: {{FACTS}}
BANNED WORDS: {{LIST}}
COPY:
{{PASTE COPY}}
```

**Good output looks like.** A row-by-row table where the LEVER column is specific ("abstraction → concrete
noun") rather than "improved flow", plus `[MECHANISM NEEDED]` markers instead of invented reasons.

---

## P8 — Harsh design critique of a screenshot

**Purpose.** Grade a rendered page against the audit gate before it ships. Run it on a real screenshot at
both viewports.
**Load first.** `{{PACK}}/build/10-conversion-audit-checklist.md`,
`{{PACK}}/psychology/05-visual-attention-and-layout.md`, `{{PACK}}/psychology/06-color-and-typography.md`

```text
Read {{PACK}}/build/10-conversion-audit-checklist.md,
{{PACK}}/psychology/05-visual-attention-and-layout.md and
{{PACK}}/psychology/06-color-and-typography.md.

Attached are screenshots of {{PAGE}} at 375px and at desktop width. The brand's energy
target is {{DIAL}}.

You are a harsh reviewer. Assume the page is flawed and find the flaws.

Step 1 — First impression, in under five seconds of looking: what is this, who is it for,
what am I meant to do? Answer as a stranger would, not as someone who read the brief.

Step 2 — Where does the eye land first, second, third? Is the primary CTA the winner? If
something competes with it, name it.

Step 3 — Walk EVERY line of the conversion checklist. Output a table: CHECK | PASS/FAIL |
EVIDENCE FROM THE SCREENSHOT. Never mark PASS on something you cannot see; mark it
UNVERIFIABLE and say what you would need.

Step 4 — List the failures ranked by damage to conversion, each with a specific fix
(a concrete instruction, not "improve hierarchy").

Step 5 — The three things that are genuinely good, so we do not break them.

Do not be encouraging. Do not summarise the page back to me. If the page is broadly fine,
say what the single highest-leverage change is anyway.
```

**Good output looks like.** Failures with pixel-level evidence, `UNVERIFIABLE` used honestly for things a
screenshot cannot show (contrast ratios, keyboard focus, load performance), and fixes phrased as
instructions.

---

## P9 — Page SEO brief

**Purpose.** Specify a page before it is written, so it targets one keyword and does not cannibalise a
sibling.
**Load first.** `{{PACK}}/search/11-seo-fundamentals.md`, `{{PACK}}/templates/page-brief.md`

```text
Read {{PACK}}/search/11-seo-fundamentals.md and {{PACK}}/templates/page-brief.md.

Produce a completed page brief for a page targeting the primary keyword
"{{KEYWORD}}" for {{BRAND}}.

Include: URL slug, page job in one line, audience and search intent (informational,
commercial, transactional, navigational), title tag and meta description within sensible
length limits, H1, the direct-answer paragraph, an H2/H3 outline with the job of each
section, the proof elements required, the objections to answer, ONE call to action with
its microcopy, internal links in and out (name the specific existing pages), schema types,
an OG image note, and acceptance criteria.

Constraints:
- One primary keyword only. List the existing pages below and state explicitly which one
  this page could cannibalise and how the brief avoids it.
- Do not invent search volumes, difficulty scores, or ranking predictions — you cannot
  verify them. Reason from intent instead.
- The title must capture the searched term; the body must hold the brand's own frame.
- Flag any claim in the outline that will require proof we may not have.

EXISTING PAGES AND THEIR KEYWORDS:
{{PASTE URL MAP}}
```

**Good output looks like.** A brief that names a specific cannibalisation risk and how it is resolved, with
no fabricated volume or difficulty numbers.

---

## P10 — GEO direct-answer writer

**Purpose.** Write the quotable block near the top of a page — the highest-leverage element for being cited
by answer engines.
**Load first.** `{{PACK}}/search/12-geo-ai-search.md`

```text
Read {{PACK}}/search/12-geo-ai-search.md.

Write the direct-answer block for the page {{URL}}, which answers the question:
"{{QUESTION}}".

Requirements:
- One paragraph, roughly 40 to 70 words, placed within the first screen of the page.
- Completely self-contained: it must remain true and comprehensible when quoted with no
  surrounding page, no images, and no prior sentence.
- Answers the question in the FIRST sentence. No preamble, no "in today's landscape".
- Names the brand once, naturally, in a way that survives being quoted.
- Plain declarative sentences; no marketing adjectives; no rhetorical questions.
- Every factual element must come from the source material below. If the honest answer
  requires a fact I have not given you, output [FACT NEEDED: ...].

Then produce:
1) Three alternative phrasings of the first sentence.
2) The three follow-up questions a reader most likely asks next, each as an FAQ entry with
   a 30-to-50-word answer written to the same rules.
3) The CSS selector or element you would mark as speakable, and why.

SOURCE MATERIAL:
{{PASTE FACTS}}
```

**Good output looks like.** A paragraph you could paste into a chat answer with attribution and it would read
as complete, plus FAQ entries that answer rather than tease.

---

## P11 — Schema generator

**Purpose.** Produce one connected structured-data graph for a page.
**Load first.** `{{PACK}}/search/13-schema-and-technical-wiring.md`

```text
Read {{PACK}}/search/13-schema-and-technical-wiring.md.

Generate the JSON-LD for {{URL}}, a {{PAGE TYPE}} page.

Requirements:
- One @graph containing every node for this page, cross-referenced by @id. The
  Organization node uses the site-wide @id "{{SITE_URL}}/#organization" and every other
  node references it.
- Include the node types the doc prescribes for this page type, plus WebPage and
  BreadcrumbList.
- WebPage carries a speakable property pointing at the direct-answer selector.
- Offers reflect the real prices below. NEVER output aggregateRating, ratingValue,
  reviewCount, or any review node — we have no verified reviews and inventing them is
  both dishonest and a policy violation.
- Every property must be true and match the page's visible content exactly. Structured
  data that contradicts the page is worse than none.
- Output valid JSON only in a fenced block, then a plain-language list of every field I
  must verify before shipping, and any field you had to leave as a placeholder.

PAGE FACTS: {{ENTITY NAME, URL, DESCRIPTION, BREADCRUMB TRAIL, PRICES, FAQ ITEMS}}
```

**Good output looks like.** A single connected graph, no rating nodes, and an explicit list of fields to
verify. Any agent that invents a rating has failed the task, not decorated it.

---

## P12 — Monthly performance review

**Purpose.** Turn a month of data into one decision, rather than a summary.
**Load first.** `{{PACK}}/ops/14-measurement-and-experimentation.md`

```text
Read {{PACK}}/ops/14-measurement-and-experimentation.md.

Below is this month's data and the experiment log. Produce a review in this order:

1. NORTH STAR: value, direction versus last month, and whether the two or three input
   metrics explain the move. If they do not, say the move is unexplained rather than
   inventing a story.
2. FUNNEL: the ratio between each adjacent stage, and which ratio is weakest RELATIVE to
   what that stage should plausibly achieve.
3. THE LEAK: name the single biggest leak and the evidence for it. Distinguish clearly
   between measured, directional, and speculative.
4. SEARCH: which queries gained impressions, whether a page owns each of them, and any
   page with high impressions and poor click-through (a title and meta problem, not a
   content problem).
5. QUALITATIVE: what the exit surveys, five-user tests, and support notes said, in the
   customers' own words. Quote them; do not paraphrase into marketing language.
6. LAST MONTH'S CHANGES: for each entry in the experiment log, keep / revert /
   inconclusive, with the reasoning.
7. THE ONE THING: the single change to make next month, why it is the highest-leverage
   one, what you expect to move, in which direction, and how much of a window it needs.

Rules: do not claim statistical significance for any comparison unless the sample size
supports it — say "directional" instead. Do not invent explanations for noise. If a
number looks wrong, flag it as a possible instrumentation problem before interpreting it.

DATA: {{PASTE}}
EXPERIMENT LOG: {{PASTE}}
```

**Good output looks like.** One named change with an expected direction and a window, and explicit
"directional, not significant" labelling. A review that lists seven opportunities has made no decision.

---

## Prompt-writing rules, if you need one this pack does not have

| Rule | Why |
|---|---|
| Name the file to read first | Grounding beats instruction; an ungrounded model averages the internet |
| Give the output shape (count, format, columns) | Unbounded requests produce unusable prose |
| Assign a stance for critique ("assume it is flawed") | Models default to agreeable, which is useless in a review |
| Separate generation from criticism into two calls | Self-grading is systematically lenient |
| Require a marker for missing facts (`[PROOF NEEDED]`) | Converts silent fabrication into a visible question |
| Repeat the honesty rails inside the prompt | "Compelling" is otherwise read as licence to invent evidence |
| Ban the things you cannot verify (volumes, ratings, availability) | Stops confident guesses entering a spec |
| End with "list what you assumed" | The cheapest single line for catching hallucination |

---

## Apply it

- [ ] `{{PACK}}` is replaced with the real relative path before any prompt is pasted.
- [ ] Every generative prompt names the document the agent must read first.
- [ ] The honesty rails are repeated inside each prompt, not just in the pack.
- [ ] Generation (P2, P6) and criticism (P3, P8) are run as separate calls.
- [ ] The discovery interview (P1) was run before any copy or design prompt.
- [ ] Every prompt's output carries explicit `[PROOF NEEDED]` / `[FACT NEEDED]` markers where evidence is absent.
- [ ] The naming prompt's output was treated as candidates only; trademark and domain checks were done by a human.
- [ ] The design critique (P8) was run on real screenshots at 375px and desktop, not on a description.
- [ ] The schema prompt's output was validated in a structured-data testing tool before shipping.
- [ ] No prompt output containing an invented statistic, rating, or testimonial has been published.
- [ ] The monthly review (P12) ends in one decision with an owner, and it lands in the experiment log.

## Related

- [../00-START-HERE.md](../00-START-HERE.md) — the context an agent needs before any prompt here
- [14-measurement-and-experimentation.md](14-measurement-and-experimentation.md) — the data P12 consumes
- [15-launch-checklist-and-build-order.md](15-launch-checklist-and-build-order.md) — which phase each prompt belongs to
- [../templates/brand-brief.md](../templates/brand-brief.md) — what P1–P5 produce
- [../templates/page-brief.md](../templates/page-brief.md) — what P9 produces
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — the voice rules P5 and P7 enforce
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the gate P8 grades against
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — the method behind P10
