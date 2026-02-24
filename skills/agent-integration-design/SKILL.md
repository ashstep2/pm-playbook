---
name: agent-integration-design
description: "Help users design their product's integration surface for agent-driven workflows — producing I/O specifications, webhook designs, event stream architecture, and orchestration compatibility assessment."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Agent Integration Design

Produces a structured design for a product's integration surface optimized for agent-driven workflows — documenting structured I/O contracts, webhook specifications, event stream architecture, idempotency guarantees, and orchestration platform compatibility. Reach for this skill when operations teams are wiring your product into automated pipelines, when agents need to chain your product with other tools, or when integration failures are causing workflow breakdowns.

## Core Principles

1. **Your output is someone else's input**
   "Every API response is consumed by another system. If your response shape changes, if your pagination is inconsistent, if your error format varies — you break every downstream integration. Design for the consumer, not the provider."
   — *Joshua Bloch, How to Design a Good API and Why It Matters* ([source](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf))

2. **Agents chain tools — your product is one link**
   "Autonomous agents compose workflows from multiple tools. Your product is not the workflow — it is one step. If that step has unpredictable output, the entire chain fails. Reliability of a single tool is more valuable than richness of features."
   — *Agent orchestration patterns, LangChain / LangGraph* ([source](https://langchain-ai.github.io/langgraph/))

3. **Idempotency is the foundation of reliable agent workflows**
   "Agents retry. Networks fail. Messages duplicate. If your mutating operations are not idempotent, agent retries cause double-creates, double-charges, or data corruption. Idempotency keys are not optional for agent-consumed APIs."
   — *Stripe Engineering, Designing robust APIs* ([source](https://stripe.com/docs/api/idempotent_requests))

4. **Webhooks beat polling for agent efficiency**
   "An agent polling an endpoint every 5 seconds is wasting context window and compute on 'has anything changed?' questions. Webhooks push events when they happen, letting agents react instead of ask. For long-running operations, webhooks are the difference between a working pipeline and a polling loop."
   — *Event-driven architecture for integrations* ([source](https://docs.github.com/en/webhooks))

5. **Standard formats reduce integration cost to zero**
   "Every custom format is an integration tax. JSON with documented schemas, ISO 8601 dates, RFC 3339 timestamps, UUID identifiers — these are the universal connectors. Every deviation forces the consumer to write a custom adapter."
   — *API design standards, JSON:API and OpenAPI* ([source](https://jsonapi.org/))

6. **Rate limits are an interface, not a restriction**
   "Rate limits should be communicated proactively, not discovered through 429 errors. Include `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and `Retry-After` headers. Agents that know their limits can self-govern. Agents that discover limits through failures cause support tickets."
   — *Rate limiting best practices, Cloudflare* ([source](https://developers.cloudflare.com/fundamentals/api/reference/limits/))

7. **Orchestration platforms are your real users**
   "Operations teams build on n8n, Zapier, Make, Temporal, and custom LangGraph pipelines. These platforms have specific requirements: webhook verification, structured triggers, standard auth (OAuth2, API keys), and predictable response envelopes. If your product works with these platforms, agents can use it immediately."
   — *Integration platform compatibility analysis* ([source](https://docs.n8n.io/integrations/creating-nodes/))

## Instructions

### Step 1: Map Integration Touchpoints

Inventory every point where external systems (agents, orchestrators, pipelines) interact with your product.

| Touchpoint | Type | Direction | Format | Auth | Reliability |
|-----------|------|-----------|--------|------|-------------|
| REST API | Request/Response | Inbound | JSON | API Key | Synchronous |
| Webhooks | Event push | Outbound | JSON | Signature | At-least-once |
| Event stream | Continuous | Outbound | SSE/WebSocket | Token | Ordered |
| CLI | Command | Inbound | JSON/text | Token/env var | Synchronous |
| MCP tools | Request/Response | Inbound | JSON | Session | Synchronous |
| File export | Batch | Outbound | CSV/JSON | N/A | On-demand |

For each touchpoint, document: current state, quality (1-5), and whether it is designed for agent consumption or only for human use.

**Artifact produced:** Integration Touchpoint Inventory.

### Step 2: Define I/O Contracts for Agent Consumption

For each integration touchpoint, formalize the input/output contract.

**Contract template:**

```
Endpoint/Tool: [name]
Direction: [inbound / outbound]

Input:
  Required fields: [field: type — description]
  Optional fields: [field: type — default — description]
  Validation rules: [constraints, mutual exclusions]

Output:
  Success envelope: { "data": ..., "meta": { "request_id": "...", "timestamp": "..." } }
  Pagination: { "next_cursor": "...", "has_more": true }
  Empty result: { "data": [], "meta": { ... } }

Error envelope: { "error": { "code": "...", "message": "...", "details": [...], "request_id": "..." } }

Idempotency: [key mechanism — header / parameter / natural]
Rate limit headers: [X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Reset]
```

**Key rules:**
- Response envelopes must be consistent across ALL endpoints
- Pagination must use the same mechanism everywhere (cursor-based preferred)
- Error envelopes must include machine-readable codes, not just messages
- Every response must include a request ID for tracing

**Artifact produced:** I/O Contract Registry (one contract per touchpoint).

### Step 3: Design the Webhook System

For each event type your product emits, design the webhook specification.

| Event | Payload Schema | Delivery | Retry Policy | Verification |
|-------|---------------|----------|-------------|--------------|
| `resource.created` | `{ "event": "resource.created", "data": {...}, "timestamp": "..." }` | POST to subscriber URL | 3 retries, exponential backoff | HMAC-SHA256 signature |
| `resource.updated` | Same envelope, diff payload | Same | Same | Same |
| `resource.deleted` | Same envelope, resource ID only | Same | Same | Same |
| `operation.completed` | Includes result data | Same | Same | Same |
| `operation.failed` | Includes error details | Same | Same | Same |

**Webhook design requirements:**
- Consistent event envelope across all event types
- HMAC signature verification (agents must validate webhook authenticity)
- Idempotency — include event ID so consumers can deduplicate
- Retry with exponential backoff and dead letter queue
- Webhook management API (subscribe, unsubscribe, list, test)

**Artifact produced:** Webhook Specification (event catalog, payload schemas, delivery guarantees).

### Step 4: Assess Orchestration Platform Compatibility

Test compatibility with the major agent orchestration platforms.

| Platform | Compatible? | Auth Method | Trigger Types | Known Issues |
|----------|------------|-------------|--------------|-------------|
| **n8n** | | OAuth2 / API Key | Webhook, Polling, Cron | |
| **Zapier** | | OAuth2 | Webhook triggers, Action calls | |
| **Make (Integromat)** | | API Key / OAuth2 | Webhook, Scheduled | |
| **LangGraph/LangChain** | | API Key | Tool calling | |
| **Temporal** | | API Key | Activity functions | |
| **Claude Code (MCP)** | | Session token | MCP tool calling | |
| **Custom agents** | | API Key | Direct API | |

For each platform, document: what works, what breaks, and what adaptation is needed.

**Artifact produced:** Orchestration Compatibility Matrix.

### Step 5: Design Event Stream Architecture (if applicable)

For products with real-time data or long-running operations, design the event streaming surface.

**Streaming options to evaluate:**
- **Server-Sent Events (SSE):** One-directional, simple, HTTP-native. Best for progress updates and real-time feeds.
- **WebSockets:** Bidirectional, complex, stateful. Best for interactive agent sessions.
- **Polling with long-poll:** Simple, stateless, universally compatible. Fallback for environments that block streaming.

**For each stream, specify:**
- Event types and their schemas
- Connection lifecycle (auth, heartbeat, reconnection)
- Ordering guarantees (ordered / best-effort)
- Backpressure handling
- State recovery after disconnect

**Artifact produced:** Event Stream Architecture Specification.

### Step 6: Build the Integration Improvement Roadmap

Compile all findings into a prioritized roadmap.

| Priority | Improvement | Impact on Agent Workflows |
|----------|------------|--------------------------|
| **P0** | Standardize response envelopes across all endpoints | Eliminates custom parsing per endpoint |
| **P0** | Add idempotency keys to all mutating operations | Prevents duplicate actions on retry |
| **P1** | Ship webhook system with HMAC verification | Enables event-driven pipelines |
| **P1** | Add rate limit headers to all responses | Enables agent self-governance |
| **P2** | Build orchestration platform connectors (n8n, Zapier) | Unlocks no-code agent workflows |
| **P3** | Add SSE streaming for long-running operations | Eliminates polling loops |

**Artifact produced:** Integration Improvement Roadmap saved as part of `applied/agent-integration-{product}.md`.

## Diagnostic Questions

1. **If an agent retries a failed create operation, will it produce a duplicate?** If yes, you need idempotency keys before anything else.

2. **Does every API response include a request ID?** Without request IDs, debugging agent workflow failures across multiple tools is nearly impossible.

3. **Can an agent subscribe to events without polling?** Polling wastes agent compute and creates unnecessary load. Webhooks or event streams are the agent-friendly alternative.

4. **Are your response envelopes consistent across all endpoints?** If list endpoints and detail endpoints return different shapes, every agent integration needs endpoint-specific parsing logic.

5. **Does your product work with n8n or Zapier today?** These platforms are proxies for agent compatibility. If they cannot integrate, neither can agents.

## Common Mistakes

1. **Inconsistent response envelopes**
   The number one integration failure. If `/users` returns `{ "users": [...] }` and `/orders` returns `{ "data": [...] }`, every consumer must special-case each endpoint. Pick one envelope and enforce it everywhere.

2. **Missing idempotency on mutations**
   Agents retry. Networks fail. Without idempotency keys, retries create duplicates. This is not a theoretical concern — it is the most common bug in agent-driven workflows.

3. **Webhook payloads without signatures**
   An unsigned webhook is an injection vector. Any system that accepts unsigned webhooks can be spoofed. HMAC-SHA256 signatures are table stakes.

4. **Rate limits discovered through errors**
   If the first time an agent learns about your rate limit is a 429 response, you have already disrupted its workflow. Communicate limits proactively via headers on every response.

5. **Custom date/time formats**
   If your timestamps are not ISO 8601, every consumer writes a custom parser. This seems trivial but it is one of the most common integration friction points.

## Context Integration

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3 | Product architecture, API surface, existing integration points. Essential for mapping touchpoints. |
| `context/competitive/` | Step 4 | Competitor integration surfaces. What orchestration platforms do competitors support? |
| `context/verticals/` | Steps 3, 5 | Vertical-specific integration requirements (e.g., healthcare needs HL7 FHIR, finance needs FIX protocol). |
| `context/company/` | Step 6 | Engineering capacity for integration work. |
| `context/signals/` | Steps 1, 4 | Integration-related feature requests and complaints from community channels. [SIGNAL] tagged. |

If no `context/` directory is present, the skill will ask for:
1. Product name and API documentation link
2. Current integration surfaces (API, webhooks, CLI, MCP)
3. Primary orchestration platforms used by customers
4. Known integration pain points
