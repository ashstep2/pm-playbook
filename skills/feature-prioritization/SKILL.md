---
name: feature-prioritization
description: "Help users prioritize features using a weighted scoring matrix, RICE framework adaptation, and sequencing analysis to produce a ranked backlog, trade-off documentation, and a sequenced roadmap."
---

# Feature Prioritization

Produces a ranked feature backlog, trade-off documentation, and sequenced roadmap by combining weighted scoring, RICE-based impact analysis, and dependency-aware sequencing -- turning an unstructured list of feature ideas into a defensible plan with clear rationale for what ships first, what ships later, and what gets cut.

## Core Principles

1. **Classify the work before you prioritize it**
   "Every task you do as a PM falls into one of three categories: Leverage, Neutral, or Overhead. Before you build a prioritization framework, you need to know which category each item belongs to. A prioritization matrix full of Overhead tasks is a well-organized waste of time."
   -- *Shreyas Doshi, Former PM at Stripe, Twitter, Google, and Yahoo* ([source](https://twitter.com/shreyas/status/1492345002224279552))

   Most backlogs fail not because the scoring formula is wrong, but because they contain items that should never have been scored at all. Before scoring, classify every item as Leverage (disproportionate impact), Neutral (proportional effort-to-impact), or Overhead (necessary but not differentiating). Only Leverage and Neutral items enter the scoring matrix.

2. **Fall in love with the problem, not the solution**
   "The biggest mistake product teams make is they jump to solutions before they understand the problem. The best product teams are missionaries, not mercenaries -- they are driven by the problem and the impact, not by the feature."
   -- *Marty Cagan, Founder of Silicon Valley Product Group and author of Inspired and Empowered* ([source](https://www.svpg.com/missionaries-vs-mercenaries/))

   Every feature in the backlog should trace back to a customer problem, not a stakeholder request. When scoring features, evaluate the problem's severity and frequency first, then evaluate the proposed solution's effectiveness second. A brilliant solution to a minor problem always loses to a decent solution to a critical problem.

3. **Reach, Impact, Confidence, Effort -- in that order**
   "RICE is designed to reduce bias. Each component forces a different kind of honesty: Reach makes you estimate who this actually affects, Impact makes you commit to how much it matters, Confidence makes you admit what you don't know, and Effort makes you respect the cost."
   -- *Sean McBride, Former Product Lead at Intercom, originator of the RICE framework* ([source](https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/))

   RICE works because it separates four dimensions that PMs instinctively conflate. The most common error is inflating Impact to justify a pet feature while ignoring that Reach is narrow or Confidence is low. Score each dimension independently before computing the composite.

4. **If everything is important, nothing is**
   "Deciding what not to do is as important as deciding what to do. That's true for companies, and it's true for products. Focus is saying no to a hundred good ideas."
   -- *Des Traynor, Co-founder of Intercom* ([source](https://www.intercom.com/blog/product-strategy-means-saying-no/))

   A prioritization exercise that does not kill features has failed. The output must include an explicit "Not Doing" section with brief rationale. Stakeholders who see features cut with a clear reason are more aligned than stakeholders who see features ranked 47th out of 50 with no explanation.

5. **Sequence matters more than score**
   "The best PMs don't just pick the highest-impact features -- they sequence them so each one creates the conditions for the next. A well-sequenced roadmap compounds; a poorly sequenced one creates rework."
   -- *Ken Norton, Former Partner at Google Ventures and PM at Google* ([source](https://www.bringthedonuts.com/essays/leading-cross-functional-teams.html))

   Two features with identical scores can have very different optimal positions on a roadmap. Feature A might unlock infrastructure that makes Feature B cheaper to build. Feature C might be more impactful but requires hiring a specialist first. After scoring, the sequencing pass reorders the ranked list based on dependencies, compounding effects, and resource availability.

6. **Confidence is the most important and most ignored dimension**
   "High-confidence bets and low-confidence bets require different strategies. A high-confidence, high-impact feature should be committed. A low-confidence, high-impact feature should be tested before it's committed. The failure mode is treating both the same."
   -- *Teresa Torres, Author of Continuous Discovery Habits* ([source](https://www.producttalk.org/2021/08/opportunity-solution-trees/))

   When a feature scores high on Impact but low on Confidence, the correct next step is not to build it -- it is to design a cheap experiment to increase confidence. The prioritized backlog should include "validate" items for low-confidence features alongside "build" items for high-confidence features.

7. **Prioritization is a communication tool, not a decision tool**
   "The primary purpose of a prioritization framework is not to produce the mathematically optimal ranking. It is to make your reasoning legible to your team and stakeholders so they can disagree productively instead of politically."
   -- *Lenny Rachitsky, Author of Lenny's Newsletter and former PM at Airbnb* ([source](https://www.lennysnewsletter.com/p/my-favorite-product-management-templates))

   The ranked list is less valuable than the trade-off documentation that accompanies it. Every prioritization decision embeds an assumption about what matters most. Making those assumptions explicit -- "we scored retention higher than acquisition because churn is currently 8% monthly" -- turns disagreements about rankings into productive debates about strategy.

8. **Cost of delay is the hidden variable**
   "Most prioritization frameworks evaluate features in isolation. But features have a time dimension: the cost of not doing something grows or shrinks over time. A feature that prevents churn has a compounding cost of delay; a nice-to-have enhancement has a flat cost of delay."
   -- *Joshua Arnold, Creator of the Weighted Shortest Job First (WSJF) concept, adapted from Don Reinertsen's Principles of Product Development Flow* ([source](https://www.amazon.com/Principles-Product-Development-Flow-Generation/dp/1935401009))

   After computing scores, apply a cost-of-delay lens: which features become significantly more expensive or less valuable if delayed by one quarter? Features with high cost of delay should be promoted in the final sequencing, even if their raw score is not the highest.

## Instructions

### Step 1: Gather and Classify the Raw Feature List

- Collect all feature candidates from every source: user feedback, stakeholder requests, engineering proposals, competitive moves, internal ideas, and strategic initiatives.
- For each item, capture: name, one-sentence description, original requester, and originating source.
- Apply Shreyas Doshi's LNO classification to every item:
  - **L (Leverage)**: Disproportionate impact relative to effort. These are prioritization candidates.
  - **N (Neutral)**: Impact roughly proportional to effort. These are prioritization candidates.
  - **O (Overhead)**: Necessary operational work (tech debt, compliance, maintenance). These skip scoring and go into a separate maintenance track.
- Remove duplicates and merge related items into coherent features.
- **Artifact produced**: Classified Feature List (table with name, description, source, LNO class).

### Step 2: Define Scoring Criteria and Weights

- Establish 4-6 scoring dimensions. The default RICE-based set:

| Dimension | Definition | Scale | Default Weight |
|---|---|---|---|
| **Reach** | Number of users/customers affected per quarter | 0.5 (few) to 3 (most users) | 20% |
| **Impact** | Degree of improvement for each affected user | 0.25 (minimal) to 3 (transformative) | 30% |
| **Confidence** | How certain you are about Reach and Impact estimates | 0.5 (speculation) to 1.0 (high confidence, validated data) | 15% |
| **Strategic Alignment** | How directly the feature advances the stated product strategy | 1 (tangential) to 5 (core to strategy) | 20% |
| **Effort** | Person-weeks to ship (used as divisor, not multiplier) | Estimated in person-weeks | 15% (inverse) |

- Adjust weights based on the company's current strategic priorities. Document why each weight was chosen.
- If stakeholders disagree on weights, that disagreement is the most valuable output of this step -- surface it and resolve it before scoring.
- **Artifact produced**: Scoring Criteria Table with definitions, scales, and agreed-upon weights.

### Step 3: Score Every Feature

- Score each L and N feature across all dimensions.
- Compute the weighted score: `Score = (Reach * w1 + Impact * w2 + Confidence * w3 + Strategic Alignment * w4) / Effort`
- For each score, record a one-sentence rationale explaining the rating. This is not optional -- unexplained scores invite political re-scoring later.
- Flag any feature where Confidence is below 0.5 and annotate it as "Validate Before Committing."
- Sort the list by weighted score, descending.
- **Artifact produced**: Scored Feature Matrix (table with all dimensions, computed score, rationale per dimension, and rank).

### Step 4: Document Trade-Offs

- For the top 10 features, write a trade-off summary that answers:
  - What are we choosing to do by building this?
  - What are we choosing NOT to do as a consequence (opportunity cost)?
  - What assumption, if wrong, would change this feature's priority?
- For the bottom quartile (features being cut or deferred), write a one-line rationale visible to stakeholders: "Not doing X because Y."
- Group deferred features into: "Next quarter candidates," "Revisit if conditions change," and "Explicitly declined."
- **Artifact produced**: Trade-Off Documentation (narrative for top 10, rationale table for deferred items, and the explicit "Not Doing" list).

### Step 5: Apply Cost-of-Delay Analysis

- For the top 15 features from Step 3, estimate the cost of delay by answering: "What happens if this feature ships 3 months later than planned?"
- Classify each feature's cost-of-delay profile:
  - **Urgent**: Cost grows rapidly (e.g., churn accelerating, compliance deadline, competitive window closing)
  - **Standard**: Cost grows linearly (e.g., steady user pain, gradual competitive erosion)
  - **Fixed-date**: Value drops to near-zero after a specific date (e.g., conference demo, partner launch)
  - **Low**: Minimal penalty for delay (e.g., nice-to-have improvements)
- Re-rank features within their score tier using cost of delay as a tiebreaker. Urgent and Fixed-date features move up; Low-delay features move down.
- **Artifact produced**: Cost-of-Delay Classification Table (feature, delay profile, rationale, adjusted rank).

### Step 6: Sequence the Roadmap

- Take the re-ranked list from Step 5 and apply sequencing constraints:
  - **Dependencies**: Feature B requires Feature A's infrastructure. A must ship first regardless of score.
  - **Compounding effects**: Feature C makes Feature D 2x more valuable. Sequence C before D.
  - **Resource constraints**: Only one ML engineer available. ML-dependent features cannot run in parallel.
  - **Learning gates**: Low-confidence features get a "validate" milestone before "build" milestone.
- Assign features to time horizons:
  - **Now (this quarter)**: Top 3-5 features. Committed.
  - **Next (next quarter)**: Next 3-5 features. Planned but flexible.
  - **Later (6+ months)**: Remaining prioritized features. Directional only.
  - **Not Doing**: Explicitly declined features with rationale.
- Produce a visual roadmap (text-based timeline) showing sequencing, dependencies, and the "validate vs. build" distinction.
- **Artifact produced**: Sequenced Roadmap (timeline with features, dependencies, and time horizons) saved as `applied/prioritized-roadmap-{product}.md`.

### Step 7: Write the Prioritization Rationale Memo

- Compile all artifacts into a single decision document:
  1. Executive summary (one paragraph: what we are building, what we are not, and why)
  2. Scoring Criteria and Weights (from Step 2)
  3. Scored Feature Matrix (from Step 3)
  4. Trade-Off Documentation (from Step 4)
  5. Cost-of-Delay Analysis (from Step 5)
  6. Sequenced Roadmap (from Step 6)
  7. Open questions and low-confidence items requiring validation
- This memo is the artifact that stakeholders review. It should make the reasoning so transparent that disagreements become specific ("I think Reach for Feature X is 2, not 1") rather than political ("Why isn't my feature on the roadmap?").
- **Artifact produced**: Prioritization Rationale Memo saved as `applied/prioritization-rationale-{product}.md`.

## Diagnostic Questions

1. **Do you have a written product strategy?** Prioritization without strategy is just opinion-sorting. If no strategy exists, the weighted scoring will lack an anchor for the Strategic Alignment dimension. Consider running the `product-portfolio-strategy` skill first.

2. **How many features are on your backlog right now?** If the answer is over 50, classification (Step 1) is essential to reduce noise before scoring. If under 10, you may be under-collecting inputs and should broaden your sources.

3. **Who are the stakeholders who need to agree with this prioritization?** Identify them now. The scoring weights (Step 2) should reflect their input, and the trade-off documentation (Step 4) should preemptively address their likely objections.

4. **What percentage of your current roadmap is reactive versus proactive?** If more than 40% of your backlog originated from stakeholder escalations or competitive reactions, the prioritization process needs to reweight toward strategic alignment and away from recency bias.

5. **Do you have data on feature usage for your existing product?** If yes, use it to calibrate Reach and Impact scores with evidence rather than estimates. If no, lower the Confidence scores across the board and add validation milestones.

6. **Is there a hard deadline driving any of these features?** Fixed-date features (partner launches, regulatory deadlines, conference demos) need special handling in the cost-of-delay analysis. Identify them upfront so they are not buried in the general scoring.

7. **Have you killed a feature in the last quarter?** If the answer is no, the prioritization process may be functioning as a rubber stamp rather than a filter. A healthy backlog has a "Not Doing" list that grows alongside the roadmap.

## Common Mistakes

1. **Scoring without agreed-upon weights**
   When dimensions are unweighted, every stakeholder mentally applies their own weights, then disputes the output. The most important step is getting explicit agreement on weights before anyone sees a score. If stakeholders cannot agree on weights, that disagreement is the real prioritization conversation -- have it openly instead of letting it corrupt the scores silently.

2. **Treating the score as the decision**
   The weighted score is an input to judgment, not a replacement for it. Two features with scores of 7.2 and 7.0 are effectively tied -- the score does not break that tie, context does. Use the score to separate the top quartile from the bottom quartile, then apply sequencing logic and strategic judgment within tiers.

3. **Ignoring cost of delay**
   Static scoring evaluates features as if time does not exist. A feature that prevents 5% monthly churn has a compounding cost of delay that a static score will not capture. Always apply the cost-of-delay pass after initial scoring, especially for features tied to retention, compliance, or competitive windows.

4. **Re-scoring to justify a predetermined outcome**
   If a senior stakeholder's preferred feature lands low on the matrix and the team adjusts scores upward to accommodate, the framework has failed. The correct response is to surface the disagreement: "This feature scores low on Reach and Impact. If we believe it should be prioritized anyway, we should articulate the strategic reason and document it as a judgment override, not inflate the scores."

5. **Skipping the "Not Doing" list**
   A prioritized roadmap without an explicit "Not Doing" section is incomplete. Stakeholders whose features are deferred need to see a clear rationale, not silence. The "Not Doing" list also serves as institutional memory: when the same feature is proposed again next quarter, the team can reference the prior rationale and decide whether conditions have changed.

6. **Prioritizing once and never revisiting**
   Prioritization is not a quarterly ceremony -- it is a living process. New information (a competitor launch, a churn spike, a key customer request) can change scores overnight. Build a cadence: full re-prioritization quarterly, lightweight re-scoring monthly for the top 10 items.

## Context Integration

This skill uses the `context/` directory to ground scoring decisions in evidence rather than opinion:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3 | Product descriptions, current feature set, pricing, and technical architecture. Informs what is already built (avoid duplicating existing capabilities), calibrates Effort estimates based on technical complexity, and anchors the Strategic Alignment dimension to the stated product vision. |
| `context/verticals/` | Steps 2, 3, 5 | Target market segments, TAM/SAM/SOM, and use cases. Calibrates Reach scores by grounding them in market size data. Identifies vertical-specific deadlines or competitive windows that feed cost-of-delay analysis. |
| `context/competitive/` | Steps 3, 4, 5 | Competitor product capabilities and roadmap signals. Informs Impact scoring (does this feature close a competitive gap or extend a lead?), feeds trade-off documentation (what happens if we don't build this and a competitor does?), and identifies features with urgent cost of delay due to competitive pressure. |
| `context/company/` | Steps 2, 6 | Team size, engineering capacity, and resource constraints. Essential for calibrating Effort scores, identifying resource bottlenecks in sequencing, and setting realistic time horizons for the roadmap. |
| `context/founders/` | Step 2 | Founder priorities and strategic vision. Informs the weighting of the Strategic Alignment dimension and ensures the scoring criteria reflect leadership's stated direction. |
| `context/signals/` | Steps 1, 3, 5 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `github-ecosystem.md` for developer demand signals (issues, feature requests), `hackernews-sentiment.md` and `reddit-discussions.md` for user pain points that validate Reach and Impact estimates, and `news-coverage.md` for competitive timing signals that feed cost-of-delay. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A brief description of their product and its current state
2. The raw list of feature candidates with sources
3. Any known constraints (team size, deadlines, dependencies)
4. The product strategy or top 3 strategic priorities for the current period
