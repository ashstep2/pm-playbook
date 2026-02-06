---
name: ecosystem-health
description: "Help users assess their platform ecosystem's health by scoring community engagement, developer adoption velocity, third-party integrations, and identifying growth levers."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Ecosystem Health

Produces a scored ecosystem health assessment covering community engagement, developer adoption velocity, third-party integration breadth, and contributor dynamics -- with peer benchmarks and a prioritized growth playbook for strengthening the weakest dimensions.

## Core Principles

1. **The best marketplaces make their participants more successful than they could be alone**
   "The most successful technology platforms and marketplaces are those that create more value for their participants than they capture. When your ecosystem participants are thriving -- building businesses, creating tools, publishing content -- your platform becomes indispensable. When they struggle, no amount of core product investment will save you."
   -- *Bill Gurley, General Partner at Benchmark* ([source](https://abovethecrowd.com/2012/11/13/all-markets-are-not-created-equal-10-factors-to-consider-when-evaluating-digital-marketplaces/))

2. **Map the landscape before you measure it**
   "All models are wrong but some are useful. When you map your ecosystem, you need to understand the components, their evolution, and the dependencies between them. You cannot assess health without understanding the structure. A healthy-looking metric on a dying component is a dangerous illusion."
   -- *Simon Wardley, Researcher at the Leading Edge Forum* ([source](https://medium.com/wardleymaps/on-being-lost-2ef5f05eb1ec))

3. **Platforms beat products because they harness external innovation**
   "The platform's power lies in its ability to facilitate interactions and harness the innovation of an external ecosystem. A platform that merely distributes a product is not a platform at all -- it is a channel. The real test of ecosystem health is whether external contributors are creating value you never anticipated."
   -- *Sangeet Paul Choudary, Author of Platform Revolution* ([source](https://platformed.info/platform-revolution/))

4. **Developers are the new kingmakers**
   "Developers are increasingly choosing the tools, platforms, and technologies that enterprises adopt. They do not respond to traditional marketing. They respond to great documentation, working examples, and community peers who vouch for the developer experience. If your ecosystem is not developer-led, you are building on sand."
   -- *James Governor, Co-founder of RedMonk* ([source](https://redmonk.com/jgovernor/2011/02/11/developers-are-the-new-kingmakers/))

5. **Compound startups win by integrating what others leave fragmented**
   "The conventional wisdom is to do one thing well. But the compounding advantage of building multiple products on a shared data model means each new product makes every other product better. Ecosystem health is not just about external participants -- it is about the coherence of your own product surface area."
   -- *Parker Conrad, CEO of Rippling* ([source](https://www.rippling.com/blog/compound-startup))

6. **Network effects require critical mass on both sides before they compound**
   "Every platform with network effects has a chicken-and-egg problem. The ecosystem is not healthy just because it exists -- it is healthy when the flywheel is self-sustaining. Before critical mass, growth requires subsidy. After critical mass, growth becomes organic. The single most important diagnostic is whether you have crossed that threshold."
   -- *Andrew Chen, General Partner at Andreessen Horowitz* ([source](https://andrewchen.com/the-cold-start-problem/))

7. **You can measure ecosystem health by what happens when you stop pushing**
   "The true test of a healthy ecosystem is what happens when you remove the artificial stimulus. If community activity, contributions, and integrations continue to grow without your direct intervention, you have achieved organic ecosystem health. If they stall, you have a marketing program, not an ecosystem."
   -- *Peter Levine, General Partner at Andreessen Horowitz* ([source](https://a16z.com/open-source-community/))

8. **Ecosystems die from the edges inward**
   "Ecosystem collapse does not start at the center. It starts when the long-tail contributors -- the small plugin developers, the community moderators, the tutorial writers -- stop showing up. By the time core contributors leave, the ecosystem is already dead. Monitor the edges, not the center."
   -- *Nadia Eghbal, Author of Working in Public* ([source](https://press.stripe.com/working-in-public))

## Instructions

### Step 1: Define the Ecosystem Boundary

- Identify all components of the ecosystem under assessment. Map them into five layers:
  - **Core platform**: The primary product or API surface area
  - **First-party extensions**: Official SDKs, plugins, integrations, and tools built by the platform team
  - **Third-party integrations**: External tools, plugins, connectors, and applications built on or connected to the platform
  - **Developer community**: Individual developers, contributors, and builder communities
  - **Content ecosystem**: Documentation, tutorials, blog posts, courses, conference talks, and educational material
- For each layer, list the key components and their current state (active, stagnant, or declining)
- **Artifact produced**: Ecosystem Boundary Map (five-layer table with components and status)

### Step 2: Score Community Engagement

Rate the platform across six community engagement metrics on a 1-5 scale:

| Metric | What to Measure | Data Sources |
|---|---|---|
| **Community size** | Total members across Discord, Slack, forums, subreddits | Platform dashboards, community tools |
| **Active participation rate** | % of members who post, comment, or react in a 30-day window | Community analytics |
| **Question response time** | Median time for a community question to receive a useful answer | Forum/Discord analytics |
| **Content creation rate** | New tutorials, blog posts, and videos per month from non-employees | Google, YouTube, Dev.to, Medium search |
| **Event engagement** | Meetup attendance, hackathon participation, conference talk submissions | Event platforms, CFP data |
| **Sentiment trajectory** | Whether community tone is improving, stable, or deteriorating over 90 days | Discourse analytics, HN/Reddit threads |

Compute a **Community Engagement Score** (sum of six metrics, max 30). Classify:
- **Thriving (25-30)**: Self-sustaining community with organic content creation and peer support
- **Healthy (18-24)**: Active community but dependent on first-party stimulation for some dimensions
- **At Risk (11-17)**: Community exists but engagement is shallow or declining
- **Critical (6-10)**: Minimal community activity; ecosystem is effectively first-party only

- **Artifact produced**: Community Engagement Scorecard (table with metrics, scores, evidence, and overall classification)

### Step 3: Measure Developer Adoption Velocity

Track adoption across four time horizons using quantitative signals:

| Signal | Metric | Benchmark Comparison |
|---|---|---|
| **Awareness** | GitHub stars, npm/PyPI weekly downloads, documentation page views | Compare to 2-3 peer platforms |
| **Trial** | API key registrations, SDK installs, "hello world" completions per month | Track month-over-month growth rate |
| **Activation** | Developers who make their first meaningful API call or deploy a working integration | Compute trial-to-activation conversion rate |
| **Retention** | Developers with sustained usage (weekly active API callers over 90-day window) | Compare 30/60/90-day retention curves to peers |

For each signal, capture the raw number, the month-over-month trend (growing, flat, declining), and a peer benchmark where available. Compute the **Adoption Velocity Index**: the average month-over-month growth rate across the four signals.

- **Artifact produced**: Developer Adoption Dashboard (table with signals, raw metrics, trends, peer comparisons, and the Adoption Velocity Index)

### Step 4: Assess Third-Party Integration Breadth and Depth

Catalog all third-party integrations and score the integration layer:

- **Breadth**: Total number of third-party integrations across categories (SaaS tools, developer frameworks, industry-specific platforms, data connectors)
- **Depth**: For the top 10 integrations by usage, rate each on a 1-5 scale for functional depth (1 = read-only data pass-through, 5 = deep bidirectional workflow integration)
- **Freshness**: What percentage of integrations have been updated in the past 6 months?
- **Coverage gaps**: Which integration categories that users request most frequently are not yet served?
- Compare integration counts and categories to 2-3 peer platforms

- **Artifact produced**: Integration Health Matrix (table with integration categories, counts, depth scores, freshness, and gap analysis)

### Step 5: Analyze Contributor Dynamics

For open-source or community-contribution-driven ecosystems, assess contributor health:

| Metric | What It Reveals |
|---|---|
| **Contributor count (90-day active)** | Size of the active contributor base |
| **Bus factor** | How many contributors account for 50% of commits -- lower means more risk |
| **New contributor inflow** | First-time contributors per month -- leading indicator of ecosystem growth |
| **Contribution diversity** | Ratio of code vs docs vs issues vs reviews -- healthy ecosystems have balanced contributions |
| **Contributor retention** | % of contributors from 6 months ago who are still active -- reveals whether the ecosystem retains talent |
| **Corporate contributor ratio** | % of contributions from employees vs community -- high corporate ratio indicates ecosystem dependency on the company |

Flag any dimension where the trend is negative for two or more consecutive months.

- **Artifact produced**: Contributor Health Report (table with metrics, current values, 3-month trends, and risk flags)

### Step 6: Benchmark Against Peers

Select 2-3 peer platforms at a comparable stage and compile a side-by-side comparison:

| Dimension | Your Platform | Peer A | Peer B | Peer C |
|---|---|---|---|---|
| Community Engagement Score (Step 2) | | | | |
| Adoption Velocity Index (Step 3) | | | | |
| Third-party integration count (Step 4) | | | | |
| Active contributor count (Step 5) | | | | |
| GitHub stars | | | | |
| SDK/package weekly downloads | | | | |

Identify the dimensions where you significantly lag peers (more than 30% below the peer average) and those where you lead. These gaps and leads become the inputs for the growth playbook.

- **Artifact produced**: Peer Benchmark Comparison (side-by-side table with gap/lead analysis)

### Step 7: Build the Growth Playbook

For each dimension where you scored At Risk or Critical (Step 2), trail peers significantly (Step 6), or show a declining trend (Steps 3-5), design a targeted intervention:

- **Lever**: Name the specific growth lever (e.g., "Launch an integration partner program," "Create a first-contribution onboarding path," "Publish a weekly ecosystem highlight newsletter")
- **Target metric**: Which metric from Steps 2-5 this lever is designed to move
- **Expected impact**: Estimated improvement (e.g., "+20% new contributors per month within 6 months")
- **Effort**: T-shirt size estimate (S/M/L/XL)
- **Priority**: Rank by impact-to-effort ratio

Compile the top 5-7 levers into a sequenced 90-day action plan.

- **Artifact produced**: Ecosystem Growth Playbook (prioritized lever table + 90-day action plan)

### Step 8: Compile the Ecosystem Health Report

Assemble all artifacts from Steps 1-7 into a single executive-ready document:
1. Executive summary (one paragraph: overall ecosystem health in plain language)
2. Ecosystem Boundary Map
3. Community Engagement Scorecard
4. Developer Adoption Dashboard
5. Integration Health Matrix
6. Contributor Health Report
7. Peer Benchmark Comparison
8. Ecosystem Growth Playbook with 90-day action plan
9. Top 3 recommended immediate actions

- **Artifact produced**: Ecosystem Health Report (the complete compiled document)

## Diagnostic Questions

1. **If you stopped all community programs tomorrow, would ecosystem activity continue to grow?** This distinguishes organic health from manufactured engagement and reveals whether the flywheel is self-sustaining.

2. **What percentage of your platform's total value is created by third parties versus your own team?** A healthy platform ecosystem derives increasing value from external contributors over time. If third-party value creation is flat or declining, the platform thesis may be failing.

3. **How long does it take a new developer to go from "I heard about this" to "I shipped something with it"?** This is the single best proxy for developer experience quality and directly predicts adoption velocity.

4. **Which integrations do your users ask for most frequently that do not exist yet?** Integration gaps are unmet demand signals. They also reveal which adjacent ecosystems your users already live in.

5. **Are your most active community contributors from 12 months ago still active today?** Contributor retention is the most underrated ecosystem health metric. High churn in your contributor base means your ecosystem has a leaky bucket, and no amount of new contributor acquisition will fix it.

6. **When was the last time a third party built something on your platform that genuinely surprised you?** Unexpected innovation is the hallmark of a healthy ecosystem. If every integration and use case was predicted by your roadmap, external participants are executing your vision rather than extending it.

7. **What is the ratio of developers who try your platform to those who become sustained users?** A large gap between trial and retention indicates friction in the developer experience that ecosystem investment alone cannot solve.

## Common Mistakes

1. **Measuring vanity metrics instead of ecosystem health**
   GitHub stars, Twitter followers, and Discord member counts are awareness metrics, not health metrics. A platform with 50,000 GitHub stars and 12 active contributors is less healthy than one with 2,000 stars and 200 active contributors. Always pair reach metrics with engagement and retention metrics.

2. **Treating the ecosystem as a marketing channel**
   Ecosystems are not distribution strategies. They are value-creation networks. When ecosystem programs are owned by marketing rather than product, they optimize for impressions and signups rather than integration depth and contributor retention. The ecosystem team should report into product, not marketing.

3. **Ignoring the long tail of contributors**
   Platforms over-invest in "hero" developers and top integration partners while neglecting the hundreds of small contributors who collectively drive ecosystem breadth. When the long tail stops contributing -- because onboarding is too hard, documentation is stale, or feedback goes unacknowledged -- the ecosystem hollows out from the edges inward.

4. **Benchmarking against the wrong peers**
   Comparing your developer ecosystem to a platform ten times your size produces misleading conclusions. Benchmark against platforms at your stage and growth rate. An 18-month-old API with 500 active developers may be outperforming an established platform with 5,000 if the growth trajectory is steeper.

5. **Confusing first-party integrations with ecosystem health**
   Building 50 integrations in-house is a product strategy, not an ecosystem strategy. True ecosystem health requires third parties to build, maintain, and invest in integrations because the economics work for them. If every integration depends on your engineering team, you have a feature, not an ecosystem.

6. **Running a quarterly assessment when the ecosystem moves monthly**
   Ecosystem dynamics can shift rapidly -- a competitor launches a developer program, a key contributor burns out, a community controversy flares up. The monitoring cadence should match the speed of change. Track leading indicators weekly and run the full assessment monthly or at minimum quarterly.

## Context Integration

This skill draws from the `context/` directory when available. Here is how each subdirectory feeds into the analysis:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 3, 4 | Product descriptions, API surface area, and SDK inventory. Defines the core platform layer of the Ecosystem Boundary Map and provides the baseline for adoption metrics. |
| `context/competitive/` | Steps 3, 6 | Competitor profiles and landscape data. Identifies peer platforms for benchmarking in Step 6 and provides comparative adoption data for Step 3. |
| `context/company/` | Steps 5, 7 | Team size, org structure, and resource constraints. Informs what ecosystem investments are feasible and helps right-size the Growth Playbook to actual capacity. |
| `context/verticals/` | Steps 1, 4 | Target market information and vertical-specific ecosystems. Reveals which integration categories matter most for each vertical and shapes the coverage gap analysis. |
| `context/founders/` | Step 7 | Founder vision and strategic priorities. Ensures the Growth Playbook aligns with the company's long-term ecosystem philosophy (open vs. controlled, broad vs. deep). |
| `context/signals/` | Steps 2, 3, 5, 6 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `github-ecosystem.md` for contributor dynamics and star/fork trends, `hackernews-sentiment.md` and `reddit-discussions.md` for community sentiment and developer perception, `news-coverage.md` for ecosystem partnership announcements, and `_synthesis.md` for cross-source trend identification. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A description of their platform and its API or extension surface area
2. Links to their GitHub organization, community forum, or Discord server
3. Names of 2-3 peer platforms they consider comparable
4. Their current understanding of ecosystem strengths and weaknesses
