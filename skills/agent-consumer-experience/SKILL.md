---
name: agent-consumer-experience
description: "Help users design products for end-user personal agents — mapping how consumer AI assistants interact with your product on behalf of humans — producing agent interaction models, consent frameworks, preference APIs, and agent-mediated UX patterns."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Agent Consumer Experience

Produces a design framework for products consumed by end-user personal agents — documenting how AI assistants will book, purchase, manage, compare, and interact with your product on behalf of human users. Delivers agent interaction models, consent and delegation frameworks, preference APIs, and agent-mediated UX patterns. Reach for this skill when consumer-facing products need to support personal AI agents (booking assistants, shopping agents, account managers), or when your product's UI-first design is being bypassed by agent workflows.

## Core Principles

1. **The user's agent is the new user interface**
   "Consumers will not open your app — their agent will. Booking, shopping, managing subscriptions, comparing alternatives. The interface between the human and your product is increasingly an AI agent, not a screen."
   — *Agent-mediated consumer interaction analysis* ([source](https://www.anthropic.com/research/building-effective-agents))

2. **Design for delegation, not direct interaction**
   "When a user tells their agent 'book me a restaurant for Saturday,' the agent needs your product to support: availability queries, preference matching, reservation creation, confirmation, and cancellation — all without the user ever seeing your interface."
   — *Agent delegation patterns for consumer services* ([source](https://docs.anthropic.com/en/docs/agents-and-tools/mcp))

3. **Consent must be explicit and granular**
   "When an agent acts on behalf of a human, the human must have explicitly authorized what the agent can do. 'Book anything under $50' is a different consent scope than 'browse menus.' Agent consent frameworks must be tiered, revocable, and auditable."
   — *Agent authorization and consent design* ([source](https://modelcontextprotocol.io/docs/concepts/tools))

4. **Preferences are structured data, not free text**
   "A user saying 'I like quiet restaurants' is useless to an agent unless it can be translated to structured preferences: `{ "noise_level": "low", "seating": "booth_preferred" }`. Products that expose structured preference APIs enable better agent matching than products that store preferences as unstructured notes."
   — *Preference modeling for agent-mediated experiences* ([source](https://schema.org/))

5. **Agents need pricing certainty, not pricing complexity**
   "Dynamic pricing, hidden fees, and 'starting at' pricing are hostile to agents. An agent needs to tell the user exactly what something costs before the user approves. If your pricing requires navigating a complex UI to reveal the real cost, agents will favor transparent competitors."
   — *Transparent pricing for agent-mediated transactions* ([source](https://openviewpartners.com/usage-based-pricing/))

6. **The agent-mediated experience must be at least as good as the direct experience**
   "If using your product through an agent is slower, more limited, or more error-prone than using it directly, agents will route users to competitors with better agent support. Agent-mediated UX is not a second-class channel."
   — *Agent experience parity principle* ([source](https://www.nngroup.com/articles/omnichannel-consistency/))

7. **Human-in-the-loop is a feature, not a failure**
   "For high-stakes actions (purchases over a threshold, medical appointments, financial transactions), the agent should escalate to the human for confirmation. This is not a broken agent journey — it is good design. The consent framework defines which actions require human approval."
   — *Human-agent handoff design, Anthropic* ([source](https://www.anthropic.com/research/building-effective-agents))

## Instructions

### Step 1: Map Agent-Mediated Consumer Interactions

Identify every interaction a personal agent would have with your product on behalf of a user.

| Interaction Category | Examples | Current Support | Agent Readiness |
|---------------------|----------|-----------------|-----------------|
| **Discovery/Search** | "Find Italian restaurants near me" | | |
| **Comparison** | "Compare plans and show me the cheapest" | | |
| **Booking/Reservation** | "Book a table for 2 on Saturday at 7pm" | | |
| **Purchase** | "Order my usual, deliver by 6pm" | | |
| **Account management** | "Cancel my subscription" "Update my address" | | |
| **Status checking** | "When does my order arrive?" | | |
| **Preference setting** | "I prefer window seats" "No peanuts" | | |
| **Complaint/Support** | "My last order was wrong, get a refund" | | |

For each category, document: what the agent needs from your product (data, actions, confirmations), what currently works programmatically, and what requires human UI interaction.

**Artifact produced:** Agent Interaction Map.

### Step 2: Design the Consent and Delegation Framework

Define what agents are authorized to do on behalf of users, with tiered permissions.

**Consent tiers:**

| Tier | Agent Can... | Requires Human Approval? | Examples |
|------|-------------|------------------------|---------|
| **Read-only** | View availability, prices, account details | No | Browse menu, check order status |
| **Low-stakes action** | Save preferences, add to wishlist, set alerts | No | Save dietary preferences, set price alert |
| **Medium-stakes action** | Make reservations, place orders under $X | User-set threshold | Book restaurant, order groceries under $50 |
| **High-stakes action** | Large purchases, cancellations, data deletion | Always yes | Annual subscription, cancel account |
| **Sensitive data access** | Health records, financial statements | Always yes + re-auth | View medical history, download tax docs |

**Framework requirements:**
- User sets per-tier thresholds (e.g., "$50 auto-approve, above $50 ask me")
- All agent actions logged with timestamp, action, and consent tier
- User can revoke agent access at any time, with immediate effect
- Consent is per-agent (user may trust Agent A with purchases but not Agent B)

**Artifact produced:** Consent and Delegation Framework with tier definitions and configuration specification.

### Step 3: Design the Preference API

Structured preferences enable agents to personalize interactions without repeated user input.

**Preference schema design:**

```
GET /users/{user_id}/preferences
Returns: { "preferences": { "category": { "key": "value", ... } } }

PUT /users/{user_id}/preferences/{category}
Body: { "key": "value", ... }
Returns: Updated preference object

Available categories:
- dietary: { "allergies": [...], "restrictions": [...], "favorites": [...] }
- scheduling: { "preferred_times": [...], "blackout_dates": [...], "timezone": "..." }
- communication: { "channel": "sms|email|push", "frequency": "..." }
- spending: { "auto_approve_limit": 50, "currency": "USD", "budget_period": "monthly" }
- product_specific: { ... } (varies by product category)
```

**Key principles:**
- Preferences are structured, not free text
- Agents can read and write preferences through the same API
- Preference changes are versioned (agent can see when a preference was set and by whom)
- Defaults are sensible — missing preferences do not break agent workflows

**Artifact produced:** Preference API Specification.

### Step 4: Design Agent-Mediated UX Patterns

For each interaction from Step 1, design the agent-mediated flow with confirmation points.

**Pattern: Search → Select → Confirm → Execute**

```
1. Agent queries your API with structured search (parameters, not free text)
2. Your API returns ranked results with structured metadata
3. Agent presents options to user (in agent's UI, not yours)
4. User selects or refines
5. Agent submits action to your API
6. Your API returns confirmation with details
7. Agent presents confirmation to user
8. User approves (if consent tier requires it)
9. Agent executes
10. Your API returns success with receipt/confirmation ID
```

**Design each flow to be:**
- Stateless (agent can abandon and restart without cleanup)
- Resumable (agent can pick up from any step)
- Cancelable (agent can cancel at any point before final execution)
- Confirmable (your API returns a preview before executing mutations)

**Artifact produced:** Agent-Mediated UX Flow Diagrams (one per interaction category).

### Step 5: Define Agent-Specific Metrics

Measure the quality of agent-mediated consumer experiences.

| Metric | What It Measures | Target |
|--------|-----------------|--------|
| **Agent task completion rate** | % of agent-initiated tasks completed successfully | >90% |
| **Agent-to-human escalation rate** | % of tasks requiring human intervention (excluding consent-required) | <10% |
| **Time-to-task-completion (agent)** | Time from agent request to completion | <30 seconds |
| **Preference match accuracy** | % of agent selections matching user preferences | >85% |
| **Agent-mediated satisfaction** | User satisfaction with agent-completed tasks vs. direct | Parity or better |
| **Consent override rate** | % of agent recommendations overridden by users | <15% (high = poor matching) |

**Artifact produced:** Agent Consumer Metrics Dashboard Specification.

### Step 6: Compile the Agent Consumer Experience Design

Assemble all artifacts:

1. Executive Summary (the shift to agent-mediated consumer interactions and your product's readiness)
2. Agent Interaction Map (Step 1)
3. Consent and Delegation Framework (Step 2)
4. Preference API Specification (Step 3)
5. Agent-Mediated UX Flow Diagrams (Step 4)
6. Agent Consumer Metrics (Step 5)
7. Implementation roadmap (P0-P3 with timeline)
8. Recommended immediate actions (top 3 things to ship)

**Artifact produced:** Agent Consumer Experience Design saved as `applied/agent-consumer-{product}.md`.

## Diagnostic Questions

1. **Can a personal agent complete the most common user task with your product without opening your app?** If not, you are forcing a channel switch that agents will avoid.

2. **What happens when two different agents try to act on the same user account simultaneously?** If you do not handle concurrent agent access, you will get race conditions (double bookings, conflicting updates).

3. **Can a user revoke agent access instantly?** If revoking access takes time or requires contacting support, you have a consent gap.

4. **Are user preferences stored as structured data or free text?** Free-text preferences cannot be matched by agents. Structured preferences enable programmatic personalization.

5. **Does your product show the real, final price before the agent commits?** Hidden fees, dynamic pricing surcharges, and "price available at checkout" patterns are hostile to agent-mediated transactions.

6. **What is the smallest useful action an agent can take with your product?** If the minimum viable interaction is a full purchase, you lose all the browse/compare/save use cases that build toward conversion.

## Common Mistakes

1. **Requiring the user to interact with your UI**
   If any step of the agent-mediated journey forces the user to open your app, click a button, or fill a form, the agent journey is broken. Every interaction must be completable through APIs.

2. **No consent framework**
   Agents acting on behalf of users without clear authorization is a liability and a bad experience. Ship consent tiers before shipping agent access. Users must control what agents can do.

3. **Unstructured preferences**
   Storing user preferences as free-text notes ("likes Italian food") instead of structured data (`{ "cuisine_preferences": ["italian"] }`) makes agent matching impossible at scale.

4. **Ignoring concurrent agent access**
   Users may have multiple agents (work agent, personal agent, shopping agent) all accessing the same account. Without concurrency handling, you get race conditions and conflicting actions.

5. **Treating agent-mediated transactions as second-class**
   If agent-mediated bookings get worse availability, higher prices, or fewer features than direct bookings, agents will route users to competitors. Agent parity is a minimum requirement.

## Context Integration

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 3, 4 | Product features, user flows, and current API surface. Essential for mapping agent interactions. |
| `context/competitive/` | Steps 1, 4 | Competitor agent support levels. Which competitors already support personal agents? |
| `context/verticals/` | Steps 1, 2 | Industry-specific consent requirements (healthcare, finance have regulatory constraints on agent delegation). |
| `context/company/` | Step 6 | Engineering capacity and product roadmap alignment. |
| `context/signals/` | Steps 1, 5 | Consumer sentiment about agent-mediated experiences. [SIGNAL] tagged. |

If no `context/` directory is present, the skill will ask for:
1. Product name and primary consumer use case
2. Most common user tasks (what do users do most frequently?)
3. Current API/programmatic access points
4. Whether personal agents (Siri, Google Assistant, Claude) are already attempting to interact with your product
