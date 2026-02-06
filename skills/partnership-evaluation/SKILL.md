---
name: partnership-evaluation
description: "Help users evaluate potential partnerships by scoring strategic fit, modeling deal structures, and producing comparative assessments with go/no-go recommendations."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Partnership Evaluation

Produces partner scorecards, deal structure analysis, strategic fit assessments, and a comparative partnership ranking with go/no-go recommendations.

## Core Principles

1. **Every partnership is a co-innovation risk, not just a business deal**
   "In our interconnected world, the success of your innovation depends not just on your own efforts but on the ability of your partners to deliver their own innovations on time and to spec. The Wide Lens framework forces you to map the full ecosystem of co-innovators and adopters before committing to a partnership."
   -- *Ron Adner, Professor at Tuck School of Business and Author of The Wide Lens* ([source](https://www.harpercollins.com/products/the-wide-lens-ron-adner))

2. **Partnerships succeed when they create value neither party could capture alone**
   "An alliance makes sense only when the value you create together exceeds the sum of what each party could create independently, minus the coordination costs. If you can build it yourself and the coordination tax is high, you should."
   -- *Reid Hoffman, Co-founder of LinkedIn and Author of The Alliance* ([source](https://www.thealliance.com/))

3. **Business ecosystems co-evolve capabilities around a shared innovation**
   "An economic community supported by a foundation of interacting organizations and individuals -- the organisms of the business world. Over time, they coevolve their capabilities and roles, and tend to align themselves with the directions set by one or more central companies."
   -- *James F. Moore, Author of The Death of Competition* ([source](https://hbr.org/1993/05/predators-and-prey-a-new-ecology-of-competition))

4. **Aggregators control demand; platforms enable supply -- know which side of the table you are on**
   "Platforms and aggregators have fundamentally different partnership dynamics. A platform makes its partners more valuable by providing capabilities they lack. An aggregator commoditizes its partners by controlling the end-user relationship. The distinction determines whether a partnership is additive or extractive."
   -- *Ben Thompson, Founder of Stratechery* ([source](https://stratechery.com/2019/a-framework-for-moderation/))

5. **The best partnerships are ones where you each have a chokehold on different parts of the value chain**
   "The strongest strategic relationships are ones where each side controls something the other genuinely cannot replicate. When both partners have substitutes for what the other provides, the partnership is inherently fragile and will be renegotiated or abandoned at the first shift in leverage."
   -- *Elad Gil, Investor and Author of High Growth Handbook* ([source](https://growth.eladgil.com/))

6. **Alliance governance is more important than alliance strategy**
   "The primary reason strategic alliances fail is not poor strategy -- it is poor governance. Misaligned incentives, ambiguous decision rights, and absence of shared metrics create friction that compounds over time until one party exits. Define the operating model before you define the roadmap."
   -- *Benjamin Gomes-Casseres, Professor at Brandeis International Business School and Author of Remix Strategy* ([source](https://hbsp.harvard.edu/product/10013-PDF-ENG))

7. **Startups should partner from a position of unique value, never from a position of need**
   "Every partnership pitch from a startup that begins with 'we need their distribution' is already in trouble. The partner knows you need them more than they need you, and the deal terms will reflect that. Lead with what you can do for them that nobody else can."
   -- *Elad Gil, Investor and Author of High Growth Handbook* ([source](https://growth.eladgil.com/book/chapter-13/))

8. **Your partner's adoption chain is your adoption chain**
   "Before a partnership can deliver value, every actor in the adoption chain must have a reason to participate. If any link in the chain -- a distributor, a regulator, a complementor -- lacks incentive to adopt, the entire initiative stalls regardless of how strong the core partnership is."
   -- *Ron Adner, Professor at Tuck School of Business and Author of The Wide Lens* ([source](https://ronaldadner.com/the-wide-lens/))

## Instructions

### Step 1: Define Partnership Objectives and Selection Criteria

- Articulate the specific strategic gap the partnership is intended to fill. Categories include: distribution, technology, content/data, credibility/brand, regulatory access, or go-to-market acceleration.
- Define 2-3 non-negotiable requirements (e.g., "partner must have existing enterprise sales motion" or "partner must own training data we cannot license independently").
- Define 3-5 weighted evaluation criteria that will be used to score all candidate partners. Recommended dimensions:

| Criterion | Weight | What It Measures |
|---|---|---|
| **Strategic Fit** | 25% | How well the partner's capabilities fill the identified gap |
| **Value Asymmetry** | 20% | Whether each side brings something the other cannot replicate |
| **Execution Capability** | 20% | Partner's track record of shipping integrations on time |
| **Market Access** | 20% | Users, channels, or segments the partner unlocks |
| **Risk Profile** | 15% | Competitive overlap, dependency concentration, and exit cost |

- **Artifact produced**: Partnership Objectives Brief (strategic gap, non-negotiables, and weighted scoring criteria)

### Step 2: Map the Candidate Partner Landscape

- Identify 3-8 candidate partners across the categories defined in Step 1
- For each candidate, document:
  - Company name, size, and stage
  - Core product and user base
  - Relevant capabilities (what they bring to the table)
  - Existing partnerships and alliance history
  - Competitive overlaps or conflicts of interest
  - Public signals of partnership interest (integrations, blog posts, conference talks, shared customers)
- Group candidates into tiers: Tier 1 (ideal strategic fit), Tier 2 (viable alternative), Tier 3 (opportunistic only)
- **Artifact produced**: Candidate Partner Landscape Map (table with all candidates profiled and tiered)

### Step 3: Score Each Partner with the Strategic Fit Scorecard

Rate each candidate partner on the criteria from Step 1 using a 1-5 scale:

| Score | Meaning |
|---|---|
| 5 | Exceptional -- best-in-class across the industry |
| 4 | Strong -- clear evidence of capability with minor gaps |
| 3 | Adequate -- meets threshold but does not differentiate |
| 2 | Weak -- significant gaps that would require mitigation |
| 1 | Disqualifying -- fails the criterion or introduces unacceptable risk |

Compute a weighted total for each partner. Additionally, apply a **co-innovation risk assessment** for each partner (from Adner's Wide Lens framework):
- **Co-innovation risk**: How likely is the partner to deliver their required innovation on time?
- **Adoption chain risk**: Are there third parties whose participation is required for the partnership to deliver value?

Flag any partner with a co-innovation or adoption chain risk rated "high" -- even a high-scoring partner is dangerous if the ecosystem around the partnership is not ready.

- **Artifact produced**: Strategic Fit Scorecard (matrix of partners x criteria with weighted scores and risk flags)

### Step 4: Model the Deal Structure for Top Candidates

For each partner scoring above the go/no-go threshold (typically weighted score >= 3.5), model the deal structure:

- **Integration type**: API integration, co-built product, white-label, reseller, data-sharing, or co-marketing
- **Value exchange**: What each party gives and gets (be explicit about economics)
- **Revenue model**: Revenue share %, flat fee, usage-based, or non-monetary (brand, data, access)
- **Exclusivity terms**: Exclusive, semi-exclusive (category-limited), or non-exclusive
- **Duration and exit**: Contract length, renewal terms, and termination conditions
- **Investment required**: Engineering effort (person-weeks), go-to-market spend, and opportunity cost
- **Governance model**: Decision rights, escalation path, shared KPIs, and review cadence

For each deal model, compute a **Partnership ROI estimate**: expected incremental value (revenue, users, or strategic positioning) divided by total investment (engineering, GTM, and management overhead) over the contract term.

- **Artifact produced**: Deal Structure Analysis (one deal model per top candidate with ROI estimates)

### Step 5: Assess Risks and Dependency Scenarios

For each top candidate, evaluate:

- **Competitive risk**: Could this partner become a competitor? What happens if they build your capability internally?
- **Dependency concentration**: What percentage of your distribution, revenue, or technology would flow through this partner? Any single partner exceeding 30% of a critical input is a concentration risk.
- **Lock-in risk**: How costly is it to exit or switch partners? Rate switching cost as low / medium / high.
- **Reputational risk**: Does the partner's brand, conduct, or market position create exposure?
- **Execution risk**: Based on the partner's alliance history, what is the probability they under-deliver?

For each risk rated "high," define a specific mitigation strategy (e.g., contractual protections, parallel partnerships, internal capability building).

- **Artifact produced**: Risk Assessment Matrix (table of partners x risk dimensions with ratings and mitigations)

### Step 6: Produce the Comparative Ranking and Go/No-Go Recommendations

Combine the Strategic Fit Scorecard (Step 3), Deal Structure ROI (Step 4), and Risk Assessment (Step 5) into a final ranking:

| Rank | Partner | Weighted Score | ROI Estimate | Risk Level | Recommendation |
|---|---|---|---|---|---|
| 1 | | | | | GO / NO-GO / CONDITIONAL |
| 2 | | | | | GO / NO-GO / CONDITIONAL |
| ... | | | | | |

For each partner, issue one of three recommendations:
- **GO**: Proceed to negotiation. Strategic fit is strong, ROI is positive, and risks are manageable.
- **CONDITIONAL**: Proceed only if specific conditions are met (name them). Typically used when a single high risk has an actionable mitigation.
- **NO-GO**: Do not pursue. The strategic fit is insufficient, the ROI is negative, or the risks are unacceptable. Document the specific reason to avoid revisiting the decision without new information.

Include a one-paragraph narrative justification for each recommendation linking back to the scorecard, deal model, and risk assessment.

- **Artifact produced**: Partnership Ranking with Go/No-Go Recommendations (the final comparative table and narrative justifications)

### Step 7: Draft the Partnership Execution Roadmap

For each partner receiving a GO recommendation, draft a 90-day execution roadmap:

- **Days 1-15**: Internal alignment (stakeholder buy-in, resource allocation, legal review initiation)
- **Days 16-30**: Partner outreach and initial negotiation (term sheet, scope definition, shared KPI agreement)
- **Days 31-60**: Technical scoping and integration design (API contracts, data flows, architecture review)
- **Days 61-90**: Pilot launch (limited rollout, success metrics tracking, first governance review)

Define the success criteria for the pilot and the decision point for scaling to full production.

- **Artifact produced**: Partnership Execution Roadmap (90-day plan per GO partner with milestones and decision gates)

## Diagnostic Questions

1. **What specific capability gap are you trying to fill, and have you exhausted the build-it-yourself option?** Partnerships carry coordination costs; they are only justified when the alternative (building internally) is slower, more expensive, or impossible.

2. **What does the partner get from you that they cannot get elsewhere?** If the answer is "nothing unique," you have no leverage and the deal terms will reflect it. Reframe or walk away.

3. **If this partner became a competitor in 18 months, how exposed would you be?** This surfaces the dependency and competitive risks that are easy to ignore during the optimism of early conversations.

4. **Who else in the adoption chain must participate for this partnership to deliver value?** A partnership between two willing parties still fails if distributors, regulators, or complementors do not play their roles.

5. **What is the smallest possible version of this partnership you could test in 30 days?** If the partnership cannot be piloted cheaply, the execution risk is high and the feedback loop is too slow.

6. **Has this partner successfully executed a similar partnership before, and can you talk to the other party?** Alliance history is the strongest predictor of alliance success. Reference checks on partners are as important as reference checks on hires.

## Common Mistakes

1. **Partnering from a position of need rather than strength**
   The most common failure mode is pursuing partnerships to compensate for a weakness rather than to extend a strength. Partners can sense desperation, and the resulting deal terms reflect the power imbalance. Always lead with what you uniquely offer before discussing what you need.

2. **Skipping the governance model**
   Teams obsess over the strategic rationale and ignore the operating model. Without clear decision rights, shared KPIs, escalation paths, and a regular review cadence, even strategically sound partnerships decay into finger-pointing within two quarters.

3. **Evaluating partners in isolation instead of comparatively**
   Assessing a single partner in a vacuum almost always produces a GO recommendation because there is no benchmark for "good enough." Always score at least 2-3 candidates against the same criteria to establish a comparative baseline.

4. **Ignoring co-innovation and adoption chain risk**
   A partner can score perfectly on strategic fit and still fail to deliver because a third party in the value chain is not ready. Map the full ecosystem of participants required for the partnership to create end-user value, and assess each link independently.

5. **Conflating a warm relationship with a strong partnership**
   Personal rapport with a partner's team is necessary but not sufficient. Good partnerships are built on structural alignment of incentives, not on the enthusiasm of individual champions. When the champion leaves, the structural logic must sustain the relationship.

## Context Integration

This skill draws from the `context/` directory when available. Here is how each subdirectory feeds into the analysis:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 3, 4 | Your own product descriptions, capabilities, technical architecture, and pricing. Essential for defining the strategic gap in Step 1 and for modeling value exchange in Step 4. |
| `context/company/` | Steps 1, 4, 5 | Funding stage, team size, org structure, and resource constraints. Informs what partnership investments are feasible, what dependency concentrations are acceptable, and what deal structures are realistic given your leverage. |
| `context/competitive/` | Steps 2, 5 | Competitor profiles and landscape overview. Critical for identifying which candidate partners have competitive overlaps or conflicts of interest, and for assessing whether a partner could become a competitor. |
| `context/verticals/` | Steps 2, 3 | Target market information and vertical-specific dynamics. Helps evaluate which partners unlock new verticals and whether the partner's market access aligns with your go-to-market priorities. |
| `context/founders/` | Steps 1, 6 | Founder backgrounds, network, and domain expertise. Relevant for assessing whether existing founder relationships can accelerate partner outreach, and for calibrating the strategic gap assessment. |
| `context/signals/` | Steps 2, 3, 5 | Auto-collected signals from GitHub, HN, Reddit, and news. [SIGNAL] tagged. Use `github-ecosystem.md` for partner integration activity, `news-coverage.md` for partnership announcements and funding signals, and `_synthesis.md` for ecosystem relationship mapping. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. A description of their product and the strategic gap they want to fill through partnerships
2. A list of candidate partners they are considering (even informal)
3. Their current stage, team size, and resource constraints
4. The verticals or markets they are targeting
