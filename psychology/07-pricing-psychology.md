# Pricing Psychology

How to choose the number, and how to show it. Read before designing a pricing page, a checkout, a
plan lineup, or any promotion; it assumes you already know who you sell to and what category you
claim. A synthesis of consumer-psychology research (Nick Kolenda's body of work, Cialdini,
behavioural-economics pricing literature) rewritten as build rules. No invented figures anywhere.

---

## 0. Two jobs, never confuse them

| Job | Question | Decided by | Failure mode |
|---|---|---|---|
| **Set the number** | What will people actually pay? | Surveys, Van Westendorp, price ladders, tests | Cost-plus pricing that ignores value |
| **Present the number** | How does the number feel? | Layout, type, order, wording | A correct price that reads as expensive |

Presentation cannot rescue a badly-set number; a well-set number can be destroyed by presentation.
Number first, page second.

## 0.1 Name the dial before you start

Almost every tactic below flips with the brand's end of the spectrum. Decide once, record it in the
brand brief, apply consistently.

| | **Calm / premium / trust end** | **Energetic / urgent / deal end** |
|---|---|---|
| Price digits | Round ($40, $120) | Charm ($39, $39.99) |
| Discounting | Rare, shallow, or never — value-adds instead | Frequent, visible, seasonal |
| Price type size | Small; the tier name dominates | Larger; the number is part of the pitch |
| Colour on price | Same ink as body text | Contrast colour on the sale price |
| Scarcity | Real capacity or cohort, stated plainly | Real deadlines, stated loudly |
| Motion | None | Allowed, still no fake timers |
| Guarantee tone | Quiet, unconditional | Loud, headline-level |

**Rule:** any tactic that raises arousal (bright price colour, exclamation marks, "hurry", stacked
badges) belongs to the right column only. On a calm brand do the inverse, and spend your one loud
element on the primary CTA.

## 1. Value-based pricing, not cost-plus

**What it is.** Price from what the outcome is worth to the buyer, not from your cost plus a margin.

**Mechanism.** Buyers never see your cost base. They compare your price to a *reference set* — what
they paid before, what the nearest alternative costs, what they expected, what doing nothing costs.
Cost-plus produces a number unrelated to that set: usually too cheap for the strong segment and
irrelevant to the weak one.

**How to apply — the value frame worksheet:**

| Line | Example (B2B scheduling SaaS) |
|---|---|
| Next-best alternative the buyer would really use | A shared spreadsheet + an admin's time |
| What that alternative costs them per month | Hours of admin time, plus missed bookings |
| Where you are measurably better | Fewer no-shows, no double-booking |
| Value gap (their cost − your cost to them) | The room your price lives in |
| Your price | A defensible share of that gap, never all of it |

Three rules: **(1) Anchor to the right category** — a dental clinic's whitening package competes
with cosmetic spend, not toothpaste; choosing the comparison category is a pricing decision, see
[positioning](../brand/01-positioning-and-category.md). **(2) Leave visible surplus** — capturing
the whole gap maximises one sale and kills renewal. **(3) Cost only sets the floor** — if the
value-based price sits below cost plus target margin, the problem is the product or the segment,
not the pricing page.

## 2. Finding willingness to pay

### Why "would you pay $X?" fails
It asks people to predict their own future behaviour with nothing at stake; answers drift toward
politeness and toward whatever number sits in the question. Indirect and choice-based methods are
consistently more predictive. **Never set a price from a direct WTP question.**

### Method picker

| Your situation | Method | Output | Effort |
|---|---|---|---|
| Few products, low traffic (new SaaS, service) | Van Westendorp | An acceptable price band | Low |
| Few products, need a revenue-maximising point | Gabor-Granger | Demand + revenue curve | Low-medium |
| Price interacts with features/packaging | Conjoint (choice-based) | Value of each feature *and* of price | High |
| Few products, high traffic | Split test | The winning live price | Medium |
| Many products, lots of transaction history | Demand curve from own sales data | Revenue-maximising point per line | Medium |
| Nothing yet, need a starting number | Category heuristics + a price ladder in sales calls | A defensible v1 | Very low |

Always **segment first**. Cross-tab every result by who answered (role, company size, use case).
Two segments with different WTP is the argument for two tiers, not for one averaged price.

### Van Westendorp, in practice
Ask four price-perception questions about the same described product:

1. So cheap you'd doubt the quality → **Too cheap**
2. A bargain, good value → **Cheap**
3. Starting to feel expensive → **Expensive**
4. So expensive you'd never consider it → **Too expensive**

Convert to cumulative percentages per price point and plot four curves. Read the crossings:

| Crossing | Name | Use |
|---|---|---|
| Too cheap × Expensive | Point of marginal cheapness | Lower bound — below this, quality doubt |
| Cheap × Too expensive | Point of marginal expensiveness | Upper bound — above this, refusal |
| Too cheap × Too expensive | Optimal price point | Balance of the two rejection reasons |
| Cheap × Expensive | Indifference price | Often near the category norm |

Ship a price inside the bound-to-bound band, then test within it. Shape beats any single crossing:
a **wide** band means price isn't the deciding factor (positioning is); a **narrow** band means the
category has a hard norm you must justify moving outside.

### Gabor-Granger and price ladders
Show each respondent a sequence of prices, record buy / no-buy at each. Share-who-buys ×
(price − unit cost) gives a revenue curve; its peak is your candidate. The same logic works with no
survey tool: in sales calls, quote a price, note the reaction, move up one rung until reactions
turn. Keep a written ladder so the sample stays comparable.

**Honesty rail:** research inputs are directional and private. Never publish them as claims
("customers say we're worth X"). Use them to choose a price, not as copy.

## 3. Anchoring

**What it is.** The first or highest number in view becomes the yardstick for everything below it.

**Mechanism.** Prices are judged against a visible range, not absolutely. Widen the top of the
range and the middle re-reads as moderate — the number did not change, the range did.

**How to apply — honest anchor inventory:**

| Anchor | How to build it honestly | Fits which end of the dial |
|---|---|---|
| Premium tier | A tier you genuinely sell and support | Both |
| Cost of the status quo | Quantified from the buyer's own numbers | Calm/premium |
| Category comparison | "Less than one hour of an agency's time" — true, checkable | Calm/premium |
| Bundle component value | Only if each component is separately purchasable at that price | Both |
| Former price | Only if it was the real price for a real period | Energetic |

**Order of presentation** — the highest-leverage free win on any pricing page:
- **Value before price.** A price met before any benefit is compared to zero, which is sticker
  shock. Outcome, proof and objection-handling go above the price — see
  [page architecture](../build/08-page-architecture-and-section-recipes.md).
- **Anchor first, target second.** In a vertical sequence, put the higher option above the target.
  In a three-card row, left-to-right reading makes descending prices feel engineered; instead let
  the premium card win attention by emphasis so it is *seen* first.
- Keep old and new price **horizontally** adjacent with a little space between; a vertical stack
  doesn't read as distance.

**The generalisation trap.** An expensive item helps when buyers compare items to each other (a
marketplace, a catalogue). It hurts when they form one summary impression of the brand — which is
what happens on a single-product pricing page and on any first visit: the top tier raises the
perceived average and every tier feels dearer. Test: *would a first-time visitor describe us by our
top price?* If yes, keep the top tier plausible or add an entry tier to pull the mean down.

## 4. The decoy (asymmetric dominance)

**What it is.** A third option, close to your target but clearly worse on one dimension, that makes
the target the obviously rational pick.

**Mechanism.** Choices are made by comparison, not absolute valuation. An option dominated by the
target on price-or-features gives the buyer an easy comparison to "win", and the target inherits
the win. Related: with three options, buyers gravitate to the middle, because each extreme carries
an obvious objection.

**How to build an honest one:**

| Rule | Why |
|---|---|
| The decoy must be a real, purchasable, supportable option | Otherwise it is a fake option — that is deception |
| Someone must be able to rationally want it | A niche buyer picking the decoy is the proof it is honest |
| Difference must be a real difference (seats, volume, support), not a fabricated restriction | Manufactured crippling is a tax on the buyer |
| Never hide the decoy's disadvantage in fine print | The comparison must be readable at a glance |

*Generic example (online course):* self-paced $X · self-paced + graded assignments $X+40 ·
self-paced + graded assignments + monthly live Q&A $X+50. The middle is dominated on
value-per-dollar, so the third reads as the sensible pick — and the middle is still a real product
a buyer who hates live calls will happily choose.

**Where the line is.** Legitimate: making a genuinely better deal easy to see. Manipulative:
inventing an option nobody can buy, degrading a plan purely to sell another, or listing one you'd
refuse to fulfil.

## 5. Tier design: good-better-best

**How many.** Three visible tiers, plus at most one "talk to us" tier for bespoke work. One price
gives no comparison and forces a buy/don't-buy decision; four or more cause comparison fatigue and
push buyers to defer.

| Tier | Its job | Contents rule | Do NOT put here |
|---|---|---|---|
| **Entry** | Make the category affordable; pull the perceived average down; qualify serious buyers | The complete core outcome at the smallest scale | Cripple-ware; missing the thing the product is *for* |
| **Target** (centre) | Where you want most revenue | Everything a typical buyer needs, plus the one feature they'd feel silly missing | Every feature — leave the premium tier a reason to exist |
| **Premium** | Anchor the range; serve the heavy segment | Scale (seats, volume, priority), not novelty | Features the target buyer will feel punished for lacking |

- **Scale on one dimension** — seats, volume, or usage — an axis buyers can self-place on. Tiers
  differing on many unrelated axes can't be compared, so buyers stall.
- **Differentiator first** in each feature list: lead with what this tier adds, don't re-list
  everything inherited before the difference.
- **Equal-height cards, identical feature order.** Any misalignment reads as a real difference.
- **Centre-stage the target.** The middle of a three-card row collects the most looks, and
  attention feeds preference.
- **Isolate it** with exactly one device — slight elevation, a border, or one honest badge. A card
  that is bigger *and* louder *and* coloured *and* badged reads as advertising, not as the choice.
- **Badges must be true.** "Most popular" only if it is; otherwise a factual label or nothing.

**Naming the tiers so the name outranks the number** — the name is read first and frames the price.

| Naming style | Examples | Effect | Use when |
|---|---|---|---|
| Primitive / functional | Starter, Basic, Standard, Team | Feels affordable and normal; suggests a social default | You want volume in the mid tier; calm brands |
| Prestige / metallic | Silver, Gold, Platinum | Feels expensive; buyers tend to settle *lower* in the ladder | Rarely — mostly when you must justify a high top price |
| Job-to-be-done | Solo, Studio, Agency | Buyers self-select by identity, price becomes secondary | Almost always the strongest option |

Job-to-be-done naming is the default: it turns "how much do I want to spend" into "which one am I",
a question buyers can answer confidently.

## 6. Presentation rules (the visual grammar of a price)

**Mechanism.** Visual magnitude bleeds into numeric magnitude — what *looks* small reads as small.
Reading order sets the reference frame. Grouping merges meaning: whatever sits beside the price
infuses it.

| Rule | Concrete setting |
|---|---|
| Tier name ≥ price in visual weight | Name at heading size; price one step below |
| Currency symbol smaller than digits | Symbol ~60–70% of digit size, superscript-aligned, slight gap |
| Benefit-first, price-last card | Order: name → outcome line → feature list → price → CTA |
| One primary CTA per card | Target card solid; other cards ghost/outline; never two solid buttons |
| Price nearer the left, button nearer the right | Small numbers associate with the left; the action sits where the hand is |
| Small-words adjacency | "from", "just", "only" adjacent to the price — but only if literally true |
| Whitespace around the price | Crowding reads as cheap and raises effort |
| Billing cadence unambiguous | "$29 / month, billed monthly" — never let annual-equivalent pricing hide the real charge |
| Old vs new price | Horizontal, small gap, strike-through on the old, both legible |

**Dial inversions:** on the energetic end the price may be the card's largest element, may carry a
contrast colour, and the sale price may outsize the original. On the calm end keep it in body ink
at a modest size and let the tier name and outcome line carry the card. Never put alarm-red on a
price for a trust-first brand — see [colour and typography](./06-color-and-typography.md).

## 7. Round, charm, precise — and the left digit

| Form | Example | Signals | Use for |
|---|---|---|---|
| **Round** | $40, $1,200 | Fluent, confident, emotional, premium, "stable" | Hedonic and identity purchases; premium brands; anything bought on feeling |
| **Charm / just-below** | $39, $39.99 | A deal; value; volume retail | Price-led offers, commodity goods, comparison shopping |
| **Precise** | $38.60, $1,247 | Calculated, justified, "we did the maths" | Analytical/reasoned purchases, B2B quotes, negotiations, large sums |
| **Parity** | Matched to a known competitor | Neutralises price as a variable | When you win on another axis and want price off the table |

**The left-digit effect.** Buyers encode magnitude from the leftmost digit onward, so $4.99 is
filed nearer $4 than $5. The gain is largest when the leftmost digit actually changes and when
that digit is small — dropping from $200 to $199 moves more than $800 to $799.

**Where charm costs you.**
- It signals "discounted" — corrosive for a premium or expert brand, and unserious for high-stakes
  services. Don't charm-price a medical or legal fee.
- Across an assortment it pulls buyers *down* the ladder; an all-round ladder tends to hold them
  higher. Want mix-shift toward the better tier? Price every tier round.
- It fights divisibility: in bundles a price that divides cleanly by the unit count ($16 for 4) is
  easier to imagine using than a cheaper one that doesn't ($15.30 for 4).

**The trade-off in one line:** *charm buys a deal signal and costs a premium signal.* Pick which
you're selling and keep every price on the site consistent — mixed endings read as sloppiness and
undermine both signals.

**Precision extras (sparingly):** precise numbers imply a derivation, useful in quotes and
negotiation — an opening *range* whose bottom is your target holds better than one round demand.
Shorter-to-say prices are easier to recall.

## 8. Magnitude framing

**Mechanism.** People react to the absolute digit in front of them more than to the underlying rate.
Reframing a cost into a smaller unit lowers felt magnitude; reframing a saving into a bigger unit
raises felt gain.

| Framing | Rule | Example |
|---|---|---|
| Daily equivalence | Only when the daily figure is genuinely small (roughly a coffee or less) and the real billing line is shown beside it | "About $1 a day — billed $30/month" |
| Per-seat / per-unit | For B2B totals large enough to alarm | "$12 per user / month" under the team total |
| Incremental difference | Sell the *step up*, not the total | "Add graded assignments for $40 more" |
| Annual savings | Show absolute money saved, not only the percentage | "Save $72 a year" beside "2 months free" |
| Comparing to a competitor | Compare on the unit where the gap looks larger — but compare all your prices or none | Yearly totals when you're cheaper |

**Percentage or money off — the working rule:** below roughly $100 a percentage usually shows the
bigger number; above roughly $100 the money amount usually does. Compute both, use whichever is
larger, and stay consistent at that price level. Exception: at very high prices a large money-off
figure reminds the buyer how much they're spending — test.

**Honesty rails.** Every reframe must be arithmetically exact, and the amount actually charged must
appear in the same visual block at readable size. A "$1/day" headline hiding an annual commitment
is the textbook dark pattern — see the ban list in §14.

## 9. Partitioned vs all-inclusive pricing

| Approach | What it does | Use when | Risk |
|---|---|---|---|
| **All-inclusive** (one number, everything in) | Lowest friction, least felt pain, no surprises | Subscriptions, services, any trust-first brand | Headline number looks higher than partitioned rivals |
| **Partitioned** (base + shipping/setup/fees) | Base looks lower; components can be justified individually | Marketplaces and catalogues where a low base wins the click, and the add-ons are genuinely optional | Reads as nickel-and-diming; kills trust if revealed late |

- **Show the total before the buyer invests effort.** A mandatory fee revealed only at the last
  checkout step is drip pricing: it converts worse across the funnel, damages trust, and is
  regulated in several markets.
- **Free shipping beats discounted shipping** at equal cost to you — a zero removes a decision
  instead of adding a comparison. If you can't, quote one flat, memorable number.
- **Name every fee in the buyer's language** with a one-line reason ("card processing", "on-site
  setup, one-off") — an unexplained fee reads as a penalty. Truly optional add-ons can sit in
  parentheses; quieter typography lowers their felt weight.

## 10. Bundling and unbundling

**Bundle when:** you want to block a like-for-like comparison with a cheaper rival; components are
complementary; you want fewer decisions; you want strong items to carry slow ones; the sum of felt
values exceeds the price you'd charge separately.

**Unbundle when:** the entry price is the barrier; buyers want one part and resent paying for the
rest; you want a low-commitment first purchase; or the bundle hides which component drives value
(you'll never learn what to improve).

- **Mixed bundling usually wins:** sell the parts *and* the bundle, price the bundle below the sum,
  label the saving in absolute money.
- **Make bundle prices divisible by unit count** — a clean per-unit figure lets buyers imagine using
  each unit ($16 for 4 beats $15.30 for 4).
- **Bundle to protect a premium brand instead of discounting it:** adding value keeps the reference
  price intact, cutting price resets it. Never bundle to obscure an increase — repackaging is
  legitimate, misrepresenting is not.

## 11. Trials, freemium, guarantees: managing perceived risk

| Instrument | What it removes | Cost to you | Fits | Failure mode |
|---|---|---|---|---|
| **Time-limited free trial** | "Will it work for me?" | Support load; some tyre-kickers | Products whose value is felt within days | Value arrives after the trial ends |
| **Freemium** | Commitment entirely | Serving free users forever | Products with network or habit effects, low marginal cost | The free tier is good enough; no upgrade trigger |
| **Money-back guarantee** | Financial risk after buying | Refunds; admin | High-consideration, high-trust purchases | Conditions so tight the promise is worthless |
| **Low-price paid trial** | Financial risk *and* the "why not?" hesitation | Small revenue | Products with real setup effort | Reads as a trick if the step-up price is buried |
| **Pilot / paid proof-of-concept** | Uncertainty at scale | Delivery time | Enterprise, services | Never converts to the full contract |

- **Match trial length to time-to-first-value.** If value takes a week to appear, a 7-day trial
  guarantees failure.
- **Free is not always the best zero.** When trying takes visible *effort*, a zero price makes
  buyers hunt for a reason to decline and they land on the effort; a token fee holds attention on
  the small number. When trying is effortless, free wins. Test which case you're in.
- **A guarantee is only as strong as its shortest sentence.** "30 days, email us, full refund" beats
  a paragraph of conditions — and conditions belong in the same breath, not a linked policy.
- **Say what happens at the end**: "we email before it ends; nothing charges unless you add a card".
- Dial note: calm brands state the guarantee quietly; energetic brands may headline it. Neither may
  overstate it.

## 12. Discount hygiene

**Mechanism.** Every price a buyer sees updates their internal reference price. A discount that
never ends *becomes* the reference price — you cut your price and lost the ability to signal a deal
later. Predictable, repeated promotions train buyers to wait for the next one.

| Rule | Detail |
|---|---|
| Never run a permanent "sale" | If the discounted price is the real price, make it the price |
| Always give a reason | Launch, seasonal, clearance, loyalty, cost change. A reason legitimises the cut *and* implies it ends |
| Deadlines must be real | The price must actually change at the stated time — enforce it |
| Vary timing and depth | Predictable monthly sales train waiting; irregular, reason-led ones don't |
| Keep depth in a sane band | Deep enough to be noticed, shallow enough not to signal desperation. A working band for most categories is modest double digits; beyond that expect quality doubt |
| Discount the right things | Functional/commodity lines tolerate cuts. Premium, identity and emotionally-bought products should get value-adds, gifts, or bundles instead |
| Protect the reference price | Show the original alongside — but only if it was genuinely charged |
| Publish the return | State when the price goes back. It makes the deadline credible and the cut trustworthy |

**Presentation notes.** A coupon applied at checkout holds attention on the reduction rather than
the final number and tends to support larger baskets; a pre-reduced price pushes attention toward
finding something cheaper. Two stated reductions feel bigger than one equivalent cut — a perception
effect, so use it only where both are real and separately justified; stacking fictional reductions
is deception.

**Price increases.** Announce ahead, give the reason, grandfather existing customers for a stated
period, and change the package at the same time so old and new aren't a bare like-for-like
comparison. Increases are forgiven most easily on services and emotionally-valued features, least
easily on commodities with an obvious unit price.

## 13. Pay-what-you-want and donation framing

**What it is.** The buyer sets the price, with or without a floor.

**Mechanism.** Any number you display becomes the target — including a "minimum" and including
the small cost figures used to illustrate impact. Buyers do not treat a low unit cost as a
multiplier ("$3 feeds one, so I'll give $30"); they treat it as the expected contribution.

**How to apply:**
- **Always show suggested amounts**, higher options in view, one gently emphasised. An open box with
  no suggestions collects the lowest defensible number.
- **Set the ladder from your own data** (typical contribution, nudged up), not from ambition — asks
  far above what people give suppress giving rather than raise it.
- **Don't advertise your smallest impact unit as the ask.** Multiply it: "$25 covers five kits",
  not "$5 covers a kit".
- **A slider's upper bound is an anchor** — its midpoint reads as the norm. Choose it deliberately.
- **A floor plus a suggestion beats pure PWYW** for anything with real delivery cost.
- PWYW fits where the buyer already knows you, marginal cost is low, and payment is socially visible
  or reciprocal. Poor fit for a first transaction with a stranger.
- Comparing a donation to a petty indulgence works but induces guilt — fine in a charity context,
  corrosive for a commercial brand.

## 14. Honest scarcity — and the ban list

**Qualifies (say it plainly, once):**
- **Real capacity** — seats in a cohort, hours in a calendar, units in stock, clients a
  practitioner can hold. State the true number and keep it updated.
- **Real founding cohorts** — "first 50 customers keep this rate as long as they stay", then
  actually stop at 50 and honour it forever.
- **Real deadlines** — a price change, an enrolment close, an event date. Something must change at
  that moment.
- **Real seasonality** — a genuine end-of-season clearance.

**Banned outright, regardless of dial position:**
- Countdown timers that reset on refresh or per-visitor
- "Only 3 left" that is not read from real inventory
- Fake "X people are viewing this"
- An "original price" never actually charged
- Permanent "launch pricing" that has run for a year
- Deadlines that quietly pass without the price changing
- Invented ratings, testimonials, customer counts, or research figures

**Why this isn't only ethics.** Manufactured urgency is checkable — visitors reload the page — and
once caught it discredits every honest claim beside it, guarantee and proof included.

**The general line:** a tactic is legitimate when it changes how easily a buyer *understands* a
true offer, and manipulative when it changes what the buyer *believes to be true*. Anchoring with a
real premium tier: legitimate. Anchoring with a price you never charged: deception. Centre-staging
a tier: legitimate. Calling it "most popular" when it isn't: deception.

## Apply it

Run this as a pricing-page audit before launch and after every price change.

- [ ] The number came from value and research, not from cost-plus — and I can name the method used
- [ ] WTP was checked per segment, never via a direct "would you pay X" question
- [ ] The dial is declared (calm/premium vs energetic/deal) and every price element matches it
- [ ] Value, proof and objection-handling appear above the first price on the page
- [ ] Three tiers, one scaling dimension, names that describe the buyer or the job — not just size
- [ ] The target tier is centre-staged and isolated by exactly one device; any badge on it is true
- [ ] A real premium tier anchors the range, and a first-time visitor wouldn't describe the brand by it
- [ ] Any decoy is a real, purchasable, supportable option someone could rationally choose
- [ ] Tier name outweighs the price visually; currency symbol smaller than the digits
- [ ] Price sits after the benefits in each card; one solid CTA on the target card, ghost elsewhere
- [ ] Digit style (round / charm / precise) is deliberate, matches the dial, and is consistent sitewide
- [ ] Every reframe (per day, per seat, annual saving) is exact and shows the real billed amount beside it
- [ ] Total price — including all mandatory fees — is visible before the buyer invests effort
- [ ] Risk instrument chosen (trial / freemium / guarantee), its length matches time-to-first-value, and its terms fit in one sentence
- [ ] No permanent discount; every promotion has a reason, a real end date, and an enforced price change
- [ ] Zero fake timers, fake stock counts, fake originals, or invented numbers anywhere on the page

## Related

- [Positioning and category](../brand/01-positioning-and-category.md) — which category you're priced against
- [Voice, messaging and copywriting](../brand/03-voice-messaging-and-copywriting.md) — wording the offer and the guarantee
- [Persuasion core](./04-persuasion-core.md) — anchoring, reciprocity, commitment, honest social proof
- [Visual attention and layout](./05-visual-attention-and-layout.md) — isolating the target card, one focal point
- [Colour and typography](./06-color-and-typography.md) — price type scale, emphasis, why not red
- [Page architecture and section recipes](../build/08-page-architecture-and-section-recipes.md) — where the pricing section sits
- [Design system and tokens](../build/09-design-system-and-tokens.md) — type scale and button variants for price cards
- [Conversion audit checklist](../build/10-conversion-audit-checklist.md) — the full-site pass this feeds
- [Measurement and experimentation](../ops/14-measurement-and-experimentation.md) — how to test a price without fooling yourself
- [Page brief template](../templates/page-brief.md) — brief a pricing page
