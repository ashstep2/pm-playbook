---
name: experiment-design
description: "Help users design and run product experiments — producing experiment briefs, statistical plans, growth loop designs, and results synthesis to systematically convert hypotheses into validated knowledge."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Experiment Design

Produces experiment briefs, experiment type selection rationale, statistical plans, growth loop designs, and results synthesis — the systematic bridge between "we think this will work" and "we know this works." Reach for this skill when a feature's impact is uncertain, when growth has stalled and you need to find the lever, or when a prototype validated desirability but you need to validate scale.

## Core Principles

1. **Most ideas fail — experimentation figures out which don't**
   "It is humbling to see how bad experts are at estimating the value of features. At Microsoft, about one-third of experiments generate positive results, one-third are flat, and one-third are negative. Experimentation is the systematic way to figure out which third you're in."
   -- *Ronny Kohavi, Former VP of Experimentation at Microsoft and Airbnb* ([source](https://www.exp-platform.com/Documents/2017-08%20KDDTutorial/KDD2017-tutorial.pdf))

   The default assumption should be that your idea will not work. Experimentation is not about proving you are right — it is about discovering you are wrong as cheaply as possible. Design experiments that can clearly falsify your hypothesis, not just confirm it.

2. **Growth is a system, not a tactic**
   "Growth loops are closed systems where the inputs through some process generate more of an output that can be reinvested in the input. Loops compound. Tactics do not."
   -- *Brian Balfour, Founder of Reforge and former VP Growth at HubSpot* ([source](https://brianbalfour.com/growth-loops))

   Individual experiments improve individual metrics. Growth loop design improves the system. Before designing point experiments, map the loops in your product: how does each user action generate conditions for the next user or the next action? Experiment on the weakest link in the loop, not on random features.

3. **Assumption testing before A/B testing**
   "Before you run an A/B test, you should have already tested the riskiest assumptions through cheaper methods — user interviews, prototype tests, fake doors. A/B tests are for optimization, not discovery."
   -- *Teresa Torres, Author of Continuous Discovery Habits* ([source](https://www.producttalk.org/2021/08/opportunity-solution-trees/))

   A/B tests are expensive: they require traffic, engineering time, and statistical patience. Use them for optimizing validated concepts, not for discovering whether a concept is viable. For discovery, use cheaper methods: fake doors, painted doors, Wizard-of-Oz tests, or beta cohorts. Match the experiment type to the question.

4. **Cold start requires different experiments**
   "The Cold Start Problem is about how new networks need to reach a tipping point of participants before the network effect kicks in. Experiments at this stage look different: you're testing whether the loop exists, not optimizing it."
   -- *Andrew Chen, General Partner at Andreessen Horowitz and author of The Cold Start Problem* ([source](https://www.coldstart.com/))

   Early-stage products cannot run A/B tests (insufficient traffic) and should not optimize loops (loops are not yet established). Early experiments focus on existence questions: does this loop exist? Can we trigger it manually? What is the minimum activation energy? Design experiments appropriate to your product's maturity.

5. **Guardrail metrics prevent false victories**
   "Every experiment has a target metric, but it must also have guardrail metrics — things that should NOT degrade when the target improves. A pricing experiment that increases ARPU but craters retention is not a win."
   -- *Ronny Kohavi, from Trustworthy Online Controlled Experiments* ([source](https://www.cambridge.org/us/academic/subjects/computer-science/computer-science-general-interest/trustworthy-online-controlled-experiments-practical-guide-ab-testing))

   An experiment without guardrails is an experiment that can succeed by doing damage. For every experiment, define 2-3 metrics that must not degrade. Common guardrails: retention, support ticket volume, error rates, page load time, NPS.

6. **Sample size determines what you can detect**
   "The most common mistake in A/B testing is running the test with too few users for too short a time, then declaring a winner. This is not experimentation — it is confirmation bias with statistical decoration."
   -- *Evan Miller, Creator of the A/B test sample size calculator* ([source](https://www.evanmiller.org/how-not-to-run-an-ab-test.html))

   Before running any experiment, calculate the sample size needed to detect your minimum detectable effect (MDE) at your chosen significance level. If you do not have enough traffic to reach that sample size in a reasonable timeframe, choose a different experiment type.

7. **Document what you learned, not just what happened**
   "The value of an experiment is not in the result — it's in what you learn. A negative result that teaches you something is more valuable than a positive result that teaches you nothing. But only if you write down the learning."
   -- *Adapted from Eric Ries, The Lean Startup* ([source](https://theleanstartup.com/principles))

   Results synthesis is not a metrics report. It is a knowledge artifact. For every experiment, document: what you expected, what happened, what surprised you, and what you will do differently as a result. Experiments without synthesis are expensive guesses.

8. **Run fewer, better experiments**
   "The temptation is to run many experiments simultaneously. But each concurrent experiment competes for traffic, introduces interaction effects, and dilutes focus. Fewer, better-designed experiments produce clearer signals."
   -- *Stefan Thomke, Professor at Harvard Business School and author of Experimentation Works* ([source](https://www.hbs.edu/faculty/Pages/item.aspx?num=56498))

   Resist the urge to parallelize experiments beyond your traffic and attention capacity. A well-designed experiment with clear hypotheses and adequate sample size beats three rushed experiments with murky results. Focus on the highest-leverage question first.

## Instructions

### Step 1: Write the Experiment Brief

Define the experiment's purpose and boundaries. Produce:

- **Hypothesis:** A falsifiable statement in the format: "We believe [change] will cause [effect] for [users] because [reasoning]."
- **Target metric:** The single primary metric this experiment aims to move. Define how it is measured and the current baseline value.
- **Minimum detectable effect (MDE):** The smallest change in the target metric that would be meaningful enough to act on. If a 1% improvement is not worth the effort, set the MDE at 2% or higher.
- **Guardrail metrics:** 2-3 metrics that must not degrade. Define acceptable degradation thresholds (e.g., "retention cannot drop more than 0.5%").
- **Success threshold:** What result constitutes a clear win? What constitutes a clear loss? What falls in the ambiguous zone?
- **Time box:** Maximum duration for the experiment. If the experiment cannot reach statistical significance in this window, it should be redesigned or abandoned.

Reference prior `prototype-driven-validation` output if the experiment follows a successful prototype. Reference `north-star-metrics` for metric definitions and baselines.

**Artifact:** Experiment brief (1 page) saved as `applied/experiment-brief-{name}.md`.

### Step 2: Select the Experiment Type

Choose the right experiment type based on the question, traffic, and product maturity. Evaluate:

| Experiment Type | Best For | Traffic Needed | Duration | Signal Quality |
|---|---|---|---|---|
| **A/B Test** | Optimizing existing flows, testing variations | High (1000s of users) | 2-4 weeks | High (causal) |
| **Fake Door / Painted Door** | Testing demand before building | Medium (100s of users) | 1-2 weeks | Medium (intent, not behavior) |
| **Beta Cohort** | Testing new features with engaged users | Low (10s of users) | 2-6 weeks | Medium-High (behavioral, not causal) |
| **Wizard-of-Oz** | Testing value before building technology | Low (10s of users) | 1-4 weeks | Medium (value signal, not scalability) |
| **Holdback / Reverse Experiment** | Measuring impact of existing features | High (1000s of users) | 2-4 weeks | High (causal) |
| **Pre/Post (with caution)** | When randomization is impossible | Any | Variable | Low (confounded) |

Decision criteria:
- If traffic is below 500 daily active users for the relevant surface, do NOT run an A/B test. Use beta cohort or fake door instead.
- If the feature does not yet exist, use fake door, Wizard-of-Oz, or `prototype-driven-validation`.
- If you need causal evidence for a high-stakes decision, use A/B test or holdback.
- If you need quick directional signal, use a beta cohort.

**Artifact:** Experiment type selection with justification.

### Step 3: Build the Statistical Plan

For quantitative experiments (A/B test, holdback, fake door with conversion metric), produce:

- **Sample size calculation:**
  - Baseline conversion rate (current metric value)
  - Minimum detectable effect (from Step 1)
  - Significance level (default: 95%, adjust for context)
  - Power (default: 80%)
  - Calculated sample size per variant
  - Estimated time to reach sample size given current traffic

- **Randomization design:** How users are assigned to variants (user-level, session-level, or cluster-level). Document any stratification needed.
- **Analysis plan:** Pre-register the primary analysis method:
  - For conversion metrics: two-proportion z-test or chi-squared
  - For continuous metrics: t-test or Mann-Whitney U
  - For time-series effects: interrupted time series or difference-in-differences
- **Stopping rules:** Define when to stop the experiment early (either for a clear winner or for futility). Do NOT peek at results daily without a sequential testing framework.
- **Interaction check:** If other experiments are running concurrently, document potential interactions and how you will handle them.

For qualitative experiments (beta cohort, Wizard-of-Oz), produce:
- **Cohort size and selection criteria**
- **Data collection protocol:** Surveys, interviews, usage logs, or all three
- **Analysis framework:** Thematic analysis for qualitative data, descriptive statistics for usage data

**Artifact:** Statistical plan or qualitative research plan.

### Step 4: Design the Growth Loop (if applicable)

If the experiment relates to growth, retention, or engagement, map the relevant growth loop before designing the experiment. Produce:

- **Loop diagram:** Map the cycle: [User Action] → [Value Created] → [Distribution Mechanism] → [New User / Return Visit].
- **Loop type:** Identify which loop pattern applies:
  - **Viral loop:** User invites or shares, attracting new users
  - **Content loop:** User creates content, content attracts new users via search/social
  - **Paid loop:** Revenue funds acquisition, acquisition generates revenue
  - **Usage loop:** User engagement generates data/value that improves the product, driving more engagement
- **Weakest link:** Which step in the loop has the highest drop-off or lowest conversion? This is where the experiment should focus.
- **Loop metric:** The conversion rate at the weakest link (e.g., "12% of created projects are shared publicly").
- **Experiment target:** The specific intervention aimed at strengthening the weakest link.

Reference `north-star-metrics` for metric hierarchies and `measuring-product-market-fit` for retention baselines.

**Artifact:** Growth loop diagram with weakest link identified and experiment targeted.

### Step 5: Synthesize Results

After the experiment concludes, produce a results synthesis. This is a knowledge artifact, not just a metrics report.

- **Results summary table:**

| Metric | Control | Variant | Delta | Confidence | Verdict |
|---|---|---|---|---|---|
| [Target metric] | X | Y | +Z% | 95% CI [a, b] | Win / Loss / Inconclusive |
| [Guardrail 1] | X | Y | +Z% | 95% CI [a, b] | Pass / Fail |
| [Guardrail 2] | X | Y | +Z% | 95% CI [a, b] | Pass / Fail |

- **Interpretation:** What the results mean in plain language, not just statistical terms. "Users who saw the new onboarding flow were 15% more likely to complete their first project, with no degradation in retention."
- **Surprises:** What was unexpected? Surprises are the highest-signal findings.
- **Segment analysis:** Did the effect vary across user segments? Reference `user-segmentation` output for segment definitions.
- **Decision:** One of:
  - **Ship:** Roll out to 100%. Define the rollout plan.
  - **Iterate:** The direction is right but the effect is too small. Define what to change.
  - **Kill:** The hypothesis was wrong. Document the learning.
  - **Extend:** The results are inconclusive. Define what additional data is needed.
- **What we learned:** The single most important insight from this experiment, stated in one sentence. This feeds the team's institutional knowledge.

**Artifact:** Results synthesis saved as `applied/experiment-results-{name}.md`.

## Diagnostic Questions

1. **What is the riskiest assumption behind this feature?** If you cannot name the assumption, you cannot design an experiment to test it. Start with assumption mapping before experiment design.

2. **Do you have enough traffic to run an A/B test?** Calculate the required sample size before committing to an A/B test. If the answer is "we'll need 3 months," choose a different experiment type.

3. **What would make you NOT ship this feature?** If no experimental result would change the decision, the experiment is theater. Only experiment on decisions that are genuinely in question.

4. **Have you pre-registered your analysis plan?** If the analysis method is decided after seeing the data, you will find what you want to find. Pre-register the primary metric, the analysis method, and the success threshold.

5. **What is the opportunity cost of running this experiment?** Experiments consume engineering time, traffic, and attention. If the experiment takes a month and the answer is "probably yes," consider whether the learning is worth the delay.

6. **Is the experiment isolated?** If other changes are happening simultaneously (new marketing campaign, product redesign, seasonal effects), the experiment results may be confounded. Document concurrent changes and adjust interpretation accordingly.

## Common Mistakes

1. **Peeking at results before reaching sample size**
   The most common experimentation error. Checking results daily and stopping when they "look significant" inflates false positive rates to 30%+ from the intended 5%. Either use a sequential testing framework that accounts for multiple looks or commit to checking results only at the pre-planned sample size.

2. **Designing experiments without guardrails**
   An experiment that increases sign-ups by 20% but crashes retention by 10% is a net loss. Always define guardrail metrics before launch. If any guardrail is breached, the experiment fails regardless of the target metric.

3. **Using A/B tests for discovery**
   A/B tests optimize existing concepts. They are expensive and slow for discovering whether a concept is viable. Use fake doors, beta cohorts, or prototypes for discovery. Reserve A/B tests for optimizing validated concepts with clear metrics.

4. **Running too many experiments simultaneously**
   Each concurrent experiment splits traffic and introduces interaction effects. Most teams should run 1-3 experiments per product surface simultaneously, not 10. If you need more experiments, increase traffic or reduce the number of surfaces being tested.

5. **Ignoring segment effects**
   An experiment that is flat overall may be strongly positive for one segment and strongly negative for another. Always check for segment-level effects, especially across new vs. returning users, power users vs. casual users, and geographic regions.

6. **Treating inconclusive results as failure**
   An inconclusive result (confidence interval includes zero) is not a negative result. It means you did not have enough power to detect the effect size. Before declaring failure, check: was the sample size sufficient? Was the MDE set appropriately? Should you extend the experiment or redesign it?

## Context Integration

| Context Directory | How It Feeds This Skill |
|---|---|
| `context/products/` | **Step 1-3**: Provides baseline metrics, traffic volumes, and product architecture for experiment design. Informs whether A/B testing is feasible or whether lower-traffic methods are needed. |
| `context/verticals/` | **Step 4-5**: Provides segment definitions for growth loop design and segment analysis in results synthesis. |
| `context/competitive/` | **Step 1, 4**: Identifies competitive benchmarks for target metrics and growth loop patterns used by competitors. |
| `context/company/` | **Step 2-3**: Team size and engineering capacity determine how many experiments can run concurrently. Company stage informs experiment type selection (early-stage = beta cohorts, growth-stage = A/B tests). |
| `context/signals/` | **Step 1**: Community signals may reveal natural experiments or user behaviors that inform hypothesis generation. Check collection timestamps for freshness. |
