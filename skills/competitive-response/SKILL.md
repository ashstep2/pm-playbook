---
name: competitive-response
description: "Help users analyze competitive threats, classify their severity, design response strategies, and identify sustainable moats."
---

# Competitive Response

Produces a threat assessment, moat audit, and actionable response playbook for each identified competitor -- classifying threats by severity and prescribing one of four response strategies: ignore, fast-follow, differentiate, or leapfrog.

## Core Principles

1. **Power is what makes a business durably valuable**
   "A business that achieves persistent differential returns must have at least one of the 7 Powers: Scale Economies, Network Effects, Counter-Positioning, Switching Costs, Branding, Cornered Resource, or Process Power. Without Power, any advantage is competed away."
   -- *Hamilton Helmer, Author of 7 Powers and founder of Strategy Capital* ([source](https://7powers.com/))

2. **Disruption comes from below, not from ahead**
   "Disruptive innovations originate in low-end or new-market footholds. Incumbents rationally ignore them because they target customers that are less profitable. By the time the threat is obvious, the disruptor has improved enough to pull mainstream customers away."
   -- *Clay Christensen, Professor at Harvard Business School* ([source](https://hbr.org/2015/12/what-is-disruptive-innovation))

3. **Aggregators win by owning demand, not supply**
   "The key distinction between platforms and aggregators is that platforms are powerful because they facilitate a relationship between third-party suppliers and users; aggregators, on the other hand, intermediate and control that relationship. This has massive strategic implications for how you compete."
   -- *Ben Thompson, Founder of Stratechery* ([source](https://stratechery.com/2017/defining-aggregators/))

4. **The only sustainable competitive advantage is the rate at which you learn**
   "The way to win is to learn faster than anyone else. The goal of a startup is not to execute a pre-existing plan -- it is to figure out the right plan through rapid experimentation."
   -- *Eric Ries, Author of The Lean Startup* ([source](https://theleanstartup.com/))

5. **Strategy is about making choices that make other choices unnecessary**
   "The essence of strategy is choosing what not to do. Competitive strategy is about being different. It means deliberately choosing a different set of activities to deliver a unique mix of value."
   -- *Michael Porter, Professor at Harvard Business School* ([source](https://hbr.org/1996/11/what-is-strategy))

6. **In AI, the moat is not the model -- it is the system around it**
   "In the long run, the models themselves are unlikely to be the primary source of defensibility. The data flywheels, distribution, user workflows, and ecosystem integrations around the model are what create durable advantages."
   -- *Elad Gil, Investor and Author of High Growth Handbook* ([source](https://blog.eladgil.com/p/defensibility-and-competition))

7. **Commoditize your complement**
   "A smart company tries to commoditize its products' complements. If you can make the things that work alongside your product cheap and interchangeable, demand for your product increases and your pricing power grows. This is one of the most important strategic moves in technology."
   -- *Joel Spolsky, Co-founder of Stack Overflow and Fog Creek Software* ([source](https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/))

8. **Competitive responses must match the type of threat, not its volume**
   "The right response to competition is not always to fight. Sometimes it's to ignore. Sometimes it's to copy. The critical error is responding to every threat with the same playbook. Classify first, then decide."
   -- *Andy Grove, Former CEO of Intel* ([source](https://www.penguinrandomhouse.com/books/72763/only-the-paranoid-survive-by-andrew-s-grove/))

9. **Speed of iteration beats quality of strategy**
   "If you're not embarrassed by the first version of your product, you've launched too late. In competitive markets, the cost of delay almost always exceeds the cost of imperfection."
   -- *Reid Hoffman, Co-founder of LinkedIn* ([source](https://www.linkedin.com/pulse/arent-any-typos-essay-too-long-reid-hoffman/))

## Instructions

### Step 1: Build the Competitive Landscape Map

- Identify all competitors and group them into three categories:
  - **Direct competitors**: Same product category, same target user, competing for the same budget
  - **Adjacent entrants**: Companies in neighboring categories that could enter your space (e.g., a cloud provider adding an AI feature that overlaps your core product)
  - **Asymmetric threats**: Startups, open-source projects, or non-obvious players attacking from a different value chain position (e.g., a research lab releasing a free model)
- For each competitor, document: name, category, current product, primary user segment, funding/resources, and growth trajectory
- **Artifact produced**: Competitive Landscape Map (table with all competitors categorized)

### Step 2: Classify Each Threat by Severity

Rate each competitor across four dimensions (1-5 scale each):

| Dimension | What It Measures |
|---|---|
| **Overlap** | How much their product addresses the same jobs-to-be-done as yours |
| **Momentum** | Growth rate, funding, hiring velocity, and market buzz |
| **Capability** | Technical depth, team quality, and resource advantage |
| **Trajectory** | Whether their roadmap is converging toward or diverging from your space |

Compute a **Threat Score** (sum of four dimensions, max 20) and classify:
- **Critical (16-20)**: Existential threat demanding immediate strategic response
- **Serious (11-15)**: Material threat requiring a defined response within one quarter
- **Monitor (6-10)**: Emerging threat worth tracking but not yet requiring action
- **Noise (1-5)**: Not a real competitive threat; do not allocate resources

- **Artifact produced**: Threat Classification Matrix (table with scores, classifications, and rationale for each competitor)

### Step 3: Audit Your Moat

Evaluate your company's defensibility against each of Hamilton Helmer's 7 Powers:

| Power | Present? | Strength (1-5) | Evidence |
|---|---|---|---|
| Scale Economies | | | |
| Network Effects | | | |
| Counter-Positioning | | | |
| Switching Costs | | | |
| Branding | | | |
| Cornered Resource | | | |
| Process Power | | | |

For each Power that scores 3 or above, describe the specific mechanism and how it would withstand the top-ranked threats from Step 2. For each Power that scores below 3, note whether it is buildable in the next 12 months and what it would take.

- **Artifact produced**: Moat Audit (7 Powers table with strength ratings, evidence, and buildability assessment)

### Step 4: Assign a Response Strategy per Competitor

For each competitor classified as Serious or Critical in Step 2, assign exactly one of four response strategies:

- **Ignore**: The threat is real on paper but your moat (Step 3) already neutralizes it, or the competitor is targeting a segment you do not need. Document why ignoring is the right call -- this is a deliberate strategic choice, not neglect.
- **Fast-Follow**: The competitor has validated a feature or market that you should also serve. Copy the proven concept and ship within one release cycle. Specify what to copy, what to skip, and the target ship date.
- **Differentiate**: The competitor is strong in the same space, so competing head-to-head is a losing game. Instead, double down on a dimension where you have an advantage they cannot easily replicate. Name the differentiating axis and the investment required.
- **Leapfrog**: The competitor has a lead today, but a technology shift, platform change, or architectural bet lets you skip ahead. Define the bet, the timeline, the risk, and the fallback plan if the bet fails.

For each assignment, include a one-paragraph justification linking back to the Threat Score and Moat Audit.

- **Artifact produced**: Response Strategy Table (competitor, classification, strategy, justification, and next actions)

### Step 5: Identify Surprise Entrant Scenarios

Beyond the known landscape, brainstorm 2-4 plausible surprise entrant scenarios:
- Which large platform company could add your feature as a free default?
- Which open-source project could erode your technical moat?
- Which adjacent startup could pivot into your space after a funding round?
- Which customer could build the product internally?

For each scenario, assign a probability (low / medium / high), the expected timeline, and a tripwire signal (an observable event that would indicate the scenario is becoming real). Define a pre-committed response for each tripwire.

- **Artifact produced**: Surprise Entrant Scenarios (table with scenario, probability, timeline, tripwire signal, and pre-committed response)

### Step 6: Design the Monitoring System

Define an ongoing competitive intelligence cadence:
- **Weekly**: Track competitor product changes, job postings, pricing moves, and public communications
- **Monthly**: Update the Threat Classification Matrix from Step 2 with new data
- **Quarterly**: Re-run the full Moat Audit and revisit response strategy assignments
- List specific data sources for each cadence (e.g., competitor changelogs, LinkedIn job postings, App Store reviews, social media, SEC filings, patent filings, developer community sentiment)

- **Artifact produced**: Monitoring Cadence Plan (table of signals, sources, frequency, and responsible owner)

### Step 7: Synthesize the Response Playbook

Compile all artifacts from Steps 1-6 into a single executive-ready document:
1. Executive Summary (one paragraph: the competitive situation in plain language)
2. Competitive Landscape Map
3. Threat Classification Matrix
4. Moat Audit
5. Response Strategy Table with justifications
6. Surprise Entrant Scenarios
7. Monitoring Cadence Plan
8. Recommended immediate actions (top 3 things to do this week)

- **Artifact produced**: Competitive Response Playbook (the complete compiled document)

## Diagnostic Questions

1. **Who would you lose your next 10 customers to, and why?** This reveals the competitor that matters most, not the one that gets the most press.

2. **If a well-funded competitor copied your product feature-for-feature tomorrow, what would still be hard for them to replicate?** This isolates your true moat from features that feel defensible but are not.

3. **Which competitor are you most afraid of, and which are you spending the most time thinking about?** If these are different, you may be misallocating competitive attention.

4. **Has a competitor recently done something that changed a customer's buying criteria?** This signals a category-level shift that requires a structural response, not a feature response.

5. **Are there companies you do not consider competitors today that your customers mention in the same breath as your product?** This identifies emerging threats you may be blind to.

6. **What is the cheapest version of your product that would still be useful?** This reveals where a disruptor could enter from below (Christensen's low-end disruption).

7. **What would you build differently if your biggest competitor did not exist?** The gap between this answer and your current roadmap shows how much of your strategy is reactive versus proactive.

## Common Mistakes

1. **Treating all competitors as equal threats**
   Not every competitor deserves a response. The most common error is spreading resources across every name in the landscape instead of concentrating on the 1-2 that are Critical. Use the Threat Classification Matrix to force prioritization and explicitly assign "Ignore" to competitors that do not warrant action.

2. **Responding to features instead of strategies**
   Copying a competitor's feature is often the wrong response if the real threat is their distribution, pricing, or ecosystem position. Before fast-following any feature, ask: "Is this feature the cause of their advantage or a symptom of it?" Respond to the cause.

3. **Confusing motion with defense**
   Shipping faster is not a competitive strategy. If you lack a structural moat, speed only buys time. Use the Moat Audit to distinguish between speed (a temporary advantage) and power (a durable one). If no Power is present, building one is more important than shipping the next feature.

4. **Ignoring adjacent entrants until it is too late**
   The most dangerous competitors are often not in your competitive set today. Platform companies that add your feature as a free default, or startups that pivot into your space, are consistently underestimated. The Surprise Entrant Scenarios step exists specifically to combat this blind spot.

5. **Over-indexing on public signals**
   Press releases, funding announcements, and social media buzz are lagging indicators. The most important competitive signals are often quiet: a key hire, a subtle API change, a new integration partner, or a shift in job posting requirements. Design your monitoring system to capture these weak signals.

6. **Letting competitive analysis become a substitute for customer insight**
   Competitive response should inform your roadmap, not drive it. If more than 30% of your roadmap is reactive to competitors rather than driven by user needs, you have ceded strategic initiative. Always validate competitive responses against customer discovery data.

## Context Integration

This skill draws heavily from the `context/` directory when available. Here is how each subdirectory feeds into the analysis:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/competitive/` | Steps 1, 2, 4, 5 | Pre-existing competitor profiles, landscape overview, and per-competitor analysis. If `landscape.md` exists, use it as the starting point for the Competitive Landscape Map rather than building from scratch. Per-competitor files provide evidence for Threat Classification scoring. |
| `context/products/` | Steps 2, 3, 4 | Your own product descriptions, features, pricing, and technical architecture. Essential for scoring Overlap in the Threat Classification and for identifying which Powers exist in the Moat Audit. |
| `context/company/` | Steps 3, 5 | Funding, team size, org structure, and resource constraints. Informs what moat-building investments are feasible and which surprise entrant scenarios are most dangerous given your resource position. |
| `context/verticals/` | Steps 1, 5 | Target market information and vertical-specific dynamics. Helps identify which adjacent entrants are plausible based on vertical boundaries. |
| `context/founders/` | Step 3 | Founder backgrounds, technical depth, and domain expertise. Can serve as evidence for Cornered Resource or Process Power in the Moat Audit. |
| `context/signals/` | Steps 1, 2, 5, 6 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `github-ecosystem.md` for developer ecosystem momentum, `hackernews-sentiment.md` and `reddit-discussions.md` for community sentiment and surprise entrant signals, `news-coverage.md` for PR/funding signals, and `_synthesis.md` for competitor mention radar. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A brief description of their product and its core value proposition
2. A list of known competitors (even informal)
3. Their current understanding of what makes their product hard to replicate
4. The market vertical(s) they operate in
