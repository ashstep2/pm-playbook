---
name: agent-journey-mapping
description: "Help users design agent journeys — mapping how AI agents discover, authenticate, use, and recover from errors with a product — producing journey maps, I/O contracts, failure mode analysis, and agent experience optimization roadmap."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Agent Journey Mapping

Produces structured agent journey maps for a product — documenting how AI agents discover, evaluate, authenticate, execute tasks, handle errors, and chain workflows — delivering I/O contracts, failure mode analysis, and an agent experience optimization roadmap. Reach for this skill when designing a new agent-accessible product, when agent adoption is lower than expected, or when agents are failing silently in production.

## Core Principles

1. **PMs must design agent journeys, not just user journeys**
   "This shift forces PMs to think beyond user journeys — you now have to design agent journeys. What inputs are passed? What outputs are guaranteed?"
   — *Agent-first product design analysis* ([source](https://docs.anthropic.com/en/docs/agents-and-tools/mcp))

2. **Agents have no patience and infinite precision**
   "A human user will tolerate ambiguity, experiment with an interface, and read between the lines. An agent does none of these things. It follows the contract exactly. If the contract is ambiguous, the agent fails."
   — *Anthropic, Building effective agents* ([source](https://www.anthropic.com/research/building-effective-agents))

3. **The agent journey starts with discovery, not with the first API call**
   "An agent's journey begins when it encounters your tool description in a registry, a tool list, or a system prompt. If your description does not clearly convey what the tool does and when to use it, the journey ends before it starts."
   — *MCP tool discovery patterns* ([source](https://modelcontextprotocol.io/docs/concepts/tools))

4. **Guaranteed output shapes are more important than flexible interfaces**
   "Agents cannot handle surprise response formats. A response that is sometimes JSON and sometimes plain text, sometimes paginated and sometimes not, will break agent workflows. Consistency of output shape is non-negotiable."
   — *API design for programmatic consumers, Stripe Engineering* ([source](https://stripe.com/docs/api))

5. **Agent error recovery is deterministic, not creative**
   "When a human hits an error, they adapt — try a different approach, search for help, ask a colleague. When an agent hits an error, it follows a decision tree: retry, try alternative, escalate to human, or fail. Design your error responses to feed that decision tree."
   — *Error handling patterns for AI agents* ([source](https://www.anthropic.com/research/building-effective-agents))

6. **Multi-step agent workflows require explicit state contracts**
   "If an agent must call Tool A before Tool B, that dependency must be explicit in the tool descriptions or enforced by the API. Implicit ordering assumptions are the leading cause of agent workflow failures."
   — *Agent orchestration design patterns* ([source](https://langchain-ai.github.io/langgraph/))

7. **The best agent journeys are boring**
   "The ideal agent interaction is entirely predictable. No surprises, no creative interpretation, no edge cases. The agent calls the tool, gets the expected response, and moves on. Boring is the goal."
   — *Reliability engineering applied to agent workflows* ([source](https://www.anthropic.com/research/building-effective-agents))

## Instructions

### Step 1: Identify Agent Personas

Not all agents are the same. Identify the 2-4 agent types most likely to interact with your product.

**Common agent personas:**

| Agent Type | Behavior Pattern | Example |
|-----------|-----------------|---------|
| **Coding agent** | Installs tools, reads docs, writes integration code | Claude Code, Cursor, GitHub Copilot Workspace |
| **Workflow orchestrator** | Chains multiple tools in a pipeline, needs reliable I/O | n8n, Zapier AI, custom LangGraph agents |
| **Research agent** | Reads data, compares options, synthesizes reports | Perplexity, custom research agents |
| **Personal assistant** | Acts on behalf of a human user, needs approval workflows | Claude with MCP, ChatGPT with plugins |
| **Enterprise agent** | Operates within compliance boundaries, needs audit trails | Custom enterprise agents with governance |

For each persona, document: what they are trying to accomplish with your product, what tools they need, and what constraints they operate under (context window limits, permission boundaries, latency requirements).

**Artifact produced:** Agent Persona Profiles (2-4 profiles with goals, tool needs, and constraints).

### Step 2: Map the Agent Journey Stages

For each agent persona, map the full journey through your product. Document every stage, decision point, and potential failure.

| Stage | What Happens | What the Agent Needs | Common Failure Points |
|-------|-------------|---------------------|----------------------|
| **Discovery** | Agent finds your tool in a registry, tool list, or system prompt | Clear tool description with when-to-use guidance | Vague description → agent skips tool |
| **Evaluation** | Agent decides whether your tool is the right one for the current task | Unambiguous description distinguishing your tool from alternatives | Overlapping descriptions → wrong tool selected |
| **Authentication** | Agent obtains and provides credentials | Token-based auth, no browser flows, scoped permissions | OAuth popup → complete failure |
| **First call** | Agent makes its first request to your tool | Clear parameter schemas, sensible defaults, copy-paste examples | Missing required params → cryptic error |
| **Task completion** | Agent chains multiple calls to accomplish a goal | Consistent response shapes, explicit ordering, state management | Inconsistent pagination → data loss |
| **Error recovery** | Agent encounters an error and attempts to recover | Structured error with code, message, and remediation hint | Generic "error" → retry loop |
| **Workflow chaining** | Agent passes your output to another tool | Structured output in standard formats (JSON, markdown) | Unparseable output → chain breaks |

For each stage, record: the happy path, 2-3 failure modes, and the agent's recovery options.

**Artifact produced:** Agent Journey Map (table per persona with all stages documented).

### Step 3: Define I/O Contracts

For every tool or endpoint an agent interacts with, define the exact input/output contract.

**For each tool, document:**

```
Tool: [name]
Purpose: [one sentence — when should an agent call this?]

Input contract:
  Required: [param: type — description]
  Optional: [param: type — default — description]
  Constraints: [max values, format requirements, mutual exclusions]

Output contract:
  Success: [exact JSON shape with field types]
  Pagination: [cursor-based / offset-based / none — next page mechanism]
  Empty result: [what shape when no data matches?]

Error contract:
  [error_code]: [when it occurs] → [agent should: retry / fix input / escalate]

Side effects: [what state changes? is it idempotent?]
Dependencies: [must Tool X be called first? does output feed Tool Y?]
```

**Artifact produced:** I/O Contract Registry (one contract per tool, collected in a single reference document).

### Step 4: Analyze Failure Modes

For each journey stage from Step 2, enumerate specific failure modes and design the recovery path.

| Failure Mode | Stage | Severity | Detection | Agent Recovery Path |
|-------------|-------|----------|-----------|-------------------|
| Tool not found in registry | Discovery | Critical | Tool list returns empty | Try alternative tool name, fall back to API |
| Wrong tool selected | Evaluation | High | Unexpected response shape | Check response, retry with correct tool |
| Auth token expired | Authentication | High | 401 response | Refresh token, retry once |
| Rate limited | Task completion | Medium | 429 + Retry-After header | Wait specified duration, retry |
| Partial data returned | Task completion | Medium | Pagination token present | Follow pagination to completion |
| Malformed output | Workflow chaining | High | JSON parse failure | Request raw format, retry |

For each failure mode, specify: can the agent recover autonomously, or must it escalate to a human?

**Artifact produced:** Failure Mode Registry (table with all identified failures, severity, and recovery paths).

### Step 5: Design Agent-Specific Metrics

Define metrics that measure agent journey health — distinct from human user metrics.

| Metric | What It Measures | Target | Warning Threshold |
|--------|-----------------|--------|-------------------|
| **Agent time-to-first-successful-call** | Seconds from tool discovery to first 200 response | <5 seconds | >15 seconds |
| **Tool selection accuracy** | % of times agents pick the right tool for a task | >90% | <75% |
| **Error recovery rate** | % of agent errors that resolve without human escalation | >80% | <60% |
| **Workflow completion rate** | % of multi-step agent workflows that complete successfully | >85% | <70% |
| **Output parseability** | % of responses that downstream tools consume without error | >99% | <95% |
| **Retry rate** | Average retries per successful operation | <1.2 | >2.0 |

**Artifact produced:** Agent Journey Metrics Dashboard Specification.

### Step 6: Build the Agent Experience Optimization Roadmap

From all findings, produce a prioritized roadmap to improve agent journeys.

| Priority | Improvement | Journey Stage Affected | Expected Impact |
|----------|------------|----------------------|-----------------|
| **P0** | [Critical fixes — agents cannot complete basic tasks] | | |
| **P1** | [High-impact — agents succeed but with friction] | | |
| **P2** | [Medium-impact — agent experience is suboptimal] | | |
| **P3** | [Nice-to-have — polish and optimization] | | |

**Artifact produced:** Agent Experience Optimization Roadmap saved as part of the complete report at `applied/agent-journey-{product}.md`.

## Diagnostic Questions

1. **Have you ever watched an agent try to use your product?** If not, you are designing agent journeys based on assumptions. Run a real agent (Claude Code, Cursor) against your MCP server and observe where it struggles.

2. **Can an agent complete a meaningful task with your product in a single session?** If the agent needs to be restarted, reconfigured, or helped by a human partway through, the journey has a break.

3. **What happens when your API changes and an agent's cached understanding is stale?** Agents cache tool descriptions. If you rename a parameter or change a response shape, every cached agent will break silently.

4. **Is there a way for agents to discover your product without a human configuring it?** The highest-reach agent distribution comes from registry discoverability, not from humans manually adding MCP configs.

5. **Do you measure agent interactions separately from human interactions?** If agent traffic is mixed into your general analytics, you cannot diagnose agent-specific journey problems.

## Common Mistakes

1. **Designing only the happy path**
   Agent journeys are defined more by their failure modes than their success paths. Agents hit errors constantly — rate limits, malformed inputs, expired tokens. If you only design the happy path, every error becomes a dead end.

2. **Assuming agents read documentation like humans**
   Agents read tool descriptions, parameter schemas, and error codes. They do not read tutorials, conceptual guides, or "how it works" pages. If critical information is only in your guide and not in your schema, agents will miss it.

3. **Implicit tool ordering**
   If Tool B requires output from Tool A, this must be stated in Tool B's description or enforced by the API. "The user should call Tool A first" in your docs is invisible to agents. Make dependencies explicit or eliminate them.

4. **Inconsistent response shapes across similar tools**
   If `list_users` returns `{ data: [...], next_cursor: "..." }` but `list_orders` returns `{ results: [...], page: 2 }`, agents must special-case each tool. Consistency across tools is more important than any individual tool's design.

5. **Forgetting the chaining step**
   Your tool's output is another tool's input. If your output is not structured, parseable, and predictable, you break every downstream workflow. Design outputs for machines, not for human readability.

## Context Integration

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3 | Product architecture and current agent use cases. Informs which agent personas are relevant and which journeys to map first. |
| `context/competitive/` | Steps 2, 5 | Competitor agent journey benchmarks. How do competing products handle agent discovery, auth, and error recovery? |
| `context/verticals/` | Steps 1, 4 | Vertical-specific agent patterns. Enterprise agents need audit trails; consumer agents need speed. |
| `context/company/` | Step 6 | Engineering capacity for implementing journey improvements. |
| `context/signals/` | Steps 2, 4 | Real agent failure reports from community channels. [SIGNAL] tagged. |

If no `context/` directory is present, the skill will ask for:
1. The product name and what agents should be able to do with it
2. The existing agent interfaces (MCP server, CLI, API)
3. Known agent failure modes or complaints
4. The primary agent frameworks being targeted
