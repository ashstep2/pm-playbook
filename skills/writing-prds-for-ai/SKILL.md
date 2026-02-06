---
name: writing-prds-for-ai
description: "Help users write PRDs for AI/ML-powered products that handle model uncertainty, define evaluation criteria instead of deterministic specs, bridge the research-to-product gap, and specify behavior for probabilistic outputs."
---

# Writing PRDs for AI

Produces a complete product requirements document tailored for AI/ML-powered products -- one that replaces deterministic feature specs with evaluation criteria, accounts for probabilistic outputs, defines acceptable failure modes, and bridges the gap between what research promises and what production delivers.

## Core Principles

1. **Spec the outcome, not the algorithm**
   "Fall in love with the problem, not the solution. If you're anchored to a specific solution, you'll miss the opportunity to explore better ones."
   -- *Marty Cagan, Partner at Silicon Valley Product Group and author of Inspired* ([source](https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/))

   AI PRDs fail when they specify "use a transformer model with 7B parameters" instead of "the system must identify the correct object in the scene at least 90% of the time." Specify the user outcome and the evaluation bar. Let the ML team choose the approach.

2. **Write specs that assume the model will be wrong**
   "The most important thing to understand about ML systems is that they will fail, and they will fail in ways that are hard to predict."
   -- *Josh Tobin, Co-founder of Gantry (prev. Research Scientist at OpenAI)* ([source](https://fullstackdeeplearning.com/course/2022/lecture-11-ml-teams/))

   Every AI PRD must define what happens when the model produces a wrong, low-confidence, or adversarial output. The fallback behavior IS the product as much as the happy path. If the PRD does not specify failure modes, engineering will invent them ad hoc.

3. **Replace acceptance criteria with evaluation frameworks**
   "Traditional software is tested for correctness. ML systems must be tested for acceptable performance across distributions."
   -- *Eugene Yan, Senior Applied Scientist at Amazon* ([source](https://eugeneyan.com/writing/testing-ml/))

   Deterministic software either passes or fails a test. AI products live on a performance curve. The PRD must define the evaluation dataset, the metrics (precision, recall, latency, cost), and the acceptable thresholds -- not just "it should work."

4. **Close the gap between the demo and the product**
   "There is a large gap between a demo that works on a handful of examples and a product that works reliably. Most of the work in ML is in that gap."
   -- *Hamel Husain, ML engineer and creator of nbdev* ([source](https://hamel.dev/blog/posts/evals/))

   Research demos cherry-pick inputs. Products must handle the full distribution. The PRD must explicitly call out the difference between "works in the demo" and "works in production" by defining edge cases, data distributions, and scale requirements.

5. **Define the spec as a living contract, not a static document**
   "The best specs are written to be rewritten. A spec that cannot be updated without a two-week approval process is a spec that will be ignored."
   -- *Shreyas Doshi, PM advisor and former PM leader at Stripe, Twitter, and Google* ([source](https://twitter.com/shreyas/status/1306302113068994561))

   AI capabilities change faster than traditional software. The PRD for an AI product must include a versioning strategy and explicit triggers for when the spec should be revisited -- for example, when a new model becomes available, when eval metrics shift, or when user behavior data reveals new patterns.

6. **Treat data as a first-class requirement**
   "Data is the most undervalued and de-glamorized aspect of AI."
   -- *Andrew Ng, Founder of DeepLearning.AI and Coursera* ([source](https://www.deeplearning.ai/the-batch/issue-129/))

   Most AI PRDs specify model behavior but ignore data requirements entirely. The PRD must define: what training/eval data exists, what data must be collected, what data quality bar is required, what labeling process will be used, and what data privacy constraints apply. Without these, engineering cannot estimate feasibility.

7. **Make the cost of intelligence explicit**
   "People underestimate how much of ML product work is managing latency, cost, and reliability tradeoffs rather than improving model quality."
   -- *Lenny Rachitsky, Author of Lenny's Newsletter, summarizing a pattern from interviews with AI PMs* ([source](https://www.lennysnewsletter.com/p/what-ai-pms-do-differently))

   Every AI feature has a cost: API calls, GPU compute, latency, token usage. The PRD must state the cost budget per inference, the acceptable latency, and the fallback if cost exceeds the budget. A feature that is technically possible but economically unviable is not a shippable feature.

8. **Ship the human-in-the-loop version first**
   "The fastest way to ship an AI product is to ship a human-in-the-loop product first, then gradually automate as confidence grows."
   -- *Josh Tobin, Co-founder of Gantry, from Full Stack Deep Learning course* ([source](https://fullstackdeeplearning.com/course/2022/lecture-11-ml-teams/))

   The PRD should define an automation ladder: what starts as fully manual, what moves to human-assisted (model suggests, human confirms), and what eventually becomes fully automated. This lets you ship faster, collect training data from human decisions, and build trust incrementally.

## Instructions

### Step 1: Define the AI-Specific Problem Statement

Write a problem statement that separates the user problem from the AI approach. Produce:

- **User problem:** What the user cannot do today, or what takes too long, stated without referencing AI or ML.
- **Why AI:** Why this problem requires a probabilistic/learned approach rather than deterministic logic. If you cannot answer this, the feature may not need AI.
- **Current baseline:** How users solve this today (manual process, existing tool, workaround). This becomes the bar the AI solution must clear.
- **Success from the user's perspective:** What "good enough" looks like to the user, in their words, not in model metrics.

**Output:** A problem statement document (1 page) saved as `applied/ai-prd-problem-{product}.md`.

If `context/products/` files exist, pull the product description and current capabilities. If `context/verticals/` files exist, pull the target user and use case context.

### Step 2: Write the Evaluation Criteria (replacing traditional acceptance criteria)

For each AI-powered capability in the PRD, define:

| Dimension | Specification |
|-----------|--------------|
| **Primary metric** | e.g., precision@90% recall, BLEU score, user satisfaction rating |
| **Eval dataset** | What data will you test against? How large? How representative? |
| **Threshold: Ship** | The minimum bar to launch (e.g., "85% accuracy on eval set") |
| **Threshold: Iterate** | Below this, do not ship -- iterate on the model |
| **Latency budget** | p50 and p99 latency requirements |
| **Cost budget** | Max cost per inference or per user session |
| **Eval cadence** | How often evals are re-run (every PR, nightly, weekly) |

For generative AI products specifically, add:
- **Quality rubric:** A human-evaluation rubric with 3-5 dimensions (e.g., relevance, coherence, factual accuracy, safety) each scored 1-5.
- **Regression definition:** What constitutes a regression vs. acceptable variance between model versions.

**Output:** An evaluation criteria table for each AI capability.

### Step 3: Specify Failure Modes and Fallback Behaviors

For each AI capability, enumerate the failure modes and define the product response:

| Failure Mode | Detection Method | User Experience | Fallback Behavior |
|-------------|-----------------|-----------------|-------------------|
| Low-confidence output | Confidence score < threshold | Show result with caveat/disclaimer | Offer manual alternative |
| Adversarial/out-of-distribution input | Input validation + anomaly detection | Block gracefully with explanation | Suggest valid input format |
| Model timeout / service unavailable | Latency exceeds budget | Loading state, then graceful degradation | Cache last-known-good or show static fallback |
| Harmful/unsafe output | Safety classifier | Suppress output entirely | Show generic safe response |
| Hallucination / factual error | Grounding check against source data | Flag as unverified | Link to source material |

The principle: every cell in the "User Experience" column must describe a designed experience, not a blank screen or a stack trace.

**Output:** A failure mode table for each AI capability, saved as part of the PRD.

### Step 4: Define the Data Requirements

Produce a data requirements section covering:

- **Training data:** What data is needed to train/fine-tune? Does it exist? What is the labeling cost and timeline?
- **Evaluation data:** What held-out data will be used for evals? How will you prevent data leakage?
- **Runtime data:** What data does the model need at inference time? Where does it come from? What is the freshness requirement?
- **Data quality bar:** What quality checks must data pass before use? (deduplication, bias audits, PII removal)
- **Data privacy and compliance:** What regulations apply (GDPR, CCPA, SOC2)? What data cannot leave certain boundaries?
- **Data collection plan:** If training data does not yet exist, how will the human-in-the-loop version (Step 6) generate it?

**Output:** A data requirements document. If `context/products/` or `context/company/` files specify data constraints, incorporate them.

### Step 5: Specify the Model Behavior Contract

Write a "model behavior contract" that engineering and PM agree on. This replaces the traditional functional spec:

- **Input specification:** What inputs the model accepts, with format, size limits, and validation rules.
- **Output specification:** What the model returns, including structure, confidence scores, and metadata.
- **Behavioral invariants:** Properties that must always hold regardless of model version (e.g., "never generate content involving minors," "always return a result within 5 seconds," "output must be valid JSON").
- **Known limitations:** What the model explicitly does NOT handle, documented so users and downstream systems do not depend on unsupported behavior.
- **Versioning strategy:** How model versions are tracked, how A/B tests are structured, and what the rollback procedure is when a new model underperforms.

**Output:** A model behavior contract document.

### Step 6: Design the Automation Ladder

Define the progression from manual to fully automated:

| Level | Description | Trigger to Advance | Metrics Required |
|-------|-------------|--------------------|--------------------|
| **L0: Manual** | Humans perform the task entirely | Baseline data collected | Task completion rate, time-per-task |
| **L1: Assisted** | Model suggests, human reviews and approves | Model accuracy > X% on eval set | Acceptance rate, override rate |
| **L2: Supervised** | Model acts, human spot-checks a sample | Override rate < Y% for Z weeks | Error rate on unreviewed outputs |
| **L3: Autonomous** | Model acts independently, human reviews exceptions only | Error rate < W% for Z weeks | Exception rate, user-reported error rate |

For each AI capability in the PRD, identify the launch level and the criteria for advancing. Most AI features should launch at L1 or L2, not L3.

**Output:** An automation ladder table for each capability, saved as part of the PRD.

### Step 7: Assemble the Complete AI PRD

Compile all artifacts into a single document with the following structure:

1. Problem Statement (from Step 1)
2. Evaluation Criteria (from Step 2)
3. Failure Modes and Fallbacks (from Step 3)
4. Data Requirements (from Step 4)
5. Model Behavior Contract (from Step 5)
6. Automation Ladder (from Step 6)
7. Open Questions and Research Dependencies -- list any capabilities that depend on research results not yet available, with expected timeline and fallback if research does not deliver.
8. Appendix: Glossary of ML terms used in the PRD, defined for non-technical stakeholders.

**Output:** A complete AI PRD saved as `applied/ai-prd-{product}.md`.

## Diagnostic Questions

Ask these before beginning the PRD to calibrate the approach:

1. **Does this feature actually need AI/ML?** If the problem can be solved with rules, heuristics, or a lookup table, it should be. AI adds complexity, cost, and unpredictability. Justify the AI approach explicitly.

2. **What is the current human baseline?** How do humans perform this task today, and how well? If you do not know the human accuracy/speed, you cannot set a meaningful bar for the model.

3. **Do you have evaluation data?** If you cannot test the model's output against a ground truth, you cannot ship with confidence. No eval data means Step 2 is blocked.

4. **What happens when the model is wrong?** If the answer is "the user sees a bad result," the PRD is incomplete. Every AI feature needs a designed failure experience.

5. **What is the cost per inference?** If you do not know the cost, you cannot forecast unit economics. An AI feature that costs $0.50 per use on a $10/month product will not survive.

6. **Who is the human in the loop?** At launch, someone will review, correct, or override model outputs. Identify that person and design their workflow before you design the autonomous flow.

7. **What changes if a better model becomes available next quarter?** If the PRD is tightly coupled to a specific model's capabilities, it will be obsolete in 3-6 months. Write the spec against the outcome, not the model.

## Common Mistakes

1. **Specifying the model instead of the outcome**
   PRDs that say "use GPT-4" or "train a ResNet-50" are specifying implementation, not requirements. Models change. The PRD should define what the system must do and how well, then let engineering choose and swap models freely. Couple the spec to the eval bar, not the architecture.

2. **Treating AI outputs as deterministic**
   Traditional PRDs say "when the user clicks X, the system does Y." AI PRDs must say "when the user provides X, the system returns Y with Z confidence, and if confidence is below threshold, the system does W instead." Ignoring the probabilistic nature of AI outputs leads to brittle products and confused users.

3. **Skipping the cost and latency budget**
   A feature that works perfectly but takes 30 seconds and costs $2 per call is not shippable for most consumer products. The PRD must treat cost and latency as first-class constraints, not afterthoughts discovered in the sprint review.

4. **Writing the PRD before the eval exists**
   If you cannot evaluate the feature, you cannot know if it works. Write the eval criteria (Step 2) before writing the rest of the PRD. If you cannot define what "good" looks like, you are not ready to write the spec.

5. **Ignoring the research-to-production gap**
   Research papers report metrics on clean benchmarks. Production systems face noisy inputs, adversarial users, distribution shift, and scale. The PRD must explicitly state which research results it depends on and what the gap is between the benchmark and production conditions.

6. **Launching at full automation**
   Teams skip the human-in-the-loop phase because it feels slow. But launching at L3 (fully autonomous) without data from L1-L2 means you have no ground truth for when things go wrong. The automation ladder exists to build confidence and training data incrementally.

## Context Integration

This skill uses the `context/` directory to ground the AI PRD in real product and market context:

| Context Directory | How It Is Used | Relevant Steps |
|-------------------|----------------|----------------|
| **`context/products/`** | Pulls existing product capabilities, architecture, and technical stack to identify where AI features fit and what infrastructure constraints exist. Informs input/output specifications in the model behavior contract. | Step 1 (Problem Statement), Step 5 (Model Behavior Contract) |
| **`context/verticals/`** | Pulls target user segments and use cases to define user-centric success criteria and calibrate the evaluation bar against real user expectations, not abstract benchmarks. | Step 1 (Problem Statement), Step 2 (Evaluation Criteria) |
| **`context/competitive/`** | Pulls competitor AI capabilities to benchmark evaluation thresholds. If a competitor's feature achieves X% accuracy, your threshold should be calibrated relative to that bar. | Step 2 (Evaluation Criteria), Step 5 (Model Behavior Contract) |
| **`context/company/`** | Pulls company stage, team composition, and resource constraints to calibrate the automation ladder. A 5-person startup should launch at L1; a 200-person company with an ML platform team may launch at L2. | Step 4 (Data Requirements), Step 6 (Automation Ladder) |
| **`context/founders/`** | Pulls leadership vision and risk tolerance to align the PRD's ambition level and safety constraints with company values. | Step 3 (Failure Modes), Step 5 (Model Behavior Contract) |
| **`context/signals/`** | Pulls ecosystem signals (GitHub activity, community discussions, news) to identify emerging model capabilities or shifts in the competitive landscape that may affect the PRD's assumptions. Check collection timestamps; warn if data is older than 14 days. | Step 7 (Open Questions and Research Dependencies) |

If no `context/` directory exists, the skill prompts the user with the diagnostic questions above to gather the minimum required context before proceeding.
