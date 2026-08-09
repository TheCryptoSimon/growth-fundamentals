# Visual Attention & Layout

How a page spends the visitor's limited attention: what actually gets looked at, in what order, and how
layout either earns a decision or burns the budget. Read this before wireframing any page, and again when a
page "looks fine" but nobody clicks the thing you need them to click.
Companion to [04-persuasion-core.md](04-persuasion-core.md) (why people say yes) and
[06-color-and-typography.md](06-color-and-typography.md) (the materials this doc arranges).

---

## 0. Name the dial before you lay anything out

Almost every attention lever below has an arousal setting. Decide the brand's position once and apply it
consistently — a page that mixes both ends reads as unstable, and instability is the enemy of trust.

| | **Calm / premium / trust end** | **Energetic / urgent / playful end** |
|---|---|---|
| Typical brands | Advisory, clinic, B2B tool, high-ticket service, anything asking vulnerability or money | Flash sale, game, event, youth DTC, limited drop |
| Accent use | One saturated accent on the whole viewport | Multiple accents, high saturation |
| Motion | Slow, eased, few, once | Fast, repeated, looming, pulsing |
| Density | Generous space, ≤4 items per group | Tight grids, dense grids, stacked offers |
| Focal grab | Contrast + isolation | Contrast + motion + colour + size, stacked |
| Failure mode | Reads empty, under-signalled | Reads cheap, distrusted, ignored (banner blindness) |

**Rule:** every "turn it up" tactic below is written for the energetic end. On the calm end you invert it and
spend your single allowed attention-grab on the one primary action. Never present a high-arousal lever as a
universal best practice — it isn't.

---

## 1. Salience is contrast against local context, not absolute loudness

**What it is.** An element is noticed because it *differs* from what surrounds it — in hue, saturation,
size, orientation, weight, or spacing. Loudness in absolute terms is irrelevant.

**Mechanism.** Perception is comparative. The visual system encodes differences, so a feature that is unique
in its neighbourhood pops out pre-attentively; a feature that is common in its neighbourhood must be found
by serial search, which most visitors will not perform.

**How to apply.**
- One accent in a muted field outranks five accents in a loud field. If everything is emphasised, nothing is.
- Contrast is additive across dimensions. A focal element that is *bigger* and *more saturated* and *more
  isolated* wins decisively; picking only one dimension usually loses to a busy neighbour.
- Contrast is **local**. A green button inside a green-tinted card is invisible; the same button on a neutral
  card is unmissable. Audit salience at the section level, not the palette level.
- The cheapest way to make an element louder is to make its neighbours quieter. See §3.

> **Dial.** Calm end: create contrast with size, weight, and empty space, and keep saturation as a scarce
> resource. Energetic end: create contrast with saturation and motion first — it is faster, and the brand can
> afford the noise.

---

## 2. One focal point per viewport

**What it is.** For each screenful the visitor can see at once, exactly one element is designed to be seen
first. On a marketing page that is normally the primary action; on an editorial page it is the headline.

**Mechanism.** People infer intent from their own attention — "I keep looking at this, so it must be the
thing that matters." A single unambiguous entry point also removes the small decision cost of "where do I
start?", which is where a lot of bounces actually happen.

**How to apply.**
- Write the intended eye path for each viewport before you design it: *first → second → third*. Three stops
  maximum. If you cannot name them, the section is not designed yet.
- Never place two solid, equally weighted buttons in one viewport. One solid primary, at most one quiet
  secondary (ghost, outline, or plain text link).
- The focal element gets the largest local size jump **and** the most surrounding empty space. Isolation is
  the most underused salience channel because it costs layout area rather than ink.
- Repeat the same primary action in a consistent visual form down the page. Familiarity makes it faster to
  find each time; a redesigned button on every section makes each one feel like a different offer.
- Test per viewport at real device widths. A layout with one focal point on desktop routinely has three on
  mobile once the columns stack.

---

## 3. Demoting the neighbours — the demotion ladder

When a focal element loses, the usual cause is a strong neighbour, not a weak focal element. Demote in this
order, cheapest first, and stop as soon as the focal element wins the squint test (§6).

| Step | Move | Typical effect |
|---|---|---|
| 1 | Drop the neighbour's colour saturation toward the neutral ramp | Large, free, reversible |
| 2 | Reduce weight (bold → regular; regular → light) | Large on text-heavy blocks |
| 3 | Reduce size one step on the type scale | Medium |
| 4 | Convert a solid button to ghost or text link | Large on competing CTAs |
| 5 | Desaturate or blur imagery adjacent to the focal element | Large when photos are involved |
| 6 | Add space around the focal element (pull neighbours away) | Large, costs layout height |
| 7 | Move the neighbour below the fold or into a disclosure | Total, costs discoverability |

Two standing rules: **imagery next to a primary action should be quieter than the action**, and **secondary
navigation is a neighbour** — a loud header link set competes with a hero CTA more often than designers
expect.

---

## 4. Gestalt grouping — six principles, six concrete layout moves

**Mechanism.** Before anyone reads a word, the visual system parses the page into objects and groups. Those
groups become the reader's mental model of the page structure. If your grouping and your logical structure
disagree, the visitor's model of your offer is wrong before comprehension starts.

| Principle | What it says | Layout application (concrete) |
|---|---|---|
| **Proximity** | Near things read as one unit | Heading sits closer to its own body than to the section above — **the space above a heading is ~2× the space below it**, stretching toward 3× at a major section break. Form labels hug their inputs. This one rule fixes most "confusing page" complaints. |
| **Similarity** | Same shape/colour/size read as one set | All items of the same rank share one card style, one icon style, one type step. If two items look different, the reader assumes they *are* different — never vary style for visual interest alone. |
| **Common region** | A shared container beats proximity | Bind a cluster (a feature triad, a filter chip group) inside one soft panel or a tinted band so it reads as one family even when spacing is inconsistent. Use this to separate two adjacent groups without adding a divider. |
| **Continuity** | The eye follows lines and alignment | Keep one strong left alignment edge down a text column; the eye rides it downward for free. Every unnecessary alignment change is a stop sign. Break continuity deliberately at a section boundary. |
| **Closure** | Incomplete shapes are completed mentally | A card that is deliberately cropped at the viewport edge tells the reader the row scrolls sideways. Conversely, a section that closes cleanly at a common viewport height reads as the end of the page — let the next section peek above the fold to defeat that false bottom. |
| **Figure / ground** | One layer reads as object, one as backdrop | The subject must be sharp and the background soft, blurred, or low-contrast. Ambiguous figure/ground (busy photo behind text) costs both legibility and trust. If the text needs a scrim, the scrim must cover the *whole* text block, not just the headline. |

**Grouping capacity.** People take in small sets at a glance; beyond roughly four items a group must be
counted rather than perceived. Cap groups at four. If you have seven features, chunk them into two labelled
clusters instead of one row of seven. A merely-labelled grouping makes a list feel organised even when the
split is arbitrary — this is a genuine effect, and it is also the point at which grouping can become
misleading, so keep the labels honest.

**The cap applies to sets the reader must *weigh*, not to sets they merely *scan*.** Four is the ceiling for
anything comparative — pricing tiers, options, competing paths, nav sections — because each extra item
multiplies the comparisons. A feature grid the reader browses rather than chooses from can run to six cards
without cost, provided nothing in it is a decision (see
[08 §3.6](../build/08-page-architecture-and-section-recipes.md)). Ask which kind of set it is before you
apply the number: *does the reader have to pick one?*

---

## 5. Hierarchy is built from five channels

| Channel | Strongest use | Cost / caution |
|---|---|---|
| **Size** | Rank the three type roles: headline, subhead, body. Aim for clearly distinct steps, not 1–2px differences | More than ~4 active sizes per page reads chaotic |
| **Weight** | Separate roles inside one size (label vs value) | Bold everywhere destroys itself; on the calm end reserve heavy weight for the focal action |
| **Colour** | Mark the one live/interactive thing | The most abused channel; colour alone is never sufficient (colour-blind users, greyscale rendering) |
| **Spacing** | Group, separate, and isolate the focal element | Costs page height, which costs scroll depth |
| **Position** | Top and left of a block are read first in LTR layouts; the optical centre of a row is privileged (§10) | Position is fixed by the grid — plan it before styling |

**Ordering rule.** Design hierarchy in the order *spacing → size → weight → colour*. Colour last, because a
hierarchy that only works in colour is a hierarchy that fails in the greyscale test, on a dimmed screen, and
for a meaningful share of your visitors.

---

## 6. Testing hierarchy — four tests you can run in minutes

| Test | How to run it | Pass condition |
|---|---|---|
| **Squint test** | Blur the screenshot heavily (or squint until text is unreadable) | Exactly one element still stands out per viewport, and it is the intended one |
| **Greyscale test** | Render the page with all colour removed | The hierarchy and the primary action are still obvious; nothing important disappears |
| **Five-second test** | Show a stranger the page for five seconds, hide it, ask: what is it, who is it for, what do you do next | Answered correctly without prompting; if they recall the illustration but not the offer, imagery is hoarding attention |
| **First-click test** | Ask a stranger where they would click to accomplish the page's goal | Majority click the primary action; wrong-target clicks name your loudest neighbour |

Run the squint and greyscale tests on **every** viewport width you ship, and run the five-second test with
someone who has never seen the product. Your own eye path is contaminated by knowing the answer.

---

## 7. Scanning patterns: F, Z, and the caveat that matters more than either

**F-pattern.** In text-dense pages (articles, documentation, long feature lists) eyes tend to read the first
lines more fully, then progressively less of each subsequent line, drifting down the left edge in LTR
layouts. Application: front-load the meaning of every heading and every list item into the first two or three
words; put the point at the start of the paragraph, not the end.

**Z-pattern.** In sparse pages with few elements (a hero, a landing page, a simple pricing screen) attention
tends to sweep across the top, diagonally down, then across the bottom. Application: logo/context top-left,
supporting element top-right, proof or visual in the middle, primary action bottom-right of the block.

**The caveat.** These are *outcomes of layout*, not laws that layouts must obey. A page with a strong single
focal point and clear grouping produces neither an F nor a Z — it produces a jump to the focal element and
then a directed path. Do not design a Z into a page that has one job. Use the patterns as a default for
undifferentiated content, and override them the moment you have a real hierarchy.

**Two practical corollaries.**
- Left-edge continuity is free scanning speed in LTR layouts. Indented, centred, or staggered text columns
  break it; use centring for short blocks only (a heading, a two-line subhead), never for body copy.
- On mobile, everything becomes a single column and all these patterns collapse into vertical order. Design
  the vertical narrative first, then widen it — the reverse produces desktop pages that fall apart at 390px.

---

## 8. Directional cues: point without hoarding

**Mechanism.** Some stimuli *hold* attention on themselves (faces, bodies, animals — we are wired to attend
to agents); others *pass it along* (arrows, lines, directional language). For guiding a visitor to an action,
you want the second kind.

| Cue | Behaviour | Use it for |
|---|---|---|
| **Arrows / chevrons** | Direct attention without keeping it | The safest pointer toward a CTA or the next section |
| **Leading lines** | Composition edges, rules, a diagonal in an image guide the eye along their length | Moving the eye between two sections |
| **Directional words** ("below", "next", "on the right") | Steer attention verbally; work regardless of colour vision | Referring to a form or option — say "the form below", not "the green form" |
| **Gaze / body orientation** | Powerful pointer *and* powerful attention sink | Only when the person is the message (a founder's credibility portrait); orient their gaze toward the copy, never off-canvas |
| **Pointing hand** | Very strong grab, strong direction | High-arousal end only; reads as pushy on the calm end |

**The face problem.** A photographed human in a hero will usually out-compete the button you actually want
clicked. Faces hold attention as well as pass it along, so gaze direction is a *tie-breaker, not a rescue*:
orienting a face toward the CTA helps at the margin, and it does not repay the attention the face itself
takes. Fix it in this order — (1) remove the person, (2) shrink and desaturate them, (3) keep them and place
the action inside their visual gravity with the gaze pointing at it. Reach for step 3 only when the person
*is* part of the message (a named founder, a real practitioner). Never treat a redirected gaze as licence to
put a large stock face beside your primary action.

**Colour-only cues are a bug.** Any instruction that depends on colour ("click the blue button") fails for
colour-blind users, in greyscale, and on badly calibrated screens. Pair colour with position words, icons, or
labels every time.

> **Dial.** Calm end: one static arrow or a directional word is plenty. Energetic end: animated arrows,
> bouncing chevrons, and pointing hands are on-brand — as long as what they point at is honest.

---

## 9. Whitespace: premium signal, grouping tool, and one dangerous void

**Two jobs.** Empty space signals confidence and value (crowding reads as cheap or discount), and it does the
grouping work described in §4 without adding any ink.

**How to apply.**
- Space is a system, not a per-element decision. Use one spacing scale everywhere (see
  [09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md)) so rhythm is consistent down the page.
- Prefer fewer, airier items to more, tighter ones — three roomy options usually beat four cramped ones on
  both comprehension and perceived quality.
- The space *around* the focal element is a salience channel. Increase it before you increase saturation.
- "Airy" is not the same as "empty but cluttered". Cut decoration that carries no meaning, collapse secondary
  detail into disclosures, and delete self-evident instructions. Space earned by removing noise is premium;
  space created by spreading noise apart is just a longer page.

**The one place a void hurts.** Directly under a persuasive claim, a large empty gap reads as "that's all we
had" — the claim feels smaller and less supported. Bound persuasive blocks (trust proofs, pricing, guarantee)
with a close edge, a visible next element, or the start of the following section. Keep the generous space
around *navigational* and *editorial* content, not immediately beneath your strongest claim.

---

## 10. Centre stage in row layouts

**What it is.** In a horizontal row of comparable options, the middle position carries an unearned advantage:
it draws more looks and more choices, and people rationalise the preference afterwards.

**How to apply.**
- Put the option you want chosen in the middle of a three-across row, and reinforce with isolation: slightly
  larger card, one step more elevation, the single accent, a label.
- Only one card in a row may carry the accent. Two "recommended" badges cancel out and cost credibility.
- Row order can carry meaning on its own — a gradient of price, capability, or tone from left to right reads
  as an intentional sequence and feels "right" for reasons the visitor cannot name.
- Watch the mobile stack: centre stage evaporates when three cards become a vertical list. Explicitly reorder
  so the intended option is **first** in the stacked order, and keep its visual distinction.

**Where the line is.** Centre-staging a genuinely well-matched option is design. Centre-staging an option
that is worse for most buyers, or manufacturing a "most popular" label that is not true, is manipulation.
Popularity labels must reflect actual data. See [07-pricing-psychology.md](07-pricing-psychology.md).

---

## 11. Instant liking: complexity, symmetry, prototypicality

**Mechanism — processing fluency.** Anything easy to process is liked more, judged more truthful, and
misattributed as higher quality. The ease is felt but its source is not, so visitors credit the *brand* for
the smoothness of their own perception. This is the quiet engine behind most "it just looks trustworthy"
reactions.

| Driver | What raises fluency | How to apply |
|---|---|---|
| **Low visual complexity** | Fewer distinct elements, colours, alignments, and type steps | Count them: aim for one accent, one neutral ramp, ≤3 type sizes and ≤2 weights per viewport, one grid |
| **Symmetry / balance** | Even visual weight around a clear axis | Balanced two-column heroes and consistent card grids read calmer; deliberate asymmetry is an energy lever, not a default |
| **Prototypicality** | Matching the category's expected layout | Navigation top, logo top-left linking home, cart/account top-right, contact in the footer, pricing that shows prices immediately |

**The prototypicality trade-off.** Familiar layouts are processed faster and liked faster; novel layouts get
noticed but pay a comprehension tax. The reliable resolution: **be prototypical in structure, distinctive in
content and craft.** Put the surprise in the words, the imagery, and the detail quality — not in where the
navigation lives.

**Expectation matching.** Whatever the page's name promises must be visible on arrival without scrolling. A
"Pricing" page shows prices in the first viewport. A "Contact" page shows a way to make contact. Violating
this costs more than any layout refinement can recover.

> **Dial.** Calm end: maximise fluency everywhere; restraint is the product signal. Energetic end: a
> deliberate disfluency (an unexpected shape, an off-grid element) can buy attention — spend it once, and
> never on the step where the visitor must understand or decide something.

---

## 12. Images and icons

**Icons — a reusable spec.**
- Outline style, **one uniform stroke width**, rounded caps and joins, drawn on one shared grid (24px is a
  common choice), each icon expressing **a single concept**.
- Draw in `currentColor` so state and theme changes are one CSS property.
- Default colour is a muted, brand-tinted neutral. The **only** icons carrying saturation are the active or
  selected ones.
- No emoji as UI icons, no mixed styles, no multicolour illustrations sitting next to line icons.
- Prefer simple geometric symbols to detailed artwork in feature rows. A simplified symbol carries fewer
  competing details, which tends to make it quicker to identify and much quieter next to the text it labels;
  an illustrated scene competes with the copy it was meant to support. (Directional craft guidance, not a
  measured finding — if an icon set genuinely aids comprehension, keep it.)

**Photography and figures.**
- **Imply people rather than depicting them.** Traces of human presence — a hand at the edge of frame, a
  used workspace, an object mid-use — let the viewer project themselves into the scene. A full stock figure
  creates distance ("that is their customer, not me") and steals attention (§8).
- The one sanctioned exception is a real person with real standing: a founder, a named practitioner, an
  actual customer with permission. Real provenance is worth the attention cost; a stock model is not.
- Keep the subject sharp and backgrounds soft or blurred (figure/ground, §4). Avoid busy high-contrast
  imagery anywhere near a decision point.
- Never present a stock image, a mock interface, or an illustration in a way that implies it is a real
  screenshot, a real customer, or a real result. See the honesty rails in
  [10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md).

**Shape carries meaning.** Round masks, soft corners, and circular crops read emotional, friendly, human,
wellness-adjacent. Crisp rectangular edges and tight radii read rational, technical, precise, competent.
Choose per brand — then apply it *systemically* to cards, chips, buttons, inputs, and image masks together.
A round avatar next to a hard-edged card is a mixed signal, and mixed signals cost fluency.

---

## 13. Motion: what it communicates before it communicates anything

**Mechanism.** Motion onset (still → moving) captures attention almost involuntarily; looming motion (growing
larger) reads as urgency; irregular or lifelike motion reads as an agent. These are potent and, on the calm
end, mostly liabilities. Speed and easing are also read as personality: slow eased motion says care and
value; fast, bouncy, or repeating motion says energy and urgency.

| Motion type | Reads as | Calm end | Energetic end |
|---|---|---|---|
| Slow eased fade / rise (≈300–500ms, ease-out) | Care, quality, deliberateness | Default for reveals and state changes | Fine, but often too slow |
| Micro-transition (≈120–200ms) | Responsiveness | Use for hover, focus, toggles | Same |
| Looming / zoom-in | Urgency, approach | Avoid | Attention-grab for offers |
| Pulsing / shimmer loops | "Act now" | Avoid — it undermines the trust read | Legitimate on a cluttered page |
| Parallax / scroll-jacking | Spectacle | Avoid; it breaks scroll expectations | Use sparingly, never over a form |
| Autoplaying carousel | Movement for its own sake | Avoid — it steals attention and hides content | Only with visible controls |

**Rules that hold at both ends.**
- Animate **one** thing per viewport. Competing animations produce no focal point at all.
- Motion must serve orientation: reveal, confirm, or explain a change of state. Motion that only decorates is
  attention spent for nothing.
- Never animate something the user is trying to read or click. Content that moves under the cursor is a
  usability defect regardless of brand.
- Honour `prefers-reduced-motion`: disable transforms and reveals, keep opacity changes minimal, and ensure
  no content is *only* revealed by an animation. A page that is blank without JavaScript animation is broken
  for a real group of users and for crawlers.
- Loading states: prefer calm skeletons over impatient spinners, and start progress indicators a few percent
  above zero — a bar pinned at 0% reads as stalled. **The bar must still track something real.** Nudging the
  first paint off zero is presentation; a bar that advances on a timer while nothing is happening is
  fabricated progress, and it belongs with the fake countdowns in
  [04 §4](04-persuasion-core.md#4-ethics-where-structuring-ends-and-deception-begins).

---

## 14. Interactive affordances and target size

Attention is wasted if the visitor cannot tell what is clickable.

- Anything interactive must announce itself in **at least two** channels: colour plus underline, or shape
  plus elevation, or icon plus label. Colour alone fails colour-blind users.
- Distinct states for **hover, focus, active, selected, and disabled**. A "selected" state that is only a
  slightly different shade is not a state.
- Change the cursor on hover for every clickable element, including cards and rows that act as links.
- Minimum tap target: **44×44 CSS pixels** of touchable area (a smaller visual element can carry a larger hit
  area via padding). Adjacent targets need clear separation; stacked links spaced only by line-height cause
  misclicks and rage-taps.
- Confirm every interaction visibly. Silence after a click reads as failure and produces double submissions.
- Powerful or destructive actions must look categorically different from ordinary ones — different colour
  family, different placement, extra confirmation. Do not make a destructive control the most beautiful
  button on the page.

---

## 15. Accessibility is a persuasion feature

Treat this as conversion work, not compliance paperwork. Every accessibility rule below is also a fluency
rule, and fluency is trust.

| Requirement | Target | Why it also persuades |
|---|---|---|
| Body text contrast | ≥ 4.5:1 against its background | Legible text is judged more truthful; low-contrast "elegant" grey text costs comprehension for everyone |
| Large text (≈24px+, or 19px+ bold) | ≥ 3:1 | Headlines are your hierarchy; a headline that fades is a hierarchy that fails |
| Interactive element boundaries & icons | ≥ 3:1 | If the button edge is invisible, the affordance is invisible |
| Focus indicator | Always visible, never `outline: none` without a replacement | Keyboard users can complete the form; the indicator also doubles as a hover cue |
| Information never colour-only | Always pair with text, icon, or position | Works in greyscale, for colour-blind users, and on cheap screens |
| Semantic headings, alt text, labels | One `h1`, ordered levels, real `<label>` elements | Screen readers, search engines, and AI answer engines all consume the same structure — see [13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) |
| Reduced motion | Respected | Prevents nausea and disorientation for a real portion of visitors |
| Text remains readable when zoomed to 200% | No content loss, no horizontal scroll | Also catches fragile layouts before real users do |

Check contrast on the **rendered** page, including text over images and over gradients, at the actual
opacity shipped — not on the palette swatches.

---

## 16. Common failure modes

| Symptom | Usual cause | Fix |
|---|---|---|
| "The page looks fine but nobody clicks" | No single focal point; competing solid buttons | §2, then the demotion ladder §3 |
| "It feels cluttered" but nothing is obviously wrong | Inconsistent spacing scale; grouping contradicts logic | §4 proximity ratio; one spacing scale |
| Visitors misread what the product is | Prototypicality violated or expectation mismatch on arrival | §11 |
| Hierarchy collapses in a screenshot | Hierarchy carried by colour only | §5 ordering rule; greyscale test |
| Mobile converts far worse than desktop | Focal point multiplied when columns stacked; centre stage lost | §2, §10 |
| Illustration is remembered, offer is not | Imagery out-competing the message | §8, §12 |
| Trust section reads weak | Void directly under the claim | §9 |
| Page feels "off" and nobody can say why | Mixed shape language or mixed motion speeds | §12, §13 |

---

## Apply it

- [ ] The arousal dial is chosen and written down; every tactic on the page matches that end.
- [ ] For each viewport, the intended eye path is named in three steps before design begins.
- [ ] Exactly one focal element per viewport; one solid primary action, at most one quiet secondary.
- [ ] Salience audited **locally** — the focal element wins against its own section, not just the palette.
- [ ] Proximity checked on every heading — space above ≈2× the space below, up to 3× at a section break.
- [ ] No *comparative* group larger than four items; larger sets chunked into labelled clusters. Scannable
      (non-choosing) grids may run to six.
- [ ] Hierarchy built in the order spacing → size → weight → colour, and it survives the greyscale test.
- [ ] Squint test and five-second test passed at every shipped viewport width, including 390px.
- [ ] Direction is carried by arrows, lines, or directional words — never by a face competing with the CTA.
- [ ] No instruction depends on colour alone.
- [ ] Persuasive claims are bounded (no dead void directly beneath them); navigational areas stay airy.
- [ ] Icons are one style, one stroke, one grid, one concept each; saturation only on active states.
- [ ] One animation per viewport, `prefers-reduced-motion` honoured, no content revealed only by motion.
- [ ] Contrast ≥4.5:1 body / ≥3:1 large text and UI edges; visible focus states; tap targets ≥44×44px.
- [ ] Nothing on the page implies a real result, real customer, or real popularity that isn't true.

---

## Related

- [04-persuasion-core.md](04-persuasion-core.md) — the persuasion principles this layout is arranging
- [06-color-and-typography.md](06-color-and-typography.md) — the materials: hue, saturation, weight, casing
- [07-pricing-psychology.md](07-pricing-psychology.md) — centre stage, anchoring and tier layout in depth
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — headlines that carry the takeaway for skimmers
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — these rules assembled into section patterns
- [../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md) — spacing scale, type scale, radius and motion tokens
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the pre-ship gate, including the honesty rails
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — semantic structure that serves both readers and machines
- [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md) — how to test a layout change without fooling yourself
