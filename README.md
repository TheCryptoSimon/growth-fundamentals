# Growth & Brand Fundamentals

A brand-neutral library for taking a product from "it has no name yet" to a live site that converts, ranks,
and gets cited by AI answer engines. Read this page to find your entry point, then open
[00-START-HERE.md](00-START-HERE.md) — that file is the operating manual and the one an AI agent should read
before touching anything.

---

## What this pack is

Seventeen numbered documents plus four fill-in templates, covering positioning, identity, voice, consumer
psychology, page construction, search and AI visibility, measurement, and launch sequencing.

Every principle in here is written in three parts:

| Part | What it gives you |
|---|---|
| **What it is** | one or two lines — no theory tour |
| **Mechanism** | why it works on a human being, so you can tell when it *won't* |
| **How to apply** | a rule, a number, or a checklist line you can act on today |

Two conventions run through the whole library:

- **The dial is always named.** Most persuasion and design tactics only hold at one end of a spectrum that
  runs from calm/premium/trust-first to energetic/urgent/playful. Wherever a tactic is direction-dependent,
  the doc says which end it belongs to and states the inverse for the other end. Nothing high-energy is ever
  presented as universal.
- **Honesty rails override tactics.** No invented numbers, no manufactured scarcity, no fabricated proof.
  Where a technique starts shading into manipulation, the doc says so and marks the line.

## What this pack is deliberately not

- **Not a clone of an existing brand.** No document says "copy this site." Every recommendation is a
  principle plus a decision rule, so a brand-new product can derive its *own* answer rather than inherit
  someone else's.
- **Not a style guide.** It tells you how to *choose* a palette, a typeface pairing, and a section order —
  it does not hand you a finished visual identity.
- **Not a growth-hack list.** Tactics that only work by confusing the reader are excluded or flagged.
- **Not a substitute for knowing your market.** It gives you the method for finding the answer; the facts
  about your buyers still have to come from your buyers.

## Who it is for

- **A founder** deciding brand, positioning, offer, and price before spending money on design or ads.
- **An AI coding agent** building the new brand's website from zero, which needs unambiguous rules,
  checklists, and acceptance criteria rather than inspiration.

Both readers are assumed to be starting from nothing: no name, no palette, no copy, no traffic.

---

## The library

### Brand — decide what the thing *is* before you design it
| Doc | What you get |
|---|---|
| [brand/01-positioning-and-category.md](brand/01-positioning-and-category.md) | How to pick the audience, the category you enter or create, and the one differentiator you defend |
| [brand/02-identity-archetype-and-naming.md](brand/02-identity-archetype-and-naming.md) | Choosing a personality that survives contact with reality, plus a name-generation and name-screening method |
| [brand/03-voice-messaging-and-copywriting.md](brand/03-voice-messaging-and-copywriting.md) | The message hierarchy, voice rules, headline and body formulas, and the claim → mechanism → proof pattern |

### Psychology — the behavioural engine under every design choice
| Doc | What you get |
|---|---|
| [psychology/04-persuasion-core.md](psychology/04-persuasion-core.md) | The durable influence principles, when each holds, and where each turns manipulative |
| [psychology/05-visual-attention-and-layout.md](psychology/05-visual-attention-and-layout.md) | Focal points, salience, gaze and directional cues, scanning behaviour, and layout rhythm |
| [psychology/06-color-and-typography.md](psychology/06-color-and-typography.md) | How to build a palette and a type system from meaning, contrast, and legibility rather than taste |
| [psychology/07-pricing-psychology.md](psychology/07-pricing-psychology.md) | Setting the number, structuring the ladder, and presenting a price so it reads fairly |

### Build — turn decisions into a site
| Doc | What you get |
|---|---|
| [build/08-page-architecture-and-section-recipes.md](build/08-page-architecture-and-section-recipes.md) | Which pages to build, in what order, and a section-by-section recipe for each |
| [build/09-design-system-and-tokens.md](build/09-design-system-and-tokens.md) | Tokens, scales, spacing, components, and accessibility defaults an agent can implement directly |
| [build/10-conversion-audit-checklist.md](build/10-conversion-audit-checklist.md) | The pre-ship gate: a pass/fail audit you run on every page before it goes live |

### Search — be findable by people and by machines
| Doc | What you get |
|---|---|
| [search/11-seo-fundamentals.md](search/11-seo-fundamentals.md) | Keyword-to-URL mapping, site architecture, on-page rules, internal linking, indexing |
| [search/12-geo-ai-search.md](search/12-geo-ai-search.md) | How to become quotable to answer engines: direct-answer blocks, named frameworks, entity consistency |
| [search/13-schema-and-technical-wiring.md](search/13-schema-and-technical-wiring.md) | Structured data as one connected graph, plus sitemaps, robots, canonicals, and crawler access |

### Ops — measure it, launch it, and hand it to an agent
| Doc | What you get |
|---|---|
| [ops/14-measurement-and-experimentation.md](ops/14-measurement-and-experimentation.md) | The small set of metrics worth tracking, how to instrument them, and how to test honestly |
| [ops/15-launch-checklist-and-build-order.md](ops/15-launch-checklist-and-build-order.md) | The end-to-end sequence from empty repo to launched site, with gates between phases |
| [ops/16-prompt-pack.md](ops/16-prompt-pack.md) | Ready prompts for driving an AI agent through each stage of the build |

### Templates & reference
| File | What you get |
|---|---|
| [templates/brand-brief.md](templates/brand-brief.md) | The single fill-in document that captures every upstream decision |
| [templates/page-brief.md](templates/page-brief.md) | A one-page spec to hand an agent before it builds any individual page |
| [templates/llms.txt.example](templates/llms.txt.example) | A starting `llms.txt` for AI answer engines |
| [templates/robots.txt.example](templates/robots.txt.example) | A starting `robots.txt` with a sane crawler policy |
| [reference/README.md](reference/README.md) | Where the ideas come from and what to read next if you want the underlying research |

---

## Read in this order

Pick the entry point that matches where you actually are. Every path starts at
[00-START-HERE.md](00-START-HERE.md) because that file locks the five decisions the rest of the pack
depends on.

**Path 1 — "I am naming and positioning a brand from scratch."**
`00-START-HERE` → `brand/01` → `brand/02` → `brand/03` → `psychology/07` (price ladder) →
fill in `templates/brand-brief.md` → then continue with Path 2.
*Do not open the design docs yet. A palette chosen before the positioning is a coin flip.*

**Path 2 — "I have positioning; I need to build the site."**
`00-START-HERE` (decisions 4 and 5) → `psychology/04` → `psychology/05` → `psychology/06` →
`build/09` (tokens first) → `build/08` (pages) → `templates/page-brief.md` per page →
`build/10` (audit gate) → `ops/15` (launch order).
*Build the design system before the pages, or every page invents its own spacing.*

**Path 3 — "I have a site; I need traffic and AI citations."**
`00-START-HERE` (skim the engines and rails) → `search/11` → `search/12` → `search/13` →
`templates/llms.txt.example` + `templates/robots.txt.example` → `ops/14` (measure) →
`build/10` (because ranked traffic that does not convert is a leak, not a win).

---

## How to use this with an AI agent

1. **Clone the pack next to the new project**, not inside it — for example `~/projects/new-brand/` and
   `~/projects/growth-fundamentals/` as siblings. It is reference material, not application code.
2. **Point the agent at `00-START-HERE.md` first**, before it writes a line of markup. That file gives it
   the five decisions, the mental model, the order of operations, and the definition of done.
3. **Copy `skills/` into the new project's `.claude/skills/`** so the agent can invoke the bundled
   procedures by name instead of improvising them.
4. **Fill `templates/brand-brief.md` yourself.** This is the human's job. An agent that guesses the
   positioning will produce a competent site for a brand that does not exist.
5. **Give the agent one `templates/page-brief.md` per page.** Scope creep in a build is usually an
   under-specified brief, not a weak model.
6. **Make `build/10-conversion-audit-checklist.md` the merge gate.** The agent should run it against its
   own output and report failures before claiming a page is done.

A short starting instruction that works:

> Read `../growth-fundamentals/00-START-HERE.md` in full, then `../growth-fundamentals/build/09` and
> `../growth-fundamentals/build/08`. Use `BRAND-BRIEF.md` in this repo as the source of truth for every
> brand decision. Do not invent statistics, testimonials, or scarcity. Build page by page, and run the
> conversion audit checklist before you tell me a page is finished.

---

## Provenance and honesty

This pack is an original synthesis. It draws on consumer-psychology research — notably the body of work
published by Nick Kolenda — alongside classic influence research (Cialdini), brand-strategy thinking in the
Aaker/Ries–Trout tradition, and a working SEO/GEO method developed in practice. Where those sources describe
an experimental finding, this pack restates it qualitatively and operationally: what tends to happen, under
what conditions, and what to do about it.

Three deliberate constraints:

- **No third-party text is reproduced here.** Every idea is re-expressed in operational wording. Paid or
  personally-licensed libraries used as background stay on their owner's machine and are not redistributed
  with this pack.
- **No invented evidence.** You will not find a percentage, a conversion-lift figure, a study citation, or a
  sample testimonial anywhere in these documents. Findings are described in words ("people tend to judge X
  as Y when Z"), never dressed up as a statistic that cannot be checked.
- **Manipulation is named, not smuggled.** Where a technique works by exploiting confusion rather than by
  helping someone decide, the doc says so and draws the line.

## Licence and sharing

This pack is an original synthesis and is safe to share, fork, and adapt. No proprietary or paid third-party
material is embedded in it. If you build on it, keep the honesty rails — they are the reason the tactics
stay usable on a brand that has to survive its own customers.

---

## Apply it

- [ ] I have read [00-START-HERE.md](00-START-HERE.md) before opening any design or build doc.
- [ ] I picked one of the three reading paths and know which docs I am skipping for now.
- [ ] The brand brief ([templates/brand-brief.md](templates/brand-brief.md)) exists and a human filled it in.
- [ ] The five upstream decisions are written down, not held in someone's head.
- [ ] The energy target on the calm ↔ urgent dial is chosen and recorded, so tactics can be inverted correctly.
- [ ] The pack is cloned as a sibling of the project, and `skills/` is copied into `.claude/skills/`.
- [ ] Every page has a page brief before an agent starts building it.
- [ ] [build/10-conversion-audit-checklist.md](build/10-conversion-audit-checklist.md) is wired in as the
      pre-ship gate, not an afterthought.
- [ ] No number, quote, rating, or testimonial appears on the site that cannot be sourced.
- [ ] Search and AI-visibility work ([search/11](search/11-seo-fundamentals.md)–[13](search/13-schema-and-technical-wiring.md))
      is scheduled, not deferred until "after launch."

## Related

- [00-START-HERE.md](00-START-HERE.md) — the operating manual: five decisions, three engines, build order
- [brand/01-positioning-and-category.md](brand/01-positioning-and-category.md) — where every path really begins
- [ops/15-launch-checklist-and-build-order.md](ops/15-launch-checklist-and-build-order.md) — the sequence from zero to live
- [ops/16-prompt-pack.md](ops/16-prompt-pack.md) — prompts for driving an agent through the build
- [reference/README.md](reference/README.md) — schools of thought behind the synthesis
