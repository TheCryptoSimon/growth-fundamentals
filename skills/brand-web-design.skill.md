---
name: brand-web-design
description: "Design or critique a brand's marketing website / landing page using behavioural-design fundamentals — set the arousal target first, then apply the layout, colour, type, copy and pricing rules, and pass the conversion audit before claiming done."
user-invocable: true
triggers:
  - "design the site"
  - "landing page"
  - "design critique"
  - "make the site convert"
  - "hero section"
  - "pricing page"
  - "CTA design"
  - "brand website"
  - "colour palette"
  - "typography"
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
---

# Brand web design

Apply the fundamentals in the **growth-fundamentals** pack to build or critique a marketing site that
converts without hype. The pack is the knowledge base; this skill is the procedure.

## Knowledge base

Set `$GF` to the pack root (default: `~/Projects/growth-fundamentals`). Read in this order — only what the
task needs:

1. `$GF/00-START-HERE.md` — the five decisions, the three engines, the order of operations. **Always.**
2. `$GF/psychology/05-visual-attention-and-layout.md` · `06-color-and-typography.md`
3. `$GF/build/08-page-architecture-and-section-recipes.md` — the section recipes
4. `$GF/brand/03-voice-messaging-and-copywriting.md` — concreteness, mechanism, microcopy
5. `$GF/psychology/07-pricing-psychology.md` — for any pricing surface
6. `$GF/build/09-design-system-and-tokens.md` — before writing any CSS
7. `$GF/build/10-conversion-audit-checklist.md` — the gate. **Always, before "done".**
8. `$GF/psychology/04-persuasion-core.md` — when you need to pick a lever or check the ethics line

## Procedure

1. **Read the brand brief** (`templates/brand-brief.md` filled in for this project). If it does not exist,
   stop and produce one first — designing without it is guessing.
2. **State the arousal target out loud** (calm/premium/trust vs energetic/urgent/playful). Write it into
   the brief. It inverts roughly half the tactics; every later decision cites it.
3. **Tokens before pixels.** Establish colour ramp, type scale, spacing, radius, motion as tokens in one
   file. No component hard-codes a value.
4. **Lay out by hierarchy, not by taste.** One focal point per viewport; the single primary CTA wins by
   contrast and isolation; everything else is demoted deliberately.
5. **Write copy to the rules, not to the vibe.** Concrete over abstract, second person, one promise,
   mechanism on every trust line, no superlatives, no manufactured urgency.
6. **Assemble the page from the section recipes**, in the order the recipe doc gives for your arousal
   target.
7. **Run the conversion audit** in `build/10`. Screenshot mobile (375px) first, then desktop. Grade every
   section. Fix, re-screenshot, repeat until a harsh reviewer finds nothing material.
8. **Document the decision** — what changed and which rule drove it — in the project's own docs.

## Safety rails

No fake urgency (countdown timers on evergreen offers, "only N left" that is not true), no invented
metrics, ratings or testimonials, no superlatives you cannot prove. Honest scarcity only (real capacity,
real cohorts, real deadlines). Legally required disclaimers go in the footer or FAQ, not woven into the
persuasive body. For a calm brand, deliberately down-tune the high-arousal levers — their absence is a
choice, not a defect.

## Definition of done

One clear focal point per screen · the single CTA wins by isolation · copy is concrete and second-person ·
every checklist section in `build/10` passes or is marked as a deliberate exception with a reason · AA
contrast holds · no horizontal scroll at 375px · reduced-motion honoured · the conversion event fires.

## Apply it

- [ ] `$GF` points at a readable copy of the pack, and `00-START-HERE.md` has been read in full.
- [ ] A filled-in brand brief exists for this project; nothing was designed before it did.
- [ ] The arousal target is stated out loud, written into the brief, and cited on every dependent choice.
- [ ] Tokens exist in one file before any component; nothing hard-codes a colour, size, or duration.
- [ ] One focal point per viewport and one primary CTA, winning by contrast and isolation.
- [ ] Copy is concrete, second person, one promise, mechanism on every trust line, no manufactured urgency.
- [ ] Sections follow the recipes for the chosen arousal target, not the order they came to mind.
- [ ] The conversion audit ran at 375px and desktop, with screenshots, and every failure was fixed or recorded.
- [ ] Nothing on the safety-rail list appears anywhere on the page.
- [ ] The decisions and the rules behind them are documented in the project's own docs.

## Related

- [README.md](README.md) — installing this skill and its sibling
- [../00-START-HERE.md](../00-START-HERE.md) — the five decisions and the arousal dial this skill assumes
- [../psychology/04-persuasion-core.md](../psychology/04-persuasion-core.md) — the levers and their ethics line
- [../psychology/05-visual-attention-and-layout.md](../psychology/05-visual-attention-and-layout.md) — focal points and layout
- [../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md) — palette and type decisions
- [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md) — any pricing surface
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — the copy rules
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — the section recipes
- [../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md) — tokens before pixels
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the gate before "done"
- [growth-search.skill.md](growth-search.skill.md) — the search and AI-visibility counterpart
