# Measurement and Experimentation

How to instrument a new brand's site so it tells you what to fix next, and how to learn from it without
lying to yourself. Read this before launch — the instrumentation decisions are cheap now and expensive
later — and again whenever you are tempted to say "we should A/B test it."

---

## 1. The rule that makes measurement worth doing

**A metric earns its place only if a specific person would do something different depending on its value.**
Everything else is decoration that costs attention every week forever.

Before adding any number to a dashboard, complete this row. If you cannot, delete the metric.

| Metric | Decision it changes | Threshold that triggers action | Who acts |
|---|---|---|---|
| Home → primary-CTA click rate | Rewrite the hero, or leave it alone | Below the rate we set as acceptable | Whoever owns copy |
| Non-brand organic sessions | Publish more, or fix indexing | Flat for two consecutive months | Whoever owns search |
| Trial → paid | Fix onboarding, or fix targeting | Falls versus the prior cohort | Whoever owns the product |

Two corollaries you will need to defend:

- **A number nobody owns is not measured, it is displayed.** Put a name against every metric.
- **Definitions are frozen for the quarter.** Redefining "engaged visit" mid-quarter destroys the only thing
  early-stage measurement has: comparability with last month.

## 2. One north-star metric, two or three inputs

**What it is.** The single number that goes up when the business is genuinely working, not when activity
merely increases.

**Mechanism.** Teams optimise what they report. A north star that measures *delivered value* pulls every
downstream choice toward the customer; a north star that measures *effort* (posts published, visits) pulls
toward theatre.

**Choosing it — four tests.** A good north star (a) rises only when a customer got real value, (b) can move
within one quarter, (c) is one number, not a composite index nobody can explain, and (d) cannot be gamed by
doing something you would be embarrassed to describe out loud.

| Business shape | Reasonable north star | Bad north star and why |
|---|---|---|
| B2B SaaS | Weekly active accounts that completed the core action | Signups — free signups can rise while the product fails |
| Online course | Learners who finished module three | Enrolments — measures marketing, not the product |
| Dental clinic | Booked appointments that were attended | Form submissions — no-shows look identical |
| Marketplace | Completed transactions with both sides rated | Listings — supply without demand is inventory, not a business |
| DTC kettle | Delivered orders net of returns | Add-to-cart — abandons and returns hide inside it |

**Then pick two or three input metrics** that mechanically produce the north star, and write the relationship
as an equation you can argue with. For example, for a course: *finishers ≈ enrolments × week-one start rate ×
week-three continuation rate.* Now you have three levers instead of one wish, and each one names a team.

**Rule.** One north star per company, two or three inputs, reviewed monthly. If you have five north stars,
you have none.

### Naming the dial

Measurement targets shift with the brand's energy setting (see
[../00-START-HERE.md](../00-START-HERE.md), decision 4).

| | Calm / premium / considered purchase | Energetic / impulse purchase |
|---|---|---|
| North star sits | Further down the funnel (retained customer, attended booking) | Nearer the transaction |
| Feedback loop | Weeks to months; do not judge a change in three days | Days; faster iteration is legitimate |
| A long session means | Serious evaluation — usually good | Confusion or friction — usually bad |
| Do not measure | Urgency-response; you are not running urgency | Depth-of-read as a primary metric |
| Success on a first visit | An informed *return*, not a same-session purchase | A same-session purchase |

## 3. The funnel, with exactly one metric per stage

Six stages. One metric each. The value of the funnel is not the numbers, it is the **ratios between adjacent
stages** — that is your leak map.

| Stage | The question it answers | The one metric | Instrument | The common lie |
|---|---|---|---|---|
| **Reach** | Did anyone encounter us? | Impressions (search) + reach (other channels) | Search Console, channel native | Counting the same person repeatedly as "reach" |
| **Visit** | Did they arrive? | Sessions, split brand vs non-brand | Analytics + Search Console query split | Brand and direct traffic inflating "growth" |
| **Engaged visit** | Did the page do its job? | Engaged-session rate, on an explicit definition | Analytics event | Redefining "engaged" until it looks good |
| **Lead / trial** | Did they raise a hand? | Primary conversion rate per session | One named conversion event | Counting three form types as one number |
| **Customer** | Did they pay? | Lead-to-customer rate | Payment system or CRM | Attributing every sale to the last click |
| **Retained** | Did it keep working? | Retention or repeat rate at a fixed horizon | Product or order data | Reporting cumulative totals, which only ever rise |

**Define "engaged visit" in writing and freeze it.** A workable definition for a marketing site: the session
scrolled past the first screen *and* lasted beyond a trivial threshold *and* fired at least one intentional
event (a click on an in-page link, a CTA, a pricing toggle, an FAQ open). Write the exact rule into the
events file so nobody re-invents it next quarter.

**Reading the leak — arithmetic illustration with placeholder numbers, not measured data:** say a month gives
10,000 impressions → 400 visits → 120 engaged → 12 leads → 3 customers. The weakest ratio, relative to what
that stage should plausibly do, is where the next change goes. Fixing the stage *before* the leak just sends
more people into the same hole.

**Rule.** Work the largest leak, not the most interesting one. Re-derive the leak monthly; it moves.

## 4. Event taxonomy: name things once, compare them forever

**Why it matters.** Event data is only useful in aggregate over time, and aggregation dies the moment two
people name the same action differently. Naming is not bureaucracy, it is the whole value.

**The convention.** `object_action`, lowercase, snake_case, past tense. `cta_clicked`, `form_submitted`,
`pricing_toggled`, `faq_opened`, `video_started`. Never `ClickedHeroButtonHomepageV2`.

**The rules, in priority order:**

1. **Name what happened, never where it happened.** Location goes in a property (`location: "hero"`), because
   pages get renamed and you still want the trend.
2. **Properties, not new event names.** One `cta_clicked` with `{location, label, destination}` beats nine
   events. Nine events means nine broken charts after the redesign.
3. **Cap the vocabulary at roughly a dozen for a new marketing site.** More events do not mean more insight;
   they mean nobody trusts any of them.
4. **No personal data in events, ever.** No emails, names, message text, or full URLs containing tokens.
   This is a legal exposure and a privacy-copy exposure at the same time.
5. **One event is the primary conversion.** Mark it in the registry. Everything else is context.
6. **The registry is a file in the repo** (`EVENTS.md`), and an AI agent may not invent an event that is not
   in it. Adding an event is a pull request, not a whim.

**The starter set for a new brand's site:**

| Event | Properties | Why it exists |
|---|---|---|
| `page_viewed` | path, referrer_group | Baseline; usually automatic |
| `engaged_session` | trigger | Stage-three metric, on the frozen definition |
| `cta_clicked` | location, label, destination | Which CTA and which position actually works |
| `form_started` | form_id | Separates "did not try" from "tried and failed" |
| `form_submitted` | form_id | Candidate primary conversion |
| `form_error` | form_id, field | The highest-value diagnostic on any site |
| `pricing_viewed` | — | Intent signal; also a funnel gate |
| `pricing_toggled` | interval, tier | Tells you whether the ladder is being explored |
| `faq_opened` | question_id | A free objection list, ranked by real demand |
| `outbound_clicked` | destination_group | Where you leak attention |
| `signup_completed` | plan | Usually the primary conversion |
| `error_shown` | code, path | Catches quiet breakage |

**Verification rule.** An event that has not been observed firing in a real browser does not exist. Test each
one once, from a phone, before launch.

## 5. The minimum stack, and the privacy trade-off

**What a new brand actually needs** — five things, none of them expensive:

| Layer | What it is | Skipping it costs you |
|---|---|---|
| First-party analytics | A cookieless, self-hosted or first-party-domain analytics tool | You are blind, or you outsource the blindness to a channel that grades its own homework |
| Search Console (+ the Bing equivalent) | Free, direct from the search engine | You cannot see indexing problems at all |
| Uptime + error monitoring | A ping on the home page and the primary form endpoint | You find out from a customer, weeks late |
| Form-delivery test | A scheduled real submission that must land in the inbox | The classic silent catastrophe: a live site whose contact form has delivered nothing for a month |
| Optional: session replay | Sampled recordings, privacy-masked | Slower discovery of unknown-unknowns; not fatal |

### The cookieless trade

A first-party, cookieless analytics tool sets no identifying cookie and shares nothing with an ad network. It
buys you three real things:

- **No consent banner in most jurisdictions** — which is also a conversion and trust win, not just a legal
  one. Every banner is an interruption placed between a stranger and your first sentence.
- **Privacy copy that is literally true.** If the site says it does not track you across the web, that has to
  be a fact about the code, not a wish. See the honesty rails in [../00-START-HERE.md](../00-START-HERE.md).
- **Lighter pages** — fewer third-party requests on the critical path.

What you give up, stated honestly:

| You lose | Practical consequence | Mitigation |
|---|---|---|
| Cross-device identity | A phone visit and a laptop purchase look like two people | Accept it; use a self-reported source question at signup |
| Multi-touch attribution | You cannot credit a journey across six touches | Use directional attribution plus incrementality tests (§12) |
| Remarketing audiences | No behavioural ad retargeting | If you later need it, you owe a consent banner and a copy change — decide deliberately |
| User-level cohorts | Weaker retention analysis from the site alone | Do retention analysis in the product or order data, where you have an account anyway |

**The rule that keeps this honest:** the moment you add a marketing pixel, you have changed what the site
does, which means the privacy page and the banner policy change in the same commit. No exceptions, no "we
will update the copy later."

## 6. Search Console: what its four numbers actually mean

Free, first-party, and the only place you see how search itself perceives you. Four headline metrics, each
routinely misread.

| Metric | What it actually is | What it is *not* | The decision it drives |
|---|---|---|---|
| **Impressions** | Times a URL appeared in results for some query | Views, or interest | Whether you are eligible at all; rising impressions with flat clicks means you match the wrong intent |
| **Clicks** | Actual visits from search | All your traffic | The only search number that reaches the site |
| **CTR** | Clicks ÷ impressions | Content quality | High position with poor CTR is almost always a title/meta problem — rewrite the snippet, not the page |
| **Average position** | A weighted average across every query, device, and country | Your "rank" | Almost nothing on its own; always split by query and page before acting |

**How to use it properly:**

- Work at the **query × page** level, never the site level. A site average blends a term you own with a term
  you have no business ranking for.
- Compare **28 days versus the previous 28**, not week to week. Search is noisy and weekly seasonal.
- The **indexing/coverage report matters more than rank** in the first months. A page that is not indexed has
  no position to improve.
- Queries you rank for but never intended are a **content map**: they tell you what the market thinks you
  are. Sometimes the right response is a new page; sometimes it is fixing your positioning.
- Search Console data is sampled and lagged by a couple of days. Do not reconcile it to the last click in
  your analytics; they measure different things and will never agree.

Deeper treatment in [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md).

## 7. Session replay and heatmaps: good eyes, bad statistics

**What they are.** Replay records anonymised sessions you can watch. Heatmaps aggregate clicks, scroll
depth, or attention into a coloured overlay.

**What they are genuinely good for** — finding the thing you did not know to ask about:

- Rage clicks on something that is not a link (a common, invisible, easily fixed frustration).
- Field-level form abandonment: which input people delete, retype, and leave on.
- Layout breakage on a device you do not own.
- Watching someone hunt for a price that you thought was obvious.

**The traps, which are severe:**

| Trap | What goes wrong |
|---|---|
| **Sampling** | Most tools record a subset. A "heatmap" from a sampled minority is not the population, and the sample is often biased toward longer sessions. |
| **Viewport blending** | Aggregating a heatmap across desktop and mobile averages two incompatible layouts into a picture of neither. Always split by device. |
| **Dynamic content** | Overlays misalign against accordions, carousels, and personalised blocks; the map shows clicks on a layout that never existed. |
| **Scroll-depth illusions** | Scroll maps flatter long pages and punish short ones; they measure page length as much as interest. |
| **The n=3 generalisation** | Watching three replays and declaring a pattern is the single most common misuse. |
| **Privacy** | Recordings can capture typed personal data. Masking must be on, verified, and mentioned in the privacy page. |

**Rule.** Use replay and heatmaps to *generate hypotheses*, never to *prove* anything. Never quote a heatmap
percentage in a decision document. If a replay suggests a problem, confirm it with an event count or a
five-user test before you rebuild anything.

## 8. Qualitative instruments, which beat analytics at low traffic

Analytics tells you *where* people stop. It never tells you *why*, and at low traffic it barely tells you the
where. Four cheap instruments carry most of the early learning.

| Instrument | Cost | Answers | Cannot answer |
|---|---|---|---|
| **Five-user usability test** | An afternoon | Where the site confuses a real human | How often it happens across everyone |
| **One-question exit survey** | A day to wire | Why this specific page failed | Anything about people who never scrolled |
| **Post-signup "what almost stopped you"** | One field | The objection your copy missed | Why non-signups left |
| **Sales and support notes** | Free, already happening | The real objection list, in the buyer's words | Whether it generalises beyond who contacted you |

**The five-user test.** Give five people from the target audience one realistic task ("find out whether this
works for a clinic your size, then start"), watch silently, and only ask "what are you thinking?" when they
go quiet. Usability research — the rule of thumb usually credited to Nielsen and Landauer — has long held
that a handful of participants surfaces most of the *problems* in an interface, because the serious problems
are the ones nearly everyone hits. Two cautions that matter more than the rule itself:

- It finds **problems**, not **rates**. Five users can tell you the pricing page confuses people. They cannot
  tell you what fraction of your traffic it confuses. Never turn five observations into a percentage.
- It only works if the task is real and you shut up. Explaining the page to the participant destroys the
  instrument.

**The exit survey.** One question, triggered on exit intent or after inactivity, on one page at a time.
"What were you hoping to find on this page?" outperforms "How was your experience?" — the first produces
usable sentences, the second produces politeness. Keep it out of the way on mobile.

**The five-second test.** Show a stranger the home page for five seconds, take it away, and ask what the
company does, who it is for, and what they were meant to do. It is the cheapest test in this document and
the one most likely to change your headline. See
[../brand/03-voice-messaging-and-copywriting.md](../brand/03-voice-messaging-and-copywriting.md).

## 9. A/B testing, honestly

**What a test really requires:** a metric chosen in advance, a sample size computed in advance, a stopping
rule fixed in advance, and enough traffic to reach that sample before the world changes underneath you. Miss
any of the four and you are not testing, you are generating stories.

### Minimum detectable effect

**MDE is the smallest true improvement your test can reliably notice.** It is chosen, not discovered, and it
drives everything: the smaller the effect you want to catch, the more traffic you need — and the relationship
is quadratic, so halving the MDE roughly quadruples the sample.

A standard planning approximation for a conversion-rate test (roughly 80% power, 95% confidence, two
variants) is **n per variant ≈ 16 × p × (1 − p) ÷ d²**, where `p` is the baseline rate and `d` the absolute
difference you want to detect. That is arithmetic, not an empirical claim, and it is enough to make the
decision honest:

| Baseline conversion | Detect +20% relative | Detect +50% relative | Detect +100% relative |
|---|---|---|---|
| 1% | ~40,000 per variant | ~6,300 per variant | ~1,600 per variant |
| 3% | ~13,000 per variant | ~2,100 per variant | ~520 per variant |
| 10% | ~3,600 per variant | ~580 per variant | ~140 per variant |

Double those for the total across both arms. Then compare against your real traffic.

**The decision rule.** If reaching the required sample takes more than four to six weeks, **do not run the
test.** Beyond that horizon, seasonality, campaigns, and your own other changes contaminate it, and you will
have spent six weeks not-shipping in exchange for a result you cannot trust.

### Peeking, and the stopping rule

Checking a running test repeatedly and stopping when it looks significant inflates false positives badly —
this is the most common way small teams get fooled, and it feels like diligence while it happens.

- Fix the **end date and sample size before starting**, and write them in the log.
- Run **whole weeks**, always. Weekday and weekend traffic behave differently; a Tuesday-to-Friday test
  measures the week, not the change.
- Expect a **novelty effect** — regular visitors react to change as change. If the audience is largely
  returning visitors, discount the first days.
- Check **sample-ratio mismatch**: if the split is meaningfully off 50/50, the assignment is broken and the
  result is void. Stop and fix the plumbing.
- Declare **one primary metric** plus **one guardrail** (typically a downstream metric such as refund rate or
  qualified-lead rate, so you do not "win" by attracting worse buyers).

### When a test is actually worth it

| Situation | Test? | Instead |
|---|---|---|
| Fewer than a few thousand relevant sessions a month | No | Sequential redesign and judgement (§10) |
| Small change (button wording, colour) at low traffic | No | Just apply the checklist rule; the effect is unmeasurable for you |
| Large change (whole hero, pricing structure, offer) with real traffic | Yes | Run it properly, whole weeks, one metric |
| A change you are contractually or ethically required to justify | Yes | Fixed horizon, pre-registered |
| Anything where the losing variant harms users | No | Do not experiment on harm |

**Never A/B test a dark pattern to see if it converts better.** It usually will, briefly. That is the reason
the rails in [../00-START-HERE.md](../00-START-HERE.md) sit above tactics, and the reason a guardrail metric
is mandatory.

## 10. What to do instead when traffic is small (which it is)

New brands almost never have test-grade traffic. This is not a handicap — it is a different method.

1. **Use the checklist as your prior.** [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md)
   encodes what usually works. At low traffic, applying a well-founded prior beats measuring a weak signal.
2. **Change one meaningful thing at a time, and make it big.** Sequential redesign: ship, wait a fixed window
   (a month is typical), compare like-for-like periods, keep or revert. You are accepting directional
   evidence deliberately, which is different from pretending you have proof.
3. **Pre-register the expectation.** Before shipping, write what you expect to move, in which direction, and
   by roughly how much. This one habit prevents most retrospective self-deception, because you will notice
   when you are explaining away a miss.
4. **Prefer stage ratios to totals.** Totals move with traffic. If the visit-to-engaged ratio improved while
   traffic was flat, something real probably happened.
5. **Buy evidence with five users, not with statistics.** A qualitative session costs an hour and answers
   *why*; an underpowered test costs a month and answers nothing.
6. **Use a reversal test when a result surprises you.** Put the old version back for a window. If the effect
   disappears and returns, you have something. If nothing changes, you had noise.

**State this posture out loud in the experiment log:** "Directional, not statistically significant." A team
that says that stays honest. A team that says "we saw a lift" from 200 sessions builds a strategy on noise.

## 11. The experiment log

One file, append-only, one block per change. It exists so that in eight months nobody re-runs a thing you
already learned, and so that "we tried that" comes with a date and a result.

```
ID: EXP-014
Date shipped: 2027-03-04        Window: 2027-03-04 → 2027-04-01 (4 weeks)
Stage: engaged visit → lead
Hypothesis: Leads are low BECAUSE the form asks for company size before we
  have earned it; removing it lowers imagined effort.
Change: Contact form reduced from 6 fields to 3. Nothing else changed.
Primary metric: form_submitted ÷ form_started
Guardrail: share of leads marked qualified by sales (must not fall)
Expected: primary up, meaningfully; guardrail flat
Method: sequential (not powered for a test) — directional evidence only
Result: primary rose; guardrail unchanged; traffic flat over both windows
Decision: KEEP
Learned: Field count was the friction, not form length per se. Next: test the
  same reduction on the demo request form.
Links: commit abc1234 · brief docs/page-briefs/contact.md
```

**Rules.** Log the failures and the inconclusive ones — those are the entries that save the most time later.
Log the *reason* in "because" form, so the log accumulates a model of your buyer rather than a list of
tweaks. One change per entry; two changes in one window is one entry with an honest note that you cannot
attribute the result.

## 12. Attribution, and how to stay sane about it

**The core problem.** People encounter a brand several times, on several devices, across weeks, and most of
those encounters are invisible to any measurement tool you can afford. Attribution models allocate credit
with confident-looking precision to data that is fundamentally incomplete.

| Model | Systematically over-credits | Systematically under-credits |
|---|---|---|
| Last click | Capture channels: brand search, direct, retargeting | Everything that created the demand |
| First click | Discovery channels | Everything that closed |
| Any multi-touch model | Whatever it can see | Word of mouth, podcasts, offline, private shares |

**Structural blind spots you cannot fix with a better tool:** links shared in private messages and group
chats land in "direct"; privacy features strip referrers; cross-device journeys break; and the strongest
channel for a considered purchase — someone recommending you in a conversation — leaves no trace at all.

**A sane practice:**

- Ask **"How did you hear about us?"** as an optional free-text field at signup or booking. It is biased and
  imprecise, and it will still tell you things no analytics tool can. Treat it as directional and read the
  actual sentences, not just the categories.
- Use analytics attribution to answer **"where is this coming from, roughly"** — not to allocate budget to
  two decimal places.
- For channel decisions with real money behind them, use **incrementality**: turn a channel off in one region
  or for a period and see whether total conversions move. It is the only method that answers "would this have
  happened anyway."
- **Tag your own campaigns consistently** with a documented convention, so at least the traffic you control
  is identifiable.
- Accept that the sum of channel-claimed conversions will exceed your real conversions. Reconcile to the
  payment system, and treat channel dashboards as claims, not accounts.

**The posture:** a number you know is approximate, used for direction, beats a precise number you quietly
know is wrong.

## 13. The review cadence

Measurement without a recurring meeting decays into a dashboard nobody opens.

| Rhythm | Length | Questions to answer, in order |
|---|---|---|
| **Weekly** | 30 min | 1. Did anything break (uptime, forms delivering, events firing, console clean)? 2. What shipped, and is it in the log? 3. Which funnel ratio moved, up or down? 4. What is the one experiment or change running now? |
| **Monthly** | 90 min | 1. North star and the two or three inputs versus last month. 2. Where is the largest leak now, and is it the same as last month? 3. What did the five-user tests and exit surveys say, in the customers' words? 4. Search: which queries gained impressions, and does a page own each of them? 5. What did we learn that changed our model of the buyer? 6. What are we stopping? |
| **Quarterly** | Half a day | 1. Is the north star still the right one? 2. Do the metric definitions still mean what they meant in January? 3. What did the experiment log teach us that we have not yet applied everywhere? 4. Re-run the full conversion audit on the top three pages. 5. Are the honesty rails intact on the live site, not just in intent? |

**Meeting rule.** Every review ends with one decision and one owner. A review that ends with observations is
a newsletter.

## 14. Anti-patterns

| Anti-pattern | Why it is corrosive |
|---|---|
| A dashboard with no owner | Nobody acts; everybody feels informed |
| Reporting cumulative totals | They only ever rise; they cannot indicate a problem |
| Redefining a metric mid-quarter | Destroys the comparison, usually right when it turns bad |
| Quoting a lift from an underpowered test, or picking the window after seeing the data | Builds strategy on noise, and institutionalises it |
| Time-on-page as a marketing-site success metric | Rewards a page that is hard to understand |
| Tracking personal data "just in case" | Legal exposure, and it makes your privacy copy false |
| A vanity chart in an investor update that you do not use internally | If it does not drive your decisions, it should not drive theirs |

## Apply it

- [ ] One north star is written down, with two or three input metrics and the equation connecting them.
- [ ] Every dashboard metric has a named owner and a stated threshold for action.
- [ ] The six funnel stages each have exactly one metric, and "engaged visit" is defined in writing and frozen.
- [ ] `EVENTS.md` exists, uses `object_action` naming, caps the vocabulary, and marks one primary conversion.
- [ ] Every event has been observed firing in a real browser, on a phone, before launch.
- [ ] Analytics is first-party and cookieless, or the consent banner and privacy copy match reality exactly.
- [ ] Search Console and its Bing equivalent are verified, and a scheduled test submission proves the
      primary form still delivers to a human inbox.
- [ ] Replay and heatmaps, if used, are privacy-masked, split by device, and used only for hypotheses.
- [ ] A five-user test has been run on the two most important pages and the notes exist.
- [ ] Before any A/B test: required sample computed, end date fixed, one primary metric, one guardrail.
- [ ] Below test-grade traffic, changes ship as pre-registered sequential redesigns and are labelled directional.
- [ ] The experiment log records failures and inconclusive results, not only wins.
- [ ] The weekly and monthly reviews are in the calendar, and each ends with one decision and one owner.

## Related

- [../00-START-HERE.md](../00-START-HERE.md) — the five decisions, the three engines, and the honesty rails
- [15-launch-checklist-and-build-order.md](15-launch-checklist-and-build-order.md) — where measurement sits in the build order
- [16-prompt-pack.md](16-prompt-pack.md) — the monthly performance-review prompt
- [../build/10-conversion-audit-checklist.md](../build/10-conversion-audit-checklist.md) — the prior to apply when you cannot test
- [../build/08-page-architecture-and-section-recipes.md](../build/08-page-architecture-and-section-recipes.md) — the pages these metrics grade
- [../search/11-seo-fundamentals.md](../search/11-seo-fundamentals.md) — reading search data properly
- [../templates/page-brief.md](../templates/page-brief.md) — where a page's acceptance criteria and metric are recorded
