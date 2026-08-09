# Design System and Tokens

The layer that turns brand decisions into values a machine can build against. Stack-agnostic: everything here
works in plain CSS, and any framework can read it. Read this after the colour and type decisions are made and
before the first component is written — a system retrofitted onto built components costs three times as much.

---

## 0. Why tokens come before components

A token is a named value with one definition and many consumers. Build them first for four reasons:

| Reason | What it prevents |
|---|---|
| **One source of truth** | The same "brand blue" existing as four slightly different hexes across six files |
| **Rebrandability** | A colour change becoming a two-week find-and-replace across every component |
| **Theming** | Dark mode being a parallel stylesheet instead of one swapped block of aliases |
| **Machine-buildability** | An agent guessing values because none were named, then guessing differently next session |

**The rule that makes all four work:** a component never contains a raw value — not a hex, not a pixel, not a
duration, not a font stack. It references a semantic token. A component needing a value that has no token is a
prompt to add a token, not to inline one.

**Sequencing.** Brand brief → colour + type decisions ([../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md))
→ tokens (this doc) → components → pages ([08-page-architecture-and-section-recipes.md](08-page-architecture-and-section-recipes.md)).
Skipping to pages produces a site that looks finished and cannot be changed.

---

## 1. The token taxonomy

Ten groups. If a value on your site belongs to none of these, ask why it exists.

| Group | Contains | Typical count |
|---|---|---|
| **Colour — brand ramp** | Tints and shades of the primary, numbered | 5–9 steps |
| **Colour — neutral ramp** | Near-white → near-black, each tinted toward the brand hue | 10–12 steps |
| **Colour — functional** | success / warning / danger / info, each with a surface and a text variant | 4 × 3 |
| **Colour — semantic aliases** | `surface-*`, `text-*`, `border-*`, `action-*` — what components actually consume | 15–25 |
| **Typography** | Families, size scale, line-height paired to each size, weights, tracking | 1 base + 7 steps |
| **Spacing** | One base unit and a ramp derived from it | 12–14 steps |
| **Radius, border, elevation** | A radius ramp plus `full`; two border widths; shadow layers, plus the border that substitutes for shadow on dark | 6 / 2 / 4 |
| **Motion** | Durations and easing curves | 4 + 4 |
| **Breakpoints** | Named viewport thresholds | 4–5 |
| **Z-index** | A named stacking ladder | 8–10 |

**Do not tokenise:** one-off page layouts, content widths that appear once, or anything you cannot name
without describing where it sits ("the-gap-under-the-hero-button" is a bug, not a token).

---

## 2. Naming that survives a redesign

Three layers. Each layer may only reference the layer above it.

```
LAYER 1  PRIMITIVES  --brand-600, --neutral-50, --space-4, --text-lg
                     Describe the VALUE. No opinion about use. Renamed almost never.
LAYER 2  SEMANTIC    --surface-page, --text-secondary, --action-primary-bg
                     Describe the ROLE. Points at a primitive. THE THEMING LAYER.
LAYER 3  COMPONENT   --button-primary-bg: var(--action-primary-bg)
                     Optional. Only when a component must deviate for a real reason.
```

**Naming rules:**

- Primitives are named after **what they are** (`--brand-600`, `--space-6`); semantics after **what they do**
  (`--text-muted`, `--border-strong`, `--surface-raised`).
- Never name a token after where it currently appears (`--hero-bg`) or after its literal colour
  (`--blue-button`). Both break the first time the design changes.
- Numeric ramps run low → light, high → dark, at a constant interval (50, 100, 200 … 900) so an agent can
  interpolate. Use one delimiter and one case, mirrored exactly in any JS/Tailwind/JSON export.
- **Components consume Layer 2 only.** A component reaching into `--brand-600` directly is the exact failure
  the taxonomy exists to prevent: it can be neither themed nor rebranded.

**The deviation test.** Before creating a Layer 3 token, ask whether this is a real, defensible difference or
a designer working around a missing semantic. Nine times in ten it is the latter — add the semantic instead.

---

## 3. Starter token file

Copy this whole block into `tokens.css`, tune the values marked **TUNE**, and never write a raw value
anywhere else. Every value below is a placeholder chosen to be visibly neutral, not to be shipped as-is.

```css
/* ============================================================
   tokens.css — the ONLY file where raw values are allowed.
   Tune the marked lines; everything else derives.
   ============================================================ */

:root {
  /* ---- TUNE: brand hue + chroma. Two numbers rebrand the site. ---- */
  --brand-h: 220;            /* TUNE  hue 0–360                      */
  --brand-s: 32%;            /* TUNE  calm 18–40% · energetic 60–90%  */
  --neutral-tint: 6%;        /* TUNE  saturation carried by greys 3–8%*/

  /* ---- LAYER 1: colour primitives. Only lightness varies down each ramp. ---- */
  --brand-50:  hsl(var(--brand-h) var(--brand-s) 97%);  --brand-100: hsl(var(--brand-h) var(--brand-s) 92%);
  --brand-200: hsl(var(--brand-h) var(--brand-s) 84%);  --brand-300: hsl(var(--brand-h) var(--brand-s) 72%);
  --brand-400: hsl(var(--brand-h) var(--brand-s) 58%);  --brand-500: hsl(var(--brand-h) var(--brand-s) 46%);
  --brand-600: hsl(var(--brand-h) var(--brand-s) 38%);  /* ← the true brand colour */
  --brand-700: hsl(var(--brand-h) var(--brand-s) 30%);  --brand-800: hsl(var(--brand-h) var(--brand-s) 22%);
  --brand-900: hsl(var(--brand-h) var(--brand-s) 15%);

  /* neutrals carry a trace of the brand hue — pure greys look accidental */
  --neutral-0:   hsl(var(--brand-h) var(--neutral-tint) 100%);  --neutral-25:  hsl(var(--brand-h) var(--neutral-tint) 98.5%);
  --neutral-50:  hsl(var(--brand-h) var(--neutral-tint) 96%);   --neutral-100: hsl(var(--brand-h) var(--neutral-tint) 92%);
  --neutral-200: hsl(var(--brand-h) var(--neutral-tint) 85%);   --neutral-300: hsl(var(--brand-h) var(--neutral-tint) 72%);
  --neutral-400: hsl(var(--brand-h) var(--neutral-tint) 58%);   --neutral-500: hsl(var(--brand-h) var(--neutral-tint) 46%);
  --neutral-600: hsl(var(--brand-h) var(--neutral-tint) 37%);   --neutral-700: hsl(var(--brand-h) var(--neutral-tint) 28%);
  --neutral-800: hsl(var(--brand-h) var(--neutral-tint) 19%);   --neutral-900: hsl(var(--brand-h) var(--neutral-tint) 12%); /* never #000 */

  --success-500: hsl(150 38% 34%);  --success-50: hsl(150 38% 95%);
  --warning-500: hsl(38  62% 42%);  --warning-50: hsl(38  62% 95%);
  --danger-500:  hsl(4   58% 44%);  --danger-50:  hsl(4   58% 96%);
  --info-500:    hsl(210 40% 40%);  --info-50:    hsl(210 40% 96%);

  /* ---- LAYER 1: type. Line-height is bound to its size step, never inherited. ---- */
  --font-sans:  ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-serif: ui-serif, Georgia, "Times New Roman", serif;
  --font-mono:  ui-monospace, SFMono-Regular, Menlo, monospace;

  --text-xs: 0.8125rem;  --lh-xs: 1.7;    --text-sm: 0.9375rem;  --lh-sm: 1.65;   /* 13 · 15 */
  --text-md: 1.0625rem;  --lh-md: 1.65;   --text-lg: 1.3125rem;  --lh-lg: 1.5;    /* 17 body · 21 */
  --text-xl: 1.625rem;   --lh-xl: 1.35;   --text-2xl: 2rem;      --lh-2xl: 1.25;  /* 26 · 32 */
  --text-3xl: clamp(2.2rem, 1.5rem + 2.2vw, 3rem);   --lh-3xl: 1.15;
  --text-4xl: clamp(2.6rem, 1.6rem + 3.4vw, 3.9rem); --lh-4xl: 1.08;

  --weight-regular: 400;  --weight-medium: 500;  --weight-semibold: 600;  --weight-bold: 700;
  --tracking-tight: -0.015em;  --tracking-normal: 0;  --tracking-wide: 0.06em;
  --measure: 65ch;                                   /* prose max-width */

  /* ---- LAYER 1: space, radius, elevation, border ---- */
  --space-unit: 0.25rem;                             /* 4px base */
  --space-1: var(--space-unit);             --space-2:  calc(var(--space-unit) * 2);
  --space-3: calc(var(--space-unit) * 3);   --space-4:  calc(var(--space-unit) * 4);
  --space-5: calc(var(--space-unit) * 5);   --space-6:  calc(var(--space-unit) * 6);
  --space-8: calc(var(--space-unit) * 8);   --space-10: calc(var(--space-unit) * 10);
  --space-12: calc(var(--space-unit) * 12); --space-16: calc(var(--space-unit) * 16);
  --space-20: calc(var(--space-unit) * 20); --space-24: calc(var(--space-unit) * 24);
  --space-32: calc(var(--space-unit) * 32);   /* section gaps live at this end */

  --radius-xs: 2px;   --radius-sm: 4px;   --radius-md: 8px;
  --radius-lg: 14px;  --radius-xl: 22px;  --radius-full: 9999px;
  --border-thin: 1px; --border-thick: 2px;

  --shadow-sm: 0 1px 2px hsl(var(--brand-h) 20% 10% / 0.06);
  --shadow-md: 0 2px 6px hsl(var(--brand-h) 20% 10% / 0.08),
               0 8px 20px hsl(var(--brand-h) 20% 10% / 0.06);
  --shadow-lg: 0 12px 40px hsl(var(--brand-h) 20% 10% / 0.12);

  /* ---- LAYER 1: motion + stacking ladder (gaps of 100 leave room to insert) ---- */
  --duration-fast: 120ms;  --duration-base: 200ms;  --duration-slow: 320ms;  --duration-slower: 520ms;
  --ease-standard: cubic-bezier(0.2, 0, 0, 1);  --ease-enter: cubic-bezier(0, 0, 0, 1);
  --ease-exit: cubic-bezier(0.4, 0, 1, 1);

  --z-base: 0;        --z-raised: 10;    --z-sticky: 100;  --z-header: 200;
  --z-dropdown: 300;  --z-overlay: 400;  --z-modal: 500;   --z-toast: 600;  --z-tooltip: 700;

  /* ========= LAYER 2: semantic aliases — the ONLY layer components read ========= */
  --surface-page: var(--neutral-25);      --surface-raised: var(--neutral-0);
  --surface-sunken: var(--neutral-50);    --surface-inverse: var(--neutral-900);
  --surface-accent-soft: var(--brand-50);
  --text-primary: var(--neutral-900);     --text-secondary: var(--neutral-600);
  --text-muted: var(--neutral-500);       --text-inverse: var(--neutral-0);
  --text-link: var(--brand-700);
  --border-subtle: var(--neutral-200);    --border-strong: var(--neutral-300);
  --border-focus: var(--brand-600);
  --action-primary-bg: var(--brand-600);        --action-primary-bg-hover: var(--brand-700);
  --action-primary-text: var(--neutral-0);      --action-secondary-border: var(--neutral-300);
  --action-disabled-bg: var(--neutral-100);     --action-disabled-text: var(--neutral-400);
  --focus-ring: 0 0 0 2px var(--surface-page), 0 0 0 4px var(--border-focus);
}

/* ---- Dark theme: ONLY Layer 2 is reassigned. Primitives never move. ---- */
:root[data-theme="dark"] {
  --surface-page: var(--neutral-900);     --surface-raised: var(--neutral-800);
  --surface-sunken: hsl(var(--brand-h) var(--neutral-tint) 9%);
  --surface-inverse: var(--neutral-50);   --surface-accent-soft: hsl(var(--brand-h) var(--brand-s) 20%);
  --text-primary: var(--neutral-50);      --text-secondary: var(--neutral-300);
  --text-muted: var(--neutral-400);       --text-inverse: var(--neutral-900);
  --text-link: var(--brand-300);
  --border-subtle: var(--neutral-700);    --border-strong: var(--neutral-600);
  --border-focus: var(--brand-300);
  /* the accent lightens + desaturates for dark, or it vibrates on near-black */
  --action-primary-bg: var(--brand-400);        --action-primary-bg-hover: var(--brand-300);
  --action-primary-text: var(--neutral-900);
  --action-disabled-bg: var(--neutral-800);     --action-disabled-text: var(--neutral-600);
  --shadow-sm: 0 1px 2px hsl(0 0% 0% / 0.4);    --shadow-md: 0 2px 8px hsl(0 0% 0% / 0.45);
  --shadow-lg: 0 14px 44px hsl(0 0% 0% / 0.55);
}

@media (prefers-reduced-motion: reduce) {
  :root { --duration-fast: 1ms; --duration-base: 1ms;
          --duration-slow: 1ms; --duration-slower: 1ms; }
}
```

**What you tune on day one:** `--brand-h`, `--brand-s`, `--neutral-tint`, the font stacks, the type base.
Everything else derives. If changing the brand takes twenty edits, the ramp was built wrong.

---

## 4. Light and dark from one set

**The mechanism:** primitives are absolute facts about colour; semantics are opinions about roles. Themes swap
opinions, never facts. A dark theme that redefines `--brand-600` has merged the two layers and will drift.

| Rule | Why |
|---|---|
| Reassign Layer 2 only, inside one selector block | The whole theme is auditable in one screen of code |
| Support both `prefers-color-scheme` and an explicit `data-theme` attribute, with the attribute winning | Respect the OS by default, honour an explicit user choice always |
| Lower the accent's saturation and raise its lightness for dark | A saturated fill that reads correct on white vibrates on near-black |
| Replace shadow with border on dark surfaces | Shadows are nearly invisible against dark; elevation must be carried by a lighter surface step or a 1px border |
| Re-run every contrast check in **both** themes | Passing in light says nothing about dark |
| Set `color-scheme: light dark` on the root | Native controls, scrollbars and form widgets follow the theme |

**Do you need dark mode at all?** A marketing site optimising for sign-ups usually does not — light suits
conversion, dark suits long-session engagement. Decide before you build tokens: a second theme added later is
cheap only if the semantic layer already exists.

---

## 5. Spacing, radius and elevation as one rhythm

**Spacing.** One base unit — 4px is the near-universal choice, 8px for a deliberately loose design. Every
margin, padding and gap is a multiple from the ramp. The payoff is not tidiness: inconsistent rhythm is the
commonest cause of a site "feeling cluttered" when nothing is individually wrong.

- Inside a component `--space-2`→`--space-6` · between components `--space-8`→`--space-12` · between page
  sections `--space-20`→`--space-32`.
- **Proximity discipline:** the gap *between* groups must be visibly larger than the gap *inside* one — aim
  for roughly double ([../psychology/05-visual-attention-and-layout.md](../psychology/05-visual-attention-and-layout.md)).

**Radius.** One radius language across buttons, inputs, cards and images; mixed radii read as unfinished. Nest
correctly — an inner radius is the outer radius minus the padding, or the corners look wrong.

**Elevation.** Shadows are a hierarchy tool, not decoration. Three levels are enough (resting card, floating
element, modal). More than three and none of them means anything.

> **Dial.** Calm/premium: larger spacing steps, soft radii (8–14px), shallow diffuse shadows.
> Energetic/playful: tighter spacing, a committed radius pole (near-0 or heavily rounded, never the middle),
> deeper and more contrasted shadows.

---

## 6. Motion, breakpoints and stacking

Motion is tokenised for the same reason colour is: "how fast does this site feel" becomes one decision instead
of forty. Four durations and three curves cover a marketing site.

| Token | Use |
|---|---|
| `--duration-fast` (~120ms) | Hover, focus, colour and opacity changes on small elements |
| `--duration-base` (~200ms) | Dropdowns, accordion panels, tab switches, toasts entering |
| `--duration-slow` (~320ms) / `--duration-slower` (~520ms) | Modals, drawers, section reveals / large full-bleed transitions only, rare |
| `--ease-standard` / `--ease-enter` / `--ease-exit` | Settling in place / arriving (decelerate) / leaving (accelerate, and faster than it arrived) |

**Non-negotiable:** honour `prefers-reduced-motion`. Collapsing every duration to ~1ms in one media query (as
in §3) covers it globally without auditing each animation. Never animate a value that shifts the reading
position of text someone is currently reading.

> **Dial.** Calm: one gentle onset on the focal element per viewport, nothing loops. Energetic: entrance
> animation, staggered reveals and hover flourishes are on-brand — but a looping, pulsing element is an
> attention tax the visitor never agreed to pay, and it never belongs on a form.

**Honesty rail.** Motion must not manufacture pressure: no ticking countdown for a deadline that does not
exist, no fake "others are viewing" animation, no progress bar moving independently of real progress. Animate
only what is true.

**Breakpoints.** Four thresholds are plenty: `sm 480 · md 768 · lg 1024 · xl 1280`. Design mobile-first.
*The gotcha every agent hits:* CSS custom properties **do not work inside `@media` queries**. Keep the numbers
in one place in the build config (a SCSS map, a Tailwind config, a JS constants file) and restate them in the
tokens file only as a comment. Two live sources for a breakpoint is a guaranteed drift bug.

**Z-index.** Never a bare number. The ladder in §3 uses 100-point gaps so a layer can be inserted without
renumbering. If you ever need `z-index: 9999`, the ladder is being bypassed and something is about to render
above your modal.

---

## 7. Core component inventory

The minimum set for a marketing site. Build them in this order — the first four unblock most pages.

| # | Component | Variants |
|---|---|---|
| 1 | **Button** | primary (one per viewport) · secondary/outline · ghost/text · destructive · sizes sm/md/lg · icon-only |
| 2 | **Link** | inline (underlined) · standalone · nav · quiet |
| 3 | **Input + Field** | text · email · textarea · select · checkbox · radio · toggle — each wrapped in a Field with label, help text and error slot |
| 4 | **Card** | static · linked (whole card clickable) · elevated · bordered |
| 5 | **Badge / Pill** | neutral · brand · success · warning · danger · info |
| 6 | **Accordion** | single-open · multi-open |
| 7 | **Tabs** | horizontal · scrollable on mobile |
| 8 | **Table** | plain · comparison (feature matrix) |
| 9 | **Modal / Dialog** | standard · confirm |
| 10 | **Toast / Inline alert** | success · error · info |
| 11 | **Nav** | desktop bar · mobile drawer · sticky variant |
| 12 | **Footer** | full · compact |

**Deliberately absent:** carousels (they hide content and perform poorly), auto-playing video heroes,
exit-intent popups, countdown timers. Each may be justifiable in a specific case; none belongs in a default
system — and a countdown belongs only where the deadline is genuine.

### 7.1 The state matrix

Every interactive component implements every state marked ✓. "It looks fine" is not a state.

| Component | default | hover | focus-visible | active | disabled | loading | error |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Button | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| Link | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Input / Field | ✓ | ✓ | ✓ | — | ✓ | ✓ | ✓ |
| Checkbox / Radio / Toggle | ✓ | ✓ | ✓ | ✓ | ✓ | — | ✓ |
| Select | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Card (linked) | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Accordion header | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Tab | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |
| Modal | ✓ | — | ✓ (trap) | — | — | ✓ | ✓ |
| Toast | ✓ | ✓ (pause) | ✓ | — | — | — | ✓ |
| Nav item | ✓ | ✓ | ✓ | ✓ | ✓ | — | — |

**State rules that catch the usual defects:**

- **Focus-visible, not focus.** Style `:focus-visible` so keyboard users get a ring and mouse users get no
  stray outline. Never delete an outline without replacing it with something meeting 3:1 contrast.
- **Hover is not a state on touch.** Anything only discoverable on hover is invisible to half your traffic.
- **Loading reserves its own space.** A button that shrinks when its label becomes a spinner shifts the layout
  under the user's finger. Keep the width, swap the contents, block re-submission.
- **Disabled must be explained** — greyed out with no reason is a dead end; pair it with helper text saying
  what would enable it. A disabled control must never be what stands between a user and cancelling,
  unsubscribing or getting a refund; that is a dark pattern wearing a state's clothing.
- **Error is a triple:** a visual change, an icon or word, and a sentence saying *what to do*. Colour alone
  fails greyscale and colour-blind users. Validate on blur or submit, never on every keystroke.
- **Feedback on every interaction.** Nobody should wonder whether their click registered. Where a wait is
  unavoidable, a skeleton placeholder beats a spinner on a blank field — it shortens the felt wait and shows
  the shape of what is coming.

### 7.2 Accessible-name requirements

Every interactive element needs a name a screen reader can announce. This is where most systems fail silently.

| Component | Requirement |
|---|---|
| Button with text | The visible text is the name. Make it the outcome ("Get the checklist"), not the mechanic ("Submit") |
| Icon-only button | `aria-label` describing the action, plus a visible tooltip on hover/focus |
| Link | Meaningful out of context — never "click here" or a bare "read more" repeated ten times per page |
| Input | A real `<label for>`. A placeholder is **not** a label; it disappears the moment the user types |
| Field error | `aria-describedby` linking the input to the error text, and `aria-invalid` on the input |
| Toggle / Checkbox | Label plus state announced (`aria-checked`, or native input semantics) |
| Accordion | Header is a real `<button>` with `aria-expanded` and `aria-controls` |
| Tabs | `role="tablist"` / `tab` / `tabpanel` wiring, arrow-key navigation, one tab stop into the set |
| Modal | `role="dialog"`, `aria-modal`, an `aria-labelledby` title, focus trapped, focus returned to the trigger on close, Escape closes |
| Toast | A polite live region so it is announced without stealing focus |
| Nav | `<nav>` with an `aria-label` when there is more than one on the page; current page marked `aria-current="page"` |
| Image | Meaningful `alt`, or `alt=""` if purely decorative — never a filename |

**Semantic HTML first.** A `<div>` with a click handler needs a role, a tabindex, keyboard handlers and
focus styles to reach parity with a `<button>` that needs none of them. Use the native element. Reach for
ARIA only when no native element exists, and remember that wrong ARIA is worse than none.

---

## 8. Accessibility gates

Pass/fail, checked before launch and re-checked in **both** themes.

| Gate | Threshold | Common failure it catches |
|---|---|---|
| **Contrast** | 4.5:1 body · 3:1 large text (~24px+, ~19px+ bold) · 3:1 interactive edges, focus rings, meaningful icons | An accent that passes on white and fails on the tinted section |
| **Focus visible** | Every interactive element, ≥3:1 against its adjacent surface | `outline: none` shipped with no replacement |
| **Tap target** | ≥44×44px, ≥8px between adjacent targets (padding counts) | A 16px icon button in a mobile nav |
| **Keyboard-complete** | Every action operable by keyboard; visible skip-to-content link; logical tab order; no trap except an intentional modal trap Escape releases | Custom dropdowns and `div` buttons |
| **Motion preference** | `prefers-reduced-motion` honoured globally; nothing conveyed by animation alone | A reveal that leaves content invisible when motion is off |
| **Colour not sole cue** | Greyscale-screenshot test passes | Red/green status dots with no icon or word |
| **Zoom 200%** | No horizontal scroll, no clipped content | Fixed-height containers with fixed-px text |
| **Mobile body size** | Never below 16px | iOS zooms form fields on focus below it |

---

## 9. Asset system

Assets drift faster than code because they live in design tools. Give them the same treatment: one export
directory, one naming convention, one rule sheet.

| Asset | Ship | Rules that prevent the usual damage |
|---|---|---|
| **Logo lockups** | Primary horizontal · stacked · mark-only · single-colour (dark backgrounds, print) | Define **clear space** as a unit derived from the mark itself (cap-height, or the height of a counter) so it scales automatically — a fixed pixel value breaks at every other size. Define a **minimum size** below which mark-only is mandatory |
| **Favicon / app icons** | SVG favicon · 32×32 PNG fallback · 180×180 apple-touch · 192 + 512 PNG + maskable for the manifest | Design the favicon *separately* from the logo — a wordmark at 32px is a smudge. Check it on both a light and a dark browser tab |
| **OG / social image** | One 1200×630 template, generated per page | Keep text ~80px inside every edge (platforms crop differently). Lock logo position, headline zone, one accent. Must read as a thumbnail. Wire `og:image` **and** `twitter:image` ([../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md)) |
| **Icon set** | One family, one 24px grid, one stroke width, consistent caps and joins | Never mix outline and filled in the same context. Meaningful icons need a label; decorative ones need `aria-hidden="true"`. Inline SVG beats an icon font — it inherits `currentColor` and does not vanish when a font request fails |

**Forbid in writing** (in `usage-rules.md`, not in someone's head): stretching the logo, recolouring outside
the approved set, adding effects, placing it on a busy image without a scrim, and rebuilding the wordmark in a
live font.

---

## 10. Documenting it so an agent can build against it

Three files. More than three and nobody reads any of them.

| File | Contains | Rule |
|---|---|---|
| `tokens.css` | Every raw value in the system, grouped and commented | The only file in the repo where a hex, a px or a duration may be written |
| `components.md` | The inventory, each component's variants, its state matrix row, its anatomy, and its accessible-name requirement | One section per component, in the same shape every time |
| `usage-rules.md` | When to use which variant, hard limits ("one primary button per viewport"), forbidden patterns, and the dial position | Written as rules with numbers, not principles with adjectives |

**Write for a machine reader.** An agent needs what a new engineer needs, plus one thing: the *negative*
space made explicit. State what must not be done, because a model will otherwise fill the gap with a plausible
convention borrowed from somewhere else. "Cards use `--shadow-sm`; never `--shadow-lg`, which is reserved for
modals" prevents a whole class of error that "use shadows tastefully" does not.

The brand brief ([../templates/brand-brief.md](../templates/brand-brief.md)) stays upstream as the source of
*intent*; these three files are the source of *implementation*. If they disagree, the brief wins and the files
get fixed. The prompt pack ([../ops/16-prompt-pack.md](../ops/16-prompt-pack.md)) covers handing the bundle to
an agent.

---

## 11. Drift prevention

A design system does not decay because someone disagrees with it. It decays because a deadline made one
hard-coded value cheaper than one new token, twenty times.

| Rule | In practice |
|---|---|
| **One source of truth per value** | A colour lives in `tokens.css` and nowhere else. A breakpoint lives in the build config and the CSS only references it |
| **A review gate against raw values** | Before merge, grep component and page files for hex codes, `rgb(`, `px` outside the tokens file, and bare `z-index` numbers. Every hit is either a new token or a mistake. Five lines of script; run it in CI and it is never skipped |
| **The rule of three** | A one-off value is allowed once. Flag it the second time. The third time it becomes a named token from the taxonomy in §1 |
| **No component reaches past Layer 2** | A component referencing `--brand-600` instead of a semantic alias is a review comment every time, not a style preference |
| **New tokens need a role name** | If you cannot name it without describing where it sits on a page, you need an existing token, not a new one |
| **Delete on sight** | An unconsumed token is worse than no token — it invites divergent use later. Sweep quarterly |
| **Change the value, not the consumers** | A rebrand edits `tokens.css` and nothing else. If that is impossible, the system already drifted and the gate was not running |

**The health check.** Shift `--brand-h` by 40 degrees and reload. If the whole site moves coherently, the
system works. Every patch of the old hue that survives is drift — fix it before shipping anything else.

---

## 12. Standing it up in a day

| Hour | Do |
|---|---|
| 1 | Copy §3 into `tokens.css`. Tune hue, chroma, neutral tint, fonts, base size. |
| 2 | Build a `/styleguide` route that renders every token as a swatch, a size sample and a spacing bar. |
| 3–4 | Button (all variants + all states), Link, Field + Input, Card. |
| 5 | Badge, Accordion, Tabs. |
| 6 | Nav, Footer, Modal, Toast. |
| 7 | Contrast pass in both themes; keyboard pass with the mouse unplugged; tap-target pass at 375px. |
| 8 | Write `components.md` and `usage-rules.md`; add the grep gate to CI. |

The styleguide route is not overhead. It is how you find the four colours that fail contrast and the three
components missing a focus ring in ten minutes — before they are copied into forty pages.

---

## Apply it

- [ ] `tokens.css` exists and is the only file in the repo containing raw colour, size, duration or z-index values.
- [ ] Three naming layers in place: primitives → semantic aliases → (rarely) component tokens; no component references a primitive.
- [ ] Brand hue and chroma are tunable in one or two lines, and the whole palette derives from them.
- [ ] Spacing derives from a single base unit; every gap on the site comes from the ramp.
- [ ] Type scale is frozen — one base, one ratio, line-height bound to each step, mobile clamped.
- [ ] Motion tokens defined, and `prefers-reduced-motion` collapses all durations globally.
- [ ] Breakpoints live in exactly one place; the z-index ladder is named with gaps and no bare numbers exist.
- [ ] Dark theme (if shipping) reassigns semantic aliases only, and contrast was re-checked in both themes.
- [ ] Every component in §7 implements every ✓ state, including focus-visible, loading and error.
- [ ] Every interactive element has an accessible name; native elements used before ARIA.
- [ ] Accessibility gates passed: contrast, visible focus, 44px targets, keyboard-complete, 200% zoom, greyscale test.
- [ ] Asset system defined: logo lockups with derived clear space, full favicon set, OG template with safe area, one icon family.
- [ ] `components.md` and `usage-rules.md` written, including the forbidden patterns.
- [ ] Drift gate running in CI, and the hue-shift health check passes cleanly.

---

## Related

- [08 — Page architecture and section recipes](08-page-architecture-and-section-recipes.md) — where these components get assembled
- [10 — Conversion audit checklist](10-conversion-audit-checklist.md) — the pass/fail gate before launch
- [06 — Colour and typography](../psychology/06-color-and-typography.md) — the decisions this doc encodes as variables
- [05 — Visual attention and layout](../psychology/05-visual-attention-and-layout.md) — the spacing and focal-point logic behind the scales
- [02 — Identity, archetype and naming](../brand/02-identity-archetype-and-naming.md) — where the logo and asset rules originate
- [13 — Schema and technical wiring](../search/13-schema-and-technical-wiring.md) — OG image and metadata wiring
- [15 — Launch checklist and build order](../ops/15-launch-checklist-and-build-order.md) — where the design system sits in the sequence
- [16 — Prompt pack](../ops/16-prompt-pack.md) — handing this system to an AI agent
- [Brand brief template](../templates/brand-brief.md) — the upstream source of intent
