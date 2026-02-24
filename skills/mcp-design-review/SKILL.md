---
name: mcp-design-review
description: "Help users review an MCP server's design quality by assessing tool naming, descriptions, schemas, permission model, and error surfaces — producing a per-tool scorecard, security audit, and prioritized recommendations."
version: "1.0.0"
last_updated: "2026-02-24"
---

# MCP Design Review

Produces a structured review of an MCP server's design quality — scoring each tool's naming, description clarity, schema completeness, permission model, and error handling — delivering a per-tool scorecard and prioritized recommendations. Reach for this skill when building or launching an MCP server, when agent adoption is lower than expected, or when tool descriptions are being written by engineers without PM review.

## Core Principles

1. **Tool descriptions are the new API documentation**
   "The description field in an MCP tool is the single most important piece of text you write. It is the only thing an agent reads before deciding whether to call your tool. If the description is ambiguous, the agent will either skip your tool or call it incorrectly."
   — *MCP specification, Tool definition best practices* ([source](https://modelcontextprotocol.io/docs/concepts/tools))

2. **Agents choose tools by reading, not by browsing**
   "An agent does not explore your MCP server the way a human explores a website. It reads every tool description once, builds a mental model, and makes a selection. If your descriptions are unclear, the agent's mental model is wrong."
   — *Anthropic, Building effective agents* ([source](https://www.anthropic.com/research/building-effective-agents))

3. **Read-only by default is the only safe starting point**
   "The April 2025 MCP security audit found tool poisoning, data exfiltration via combined tools, and lookalike tool shadowing as real vulnerabilities. Ship read-only defaults and explicit approval workflows."
   — *Invariant Labs, MCP Security Notification* ([source](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

4. **Schema completeness prevents hallucinated parameters**
   "When an MCP tool's input schema is incomplete — missing descriptions, untyped parameters, no enums — the agent fills the gaps by guessing. Guessing means hallucinating parameter values. Complete schemas eliminate this failure mode."
   — *MCP specification, Input schema requirements* ([source](https://modelcontextprotocol.io/docs/concepts/tools))

5. **Fewer tools done well beats many tools done poorly**
   "The best MCP servers have 5-15 well-described tools, not 50 poorly described ones. Agent context windows are finite. Every tool you add competes for attention with every other tool. Curate ruthlessly."
   — *Analysis of high-adoption MCP server patterns* ([source](https://github.com/modelcontextprotocol/servers))

6. **Tool naming is a contract with the agent**
   "A tool named `process_data` tells the agent nothing. A tool named `search_customer_orders_by_date_range` tells the agent exactly when to reach for it. Name tools for their job-to-be-done, not their implementation."
   — *API design principles applied to MCP tools, Joshua Bloch* ([source](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf))

7. **Error responses must be agent-recoverable**
   "When an MCP tool returns an error, the agent has three options: retry, try a different tool, or give up. The error message determines which option the agent chooses. A message like 'Error occurred' leads to retry loops. A message like 'Invalid date format, expected YYYY-MM-DD' leads to immediate correction."
   — *Error design for programmatic consumers* ([source](https://modelcontextprotocol.io/docs/concepts/tools))

## Instructions

### Step 1: Inventory the MCP Server

- List every tool the MCP server exposes
- For each tool, record: name, description, input schema (parameters with types), output format, side effects (read-only vs. mutating), and required auth/permissions
- Group tools by capability domain (e.g., data retrieval, content creation, configuration management)
- Note the total tool count and whether it falls in the optimal range (5-15 tools)

**Artifact produced:** MCP Tool Inventory (table with all tools, their metadata, and groupings).

### Step 2: Score Each Tool's Description Quality

Evaluate each tool's description on five dimensions using a 1-5 scale:

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| **Clarity** | Vague or missing description | Describes what the tool does | Describes what, when to use, and when NOT to use |
| **Completeness** | Missing key information | Covers inputs and outputs | Covers inputs, outputs, side effects, and edge cases |
| **Specificity** | Generic ("processes data") | Somewhat specific | Fully specific ("searches orders by date range, returns max 100") |
| **Disambiguation** | Overlaps with other tools | Mostly distinct | Clearly explains when to use THIS tool vs. alternatives |
| **Actionability** | Agent cannot determine when to call | Agent can sometimes determine | Agent always knows when this tool is the right choice |

Compute per-tool and overall averages.

**Artifact produced:** Tool Description Scorecard (table with scores per dimension per tool).

### Step 3: Audit Input Schemas

For each tool, evaluate the input schema:

- Are all parameters typed (string, number, boolean, array, object)?
- Do parameters have descriptions explaining what they control?
- Are required vs. optional parameters marked correctly?
- Are enums used where values are constrained?
- Are defaults specified for optional parameters?
- Are format hints provided (e.g., "ISO 8601 date", "UUID v4")?
- Do parameter names follow a consistent convention?

Flag every instance of: untyped parameters, missing descriptions, stringly-typed enums (string where enum is appropriate), and ambiguous parameter names.

**Artifact produced:** Schema Completeness Audit (table of findings per tool with severity ratings).

### Step 4: Evaluate the Permission and Security Model

**Permission model assessment:**
- Which tools are read-only? Which mutate state? Is this clearly marked?
- Can agents connect with read-only access by default?
- Do mutating tools require explicit confirmation or approval?
- Is there permission scoping (e.g., tool-level access control)?

**Security checklist:**
- [ ] Tool descriptions contain no instruction injection vectors (no embedded prompts)
- [ ] Tool discovery does not expose sensitive metadata (API keys, internal URLs, user data)
- [ ] Input validation prevents injection through parameters
- [ ] Rate limiting is implemented per-tool or per-session
- [ ] Mutating operations are idempotent or clearly marked as non-idempotent
- [ ] Error messages do not leak internal system details

**Artifact produced:** Permission and Security Assessment (model evaluation + security checklist results).

### Step 5: Test Error Handling

Deliberately trigger errors and evaluate agent-recoverability:

- Missing required parameters — does the error say which parameter and what type?
- Invalid parameter values — does the error say what was wrong and what is expected?
- Auth failures — does the error distinguish expired vs. invalid vs. missing credentials?
- Rate limiting — is there a retry hint? Does the error include a wait duration?
- Internal errors — is there a request/trace ID? Is the message helpful or generic?

For each error, rate: **specificity** (does it say what went wrong?), **actionability** (does it say how to fix it?), and **recoverability** (can an agent correct the request without human help?).

**Artifact produced:** Error Handling Audit (table of triggered errors with recoverability ratings).

### Step 6: Produce Prioritized Recommendations

Compile all findings from Steps 2-5. Categorize each:

| Priority | Impact | Effort | Examples |
|----------|--------|--------|----------|
| **P0 — Fix before launch** | High | Low | Rewrite vague tool descriptions, add missing parameter types, fix injection vectors |
| **P1 — Fix this quarter** | High | Medium | Add read-only defaults, implement per-tool rate limits, add disambiguation to overlapping tools |
| **P2 — Plan for next quarter** | Medium | Medium-High | Build approval workflows for mutating tools, add tool versioning, create agent-specific quickstart |
| **P3 — Backlog** | Low-Medium | High | Multi-tenant permission model, tool analytics dashboard, community tool contributions |

Star the top 5 recommendations as "fix before shipping to agents."

**Artifact produced:** Prioritized Recommendations Table. Complete report saved as `applied/mcp-review-{server}.md`.

## Diagnostic Questions

1. **Can you explain when an agent should use each tool without looking at the description?** If the tool names alone are not descriptive enough, agents will struggle with tool selection.

2. **Are any two tools confusable?** If an agent could reasonably call either tool for the same task, you have a disambiguation problem that will cause unpredictable behavior.

3. **What happens when an agent calls a mutating tool by mistake?** If there is no confirmation step or undo mechanism, a single misrouted tool call can cause data loss.

4. **How many tools does your server expose?** If more than 15, agents spend more context processing tool descriptions than doing work. Consider splitting into multiple focused servers.

5. **Have you tested your MCP server with multiple agent frameworks (Claude, GPT, Gemini)?** Tool selection behavior varies across models. A description that works for Claude may confuse GPT.

6. **Do your tool descriptions mention other tools by name?** If Tool A's description says "use Tool B first," you are creating implicit workflows that agents may not follow. Make each tool self-contained.

## Common Mistakes

1. **Writing descriptions for humans, not agents**
   Human-facing descriptions use marketing language ("powerful", "comprehensive"). Agent-facing descriptions use functional language ("returns a list of orders filtered by date range, maximum 100 results, sorted by recency"). Strip adjectives, add specifics.

2. **Exposing internal implementation as tools**
   Tools should map to user jobs-to-be-done, not internal functions. If your MCP server has tools like `query_postgres` or `call_internal_api`, you are exposing implementation, not capability. Wrap internal operations in tools named for what the user accomplishes.

3. **No read-only default**
   Every new agent connection should start with read-only access. If your MCP server grants full write access immediately, you are one misconfigured agent away from data corruption. Read-only defaults are the seatbelt.

4. **Treating tool count as a feature**
   More tools is not better. Each tool competes for agent attention and context space. A server with 50 tools forces the agent to process 50 descriptions before making a selection. Consolidate related operations and split unrelated domains into separate servers.

5. **Generic error messages**
   "Error" or "Bad request" forces the agent into a retry loop. Every error must include: what went wrong (specific), what was expected (concrete), and whether the request can be corrected (actionable). Design errors for machines, not humans.

## Context Integration

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 6 | Product architecture and intended agent use cases. Informs which tools are highest-priority and what job-to-be-done each should serve. |
| `context/competitive/` | Steps 2, 6 | Competitor MCP servers as benchmarks for tool design, description quality, and feature coverage. |
| `context/verticals/` | Steps 4, 6 | Vertical-specific security and compliance requirements that affect the permission model (e.g., healthcare requires stricter access controls). |
| `context/company/` | Step 6 | Team capacity for implementing recommendations. Informs effort estimates. |
| `context/signals/` | Steps 1, 6 | Community feedback on MCP server usability, agent framework compatibility issues. [SIGNAL] tagged. |

If no `context/` directory is present, the skill will ask for:
1. The MCP server name and how to access it (npm package, GitHub repo, or running instance)
2. The intended agent use cases (what should agents accomplish with this server?)
3. The target agent frameworks (Claude, GPT, Gemini, etc.)
4. Any known issues with tool selection or agent behavior
