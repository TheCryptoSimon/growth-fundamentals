# Conversion Audit Checklist

The pre-ship gate. Run every check on this page before a URL goes live, and re-run it on a cadence after.
It is deliberately unkind: its job is to find the reason the page will underperform *before* traffic does.
Read [08-page-architecture-and-section-recipes.md](08-page-architecture-and-section-recipes.md) to build the
page; read this to decide whether it is allowed to ship.

---

## 0. How to run it

**Severity codes.** Every check carries one. Nothing else is negotiable.

| Code | Meaning | Consequence |
|---|---|---|
| **B** | Blocker | Page does not ship. No exceptions, no "we'll fix it next sprint". |
| **M** | Major | Ships only with a named owner and a date, logged in the audit record. |
| **m** | Minor | Logged, batched, fixed in the next polish pass. |

**Ship rule.** Zero **B**. No more than three **M**, each with an owner and a date. Minors logged, not
counted. A section with any unresolved **B** is scored zero regardless of what else passed.

**Section score.** `passed checks ÷ applicable checks`, rounded down. A section passes at **80%** and no
blockers. Mark a check `n/a` only when the page genuinely has no such element (a pricing table on a contact
page), never because it was hard to verify.

**Who runs it.** Not the person who wrote the page. Self-audit finds roughly the problems you already knew
about. If there is no second person, use the critique-gate protocol in §14 — a fresh-context reviewer with
no memory of the drafting decisions.

**Evidence, not opinion.** Every failed check needs an artefact: a screenshot, a console line, a validator
output, a quote from a test participant. "Feels cluttered" is not a finding. "Three elements compete for
first fixation at 375px — see screenshot" is.

**Name the dial first.** Several checks below have an inverse depending on where the brand sits on the
calm/premium/trust axis versus the energetic/urgent/playful one. That choice is made once, in
[../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md), and this audit enforces
consistency with it — not with some universal ideal. A page that mixes both ends fails the consistency check
even if each individual element is defensible.

| Section | What it protects | Blockers live here |
|---|---|---|
| 1 Clarity | Comprehension in five seconds | Yes |
| 2 Hierarchy | One focal point per viewport | Yes |
| 3 Message | One promise, evidenced | Yes |
| 4 Offer & CTA | A single unmistakable action | Yes |
| 5 Proof | Belief, honestly earned | Yes |
| 6 Objections | The five reasons people leave | No |
| 7 Pricing presentation | Price legibility and framing | No |
| 8 Friction | Every step justified | Yes |
| 9 Trust & compliance | Legitimacy and legal safety | Yes |
| 10 Technical & a11y | The page actually works | Yes |
| 11 Search & AI | Findable and quotable | No |
| 12 Analytics | You will know if it worked | Yes |

---

## 1. Clarity

A first-time visitor, with no context, can state **what it is**, **who it is for**, and **what to do next**
within five seconds. If they cannot, nothing else on this list matters.

### The five-second test, run cheaply

1. Capture a screenshot of the page as it appears on first paint at 375px wide, and a second at 1440px.
   Crop to the visible viewport — no scrolling.
2. Recruit five people who have never seen the product. Colleagues from another team, a friend, a partner's
   flatmate. Five is enough to surface a clarity failure; you are not measuring anything, you are looking for
   a pattern of confusion.
3. Show the image for five seconds. Use a phone timer. Then hide it.
4. Ask, in this order, without prompting: *What does this company do? Who is it for? What would you do next
   if you were interested?*
5. Record verbatim answers. Do not explain, defend, or correct — the moment you explain, the test is over.

**Pass criteria.** At least four of five name the category correctly (a course, a clinic, a scheduling tool).
At least four of five name the intended next action. At least three of five name the audience. Anything lower
is a **B**.

A model with no prior context can substitute for one of the five when you are iterating fast: paste the
screenshot and ask the same three questions cold. It is a useful smoke test and a poor final judge — it reads
text a human would never have fixated on. Never let it replace all five humans on a page that matters.

| # | Check | Sev |
|---|---|---|
| 1.1 | Five-second test passed at both 375px and desktop width | B |
| 1.2 | The headline names the category or the outcome, not a mood ("Scheduling for dental clinics", not "Your day, reimagined") | B |
| 1.3 | The audience is stated or unmistakably implied above the fold | M |
| 1.4 | No jargon, invented product noun, or internal codename appears before the visitor knows what the thing is | M |
| 1.5 | The page matches the promise of the link that led here — an ad about pricing lands on visible pricing | B |
| 1.6 | The primary essence is visible on load, not after an animation completes | M |
| 1.7 | Nothing above the fold requires a hover or a click to become comprehensible | M |

---

## 2. Hierarchy

One focal point per viewport. Every viewport, not just the first.

**The squint test.** Blur your eyes until text is unreadable (or apply a heavy Gaussian blur in any image
tool). Exactly one element should still assert itself per screenful. If two do, they are fighting; if none
do, the page is flat and the visitor has no entry point.

**The greyscale test.** Desaturate the screenshot completely. Hierarchy must survive — it should still be
obvious what is primary, what is secondary, what is body. If the structure collapses without colour, the
hierarchy was made of colour alone, which fails for colour-blind visitors and in low-light viewing.

**The single-accent rule.** One saturated accent colour in the whole viewport, spent on the primary action.
Everything else is neutral or a muted tint. *Dial:* this is the calm/premium setting and it is the safer
default. At the energetic end you may run two or three accents, but the primary action must still win on the
combined stack of size, contrast, and isolation — "more colours" never substitutes for "one clear winner".

| # | Check | Sev |
|---|---|---|
| 2.1 | Squint test: exactly one dominant element per viewport, at both widths | B |
| 2.2 | Greyscale test: hierarchy survives desaturation | M |
| 2.3 | One saturated accent per viewport, on the primary action | M |
| 2.4 | Hierarchy built with spacing and size before colour — headings sit closer to their own content than to the block above | M |
| 2.5 | No group of more than four peer items without sub-grouping | m |
| 2.6 | Whitespace is consistent — the spacing scale is used, not ad-hoc pixel values | m |
| 2.7 | No instruction depends on colour alone ("the button below", never "the green button") | M |
| 2.8 | Related elements are visually grouped; unrelated ones are separated | m |

---

## 3. Message

| # | Check | Sev |
|---|---|---|
| 3.1 | **One** promise on the page. If you can name two competing ones, cut or demote one | B |
| 3.2 | Written in second person, present tense | M |
| 3.3 | Concrete over abstract everywhere — "answers within one business day", not "responsive support" | M |
| 3.4 | Every claim that matters carries a *because* — the mechanism that makes it true, not a restatement | B |
| 3.5 | No superlative without evidence on the page ("the best", "the leading", "#1") | B |
| 3.6 | No unverifiable number anywhere. If you cannot point to the source, the number does not ship | B |
| 3.7 | Outcome described vividly; the process described lightly | m |
| 3.8 | Headings carry the takeaway, so a skimmer reading only headings gets the argument | M |
| 3.9 | Reading level appropriate to the audience; sentences short enough to parse on a phone | m |
| 3.10 | Terminology consistent with the rest of the site — one name per concept | m |

**The mechanism rule, stated plainly.** A trust line without a mechanism is decoration. "Your data is safe"
is decoration. "Your data is encrypted in transit and at rest, and we cannot read it because the key never
leaves your device" is a claim — testable, falsifiable, and therefore believable. Audit every trust line for
its mechanism. If a mechanism cannot be stated because it isn't true, delete the line; do not soften it.

---

## 4. Offer and CTA

| # | Check | Sev |
|---|---|---|
| 4.1 | Exactly one primary action on the page. Repeated, yes; competed with, no | B |
| 4.2 | The label is a literal motor verb plus its object: "Book a call", "Start the free trial", "Download the guide" | M |
| 4.3 | The same label everywhere it appears — no synonym drift between hero, mid-page, and footer | M |
| 4.4 | Secondary actions are visually quiet (text or ghost), never a second solid button of similar weight | B |
| 4.5 | The button is isolated by whitespace on all four sides | M |
| 4.6 | Assurance microcopy sits directly under the button, pre-answering the cost of clicking: what happens next, what it costs, what is not required | M |
| 4.7 | A freedom-to-choose line at the ask ("Cancel any time", "No card needed") | m |
| 4.8 | The click destination matches the label exactly. A "See pricing" button lands on prices, not a form | B |
| 4.9 | No exit-intent overlay, countdown, or interstitial fires before the visitor has seen the offer | M |
| 4.10 | Every CTA reachable and tappable at 375px without zoom | B |

**Why the label matters.** A button naming the physical action reads as lower risk than one naming a
commitment. "Get started" is vague; "Create your first schedule" tells the brain exactly what the next second
of life looks like, and a concrete next second is easier to agree to than an abstract relationship.

**Dial.** Urgency-flavoured labels ("Claim yours now", "Grab the deal") belong at the energetic end. On the
calm/premium end they read as pressure and cost you trust, which is the exact asset that end is buying.
Invert to a plain declarative: "Book a consultation."

**Where the line is.** Assurance microcopy that is true is service. Assurance microcopy that is technically
true but engineered to conceal a cost ("Free to start" over a page that requires a card) is manipulation, and
the churn arrives about four weeks later with a chargeback attached.

---

## 5. Proof

| # | Check | Sev |
|---|---|---|
| 5.1 | Nothing invented. No fabricated testimonial, logo, rating, count, or case study. This is a career-ending check, not a style check | B |
| 5.2 | Every testimonial is attributable — a real name, role, and where they can be verified — or it is removed | B |
| 5.3 | Proof is specific: what changed, over what period, measured how | M |
| 5.4 | Proof appears *before* the ask, not after — objections answered ahead of the price | M |
| 5.5 | Aggregate ratings shown only if they come from a real, linked source, and the schema matches what is displayed | B |
| 5.6 | Client logos used only with permission and only for real customers | B |
| 5.7 | Authority signals state their basis: the credential, the years, the volume handled | m |
| 5.8 | Screenshots are of the real product at the current version | M |
| 5.9 | Any result shown is labelled as an individual result where outcomes vary | B |

---

## 6. Objections

Name the five reasons a qualified visitor leaves without acting. Write them as the visitor would say them,
not as marketing would phrase them. Then find each one answered on the page.

Typical shapes, adapt to your case: *too expensive for what it is* · *I don't believe it works for someone
like me* · *I don't have time to set it up* · *what if it's wrong for me and I'm stuck* · *why you and not
the cheaper one I already know*.

| # | Check | Sev |
|---|---|---|
| 6.1 | The top five objections are written down before the audit, from support tickets, sales calls, or churn interviews — not guessed at the desk | M |
| 6.2 | Each of the five has a specific answer on the page, findable without a search | M |
| 6.3 | The answers use the visitor's language, not the internal euphemism | m |
| 6.4 | A two-sided line exists — who this is *not* for — placed before the price | m |
| 6.5 | The FAQ answers real objections, not softballs that only restate features | M |
| 6.6 | No objection is answered by a claim that itself lacks a mechanism (§3.4) | M |

---

## 7. Pricing presentation

Applies to any page showing a price. See [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md)
for the reasoning behind each.

| # | Check | Sev |
|---|---|---|
| 7.1 | The price is visible without interaction. A pricing page that hides prices behind a form fails | M |
| 7.2 | The plan name reads at least as large as the price | m |
| 7.3 | The currency symbol is rendered smaller than the digits | m |
| 7.4 | Total cost is unambiguous: billing period, per-seat or flat, taxes, and anything added later | B |
| 7.5 | Annual savings shown as an absolute amount, not only a percentage | m |
| 7.6 | The intended plan is centre-stage and visually isolated; one CTA per card | M |
| 7.7 | Non-featured plans use quiet buttons | m |
| 7.8 | Any scarcity or deadline is literally true, with a real end date and a real consequence | B |
| 7.9 | No countdown timer that resets on reload | B |
| 7.10 | Refund, cancellation, and trial terms stated at the price, not only in the terms page | M |

**Dial.** Charm endings (`.99`) and strike-through anchors read as bargain framing and suit the energetic end.
Round numbers read as calm and considered and suit premium and emotional purchases — a therapy practice
pricing at `.99` undercuts itself. Pick per the brand's dial and apply it to every price on the site.

---

## 8. Friction

| # | Check | Sev |
|---|---|---|
| 8.1 | Every form field justified out loud, one at a time: what breaks if we don't collect this now? Anything without an answer is deleted | M |
| 8.2 | No field asks for something you can derive, default, or collect later | M |
| 8.3 | Labels are always visible — no placeholder-only labels that vanish on focus | M |
| 8.4 | Input formats are forgiving (spaces in card and phone numbers stripped silently, not rejected) | M |
| 8.5 | Errors prevented rather than scolded: unavailable dates disabled, submit disabled after click, required fields marked before submission | M |
| 8.6 | Validation is inline and specific; the error names the fix and does not say "you" | m |
| 8.7 | Entered data survives every error and every back navigation | B |
| 8.8 | The browser back button works from every step and loses nothing | B |
| 8.9 | Multi-step flows show position and remaining steps | m |
| 8.10 | Every dead end has an exit: a zero-results state offers alternatives, a failed payment offers a retry and a contact | M |
| 8.11 | Nothing irreversible happens without confirmation; nothing reversible demands one | m |
| 8.12 | The full path from landing to conversion has been walked end to end, on a phone, on cellular data | B |

---

## 9. Trust and compliance

| # | Check | Sev |
|---|---|---|
| 9.1 | Real, reachable contact information — an address or a monitored channel, not a bare form | B |
| 9.2 | Legal identity of the operating entity stated where the jurisdiction requires it | B |
| 9.3 | Privacy policy, terms, and cookie handling present, current, and linked from every page | B |
| 9.4 | The privacy copy matches what the site actually does — every tracker on the page is disclosed | B |
| 9.5 | Consent requested before non-essential tracking fires, where required | B |
| 9.6 | Required disclaimers present, accurate, and legible — never in 9px grey on grey | B |
| 9.7 | Disclaimers sit outside the persuasive body (a footer band or a dedicated block), so they inform without poisoning the argument | m |
| 9.8 | No claim on the page would embarrass you if quoted back in a complaint | B |
| 9.9 | Third-party marks and imagery are licensed | M |
| 9.10 | Security signals (payment badges, certifications) are real and current | B |

**On disclaimer placement.** Burying a required disclaimer is a compliance risk; splicing it into the middle
of your strongest paragraph is a conversion risk. The resolution is *proximity without interruption*: a clear,
readable block adjacent to the claim or in a consistent footer band, same on every page, never collapsed
behind a toggle.

---

## 10. Technical and accessibility

| # | Check | Sev |
|---|---|---|
| 10.1 | 375px wide: no horizontal scroll. Verify `document.documentElement.scrollWidth === window.innerWidth` | B |
| 10.2 | No text smaller than 14px on mobile body copy | M |
| 10.3 | Tap targets at least 44×44 CSS px with 8px between adjacent targets | M |
| 10.4 | Contrast meets AA: 4.5:1 body text, 3:1 large text and meaningful UI edges — measured, not eyeballed | B |
| 10.5 | Text over imagery is legible across the whole text block, not only where the scrim happens to sit | M |
| 10.6 | Visible `:focus-visible` state on every interactive element | B |
| 10.7 | The whole conversion path is completable by keyboard alone, in a sensible tab order, with no traps | B |
| 10.8 | `prefers-reduced-motion` honoured; no content is revealed only by animation | M |
| 10.9 | Every meaningful image has alt text; decorative images have empty alt | M |
| 10.10 | Landmarks and one `h1`; headings descend without skipping levels | m |
| 10.11 | Core Web Vitals within the standard "good" thresholds — LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 — measured on a mid-range phone on throttled network, not on your laptop | M |
| 10.12 | No layout shift on load: images and embeds have reserved dimensions, web fonts have a fallback metric-matched | B |
| 10.13 | The LCP element is prioritised (preloaded hero, no lazy-loading above the fold) | M |
| 10.14 | Console clean of errors on load and on the conversion click | M |
| 10.15 | The page renders usefully with JavaScript blocked or slow — critical content is in the HTML | M |
| 10.16 | Verified in at least one non-Chromium browser and on a real phone, not only a simulator | M |

---

## 11. Search and AI answerability

| # | Check | Sev |
|---|---|---|
| 11.1 | Exactly one primary keyword or query intent per URL; no other page on the site targets the same one | M |
| 11.2 | Title, meta description, and `h1` capture that intent; the body reads in the brand's own frame | M |
| 11.3 | A self-contained direct answer appears within the first screenful — roughly 40 to 60 words that stand alone if lifted out of context and cited | M |
| 11.4 | Definitions and key facts are stated once, canonically, and reused verbatim across the site | m |
| 11.5 | Structured data present, of the correct type, and validating clean | M |
| 11.6 | Schema describes only what is on the page; no rating or review markup without real, displayed reviews | B |
| 11.7 | Canonical URL present and self-referential unless deliberately pointing elsewhere | M |
| 11.8 | Open Graph and social card image present, 1200×630, with legible text at thumbnail size | m |
| 11.9 | The page links **out** to two or more relevant siblings and **up** to its parent hub, with descriptive anchor text | m |
| 11.10 | The page is in the sitemap, is not blocked by robots, and is server-rendered | B |
| 11.11 | Headings are phrased as questions or claims a person would actually search or ask | m |

---

## 12. Analytics

Nothing here is optional. A page whose conversion you cannot measure is a page you cannot improve, and the
absence will not be noticed until someone asks for numbers three months from now.

| # | Check | Sev |
|---|---|---|
| 12.1 | The conversion event exists, is named per the site's naming convention, and is documented | B |
| 12.2 | The event has been **fired and observed in the live tool** on production after deploy — not assumed from code review | B |
| 12.3 | It fires once per conversion. Double-fires and re-fires on back navigation checked explicitly | M |
| 12.4 | Micro-conversions instrumented where they inform the funnel: form start, step completion, pricing viewed | m |
| 12.5 | No personal data in URLs, event parameters, or page titles | B |
| 12.6 | Traffic source survives the whole path — parameters are not stripped by a redirect mid-funnel | M |
| 12.7 | The measurement respects the consent state and the privacy copy in §9.4 | B |
| 12.8 | A baseline is recorded before the change, so the next audit has something to compare against | M |

---

## 13. What to fix first

Two rules, applied in order.

**Rule one — the ordering law.** Clarity beats persuasion beats polish. A visitor who does not understand the
offer cannot be persuaded by it, and a beautifully typeset page nobody comprehends converts at zero. Fix in
that order even when the polish fix is easier and more satisfying. Every blocker in §1 outranks every finding
in §2 through §12.

**Rule two — score the rest.**

```
Priority = (Impact × Confidence) ÷ Effort
```

| Factor | 1 | 3 | 5 |
|---|---|---|---|
| **Impact** | Affects a minor element below the fold | Affects a section most visitors see | Affects the headline, the primary action, or the whole path |
| **Confidence** | A hunch worth testing | A known principle, unverified here | Observed failure — a test participant confused, an error in the console, a validator failing |
| **Effort** | Copy change or token swap, minutes | A section rebuild, hours | New component or backend work, days |

Work the highest scores first. Two overrides:

- **Any B jumps the queue** regardless of score. Blockers are not scored; they are removed.
- **A confidence of 5 outranks an impact of 5** when the impact is speculative. Fixing an observed failure
  beats redesigning a hero because someone had an idea about heroes.

Log every finding with its severity, score, owner, and date, even the ones you fix immediately. The log is
what turns a one-off audit into a standard — repeated findings across pages become design-system fixes in
[09-design-system-and-tokens.md](09-design-system-and-tokens.md), not another manual patch.

---

## 14. The critique gate

The audit above is the instrument. This is the loop you run it in.

1. **Screenshot mobile first, at 375px.** Always mobile before desktop. Desktop hides the crowding, the
   overflow, and the tap-target failures, and it flatters a hierarchy that will collapse on a phone. Capture
   the first viewport, then every subsequent viewport down the page.
2. **Then desktop**, at a common width. Same discipline — viewport by viewport.
3. **Grade cold.** Hand the screenshots to a reviewer with no memory of the design decisions — another
   person, or a fresh model session with the brief but not the debate. Ask, in the harshest register
   available: *Where does my eye land first, and is that the thing you wanted? What is competing with the
   primary action? Which claim did you not believe, and why? Which sentence made you stop reading? What would
   make you leave this page? Is anything here dishonest, or engineered to be technically true?*
4. **Fix what is material.** Not everything named — material means it maps to a check above with a severity.
   A reviewer's stylistic preference with no check behind it is noted and ignored.
5. **Re-screenshot and repeat.** Same viewports, same questions, fresh context.
6. **Stop when a harsh reviewer finds nothing material.** Not when they find nothing — a determined critic
   always finds something. Nothing *material*: no blockers, no more than three majors with owners.
7. **Cap the loop at three rounds.** If round three still surfaces blockers, the problem is upstream — the
   positioning or the page brief, not the execution. Go back to
   [../templates/page-brief.md](../templates/page-brief.md) rather than iterating the surface.

**The rule that makes this work:** the reviewer must not be the author, and must not be told the reasoning.
Every explanation you give the reviewer is an explanation your visitors will never receive. If the page needs
the preamble, the page is the problem.

### Cadence after launch

| When | What to run |
|---|---|
| Before every ship | The full audit |
| 7 days after ship | §12 analytics verification, plus §1 if traffic behaves oddly |
| Monthly on money pages | §3 message, §5 proof (dates go stale), §11 search |
| Quarterly, whole site | Full audit on the top five pages by traffic and by revenue |
| After any CMS, theme, plugin, or dependency update | §10 technical, §12 analytics — updates silently break both |
| Whenever a claim, price, or policy changes | §3, §5, §7, §9 on every page repeating it |

---

## Apply it

- [ ] Severity codes assigned to every finding; zero blockers before ship, majors capped at three with owners and dates.
- [ ] Five-second test run with five fresh people at 375px and desktop; four of five name the category and the next action.
- [ ] Squint test and greyscale test passed on every viewport, at both widths.
- [ ] Exactly one primary action, one literal motor-verb label, repeated unchanged, isolated by whitespace, with assurance microcopy under it.
- [ ] Every claim carries its mechanism; every superlative carries evidence; every number is traceable to a source.
- [ ] Nothing invented anywhere — no fabricated testimonial, rating, logo, count, scarcity, or countdown.
- [ ] The top five objections written from real evidence and each answered on the page before the ask.
- [ ] Every form field justified out loud; entered data survives errors and the back button; no dead ends.
- [ ] Real contact details, current legal pages, and honest disclaimers placed outside the persuasive body.
- [ ] 375px with no horizontal scroll, tap targets ≥44px, AA contrast measured, focus-visible present, full keyboard path, reduced motion honoured.
- [ ] Core Web Vitals within good thresholds on a throttled mid-range phone, with no layout shift on load.
- [ ] One primary keyword, a self-contained direct answer in the first screenful, valid schema describing only what is displayed, canonical and OG present, links out and up.
- [ ] The conversion event fired and was **observed** in the live tool on production, once, with no personal data in the payload.
- [ ] Critique gate run mobile-first with a cold reviewer, capped at three rounds, closed only when nothing material remains.

---

## Related

- [08-page-architecture-and-section-recipes.md](08-page-architecture-and-section-recipes.md) — the section patterns this audit grades
- [09-design-system-and-tokens.md](09-design-system-and-tokens.md) — where repeated findings get fixed once, at the token level
- [../psychology/04-persuasion-core.md](../psychology/04-persuasion-core.md) — the mechanisms behind the message and proof checks
- [../psychology/05-visual-attention-and-layout.md](../psychology/05-visual-attention-and-layout.md) — the reasoning behind the hierarchy tests
- [../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md) — contrast, weight, and the single-accent rule
- [../psychology/07-pricing-psychology.md](../psychology/07-pricing-psychology.md) — why each pricing presentation gate exists
- [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md) — where the arousal dial is set
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — the message and CTA-label standards
- [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md) — keyword mapping and internal linking
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — the direct-answer and quotability checks
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — schema validation and canonical wiring
- [../ops/14-measurement-and-experimentation.md](../ops/14-measurement-and-experimentation.md) — verifying the conversion event and reading the result honestly
- [../ops/15-launch-checklist-and-build-order.md](../ops/15-launch-checklist-and-build-order.md) — where this gate sits in the launch sequence
- [../templates/page-brief.md](../templates/page-brief.md) — the brief this audit checks the page against
