---
name: user-onboarding-optimization
description: "Help users audit and optimize their product's onboarding flow by mapping the user journey, measuring time-to-value, defining activation metrics, identifying friction points, and producing an improvement roadmap."
version: "1.0.0"
last_updated: "2026-02-06"
---

# User Onboarding Optimization

Produces an onboarding funnel analysis, time-to-value measurement, activation metric definition, friction map, and a prioritized improvement roadmap -- turning a leaky new-user experience into a repeatable path to the product's "aha moment."

## Core Principles

1. **People do not want your product -- they want a better version of themselves**
   "People don't buy products; they buy better versions of themselves. When you're trying to win customers, are you listing the attributes of the flower or describing how awesome it is to throw fireballs?"
   -- *Samuel Hulick, Founder of UserOnboard* ([source](https://www.useronboard.com/features-vs-benefits/))

   Onboarding is not a product tour. It is the bridge between a user's current struggle and the outcome they signed up to achieve. Every screen, tooltip, and email must advance the user toward that outcome or be removed.

2. **Activation is the moment the user experiences value, not the moment they complete setup**
   "The most important thing is to identify the 'aha moment' -- the moment when a user first experiences the core value of your product. Everything in onboarding should be designed to get users to that moment as quickly as possible."
   -- *Chamath Palihapitiya, Former VP of Growth at Facebook* ([source](https://www.youtube.com/watch?v=raIUQP71SBU))

   Facebook's growth team discovered that users who added 7 friends in 10 days retained at dramatically higher rates. The onboarding insight was not "get users to complete their profile" but "get users to the aha moment." Find your equivalent.

3. **Reduce time-to-value before you optimize anything else**
   "Time-to-value is the North Star of onboarding. The faster users experience value, the more likely they are to stick around. If your TTV is measured in days, you're losing users by the hour."
   -- *Wes Bush, Founder of ProductLed and author of Product-Led Growth* ([source](https://productled.com/blog/time-to-value))

4. **Bowling alley onboarding: use bumpers, not instructions**
   "The best onboarding creates a bowling alley experience -- set up bumpers (product defaults, smart constraints, progressive disclosure) so users can't fail, rather than giving them a manual for how to bowl."
   -- *Ramli John, Author of Product-Led Onboarding and Managing Director at ProductLed* ([source](https://www.productledonboarding.com/))

   Instead of explaining features, design the product so that the next right action is the most obvious one. Defaults, templates, and pre-populated data are bumpers. Tooltips and walkthroughs are instructions -- use them only when bumpers are not possible.

5. **Measure the setup experience like a product, not a funnel**
   "The most common mistake in SaaS onboarding is treating it as a one-time funnel instead of a product experience that compounds. The best companies instrument onboarding as carefully as they instrument their core product."
   -- *Hiten Shah, Co-founder of KISSmetrics and Crazy Egg* ([source](https://hitenism.com/saas-onboarding/))

6. **Successful onboarding is a conversation, not a monologue**
   "Great onboarding asks questions. It segments users by intent and adapts the path accordingly. A developer evaluating an API and a product manager exploring a demo need completely different first five minutes."
   -- *Claire Suellentrop, Co-founder of Forget The Funnel* ([source](https://forgetthefunnel.com/))

   The first question you ask a new user is more important than the first thing you show them. Use welcome surveys, role selectors, or intent questions to route users to the fastest path to their specific aha moment.

7. **Friction is not always bad -- remove the wrong friction**
   "Don't remove all friction from onboarding. Remove unproductive friction (confusing UI, unnecessary steps, jargon) but keep productive friction (asking users to make a meaningful choice that improves their experience). The goal is not zero friction -- it is zero wasted friction."
   -- *Nir Eyal, Author of Hooked and Indistractable* ([source](https://www.nirandfar.com/friction/))

8. **The first run experience IS the product for new users**
   "You never get a second chance to make a first impression. For most SaaS products, 40-60% of users who sign up will never return after their first session. Your first-run experience is not a nice-to-have -- it is the highest-leverage surface in your entire product."
   -- *Patrick Campbell, Founder of ProfitWell (acquired by Paddle)* ([source](https://www.profitwell.com/recur/all/first-run-experience))

## Instructions

### Step 1: Map the Current Onboarding Funnel

Document every step a new user takes from first touchpoint to activation. Be exhaustive -- include steps that feel trivial.

- **Start**: Where does the user first encounter the product? (Ad, blog post, referral, docs page, GitHub repo)
- **Sign-up**: What information is collected? How many fields? Is there social/SSO login?
- **Verification**: Email confirmation, phone verification, waitlist, approval queue?
- **First screen**: What does the user see after sign-up? Empty state, dashboard, wizard, tutorial?
- **First action**: What is the first thing the product asks the user to do?
- **Aha moment**: At what point does the user experience the core value proposition?
- **Habit formation**: What brings the user back for a second session?

Produce a sequential flow diagram (as a numbered list or table) with each step, the user action required, the estimated time, and the drop-off risk (low / medium / high).

**Artifact produced**: Onboarding Funnel Map -- a step-by-step table documenting the current new-user journey with estimated time and drop-off risk per step.

### Step 2: Measure Time-to-Value (TTV)

Calculate the elapsed time from sign-up to the moment the user first experiences the core value of the product.

- Define the **value moment** explicitly. This is not "completed setup" -- it is the action that delivers the promise. Examples: "Generated their first 3D world," "Sent their first API request and received a response," "Saw their first dashboard with real data."
- Measure TTV in three ways:
  - **Clock time**: Wall-clock minutes from account creation to value moment
  - **Active time**: Minutes the user is actively engaged (excludes waiting, processing)
  - **Step count**: Number of discrete actions required to reach value
- If analytics data is available, pull median and P90 TTV. If not, walk through the flow yourself and time it.
- Benchmark against the user's expectation. A user arriving from a "generate a 3D world in 30 seconds" ad who waits 5 minutes feels friction; a user arriving from a technical whitepaper who waits 5 minutes does not.

| TTV Metric | Current Value | Target Value | Gap |
|---|---|---|---|
| Clock time to value moment | | | |
| Active time to value moment | | | |
| Steps to value moment | | | |

**Artifact produced**: Time-to-Value Measurement -- a table with current TTV, target TTV, and the gap for each measurement dimension.

### Step 3: Define the Activation Metric

Define a single, measurable activation metric that predicts long-term retention. This is the onboarding equivalent of Facebook's "7 friends in 10 days."

- **Method**: Correlate early user behaviors with 30-day (or 60-day) retention. Identify which specific action, completed within what timeframe, is most predictive of a user becoming a retained user.
- If you lack retention data, use the "would you be disappointed?" proxy: which early action, if a user failed to complete it, would make them most likely to churn?
- The activation metric must be:
  - **Specific**: A discrete, observable action (not "engaged with the product")
  - **Time-bounded**: Completed within a defined window (e.g., within 7 days of sign-up)
  - **Predictive**: Users who complete it retain at 2x+ the rate of those who do not
  - **Influenceable**: The product team can design interventions to increase the completion rate

| Component | Definition |
|---|---|
| Activation action | [e.g., "Created and viewed a generated 3D world"] |
| Time window | [e.g., "Within 3 days of sign-up"] |
| Current activation rate | [e.g., "34% of sign-ups"] |
| Target activation rate | [e.g., "55% of sign-ups within 90 days"] |
| Retention correlation | [e.g., "Activated users retain at 68% vs. 12% for non-activated"] |

**Artifact produced**: Activation Metric Definition -- a specification of the activation action, time window, current rate, target rate, and retention correlation.

### Step 4: Build the Friction Map

Walk through the onboarding funnel from Step 1 and identify every source of friction. Classify each friction point:

**Friction types:**
- **Cognitive friction**: User does not understand what to do or why ("What does this button do?")
- **Technical friction**: Something does not work or is slow (error, timeout, broken link, loading state)
- **Emotional friction**: User feels uncertain, anxious, or overwhelmed (too many choices, unclear pricing, fear of breaking something)
- **Process friction**: Unnecessary steps that do not contribute to the value moment (forced email verification before any value, mandatory profile completion, multi-page forms)
- **Productive friction**: Friction that improves the experience (role selector that personalizes the path, API key creation that enables real usage). Do NOT remove this.

For each friction point, document:

| Step | Friction Point | Type | Severity (1-5) | Evidence | Remove or Redesign? |
|---|---|---|---|---|---|
| e.g., Step 3 | Email verification required before any product access | Process | 4 | 23% drop-off at this step | Redesign: allow limited access before verification |

**Artifact produced**: Friction Map -- a scored table of every friction point in the onboarding flow, classified by type and severity.

### Step 5: Design Activation Experiments

For the top 5 friction points from the Friction Map (sorted by severity), design a specific experiment to reduce or eliminate the friction.

Each experiment must include:

- **Hypothesis**: "If we [change], then [metric] will improve by [amount] because [reasoning]."
- **Change description**: What specifically will be different in the user experience.
- **Success metric**: The specific number that determines whether the experiment worked.
- **Effort estimate**: T-shirt size (S/M/L) for implementation.
- **Risk**: What could go wrong or what trade-off is being made.

Prioritize experiments using an ICE framework:

| Experiment | Impact (1-10) | Confidence (1-10) | Ease (1-10) | ICE Score | Priority |
|---|---|---|---|---|---|
| e.g., Replace 5-field sign-up with Google SSO | 7 | 8 | 6 | 336 | 1 |

**Artifact produced**: Experiment Backlog -- a prioritized table of 5 onboarding experiments with hypotheses, success metrics, and ICE scores.

### Step 6: Produce the Improvement Roadmap

Sequence the experiments from Step 5 into a phased roadmap:

**Phase 1 -- Quick wins (Week 1-2):** Small-effort, high-confidence experiments that can ship immediately. Typically: copy changes, default adjustments, removing unnecessary steps.

**Phase 2 -- Structural improvements (Week 3-6):** Medium-effort experiments that require design or engineering work. Typically: flow redesign, progressive disclosure, personalized paths.

**Phase 3 -- System investments (Week 7-12):** Large-effort changes that require instrumentation, A/B testing infrastructure, or architectural changes. Typically: event-based onboarding emails, in-app guidance systems, lifecycle automation.

For each phase, define:
- The experiments included and their expected activation rate impact
- The resources required (engineering days, design support)
- The measurement plan (what to track, when to evaluate)
- The decision criteria for moving to the next phase

**Artifact produced**: Onboarding Improvement Roadmap -- a phased plan with experiments, timelines, resource requirements, and success criteria, saved as `applied/onboarding-roadmap-{product}.md`.

### Step 7: Compile the Onboarding Audit Report

Assemble all artifacts from Steps 1-6 into a single document:

1. Executive Summary (one paragraph: the current state of onboarding, the biggest opportunity, and the expected impact)
2. Onboarding Funnel Map (Step 1)
3. Time-to-Value Measurement (Step 2)
4. Activation Metric Definition (Step 3)
5. Friction Map (Step 4)
6. Experiment Backlog (Step 5)
7. Improvement Roadmap (Step 6)
8. Recommended immediate actions (top 3 things to do this week)

**Artifact produced**: Onboarding Audit Report -- the complete compiled document, saved as `applied/onboarding-audit-{product}.md`.

## Diagnostic Questions

1. **Can you describe the "aha moment" for your product in one sentence?** If not, you need to define it before optimizing onboarding. The aha moment is the foundation -- everything else is a path to it.

2. **What percentage of users who sign up complete the core value action within their first session?** If you do not know this number, instrumenting your onboarding funnel is the first step, not redesigning it.

3. **How long does it take a new user to go from sign-up to experiencing value?** Time it yourself. If TTV exceeds the user's patience threshold for your product category (seconds for a consumer app, minutes for a developer tool, hours for enterprise software), you are losing users to impatience, not to competitors.

4. **Where is the single biggest drop-off in your sign-up-to-activation funnel?** If you do not have funnel data, watch 5 users go through onboarding on a screen share. The biggest friction point will be obvious.

5. **Does your onboarding treat all users the same, or does it adapt based on role, intent, or experience level?** A developer and a designer arriving at the same product need different first five minutes. If you serve them identically, at least one group is getting a suboptimal experience.

6. **What happens when a new user opens your product and does nothing?** The empty state is one of the most neglected surfaces in product design. If a new user sees a blank dashboard with no guidance, your onboarding has a hole.

7. **Are you measuring onboarding success by completion of a setup wizard, or by the user achieving an outcome?** Wizard completion is a vanity metric. The only onboarding metric that matters is whether the user experienced the value that brought them to the product.

## Common Mistakes

1. **Optimizing the tour instead of the path to value**
   Product tours, tooltips, and walkthrough modals are band-aids for a confusing product, not a substitute for good onboarding design. If you need a 7-step tooltip tour to explain your first screen, the first screen is wrong. Redesign the experience so the next action is obvious without instruction, then use tours only for non-obvious power features.

2. **Measuring onboarding completion instead of activation**
   "100% of users completed the setup wizard" is meaningless if only 20% went on to use the product. The setup wizard is a means, not an end. Measure the outcome (activation rate, TTV) not the process (wizard completion rate, tooltip click-through rate).

3. **Forcing all users through the same linear flow**
   A developer evaluating an API, a product manager exploring a demo, and an enterprise buyer running a security review have fundamentally different needs in their first session. Segment users at the start and route them to different paths. One-size-fits-all onboarding fits no one well.

4. **Front-loading data collection before delivering value**
   Every form field, verification step, and profile question between sign-up and value is a toll booth. Each toll booth costs you users. Collect only what is strictly necessary to deliver the first value moment, then gather additional information progressively as the user engages.

5. **Ignoring the return-user onboarding experience**
   Onboarding does not end at activation. Users who activated but did not return within 7 days need a re-engagement experience that is different from both the new-user flow and the active-user flow. Design for the "day 8 return" as deliberately as you design for day 1.

6. **Treating onboarding as a project instead of a product**
   Onboarding is not something you build once and ship. It is a product surface that needs continuous measurement, experimentation, and iteration. The best onboarding teams run 2-3 experiments per month on the new-user flow indefinitely.

## Context Integration

This skill uses the `context/` directory to ground the audit in company-specific data:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3, 7 | Product descriptions, feature lists, pricing tiers, and technical architecture. Used to map the onboarding funnel accurately, identify the value moment, and define the activation metric. If product files describe the intended user journey, use that as the baseline for the funnel map. |
| `context/verticals/` | Steps 1, 4, 5 | Target market information, user personas, and use cases. Different verticals have different TTV expectations and friction tolerances. A gaming developer expects instant gratification; a robotics engineer expects a setup process. Use vertical context to calibrate friction severity ratings and experiment prioritization. |
| `context/company/` | Steps 5, 6 | Company stage, team size, and resource constraints. A 5-person startup cannot run 3 parallel A/B tests -- the roadmap should sequence experiments. A larger team can parallelize. Use company context to make the improvement roadmap realistic. |
| `context/competitive/` | Steps 2, 4 | Competitor onboarding flows and TTV benchmarks. If competitors offer a faster path to value, your TTV target must match or beat them. Competitor friction points are opportunities -- if a competitor requires a 10-step setup, your 3-step alternative is a differentiator. |
| `context/founders/` | Step 3 | Founder vision and product philosophy. The activation metric should align with what the founders believe is the core value of the product. If founders emphasize "spatial intelligence accessible to everyone," the activation metric should reflect accessibility, not power-user depth. |
| `context/signals/` | Steps 1, 4 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `reddit-discussions.md` and `hackernews-sentiment.md` to identify onboarding pain points mentioned by real users. Use `github-ecosystem.md` to spot documentation gaps or common first-issue patterns that indicate onboarding friction. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A description of their product and its core value proposition
2. The intended user persona and their primary job-to-be-done
3. A walkthrough of the current sign-up-to-activation flow (or a link to the product)
4. Any existing funnel data or user feedback on the onboarding experience
