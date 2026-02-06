---
name: measuring-product-market-fit
description: "Help users measure product-market fit for new-category products by building a PMF scorecard, tracking leading signals, and making pivot/persevere decisions."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Measuring Product-Market Fit

Produces a PMF scorecard combining quantitative surveys, qualitative signals, and behavioral metrics -- specifically designed for new-category products where no incumbent benchmark exists -- and delivers a pivot/persevere recommendation with supporting evidence.

## Core Principles

1. **PMF is not a metric -- it is a feeling backed by data**
   "Product/market fit means being in a good market with a product that can satisfy that market. You can always feel when product/market fit isn't happening. The customers aren't quite getting value out of the product, word of mouth isn't spreading, usage isn't growing that fast. And you can always feel product/market fit when it's happening."
   -- *Marc Andreessen, Co-founder of Andreessen Horowitz* ([source](https://pmarchive.com/guide_to_startups_part4.html))

2. **The "very disappointed" test is the leading indicator**
   "If you survey your users and ask 'How would you feel if you could no longer use this product?' and more than 40% say 'very disappointed,' you have product-market fit. Less than 40%, you need to keep iterating."
   -- *Sean Ellis, Creator of the Sean Ellis Test and author of Hacking Growth* ([source](https://www.startup-marketing.com/the-startup-pyramid/))

3. **PMF is a spectrum, not a binary threshold**
   "I've come to think of product-market fit as more of a spectrum. There is no single moment where you suddenly have it. Instead, there is a series of signals that become progressively stronger."
   -- *Rahul Vohra, Founder and CEO of Superhuman* ([source](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/))

4. **Optimize for the "very disappointed" segment first**
   "Rather than trying to make everyone somewhat happy, narrow your focus to users who already love you. Understand what they love. Then double down on that for everyone else. Almost all of our product decisions flowed from this insight."
   -- *Rahul Vohra, Founder and CEO of Superhuman* ([source](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/))

5. **Value hypothesis before growth hypothesis**
   "A startup needs to test two hypotheses. The first is the value hypothesis: does the product deliver value to customers once they use it? Only after proving the value hypothesis should you test the growth hypothesis."
   -- *Andy Rachleff, Co-founder of Wealthfront, coined the term "product-market fit"* ([source](https://a16z.com/why-startups-fail/))

6. **Retention is the true measure of PMF**
   "Retention is the single most important thing for growth. If your retention is poor, then nothing else matters. The number one thing that I've seen correlate with long-term success is having a strong retention curve that flattens out."
   -- *Casey Winters, former Growth Lead at Pinterest and Grubhub* ([source](https://www.lennysnewsletter.com/p/what-is-good-retention-casey-winters))

7. **For new categories, PMF is about pull, not push**
   "The easiest way to tell if you have product-market fit: are people pulling the product out of your hands? Are they signing up faster than you can onboard them? Are they telling other people without being asked?"
   -- *Lenny Rachitsky, author of Lenny's Newsletter* ([source](https://www.lennysnewsletter.com/p/how-to-know-if-youve-got-product))

8. **New-category products must educate before they can measure**
   "When you're creating a new category, your biggest competitor is the status quo -- doing nothing. You can't measure PMF against an existing alternative because there is no existing alternative. You have to measure whether people understand the problem you're solving and whether they would go back to life without your product."
   -- *April Dunford, author of Obviously Awesome and positioning expert* ([source](https://www.aprildunford.com/post/obviously-awesome))

9. **Engagement frequency reveals habit formation**
   "The most important metric that founders should track is not how many users sign up, but how many come back. If you look at the ratio of DAU to MAU, what you're really looking for is a natural frequency of engagement that matches the value proposition."
   -- *Andrew Chen, General Partner at Andreessen Horowitz* ([source](https://andrewchen.com/dau-mau-is-an-important-metric/))

## Instructions

### Step 1: Define the Product and Its Category Context

Identify whether the product is entering an existing category or creating a new one, because measurement strategy differs fundamentally.

- **Read** `context/products/` and `context/competitive/` if available
- Classify the product:
  - **Existing category** -- Users have a known alternative (e.g., a new CRM). Benchmark against incumbents.
  - **New category** -- No direct alternative exists (e.g., first AI world-generation API). Benchmark against the status quo (manual processes, workarounds, or doing nothing).
- **Produce:** A one-paragraph product positioning statement and a category classification (existing vs. new) with the identified "current alternative" users would revert to

### Step 2: Identify and Segment Target Users

Build a user segmentation that separates high-expectation customers (HXC) from casual users, because PMF signals come from your most passionate segment first.

- **Read** `context/verticals/` if available for target market data
- Define 3-5 user segments by role, use case, or adoption stage
- For each segment, note:
  - How they discovered the product
  - What their "current alternative" is (the workflow or tool they used before)
  - Frequency of use (daily, weekly, project-based)
- Identify the **high-expectation customer (HXC)**: the segment whose needs align most tightly with the product's core value. This is the group whose "very disappointed" score you optimize for first.
- **Produce:** A user segment table with columns: Segment Name | Description | Current Alternative | Expected Frequency | HXC Candidate (Y/N)

### Step 3: Build the PMF Survey Instrument

Construct a survey combining the Sean Ellis test, Rahul Vohra's Superhuman framework, and new-category-specific questions.

- **Core survey questions (include all of these):**
  1. "How would you feel if you could no longer use [product]?" -- Very disappointed / Somewhat disappointed / Not disappointed
  2. "What type of person do you think would most benefit from [product]?" (open text)
  3. "What is the primary benefit you receive from [product]?" (open text)
  4. "How can we improve [product] for you?" (open text)
- **New-category supplemental questions (add these when category = new):**
  5. "Before [product], how did you accomplish this task?" (open text -- reveals the real alternative)
  6. "How would you explain what [product] does to a colleague who has never heard of it?" (open text -- tests whether users can articulate the value)
  7. "If [product] did not exist, what would you do instead?" (open text -- validates lock-in)
  8. "How frequently do you use [product]?" with options matched to expected natural frequency
- **Deployment guidance:**
  - Minimum sample: 40 responses per segment to reach statistical relevance
  - Target users who have experienced the core value at least twice (not first-time visitors)
  - Avoid surveying during onboarding (they haven't formed an opinion yet)
- **Produce:** A ready-to-deploy survey document with all questions, answer formats, and deployment criteria

### Step 4: Define the Behavioral Metrics Dashboard

Identify the quantitative signals to track alongside survey data. These are the "revealed preference" signals that complement the "stated preference" of surveys.

- **Retention metrics:**
  - Day 1 / Day 7 / Day 30 retention rates
  - Cohort retention curve shape: does it flatten or trend to zero?
  - Reactivation rate: do churned users come back unprompted?
- **Engagement metrics:**
  - DAU/MAU ratio (target: >20% for daily-use tools, >40% for communication tools)
  - Core action frequency: how often do users perform the key value-delivering action?
  - Session depth: how many core actions per session?
- **Organic growth signals (PMF pull indicators):**
  - Organic vs. paid acquisition ratio
  - NPS or referral rate
  - Inbound interest (waitlist growth, unsolicited inquiries, social mentions)
  - Time-to-value: how quickly do new users reach the "aha moment"?
- **New-category-specific signals:**
  - Category vocabulary adoption: are users using your terminology when describing the problem?
  - "Show a friend" rate: percentage of users who share output or demo the product to someone else
  - Integration/embedding requests: are developers asking to build on top of your product?
- **Produce:** A metrics dashboard specification with: Metric Name | Definition | Data Source | Target Threshold | Current Value (if known)

### Step 5: Score the PMF Scorecard

Combine survey results and behavioral data into a single scorecard. Score each dimension on a 1-5 scale.

- **PMF Scorecard Dimensions:**

| Dimension | Weight | What It Measures | Scoring Criteria |
|---|---|---|---|
| Very Disappointed % | 25% | Would users be devastated to lose the product? | 1: <15%, 2: 15-25%, 3: 25-35%, 4: 35-40%, 5: >40% |
| Retention Curve Shape | 20% | Do users keep coming back? | 1: Trends to 0, 2: Slow decline, 3: Flattens >5%, 4: Flattens >15%, 5: Flattens >25% |
| Organic Pull | 15% | Is the product spreading without paid push? | 1: <10% organic, 2: 10-25%, 3: 25-50%, 4: 50-75%, 5: >75% organic |
| Core Action Frequency | 15% | Are users engaging at the expected natural frequency? | 1: <10% of expected, 2: 10-30%, 3: 30-60%, 4: 60-85%, 5: >85% |
| User Articulation | 10% | Can users explain the value in their own words? | 1: Cannot explain, 2: Vague, 3: Accurate but generic, 4: Specific and compelling, 5: Evangelistic |
| Willingness to Pay / Expand | 10% | Would users pay (more) for this? | 1: No, 2: Maybe at low price, 3: Yes at current price, 4: Would pay more, 5: Already paying + expanding |
| Status Quo Rejection | 5% | Would users refuse to go back to the old way? | 1: Prefer old way, 2: Indifferent, 3: Slight preference for product, 4: Strong preference, 5: Cannot imagine going back |

- **Composite score calculation:** Weighted average of all dimensions (1.0 - 5.0 scale)
  - **1.0 - 2.0:** No PMF. Fundamental value hypothesis unproven.
  - **2.0 - 3.0:** Early signal. PMF emerging in one segment but not durable.
  - **3.0 - 3.5:** Approaching PMF. Strong in HXC segment, weak outside it.
  - **3.5 - 4.0:** PMF achieved for HXC segment. Ready to expand.
  - **4.0 - 5.0:** Strong PMF. Growth hypothesis is safe to test.
- **Produce:** A filled PMF scorecard table with scores, evidence citations for each score, and a composite score with interpretation

### Step 6: Identify the PMF Engine (What Drives It)

Analyze survey open-text responses to extract the product's PMF engine -- the specific value that the "very disappointed" users cannot live without.

- From the "very disappointed" respondents:
  - Cluster the "primary benefit" answers into 3-5 themes
  - Identify the single most common theme -- this is the PMF engine
  - Cross-reference with "how would you explain this to a colleague" answers to find the natural positioning language
- From the "not disappointed" respondents:
  - Identify what they are missing or misunderstanding
  - Determine whether they are in the wrong segment or whether the product failed to deliver its core value to them
- **Produce:** A PMF engine statement: "[Product] achieves PMF when [specific user segment] uses it to [specific action] because [specific benefit that no alternative provides]." Include the supporting evidence clusters.

### Step 7: Make the Pivot/Persevere Decision

Use the scorecard and PMF engine analysis to produce a clear recommendation.

- **Decision framework:**

| Composite Score | Very Disappointed % | Recommendation |
|---|---|---|
| < 2.0 | < 15% | **Pivot.** Redefine the value hypothesis. Consider a different user segment, different core action, or different positioning. |
| 2.0 - 3.0 | 15-25% | **Iterate aggressively.** Double down on the HXC segment. Narrow scope. Remove features the "not disappointed" group uses but the "very disappointed" group ignores. |
| 3.0 - 3.5 | 25-35% | **Persevere and deepen.** PMF is emerging. Focus on converting "somewhat disappointed" users to "very disappointed" by closing the gaps they identified. |
| 3.5 - 4.0 | 35-40% | **Expand carefully.** PMF is proven for the HXC segment. Begin testing adjacent segments. Start growth experiments. |
| > 4.0 | > 40% | **Scale.** Shift investment from product iteration to growth. PMF is durable. |

- For each recommendation, produce:
  - **Top 3 actions** to take in the next 30 days
  - **What to stop doing** (features, segments, or channels to cut)
  - **What to double down on** (the PMF engine from Step 6)
  - **Re-measurement timeline** (when to re-run this scorecard -- typically 4-8 weeks)
- **Produce:** A pivot/persevere recommendation memo with the decision, supporting evidence, action items, and re-measurement date

### Step 8: Create the PMF Tracking Cadence

Establish an ongoing measurement system so PMF is tracked over time, not measured once.

- Define a PMF review cadence:
  - **Weekly:** Track behavioral metrics (retention, core action frequency, organic signals)
  - **Monthly:** Run the abbreviated survey (questions 1 + 8 only) on a rolling sample of recent active users
  - **Quarterly:** Run the full survey instrument and re-score the complete PMF scorecard
- Set alert thresholds:
  - "Very disappointed" drops below 35% after previously exceeding it -- investigate immediately
  - Retention curve steepens after previously flattening -- investigate within one week
  - Organic acquisition share drops by more than 10 percentage points -- review positioning
- **Produce:** A PMF tracking schedule document with cadence, responsible owners (roles, not names), alert thresholds, and escalation procedures

## Diagnostic Questions

Ask these before beginning the scorecard to calibrate the analysis:

1. **Has the product been in users' hands long enough for them to form a habit?** If launched less than 4 weeks ago or users have completed fewer than 3 core actions, survey data will be unreliable. Focus on qualitative signals and behavioral instrumentation first.

2. **Can you identify at least one user segment that would be "very disappointed" to lose the product?** If no segment comes to mind, you may not have a value hypothesis to test yet. Start with customer discovery instead.

3. **Is the product creating a new category or entering an existing one?** This determines whether you benchmark against competitors or against the status quo. New-category products typically take longer to reach PMF because they must educate users first.

4. **Do you have direct access to users for surveys and interviews?** If the product is B2B2C or sold through partners, you may need proxy signals (partner satisfaction, integration depth) rather than direct end-user surveys.

5. **What is the expected natural usage frequency?** A world-generation API used for project-based work has a different healthy DAU/MAU than a daily communication tool. Mismatched frequency expectations produce misleading retention data.

6. **Are you measuring PMF for the whole product or a specific workflow?** Broad products may have PMF in one workflow (e.g., text-to-world) but not another (e.g., multi-image-to-world). Scope the measurement to the specific value proposition being tested.

7. **Is there revenue data, or is the product free/pre-monetization?** Willingness to pay is a strong PMF signal, but pre-revenue products should weight behavioral signals more heavily and use willingness-to-pay survey questions as a proxy.

## Common Mistakes

1. **Surveying too early**
   Running the "very disappointed" test on users who signed up yesterday produces meaningless data. Users need to experience the core value loop at least 2-3 times before they can evaluate whether they would miss it. Wait until users have completed the key action at a natural frequency for at least 2 weeks.

2. **Averaging across all users instead of segmenting**
   A 30% "very disappointed" score across all users might hide a 60% score among power users and a 5% score among tourists. Always segment first. PMF starts in a niche and expands -- measuring the average obscures whether you have it anywhere.

3. **Confusing growth with PMF**
   Paid acquisition can mask poor retention. A product with strong top-of-funnel growth but a retention curve that trends to zero does not have PMF -- it has a marketing budget. Always check retention independently of acquisition.

4. **Treating PMF as binary and permanent**
   PMF can be lost. Market shifts, new competitors, or product bloat can erode it. The "very disappointed" percentage should be tracked continuously, not measured once and declared victory. Re-score the full PMF scorecard quarterly.

5. **Ignoring the "somewhat disappointed" group**
   The path from 30% to 40% "very disappointed" often runs through converting the "somewhat disappointed" group. Analyze their open-text responses: what is the gap between their experience and the "very disappointed" group's experience? That gap is your product roadmap.

6. **Using vanity metrics as PMF proxies**
   Total signups, page views, social media followers, and press coverage are not PMF signals. They measure awareness, not value delivery. Focus on metrics that require the user to have experienced the core value: retention, core action frequency, and organic referrals.

## Context Integration

When a `context/` directory is available, the skill uses it as follows:

| Context Directory | Used In | How |
|---|---|---|
| `context/products/` | Step 1 | Read product descriptions, pricing tiers, and feature lists to define the product positioning statement and identify the core value proposition being tested |
| `context/competitive/` | Step 1, Step 4 | Read competitive landscape to classify the product as new-category vs. existing-category and to identify the "current alternative" for each user segment. Informs organic pull benchmarks |
| `context/verticals/` | Step 2 | Read target market data to define user segments, estimate segment sizes, and identify the high-expectation customer (HXC) |
| `context/founders/` | Step 6, Step 7 | Read founder quotes and vision statements to cross-reference the PMF engine with the founder's original value hypothesis. Surface gaps between intended positioning and user-perceived value |
| `context/company/` | Step 7, Step 8 | Read company stage, funding, and team composition to calibrate the pivot/persevere recommendation. A seed-stage company with 18 months of runway has different thresholds than a Series C company with pressure to scale |
| `context/signals/` | Step 4, Step 5 | Auto-collected signals provide organic growth evidence. [SIGNAL] tagged. Use HN/Reddit discussions as proxy for community buzz and organic pull. GitHub stars/forks trajectory serves as a developer PMF signal for API products. Check freshness before citing. |

When no `context/` directory is available, the skill prompts the user to provide:
- A brief product description and its target market
- Whether the product is creating a new category or entering an existing one
- Any existing user data (retention numbers, survey results, NPS scores)
- Current stage and constraints (runway, team size, growth expectations)
