# Drop-in agent skills

Two skills that make an AI coding agent actually *use* this pack instead of improvising.

## Install (Claude Code / Codex on the new machine)

```bash
mkdir -p ~/.claude/skills
cp skills/brand-web-design.skill.md   ~/.claude/skills/brand-web-design.md
cp skills/growth-search.skill.md      ~/.claude/skills/growth-search.md
```

Or keep them project-local at `<your-project>/.claude/skills/`.

Both skills assume this pack is cloned somewhere the agent can read it. Set the path once:

```bash
export GROWTH_FUNDAMENTALS=~/Projects/growth-fundamentals
```

…and tell the agent that variable in your project's `CLAUDE.md` / `AGENTS.md`, e.g.:

> The brand + growth fundamentals pack lives at `~/Projects/growth-fundamentals`.
> Read `00-START-HERE.md` before any design, copy, or search work.

## What each one does

| Skill | Triggers on | What it enforces |
|---|---|---|
| `brand-web-design` | designing/critiquing a site, landing page, hero, pricing section, CTA, colour, type | Decide the arousal target first, then apply the layout/colour/type/copy rules and pass the conversion audit before claiming done |
| `growth-search` | SEO, GEO, "rank for", schema, llms.txt, sitemap, indexing, AI citations | Detect the stack, one keyword per URL, capture-the-keyword/reframe-the-category, the GEO layer, one connected schema graph, then verify |
