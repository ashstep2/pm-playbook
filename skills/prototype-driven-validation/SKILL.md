---
name: prototype-driven-validation
description: "Help users replace PRD-first workflows with prototype-first validation — producing prototype briefs, variation matrices, customer test plans, feedback synthesis, and build/kill decisions grounded in real user reactions to tangible artifacts."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Prototype-Driven Validation

Produces a prototype brief, variation matrix, customer test plan, feedback synthesis report, and a build/kill decision — replacing the traditional PRD-first workflow with a prototype-first approach that validates desirability and feasibility before committing to a full spec. Reach for this skill when confidence is low, when stakeholders disagree on the right direction, or when a concept needs to survive contact with real users before it earns a PRD.

## Core Principles

1. **A prototype saves a thousand meetings**
   "A prototype is worth a thousand meetings. You can debate an idea endlessly, or you can build a rough version and let people react to something real."
   -- *Charlie Sutton, Chief Design Officer at Atlassian* ([source](https://www.atlassian.com/blog/leadership))

   Prototypes collapse ambiguity faster than any document. When stakeholders cannot agree on a direction, show them something tangible. When you are unsure if the concept works, build a rough version and test it. The goal is not to build the product — it is to answer the most dangerous questions before committing resources.

2. **You have to actually build it to answer that**
   "There are some questions you can only answer by building something. Not by writing about it, not by discussing it, not by analyzing it — by actually making a thing that someone can touch and react to."
   -- *MJ Felix, Product Lead at Notion* ([source](https://www.notion.so/blog/building-product))

   Many product decisions look clear on paper but fall apart in practice. Interaction details, information hierarchy, and moment-to-moment user experience can only be evaluated through tangible artifacts. If the question is about desirability, usability, or emotional resonance, the prototype is the only honest answer.

3. **Show multiple variations to reduce anchoring bias**
   "When you show one prototype, people critique it. When you show three, people compare and contrast. Comparison produces dramatically better feedback than critique."
   -- *David Kossnick, VP of Product at Figma* ([source](https://www.figma.com/blog/))

   Single prototypes anchor stakeholders and users on one direction. Multiple variations unlock comparative judgment — users reveal preferences they cannot articulate in the abstract. Always test at least two variations, ideally three, so feedback becomes "I prefer A because..." rather than "I don't like this."

4. **Prototype for feasibility, usability, and value simultaneously**
   "Product teams must simultaneously address three risks: will the customer buy it (value), can the customer figure out how to use it (usability), and can we build it (feasibility). A well-designed prototype answers all three."
   -- *Marty Cagan, Partner at Silicon Valley Product Group* ([source](https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/))

   Do not treat prototyping as only a design exercise. The best prototype tests reveal whether the concept is technically achievable (feasibility), whether users can navigate it without instruction (usability), and whether they actually want it (value). Design your prototype and test plan to address all three risks.

5. **Compare and contrast to surface hidden assumptions**
   "The biggest risk in product development is anchoring on a single solution too early. Compare-and-contrast testing forces the team to articulate what differs between options, which surfaces the hidden assumptions baked into each one."
   -- *Teresa Torres, Author of Continuous Discovery Habits* ([source](https://www.producttalk.org/2021/08/opportunity-solution-trees/))

   The variation matrix exists to make assumptions visible. When you define what differs between Variation A and Variation B, you are making explicit the design decisions that would otherwise remain implicit. This is where the real learning happens — not in whether users prefer A or B, but in understanding which underlying assumption each choice tests.

6. **Iterate and change plans quickly**
   "The ability to iterate and change plans quickly is the single biggest advantage a product team can have. Long planning cycles are a liability. Shorter cycles with prototypes let you fail fast and learn fast."
   -- *MJ Felix, Product Lead at Notion* ([source](https://www.notion.so/blog/building-product))

   Prototype-driven validation compresses the learning cycle from months to days. Instead of spending six weeks writing a PRD, debating it for two weeks, then building for eight weeks before discovering the concept does not resonate — build a prototype in days, test it in a week, and know whether to proceed or pivot before committing engineering time.

7. **Kill early, kill cheaply**
   "The most valuable outcome of a prototype is a clear kill signal. A concept killed at the prototype stage costs days. The same concept killed after engineering implementation costs months. Make killing cheap and you make innovation possible."
   -- *Jake Knapp, Creator of the Design Sprint and author of Sprint* ([source](https://www.thesprintbook.com/))

   The build/kill decision is the most important artifact this skill produces. Prototype-driven validation exists to reduce the cost of killing bad ideas. If the prototype reveals that the concept does not solve the stated problem, does not resonate with users, or is technically infeasible — that is a win. Document the kill rationale and move on.

8. **Fidelity should match the question, not the ambition**
   "The biggest mistake teams make with prototypes is over-investing in fidelity. A paper sketch can answer 'does this flow make sense?' A coded prototype is needed for 'does this interaction feel right?' Match the fidelity to the question you need to answer."
   -- *Tom Chi, former Head of Experience at Google X* ([source](https://www.ted.com/talks/tom_chi_rapid_prototyping_google_glass))

   Not every prototype needs to be interactive or high-fidelity. A paper sketch tests information architecture. A clickable wireframe tests flow logic. A coded prototype tests interaction feel. A Wizard-of-Oz prototype tests value without building any technology. Choose the lowest fidelity that answers your most important question.

## Instructions

### Step 1: Write the Prototype Brief

Define what you are prototyping and why. Produce:

- **Problem statement:** The user problem this prototype addresses, stated without referencing a solution. Pull from `customer-discovery` output if available.
- **Key question:** The single most important question this prototype must answer (e.g., "Will users understand how to create their first project without guidance?").
- **Validation type:** Is this a **desirability** test (do they want it?), **usability** test (can they use it?), **feasibility** test (can we build it?), or **value** test (will they pay/switch for it?)?
- **Fidelity level:** Paper sketch, clickable wireframe, coded prototype, or Wizard-of-Oz. Justify the choice based on the key question.
- **Success criteria:** What specific evidence would make you proceed to a PRD? What would make you kill the concept?
- **Time box:** How many days to build the prototypes (recommend 2-5 days max).

**Artifact:** Prototype brief document (1 page) saved as `applied/prototype-brief-{concept}.md`.

If `context/products/` exists, reference current product capabilities to ensure prototypes build on or contrast with the existing experience. If prior `customer-discovery` output exists in `applied/`, pull the validated pain points.

### Step 2: Build the Variation Matrix

Define 2-3 prototype variations that test different assumptions. Produce a matrix:

| Dimension | Variation A | Variation B | Variation C (optional) |
|---|---|---|---|
| **Core concept** | [What this version does] | [What this version does] | [What this version does] |
| **Key assumption tested** | [What must be true for A to win] | [What must be true for B to win] | [What must be true for C to win] |
| **Interaction model** | [How the user interacts] | [How the user interacts] | [How the user interacts] |
| **Information hierarchy** | [What's prominent vs. secondary] | [What's prominent vs. secondary] | [What's prominent vs. secondary] |
| **Technical approach** | [How it could be built] | [How it could be built] | [How it could be built] |
| **Biggest risk** | [What could go wrong] | [What could go wrong] | [What could go wrong] |

Rules for good variations:
- Each variation must differ on at least one meaningful dimension (not just color or copy)
- At least one variation should challenge the team's default assumption
- Variations should be genuinely plausible — do not include a straw man
- If a prior `feature-prioritization` run flagged low-confidence items, use those as variation inputs

**Artifact:** Variation matrix table.

### Step 3: Design the Customer Test Plan

Define who tests what and how. Produce:

- **Participant profile:** Who should test (role, context, qualifying criteria). Minimum 5 participants per variation.
- **Recruitment source:** Where to find them (existing users, community, partner introductions). Reference `context/verticals/` for segment-specific channels.
- **Test format:** In-person, remote video, unmoderated (tool-based), or diary study. Justify the format based on fidelity level.
- **Task design:** 3-5 tasks that each participant attempts with the prototype. Tasks should be realistic scenarios, not feature demos. Each task must map to the key question from Step 1.
- **Observation protocol:** What to watch for beyond task completion — hesitation, confusion, delight, workarounds, questions asked, and unsolicited comments.
- **Measurement plan:**
  - **Quantitative:** Task success rate, time-on-task, error rate, preference ranking (if testing multiple variations)
  - **Qualitative:** Think-aloud observations, post-task interview questions (3-5 questions), overall preference and reasoning

**Artifact:** Customer test plan document with participant profile, task design, and measurement plan.

### Step 4: Synthesize Feedback

After testing, synthesize findings across all participants and variations. Produce:

- **Variation scorecard:** Rate each variation across the dimensions from Step 2, incorporating both quantitative results and qualitative themes.

| Dimension | Variation A | Variation B | Variation C |
|---|---|---|---|
| Task success rate | X% | X% | X% |
| Average time-on-task | Xm | Xm | Xm |
| User preference rank | #X | #X | #X |
| Key qualitative theme | [Theme] | [Theme] | [Theme] |

- **Surprise log:** What did users do or say that you did not expect? These are the highest-signal findings.
- **Quote bank:** 5-10 verbatim quotes indexed by participant, variation, and theme.
- **Assumption verdict:** For each assumption in the variation matrix, state: **Validated** (evidence supports it), **Invalidated** (evidence contradicts it), or **Inconclusive** (insufficient evidence).
- **Convergence opportunities:** Elements from different variations that could be combined into a stronger solution.

**Artifact:** Feedback synthesis report with scorecard, surprise log, quote bank, and assumption verdicts.

### Step 5: Make the Build/Kill Decision

Based on the synthesis, produce a clear recommendation:

- **Decision:** One of:
  - **Build** — Proceed to PRD. The prototype validated the core concept. Reference `writing-prds-for-ai` for the next step.
  - **Iterate** — Run another prototype round with specific changes. Define what must change and why.
  - **Pivot** — The concept failed but a related opportunity emerged from the testing. Define the new direction.
  - **Kill** — The concept does not solve the stated problem. Document the rationale for institutional memory.

- **Evidence summary:** The 3-5 most compelling data points supporting the decision.
- **Conditions for reversal:** What new information would change this decision?
- **Recommended next steps:**
  - If Build: What should the PRD include based on prototype learnings? What should the PRD explicitly exclude?
  - If Iterate: What changes to the prototype, test plan, or participant profile?
  - If Pivot: What is the new problem hypothesis?
  - If Kill: What did the team learn that applies to future concepts?

- **Stakeholder communication:** A 3-sentence summary suitable for sharing with executives. Reference `stakeholder-alignment` for alignment on contentious decisions.

**Artifact:** Build/kill decision document saved as `applied/prototype-decision-{concept}.md`.

## Diagnostic Questions

1. **How confident are you in the problem definition?** If above 80%, you might not need prototyping — go straight to a PRD. If below 50%, you might need `customer-discovery` first. Prototyping is most valuable in the 50-80% confidence range.

2. **Can you articulate what differs between two reasonable approaches?** If you can only imagine one solution, you are anchored. Force yourself to generate at least one alternative before prototyping — even if it feels inferior.

3. **What is the cheapest way to test your riskiest assumption?** If a paper sketch answers the question, do not build a coded prototype. If a conversation answers the question, do not build a prototype at all. Match fidelity to the question.

4. **Who will see the prototype results?** If the audience is the product team, low-fidelity is fine. If the audience includes executives who will make a funding decision, higher fidelity may be needed to communicate the concept effectively — but beware of confusing "looks polished" with "concept is validated."

5. **Is the team willing to kill this concept?** If the prototype is a formality and the team has already committed to building, the exercise is theater. Prototype-driven validation only works when the kill outcome is genuinely on the table.

6. **Do you have access to real users for testing?** Internal team members and stakeholders are not substitutes for real users. If you cannot recruit real users, the prototype results have a confidence ceiling. Adjust your build/kill criteria accordingly.

## Common Mistakes

1. **Prototyping when the problem is not yet validated**
   A prototype tests a solution, not a problem. If you have not validated that the problem exists and is painful enough to solve, no amount of prototyping will help. Run `customer-discovery` first, then prototype solutions to validated problems.

2. **Testing only one variation**
   Single-variation testing produces critique, not comparison. Users anchor on the one thing in front of them and nitpick details. Multiple variations unlock comparative judgment — "I prefer A because..." is dramatically more useful than "I don't like this button."

3. **Over-investing in prototype fidelity**
   High-fidelity prototypes feel productive but are expensive to build and emotionally expensive to kill. Teams that spend two weeks on a polished prototype are psychologically committed to building it regardless of test results. Keep the fidelity low enough that killing the concept is painless.

4. **Confusing user preference with product viability**
   Users may prefer Variation A in a test but never use it in practice. Preference data must be triangulated with behavioral signals (did they complete the task? how long did it take? did they ask for help?) and viability signals (can we build this? at what cost?).

5. **Skipping the kill decision**
   Many teams run prototypes, collect feedback, and then... just start building whatever seems popular without making an explicit decision. The build/kill decision document is not optional. Without it, the prototype was a user research exercise, not a validation gate.

6. **Testing with the wrong participants**
   Internal team members, friendly investors, and family members are not valid test participants. They have context, goodwill, and incentives that real users do not. Recruit participants who match the target user profile and have no prior relationship with the team.

## Context Integration

| Context Directory | How It Feeds This Skill |
|---|---|
| `context/products/` | **Step 1-2**: Grounds prototype variations in current product capabilities. Ensures prototypes build on or meaningfully diverge from the existing experience rather than reimagining from scratch. |
| `context/verticals/` | **Step 3**: Identifies segment-specific recruitment channels and qualifying criteria for test participants. Provides market context for interpreting prototype results. |
| `context/competitive/` | **Step 2**: Informs variation design by incorporating competitive approaches. If a competitor solved this differently, test their approach as one variation. |
| `context/company/` | **Step 1, 5**: Calibrates prototype fidelity and scope based on team size and resources. Informs the build/kill decision based on what the team can realistically execute. |
| `context/founders/` | **Step 5**: Surfaces leadership priorities and risk tolerance for the build/kill decision. Founder-led teams may need higher-fidelity prototypes to secure internal buy-in. |
| `context/signals/` | **Step 2, 4**: Supplements prototype findings with community sentiment and ecosystem signals. Check collection timestamps for freshness. |
