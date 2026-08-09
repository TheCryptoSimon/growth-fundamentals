# Colour and Typography

The two decisions that set a site's emotional temperature before a single word is read. This doc separates
what actually generalises about colour and type from folklore, then turns each finding into a build rule with
numbers. Read it when you are choosing the primary colour, the typefaces, or the scale — before any page is
designed. Pair it with `09-design-system-and-tokens.md`, which turns these decisions into variables.

---

## 0. Set the dial first

Nearly every tactic below flips depending on one prior decision. Make it now and write it into the brand brief.

| Dial position | Reads as | Use when | Colour posture | Type posture |
|---|---|---|---|---|
| **Calm / premium / trustworthy** | considered, safe, expensive, expert | high price, high risk, slow decision, health, money, B2B, professional services | cool or neutral, low saturation, light or very dark surfaces, one accent | light-to-medium weights, generous tracking on labels, roomy line-height |
| **Energetic / urgent / playful** | alive, cheap-and-cheerful, now, fun | impulse purchase, entertainment, youth, promotions, marketplaces, events | warmer, higher saturation, more than one accent, stronger colour blocking | heavier weights, tighter tracking, bigger jumps between steps |

The rest of this document names which end each rule belongs to. **If a rule does not say "calm" or
"energetic", it holds at both ends.** Do not apply a high-arousal tactic to a trust-first brand because it
"tested well" somewhere else — it tested well on a different dial position.

Position the dial in `../templates/brand-brief.md`. Everything downstream inherits it.

---

## 1. Colour: what generalises, and what does not

### 1.1 The three dimensions that carry meaning

Research in consumer psychology (see the colour work summarised in Nick Kolenda's consumer-psychology
library, and the perception literature it draws on) converges on an uncomfortable conclusion for brand
decks: **hue is the weakest of the three colour dimensions.** Temperature, saturation and lightness carry
the reliable signal.

| Dimension | What it reliably reads as | Mechanism | Build rule |
|---|---|---|---|
| **Temperature** (warm ↔ cool) | Warm = activating, alert, impulsive, dominant, time-feels-shorter. Cool = calm, deliberate, trustworthy, patient. | Warmth is tied to physical heat and sun, so it travels better across cultures than a specific hue's symbolism does — more portable, not universal. Verify it holds in your markets before betting a rebrand on it. | Calm brand: cool or neutral base, warm only as a small accent. Energetic brand: warm base is legitimate. Never put a warm saturated field behind a long form or a loading state. |
| **Saturation** (vivid ↔ muted) | Vivid = loud, strong, potent, urgent, *bigger*, sooner, more noticeable. Muted = gentle, natural, healthy, premium, private, further away. | Saturation is an arousal cue; arousal is misread as intensity of the thing itself. | Treat saturation as a **budget**. Spend it on one element per viewport. Everything else desaturates. |
| **Lightness** (light ↔ dark) | Light = easy, light-weight, approachable, natural, safe. Dark = heavy, dense, durable, serious, important, rich. | Weight and importance are physically grounded metaphors. | Light surfaces for "this is easy to start". Dark surfaces for "this is substantial / serious / expensive". |

Two corollaries you can act on directly: a muted palette signals gentle, natural and premium while a vivid one
signals potent and effective (skincare goes muted; a cleaning product goes vivid); and low saturation also
signals **discretion**, so anything a buyer might feel self-conscious about — a debt tool, a medical product,
a beginner's course — should mute the palette to lower the felt exposure.

### 1.2 What does NOT generalise: fixed meanings per hue

"Blue means trust, green means growth, red means passion" is the most repeated and least reliable claim in
brand design. Hue meaning is dominated by **culture, category convention, personal association and the
object the colour is on**. The same green reads "fresh" on a salad box and "sickly" on a face. Treat hue
charts as folklore.

**What to do instead — pick hue on strategy, not on meaning:**

| Situation | Hue choice | Why |
|---|---|---|
| Crowded category, you are credible enough to lead | A hue nobody in the set owns | Distinctiveness aids memory and recall; you become "the orange one" |
| New entrant, low trust, buyer risk-averse | A hue near the category convention | Convention borrows the category's legitimacy; the buyer does not have to re-learn what you are |
| Category convention is itself distrusted | Break it hard, then over-invest in trust proof elsewhere | The break must be paid for with evidence, not just aesthetics |

Do the audit before you choose: list the top 8 competitors, screenshot their primary colour, and place yours
on the map. See `../brand/01-positioning-and-category.md` for the category framing this depends on.

### 1.3 Deriving your primary from brand adjectives

A repeatable procedure that avoids "we all liked the teal":

1. Write the 3 adjectives from the brand brief (e.g. *precise, calm, expert*).
2. Score the brand 0–100 on **"loud / immediate / intense"** → that is roughly your **saturation**.
3. Score it 0–100 on **"light / easy / effortless"** → that is roughly your **lightness**.
4. Pick temperature from the dial (§0), then choose any hue inside that temperature using §1.2.
5. Enter S and L into an HSL picker, sweep the hue, and take the first value that survives §4's contrast gate.

A calm expert brand typically lands somewhere near `S 20–45 / L 25–45`. A playful consumer brand near
`S 65–90 / L 45–60`. These are starting coordinates, not laws.

---

## 2. Light interface or dark interface

This is not a taste question, but it is not a settled empirical one either. **There is no reliable general
finding that light themes convert better or that dark themes are read for longer** — treat the table below
as convention and craft, matched to the reading conditions each surface actually has, not as a measured
effect. What *is* well established is narrower and it belongs to legibility: dark backgrounds need lighter
type weights and slightly looser tracking, and long reading on either theme is hurt by low contrast.

| | Light interface | Dark interface |
|---|---|---|
| Conventional for | Acting: signing up, buying, submitting a form | Dwelling: reading, editing, monitoring, long sessions |
| Feels | open, visible, public, easy to act in | enclosed, private, focused, cinematic |
| Best for | marketing site, pricing page, checkout, forms, onboarding | media players, dashboards, editors, code tools, night-use apps |
| Watch out | large pure-white fields can feel clinical and cheap without texture | text on dark needs *lighter weights and more tracking*, or it smears |

**Build rule.** Default the marketing site to light, because that is what visitors expect of one and
expectation-matching is a real fluency gain (§10); go dark for the logged-in product if it is a long-session
tool or is used in the dark. Shipping both means every colour token needs a dark-mode pair from day one —
decide before you build tokens, not after (`../build/09-design-system-and-tokens.md`). If you ship dark,
never use the saturated accent as a large field (it vibrates); drop its saturation ~10–15% and raise
lightness for dark. If you want to claim a theme performs better *for your product*, that is a measurement
question, and at a new brand's traffic you almost certainly cannot answer it
(`../ops/14-measurement-and-experimentation.md` §9).

---

## 3. Building a palette from scratch

The whole palette, as a spec you can hand to an agent:

```
PRIMARY        1 colour   — from §1.3
PRIMARY SCALE  5–9 steps  — tints and shades of the primary
NEUTRALS       ~10 steps  — near-white → near-black, each tinted toward the primary
FUNCTIONAL     4 colours  — success, warning, danger, info
ACCENT         0–1 colour — only if the primary cannot carry the focal CTA
```

### 3.1 The primary scale

Generate 5–9 steps by layering white and black over the primary at increasing opacity, then sampling. Do not
just change lightness in HSL — that produces muddy mid-tones. Name them numerically (`primary-50` … `900`) so
the scale is machine-usable. **Fewer steps (5)** reads uniform and calm; **more steps (9)** reads varied and
energetic. Keep the *true* primary reserved for the logo and one interactive element — if it appears in six
places, it is no longer primary.

### 3.2 Neutrals — the step almost everyone skips

Build ~10 neutral steps, and **mix a small amount of the primary hue into every one** (roughly 3–8%
saturation). Pure system greys look accidental; hue-tinted greys look designed, and they make the whole
interface feel like one object. This single move separates amateur palettes from professional ones more
reliably than the choice of primary.

**Never use pure `#000000` for large areas.** It is heavier than any real-world black and produces harsh
halation on light themes. Use a near-black tinted toward the primary (cool brands: a blue-black; warm brands:
a brown-black); reserve pure black, if at all, for very small text. Equally, **avoid pure `#FFFFFF` as the
only light surface** — keep a second, faintly tinted surface so cards and sections separate without borders.

### 3.3 Functional colours, and the alarm-red problem

| Role | What it must do | Calm brand | Energetic brand |
|---|---|---|---|
| Success | confirm without celebrating | muted green, low saturation, small area | brighter green, may animate once |
| Warning | slow the user down | amber, low saturation, always paired with an icon | saturated amber |
| Danger / error | stop the user | see below | saturated red is acceptable |
| Info | explain, not alert | a desaturated blue or the primary tint | primary tint |

**The alarm-red rule.** Saturated red is a *stop* signal. Using it for routine, non-failure states — an
empty field the user simply has not reached yet, a "0 items" count, an unmet optional condition, a form
field that turns red the moment focus leaves it — trains the visitor to feel low-grade threat while using
your product. On a calm/premium brand this is directly counter-brand: the palette says "safe, considered"
and the states say "you are doing it wrong."

Use instead, in order of severity: **neutral grey + helper text** for "not done yet" (no colour at all);
**amber + icon + a sentence saying what to do** for "needs attention"; **red only for a real, blocking failure
the user must resolve now** — payment declined, upload failed.

Two notes: if your brand primary *is* red, do not also use red for errors — the brand and the alarm become the
same object. And a desaturated blue works well as a universal error colour, because it reframes the event as
"here is a correction" rather than "you failed".

### 3.4 The saturation-hoarding rule

> **One element per viewport gets full saturation. Everything else is muted or neutral.**

That element is almost always the primary call to action. If a hero has a saturated button, a saturated
badge, a saturated illustration and a saturated navigation pill, the button has no advantage and the page
has no focal point. Desaturate imagery placed near a CTA so the CTA wins on colour alone.

This is the colour half of the focal-point discipline in `05-visual-attention-and-layout.md`.

---

## 4. Contrast and accessibility: hard gates, not preferences

These are pass/fail. A design that fails them is not "bold", it is broken for a measurable share of visitors,
and low contrast reduces conversion for everyone on a phone in daylight.

| Element | Minimum contrast ratio (WCAG AA) |
|---|---|
| Body text and any text under ~24px (or under ~19px bold) | **4.5 : 1** |
| Large text — ~24px+, or ~19px+ bold | **3 : 1** |
| Interactive component boundaries, focus rings, icons carrying meaning, chart strokes | **3 : 1** |
| Decorative graphics, disabled controls | no requirement — but disabled must still be distinguishable |

Additional gates that catch the common failures:

- [ ] **Never let colour alone carry meaning.** Every colour-coded state also has an icon, a word, a shape or
      a position. Test by converting a screenshot to greyscale — if you cannot read the status, it fails.
- [ ] **Placeholder text is not label text.** Placeholders are typically low-contrast by design; if the label
      only exists as a placeholder, the field becomes unlabelled the moment the user types.
- [ ] **Focus states must be visible** and meet 3:1 against the adjacent surface. Do not remove the outline
      without replacing it.
- [ ] **Check the accent on BOTH surfaces** it will sit on (light card and dark section), not just one.
- [ ] **Check text over images** with the darkest and lightest images that can appear, or apply a scrim.
- [ ] Measure with a real contrast checker at build time. Do not eyeball ratios, and do not trust a hex value
      because it "looks fine on this monitor".

Aim for AA as the floor and AAA (7:1) for long-form body copy — long reading is where low contrast costs the
most, and higher contrast on body text has no brand downside.

---

## 5. Colour and category fit

Every category carries a colour convention: finance skews to deep blues and greens, food to warm reds and
yellows, health to whites, blues and soft greens, luxury to black, cream and metallics, developer tools to
dark surfaces with a single neon accent.

Convention is a shortcut for the visitor: it answers "what kind of thing is this?" in under a second.

| Strategy | When it wins | Cost you must pay |
|---|---|---|
| **Match convention** | Low-trust entrant, complex product, buyer needs to categorise you fast | You look like everyone else — differentiate on layout, voice and photography instead |
| **Adjacent shift** (same family, distinct value) | Most brands, most of the time | Requires discipline: the shift must be visible at thumbnail size |
| **Deliberate break** | The category convention itself signals something you are rejecting (e.g. a dental clinic that refuses the clinical-blue-and-white look to feel like hospitality) | The break has to be *coherent*, not just contrarian, and you must over-supply proof elsewhere |

**Test.** Put your hero as a 200px thumbnail beside eight competitors'. If a stranger cannot pick yours out in
two seconds, the palette is doing no brand work. If they can pick yours but cannot tell what category it is
in, you broke convention without paying for it.

---

## 6. Typography: what a typeface class signals

A typeface's visual traits activate related concepts, and those concepts transfer to the brand. Choose type
whose adjectives match the brand's adjectives — not whose adjectives you personally like.

| Class | Signals | Baggage / risk | Use for |
|---|---|---|---|
| **Serif** | traditional, established, editorial, credible, scholarly | can read as slow, old, institutional | headings on trust-first brands; long-form body on editorial sites |
| **Sans-serif** | modern, neutral, clean, efficient | neutral to the point of invisible; easy to look generic | UI, body copy, most interfaces |
| **Slab serif** | sturdy, blunt, confident, workmanlike | loud at large sizes; dates quickly | display headlines for practical/rugged brands |
| **Geometric sans** | precise, rational, designed | low-contrast letterforms hurt readability at small sizes (a/o/e collapse) | display and headings, rarely small body |
| **Humanist sans** | approachable, readable, human | less "designed" | the safest body choice at every dial position |
| **Monospace** | technical, precise, raw, code | reads as unfinished or developer-only outside tech | code, data, timestamps, one accent label |
| **Script / handwritten** | personal, hand-made, warm, gift-like | drops readability hard; can read as amateur or wedding-stationery | a signature, a single short flourish — never a paragraph |
| **Display / novelty** | whatever it depicts | one-note; unusable below ~32px | logo and hero only, if at all |

**Default pairing that is hard to get wrong:** a serif or a distinctive sans for headings + a humanist sans
for body. Two families is the correct number. Three is a decision you must be able to defend; four is a bug.

---

## 7. The tone dials in type

Each of these is a slider you can move without changing typeface.

| Dial | One end | Other end | Rule |
|---|---|---|---|
| **Weight** | Light/Regular = refined, delicate, premium, and most readable at body sizes | Bold/Black = powerful, assertive, urgent — but can read domineering or shouty | Calm: 300–500 for body and most headings, 600 only on the focal CTA. Energetic: 700–900 headlines are on-brand. Never set body copy below 400 on a light background. |
| **Width** | Condensed = tight, precise, slim, efficient; fits more per line | Extended = stable, heavy, durable, expansive | Match to the claim. A "compact" product in a condensed face is congruent. Avoid condensed for body text — it costs readability. |
| **Tracking** | Tight = crowded, busy, dense — and reads *cheaper* | Loose = relaxed, spacious, premium | Calm/premium: track small caps and eyebrow labels out (+0.06em to +0.12em). Never track out body copy. Tighten headlines slightly (−0.01 to −0.02em) at large sizes to close optical gaps. |
| **Case** | Sentence case = most readable | UPPERCASE = strong, formal, premium — and slow to read | Sentence case for headlines, body, buttons and links. UPPERCASE only for labels of roughly 1–3 words: eyebrows, badges, table headers, small nav. Never a full uppercase sentence. |
| **Roundness** | Round letterforms and corners = friendly, soft, safe | Angular = formal, mechanical, serious | Carry it through to the UI: border-radius is a typographic decision too. Pick one radius language and apply it to buttons, cards and images alike. |
| **Slant** | Upright = stable | Italic = fast, urgent, in-motion | Italics for citation and emphasis. **Never italicise prices or CTAs on a calm brand** — the slant injects urgency the brand is trying not to have. |

**Small caps.** Tracked-out small caps read as premium and structured and solve the eyebrow-label problem
elegantly. Use real small caps or `font-variant: all-small-caps` where the family supports it; faked small
caps (scaled-down capitals) look thin and wrong beside the real thing.

---

## 8. Readability constants

These are close to universal. Treat them as build defaults and deviate only with a reason.

| Property | Value | Notes |
|---|---|---|
| **Measure (line length)** | 45–75 characters; ~66 is the sweet spot | Set with `max-width: 65ch` on prose containers, not a pixel value |
| **Body size** | 16–18px minimum on desktop; never below 16px on mobile | Below 16px on mobile, iOS zooms form fields on focus |
| **Body line-height** | 1.5–1.7 | Longer measure → higher line-height |
| **Heading line-height** | 1.1–1.25 | Large type needs *less* leading, not more |
| **Small text (12–14px)** | line-height ~1.6–1.8, plus +0.01–0.03em tracking | Small text needs both more leading and more tracking |
| **Paragraph spacing** | 0.75–1.25× the body line-height as margin-bottom | Space between paragraphs must clearly exceed space between lines, or the block reads as one slab |
| **Space above a heading** | ~2× the space below it (up to 3× at a major section break) | Headings belong to the content that follows them (proximity) |
| **Bullets** | max ~2 lines each. **3–5 per list where the reader must weigh the items**; up to ~7 for a reference list they only scan | Longer than that and it is prose pretending to be a list. Persuasive lists are capped harder — see `../brand/03-voice-messaging-and-copywriting.md` §10 |
| **Justification** | left-aligned (ragged right) always | Justified web text creates rivers; centred text is only for ≤3 lines |
| **Hyphenation** | off for headings, optional for narrow-column body | Never hyphenate a headline |

**Mobile-specific:** re-check measure at 375px width. A 16px body in a full-width container on a phone lands
near 35–40 characters, which is short but acceptable; a 14px body with side padding can drop under 30 and
starts to feel like a poem.

---

## 9. Building a type scale

Use a ratio, not arbitrary numbers. A scale makes every future decision automatic and stops per-page drift.

1. **Pick a base:** 16px (or 17–18px if the audience skews older or the content is long-form).
2. **Pick a ratio:**

| Ratio | Name | Character | Fits |
|---|---|---|---|
| 1.125 | Major second | very tight, dense, utilitarian | data-heavy dashboards |
| 1.200 | Minor third | calm, close, editorial | text-heavy sites, documentation |
| 1.250 | Major third | balanced — the safe default | most marketing sites |
| 1.333 | Perfect fourth | confident, clear hierarchy | landing pages |
| 1.500 | Perfect fifth | dramatic, poster-like | bold, energetic brands |

3. **Generate 5–7 steps** up from the base plus 1–2 down. Round to whole pixels. Example at base 16 / ratio
   1.25: `13 · 16 · 20 · 25 · 31 · 39 · 49 · 61`.
4. **Use a smaller ratio on mobile** (e.g. 1.2 where desktop is 1.333), or clamp: a desktop 61px headline at
   375px is unreadable. `clamp()` with viewport units handles this in one line.
5. **Freeze it.** Every size on the site comes from the scale. No one-off `font-size: 22px`.

**Pairing rules for the scale:**

- Adjacent steps are too close to signal hierarchy. Skip a step between a heading and its body.
- A step change and a weight change and a colour change all at once is one change too many. Use two.
- Keep no more than 3 active text colours: primary text, secondary/muted text, and link/accent.
- Line-height decreases as size increases — bind it to the step, not to the element.

---

## 10. Legible → fluent → believed

The chain that makes typography a persuasion decision rather than a decoration decision:

> Text that is **easy to process** feels **familiar**, familiarity feels like **truth and competence**, and the
> reader silently credits the *product* with that ease.

People are generally poor at knowing *why* something felt easy. They experience the ease and attribute it to
the claim being sound or the company being competent. This is why illegible type does not merely annoy — it
quietly lowers belief in what the type says.

Practical consequences: the most persuasive typographic choice is usually the most readable one; fixing
contrast, measure and line-height is often worth more than rewriting the headline; expectation-matching counts
as fluency, so a pricing page that *looks* like a pricing page is trusted faster than a clever one; and short
sentences in readable type are two multipliers on the same effect
(`../brand/03-voice-messaging-and-copywriting.md`).

### The disfluency exception (and why it is almost never yours)

There is a real, narrow counter-effect: **slight** processing difficulty can increase attention, effortful
encoding and memory, and can make an item feel special or artisanal rather than mass-produced.

Where it can legitimately apply: a single luxury product name, a limited-edition label, a high-end restaurant
menu, a printed invitation. **Where it must not apply:** headlines, body copy, navigation, buttons, prices,
forms, error messages, legal text — anything on a page whose job is to get a decision made. On a marketing
page the fluency effect dominates, and a memory benefit is worthless if the reader leaves. If you want the
effect, buy it with an unusual *layout* or an unexpected *image*, not with unreadable type.

Flag for honesty: making terms, prices or cancellation paths harder to read is not a disfluency tactic, it is
a dark pattern. The line is simple — **difficulty that serves the reader's attention is a craft choice;
difficulty that serves your conversion rate at the reader's expense is manipulation.** Anything the buyer
would be annoyed to discover was deliberate belongs on the wrong side of it.

---

## 11. Starter specifications

Two ready-to-use starting points. Copy the one that matches your dial, then substitute your own hue. Both
still need the §4 contrast check with real values before shipping.

### 11.1 Calm / premium / trust-first

*(a B2B compliance platform, a private dental clinic, a wealth-planning service, a professional course)*

| Token | Value / rule |
|---|---|
| Theme | Light. Off-white base, never pure `#FFFFFF` everywhere |
| Primary | Cool or neutral hue, `S 20–40 / L 28–42` |
| Accent (CTA) | The primary at full strength, used on exactly one element per viewport |
| Neutrals | 10 steps, each carrying 4–6% of the primary's hue |
| Near-black | Tinted, ~`L 12–18` — never `#000000` |
| Surfaces | Base + one 2–4% tinted surface for cards/sections |
| Functional | Muted green / amber-with-icon / red reserved for blocking failures only |
| Saturation budget | 1 saturated element per viewport |
| Heading face | Serif, or a low-contrast humanist sans |
| Body face | Humanist sans, 400 weight |
| Weights in play | 400 body · 500 subheads · 600 focal CTA only |
| Base size / ratio | 17–18px / 1.200–1.250 |
| Body line-height | 1.6–1.7 |
| Measure | 62–70ch |
| Labels | UPPERCASE small caps, 12–13px, tracking +0.08em to +0.12em |
| Case | Sentence case everywhere else, including buttons |
| Radius | Soft and consistent — 8–12px on cards and buttons |
| Motion | One gentle reveal maximum; honour `prefers-reduced-motion` |
| Forbidden | italic prices, countdown styling, alarm-red for routine states, tight tracking, 700+ body weight |

### 11.2 Energetic / urgent / playful

*(a DTC kettle, a ticketing marketplace, a mobile game, a flash-sale retailer)*

| Token | Value / rule |
|---|---|
| Theme | Light for conversion pages; dark permitted for immersive/media surfaces |
| Primary | Warm or high-chroma hue, `S 60–90 / L 45–58` |
| Accent (CTA) | A second high-contrast hue — the primary and the CTA may differ |
| Neutrals | 10 steps, 6–8% primary tint — warmer greys |
| Near-black | Tinted warm, ~`L 10–16` |
| Surfaces | Colour blocking allowed: full-bleed primary sections between neutral ones |
| Functional | Saturated green / saturated amber / saturated red are all on-brand |
| Saturation budget | 2 saturated elements per viewport maximum — still not unlimited |
| Heading face | Geometric or grotesque sans, or a slab for a practical-goods brand |
| Body face | Humanist or neutral sans, 400–450 |
| Weights in play | 400 body · 600 subheads · 700–900 display headlines |
| Base size / ratio | 16px / 1.333–1.500 |
| Body line-height | 1.5–1.6 |
| Measure | 50–65ch |
| Labels | UPPERCASE, 12–14px, 600–700 weight, tracking +0.04em |
| Case | Sentence case body; short uppercase badges and eyebrows are fine |
| Radius | Pick a pole — either near-0 (sharp, modern) or heavily rounded (playful). Do not sit in the middle |
| Motion | Entrance animation permitted; still honour `prefers-reduced-motion` |
| Forbidden | fake countdowns, invented scarcity, red used where nothing is actually failing, contrast below AA "for the look" |

Note what is forbidden in **both** columns: fabricated urgency and sub-AA contrast. Those are not dial
positions, they are defects.

---

## 12. Failure modes to check for

| Symptom | Cause | Fix |
|---|---|---|
| Feels "generic" despite a good logo | Pure system greys, unmodified defaults | Tint every neutral toward the primary |
| Nothing draws the eye | Saturation spent in 5 places | Enforce the one-saturated-element rule |
| Premium brand feels cheap | Tight tracking, crowding, too many weights | More spacing, cut to 3 weights, raise whitespace |
| Copy skimmed but not absorbed | Measure over ~85 chars, line-height under 1.4 | `max-width: 65ch`, line-height 1.6 |
| "The site felt stressful" | Warm saturated fields, red on routine states, motion | Cool the base, red for blocking failures only |
| Headlines look wrong when large | Body line-height inherited by display type | Bind line-height to the scale step |
| Collapses on mobile | Fixed desktop scale, no clamp | Smaller ratio or `clamp()` above the base |
| Colour-blind users misread status | Colour is the only cue | Add icon + word; greyscale-screenshot test |

---

## Apply it

- [ ] Dial position (calm/premium vs energetic) is written into the brand brief before any colour is picked.
- [ ] Primary colour derived from saturation + lightness scores and a competitor hue map — not from taste.
- [ ] Light vs dark interface chosen against the goal (conversion vs engagement), and dark-mode token pairs
      planned if both ship.
- [ ] Palette generated: 1 primary, 5–9 scale steps, ~10 neutrals **tinted toward the primary**, 4 functional
      colours.
- [ ] No pure `#000000` on large areas; a tinted near-black and a tinted off-white surface both exist.
- [ ] Alarm-red is reserved for blocking failures; routine "not done yet" states use neutral or amber + icon.
- [ ] Exactly one fully saturated element per viewport, and it is the primary CTA.
- [ ] Every text/background pair measured with a contrast checker: 4.5:1 body, 3:1 large text and UI edges.
- [ ] Greyscale screenshot test passed — no meaning is carried by colour alone.
- [ ] Two typefaces maximum, chosen against the brand's adjectives, with the class signal named in the brief.
- [ ] Type scale frozen: one base size, one ratio, 5–7 steps, mobile clamped; no off-scale sizes anywhere.
- [ ] Readability constants met: 45–75ch measure, 1.5–1.7 body line-height, paragraph spacing clearly larger
      than line spacing.
- [ ] Case discipline: sentence case for everything except 1–3 word labels; no uppercase sentences; no
      italicised prices or CTAs on a calm brand.
- [ ] Tokens exported as variables (not hard-coded hex/px) and handed to `../build/09-design-system-and-tokens.md`.

---

## Related

- [04 — Persuasion core](04-persuasion-core.md) — fluency, spreading activation and the mechanisms these rules run on
- [05 — Visual attention and layout](05-visual-attention-and-layout.md) — the focal-point discipline that the saturation budget serves
- [07 — Pricing psychology](07-pricing-psychology.md) — how type size, weight and case are applied to price figures
- [01 — Positioning and category](../brand/01-positioning-and-category.md) — the category map behind the hue decision
- [02 — Identity, archetype and naming](../brand/02-identity-archetype-and-naming.md) — where the brand adjectives come from
- [03 — Voice, messaging and copywriting](../brand/03-voice-messaging-and-copywriting.md) — the copy side of the fluency chain
- [08 — Page architecture and section recipes](../build/08-page-architecture-and-section-recipes.md) — where these tokens get used
- [09 — Design system and tokens](../build/09-design-system-and-tokens.md) — turning this doc into variables
- [10 — Conversion audit checklist](../build/10-conversion-audit-checklist.md) — the pass/fail gate before launch
- [Brand brief template](../templates/brand-brief.md) — record the dial, the palette and the type decisions here
