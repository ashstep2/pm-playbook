---
name: user-segmentation
description: "Help users define, profile, and prioritize user segments -- producing segment profiles, a prioritization matrix, and cross-segment insights that inform product strategy."
version: "1.0.0"
last_updated: "2026-02-06"
---

# User Segmentation

Produces detailed segment profiles grounded in jobs-to-be-done, a scored prioritization matrix for resource allocation, and cross-segment insight analysis that reveals hidden opportunities and informs product roadmap decisions.

## Core Principles

1. **Segment by the job, not the persona**
   "People don't want to buy a quarter-inch drill. They want a quarter-inch hole. When you understand the job the customer is trying to get done, you can segment your market in a way that corresponds to how customers actually make choices -- not by demographics, but by the progress they are seeking."
   -- *Clayton Christensen, Professor at Harvard Business School and author of The Innovator's Dilemma* ([source](https://hbr.org/2016/09/know-your-customers-jobs-to-be-done))

2. **Find your high-expectation customer**
   "Your high-expectation customer is the most discerning person within your target demographic. They will squeeze the most value out of your product, spread the word, and give you the most useful feedback. If you build for this person, everyone else is delighted. If you build for the average, you inspire no one."
   -- *Rahul Vohra, Founder and CEO of Superhuman* ([source](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/))

3. **People buy when they have a struggling moment**
   "Customers don't just decide to buy something. There's a push from the current situation, a pull toward a new solution, anxiety about the new, and habit of the old. You segment the market by understanding these forces, not by asking people what category they belong to."
   -- *Bob Moesta, Co-architect of Jobs-to-be-Done theory and author of Demand-Side Sales 101* ([source](https://www.demandsidesales.com/))

4. **Users hire products to make progress in their lives**
   "When we buy a product, we essentially hire something to get a job done. If it does the job well, the next time we're confronted with the same job, we hire that same product again. If it does a crummy job, we fire it and look for something else."
   -- *Alan Klement, Author of When Coffee and Kale Compete* ([source](https://jtbd.info/2-what-is-jobs-to-be-done-jtbd-796b82081c5a))

5. **Continuous discovery requires continuous contact with users across segments**
   "If you're not talking to customers every single week, you're just guessing. The teams that consistently deliver value are the ones that maintain continuous touchpoints across their user segments, not the ones that run a research project once a quarter."
   -- *Teresa Torres, Author of Continuous Discovery Habits* ([source](https://www.producttalk.org/2021/05/continuous-discovery-habits/))

6. **Delight is the engine of growth -- and it differs by segment**
   "Great product strategy starts with deciding who to delight. You cannot delight everyone equally. The most important strategic choice a PM makes is which segment to over-serve and which to consciously under-serve."
   -- *Gibson Biddle, former VP of Product at Netflix* ([source](https://gibsonbiddle.medium.com/4-how-to-delight-customers-nir-model-for-habit-forming-products-and-how-to-apply-it-to-netflix-935e1c4c2d61))

7. **The most dangerous segment is the one you never identified**
   "If you lump all your users into one bucket, you'll build for the average and delight nobody. But the bigger risk is missing a segment entirely -- a group of people trying to use your product for a job you never imagined. Those invisible segments are where breakout growth hides."
   -- *April Dunford, Author of Obviously Awesome and positioning expert* ([source](https://www.aprildunford.com/post/obviously-awesome))

8. **Behavioral cohorts reveal more than declared intent**
   "Don't just listen to what users say they want. Watch what they actually do. Behavioral segmentation -- grouping users by their actions, frequency, and feature adoption patterns -- is more predictive of retention and expansion than any demographic or firmographic cut."
   -- *Andrew Chen, General Partner at Andreessen Horowitz* ([source](https://andrewchen.com/power-user-curve/))

## Instructions

### Step 1: Define the Segmentation Objective and Scope

Establish what product decisions the segmentation must inform, because segmentation without a decision context is academic exercise.

- Identify the product decision at stake: Are you deciding who to build for next? Which vertical to expand into? How to price? Where to focus onboarding investment?
- Define scope boundaries: geographic, product line, time horizon
- **Read** `context/products/` and `context/company/` if available to understand the product's current state and constraints
- **Artifact produced**: A segmentation brief (one page) stating the decision to be informed, the scope, and the data sources available

### Step 2: Identify Candidate Segments

Generate an initial list of candidate segments using multiple lenses to avoid premature convergence on a single segmentation axis.

- Apply at least three segmentation lenses:
  - **Job-to-be-done**: What progress is each group trying to make? What is the struggling moment that triggers their search?
  - **Behavioral**: How do users actually interact with the product? Group by activation milestones reached, feature usage patterns, frequency of core action, and session depth.
  - **Contextual**: What is the situation of use? Team size, technical sophistication, industry vertical, buying process, and integration environment.
- For each lens, brainstorm 3-6 candidate segments
- Deduplicate and merge segments that appear across multiple lenses -- these are the strongest candidates
- Target a final list of 4-7 distinct candidate segments
- **Artifact produced**: Candidate segment list with a name, one-sentence description, and originating lens(es) for each segment

### Step 3: Build Detailed Segment Profiles

For each candidate segment, construct a full profile that goes beyond demographics to capture motivations, alternatives, and switching forces.

- **Segment Profile Template** (complete for each segment):

| Field | Description |
|---|---|
| **Segment Name** | A memorable, descriptive name (e.g., "Weekend Prototypers," "Pipeline-First Studios") |
| **Job-to-be-Done** | The core progress this segment is trying to make, stated in their language |
| **Struggling Moment** | The trigger event or frustration that causes them to seek a solution |
| **Current Alternative** | What they do today to get this job done (competitor, manual process, or nothing) |
| **Push Forces** | What is driving them away from their current solution |
| **Pull Forces** | What attracts them to your product specifically |
| **Anxiety** | What makes them hesitate to adopt (risk, learning curve, switching cost) |
| **Habit of the Old** | What keeps them attached to their current way of working |
| **Success Metric** | How this segment measures whether the product is working for them |
| **Willingness to Pay** | Price sensitivity and value framing (is this a must-have or a nice-to-have?) |
| **Estimated Size** | Order-of-magnitude estimate of addressable users or accounts in this segment |
| **Acquisition Channel** | Where you would reach this segment (community, search, partnerships, events) |

- **Read** `context/verticals/` and `context/competitive/` if available to ground profiles in market data
- **Artifact produced**: A complete Segment Profile document with one filled template per candidate segment

### Step 4: Score and Prioritize Segments

Rank segments using a weighted scoring matrix so resource allocation is explicit and defensible rather than based on intuition.

- Score each segment across six dimensions (1-5 scale each):

| Dimension | What It Measures |
|---|---|
| **Job Urgency** | How painful is the struggling moment? How frequently does it recur? |
| **Willingness to Pay** | Would this segment pay enough to sustain the business? Is the job worth real money to them? |
| **Segment Size** | Is this segment large enough to matter for the business's growth targets? |
| **Product Fit** | How well does the current product (or near-term roadmap) serve this segment's job? |
| **Acquisition Feasibility** | Can you reach this segment efficiently through channels you control or can build? |
| **Strategic Alignment** | Does winning this segment unlock network effects, ecosystem value, or future segments? |

- Assign weights based on the segmentation objective from Step 1. Default weights if no specific reason to deviate: Job Urgency (20%), Willingness to Pay (20%), Segment Size (15%), Product Fit (20%), Acquisition Feasibility (10%), Strategic Alignment (15%).
- Compute a weighted composite score (1.0 - 5.0) for each segment
- Classify each segment:
  - **Primary (4.0-5.0)**: Build for this segment first. Allocate majority of product and go-to-market resources.
  - **Secondary (3.0-3.9)**: Serve this segment where it overlaps with Primary. Do not build features exclusively for them yet.
  - **Monitor (2.0-2.9)**: Track this segment's growth and needs. Revisit next quarter.
  - **Deprioritize (1.0-1.9)**: Consciously choose not to serve. Document why so the decision is revisitable.
- **Artifact produced**: Prioritization Matrix (table with dimension scores, composite scores, classifications, and a one-sentence rationale for each segment's classification)

### Step 5: Map Cross-Segment Insights

Analyze the segment profiles and scores collectively to surface patterns that no single profile reveals on its own.

- Answer each of the following:
  - **Shared jobs**: Which segments share the same underlying job-to-be-done despite different contexts? These are candidates for a single product experience with contextual customization.
  - **Contradictory needs**: Where do segments require mutually exclusive features or workflows? These reveal architectural decisions (e.g., simple vs. advanced modes, separate product tiers).
  - **Migration paths**: Which Monitor or Secondary segments could become Primary as the product matures? What would trigger that migration?
  - **Ecosystem effects**: Does serving one segment create assets (content, integrations, data) that make other segments more attractive?
  - **Risk concentration**: Is more than 60% of projected revenue coming from a single segment? Document the dependency risk.
- **Artifact produced**: Cross-Segment Insight Memo (structured analysis addressing each question above, with specific recommendations for product architecture and sequencing)

### Step 6: Translate Segments into Product Strategy Inputs

Convert the segmentation work into concrete inputs that other PM skills and product processes can consume directly.

- **For the Primary segment(s):**
  - Write a High-Expectation Customer (HXC) definition: one paragraph describing this person's role, context, daily workflow, and what "delighted" looks like for them
  - Define the onboarding critical path: the 3-5 actions this segment must complete to experience core value
  - List the top 3 features or improvements that would convert "somewhat disappointed" users in this segment to "very disappointed"
- **For Secondary segments:**
  - Identify the minimum viable experience: what subset of the product already serves them adequately?
  - Note the trigger condition that would promote them to Primary (market growth, product capability, competitive shift)
- **For all segments:**
  - Map each segment to relevant product metrics (retention rate, core action frequency, expansion revenue) so dashboards can be filtered by segment
- **Artifact produced**: Product Strategy Input Document containing HXC definition, onboarding critical paths, feature priorities by segment, and segment-specific metric definitions

### Step 7: Compile the Segmentation Deliverable

Assemble all artifacts into a single reference document for stakeholder alignment and ongoing use.

1. Executive Summary (one paragraph: who your users are, which segment to prioritize, and why)
2. Segmentation Brief (from Step 1)
3. Candidate Segment List (from Step 2)
4. Segment Profiles (from Step 3)
5. Prioritization Matrix (from Step 4)
6. Cross-Segment Insight Memo (from Step 5)
7. Product Strategy Inputs (from Step 6)
8. Recommended next actions (top 3 things to do this week)
9. Re-segmentation trigger criteria (when to re-run this analysis -- typically after a major launch, market shift, or quarterly review)

- **Artifact produced**: Complete Segmentation Deliverable (the compiled document ready for stakeholder review)

## Diagnostic Questions

1. **Can you name the top job-to-be-done for your most engaged users without guessing?** If not, you are segmenting by assumption rather than evidence. Start with behavioral data or customer interviews before building profiles.

2. **If you had to cut your user base in half and keep only one group, who would you keep and why?** This forces the prioritization that segmentation is supposed to produce. If the answer is not obvious, the prioritization matrix is the place to start.

3. **What does your "not disappointed" user look like, and why are they using your product at all?** Understanding who your product fails for is as informative as understanding who it delights. These users may be in the wrong segment or revealing a positioning gap.

4. **Are there users doing something unexpected with your product that you did not design for?** Unexpected use cases often signal an invisible segment with a job-to-be-done you have not yet named. These segments can be high-value precisely because no competitor is serving them intentionally.

5. **How would your segmentation change if you 10x'd your price?** Price sensitivity is the fastest way to separate segments that find your product essential from those that find it convenient. The segments that remain at 10x price are your strategic core.

6. **Which segment would your competitors least want you to win?** This reveals where your competitive differentiation is strongest and where winning a segment would create the most strategic leverage.

7. **Do your current metrics let you distinguish retention and engagement across segments?** If your analytics treat all users as one cohort, you cannot validate whether a segmentation is real or theoretical. Instrumentation is a prerequisite for actionable segmentation.

## Common Mistakes

1. **Segmenting by demographics instead of jobs**
   Grouping users by company size, industry, or job title feels rigorous but often produces segments that behave identically. Two enterprise companies in different industries may have the same struggling moment, while two companies in the same industry may have completely different jobs-to-be-done. Always start with the job and validate demographic correlations afterward.

2. **Creating too many segments**
   More than 5-7 segments at a time overwhelms product teams and dilutes focus. Every additional segment competes for roadmap space, design attention, and go-to-market resources. If you have more than 7, look for segments that share enough common ground to merge. You can always split later as the product matures.

3. **Prioritizing by segment size alone**
   The largest segment is not always the best segment to serve first. A smaller segment with higher urgency, willingness to pay, and strategic value (e.g., one that creates ecosystem assets for other segments) may be a far better beachhead. Use the full scoring matrix, not a single dimension.

4. **Treating segmentation as a one-time exercise**
   Segments shift as the market evolves, as your product changes, and as competitors enter or exit. A segmentation built at launch may be invalid six months later. Set explicit re-evaluation triggers and re-run the analysis at least quarterly.

5. **Building for the "average" across segments instead of delighting one**
   When multiple segments are prioritized equally, the product drifts toward a middle ground that satisfies no one deeply. The entire point of prioritization is to give yourself permission to over-serve one segment and consciously under-serve others. If every segment is "Primary," none of them are.

6. **Ignoring switching forces in segment profiles**
   Identifying a segment's job-to-be-done is necessary but not sufficient. If the anxiety about switching is high and the habit of the old is strong, even a superior product will fail to convert that segment. The four forces (push, pull, anxiety, habit) must all be analyzed to predict adoption realistically.

## Context Integration

When a `context/` directory is available, the skill draws from it as follows:

| Context Directory | Used In | How |
|---|---|---|
| `context/products/` | Steps 1, 3, 4, 6 | Read product descriptions, feature lists, pricing tiers, and usage data to ground segment profiles in real product capabilities and to score Product Fit accurately in the prioritization matrix |
| `context/competitive/` | Steps 3, 5 | Read competitor profiles and landscape analysis to identify each segment's current alternative and to detect segments that competitors are ignoring (whitespace opportunities for cross-segment insights) |
| `context/verticals/` | Steps 2, 3, 4 | Read target market data, vertical definitions, and TAM estimates to generate candidate segments, estimate segment sizes, and calibrate willingness-to-pay assumptions |
| `context/company/` | Steps 1, 4 | Read company stage, funding, team size, and resource constraints to set realistic scope boundaries and to weight Acquisition Feasibility appropriately in the prioritization matrix |
| `context/founders/` | Steps 3, 6 | Read founder vision and value hypothesis to cross-reference segment profiles against the original product thesis. Surface gaps between who the founders intended to build for and who the product actually serves |
| `context/signals/` | Steps 2, 5 | Auto-collected signals from GitHub, HN, Reddit, and news provide behavioral evidence for segment identification. [SIGNAL] tagged. Use community discussions to discover segments the team has not named yet and to validate cross-segment migration patterns. Check freshness before citing. |

When no `context/` directory is available, the skill prompts the user to provide:
- A brief product description and its current user base
- Any existing user data (analytics, survey results, interview notes)
- Known or suspected user segments and what distinguishes them
- The product decision this segmentation needs to inform
