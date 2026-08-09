# Launch Checklist and Build Order

The sequence from an empty repository to a live site, split into eight phases with a gate between each.
Read it before starting the build, and use it as the running plan. If you are an AI agent, treat each gate
as a hard stop: report the gate result and wait rather than proceeding on an unproven phase.

---

## 0. How the phases work

Each phase has **deliverables**, a **gate** that must be demonstrably true before the next phase begins, and
a **failure mode** — the specific way teams get this phase wrong, which is almost always the same way.

**Why gates rather than a task list.** Website work fails backwards: a wrong decision in phase 0 does not
look like a problem until phase 5, when it appears as "the copy is fine but the site does not work." A gate
converts an invisible upstream error into a visible, cheap stop.

| Phase | Ships | Gate in one line |
|---|---|---|
| **0. Decide** | Brand brief | A human answered the five decisions in writing |
| **1. Identity + system** | Name, tokens, components | Tokens exist in code and pass contrast |
| **2. Core pages** | Home + the one page that carries the offer | Both pass the conversion audit on two viewports |
| **3. Search layer** | URL map, metadata, schema, sitemap, robots, `llms.txt` | Structured data validates; no two pages compete |
| **4. Measurement** | Analytics, events, the primary conversion | The conversion event fired in a real browser |
| **5. Pre-launch QA** | The QA sweep below | Every line green or written down as an accepted gap |
| **6. Launch** | The site, live | Logged-out visitors get 200s and the same content |
| **7. First 90 days** | Learning loop | One change at a time, each logged |

**Time-boxing rule.** If a phase runs more than double its planned time, the problem is upstream, not in the
work. Go back one phase and check the gate really passed.

## 0.1 The smallest responsible version

This library describes the full method. Most people reading it are one or two people with a few weeks, and
a plan that cannot be executed gets abandoned wholesale — which is worse than a plan that was cut on purpose.
So: here is what a first launch may drop, what it may defer, and what it may never drop. Decide this
explicitly at the start rather than discovering it at 2am the night before launch.

**Never cut — these are not scope, they are the conditions for shipping at all.** The five decisions and a
written brand brief. One promise with its mechanism. The honesty rails. AA contrast and a keyboard-operable
conversion path. Legal pages that describe what the site actually does. A working form that has been proven
to deliver to a human inbox. One conversion event, observed firing. `robots.txt` and `noindex` verified on
the live domain. Cutting any of these does not save time; it converts a week of work into a liability.

**Cut for v1, add in the first 90 days.** The comparison pages, the glossary, the blog, the interactive
element, the second and third audience pages, dark mode, the prompt panel, session replay, `llms.txt` (it is
cheap but nothing depends on it), IndexNow, and every page in tiers 3–6 of the architecture. A four-page site
that is clear and honest outranks and outconverts a fifteen-page site that is thin — and it is the only kind
of site two people can keep true.

**The one-week version, in order.** Day 1: the five decisions, written. Day 2: name cleared enough to buy the
domain, tokens in code, contrast checked. Days 3–4: home page and the one page that carries the offer, both
against a page brief, both audited at 375px. Day 5: legal pages, forms tested for real, analytics with one
event observed, schema for `Organization` + `WebPage`, sitemap and robots verified live. Day 6: the critique
gate — a cold reviewer, two rounds. Day 7: launch by the Phase 6 runbook. Everything else in this pack is
month two onward.

**The honest trade you are making.** A cut launch reaches fewer queries and carries less proof; it does not
get to be less true, less accessible, or less measurable. If a deadline is forcing you toward the "never cut"
list, the deadline is wrong — move it, or launch a smaller site, but do not launch a dishonest or broken one
and plan to fix it later. Later is where that work goes to die.

**Write the cuts down.** Whatever you defer goes on the accepted-gaps list from Phase 5, with an owner and a
date, on day one — not in someone's memory. A deferred decision that nobody recorded is indistinguishable
from an oversight six weeks later.

## Phase 0 — Decide

**Deliverables**

- [../templates/brand-brief.md](../templates/brand-brief.md), filled in by a human: audience, category, the
  one promise with its mechanism, the energy target on the calm ↔ urgent dial, and the price ladder.
- The real alternative set the buyer is weighing, including "do nothing."
- The honesty rails for this specific brand — including any regulated claims you may not make.
- A single-sentence definition of what the site is *for*: one primary conversion, named.

**Gate.** Somebody who has never heard of the product can read the brand brief and correctly state what it
is, who it is for, why it beats the alternative, and what it costs. If they cannot, the brief is not done and
no design work should start.

**How teams get it wrong.** They start in Figma or in a component library because it feels like progress,
then reverse-engineer positioning from a layout they already like. The resulting site is competent and
generic, and no amount of later copy editing fixes it — the structure encodes the missing decision.

**Depth:** [../00-START-HERE.md](../00-START-HERE.md), [../brand/01-positioning-and-category.md](../brand/01-positioning-and-category.md).

## Phase 1 — Identity and design system

**Deliverables**

- Name, cleared: trademark search in the relevant classes and territories, domain, social handles, and the
  spelling and pronunciation tests. Do not skip the legal clearance because the domain was available.
- Logo or wordmark at the minimum useful set of sizes, plus a favicon set and a monochrome variant.
- **Design tokens in code before any page exists**: colour (with semantic names, not `blue-500` scattered in
  markup), a type scale, a spacing scale, radii, shadows, motion durations, breakpoints.
- Core components: button variants (exactly one primary style), input, card, section wrapper, nav, footer.
- The canonical entity paragraph — one description used identically in the footer, the About page, schema,
  `llms.txt`, and every external profile.

**Gate.** Tokens are referenced by components, not hard-coded; body text passes AA contrast (4.5:1) and large
text and UI boundaries pass 3:1, including text over images; the energy target is *visible* in the tokens —
someone should be able to infer the dial setting from the palette, weights, and motion durations alone.

**How teams get it wrong.** Building pages first and extracting a system afterwards. You end up with eleven
greys, four spacing rhythms, and three button styles, and every later change costs three times what it
should. The second failure: choosing the palette from a mood board rather than from the meaning you want
borrowed.

**Depth:** [../brand/02-identity-archetype-and-naming.md](../brand/02-identity-archetype-and-naming.md),
[../psychology/06-color-and-typography.md](../psychology/06-color-and-typography.md),
[../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md).

## Phase 2 — The core pages

Build two pages properly before building ten pages adequately.

**Deliverables**

- The **home page** and **the one page that carries the offer** (pricing, product, book-an-appointment,
  whichever is your primary conversion).
- A [../templates/page-brief.md](../templates/page-brief.md) for each, written *before* the page.
- Message hierarchy applied: one promise above the fold, three pillars with proof under each, objections
  answered before the ask.
- One primary CTA per viewport, and quiet secondaries.
- Real content. Not lorem ipsum, not placeholder testimonials, not a stock hero of people laughing at a
  laptop.

**Gate.** Both pages pass [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md)
at 375px and at desktop width, and a five-second test on a stranger returns the correct answers to *what is
it, who is it for, what do I do next*.

**How teams get it wrong.** Shipping fifteen thin pages instead of two strong ones, because page count feels
like progress. A second, subtler version: filling the page with sections copied from admired sites, producing
a page that is structurally a tour of other companies' priorities.

**Then, and only then:** about, contact, proof, FAQ, legal, and any supporting pages — each with its own
brief, each passing the same audit.

**Depth:** [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md),
[../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md).

## Phase 3 — The search and AI-visibility layer

**Deliverables**

- **Keyword-to-URL map**: one primary keyword per URL, with no two pages competing. Done as a table, checked
  in to the repo.
- Titles and meta descriptions written per page (not templated from the H1), canonical URLs on every page,
  and a coherent H1/H2 outline.
- A **direct-answer paragraph** near the top of every important page — self-contained, quotable, and true
  without the surrounding page.
- **Structured data as one connected graph** — every node cross-referencing a single organisation identifier
  — validated in a structured-data testing tool.
- `sitemap.xml` generated from one registry (never maintained by hand), `robots.txt` with a deliberate
  crawler policy, `llms.txt` describing what the product is and is not.
- Internal links: every page links up to its hub and across to two or three genuinely relevant siblings.
- Per-page Open Graph images and descriptions.

**Gate.** Structured data validates with no errors; the sitemap contains only indexable public URLs (no
staging, no private routes, no redirects, no 404s); every page has exactly one canonical; nothing important
depends on client-side JavaScript to become visible in the raw HTML.

**How teams get it wrong.** Treating this as a post-launch task. Retrofitting a URL map after publishing
means redirects, lost equity, and cannibalised pages. The other classic: a hand-maintained sitemap that
silently drifts from reality within a fortnight.

**Depth:** [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md),
[../search/12-geo-ai-search.md](../search/12-geo-ai-search.md),
[../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md).

## Phase 4 — Measurement

**Deliverables**

- First-party, cookieless analytics installed on marketing surfaces only.
- `EVENTS.md` with the capped event vocabulary and one named primary conversion.
- Search Console and the Bing equivalent verified; sitemap submitted (submission itself happens on launch
  day, but verification is set up now).
- Uptime monitoring on the home page and the primary form endpoint; error logging wired.
- A scheduled real form submission that must arrive in a human inbox.

**Gate.** The primary conversion event has fired in a real browser, on a phone, and appears in the analytics
tool. Not "the code is installed" — *observed*.

**How teams get it wrong.** Installing analytics, never testing an event, and discovering three months later
that the conversion event was never wired to the button that matters. Second failure: adding a marketing
pixel without updating the privacy page and consent policy in the same change.

**Depth:** [14-measurement-and-experimentation.md](14-measurement-and-experimentation.md).

## Phase 5 — Pre-launch QA

Run this as a single sweep, in order, on the actual staging build. Every line is a yes/no you can verify.
Anything you choose not to fix goes on a written accepted-gaps list — not into someone's memory.

### 5.1 Rendering and responsive

- [ ] Every page checked at 375px, ~768px, and desktop; and in at least two browser engines (a Chromium
      browser and Safari or Firefox).
- [ ] No horizontal scroll anywhere at 375px — verify the document width equals the viewport width, do not
      eyeball it.
- [ ] Console is clean on every page: no errors, no failed requests, no mixed-content warnings.
- [ ] Nothing important requires JavaScript to appear; disable JS and confirm the core message is still there.
- [ ] Dark-mode or forced-colors behaviour is either correct or explicitly disabled — not accidental.
- [ ] Long-content edge cases: a very long name in a testimonial, a two-line heading, a nine-item nav.

### 5.2 Content and legal

**Working out what actually applies to you.** The checks below assume you already know which obligations you
carry. Most first-time founders do not, and "we'll add a privacy policy" is where that gap usually hides.
This is not legal advice and this pack cannot give you any — but the *questions* are answerable in an
afternoon, and answering them is what turns a generic template into something defensible:

1. **Where is the operating entity, and where do the visitors come from?** Obligations follow both. Selling
   into a market usually attaches that market's rules regardless of where you are incorporated.
2. **What personal data does the site touch, and on what basis?** List every field, every embed, every
   analytics call, every form processor. If you cannot list them, you cannot describe them, and the privacy
   page will be fiction. This list *is* the privacy policy's raw material.
3. **Who is your data processor for each one?** Form handler, email tool, analytics, hosting, chat widget.
   Most regimes expect you to name categories of recipients; you cannot name what you never inventoried.
4. **Does the jurisdiction require the legal entity, address, or a registration number on the site?** Several
   do, and it is usually a footer or imprint obligation with a fixed format.
5. **Is your category regulated?** Health, finance, legal, insurance, food, children's products, alcohol,
   crypto, employment — each carries claim restrictions that override every persuasion tactic in this pack.
   Write those into §13 of the brand brief as hard rails before a word of copy is drafted.
6. **What are the consumer-facing obligations of the model you chose?** Subscriptions, trials that convert to
   paid, and distance selling typically carry specific disclosure, cancellation and refund requirements —
   and they change the copy, not just the terms page.

**Where the pages come from.** A reputable generator or a template from your payment provider is an
acceptable *starting point* and a poor finishing point: it will describe a generic site, not yours. Redline
it against the answers above, delete every clause about a thing you do not do, and add every tool from
question 2 by name. For anything in question 5, or any contract a customer signs, pay a qualified lawyer in
your jurisdiction — this is the one line item where a few hundred spent early is unambiguously cheaper than
the alternative.

**The rail this exists to protect.** A privacy policy that does not match the trackers on the page is not a
paperwork failure, it is a false statement on your website, and it sits on the wrong side of the honesty
rails in [../00-START-HERE.md](../00-START-HERE.md) exactly like an invented testimonial does.

- [ ] Every claim on the site has a mechanism stated near it and a real source behind it.
- [ ] The data inventory from question 2 exists as a written list, and the privacy policy matches it item by
      item — including anything added since the policy was written.
- [ ] Any regulated-category restriction is recorded in the brand brief and has been checked against the
      live copy, not just intended.
- [ ] No placeholder text, no sample testimonials, no logos of organisations that are not customers.
- [ ] Prices, plan contents, and refund terms on the site match the payment system exactly.
- [ ] Privacy policy describes the **actual** data flow, including analytics, embeds, and form processing.
- [ ] Terms, cookie policy (if any cookies), and required company or regulatory identifiers are present.
- [ ] Contact information is real and monitored; a physical address if your jurisdiction requires one.
- [ ] Spelling and grammar pass, and the voice rules pass on every new surface.
- [ ] Any regulated or restricted claim has been checked against the rules for your category.

### 5.3 Forms and email

- [ ] Every form submitted for real, from a phone and a desktop, and the message **arrived in the inbox**.
- [ ] Confirmation state is unambiguous — the user knows it worked without guessing.
- [ ] Validation messages are helpful, described in text (not colour alone), and appear next to the field.
- [ ] Spam protection is present and does not block real people; no CAPTCHA where a honeypot suffices.
- [ ] Autofill works: correct `autocomplete`, `type`, and `inputmode` on every field.
- [ ] Any automated reply sends from a monitored address and does not land in spam (test to two providers).

### 5.4 Errors and edge routes

- [ ] A real 404 page exists, is styled, returns HTTP 404 (not 200), and offers a route back.
- [ ] A 500/error page exists and does not leak stack traces.
- [ ] Trailing-slash and case behaviour is consistent and redirects rather than duplicates.
- [ ] `http://` and the non-canonical `www` variant both redirect once to the canonical origin — one hop, not
      a chain.

### 5.5 Search and indexing

- [ ] `robots.txt` is correct and does **not** block the whole site (the classic launch catastrophe).
- [ ] No stray `noindex` on production pages; verify in the rendered HTML, not in the CMS setting.
- [ ] `sitemap.xml` returns 200, lists only canonical indexable URLs, and is referenced from `robots.txt`.
- [ ] Structured data validates; the entity name, URL, and description match everywhere.
- [ ] `llms.txt` exists and agrees with the sitemap and the entity paragraph.
- [ ] Redirects from any previous URLs are in place, 301, single-hop, and tested from a list.

### 5.6 Sharing and assets

- [ ] Favicon set present, including the sizes used by mobile home screens.
- [ ] Open Graph and card metadata render correctly in a **real share preview** — paste the URL into a
      messaging app and a social composer and look at it. Validators lie about caching.
- [ ] OG images are the right dimensions, readable at thumbnail size, and not text-heavy.
- [ ] Images have meaningful `alt` text, explicit dimensions, modern formats, and lazy loading below the fold.

### 5.7 Accessibility

- [ ] Contrast: 4.5:1 for body text, 3:1 for large text and interactive boundaries, including over images.
- [ ] Full keyboard traversal: every interactive element reachable, in a sensible order, with a **visible**
      focus style. No keyboard traps in modals or menus.
- [ ] Heading order is hierarchical and used for structure, not sizing; exactly one H1 per page.
- [ ] All inputs have real labels; icon-only buttons have accessible names.
- [ ] `prefers-reduced-motion` is honoured and actually removes the motion.
- [ ] Page language is set; the tab order matches the visual order.
- [ ] One screen-reader pass on the home page and the primary conversion flow.

### 5.8 Performance budget

Set the budget before you optimise, then hold it.

| Target | Default worth adopting |
|---|---|
| Largest Contentful Paint | under 2.5s on a mid-range phone on a throttled connection |
| Cumulative Layout Shift | under 0.1 |
| Interaction responsiveness | under 200ms |
| Transferred weight, landing route | a few hundred KB; hero image well under 200KB |
| Fonts | at most two families, subset, `font-display: swap`, self-hosted |
| Third-party scripts on the critical path | zero |

- [ ] Measured on a throttled mobile profile, not on your laptop on office wifi.
- [ ] Hero image preloaded and sized; no layout shift as fonts and images land.
- [ ] Caching headers and compression are on; the build has no unused CSS or JS shipping to production.

### 5.9 Security and operations

- [ ] HTTPS everywhere, valid certificate, auto-renewal confirmed.
- [ ] Admin, staging, and preview environments are not publicly indexable and are password-protected.
- [ ] No secrets in the client bundle or the repository; environment variables checked.
- [ ] Backups exist and a restore has been tested at least once.
- [ ] DNS records documented, with TTLs lowered ahead of launch day if you are cutting over.

**Gate for phase 5.** Every box above is ticked or listed on the accepted-gaps document with an owner and a
date. "We will fix that after launch" is acceptable only when it is written down.

## Phase 6 — Launch day

Launch is a procedure, not an event. Do it early in your working day, never on a Friday afternoon, and never
the day before someone leaves for holiday.

**T-1 day**

1. Freeze content changes. Take a full backup of the current site if one exists.
2. Lower DNS TTLs (an hour or less) so a rollback propagates quickly.
3. Re-run the full QA sweep on the exact build you intend to ship.
4. Confirm the redirect map from old URLs, line by line, against a list.
5. Post the rollback plan where the team can see it: what "bad" looks like, who decides, how to revert.

**T-0, in order**

1. Deploy. Confirm the build that went out is the build you tested (check a commit hash or version string).
2. Load the site **logged out, in a private window, on a phone on mobile data** — not on the office network,
   not with your admin session. This catches cached, personalised, and permission-gated differences.
3. Verify the top ten URLs return 200 and render the intended content. Verify one deliberately wrong URL
   returns a styled 404.
4. Check `robots.txt` and `sitemap.xml` on the live domain. This is where the "block everything" mistake gets
   caught, and it is the single most expensive launch bug.
5. Submit the sitemap in Search Console and the Bing equivalent; request indexing on your handful of priority
   URLs.
6. Submit a real form. Confirm it arrives. Do this on production, not staging.
7. Complete the primary conversion yourself end to end, including any payment, then confirm the event
   appears in analytics and the record appears in the payment system.
8. Paste the home page URL into a messaging app and a social composer; confirm the share preview renders.
9. Turn on uptime monitoring against production and confirm the first successful check.
10. Only now, announce.

**T+24 hours**

- Re-check indexing status, the error log, and the form inbox.
- Read the first sessions or replays with genuine curiosity — the first day of real strangers is the highest
  information density you will ever get.
- Fix breakage only. Resist redesigning on day one; you do not yet have signal, and you will destroy your
  baseline.

**Rollback triggers, decided in advance:** the primary conversion path is broken, forms do not deliver, a
privacy or legal page is wrong, the site is unreachable for a segment of users, or a payment flow charges
incorrectly. Any of these means revert first and diagnose after.

## Phase 7 — The first 30, 60, and 90 days

| Window | Focus | Concrete work | What "good" looks like |
|---|---|---|---|
| **Days 1–30** | Truth-gathering | Watch sessions; run two five-user tests; read every inbound message; fix breakage and confusion only | You can name the top three points of confusion in the buyer's own words |
| **Days 31–60** | The biggest leak | Compute the funnel ratios; pick the weakest stage; make one large, pre-registered change; add the first supporting content | One stage ratio improved and it is logged, not just felt |
| **Days 61–90** | Compounding | Publish against the keyword map on a rhythm you can sustain; build internal links; strengthen proof with real customer material; revisit pricing presentation with real objection data | Non-brand organic sessions are rising, and the experiment log has entries with decisions |

**Rules for the first 90 days**

- **One meaningful change at a time**, each with a stated expectation and a measurement window. Two
  simultaneous changes produce one uninterpretable result.
- **Do not redesign in month one.** Almost every early redesign impulse is discomfort with strangers'
  behaviour, not evidence.
- **Do not add pages faster than you can keep them true.** A thin page with a wrong price costs more than a
  page that does not exist.
- **Re-run the conversion audit monthly** on the top three pages; drift is real and invisible.
- **Keep the honesty rails under review.** Growth pressure is exactly when the fake countdown gets proposed.

## The ordering rules teams break most often

| Rule | What happens when it is broken |
|---|---|
| Tokens before pages | Every page invents its own spacing and greys; changes become archaeology |
| Keyword-to-URL map before content | Two pages compete for one term and both underperform |
| Positioning before design | A beautiful site that describes nobody in particular |
| Real content before layout polish | The layout gets designed around text that will not exist |
| Measurement before launch | The first, most informative week of data is lost forever |
| Legal and privacy before launch | You ship a claim about data handling that is not true |
| Redirect map before switching domains | You lose accumulated search equity permanently |
| One primary conversion before building CTAs | Every section proposes its own next step and none of them wins |

## Apply it

- [ ] The scope was decided deliberately against §0.1 — what is being cut for v1 is written down with an
      owner and a date, and nothing from the "never cut" list is on it.
- [ ] The brand brief is complete and a stranger can restate the offer correctly from it alone.
- [ ] The six legal questions in §5.2 are answered in writing, the data inventory exists, and the privacy
      policy was redlined against it rather than pasted.
- [ ] Design tokens exist in code and no page hard-codes a colour or spacing value.
- [ ] The home page and the offer page were built first and both pass the conversion audit on two viewports.
- [ ] A page brief exists for every page before it is built.
- [ ] One primary keyword per URL is mapped in a checked-in table, with no two pages competing.
- [ ] Structured data validates as one connected graph, and `sitemap.xml`, `robots.txt`, and `llms.txt` agree.
- [ ] The primary conversion event was observed firing in a real browser on a phone.
- [ ] Every section of the pre-launch QA sweep is green, or the exception is written down with an owner.
- [ ] Forms were submitted on production and the messages arrived in a human inbox.
- [ ] The share preview was checked by pasting the URL into a real messaging app.
- [ ] Accessibility passes: contrast, keyboard traversal, visible focus, reduced motion, one H1 per page.
- [ ] A performance budget is written down and was measured on a throttled mobile profile.
- [ ] The launch-day runbook was followed in order, including the logged-out check on mobile data.
- [ ] Rollback triggers were agreed before launch, and everyone knows who decides.

## Related

- [../00-START-HERE.md](../00-START-HERE.md) — the five decisions and the definition of done
- [14-measurement-and-experimentation.md](14-measurement-and-experimentation.md) — what to instrument in phase 4
- [16-prompt-pack.md](16-prompt-pack.md) — prompts for driving an agent through each phase
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the gate for phases 2 and 5
- [../build/09-design-system-and-tokens.md](../build/09-design-system-and-tokens.md) — the phase 1 deliverable
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — what to build in phase 2
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — the phase 3 wiring
- [../templates/brand-brief.md](../templates/brand-brief.md) — the phase 0 deliverable
- [../templates/page-brief.md](../templates/page-brief.md) — required before any page in phase 2
