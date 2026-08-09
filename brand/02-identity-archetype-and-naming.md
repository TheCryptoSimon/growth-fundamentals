# Brand Identity, Archetype and Naming

How to choose a personality you can actually hold, pick an archetype that keeps every later
decision coherent, and generate + screen a name that is easy to say, easy to spell and safe to own.
Read this immediately after `01-positioning-and-category.md` and before you touch colour, type or
copy — identity is the input those documents consume.

---

## 1. What identity is, and what it is not

Identity is **a small set of constraints you promise not to break**. It is not a logo, not a mood
board, not a colour. Its only job is to make thousands of future micro-decisions (button wording,
photo choice, error message tone, pricing name) come out consistent without a meeting each time.

| Identity IS | Identity is NOT |
|---|---|
| A trait list you refuse to contradict | Nice adjectives everyone agrees with |
| A dial position (calm ↔ energetic) | "Professional but also fun and edgy" |
| A set of forbidden moves | A style guide written after the site is built |
| Testable by a stranger | A feeling only the founder can adjudicate |

**The test that matters:** hand your trait list plus three unbranded page mockups to someone who has
never seen your product. If they cannot pick which mockup is yours, your identity is decorative.

---

## 2. Personality: pick traits from a menu, then hold them

Marketing research on brand personality — the work most people know through Jennifer Aaker's
five-dimension model — found that the traits people spontaneously attribute to brands cluster into a
handful of families. Treat those families as a **selection menu**, not a horoscope. You are picking
which cluster you want the market to feel, and accepting the cost of the ones you gave up.

| Dimension | Reads to a customer as | Typical proof it demands | Typical cost of choosing it |
|---|---|---|---|
| **Sincerity** | Honest, wholesome, down-to-earth, warm | Plain language, real people, transparent pricing, admitted limits | You cannot also look elite or exclusive |
| **Excitement** | Daring, spirited, imaginative, current | Novelty cadence, bold visuals, strong opinions | Reads less safe; hurts high-risk purchases |
| **Competence** | Reliable, capable, intelligent, credentialed | Specifics, mechanisms, uptime/accuracy claims, method pages | Can read cold and forgettable |
| **Sophistication** | Refined, upper-class, charming | Restraint, whitespace, understatement, price confidence | Excludes budget buyers; punishes clutter |
| **Ruggedness** | Tough, outdoorsy, durable, no-nonsense | Field evidence, stress tests, blunt copy | Reads unrefined; poor fit for delicate services |

### The selection rule

- **One dominant trait.** It wins every tie-break.
- **Two supporting traits.** They colour execution but never override the dominant.
- **One explicitly forbidden trait.** Write it down. "We are never *exciting*" is more operationally
  useful than any of the three you picked, because it is falsifiable in review.

> A dental clinic might land on *sincerity* (dominant) + *competence* and *sophistication*
> (supporting) + *excitement* (forbidden). That single line already resolves: no countdown timers,
> no exclamation marks, no neon, no stock photos of high-fives.

### Anti-traits beat traits

Every brand claims trustworthy, innovative and customer-focused; those words constrain nothing. Test
each trait with: *would a credible competitor claim the opposite?* If nobody would ever claim
"unreliable," then "reliable" is table stakes, not personality — keep it as hygiene and pick again.

### Write it as a spec, not a vibe

```
DOMINANT:    competence
SUPPORTING:  sincerity, sophistication
FORBIDDEN:   excitement, ruggedness
WE SOUND:    precise, unhurried, plain-spoken
WE NEVER:    hype, urgency language, slang, exclamation marks, superlatives
ARBITER:     when two options tie, choose the one a careful expert would choose
```

Paste this block into `../templates/brand-brief.md` and into every AI build prompt
(`../ops/16-prompt-pack.md`). An agent with this block writes on-brand copy on the first pass.

---

## 3. Personality decides the arousal dial

`../00-START-HERE.md` establishes the master dial: most persuasion and design tactics only hold at
one end of a **calm / premium / trust** ↔ **energetic / urgent / playful** spectrum. Personality is
what sets that dial, and once set it inverts or licenses roughly half the tactics in this pack.

| If your dominant trait is | Dial position | Then these are ON | And these are OFF (inverted) |
|---|---|---|---|
| Sophistication | Far calm | Muted/cool palette, generous spacing, light type weights, slow or no motion, round prices | Saturated accents everywhere, urgency, countdowns, exclamation marks, dense grids |
| Competence | Calm | Specifics, mechanism copy, restrained single accent, tables and evidence | Emotional escalation, scarcity framing, playful microcopy |
| Sincerity | Mid-calm | Warm neutrals, plain words, human photography, transparent limits | Exclusivity signals, coldness, prestige naming |
| Ruggedness | Mid-energetic | High contrast, heavy weights, blunt short sentences, field imagery | Delicate type, pastel palettes, ornamental flourish |
| Excitement | Energetic | Saturation, motion, bold claims, novelty cadence, playful copy | Whitespace-heavy restraint, understatement, long-form sober proof |

**Two rules that never invert:**

1. **One focal point per viewport.** True at both ends; only the *loudness* of the focal element
   changes.
2. **The honesty rails.** No invented numbers, no fake scarcity, no fabricated proof — regardless of
   dial position. An energetic brand may shout; it may not lie.

Mechanism for the dial's colour and type consequences lives in
`../psychology/06-color-and-typography.md`; the attention consequences in
`../psychology/05-visual-attention-and-layout.md`.

---

## 4. Archetypes: a shortcut to coherence

An archetype is a pre-packaged bundle of personality + narrative role. Its value is not mysticism —
it is **compression**. Instead of relitigating tone for every asset, you ask one question: *would
this archetype do that?* The twelve below are the practical working set most brand teams use
(descended from Jungian character types, popularised for brands by Mark and Pearson).

Pick **one primary**. Optionally add **one secondary** from an adjacent row. Never combine opposites
(Ruler + Outlaw, Caregiver + Jester) — the result is a brand nobody can predict, which is the exact
failure identity exists to prevent.

| Archetype | Core drive | Licenses in copy | Forbids | Dial |
|---|---|---|---|---|
| **Sage** | Understanding, truth | Teaching, mechanisms, caveats, sources, long-form | Hype, mystery, dumbing down, urgency | Calm |
| **Caregiver** | Protection, service | Reassurance, "we handle it", safety proofs, warmth | Elitism, sarcasm, risk language | Calm |
| **Ruler** | Order, control | Standards, authority, precision, prestige naming | Chaos, self-deprecation, discount framing | Calm |
| **Creator** | Expression, craft | Process reveals, materials, originality, detail | Mass-market framing, "quick and easy" | Calm–mid |
| **Innocent** | Simplicity, optimism | Plain promises, purity, minimalism, honesty | Cynicism, complexity, fear appeals | Calm–mid |
| **Everyman** | Belonging, fairness | Plain speech, "people like you", no-jargon pricing | Exclusivity, luxury cues, superiority | Mid |
| **Lover** | Intimacy, beauty | Sensory language, aesthetics, desire, closeness | Clinical tone, austerity, bargain framing | Mid |
| **Explorer** | Freedom, discovery | Journey language, frontier imagery, independence | Bureaucracy, safety-first framing, conformity | Mid–energetic |
| **Hero** | Mastery, achievement | Challenge, progress, effort, measurable wins | Passivity, softness, "it's easy" without proof | Energetic |
| **Magician** | Transformation | Before/after, "watch this", wonder, reveal | Boring process detail, hedging | Energetic |
| **Outlaw** | Disruption, rebellion | Enemy framing, taboo, blunt opinions | Corporate polish, appeasement, hedging | Energetic |
| **Jester** | Play, delight | Jokes, surprise, self-aware copy, absurdity | Solemnity, fear appeals, ceremony | Energetic |

### What each archetype implies downstream

| Archetype | Colour direction | Type direction | Imagery | Motion |
|---|---|---|---|---|
| Sage | Cool, low saturation, ink neutrals | Serif headings, mixed-case body, medium weight | Diagrams, annotated detail, few faces | Minimal; one gentle reveal |
| Caregiver | Warm neutrals, soft mid-tones | Rounded sans, lowercase-friendly | Real people, hands, care moments | Slow fades |
| Ruler | Deep dark neutral + one metallic-ish accent | High-contrast serif, tracked uppercase labels | Architecture, symmetry, empty rooms | Almost none |
| Creator | Material-led, one unexpected accent | Distinctive display face + neutral body | Process, tools, close-up texture | Reveals of making |
| Innocent | Light, airy, low chroma | Simple geometric sans | Open space, sky, single object | Minimal |
| Everyman | Familiar mid palette, no luxury cues | Plain workhorse sans, mixed case | Candid, imperfect, everyday | Functional only |
| Lover | Rich, warm, deep | Elegant serif, light weights, generous tracking | Skin, fabric, shallow depth of field | Slow, lingering |
| Explorer | Earthy, natural, wide range | Sturdy sans, wide widths | Landscape, motion, distance | Parallax, travel |
| Hero | Strong contrast, one bold accent | Bold weights, condensed allowed | Effort, progress, results | Purposeful, forward |
| Magician | Dark base + luminous accent | Elegant contrast, some drama | Transformation, light, shift | Reveal-driven |
| Outlaw | High contrast, unexpected pairings | Heavy, condensed, rule-breaking | Grit, texture, defiance | Abrupt, punchy |
| Jester | Saturated, playful pairings | Rounded display, playful sizes | Absurd, bright, unexpected | Bouncy, quick |

**Common failure:** picking an energetic archetype (Hero, Magician, Outlaw) because it sounds
exciting, while selling something that carries real downside risk for the buyer. High-consideration,
high-risk purchases — anything medical, financial, legal, or expensive-and-hard-to-reverse — almost
always want the calm end. Excitement in those categories reads as *inexperienced*, not *fresh*.

### Sanity checks before you lock it

1. Would your *best current customer* recognise the brand here, or is this aspirational cosplay?
2. Can you name three things the archetype forbids that you were otherwise about to do?
3. Does it survive your worst day — an outage, a refund fight? Crisis tone is the real test.
4. Is it different from your two closest competitors? If all three are Sage, that is a positioning
   vacancy — see `01-positioning-and-category.md`.

---

## 5. Naming: what a name must do

A name has four jobs, in this order of practical importance:

1. **Be repeatable.** Someone must be able to say it aloud and have the listener find it.
2. **Be ownable.** Legally clear and not confusable with an incumbent.
3. **Be neutral-to-positive on first hearing.** No unfortunate readings, no wrong category cue.
4. **Carry meaning.** Nice, not necessary — meaning can be built by the brand over time; a name that
   cannot be spelled cannot be.

Most founders optimise (4) and ignore (1). Reverse that priority.

### The name-type menu

| Type | What it is | Pros | Cons | Right when |
|---|---|---|---|---|
| **Descriptive** | Says what it does ("City Dental Care") | Instantly clear; zero education cost | Weakest trademark protection; hard to grow beyond the description; generic-looking; blends into competitors | Local service businesses, low-ambition scope, category where clarity beats distinctiveness |
| **Suggestive / associative** | Hints at the benefit without stating it | Good balance of meaning and ownability; easy to build story on | Requires taste; can drift into cliché suffix soup | Most startups; the safe default |
| **Coined** | Invented word built from parts | Highly protectable; blank canvas; usually available | Costs money/time to give it meaning; spelling risk | Well-funded, global ambition, crowded namespace |
| **Abstract / arbitrary** | Real word, unrelated to the product | Memorable; strong protection; emotionally borrowable | Zero built-in clarity; needs a descriptor beside it | Consumer brands with budget to teach the association |
| **Founder / eponymous** | A person's name | Instant authority for expert services; personal trust | Ties company value to a person; awkward on exit; hard to spell if uncommon | Consultancies, clinics, studios, craft brands |
| **Acronym** | Initials ("NRG Systems") | Short; fits narrow spaces | Meaningless; unmemorable; usually already taken; terrible for search | Almost never at launch — acronyms should be *earned* after the full name is known |

**Rule of thumb:** the more crowded and searchable your category, the further you should move from
descriptive. Descriptive names lose to the category itself in search results, because engines and AI
answer systems treat the words as topic signals rather than as an entity.

**Moderate distinctiveness wins.** Names that are completely literal are forgettable; names that are
completely disconnected are confusing. The sweet spot is a name where the connection to the product
is *findable with a second of thought* — the small resolution effort makes the meaning stick.

---

## 6. Sound symbolism, honestly

People reliably map speech sounds to physical qualities, across languages and before literacy. The
classic demonstration: given a round blob and a spiky shape, the overwhelming majority of people
assign the "spiky" name to the spiky shape. The effect is real, replicated, and **small**. Treat
phonetics as a **tie-breaker between finalists**, never as a reason to pick a name that fails
spelling or availability.

### The dials

| Sound feature | Examples | Tends to suggest |
|---|---|---|
| **Front vowels** (ee, i, e) | *slim, kit, mini* | Small, light, fast, sharp, precise, delicate |
| **Back vowels** (o, oo, ah, u) | *bold, room, grand* | Large, heavy, slow, round, soft, substantial |
| **Plosives / stops** (p, t, k, b, d, g) | *pop, kick, bud* | Abrupt, energetic, decisive, crisp, punchy |
| **Fricatives** (f, s, sh, v, z) | *soft, hush, ease* | Smooth, continuous, flowing, calm, gentle |
| **Voiced consonants** (b, d, g, v, z) | *bloom, glide* | Warmer, heavier, rounder |
| **Voiceless consonants** (p, t, k, f, s) | *crisp, task* | Cooler, lighter, sharper |
| **Liquids / nasals** (l, r, m, n) | *lumen, mira* | Soft, comfortable, flowing |

### Rhythm and repetition aid recall

- **Alliteration** (same initial sound) and **assonance** (repeated vowel) both make a name easier to
  encode and retrieve. Two-word names with a shared initial sound are noticeably stickier.
- **Two or three syllables with a clear stress pattern** are easiest to remember; a strong beat on
  the first syllable reads as a *thing*, later stress reads as an *action*.
- **A hard opening consonant** gives a name a crisper attack, which plausibly helps it survive being heard
  once across a room. Do not read the many famous brands beginning with a plosive as evidence for this —
  that is survivorship, not a finding. Tie-breaker only, like everything else in this section.

### Matching sound to your dial

| Your dial | Reach for | Avoid |
|---|---|---|
| Calm / premium / trust | Back vowels, fricatives, liquids, longer words, soft endings | Staccato plosive clusters, aggressive short barks |
| Energetic / urgent / playful | Front vowels, plosives, short punchy syllables, hard endings | Long flowing multi-syllable names that drag |

### Honesty caveat

Do not oversell this to stakeholders. You cannot claim a name will "convert better" because of its
vowels — the published effects are directional preferences measured in lab conditions, not revenue
guarantees. The correct claim is: *given two equally available, equally spellable finalists, prefer
the one whose sound matches the dial.*

---

## 7. Fluency: the criterion that actually predicts pain

Ease of processing is the most reliable naming criterion you have. Names that are easy to read, say
and spell get judged as more familiar, safer and more trustworthy; hard names get judged as more
novel, riskier and more complex. Note the direction dependency: **if your dial is calm/trust, choose
fluent. If your brand's whole pitch is novelty or edge, mild disfluency is an asset, not a bug.**

### The bad-phone-line test

Say the name aloud once, at normal speed, to someone who has never heard it, over a poor connection
or in a noisy room. Then ask them to type it. Run this with at least eight people from your target
segment.

- **Spelling error rate above ~1 in 4 → kill the name.** You will pay for that error forever in lost
  direct traffic, misdirected email and support confusion.
- **Any request to "spell that?" → a warning, not a veto.** One clarification is survivable; two is
  not.

### Spelling traps to screen out

| Trap | Example pattern | Why it hurts |
|---|---|---|
| Dropped vowels | *Flkr*-style | Every mention needs a spelling |
| Number/letter swaps | *4*, *2*, *X* for *for/to/ex* | Ambiguous when spoken |
| Homophone forks | *-ly / -li*, *-tion / -shun*, *c/k/q* | Traffic splits across variants |
| Double letters | *-ll-*, *-ss-*, *-tt-* | Coin-flip when typed |
| Silent letters | *-gh-*, *ps-*, *-mn* | Unfindable by ear |
| Compound ambiguity | Two words / one word / hyphen | Three URLs, three search behaviours |
| Awkward initialism | The initials spell something unfortunate | Discovered later, publicly |

### Length

**1–3 syllables** for anything typed often. Shorter names read as simpler and more down-to-earth;
longer names read as more complex, grander and more imaginative — match your positioning, not
fashion. The written form must survive a small header, a favicon, an app icon and a 16-character
social handle.

---

## 8. Generation: semantic association mapping

Do not brainstorm names. Brainstorm **concepts**, then convert.

**Step 1 — Seed the map (30 min).** Write the product's core benefit in one plain sentence, then
cluster around it: what the customer *has* afterwards (state words); what they *escape* (pain words);
the mechanism or material (technical words); metaphors for the transformation (**concrete nouns
only** — a physical object is easier to picture, draw and remember than an abstraction); adjacent
worlds (nature, craft, navigation, architecture, light, time, measurement); and the words customers
actually use (mine reviews, support tickets, sales-call transcripts). Target **100+ words** before
you evaluate a single one.

**Step 2 — Convert words into candidates** using mechanical operators:

| Operator | Method | Illustration (invented) |
|---|---|---|
| Blend | Fuse two words | *clear + ledger* → **Clearedge** |
| Truncate | Cut a word short | *lumina* → **Lumin** |
| Affix | Add a prefix/suffix with meaning | *-craft, -works, -form, hearth-* |
| Respell | Homophone rewrite | *quill* → **Kwil** (spelling-risk flag) |
| Translate | The concept in another language | Screen for meaning in that market |
| Compound | Two real words joined | **Northroot**, **Kettlewright** |
| Rhyme / alliterate | Sound-linked pair | **Perch & Pine** |
| Metaphor noun | A concrete object standing for the benefit | **Anvil**, **Compass**, **Harbor** |

**Step 3 — Do not judge during generation.** Aim for 150–300 raw candidates before the first cut.
A shortlist assembled from 20 candidates is a shortlist of your first instincts.

---

## 9. The screening funnel

Run candidates through the gates **in this order** — each gate is cheaper than the next, so kill
early.

| # | Gate | Method | Kill criterion |
|---|---|---|---|
| 1 | **Category fit** | Does it plausibly belong in the category, or does it cue the wrong one? | Cues a different industry |
| 2 | **Dial/archetype fit** | Rate against your personality spec | Contradicts the dominant trait |
| 3 | **Phonetic fit** | Sound dials vs your dial | Actively fights the dial |
| 4 | **Pronounceability** | Say it cold to three people | Two different pronunciations |
| 5 | **Spelling** | The bad-phone-line test | >25% error rate |
| 6 | **Collision** | Search the exact string + your category | An established player owns it |
| 7 | **Language / slang** | Check your target markets, plus internet slang and initials | Any offensive or comedic reading |
| 8 | **Digital availability** | Exact-match domain (`.com` still carries the most trust for most audiences), plus consistent handles across the platforms you will use | Handle string differs per platform |
| 9 | **Trademark** | Search the relevant classes in every market you'll operate in; then have a qualified attorney clear the finalists | Conflict in your class — do not proceed on your own reading |
| 10 | **Shortlist test** | See §10 | Fails association or recall |

**Notes that save money:** do gates 1–5 on a spreadsheet in a day, and spend gates 6–9 only on 5–10
finalists. Availability is a *constraint*, not a criterion — do not let domain scarcity push you into
a spelling trap; a domain with a short category word appended beats a broken name. Trademark
screening is not legal advice, and neither is this document: budget for a clearance search before
you print anything.

---

## 10. Testing a shortlist without a taste vote

**Never ask "which name do you like best?"** Preference votes measure familiarity and the loudest
person in the room. They also reward safe, generic names. Ask questions with right answers instead.

| Test | What you ask | What you learn | Pass bar |
|---|---|---|---|
| **Blind association** | Show the name alone: "What do you think this company does? What kind of company is it?" | Whether the name cues the right category and feeling | Majority land in the right category *neighbourhood* |
| **Trait rating** | Rate 1–7 on your four chosen trait words plus your forbidden one | Whether the name carries your personality | Dominant trait scores highest; forbidden scores lowest |
| **Recall** | Show 5 names, do 5 minutes of unrelated tasks, ask them to write down what they remember | Stickiness | Your name recalled by a clear majority |
| **Spelling** | Say it once aloud, ask them to type it | The expensive failure mode | ≥75% exact |
| **Pronunciation** | Ask them to read it aloud, cold | Fluency + variant risk | One consistent pronunciation |
| **Confusion** | "Have you heard of this? Does it remind you of another company?" | Collision risk you missed | No consistent competitor named |

Run with **8–15 people from the actual target segment**. This is directional qualitative research —
report it as "6 of 10 read it as a services company," never as a percentage generalised to a market.
Do not run it on friends, your team, or a design community: taste opinions, no purchase intent.
**Decide with the founder, informed by the tests** — a committee average produces the least
objectionable name, which is not the same as the best one.

---

## 11. Naming the things inside the brand

| Layer | Rule |
|---|---|
| **Products** | Descriptive is fine here — the parent brand carries distinctiveness. Clarity beats cleverness inside the house. |
| **Tiers** | Plain, ordinal names (Starter / Standard / Pro) read accessible and social; prestige names (Signature / Platinum) read expensive and exclusive. Pick per your dial, and keep the intended choice in the centre. See `../psychology/07-pricing-psychology.md`. |
| **Features** | Name a feature only if customers will say the word out loud. Otherwise describe it. Every named feature is a term you must teach. |
| **Versions/models** | Numbers work for technical products. Higher numbers read as more advanced; round numbers read as simpler and lower-risk. Do not skip numbers to look bigger — it is a small lie that compounds. |

---

## 12. Tagline vs descriptor vs positioning statement

Three different artefacts, constantly confused. You need all three, written separately.

| Artefact | Audience | Length | Job | Example shape (invented, generic) |
|---|---|---|---|---|
| **Descriptor** | Everyone, everywhere | 2–6 words | Says the category so nobody has to guess. Sits beside the logo, in the meta title, in the bio | "Scheduling software for clinics" |
| **Tagline** | Prospects | 3–8 words | Carries the *feeling* and the differentiator; memorable, repeatable | "Fewer no-shows, quieter mornings" |
| **Positioning statement** | Internal only | 1–3 sentences | The decision rule the team argues from; never printed on the site | "For independent clinics who lose revenue to no-shows, [brand] is scheduling software that confirms patients automatically — unlike general calendar tools, it is built around clinic booking rules." |

Rules:

- **The descriptor is not optional** for a coined or abstract name. It does the clarity work in every
  context — header, footer, social bios, email signature, structured data.
- **A tagline may not be a claim you cannot support.** If it implies a result, it is a claim; see the
  honesty rails in `03-voice-messaging-and-copywriting.md`.
- **Never run a tagline instead of a headline.** The homepage headline sells the specific promise; the
  tagline is brand furniture (`../build/08-page-architecture-and-section-recipes.md`).
- **Test taglines by comprehension, not applause:** "What does this company do, and who is it for?"

---

## 13. Entity consistency: one canonical string, everywhere

This is the highest-leverage, lowest-effort rule in the whole document.

Decide **one canonical name string** and **one canonical one-paragraph description**, then use them
character-for-character everywhere: site header, `<title>` suffix, `Organization` structured data,
footer, social profiles, directory listings, app stores, press boilerplate, email signatures,
`llms.txt`, README files, invoices.

**Why it matters mechanically:** search engines and AI answer systems build an internal record of
your brand as an *entity* by reconciling mentions across sources. Every variation — a stray "The", a
different capitalisation, a hyphen that appears in some places and not others, three different
one-liners — splits the evidence and weakens the record. Consistent repetition of the same string
and the same description makes the entity easy to resolve and easy for a model to reproduce
accurately when someone asks about you. The full mechanism and the file-level wiring are in
`../search/12-geo-ai-search.md` and `../search/13-schema-and-technical-wiring.md`.

### The canonical block (fill once, paste forever)

```
CANONICAL NAME:      Northroot            (exact casing; no "The", no Inc., no tagline)
LEGAL NAME:          Northroot Ltd.       (used only in legal/footer/schema legalName)
DESCRIPTOR:          Scheduling software for clinics
ONE-LINE:            Northroot is scheduling software that cuts clinic no-shows.
ONE-PARAGRAPH:       Northroot is scheduling software for independent clinics. It confirms
                     appointments automatically, fills cancellations from a waitlist, and
                     reports on no-show rates. Founded 20XX, used by clinics in X markets.
PRONUNCIATION:       NORTH-root
NEVER WRITE:         North Root, north-root, NorthRoot, The Northroot
```

Keep this block in the repository so both humans and coding agents read the same source of truth. If
you change it, change it everywhere in one pass — a half-migrated name is worse than either version.

---

## Apply it

- [ ] Personality spec written: one dominant trait, two supporting, one **forbidden**, with the tie-break arbiter line.
- [ ] Dial position chosen (calm ↔ energetic) and recorded, with the list of tactics it inverts.
- [ ] One primary archetype selected (plus at most one non-opposing secondary), and three things it forbids written down.
- [ ] Archetype translated into colour / type / imagery / motion directions and handed to `../psychology/06-color-and-typography.md`.
- [ ] 100+ concept words mapped before any name was written; 150+ raw candidates generated.
- [ ] Name type chosen deliberately (descriptive / suggestive / coined / abstract / founder / acronym) with the trade-off named.
- [ ] Phonetics checked against the dial — used as a tie-breaker only, with no performance claims attached.
- [ ] Bad-phone-line spelling test run with 8+ target-segment people; anything above ~25% error killed.
- [ ] Finalists cleared for collisions, slang and other-language readings; trademark search run by a qualified attorney before any spend.
- [ ] Shortlist tested by association / trait rating / recall / spelling — no taste votes anywhere in the process.
- [ ] Descriptor, tagline and internal positioning statement written as three separate artefacts.
- [ ] Canonical name string + one-paragraph description locked and committed to the repo.
- [ ] Canonical block pasted into `../templates/brand-brief.md` and into the build prompts in `../ops/16-prompt-pack.md`.
- [ ] No invented statistics, ratings or claims introduced anywhere in the identity or tagline.

## Related

- [00-START-HERE.md](../00-START-HERE.md) — the arousal dial that personality sets
- [01-positioning-and-category.md](./01-positioning-and-category.md) — the category and audience this identity dresses
- [03-voice-messaging-and-copywriting.md](./03-voice-messaging-and-copywriting.md) — turning personality into sentences
- [../psychology/05-visual-attention-and-layout.md](../psychology/05-visual-attention-and-layout.md) — attention rules that hold at both dial ends
- [../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md) — archetype → palette and type decisions
- [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md) — naming and framing tiers
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — where descriptor, tagline and headline each live
- [../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md) — encoding identity as tokens
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — why entity consistency decides how AI answers describe you
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — where the canonical strings get wired
- [../templates/brand-brief.md](../templates/brand-brief.md) — the fill-in artefact for everything above
- [../ops/16-prompt-pack.md](../ops/16-prompt-pack.md) — prompts that carry the identity spec to a coding agent
