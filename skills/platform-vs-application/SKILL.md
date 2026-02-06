---
name: platform-vs-application
description: "Help users decide whether to build a platform, an application, or a hybrid by analyzing ecosystem dynamics, developer economics, and strategic positioning."
---

# Platform vs Application

Guides users through a structured analysis to determine the optimal build strategy -- platform, application, or hybrid -- producing a build/buy/partner analysis, platform economics model, ecosystem design, and an investment allocation recommendation.

## Core Principles

1. **Software is eating the world, but platforms are eating software**
   "In a world where every company is becoming a software company, the most valuable companies are the ones that become platforms -- enabling entire ecosystems of third-party innovation on top of their core product."
   -- *Marc Andreessen, Co-founder of Andreessen Horowitz* ([source](https://a16z.com/why-software-is-eating-the-world/))

2. **Aggregators win by controlling demand, not by producing supply**
   "The key insight of Aggregation Theory is that the internet has made distribution free, removing the need for intermediaries that controlled access to customers. The winners are aggregators that own the user relationship and commoditize suppliers, not platforms that serve suppliers."
   -- *Ben Thompson, Founder of Stratechery* ([source](https://stratechery.com/2015/aggregation-theory/))

3. **Platforms beat products because they harness network effects**
   "A platform is a business model that creates value by facilitating exchanges between two or more interdependent groups. The platform's overarching purpose is to consummate matches among users and facilitate the exchange of goods, services, or social currency, thereby enabling value creation for all participants."
   -- *Sangeet Paul Choudary, Author of Platform Scale and co-author of Platform Revolution* ([source](https://platformed.info/platform-scale/))

4. **Smart companies commoditize their complements**
   "Every product in the demand chain is either a substitute or a complement of every other product. A smart company tries to commoditize its products' complements. All else being equal, demand for a product increases when the prices of its complements decrease. This is Economics 101."
   -- *Joel Spolsky, Co-founder of Stack Overflow and Fog Creek Software* ([source](https://www.joelonsoftware.com/2002/06/12/strategy-letter-v/))

5. **The next big thing always starts out looking like a toy**
   "Something that looks like a toy to most people but is already useful to a small number of early adopters is often the seed of a platform shift. Dismissing new technologies as toys has caused large incumbents to miss transformative platform opportunities over and over again."
   -- *Chris Dixon, General Partner at Andreessen Horowitz* ([source](https://cdixon.org/2010/01/03/the-next-big-thing-will-start-out-looking-like-a-toy))

6. **Map the landscape before choosing where to build**
   "All components evolve from genesis to commodity. Strategy depends on understanding where each component sits on that evolution axis. Build custom only what is novel; consume as commodity everything that is industrialized. The mistake is building platforms where the component has already been commoditized -- or shipping applications where a platform play would capture the value chain."
   -- *Simon Wardley, Researcher at the Leading Edge Forum* ([source](https://medium.com/wardleymaps/on-being-lost-2ef5f05eb1ec))

7. **Come for the tool, stay for the network**
   "The best way to bootstrap a platform is to first build a single-player tool that is useful on its own, then layer on multi-player network effects once you have a critical mass of users. Starting with the network before the tool almost never works because you face a cold-start problem."
   -- *Chris Dixon, General Partner at Andreessen Horowitz* ([source](https://cdixon.org/2015/01/31/come-for-the-tool-stay-for-the-network))

8. **Platform value scales with the square of participants; application value scales linearly**
   "A platform that connects N participants can facilitate up to N-squared interactions. This is fundamentally different from an application, where value scales linearly with users. The implication is that platforms, once past critical mass, generate increasing returns -- but they require far more patience and investment to reach that threshold."
   -- *Sangeet Paul Choudary, Author of Platform Scale* ([source](https://platformed.info/platform-scale/))

## Instructions

### Step 1: Map the Value Chain and Identify Control Points

- Diagram the full value chain for your product category, from raw inputs to end-user outcomes
- For each stage, document: who owns it today, whether it is commoditized or differentiated, and whether value is accruing to the layer above or below
- Apply Wardley Mapping principles: plot each component on the genesis-to-commodity evolution axis and assess movement direction
- Identify the 1-3 control points where strategic leverage is highest -- these are the stages where switching costs are high, supply is constrained, or network effects can form
- **Artifact produced**: Value Chain Map with control point annotations (diagram or structured table showing each layer, current owner, evolution stage, and strategic leverage score 1-5)

### Step 2: Assess Platform Viability

Evaluate whether a platform strategy is viable by scoring the following preconditions (1-5 scale each):

| Precondition | What It Tests |
|---|---|
| **Multi-sided demand** | Are there at least two distinct user groups that need each other? |
| **Fragmented supply** | Is the supply side made up of many small providers rather than a few large ones? |
| **Transaction friction** | Is there meaningful friction in how these groups currently find and transact with each other? |
| **Network effect potential** | Does each additional participant make the platform more valuable to others? |
| **Commoditized complement** | Can you commoditize a complement (per Spolsky) to increase demand for your platform layer? |
| **Repeatable interaction** | Will participants return and transact repeatedly, not just once? |

Compute a **Platform Viability Score** (max 30). Classify:
- **Strong candidate (24-30)**: Platform economics are favorable; prioritize platform investment
- **Conditional (16-23)**: Platform is viable but requires deliberate network-effect bootstrapping
- **Weak (8-15)**: Application-first strategy is likely superior; platform can be layered later
- **Non-viable (1-7)**: Do not pursue a platform strategy; build an application

- **Artifact produced**: Platform Viability Scorecard (table with precondition ratings, total score, classification, and rationale for each rating)

### Step 3: Model Platform Economics

If the Platform Viability Score is 16 or above, build a quantitative model:

- **Participant economics**: For each side of the platform, estimate cost of acquisition, lifetime value, and contribution to the other side's value
- **Critical mass threshold**: Estimate the minimum number of participants on each side needed before self-sustaining network effects kick in (the point where organic growth exceeds paid acquisition)
- **Subsidy strategy**: Determine which side to subsidize and which to monetize. The side with more price sensitivity and higher contribution to cross-side value is typically subsidized
- **Time to critical mass**: Estimate months and capital required to reach critical mass given current growth rate and acquisition costs
- **Rake/take-rate benchmark**: Research comparable platforms in adjacent markets and document their take rates as a benchmark range

- **Artifact produced**: Platform Economics Model (spreadsheet or structured table showing participant economics per side, critical mass estimates, subsidy allocation, time-to-critical-mass projection, and take-rate benchmarks)

### Step 4: Design the Ecosystem Architecture

Define the structural design of the platform ecosystem:

- **Core interaction**: What is the single most important interaction the platform enables? (e.g., "developer publishes integration; end-user discovers and installs it")
- **Governance model**: What rules govern participation? Who can join? What quality standards apply? How are disputes resolved?
- **Incentive alignment**: What motivates each participant type to contribute? How do you prevent value extraction without contribution?
- **API surface**: What capabilities are exposed programmatically? What is kept internal? Apply the Spolsky complement test -- expose as API anything that commoditizes a complement
- **Extension model**: How do third parties extend the platform? (plugins, integrations, marketplace listings, SDKs)
- **Trust architecture**: How is trust established between participants who do not know each other? (ratings, reviews, verification, escrow, SLAs)

- **Artifact produced**: Ecosystem Design Document (structured specification covering core interaction, governance, incentives, API surface, extension model, and trust architecture)

### Step 5: Conduct Build / Buy / Partner Analysis

For each major capability needed in the product, decide whether to build, buy, or partner:

| Capability | Build | Buy | Partner | Recommendation | Rationale |
|---|---|---|---|---|---|
| *Capability name* | Cost / timeline / risk | Vendor options / cost | Partner options / terms | One of B/B/P | Why |

Decision criteria:
- **Build** when the capability is a core differentiator, is on the genesis end of the evolution axis, or when no adequate external option exists
- **Buy** when the capability is commoditized, time-to-market is critical, and reliable vendors exist
- **Partner** when another company has a complementary strength, the capability requires domain expertise you lack, or co-marketing creates mutual value

- **Artifact produced**: Build/Buy/Partner Matrix (table with each capability, all three options evaluated, final recommendation, and rationale)

### Step 6: Define the Investment Allocation

Based on all preceding analysis, allocate investment across four buckets:

- **Core product** (the application layer that delivers direct user value)
- **Platform infrastructure** (APIs, SDKs, developer tools, partner onboarding)
- **Ecosystem development** (developer relations, marketplace seeding, partner programs)
- **Go-to-market** (sales, marketing, community, content)

Express allocation as percentage of total product investment (engineering + design + PM time). Provide a recommended allocation for the next 12 months and a projected shift for months 13-24 as the platform matures.

Include a sensitivity analysis: if Platform Viability Score had been one tier lower, how would the allocation change?

- **Artifact produced**: Investment Allocation Recommendation (pie chart or table with four buckets, 12-month allocation, 24-month projection, and sensitivity analysis)

### Step 7: Synthesize the Strategy Memo

Compile all artifacts into a single executive-ready document:

1. Executive Summary (one paragraph: the strategic recommendation in plain language)
2. Value Chain Map with control points
3. Platform Viability Scorecard with classification
4. Platform Economics Model (if applicable)
5. Ecosystem Design Document (if applicable)
6. Build/Buy/Partner Matrix
7. Investment Allocation Recommendation
8. Key risks and mitigation strategies
9. Decision criteria for revisiting the platform-vs-application choice (specific metrics and thresholds that would trigger a strategy pivot)

- **Artifact produced**: Platform Strategy Memo (the complete compiled document)

## Diagnostic Questions

1. **If you removed your product tomorrow, would any third party's business break?** If yes, you already have platform dynamics whether you designed for them or not. If no, you are an application -- and that may be the right answer.

2. **Are your users asking for APIs and integrations, or for more features?** API requests signal latent platform demand. Feature requests signal application demand. The ratio reveals where you sit on the spectrum.

3. **Does each additional user make your product more valuable to other users, or only to that user?** This is the litmus test for network effects. If value is purely single-player, a platform strategy will stall at the cold-start problem.

4. **What would happen if a large platform added your product's core functionality for free?** If the answer is "we'd lose most of our users," you are a feature, not a product. Consider whether becoming a platform yourself is the way to avoid being commoditized.

5. **Who are you subsidizing, and is that the right side?** Every platform subsidizes one side. If you are not deliberately choosing which side to subsidize, you are probably subsidizing the wrong one, or subsidizing neither and failing to grow.

6. **What is the complement to your product, and who controls it?** Per Spolsky and Wardley, the strategic move is to commoditize your complement. If someone else controls your complement and is not commoditizing it, they hold leverage over your business.

7. **Could you reach critical mass in a single niche before expanding?** Most successful platforms start narrow. If your platform strategy requires broad adoption across multiple segments simultaneously, the cold-start problem may be insurmountable.

## Common Mistakes

1. **Building a platform before achieving product-market fit as an application**
   The "come for the tool, stay for the network" principle exists because platforms without a strong single-player use case face an impossible cold-start problem. Ship an application that is independently valuable first. Layer on platform dynamics only after you have a retained user base that third parties want to reach.

2. **Confusing an API with a platform**
   Exposing an API does not make you a platform. A platform requires multi-sided network effects where participants on each side increase value for the other side. An API alone is just a distribution mechanism for your application. Before claiming a platform strategy, verify that you pass the multi-sided demand precondition in Step 2.

3. **Subsidizing the wrong side of the market**
   Platform economics require subsidizing one side to attract the other. The most common error is subsidizing the side that is easiest to acquire rather than the side whose presence creates the most cross-side value. Use the participant economics model in Step 3 to make this decision with data, not intuition.

4. **Underestimating time and capital to reach critical mass**
   Platforms have a J-curve: they require significant investment before network effects generate self-sustaining growth. Teams that apply application-stage growth expectations to a platform-stage product will either kill the strategy prematurely or run out of runway. The Platform Economics Model in Step 3 exists to make this timeline explicit and fundable.

5. **Trying to be both aggregator and platform simultaneously**
   Per Ben Thompson, aggregators control the user relationship and commoditize suppliers; platforms empower suppliers and facilitate direct relationships. These are different strategies with different economics. Trying to do both creates conflicting incentives -- you cannot empower your ecosystem partners while also disintermediating them. Choose one.

6. **Ignoring governance until the ecosystem is in crisis**
   Platform governance -- who can participate, what quality standards apply, how disputes are resolved -- feels premature when you have 10 ecosystem partners. But governance decisions made under pressure at 1,000 partners are almost always worse than those designed deliberately at 10. Define governance in Step 4 before you need it.

## Context Integration

This skill draws from the `context/` directory when available. Here is how each subdirectory feeds into the analysis:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 4, 5 | Your product descriptions, technical architecture, and API surface. Essential for mapping the value chain, assessing platform viability preconditions, and deciding which capabilities to build vs buy vs partner. |
| `context/competitive/` | Steps 1, 2, 6 | Competitor profiles and landscape overview. Reveals whether competitors are pursuing platform or application strategies, which control points are contested, and how investment allocation should account for competitive dynamics. |
| `context/company/` | Steps 3, 5, 6 | Funding, team size, and resource constraints. Critical for estimating time to critical mass, evaluating build vs buy feasibility, and setting realistic investment allocation percentages. |
| `context/verticals/` | Steps 1, 2, 4 | Target market and vertical-specific dynamics. Informs whether multi-sided demand exists, how fragmented the supply side is, and what governance model fits the vertical's norms. |
| `context/founders/` | Steps 3, 5 | Founder backgrounds, technical depth, and domain expertise. Helps assess whether the team can credibly execute a platform strategy and where build vs partner decisions should lean toward partner. |
| `context/signals/` | Steps 2, 5, 6 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `github-ecosystem.md` for developer adoption signals relevant to platform viability, `hackernews-sentiment.md` and `reddit-discussions.md` for ecosystem sentiment, and `_synthesis.md` for emerging platform-vs-application positioning shifts in the market. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A description of their product and its core user value proposition
2. Whether they currently have an API, SDK, or any third-party integrations
3. Who the distinct user groups are that interact with or through their product
4. Their current team size, funding stage, and time horizon for the strategy
