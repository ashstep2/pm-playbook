---
name: pricing-and-monetization
description: "Help users design pricing models and monetization strategy by analyzing willingness-to-pay, competitive positioning, and packaging to maximize revenue and adoption."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Pricing and Monetization

Produces a pricing architecture, willingness-to-pay analysis, tier design, usage-based pricing model (especially for API products), and a pricing experimentation roadmap.

## Core Principles

1. **Monetization is not an afterthought -- it is a core product decision**
   "The number one reason new products fail is the failure to put the customer's willingness to pay at the very center of product design. Most companies delay pricing decisions until after the product is developed. By then, it's too late."
   -- *Madhavan Ramanujam, Partner at Simon-Kucher and co-author of Monetizing Innovation* ([source](https://www.simonkucher.com/insights/monetizing-innovation/))

   Pricing must be designed alongside the product, not bolted on after launch. If you wait until the product is built to think about willingness-to-pay, you have already made irreversible packaging decisions.

2. **Your pricing is the exchange rate on the value you create**
   "Pricing is the exchange rate you put on everything that your business does. When you get pricing wrong, you damage a business that took years to build."
   -- *Patrick Campbell, Founder of ProfitWell (acquired by Paddle)* ([source](https://www.profitwell.com/recur/all/pricing-strategy-guide))

   Pricing is not a spreadsheet exercise -- it is a signal to the market about who you are and what you are worth. Underpricing signals low confidence. Overpricing without justification signals disconnection from user value.

3. **Software is too cheap**
   "In the history of software, almost no company has died because they charged too much. Far more die because they charge too little, can't fund growth, and fade into irrelevance."
   -- *Marc Andreessen, Co-founder of Andreessen Horowitz* ([source](https://fictivekin.github.io/pmarchive-jekyll/guide_to_startups_part4.html))

   Most builders systematically underprice because they optimize for adoption over revenue. Resist the instinct. Price for the value you deliver, not the cost of what you built.

4. **Usage-based pricing aligns your revenue with your customer's success**
   "Usage-based pricing has emerged as the dominant model for developer infrastructure because it solves the alignment problem: you only pay more when you get more value. The best usage-based models pick a value metric that grows as the customer succeeds."
   -- *Kyle Poyar, Operating Partner at OpenView and author of Growth Unhinged* ([source](https://openviewpartners.com/blog/state-of-usage-based-pricing/))

   For API products, usage-based pricing is almost always the right foundation. The challenge is choosing the right value metric -- one that is predictable enough for customers to budget around, but scales with the value they extract.

5. **Free is a strategy, not a price point**
   "Free is not a business model. Free is a marketing strategy. The question is not whether to offer something free -- it's what to give away, what to charge for, and how the free thing creates demand for the paid thing."
   -- *Tomasz Tunguz, Managing Director at Theory Ventures* ([source](https://tomtunguz.com/the-three-part-pricing-framework/))

   Free tiers, trials, and freemium models are powerful acquisition tools when designed intentionally. They become value destroyers when they give away the core product without creating a natural upgrade trigger.

6. **Good packaging makes the customer self-select into the right tier**
   "The best packaging doesn't force customers into tiers -- it lets them recognize themselves. Each tier should map to a distinct persona with a distinct job-to-be-done. If customers are confused about which plan to pick, your packaging is wrong."
   -- *Patrick Campbell, Founder of ProfitWell (acquired by Paddle)* ([source](https://www.profitwell.com/recur/all/saas-packaging-strategy))

   Tier confusion is the silent killer of conversion. Each tier should correspond to a clear user archetype. If a customer reads three tier descriptions and cannot instantly identify which one is for them, the packaging needs to be redesigned.

7. **Price on value, not on cost**
   "The biggest pricing mistake is anchoring to your costs. Your costs are irrelevant to the customer. What matters is the value your product creates relative to the customer's next-best alternative. Price to that delta."
   -- *Madhavan Ramanujam, Partner at Simon-Kucher and co-author of Monetizing Innovation* ([source](https://www.amazon.com/Monetizing-Innovation-Companies-Design-Product/dp/1119240867))

   Cost-plus pricing is the default because it feels safe. But it leaves enormous value on the table when your product creates transformational outcomes, and it overcharges when the user perceives less value than you assume.

8. **Pricing is never done -- it is a living experiment**
   "The companies that grow fastest treat pricing as a product feature, not a one-time decision. They test, measure, and iterate on pricing with the same rigor they apply to product features. Most companies revisit pricing once every three years. The best do it every six months."
   -- *Kyle Poyar, Operating Partner at OpenView and author of Growth Unhinged* ([source](https://kylepoyar.substack.com/p/the-10-commandments-of-usage-based))

   Pricing stagnation is a growth ceiling in disguise. Build a pricing experimentation roadmap from day one, and treat each pricing change as a hypothesis to be validated with data.

## Instructions

### Step 1: Map the Value Architecture

Before setting any prices, document the value your product creates across all user segments:

- **Core value metric**: The single unit of value your product delivers (e.g., API calls, worlds generated, seats, GB stored, minutes of compute). This metric should scale linearly with the value the customer receives.
- **Value chain**: Map the user journey from first interaction to full adoption. Identify where value is created, where friction exists, and where the "aha moment" occurs.
- **Value benchmarks**: For each user segment, quantify the value of the problem you solve. What does it cost them today (in time, money, or opportunity cost) to do what your product does?

**Artifact produced**: A Value Architecture document with the core value metric, value chain map, and per-segment value benchmarks, saved as `applied/pricing-value-architecture-{product}.md`.

### Step 2: Conduct Willingness-to-Pay Analysis

Design and execute (or simulate) a WTP study to establish price boundaries:

- **Van Westendorp Price Sensitivity Meter**: For each target segment, identify the four price points:
  - Too cheap (quality concern)
  - Cheap (good deal)
  - Expensive (but still acceptable)
  - Too expensive (would not buy)
- **Gabor-Granger method**: If direct surveying is possible, test specific price points to build a demand curve.
- **Competitive anchoring**: Map competitor pricing for equivalent value. Position your price relative to the competitive set -- are you premium, parity, or penetration?
- **Segment-level variance**: WTP differs dramatically across segments. An indie developer and an enterprise team have different budgets and different perceptions of value. Run the analysis per segment, not in aggregate.

**Artifact produced**: A Willingness-to-Pay report with price boundaries per segment, competitive price map, and recommended price range, saved as `applied/pricing-wtp-analysis-{product}.md`.

### Step 3: Design the Pricing Model

Choose and design the pricing model that best fits your product and market:

| Model | Best For | Risk |
|---|---|---|
| **Usage-based** | API products, infrastructure, compute | Revenue volatility; customer budgeting anxiety |
| **Tiered subscription** | SaaS with distinct personas per tier | Tier confusion; feature gating resentment |
| **Per-seat** | Collaboration tools, team-based products | Seat-cheating; discourages viral expansion |
| **Hybrid (subscription + usage)** | Products with a base platform and variable consumption | Complexity; hard to communicate simply |
| **Credit-based** | Products with heterogeneous operations at different costs | Opacity; customers struggle to predict spend |

For API products specifically, design the usage-based component:

- **Value metric selection**: Pick the metric that most closely tracks customer value (not your cost). Validate by asking: "When this metric goes up, does the customer always get more value?"
- **Rate structure**: Flat rate per unit, volume tiers (declining marginal cost), or committed-use discounts?
- **Spending controls**: Alerts, hard caps, budget limits. Usage-based pricing without spending controls creates customer anxiety.
- **Minimum commitment**: Floor spend to ensure revenue predictability.

**Artifact produced**: A Pricing Model Design document specifying the model type, value metric, rate card, tier boundaries, and spending control mechanisms.

### Step 4: Design the Tier and Packaging Structure

Create 2-4 tiers, each mapped to a distinct user persona:

For each tier, define:
- **Tier name**: Should evoke the persona, not the feature set (e.g., "Starter" not "10k API calls")
- **Target persona**: Who is this tier for? One sentence.
- **Included capabilities**: Features, limits, and support level
- **Upgrade trigger**: The specific usage pattern or need that causes this persona to outgrow this tier
- **Price point**: Based on WTP analysis from Step 2

Design the free tier (if applicable) with care:
- The free tier must deliver enough value to reach the "aha moment"
- The free tier must have a natural ceiling that triggers upgrade consideration
- The free tier must not cannibalize paid tiers -- if 90% of users never upgrade, the ceiling is too high

**Artifact produced**: A Tier Design Matrix with persona mapping, feature allocation, upgrade triggers, and price points for each tier.

### Step 5: Model Revenue Scenarios

Build a revenue model that projects outcomes under three adoption scenarios:

- **Conservative**: Slow adoption, high churn, low expansion revenue
- **Base case**: Expected adoption curve, moderate churn, moderate expansion
- **Optimistic**: Fast adoption, low churn, strong expansion and upsell

For each scenario, model:
- Monthly Recurring Revenue (MRR) trajectory over 12 months
- Average Revenue Per User (ARPU) by tier
- Net Revenue Retention (NRR) -- expansion revenue vs. churn
- Gross margin (revenue minus cost-to-serve per unit of value metric)
- Payback period on customer acquisition cost

For usage-based models, include sensitivity analysis on the value metric: what happens to revenue if average usage per customer is 50% lower or 200% higher than expected?

**Artifact produced**: A Revenue Model spreadsheet or document with three scenarios, sensitivity analysis, and key assumptions documented.

### Step 6: Build the Pricing Experimentation Roadmap

Pricing is a hypothesis. Define a structured experimentation plan:

- **Month 1-3 (Launch pricing)**: Ship the initial pricing. Instrument analytics to track conversion rates at each tier boundary, upgrade/downgrade patterns, and price sensitivity signals (e.g., cart abandonment, plan comparison page dwell time).
- **Month 3-6 (Calibration)**: Run the first pricing experiment. Test one variable at a time: a different price point for one tier, a different free tier ceiling, or a different value metric. Use A/B testing or cohort comparison.
- **Month 6-12 (Optimization)**: Based on data, adjust tier boundaries, introduce annual pricing discounts, add enterprise tier if demand warrants, or restructure the value metric. Re-run WTP analysis with real users.

For each experiment, define:
- Hypothesis (e.g., "Raising the Pro tier from $29 to $49 will reduce conversion by less than 15% and increase ARPU by more than 40%")
- Test design (A/B, before/after, cohort)
- Success criteria
- Rollback plan if the experiment harms revenue or adoption

**Artifact produced**: A Pricing Experimentation Roadmap with a sequenced list of experiments, hypotheses, and decision criteria, saved as `applied/pricing-experimentation-roadmap-{product}.md`.

### Step 7: Compile the Pricing Strategy Document

Assemble all artifacts from Steps 1-6 into a single pricing strategy:

1. Value Architecture (from Step 1)
2. Willingness-to-Pay Analysis (from Step 2)
3. Pricing Model Design (from Step 3)
4. Tier and Packaging Structure (from Step 4)
5. Revenue Scenarios (from Step 5)
6. Experimentation Roadmap (from Step 6)
7. Executive summary: one paragraph stating the recommended pricing, the rationale, and the expected revenue impact

**Artifact produced**: A complete Pricing Strategy saved as `applied/pricing-strategy-{product}.md`.

## Diagnostic Questions

Ask these before beginning the pricing analysis to calibrate the approach:

1. **What is the customer's next-best alternative, and what does it cost them?** If you cannot answer this, you cannot price on value. Start with competitive research or customer discovery first.

2. **Is your primary growth constraint adoption or revenue?** If adoption, lean toward lower prices and generous free tiers. If revenue, lean toward higher prices and tighter packaging. These are fundamentally different pricing strategies.

3. **Does your value metric scale linearly with customer value?** If API calls go up but customer value does not, you are charging for cost, not value. Find a better metric.

4. **Can your customers predict their monthly spend?** If not, usage-based pricing will create budget anxiety that suppresses adoption. Add spending controls, committed-use discounts, or a hybrid model to restore predictability.

5. **Who in the customer's organization controls the budget?** Pricing aimed at developers but approved by finance teams needs different packaging than pricing where the developer is the buyer. Understand the buying process before setting tier boundaries.

6. **What percentage of your current free users would you be comfortable losing if you introduced or raised pricing?** This reveals your true pricing philosophy and helps calibrate how aggressive the initial price point should be.

## Common Mistakes

1. **Pricing on cost instead of value**
   Your infrastructure cost per API call is irrelevant to the customer. What matters is the value of what that API call produces. A world generation API that saves a game studio three weeks of manual environment design can command a premium that has nothing to do with your GPU costs. Always price to the customer's alternative, not to your margin target.

2. **Giving away too much in the free tier**
   A generous free tier accelerates adoption -- until it doesn't. If 95% of users never convert, the free tier is subsidizing non-customers at the expense of the business. The free tier ceiling should be high enough to demonstrate clear value but low enough that anyone deriving real, ongoing value naturally hits the upgrade trigger.

3. **Designing tiers around features instead of personas**
   Feature-gating (locking specific capabilities behind higher tiers) creates resentment when the gated feature is the reason the user signed up. Instead, design tiers around usage volume, support level, and scale -- let all users access the core capability, and charge more as they use more.

4. **Setting pricing once and never revisiting it**
   Launch pricing is a guess. The most important thing about your first price is that it exists and generates data. Plan to revisit pricing within 90 days of launch, and every 6 months thereafter. Companies that treat pricing as static leave 20-40% of potential revenue on the table.

5. **Ignoring the psychological dimension of pricing**
   Price anchoring, charm pricing, decoy tiers, and annual discount framing are not gimmicks -- they are well-documented cognitive biases that affect purchasing decisions. A three-tier structure where the middle tier is the "intended" choice, anchored by a premium tier above it, consistently outperforms a two-tier structure. Design for how people actually make decisions.

## Context Integration

This skill draws from the `context/` directory when available to ground the pricing analysis in real data:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 3, 4, 5 | Product descriptions, current pricing (if any), feature set, and technical architecture. Essential for identifying the core value metric in Step 1 and designing tier boundaries in Step 4. If existing pricing is documented, use it as the baseline for the experimentation roadmap. |
| `context/competitive/` | Steps 2, 3 | Competitor pricing, packaging, and positioning. Feeds the competitive anchoring analysis in the WTP study (Step 2) and informs pricing model selection (Step 3). Per-competitor files with pricing details enable direct price-positioning analysis. |
| `context/verticals/` | Steps 1, 2, 4 | Target market segments, TAM/SAM/SOM, and use case profiles. Drives per-segment WTP analysis (Step 2) and ensures tier personas map to real vertical needs (Step 4). Different verticals often have radically different WTP. |
| `context/company/` | Steps 5, 6 | Funding stage, burn rate, revenue targets, and team size. Calibrates how aggressive the revenue model (Step 5) should be and how much pricing experimentation capacity exists (Step 6). A pre-revenue startup and a scaling company have different pricing urgency. |
| `context/founders/` | Step 1 | Founder vision and strategic priorities. Ensures the pricing philosophy (premium vs. penetration, PLG vs. sales-led) aligns with the founders' stated go-to-market intent. |
| `context/signals/` | Steps 2, 6 | Community sentiment, developer feedback, and competitor pricing changes. Use `reddit-discussions.md` and `hackernews-sentiment.md` for pricing sentiment signals. Use `news-coverage.md` to detect competitor pricing moves that should trigger experimentation. |

If no `context/` directory is present, the skill will prompt the user to provide:
1. A description of the product and its core value proposition
2. Known competitors and their pricing (even approximate)
3. Target customer segments and their budget constraints
4. Current pricing (if any) and what is or is not working about it
