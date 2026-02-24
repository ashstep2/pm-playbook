---
name: agent-surface-audit
description: "Help users audit whether their product is discoverable and usable by AI agents — producing an agent accessibility scorecard, surface area inventory, machine-readability assessment, and prioritized remediation roadmap."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Agent Surface Audit

Produces a scored audit of a product's agent-accessible surface area — CLI, MCP server, machine-readable documentation, structured output, auth model — delivering an agent accessibility scorecard and prioritized roadmap to make the product discoverable and usable by autonomous agents. Reach for this skill when agents are part of your distribution strategy, when competitors ship MCP servers, or when you realize your product is invisible to the fastest-growing software consumer: the AI agent.

## Core Principles

1. **If agents cannot access your product, you do not exist in agent workflows**
   "If you have any kind of product or service think: can agents access and use them? It's 2026. Build. For. Agents."
   — *Andrej Karpathy, Co-founder of OpenAI, Former Senior Director of AI at Tesla* ([source](https://x.com/kaborge/status/1893751065683628530))

2. **CLIs are the agent-native interface**
   "CLIs are super exciting precisely because they are a 'legacy' technology, which means AI agents can natively and easily use them, combine them, interact with them via the entire terminal toolkit."
   — *Andrej Karpathy, Co-founder of OpenAI, Former Senior Director of AI at Tesla* ([source](https://x.com/kaborge/status/1893751065683628530))

3. **MCP is the new baseline for product discovery**
   "Running an MCP server is now compared to running a web server. MCP went from zero to 97 million monthly SDK downloads in twelve months, with 10,000+ active servers."
   — *Model Context Protocol adoption data, Anthropic / Linux Foundation* ([source](https://modelcontextprotocol.io/))

4. **Machine-readable docs are the real unlock**
   "MCP servers without clear tool descriptions are like websites without text — technically accessible, functionally useless. The companies that invest in context engineering for their developer docs will pull ahead."
   — *Contextual analysis of agent-first distribution patterns* ([source](https://www.anthropic.com/research/building-effective-agents))

5. **Agent-accessible surface area is the new competitive moat**
   "Your competitor ships an MCP server and suddenly every Claude Code user, every Cursor session, every autonomous workflow can discover and use their product. No human ever visits the website."
   — *Analysis of agent-first distribution dynamics* ([source](https://docs.anthropic.com/en/docs/agents-and-tools/mcp))

6. **Agent-first startups beat GUI-first incumbents**
   "A startup can launch agent-first from day one with full CLI and MCP support, zero legacy UI debt. We saw this exact pattern play out with mobile. The companies that tried to retrofit desktop apps for phones lost to mobile-native startups."
   — *Platform transition analysis, mobile-to-agent analogy* ([source](https://a16z.com/the-new-new-moats/))

7. **Security is not optional for agent surfaces**
   "Building for agents without building agent-grade security is how you end up in a breach headline. The smart move is shipping MCP support with read-only defaults and explicit approval workflows before opening up write access."
   — *MCP security audit findings, April 2025* ([source](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks))

8. **Design for stdin/stdout, not for screens**
   "The entire Unix philosophy was accidentally designed for AI agents decades before they existed. stdin/stdout, flags, JSON output — these are the primitives agents understand natively."
   — *Unix design philosophy applied to agent interfaces* ([source](https://en.wikipedia.org/wiki/Unix_philosophy))

## Instructions

### Step 1: Inventory Current Agent Surface Area

Catalog every programmatic access point your product currently exposes. Be exhaustive — include surfaces that exist but are poorly documented.

**Surface types to check:**

| Surface | Exists? | Quality (1-5) | Notes |
|---------|---------|---------------|-------|
| **REST/GraphQL API** | | | Documented? Versioned? JSON responses? |
| **CLI tool** | | | Installable via package manager? JSON output flag? |
| **MCP server** | | | Published? How many tools? Tool descriptions quality? |
| **SDK/client libraries** | | | Which languages? Auto-generated or hand-crafted? |
| **Webhooks/event streams** | | | Structured payloads? Retry logic? |
| **Machine-readable docs** | | | OpenAPI spec? Markdown exportable? |
| **Structured error responses** | | | Machine-parseable? Error codes? Remediation hints? |

For each surface that exists, note: discoverability (can an agent find it?), parseability (can an agent understand the output?), and actionability (can an agent accomplish a task end-to-end?).

**Artifact produced:** Agent Surface Inventory (table with all surfaces, existence, quality scores, and gap analysis).

### Step 2: Test Agent Discoverability

Simulate an agent trying to discover and use your product. This is the agent equivalent of the time-to-hello-world test.

**Discovery protocol:**
1. Search for your product name + "MCP server" — does anything come up?
2. Search for your product name + "CLI" — is there an installable tool?
3. Check your docs landing page — is there a machine-readable version (OpenAPI, markdown export)?
4. Look for your product on MCP registries (mcp.run, Smithery, glama.ai)
5. Check npm/pip/brew for a CLI or SDK package
6. Read your API docs as an agent would — are tool descriptions, parameter schemas, and response formats unambiguous?

**Scoring rubric:**

| Agent Discoverability | Grade | Benchmark |
|----------------------|-------|-----------|
| MCP server + CLI + OpenAPI spec | A | Fully agent-accessible |
| API + CLI with JSON output | B | Usable but requires integration work |
| API only, no CLI or MCP | C | Agent must build its own adapter |
| GUI only, no programmatic access | D | Invisible to agents |
| No public surface at all | F | Does not exist in agent workflows |

**Artifact produced:** Agent Discoverability Report (test results, grade, and gap analysis).

### Step 3: Assess Machine-Readability of Documentation

Evaluate whether your documentation can be consumed by agents, not just read by humans.

**Dimensions to evaluate:**

| Dimension | What to Check | Score (1-5) |
|-----------|--------------|-------------|
| **Format accessibility** | Are docs available in markdown, not just rendered HTML? Can they be fetched programmatically? |  |
| **Tool descriptions** | For each API endpoint/MCP tool: is the description unambiguous? Does it specify what the tool does, required inputs, expected outputs, and side effects? |  |
| **Parameter schemas** | Are all parameters typed with descriptions? Are enums documented? Are defaults specified? |  |
| **Response contracts** | Is the response shape guaranteed? Are all fields documented with types? Is pagination documented? |  |
| **Error cataloging** | Are all error codes listed with machine-readable codes (not just messages)? Are remediation steps included? |  |
| **Example completeness** | Are there copy-paste-runnable examples for every major workflow? Do examples include expected responses? |  |

For each dimension scoring 3 or below, provide a specific example and remediation.

**Artifact produced:** Machine-Readability Scorecard (6 dimensions with scores, evidence, and fixes).

### Step 4: Evaluate the Auth and Permission Model for Agent Access

Agents need a different auth model than humans. Evaluate whether your product supports agent-safe access patterns.

**Check for:**
- API key or token-based auth (agents cannot complete OAuth browser flows without human intervention)
- Scoped permissions (can an agent get read-only access? Can permissions be narrowed to specific resources?)
- Rate limiting transparency (are limits documented? Is there a `Retry-After` header? Can agents detect approaching limits?)
- Approval workflows (can write operations require human approval before execution?)
- Audit trail (are agent actions logged separately from human actions?)

**Security checklist (from MCP security audit findings):**
- [ ] Read-only defaults for new agent connections
- [ ] Explicit opt-in for write/delete operations
- [ ] Tool descriptions do not contain injection vectors
- [ ] No sensitive data exposed in tool discovery responses
- [ ] Rate limits prevent agent-driven resource exhaustion

**Artifact produced:** Agent Auth and Security Assessment (auth model evaluation, permission gap analysis, security checklist results).

### Step 5: Score the Agent Accessibility Scorecard

Synthesize findings from Steps 1-4 into a composite score.

| Category | Score (1-10) | Weight | Weighted Score | Key Finding |
|----------|-------------|--------|---------------|-------------|
| Surface area breadth (CLI, MCP, API, SDK) | | 20% | | |
| Agent discoverability | | 25% | | |
| Machine-readability of docs | | 25% | | |
| Auth and permission model | | 15% | | |
| Structured output quality | | 15% | | |
| **Overall Agent Accessibility Score** | | **100%** | | |

**Grading thresholds:**
- **80-100:** Agent-first product — fully discoverable and usable by autonomous agents
- **60-79:** Agent-accessible with friction — agents can use it but require workarounds
- **40-59:** Agent-hostile — significant investment needed to become agent-accessible
- **Below 40:** Agent-invisible — product does not exist in agent workflows

**Artifact produced:** Agent Accessibility Scorecard with overall grade.

### Step 6: Build the Agent Surface Remediation Roadmap

Prioritize investments to make the product agent-accessible.

| Priority | Impact | Effort | Examples |
|----------|--------|--------|----------|
| **P0 — Ship this month** | High | Low | Add `--json` flag to CLI, publish OpenAPI spec, write MCP tool descriptions |
| **P1 — Ship this quarter** | High | Medium | Build and publish MCP server, add scoped API keys, export docs as markdown |
| **P2 — Plan for next quarter** | Medium | Medium-High | Build SDK with agent-friendly defaults, add webhook subscriptions, create agent-specific quickstart |
| **P3 — Backlog** | Low-Medium | High | Agent-specific analytics dashboard, multi-agent collaboration support, agent marketplace listing |

For each item, specify: the gap it closes (reference the step), expected impact on Agent Accessibility Score, effort estimate, and owner.

**Artifact produced:** Agent Surface Remediation Roadmap (prioritized table).

### Step 7: Compile the Agent Surface Audit Report

Assemble all artifacts:

1. Executive Summary (one paragraph: overall grade, top 3 strengths, top 3 gaps, competitive implications)
2. Agent Surface Inventory (Step 1)
3. Agent Discoverability Report (Step 2)
4. Machine-Readability Scorecard (Step 3)
5. Agent Auth and Security Assessment (Step 4)
6. Agent Accessibility Scorecard (Step 5)
7. Agent Surface Remediation Roadmap (Step 6)
8. Recommended immediate actions (top 3 things to ship this week)

**Artifact produced:** Complete Agent Surface Audit Report saved as `applied/agent-surface-audit-{product}.md`.

## Diagnostic Questions

1. **Can an AI agent install your product and make a successful request without any human guidance?** If not, you have an agent onboarding problem that maps directly to lost distribution.

2. **Does your product appear on any MCP registry?** If a developer searches for your category on mcp.run or Smithery and finds a competitor but not you, that competitor wins every agent workflow.

3. **What happens when an agent calls your API and gets an error?** If the error response is a human-readable string instead of a structured object with an error code, the agent cannot recover programmatically.

4. **Can an agent get read-only access to your product without human intervention?** OAuth browser flows, CAPTCHA, and email verification all break agent workflows. Token-based auth with scoped permissions is the minimum.

5. **Are your docs available as markdown or only as rendered HTML?** Agents consume markdown natively. A beautiful docs site that only serves HTML is a walled garden to agents.

6. **What percentage of your product's functionality is accessible via API vs. only via GUI?** The GUI-only percentage is your agent-invisible surface area.

7. **Has a competitor shipped an MCP server or CLI for equivalent functionality?** If yes, every autonomous workflow will route to them instead of you.

## Common Mistakes

1. **Shipping a CLI wrapper and calling it done**
   A CLI that wraps your API with `curl` commands is not agent-accessible. Agents need structured JSON output, consistent flag conventions, composable commands, and non-interactive authentication. The CLI must be designed as a first-class interface, not an afterthought.

2. **Publishing an MCP server without good tool descriptions**
   An MCP server with tool names like `do_thing` and descriptions like "Does the thing" is functionally useless. Each tool needs a description that tells an agent: what it does, what inputs it requires, what output it returns, what side effects it has, and when to use it vs. alternatives.

3. **Requiring OAuth browser flows for all access**
   Agents cannot click "Authorize" in a browser popup. If your only auth mechanism requires human browser interaction, you have zero agent accessibility. Ship API keys or service tokens with scoped permissions as a parallel auth path.

4. **Treating agent security as a future concern**
   The April 2025 MCP security audit found real vulnerabilities: tool poisoning, data exfiltration, and tool shadowing. Shipping agent access without read-only defaults, permission scoping, and input validation is shipping a vulnerability.

5. **Optimizing the landing page instead of the tool descriptions**
   Agents do not read landing pages. They read tool descriptions, parameter schemas, and response contracts. Every hour spent on landing page copy instead of machine-readable documentation is an hour invisible to agent-mediated distribution.

6. **Forgetting that agents are a distribution channel, not just a feature**
   Agent accessibility is not a "nice to have" integration. It is a distribution channel. When 85% of enterprises deploy AI agents, those agents decide which tools enter the workflow. If your product is not agent-accessible, it is not in the consideration set.

## Context Integration

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3, 5 | Product architecture, API surface, existing integrations. Essential for inventorying current agent surfaces and identifying gaps. |
| `context/competitive/` | Steps 2, 5, 6 | Competitor agent surfaces (do they have MCP servers? CLIs?). Calibrates urgency and helps prioritize remediation. |
| `context/verticals/` | Steps 2, 6 | Target market expectations for agent access. Enterprise verticals may require stricter auth models; developer verticals demand CLI and MCP first. |
| `context/company/` | Steps 4, 6, 7 | Team size and engineering capacity. Informs effort estimates and P0/P1 scoping in the remediation roadmap. |
| `context/signals/` | Steps 1, 2, 5 | Auto-collected signals about agent ecosystem trends, MCP adoption, competitor MCP launches. [SIGNAL] tagged. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. The product name and a link to its documentation
2. A list of existing programmatic access points (API, CLI, SDK)
3. The primary user personas (developers, enterprise buyers, consumers)
4. Whether any competitors have shipped MCP servers or agent-specific interfaces
