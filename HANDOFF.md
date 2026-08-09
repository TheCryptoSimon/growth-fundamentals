# Handoff — paste this to the agent on the new machine

Copy everything below the line into the first message of a fresh session on the machine that is building
the new brand.

---

We are building a **brand-new product with a brand-new brand**. It is unrelated to anything I have built
before — do not carry over any existing brand's positioning, palette, voice, or page structure. You are
starting from first principles.

**Step 1 — get the knowledge pack.**

```bash
gh repo clone TheCryptoSimon/growth-fundamentals ~/Projects/growth-fundamentals
```

**Step 2 — install the two agent skills.**

```bash
mkdir -p ~/.claude/skills
cp ~/Projects/growth-fundamentals/skills/brand-web-design.skill.md ~/.claude/skills/brand-web-design.md
cp ~/Projects/growth-fundamentals/skills/growth-search.skill.md    ~/.claude/skills/growth-search.md
```

Then add this line to the new project's `CLAUDE.md` (create it if missing):

> The brand + growth fundamentals pack lives at `~/Projects/growth-fundamentals`. Read `00-START-HERE.md`
> before any brand, design, copy, or search work. It is READ-ONLY reference — never edit it from this
> project.

**Step 3 — read before doing anything.** In this order: `README.md`, then `00-START-HERE.md`. Do not skim.
`00-START-HERE.md` defines the five decisions that must be locked before a single pixel or page exists, and
the arousal dial that inverts roughly half of the tactics in the rest of the pack.

**Step 4 — interview me, then write the brand brief.** Use the brand-discovery and positioning prompts in
`ops/16-prompt-pack.md`. Ask me the questions; do not invent answers. Output a filled-in copy of
`templates/brand-brief.md` **into the new project repo** (not into the pack) at `docs/BRAND-BRIEF.md`. That
file becomes the single source of truth for everything after it. Nothing else gets built until it exists
and I have approved it.

**Step 5 — build in this order**, using the pack doc named at each step:

1. Positioning + category — `brand/01-positioning-and-category.md`
2. Name, personality, archetype, canonical entity paragraph — `brand/02-identity-archetype-and-naming.md`
3. Voice, message hierarchy, banned words — `brand/03-voice-messaging-and-copywriting.md`
4. Design tokens (colour ramp, type scale, spacing, motion) — `build/09-design-system-and-tokens.md` +
   `psychology/06-color-and-typography.md`
5. Page architecture and section-by-section build — `build/08-page-architecture-and-section-recipes.md` +
   `psychology/05-visual-attention-and-layout.md`
6. Pricing surface — `psychology/07-pricing-psychology.md`
7. Search layer: keyword map, on-page, schema, llms.txt, robots, indexing —
   `search/11-seo-fundamentals.md`, `search/12-geo-ai-search.md`, `search/13-schema-and-technical-wiring.md`
8. Measurement — `ops/14-measurement-and-experimentation.md`
9. Launch gates — `ops/15-launch-checklist-and-build-order.md`

**Non-negotiables.**

- State the arousal target (calm/premium/trust vs energetic/urgent) out loud before any design decision, and
  cite it when a choice depends on it.
- Tokens before pixels. No component hard-codes a colour, size, or duration.
- One focal point per viewport; one primary CTA; it wins by contrast and isolation.
- One primary keyword per URL. Capture the keyword in title/meta/H1/schema; hold the brand frame in the body.
- Honesty rails: no invented metrics, ratings, testimonials, or countdown timers on evergreen offers. No
  superlative you cannot prove. If a tactic only works because a fact is false, it is out.
- Nothing is "done" until it passes `build/10-conversion-audit-checklist.md` at 375px **and** desktop, with
  screenshots. Grade, fix, re-screenshot, repeat until a harsh reviewer finds nothing material.

**How to report.** Short. What you built, which rule drove each non-obvious choice, what failed the audit and
what you did about it. Decisions, not questions — bring me a recommendation when you need my call.
