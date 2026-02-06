---
name: north-star-metrics
description: "Help users define their North Star Metric, build a metric tree of leading and lagging indicators, design a metrics dashboard, and establish a measurement cadence."
---

# North Star Metrics

Produces a North Star Metric definition, a hierarchical metric tree connecting leading inputs to lagging outcomes, a dashboard specification, and a measurement cadence -- giving a product team a single source of truth for whether they are winning.

## Core Principles

1. **The North Star Metric captures the value you deliver, not the value you extract**
   "Your North Star Metric should measure the core value that your product delivers to customers. It is not revenue. Revenue is an outcome of delivering value. The North Star is the thing that, if it goes up, means customers are getting more value and revenue will follow."
   -- *Sean Ellis, Creator of the Sean Ellis Test and author of Hacking Growth* ([source](https://blog.growthhackers.com/what-is-a-north-star-metric-b31a8512923))

2. **A metric tree makes strategy legible**
   "When you break your North Star into a tree of input metrics, you make your strategy visible. Every team can see which lever they own and how it connects to the outcome the company cares about. Without the tree, teams optimize locally and the whole system drifts."
   -- *John Cutler, Product Evangelist and former Head of Product Education at Amplitude* ([source](https://cutlefish.substack.com/p/tbm-216-the-magic-of-small-batches))

3. **DAU/MAU is a ratio, not a religion**
   "DAU/MAU is only useful when the expected frequency of your product matches daily use. If your product is naturally weekly or project-based, forcing a daily metric creates perverse incentives. Match the frequency of your metric to the natural frequency of the value your product delivers."
   -- *Andrew Chen, General Partner at Andreessen Horowitz* ([source](https://andrewchen.com/dau-mau-is-an-important-metric/))

4. **Input metrics are the only ones you can act on**
   "There are metrics you can directly influence -- input metrics -- and metrics that result from those actions -- output metrics. Teams that focus on output metrics (revenue, retention) end up frustrated because those numbers move slowly and have many causes. Teams that focus on input metrics (activation rate, time-to-value) can run experiments and see results."
   -- *Amplitude Product Team, North Star Playbook* ([source](https://amplitude.com/books/north-star))

5. **Increase the tempo**
   "The most important thing a leader can do is raise the pace -- the intensity of execution. When I say amp it up, I mean take what you think is an acceptable level of performance and raise it dramatically. This applies to metrics: measure more frequently, react faster, iterate shorter cycles."
   -- *Frank Slootman, Chairman and former CEO of Snowflake, author of Amp It Up* ([source](https://www.amazon.com/Amp-Unlocking-Hypergrowth-Expectations-Intensity/dp/1119836115))

6. **Retention is the king of metrics**
   "If your retention is poor, then nothing else matters. You can acquire all the users in the world, but if they don't stick, you are filling a leaky bucket. Retention is the best single proxy for product-market fit and should be the foundation of any metric tree."
   -- *Casey Winters, former Growth Lead at Pinterest and Grubhub* ([source](https://www.lennysnewsletter.com/p/what-is-good-retention-casey-winters))

7. **Usage is the leading indicator; revenue is the lagging one**
   "The single most telling metric for a great product is whether or not people use it. Not just whether they sign up, but whether they keep using it over time. If people are using your product a lot, you almost always find a way to generate revenue from it."
   -- *Josh Elman, former VP Product at Robinhood and ex-Twitter, LinkedIn, Facebook* ([source](https://news.greylock.com/the-only-metric-that-matters-now-with-fancy-slides-232474cf414c))

8. **A North Star without a counter-metric is a recipe for gaming**
   "Every metric, if pursued in isolation, will be gamed or will drive pathological behavior. For every North Star, define at least one counter-metric -- a guardrail that ensures you are not achieving the target at the expense of something important."
   -- *Julie Zhou, Co-founder of Sundial and former VP Design at Facebook* ([source](https://medium.com/the-year-of-the-looking-glass/how-do-you-set-metrics-59f78fea7e44))

## Instructions

### Step 1: Identify the Core Value Exchange

- Define the product's primary value proposition in one sentence: what does the user get from using the product?
- Identify the **core action** -- the single action a user takes that delivers this value (e.g., "generates a 3D world," "completes a simulation run," "publishes a design")
- Map the value exchange: what the user invests (time, money, data) and what they receive (output, insight, saved effort)
- If `context/products/` exists, read it to extract the product description and feature set
- **Artifact produced:** A one-paragraph value exchange statement and identification of the core action

### Step 2: Define the North Star Metric

- Using the core action from Step 1, formulate a North Star Metric that satisfies all four criteria:
  1. **Measures value delivered** -- it goes up when customers get more value, not just when the company extracts more revenue
  2. **Is a leading indicator of revenue** -- if this metric grows sustainably, revenue growth will follow
  3. **Is actionable** -- teams can run experiments that move it within a sprint cycle
  4. **Is understandable** -- anyone in the company can explain what it means and why it matters
- Test the candidate metric against three failure modes:
  - Can it be gamed without delivering real value? If yes, it fails.
  - Does it move at a frequency that allows weekly decision-making? If not, pick a faster-moving proxy.
  - Does it conflate multiple user segments whose health should be tracked separately? If yes, segment it.
- Define one **counter-metric** (the guardrail that prevents pathological optimization)
- **Artifact produced:** North Star Metric definition with name, formula, measurement frequency, and counter-metric

### Step 3: Build the Metric Tree

- Decompose the North Star into a tree of 3-5 **input metrics** (leading indicators the team can directly influence) and 2-3 **output metrics** (lagging indicators that confirm value delivery)
- Structure the tree in three tiers:

```
North Star Metric
├── Input Metric A (Acquisition)
│   ├── Sub-metric A1
│   └── Sub-metric A2
├── Input Metric B (Activation)
│   ├── Sub-metric B1
│   └── Sub-metric B2
├── Input Metric C (Engagement)
│   └── Sub-metric C1
└── Output Metrics (Lagging)
    ├── Revenue / Monetization
    └── Retention
```

- For each metric in the tree, document:
  - **Definition:** What it measures, precisely
  - **Formula:** How it is calculated
  - **Owner:** Which team or role is responsible
  - **Cadence:** How frequently it is measured (daily, weekly, monthly)
  - **Target:** The threshold for "healthy" and the threshold for "investigate"
- **Artifact produced:** A metric tree diagram (text-based) and a companion table with definitions, formulas, owners, cadences, and targets

### Step 4: Set Baselines and Targets

- For each metric in the tree, establish a baseline using one of three methods:
  - **Historical data:** If the product has usage data, pull the trailing 4-week average
  - **Benchmark data:** If the product is pre-launch or early-stage, use industry benchmarks (cite sources)
  - **Hypothesis:** If neither exists, state an explicit assumption and flag it for validation within 30 days
- Set targets for three time horizons:
  - **30-day target:** What must be true in one month for the metric to be "on track"
  - **90-day target:** Where the metric should land by end of quarter
  - **12-month aspiration:** The ambitious goal that defines success for the year
- For each target, define the threshold below which the team should escalate or change strategy
- If `context/company/` exists, read it to calibrate targets to company stage and resources
- **Artifact produced:** A baselines and targets table with columns: Metric | Baseline | 30-Day Target | 90-Day Target | 12-Month Aspiration | Investigate Threshold

### Step 5: Design the Metrics Dashboard

- Specify a dashboard layout that makes the metric tree visible at a glance:
  - **Top row:** North Star Metric (large, prominent) with trend line (trailing 4 weeks) and counter-metric
  - **Middle row:** Input metrics (one card per metric) with sparklines showing weekly trend
  - **Bottom row:** Output metrics (retention curve, revenue trend) updated monthly
- For each dashboard element, specify:
  - Data source (analytics tool, database query, manual collection)
  - Refresh frequency
  - Visual format (number, trend line, bar chart, cohort table)
  - Alert condition (when should this element turn red?)
- Include a **weekly snapshot** format: a one-screen summary that can be pasted into Slack or email for the weekly metrics review
- **Artifact produced:** A dashboard specification document with layout, data sources, refresh cadences, alert conditions, and a weekly snapshot template

### Step 6: Establish the Measurement Cadence

- Define a recurring review rhythm:
  - **Daily (automated):** North Star Metric and input metrics surfaced in a dashboard or Slack channel. No meeting required -- team scans for anomalies.
  - **Weekly (30 min):** Review the weekly snapshot. For each input metric, answer: "Is it on track? If not, what experiment are we running this week to move it?" Decide on one action per off-track metric.
  - **Monthly (60 min):** Review output metrics (retention, revenue). Compare actuals to 30-day targets. Adjust targets if the baseline assumption proved wrong. Review the counter-metric to check for unintended side effects.
  - **Quarterly (90 min):** Re-evaluate the North Star Metric itself. Has the product's value proposition shifted? Has the user mix changed? Should input metrics be reweighted? Re-score the full metric tree and update the 12-month aspiration.
- Assign a **metrics owner** (role, not person) responsible for preparing the weekly snapshot and flagging anomalies
- **Artifact produced:** A measurement cadence document with meeting formats, agendas, attendees (by role), and escalation rules

### Step 7: Compile the North Star Package

- Assemble all artifacts from Steps 1-6 into a single reference document:
  1. Value Exchange Statement (Step 1)
  2. North Star Metric Definition with counter-metric (Step 2)
  3. Metric Tree diagram and companion table (Step 3)
  4. Baselines and Targets table (Step 4)
  5. Dashboard Specification (Step 5)
  6. Measurement Cadence (Step 6)
- Write a one-paragraph executive summary at the top: what is the North Star, why this metric, and what does the team need to do differently starting this week
- **Artifact produced:** A complete North Star package saved as `applied/north-star-{product}.md`

## Diagnostic Questions

1. **If you could only look at one number each morning to know whether the product is healthy, what would it be?** If the answer is revenue, you are measuring extraction, not value delivery. Keep asking until you find the metric that represents value to the user.

2. **Does your current "key metric" go up when users get more value, or only when the company makes more money?** These often diverge. A metric that rewards user value will eventually drive revenue; a metric that rewards extraction will eventually drive churn.

3. **Can every team in the company explain how their work connects to the North Star?** If not, either the North Star is too abstract or the metric tree has gaps. Every team should own at least one input metric that feeds the North Star.

4. **How quickly does your North Star Metric move?** If it takes 6 months to see a change, it is not actionable for weekly decision-making. You need a faster-moving leading indicator as a proxy.

5. **What behavior would a rational but unscrupulous team adopt to maximize this metric?** This reveals gaming risks. If the answer is something harmful (e.g., sending spam notifications to boost DAU), you need a counter-metric.

6. **Are you measuring what matters or what is easy to measure?** Teams default to metrics they can already instrument. The right metric might require new instrumentation. Do not let data availability drive metric selection.

7. **When was the last time you changed your key metric?** If never, you are likely measuring inertia, not strategy. As the product evolves, the North Star should evolve with it.

## Common Mistakes

1. **Choosing revenue as the North Star**
   Revenue is an output of delivering value, not the value itself. When revenue is the North Star, teams optimize for extraction (pricing tricks, dark patterns, upsells) rather than for making the product indispensable. Choose a metric that measures the value users receive; revenue becomes an output metric in the tree.

2. **Building a metric tree with too many metrics**
   A tree with 20+ metrics creates dashboard blindness -- no one knows where to look. Limit the tree to 3-5 input metrics and 2-3 output metrics. If a metric does not change a decision you would make this week, remove it.

3. **Measuring without a cadence**
   Dashboards without a review rhythm become wallpaper. The metrics exist but no one acts on them. Establish a weekly review where each off-track input metric gets exactly one action item. If the meeting produces no actions, the metrics are not actionable.

4. **Skipping the counter-metric**
   Every metric optimized in isolation produces pathological behavior. DAU without session quality incentivizes spam notifications. Activation rate without retention incentivizes lowering the bar for "activated." Always pair the North Star with a guardrail.

5. **Setting targets without baselines**
   A target of "10,000 weekly active worlds" is meaningless without knowing the current number is 200 or 8,000. Always establish a baseline first, then set targets as a function of achievable growth from that baseline. Aspirational targets without anchoring demoralize teams.

6. **Confusing correlation with causation in the metric tree**
   Input metrics should have a causal relationship with the North Star, not merely a correlational one. Test causation by running an experiment: if you increase Input Metric A, does the North Star actually move? If you have never tested this, the tree is a hypothesis, not a fact.

## Context Integration

This skill uses the `context/` directory to ground the metric tree in company-specific reality:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3 | Product descriptions, feature sets, and pricing tiers inform the core value exchange (Step 1), shape the North Star Metric definition (Step 2), and determine which input metrics matter most (Step 3). If product files describe multiple products, build a separate metric tree per product or choose the primary product. |
| `context/verticals/` | Steps 2, 4 | Target market data and use cases inform whether the North Star should be segmented by vertical. TAM/SAM data from vertical files helps calibrate 12-month aspiration targets (Step 4). Different verticals may have different natural usage frequencies, affecting metric cadence. |
| `context/competitive/` | Steps 2, 4 | Competitor data helps benchmark metric targets. If competitors publish usage metrics (MAU, API calls, retention), use them to calibrate baselines and targets. Competitor positioning also helps validate that the North Star measures a differentiating dimension, not a commodity one. |
| `context/company/` | Steps 4, 6 | Company stage, funding, and team size calibrate target ambition and measurement cadence. A 5-person team cannot sustain a daily metrics review meeting; a 200-person company cannot rely on ad hoc Slack messages. Resource constraints shape what cadence is realistic. |
| `context/founders/` | Steps 1, 2 | Founder vision and mission statements provide a gut-check on whether the North Star aligns with the company's reason for existing. If the founder's stated mission is about democratizing 3D creation, the North Star should measure creation volume and breadth, not just revenue. |
| `context/signals/` | Steps 3, 4 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. GitHub metrics (stars, forks, issues) can serve as developer ecosystem input metrics. Community sentiment from HN/Reddit provides qualitative context for interpreting metric movements. Check freshness before citing. |

When no `context/` directory is available, the skill prompts the user to provide:
1. A brief description of their product and its core value proposition
2. The primary action users take that delivers value
3. Any existing metrics they track today and their current values
4. Company stage and team size (to calibrate cadence recommendations)
