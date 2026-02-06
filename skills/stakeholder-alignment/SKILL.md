---
name: stakeholder-alignment
description: "Help users align cross-functional stakeholders by producing stakeholder maps, RACI matrices, communication plans, decision-making frameworks, and research-product interface designs."
---

# Stakeholder Alignment

Produces a stakeholder map, RACI matrix, communication plan, decision-making framework, and research-product interface design to align cross-functional teams around shared goals, especially in research-led organizations where the tension between exploration and execution is the central coordination challenge.

## Core Principles

1. **Empowered teams require empowered stakeholders**
   "In the empowered team model, the product team is given problems to solve, not features to build — and they are empowered to come up with solutions that work for the customer AND work for the business."
   — *Marty Cagan, Partner at Silicon Valley Product Group* ([source](https://www.svpg.com/empowered-product-teams/))

   Stakeholder alignment is not about getting sign-off. It is about ensuring every stakeholder understands the problem space deeply enough to trust the product team's decisions. The RACI matrix should reflect empowerment, not control. If every decision requires escalation, you have a governance document, not an alignment plan.

2. **Managing up is not optional; it is the job**
   "Your manager is your ally, not your enemy. The sooner you learn to work with them effectively, the faster you can grow."
   — *Julie Zhuo, former VP of Product Design at Meta* ([source](https://www.juliezhuo.com/book/manager.html))

   Stakeholder alignment runs in all directions: up to executives, across to peer functions, and down to individual contributors. The communication plan must differentiate between these audiences. Executives need strategic context and decision points. Peers need coordination cadences. ICs need clarity on their autonomy boundary.

3. **Bring the donuts — build relationships before you need them**
   "Product management is fundamentally about earning trust and building relationships. Bring the donuts. Show up for people before you need something from them."
   — *Ken Norton, former Partner at Google Ventures* ([source](https://www.bringthedonuts.com/essays/leading-cross-functional-teams.html))

   The stakeholder map is not a one-time artifact. It is a living relationship inventory. The PM who only reaches out to stakeholders when a decision is needed will find those stakeholders unresponsive or adversarial. Build the relationship infrastructure before the first contentious decision arrives.

4. **Radical focus comes from saying no together**
   "If everything is important, nothing is important. You need to pick the one thing and say no to everything else."
   — *Christina Wodtke, author of Radical Focus* ([source](https://eleganthack.com/the-art-of-the-okr/))

   Alignment is not consensus. Alignment is a shared understanding of what the team will NOT do and why. The decision-making framework must include explicit criteria for saying no. If the stakeholder group cannot agree on what to deprioritize, they are not aligned — they are just polite.

5. **Without trust, no team can function**
   "Not finance. Not strategy. Not technology. It is teamwork that remains the ultimate competitive advantage, both because it is so powerful and so rare."
   — *Patrick Lencioni, author of The Five Dysfunctions of a Team* ([source](https://www.tablegroup.com/the-five-dysfunctions-of-a-team/))

   Lencioni's dysfunction pyramid starts with absence of trust and ends with inattention to results. Every stakeholder alignment artifact in this skill — the RACI, the comms plan, the decision framework — is a tool for building trust through transparency. If stakeholders do not feel safe raising concerns, the artifacts become theater.

6. **Disagree and commit is a feature, not a failure**
   "Have backbone; disagree and commit. Leaders are obligated to respectfully challenge decisions when they disagree, even when doing so is uncomfortable. Once a decision is determined, they commit wholly."
   — *Jeff Bezos, founder of Amazon* ([source](https://www.aboutamazon.com/about-us/leadership-principles))

   The decision-making framework must define what happens after the debate. Many teams are good at surfacing disagreement but bad at reaching closure. The framework should specify: who makes the call, by when, and what "commit" looks like for the people who disagreed. Without this, alignment erodes the moment the meeting ends.

7. **Research and product speak different languages — translate deliberately**
   "The transition from research to product requires a translation layer. Researchers optimize for novelty and correctness. Product teams optimize for reliability and user value. Neither is wrong, but both must understand the other's constraints."
   — *Shreya Shankar, ML Engineer and UC Berkeley researcher* ([source](https://www.shreya-shankar.com/phd-year-one/))

   In research-led organizations, the single most important alignment interface is between the research team and the product team. The research-product interface design must make implicit assumptions explicit: What does "ready" mean? What does "good enough" mean? Who decides when a capability moves from research to product? This translation layer prevents the most common failure mode: researchers feeling exploited and PMs feeling blocked.

8. **Write it down or it did not happen**
   "The discipline of writing things down forces a degree of precision that oral conversation does not. Writing is not the artifact; clarity is."
   — *Ben Horowitz, co-founder of Andreessen Horowitz* ([source](https://a16z.com/good-product-manager-bad-product-manager/))

   Every alignment artifact in this skill is a written document. Not because documentation is inherently valuable, but because writing forces precision. A verbal agreement on roles and responsibilities will be remembered differently by every person in the room. A written RACI matrix will not. The communication plan should specify which decisions require written artifacts and which can be verbal.

## Instructions

### Step 1: Map the Stakeholder Landscape

Produce a **Stakeholder Map** identifying every person and function that has influence over or is affected by the product.

- Read `context/company/` to understand organizational structure, team composition, and reporting lines
- Read `context/founders/` to understand the founding team's vision and where decision authority concentrates
- Identify every stakeholder by name and role, not just by function ("research team" is not a stakeholder; "Dr. X, research lead for 3D generation" is)
- For each stakeholder, document:
  - **Influence level:** Decision-maker, strong influencer, contributor, or informed
  - **Interest level:** High (actively engaged), medium (engaged when relevant), low (needs only updates)
  - **Disposition:** Champion, supporter, neutral, skeptic, or blocker
  - **Core concern:** The one thing this person cares most about (e.g., research velocity, launch dates, user experience, technical debt)
- Plot stakeholders on a 2x2 influence/interest matrix to identify the four quadrants: manage closely (high/high), keep satisfied (high/low), keep informed (low/high), monitor (low/low)

**Output:** A Stakeholder Map with named individuals, their influence/interest positions, dispositions, and core concerns.

### Step 2: Build the RACI Matrix

Produce a **RACI Matrix** mapping every major decision and deliverable to clear roles.

- List the 10-20 most critical decisions and deliverables for the product (e.g., API design, launch timeline, pricing, quality bar, research roadmap prioritization)
- For each item, assign exactly one of four roles to every relevant stakeholder:
  - **R (Responsible):** Does the work
  - **A (Accountable):** Makes the final decision; exactly one person per item
  - **C (Consulted):** Provides input before the decision
  - **I (Informed):** Told after the decision is made
- Validate: No item should have more than one A. No item should have zero R's. If a stakeholder is C on more than 60% of items, they are a bottleneck — redesign.
- Flag any items where the A and R are both researchers — these are the research-product handoff points that need explicit interface design in Step 6

**Output:** A RACI Matrix table with all critical decisions, named stakeholders, and validated role assignments.

### Step 3: Design the Communication Plan

Produce a **Communication Plan** specifying how information flows between stakeholders at defined cadences.

- Read `context/products/` to understand existing communication norms and tooling
- For each stakeholder quadrant from Step 1, define:
  - **Cadence:** How often they receive updates (daily, weekly, biweekly, monthly, ad hoc)
  - **Format:** Standup, written brief, dashboard, 1:1, all-hands, Slack channel, email digest
  - **Content:** What information they need (progress, blockers, decisions needed, metrics, context)
  - **Owner:** Who is responsible for preparing and delivering each communication
- Design escalation paths: When a decision is blocked, who escalates to whom, within what timeframe?
- Specify the "single source of truth" for project status (one document or dashboard, not many)
- Include asynchronous-first defaults with synchronous meetings reserved for decisions, not status updates

**Output:** A Communication Plan table with cadence, format, content, and owner for each stakeholder group, plus escalation paths.

### Step 4: Define the Decision-Making Framework

Produce a **Decision-Making Framework** that specifies how the team makes different types of decisions.

- Classify decisions into three tiers:
  - **Tier 1 — Reversible and low-stakes:** Made by the individual closest to the work, communicated async. Examples: copy changes, minor UI tweaks, internal tooling choices
  - **Tier 2 — Significant but bounded:** Made by the product lead with input from affected stakeholders (C in RACI), decided within 48 hours. Examples: feature scope, sprint priorities, API parameter naming
  - **Tier 3 — Irreversible or high-stakes:** Made with full stakeholder input, explicit decision meeting, written rationale. Examples: pricing model, public API contract, launch date, deprecation
- For each tier, specify: who decides, how input is gathered, what the time limit is, and what "disagree and commit" looks like
- Read `context/competitive/` to identify decisions that are time-sensitive due to competitive pressure — these may need compressed decision timelines
- Define the "decision log" format: every Tier 2 and Tier 3 decision is documented with date, decision-maker, options considered, rationale, and dissenting views

**Output:** A Decision-Making Framework with tier definitions, decision criteria, time limits, and a decision log template.

### Step 5: Design the Research-Product Interface

Produce a **Research-Product Interface Design** specifying how the research and product functions coordinate.

- Read `context/founders/` to understand the founding team's expectations for research-product interaction
- Define the handoff protocol:
  - What artifacts does research deliver to product? (Model weights, evaluation results, capability documentation, known limitations)
  - What does "research complete" mean in concrete, testable terms?
  - Who decides when a capability moves from research exploration to product hardening?
- Define the feedback protocol:
  - What product data flows back to research? (User behavior, failure modes, edge cases, feature requests)
  - At what cadence does product share insights with research?
  - How does research signal that a new capability is approaching productization readiness?
- Design the shared ritual: a recurring meeting (suggest biweekly) where research and product jointly review the pipeline of capabilities moving toward productization, using the Research Readiness Scorecard format if available
- Address the incentive gap: researchers publish papers, PMs ship products. The interface design should create shared wins (e.g., joint blog posts, research papers citing product usage data, product launches crediting research breakthroughs)

**Output:** A Research-Product Interface Design with handoff protocol, feedback protocol, shared ritual, and incentive alignment plan.

### Step 6: Validate and Stress-Test the Alignment Plan

Produce a **Validation Report** by testing the alignment plan against real scenarios.

- Select 3-5 recent or anticipated contentious decisions (e.g., "Should we delay launch to improve quality?" or "Should research prioritize the product team's request over their current exploration?")
- For each scenario, walk through the alignment plan:
  - Does the RACI clearly identify who decides?
  - Does the communication plan ensure the right people are informed at the right time?
  - Does the decision framework produce a timely resolution?
  - Does the research-product interface handle the handoff or feedback clearly?
- Identify gaps: any scenario where the plan breaks down, produces ambiguity, or creates a bottleneck
- Revise the artifacts from Steps 2-5 to close identified gaps
- Document remaining risks: alignment challenges that the plan mitigates but cannot eliminate (e.g., founder override, external market shocks, key person dependency)

**Output:** A Validation Report documenting each stress-test scenario, how the plan performed, what was revised, and what residual risks remain.

## Diagnostic Questions

1. **Can every stakeholder name the single person accountable for the most critical decision?** If two people think they are the decision-maker, or nobody does, the RACI is broken. Test this by asking — do not assume the document is being read.

2. **Does the research team know what "good enough for product" means in specific, measurable terms?** If the handoff criteria are subjective ("when it feels ready"), the interface will generate friction at every transition. Define thresholds, not feelings.

3. **When was the last time the team genuinely disagreed and reached closure within the framework?** If the answer is "never" or "we just avoid conflict," the decision framework is decorative. Healthy teams disagree frequently and resolve quickly.

4. **Is any stakeholder consulted on more than 60% of decisions?** This person is a bottleneck regardless of their talent. The RACI should redistribute their involvement to only the decisions where their input is genuinely irreplaceable.

5. **Do researchers and product managers attend each other's reviews?** If research reviews and product reviews are separate audiences with no overlap, the two functions are aligned on paper but diverging in practice. The shared ritual from Step 5 should prevent this.

6. **Can you point to a written decision log with at least five entries?** If the decision-making framework exists but nobody logs decisions, the framework is not in use. The log is the evidence that alignment is operational, not aspirational.

7. **Would a new team member understand the power dynamics from the artifacts alone?** The stakeholder map and RACI should make implicit organizational dynamics explicit enough that someone joining next month can navigate them without six weeks of hallway conversations.

## Common Mistakes

1. **Treating alignment as a one-time event rather than a continuous practice**
   Many PMs build the RACI and communication plan at project kickoff and never revisit them. Stakeholder dynamics shift as the project evolves — new people join, priorities change, power shifts. Schedule a quarterly alignment review to update all artifacts and surface emerging tensions before they become crises.

2. **Confusing consensus with alignment**
   Alignment means everyone understands the decision, the rationale, and their role — even if they disagree. Consensus means everyone agrees. Pursuing consensus on every decision paralyzes the team. The decision framework must explicitly permit decisions where some stakeholders disagree but commit.

3. **Building the RACI around functions instead of named individuals**
   A RACI that says "Engineering" is accountable is a RACI that says nobody is accountable. Use specific names. When someone changes roles, update the RACI. The discomfort of naming names is precisely what makes the exercise valuable.

4. **Ignoring the research team's publication incentives**
   In research-led organizations, researchers are motivated by papers, conference presentations, and intellectual recognition. If the alignment plan treats researchers as a service function that produces models on demand, they will disengage. The research-product interface must create shared incentives where productization generates publishable insights.

5. **Over-communicating status, under-communicating context**
   Many communication plans devolve into status update theaters — weekly emails that say "on track" without explaining why the work matters or what decisions are coming. The communication plan should prioritize context (why are we doing this, what trade-offs are we making) over status (what percentage complete are we).

6. **Designing the decision framework for normal times only**
   Most decision frameworks work when things are calm. They break under pressure — a competitor launches, a key researcher leaves, an investor demands a pivot. The framework must include a "crisis mode" protocol that compresses decision timelines and clarifies who has authority when speed matters more than consensus.

## Context Integration

This skill draws from multiple context directories to produce its artifacts:

| Context Directory | Used In | Purpose |
|---|---|---|
| `context/company/` | Step 1 (Stakeholder Map), Step 2 (RACI Matrix) | Organizational structure, reporting lines, and team composition determine who the stakeholders are and where decision authority resides. Funding stage signals whether governance should be lightweight (early stage) or structured (growth stage). |
| `context/founders/` | Step 1 (Stakeholder Map), Step 5 (Research-Product Interface) | Founder vision and leadership style shape the research-product dynamic. Founder-led research organizations have different alignment needs than those with hired research leaders. Understanding founder priorities prevents building alignment plans that conflict with implicit authority structures. |
| `context/products/` | Step 2 (RACI Matrix), Step 3 (Communication Plan) | Existing product surface reveals which decisions are already governed by established processes and which are new. Current communication tooling and norms inform realistic cadence design rather than aspirational ones. |
| `context/competitive/` | Step 4 (Decision-Making Framework), Step 6 (Validation Report) | Competitive pressure determines how fast decisions must be made. A fast-moving competitor compresses Tier 2 decision windows from 48 hours to 24. Competitive scenarios are excellent stress tests for the alignment plan. |
| `context/verticals/` | Step 2 (RACI Matrix), Step 5 (Research-Product Interface) | Different verticals have different stakeholder profiles. A gaming vertical involves creative directors and level designers; a robotics vertical involves simulation engineers and safety reviewers. The RACI and interface design must reflect vertical-specific roles. |

When `context/` directories are not populated, the skill prompts the user for the equivalent information before proceeding with each step.
