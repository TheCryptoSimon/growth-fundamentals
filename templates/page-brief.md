# Page Brief — `<<PAGE NAME>>`

The one-page spec an agent or a writer needs *before* building any single page. Copy it per page into
`docs/page-briefs/<slug>.md`. Scope creep in a build is almost always an under-specified brief, not a weak
builder — so fill this in first and refuse to start without it.

> **Status:** `<<DRAFT | APPROVED>>` · **Owner:** `<<NAME>>` · **Date:** `<<YYYY-MM-DD>>` ·
> **Brand brief version this inherits from:** `<<v1>>`

---

## 1. Identity

| Field | Value |
|---|---|
| URL / slug | `<<https://example.com/slug>>` |
| Page type | `<<home | product | pricing | comparison | audience | problem | glossary | article | about | contact | legal>>` |
| Template | `<<which layout template it uses>>` |
| Priority | `<<core | supporting>>` |
| Replaces / redirects from | `<<old URL, or n/a>>` |

**The page's job, in one sentence.** What it must accomplish for the business. If you need "and", it is
probably two pages.
`<<...>>`

**The one thing a reader should do next.** `<<...>>`

**What this page is deliberately NOT for.** The job it hands off to another page.
`<<...>>`

---

## 2. Audience and intent

*How to fill this in: describe the person arriving on this specific page, which is rarely the same as the
brand's primary buyer at every stage. Someone landing on a comparison page has already decided the category
is worth buying; someone landing on a problem page has not.*

| Field | Value |
|---|---|
| Who arrives here | `<<...>>` |
| Where they came from | `<<search / internal link / ad / referral>>` |
| What they already know | `<<...>>` |
| What they are afraid of | `<<...>>` |
| Search intent | `<<informational | commercial | transactional | navigational>>` |
| Stage in the funnel | `<<reach / visit / engaged / lead / customer>>` |
| Energy target for this page | `<<inherit from brand brief §8, or state the deviation and why>>` |

**The question in their head when they land:**
`<<"...">>`

---

## 3. Search

*How to fill this in: one primary keyword per URL, always. Two pages competing for one term means both
underperform. Do not record search volumes or difficulty scores you cannot verify — reason from intent.*

| Field | Value |
|---|---|
| Primary keyword | `<<one, exactly>>` |
| Secondary terms (support, never compete) | `<<...>>` |
| Which existing page could this cannibalise | `<<page + how this brief avoids it>>` |
| Title tag (`<<n>>` chars) | `<<captures the searched term>>` |
| Meta description (`<<n>>` chars) | `<<the reason to click, not a summary>>` |
| H1 (visible, may differ from title) | `<<holds the brand's own frame>>` |
| Canonical URL | `<<...>>` |
| Indexable | `<<yes | no + reason>>` |

**The rule this encodes:** capture the searched term in the title and metadata; hold your real positioning in
the body. See [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md).

---

## 4. The direct-answer paragraph

*How to fill this in: 40–70 words, inside the first screen, self-contained enough to be quoted with no
surrounding page and still be true. This is the single highest-value element for being cited by AI answer
engines, and it doubles as the clearest thing a hurried human reads.*

**Question this page answers:** `<<...>>`

**Direct answer (draft it here, verbatim as it will appear):**
> `<<Answer the question in the first sentence. No preamble. Name the brand once, naturally. Plain
> declarative sentences. Every fact checkable.>>`

**Marked as speakable in schema:** `<<selector>>`

---

## 5. Section outline

*How to fill this in: one job per section, in the order a sceptical reader needs them. Objections come before
the ask, never after it. If a section has no job, delete it — a section that exists because the page "looked
short" costs more than the whitespace it replaced.*

| # | Section | Its single job | Key content | Proof / mechanism used |
|---|---|---|---|---|
| 1 | Hero | Say what it is, who for, what to do | `<<headline + subhead + CTA>>` | `<<...>>` |
| 2 | `<<...>>` | `<<...>>` | `<<...>>` | `<<...>>` |
| 3 | `<<...>>` | `<<...>>` | `<<...>>` | `<<...>>` |
| 4 | `<<...>>` | `<<...>>` | `<<...>>` | `<<...>>` |
| 5 | `<<...>>` | `<<...>>` | `<<...>>` | `<<...>>` |
| 6 | FAQ | Discharge the remaining objections | `<<4–8 real questions>>` | `<<...>>` |
| 7 | Closing ask | One action, restated | `<<CTA + microcopy>>` | `<<...>>` |

**Heading outline** (exactly one H1; H2s carry the point rather than labelling the section):
```
H1  <<...>>
  H2  <<...>>
    H3  <<...>>
  H2  <<...>>
  H2  <<...>>
```

---

## 6. Proof elements

*How to fill this in: every claim on this page needs a mechanism next to it and a real source behind it. If
the proof does not exist, mark it and either cut the claim or delay the page. Never ship a placeholder
testimonial; placeholders have a way of becoming production.*

| Claim on this page | Mechanism stated next to it | Proof source (real, checkable) | Status |
|---|---|---|---|
| `<<...>>` | `<<...>>` | `<<...>>` | `<<HAVE | [PROOF NEEDED]>>` |
| `<<...>>` | `<<...>>` | `<<...>>` | `<<HAVE | [PROOF NEEDED]>>` |
| `<<...>>` | `<<...>>` | `<<...>>` | `<<HAVE | [PROOF NEEDED]>>` |

**Proof formats used on this page:** `<<customer account | worked example | demonstration | credential |
methodology explanation | third-party verification>>`

**Explicitly absent:** `<<no ratings, no counts, no logos — we do not have verified ones>>`

---

## 7. Objections to answer

*How to fill this in: in the order a real buyer raises them. Each one gets a location on the page, before the
ask. A two-sided line — who this is not for — raises credibility and self-selects the right reader.*

| # | Objection (their words) | Answered in section | Our honest answer |
|---|---|---|---|
| 1 | `<<"...">>` | `<<...>>` | `<<...>>` |
| 2 | `<<"...">>` | `<<...>>` | `<<...>>` |
| 3 | `<<"...">>` | `<<...>>` | `<<...>>` |

**"Not for you if..." line, and where it sits:** `<<...>>`

---

## 8. The call to action

*How to fill this in: one primary CTA for the whole page, repeated as needed but never competing with a
second solid button. The microcopy underneath usually does more work than the label.*

| Field | Value |
|---|---|
| Primary CTA label (the outcome, not the mechanic) | `<<...>>` |
| Destination | `<<...>>` |
| Microcopy under it (pre-answers the friction question) | `<<...>>` |
| Analytics event + properties | `<<cta_clicked {location, label, destination}>>` |
| Appears in sections | `<<...>>` |
| The one quiet secondary action | `<<... | none>>` |

**Friction check.** What does the reader fear happens when they click, and does the microcopy answer it
before they have to wonder?
`<<...>>`

---

## 9. Internal links

*How to fill this in: name specific existing URLs, not categories. A page with no inbound internal links is
an orphan; a page with no outbound links is a dead end. Anchor text should describe the destination, never
"click here" or "learn more".*

**Links IN — pages that will link to this one (and from where in them):**

| Source page | Section it links from | Anchor text |
|---|---|---|
| `<<...>>` | `<<...>>` | `<<...>>` |
| `<<...>>` | `<<...>>` | `<<...>>` |

**Links OUT — where this page sends people:**

| Destination | Why | Anchor text |
|---|---|---|
| `<<hub / parent page>>` | `<<...>>` | `<<...>>` |
| `<<sibling>>` | `<<...>>` | `<<...>>` |
| `<<conversion page>>` | `<<...>>` | `<<...>>` |

---

## 10. Structured data

| Field | Value |
|---|---|
| Primary node type(s) | `<<...>>` |
| Always also | `WebPage`, `BreadcrumbList` |
| FAQ schema | `<<yes — from the on-page FAQ array, one source | no>>` |
| Breadcrumb trail | `<<Home > Hub > This page>>` |
| Organisation `@id` referenced | `<<https://example.com/#organization>>` |
| Speakable selector | `<<...>>` |
| Ratings/reviews | **none** — we have no verified reviews, and inventing them is out of the question |

Validate before shipping. Structured data that contradicts the visible page is worse than none. See
[../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md).

---

## 11. Assets

| Asset | Spec | Status |
|---|---|---|
| Hero image | `<<subject, not a mood; sized, preloaded, alt text written>>` | `<<...>>` |
| OG / share image | `<<readable at thumbnail size; not text-heavy; matches page subject>>` | `<<...>>` |
| Other images | `<<alt text, dimensions, format>>` | `<<...>>` |
| Icons / diagrams | `<<...>>` | `<<...>>` |

**OG image note.** `<<what it shows and why it will still read at 300px wide in a chat app>>`

---

## 12. Acceptance criteria

*The builder does not get to call this page done until every line is demonstrably true. "Demonstrably" means
observed in a browser, not intended.*

- [ ] The page's stated job is achieved, and a stranger can restate it after five seconds on the first screen.
- [ ] Exactly one H1; heading order is hierarchical; H2s carry the point.
- [ ] One primary CTA per viewport; secondaries are visually quiet; no two competing solid buttons.
- [ ] Every claim has its mechanism next to it, and no `[PROOF NEEDED]` markers remain in published copy.
- [ ] The direct-answer paragraph sits within the first screen and reads correctly when quoted alone.
- [ ] Title, meta description, H1, and canonical are set and match this brief.
- [ ] No other page targets this primary keyword.
- [ ] Internal links in and out exist as specified, with descriptive anchor text.
- [ ] Structured data validates and matches the visible content.
- [ ] Verified at 375px and desktop: no horizontal scroll, clean console, no layout shift.
- [ ] Contrast passes AA including any text over images; keyboard traversal works with visible focus.
- [ ] Motion matches the energy target and honours reduced-motion preferences.
- [ ] The CTA event fires and was observed in analytics from a real browser.
- [ ] [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) passes end to end.
- [ ] Share preview renders correctly when the URL is pasted into a real messaging app.

**Measured by:** `<<which metric tells us this page works>>` · **Reviewed on:** `<<date>>`

---

## Apply it

- [ ] This brief was written and approved before any markup existed.
- [ ] The page has exactly one job and one primary keyword, and both are written down.
- [ ] Cannibalisation against an existing page was checked by name, not assumed.
- [ ] The direct-answer paragraph is drafted here, verbatim, before the page is built.
- [ ] Every section in the outline has a stated job; sections without one were deleted.
- [ ] Every claim has a real proof source, or is marked and excluded from the published version.
- [ ] Objections are answered before the ask, and a "not for you if" line exists.
- [ ] One CTA, with its microcopy and its analytics event, is specified here.
- [ ] Internal links in and out name specific URLs and specific anchor text.
- [ ] The acceptance criteria were verified in a browser at both viewports before anyone called it done.

## Related

- [brand-brief.md](brand-brief.md) — the upstream source of truth this page inherits from
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — section recipes per page type
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the gate in the acceptance criteria
- [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md) — keyword-to-URL mapping and on-page rules
- [../search/12-geo-ai-search.md](../search/12-geo-ai-search.md) — writing the direct-answer paragraph
- [../search/13-schema-and-technical-wiring.md](../search/13-schema-and-technical-wiring.md) — the schema section
- [../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md) — headline and microcopy craft
- [../ops/16-prompt-pack.md](../ops/16-prompt-pack.md) — prompt P9 generates a first draft of this brief
