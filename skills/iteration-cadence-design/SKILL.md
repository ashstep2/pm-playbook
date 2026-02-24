---
name: iteration-cadence-design
description: "Help users design their team's operating rhythm — producing cadence architectures, weekly PM calendars, ritual designs, decision rhythms, and adaptation triggers that replace rigid quarterly planning with shorter, learning-oriented cycles."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Iteration Cadence Design

Produces a cadence architecture, weekly PM operating calendar, ritual design document, decision rhythm framework, and adaptation triggers — the operating system for how the team works week-to-week. Reach for this skill when planning cycles feel too long, when the team ships but does not learn, or when meetings consume time without producing decisions.

## Core Principles

1. **Iterate and change plans quickly**
   "The ability to iterate and change plans quickly is the single biggest advantage a product team can have. The teams that learn fastest win. Long planning cycles are a liability — they embed assumptions that become stale before the cycle ends."
   -- *MJ Felix, Product Lead at Notion* ([source](https://www.notion.so/blog/building-product))

   The default planning cadence in most organizations (quarterly OKRs, 2-week sprints) was designed for a world with slower feedback loops. In a world where you can prototype in days, test in a week, and ship in two weeks, 12-week planning cycles are a competitive disadvantage. Design the cadence around the speed of learning, not the speed of building.

2. **Shape the work, then build it in cycles**
   "We work in six-week cycles with a two-week cooldown. During a cycle, teams have full autonomy. During cooldown, they fix bugs, explore ideas, and prepare for the next cycle. The fixed cycle length creates rhythm; the cooldown prevents burnout."
   -- *Ryan Singer, Creator of Shape Up (Basecamp)* ([source](https://basecamp.com/shapeup))

   Fixed-length cycles with built-in slack create a sustainable rhythm. The cooldown is not wasted time — it is where teams pay down technical debt, explore unstructured ideas, and recover. Teams without cooldown accumulate debt and burn out. Designing the cadence means designing the breathing room, not just the work.

3. **Planning is guessing**
   "Plans are nothing; planning is everything. The further out you plan, the more wrong you will be. Accept this and design a system that replans frequently rather than one that pretends the long-range plan is accurate."
   -- *Jason Fried, Co-founder of Basecamp* ([source](https://basecamp.com/books/rework))

   Long-range planning feels productive but is mostly fiction. A detailed 6-month plan is indistinguishable from guessing. Design the cadence so that replanning is cheap and frequent. The weekly review is the most important meeting — not because it produces plans, but because it corrects them.

4. **The purpose of the sprint is to learn**
   "The goal of the sprint is not to ship features — it is to learn whether the features you shipped were the right ones. If the team is not learning, the sprint is just a work container with arbitrary deadlines."
   -- *Marty Cagan, Partner at Silicon Valley Product Group* ([source](https://www.svpg.com/empowered-product-teams/))

   Every cycle must end with a learning review, not just a demo. The question is not "did we finish what we planned?" but "what did we learn that changes what we plan next?" If the answer is consistently "nothing," the cadence is producing output without insight.

5. **Kill meetings that do not produce artifacts or decisions**
   "Every meeting should either produce a decision, an artifact, or be cancelled. Status meetings are the worst offender — they exist because the team lacks a shared dashboard, not because they need synchronous time."
   -- *Adapted from Jeff Bezos' meeting principles at Amazon* ([source](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders))

   The ritual design must include kill criteria for every recurring meeting. If a meeting consistently fails to produce its intended artifact or decision, it should be cancelled or redesigned. Most teams have 30-50% more recurring meetings than they need.

6. **Make decisions at the right cadence, not at the same cadence**
   "Not every decision needs the same decision-making process. Reversible decisions should be made quickly and locally. Irreversible decisions deserve more deliberation. The mistake is treating all decisions the same."
   -- *Jeff Bezos, Founder of Amazon (Type 1 vs. Type 2 decisions)* ([source](https://www.aboutamazon.com/about-us/leadership-principles))

   The decision rhythm must distinguish between decisions that need to be made weekly (what to work on next), per-cycle (what to commit to), and quarterly (where to invest). Applying the same process to all decisions either slows the team (over-deliberating trivial choices) or creates risk (under-deliberating consequential ones).

7. **Adaptation is a feature, not a failure**
   "The best teams treat changing the plan as a sign of learning, not a sign of failure. If you never change the plan, you are either incredibly prescient or dangerously stubborn."
   -- *Henrik Kniberg, Agile/Lean coach and creator of Spotify's Squad model* ([source](https://blog.crisp.se/2016/01/25/henrikkniberg))

   The cadence must include explicit adaptation triggers — conditions under which the team changes the plan mid-cycle. Teams without adaptation triggers face a false choice: follow the plan (even when it is wrong) or abandon the process (and lose the benefits of structured cadence). Design the third option: structured mid-cycle adaptation with clear criteria.

8. **Protect maker time from manager time**
   "A single meeting can blow a whole afternoon, by breaking it into two pieces each too small to do anything hard in. The manager's schedule works in 30-minute blocks. The maker's schedule works in half-day blocks. A cadence that respects both is the PM's responsibility to design."
   -- *Paul Graham, Co-founder of Y Combinator* ([source](https://paulgraham.com/makersschedule.html))

   The weekly operating calendar must protect contiguous blocks for deep work. Meetings should cluster on specific days or half-days, leaving other blocks meeting-free. The PM's calendar is the team's cadence — if the PM's calendar is fragmented, the team's work will be too.

## Instructions

### Step 1: Assess Current Cadence and Design the Cadence Architecture

Evaluate the team's current operating rhythm and design the target cadence. Produce:

- **Current state audit:** What is the current cycle length? How many recurring meetings exist? When was the last time the cadence was deliberately designed (vs. evolved by accumulation)?
- **Cadence architecture recommendation:**

| Factor | Assessment | Implication |
|---|---|---|
| **Team size** | [N people] | Smaller teams → shorter cycles (1-2 weeks). Larger teams → longer cycles (4-6 weeks) with sub-team sprints. |
| **Uncertainty level** | High / Medium / Low | High uncertainty → shorter cycles with more learning reviews. Low uncertainty → longer cycles with more execution focus. |
| **Product maturity** | Pre-PMF / Growth / Mature | Pre-PMF → 1-2 week cycles (maximize learning). Growth → 4-6 week cycles (balance learning and shipping). Mature → 6-8 week cycles (optimize execution). |
| **External dependencies** | [List] | External dependencies (partner launches, regulatory deadlines) may require fixed milestones within flexible cycles. |
| **Feedback loop speed** | Days / Weeks / Months | How fast can you get signal from users? Cycle length should be ≥ feedback loop speed. |

- **Recommended cycle length:** [N weeks] with rationale. Include cooldown/buffer time (recommend 15-20% of cycle length).
- **Cycle structure:** What happens in weeks 1, 2, ... N? (e.g., Week 1: scope and commit. Weeks 2-4: build. Week 5: test and learn. Week 6: cooldown.)

Reference `context/company/` for team size and stage. Reference `stakeholder-alignment` output for existing coordination requirements.

**Artifact:** Cadence architecture document with current state audit and recommended cycle structure.

### Step 2: Design the Weekly PM Operating Calendar

Produce a weekly calendar template showing how PM time is allocated. The calendar should protect maker time and cluster meetings.

| Day | Morning (9-12) | Afternoon (1-5) |
|---|---|---|
| **Monday** | [Activity] | [Activity] |
| **Tuesday** | [Activity] | [Activity] |
| **Wednesday** | [Activity] | [Activity] |
| **Thursday** | [Activity] | [Activity] |
| **Friday** | [Activity] | [Activity] |

Design principles:
- **Meeting-free blocks:** At least 2 half-days per week with zero meetings (protect deep work time).
- **Meeting clusters:** Group meetings on 2-3 days to minimize context switching.
- **External vs. internal:** Separate customer/external meetings from internal coordination.
- **Recurring vs. ad hoc:** Recurring meetings get fixed slots; ad hoc meetings fill remaining availability.

Include specific time allocations:
- **Customer time:** Minimum 2-3 hours/week talking to users (discovery, feedback, support listening).
- **Strategy time:** 2-3 hours/week for roadmap thinking, competitive analysis, and narrative work.
- **Coordination time:** 3-5 hours/week for team syncs, stakeholder updates, and 1:1s.
- **Deep work:** 4-6 hours/week for writing specs, analyzing data, and designing experiments.

**Artifact:** Weekly PM operating calendar template.

### Step 3: Design the Rituals

For each recurring meeting/ritual, produce a ritual design card:

| Field | Definition |
|---|---|
| **Name** | Short, memorable name (not "Weekly Sync #3") |
| **Purpose** | One sentence: what this ritual exists to produce |
| **Cadence** | How often (weekly, per-cycle, quarterly) |
| **Duration** | Maximum time. If it regularly exceeds this, the ritual needs redesign. |
| **Attendees** | Who must attend vs. who is optional |
| **Input artifact** | What must be prepared before the meeting starts |
| **Output artifact** | What must be produced by the end of the meeting |
| **Facilitator** | Who runs it |
| **Kill criteria** | Under what conditions should this ritual be cancelled or redesigned |

Recommended minimum ritual set:

1. **Weekly Check-in** (15-30 min): Review metrics dashboard, surface blockers, adjust this week's priorities. Input: updated dashboard. Output: adjusted weekly priorities.
2. **Cycle Planning** (1-2 hours, per cycle): Commit to the cycle's scope. Input: prioritized backlog. Output: cycle commitment document.
3. **Cycle Review** (1 hour, per cycle): Demo what shipped, review metrics against predictions, extract learnings. Input: shipped work + metrics. Output: learning log entry.
4. **Customer Insight Share** (30 min, weekly or biweekly): Share raw customer feedback and discovery findings. Input: interview notes or feedback summary. Output: updated assumption tracker.
5. **Quarterly Strategy Review** (2-4 hours): Revisit product vision, roadmap narrative, and portfolio priorities. Input: prior quarter metrics + updated competitive landscape. Output: updated strategy narrative.

For each ritual, apply the kill criteria: if the output artifact is not produced for 3 consecutive instances, the ritual is failing and must be redesigned or cancelled.

**Artifact:** Ritual design document with cards for each recurring meeting.

### Step 4: Define the Decision Rhythm

Map which decisions happen at which cadence. Produce:

| Decision Type | Cadence | Who Decides | Input Required | Examples |
|---|---|---|---|---|
| **Tactical** | Weekly or ad hoc | Individual contributor or PM | Own judgment | Bug priority, copy changes, minor UX tweaks |
| **Cycle-level** | Per cycle | PM with team input | Prioritized backlog, cycle goals | Feature scope, experiment design, build vs. validate |
| **Strategic** | Quarterly | PM + leadership | Strategy review, competitive analysis, metrics | Roadmap direction, pricing changes, market expansion |
| **Structural** | Ad hoc (trigger-based) | Leadership | Significant new information | Team structure, platform bets, partnerships |

For each row, reference the relevant ritual from Step 3 where the decision is made. Ensure every decision type has a clear forum — if a decision has no natural home, it will either be made in hallways or not made at all.

Reference `stakeholder-alignment` output for RACI and decision-making framework. Reference `feature-prioritization` for the prioritized backlog that feeds cycle-level decisions.

**Artifact:** Decision rhythm matrix.

### Step 5: Define Adaptation Triggers

Specify when the team should deviate from the current cycle plan. Produce:

| Trigger | Signal | Response | Who Initiates |
|---|---|---|---|
| **User emergency** | Spike in error reports, support tickets, or churn beyond threshold | Pause current cycle, triage and fix. Resume cycle with adjusted scope. | On-call engineer or PM |
| **Competitive move** | Competitor launches feature in your core area | Assess impact (1 day). If significant, adjust current or next cycle scope. Do NOT panic-ship. | PM |
| **Experiment result** | Experiment produces strong signal (positive or negative) mid-cycle | If positive: accelerate. If negative: stop work on related features. | PM |
| **Prototype kill** | Prototype validation (from `prototype-driven-validation`) produces a kill decision | Remove related items from current/next cycle. Redirect resources. | PM |
| **Capacity change** | Team member joins/leaves, key dependency slips | Rescope current cycle within 48 hours. Do not try to absorb the change without adjusting scope. | PM or engineering lead |
| **Strategic shift** | Leadership changes direction, funding changes, market shift | Trigger ad hoc strategy review. Suspend current cycle if direction fundamentally changes. | Leadership |

For each trigger, specify:
- **Detection mechanism:** How the team notices (automated alerts, regular metrics review, stakeholder communication)
- **Response time:** How quickly the team must act (hours, days, or next cycle)
- **Scope of change:** What changes (current cycle only, next cycle, or full re-plan)

Also define when to **change the cadence itself:**
- If the team consistently finishes cycles early → shorten cycles
- If the team consistently carries over work → lengthen cycles or reduce scope per cycle
- If learning reviews produce no new insights → something is wrong with feedback loops, not the cycle length

**Artifact:** Adaptation trigger matrix saved as part of `applied/cadence-design-{team}.md`.

### Step 6: Compile the Cadence Design Document

Assemble all artifacts into a single operating rhythm document:

1. Cadence Architecture (from Step 1)
2. Weekly PM Operating Calendar (from Step 2)
3. Ritual Design (from Step 3)
4. Decision Rhythm (from Step 4)
5. Adaptation Triggers (from Step 5)

Add an implementation plan: how to transition from the current cadence to the new one. Recommend a 2-cycle trial period where the team runs the new cadence and evaluates whether it improves learning velocity and team satisfaction.

**Artifact:** Complete cadence design document saved as `applied/cadence-design-{team}.md`.

## Diagnostic Questions

1. **When was the last time you changed your planning process?** If the answer is "never" or "years ago," the cadence is likely a legacy of conditions that no longer apply. Cadence should be redesigned when team size, product maturity, or market conditions change significantly.

2. **How many recurring meetings does the team have per week?** Count them. If the total exceeds 8-10 hours per person per week, the cadence is meeting-heavy. Cut meetings that do not produce artifacts or decisions.

3. **How often does the team change plans mid-cycle?** If never: the team may be too rigid. If constantly: the cycles may be too long or the scope too ambitious. The adaptation trigger framework should make mid-cycle changes structured, not chaotic.

4. **Do engineers have at least 2 contiguous half-days per week without meetings?** If not, the cadence is destroying maker time. Redesign the calendar before touching anything else.

5. **Can the team describe what they learned last cycle?** If the answer is vague or focused on output ("we shipped X features"), the cadence lacks learning rituals. Add a cycle review focused on insights, not demos.

6. **How long does it take from "idea" to "user feedback?"** This is the true cycle time. If it is longer than 4-6 weeks, the cadence may need to be compressed or prototyping should be introduced to shorten the feedback loop.

## Common Mistakes

1. **Designing the cadence around the PM's preferences, not the team's needs**
   PMs who love planning create heavy planning rituals. PMs who love shipping create minimal coordination. The cadence should match the team's needs: team size, uncertainty level, and feedback loop speed — not the PM's personality.

2. **Adding meetings without removing meetings**
   Every new ritual should replace or consolidate an existing one. Teams that only add meetings will eventually spend all their time in meetings and none on work. Apply the kill criteria from Step 3 ruthlessly.

3. **Making cycles too short for meaningful work**
   One-week cycles work for small teams with low-complexity work. For teams building complex features, cycles under 2 weeks create thrashing — the team spends more time planning and context-switching than building. Match cycle length to the minimum meaningful unit of work.

4. **Treating cooldown as optional**
   When deadlines pressure the team, cooldown is the first thing cut. This is a false economy — skipped cooldown accumulates as technical debt, team burnout, and unexplored ideas. Protect cooldown as a non-negotiable part of the cadence.

5. **Applying one cadence to all workstreams**
   Maintenance work, feature development, and research exploration have different rhythms. The cadence architecture should allow different workstreams to operate at different speeds, with clear synchronization points.

## Context Integration

| Context Directory | How It Feeds This Skill |
|---|---|
| `context/company/` | **Step 1-2**: Team size, stage, and organizational structure determine cycle length, ritual complexity, and calendar design. A 5-person startup needs different rituals than a 50-person growth-stage company. |
| `context/products/` | **Step 1, 5**: Product maturity and complexity inform cycle length. Products with longer feedback loops need longer cycles. Products with fast feedback loops can use shorter cycles. |
| `context/competitive/` | **Step 5**: Competitive pressure may require tighter adaptation triggers and shorter response times. |
| `context/founders/` | **Step 3-4**: Leadership communication preferences shape ritual design and decision rhythm. Some leaders want weekly briefings; others prefer async updates. |
