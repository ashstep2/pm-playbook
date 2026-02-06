---
name: api-design-review
description: "Help users review an API's design quality by assessing endpoints against REST conventions, consistency standards, and developer ergonomics — producing a per-endpoint scorecard, naming audit, error handling review, and prioritized recommendations."
version: "1.0.0"
last_updated: "2026-02-06"
---

# API Design Review

Produces a structured API design review scoring each endpoint against REST conventions, consistency standards, and developer ergonomics. Reach for this skill when launching a new API, onboarding external developers, preparing for a public beta, or auditing an existing surface for inconsistencies before they calcify.

## Core Principles

1. **APIs are forever**
   "Public APIs, like diamonds, are forever. You have one chance to get it right, so give it your best."
   -- *Joshua Bloch, How to Design a Good API and Why It Matters* ([source](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/32713.pdf))

2. **Consistency is the ultimate feature**
   "We've found that the most important thing in API design is consistency. If you have to choose between the best possible name for a single endpoint and keeping things consistent across your entire API, choose consistency every time."
   -- *Stripe Engineering, Designing APIs for Humans* ([source](https://dev.to/stripe/designing-apis-for-humans-object-ids-2afo))

3. **Design for the consumer, not the provider**
   "An API is a user interface for developers. Your job is to make the developer successful as quickly as possible. Every design decision should be evaluated from the caller's perspective."
   -- *Joshua Bloch, Bumper-Sticker API Design* ([source](https://www.infoq.com/articles/API-Design-Joshua-Bloch/))

4. **Names carry contracts**
   "Naming is the most important and most difficult aspect of API design. A good name drives the design, while a bad name hides design problems under a veil of ambiguity."
   -- *Arnaud Lauret, The Design of Web APIs, Manning Publications* ([source](https://www.manning.com/books/the-design-of-web-apis))

5. **Errors are part of the interface**
   "When an API returns an error, the developer using it is stuck. An error response is not a failure of the system to communicate — it IS the communication. Make it count."
   -- *Mike Amundsen, Design and Build Great Web APIs, Pragmatic Bookshelf* ([source](https://pragprog.com/titles/maapis/design-and-build-great-web-apis/))

6. **Hypermedia as affordance**
   "A truly RESTful API tells the client what it can do next. If your API requires out-of-band knowledge to navigate, it's an HTTP API — not a REST API — and that's fine, but know which one you're building."
   -- *Leonard Richardson and Mike Amundsen, RESTful Web APIs, O'Reilly Media* ([source](https://www.oreilly.com/library/view/restful-web-apis/9781449359713/))

7. **APIs encode organizational decisions**
   "Every API is an expression of organizational priorities, technical debt, and design philosophy — whether intentional or not. Reviewing an API tells you as much about the company as it does about the endpoints."
   -- *Kin Lane, API Evangelist* ([source](https://apievangelist.com/2014/06/05/what-are-the-incentives-for-creating-machine-readable-api-definitions/))

8. **Versioning is a social contract**
   "The hardest part of API versioning is not the technical mechanism. It's the organizational commitment to support old versions while shipping new ones. Your versioning strategy is a promise about how much you value backwards compatibility."
   -- *Stripe Engineering, APIs as infrastructure* ([source](https://stripe.com/blog/api-versioning))

## Instructions

### Step 1: Inventory the API Surface

- List every endpoint (method + path) the API exposes
- For each endpoint, record: HTTP method, path, authentication requirements, request body schema, response schema, documented status codes
- Group endpoints by resource (e.g., all `/worlds/*` endpoints, all `/media-assets/*` endpoints)
- Note which endpoints are CRUD operations vs. custom actions vs. long-running operations

**Artifact:** API Surface Inventory table with columns: Resource, Method, Path, Auth, Input Type, Output Type, Action Category

### Step 2: Score Each Endpoint Against REST Conventions

Evaluate each endpoint on the following dimensions using a 1-5 scale:

| Dimension | 1 (Poor) | 3 (Acceptable) | 5 (Excellent) |
|---|---|---|---|
| **Resource naming** | Verbs in paths, inconsistent pluralization | Mostly nouns, minor inconsistencies | Clean plural nouns, logical hierarchy |
| **HTTP method correctness** | GET with side effects, POST for reads | Minor mismatches | Methods match semantics precisely |
| **Status code accuracy** | 200 for everything | Correct for happy path, generic for errors | Correct and specific for all cases |
| **Idempotency** | No idempotency on mutating calls | Partial coverage | Idempotency keys on all mutating endpoints |
| **Pagination** | No pagination on list endpoints | Offset-based only | Cursor-based with consistent envelope |

- Score each endpoint on each dimension
- Compute a per-endpoint average and an overall API average

**Artifact:** Per-Endpoint Scorecard (table with scores per dimension per endpoint, plus averages)

### Step 3: Audit Naming Conventions and Consistency

- Extract all resource names, field names, query parameter names, and header names
- Check for: consistent casing (camelCase vs. snake_case vs. kebab-case), consistent pluralization, consistent use of abbreviations, consistent date/time formats
- Flag mixed conventions (e.g., `world_id` in one response, `worldId` in another)
- Check action naming for custom endpoints (e.g., `:generate` vs. `/generate` vs. POST to collection)
- Compare against the API's own stated conventions (if documented) and against industry norms

**Artifact:** Naming Consistency Audit listing every inconsistency found, grouped by category (casing, pluralization, abbreviation, formatting)

### Step 4: Review Error Handling

- Document every error response format the API uses
- Check for: consistent error envelope structure, machine-readable error codes (not just HTTP status), human-readable error messages, field-level validation errors, request ID / trace ID in error responses
- Test edge cases: What happens with malformed input? Missing required fields? Invalid auth? Rate limiting?
- Compare error format against established patterns (RFC 7807 Problem Details, Google API error format, Stripe error object)

**Artifact:** Error Handling Review with a format consistency table, a gap analysis vs. RFC 7807, and specific findings for each error scenario tested

### Step 5: Evaluate Versioning Strategy

- Identify the current versioning mechanism (URL path, header, query parameter, or none)
- Assess: Is the versioning scheme documented? Are breaking vs. non-breaking change policies defined? Is there a deprecation timeline and communication plan? How are beta/experimental endpoints marked?
- Review the changelog or release notes for evidence of how versioning has been practiced (not just documented)
- Flag any unversioned public endpoints as high-risk

**Artifact:** Versioning Strategy Evaluation with mechanism assessment, policy gap analysis, and risk rating (low/medium/high) for backwards compatibility

### Step 6: Assess Developer Ergonomics

- Evaluate the "time to first successful call" — how many steps from reading the docs to getting a 200 response?
- Check for: sandbox/test mode availability, copy-pasteable examples in docs, SDK availability and quality, rate limit headers and documentation, webhook/callback patterns for async operations
- Assess the polling pattern for long-running operations: Is there a webhook alternative? Are progress indicators available? Is the polling interval documented?

**Artifact:** Developer Ergonomics Assessment rating time-to-first-call, documentation completeness, SDK quality, and async operation patterns

### Step 7: Produce Prioritized Recommendations

- Compile all findings from Steps 2-6
- Categorize each finding as: **Breaking** (requires versioning to fix), **Non-breaking** (can ship immediately), or **Convention** (style preference, adopt going forward)
- Prioritize by: developer impact (how many developers hit this), severity (confusion vs. blocker), fix cost (minutes vs. weeks)
- Produce a ranked recommendation list with the top 5 starred as "fix before public launch" items

**Artifact:** Prioritized Recommendations Table with columns: Priority Rank, Finding, Category (Breaking/Non-breaking/Convention), Developer Impact (High/Med/Low), Fix Cost (High/Med/Low), Recommendation

## Diagnostic Questions

1. **Is the API public, partner-only, or internal?** Public APIs face the strictest consistency bar because breaking changes affect unknown consumers. Partner APIs allow more coordination. Internal APIs can iterate faster.

2. **What stage is the API in?** Pre-launch APIs can absorb breaking changes freely. Post-launch APIs require versioning for any breaking fix. The review should calibrate urgency accordingly.

3. **What are the primary consumer personas?** An API consumed by frontend engineers has different ergonomic needs than one consumed by data scientists or embedded systems developers.

4. **Does the API have an existing style guide or design spec?** If yes, the review audits compliance. If no, the review produces a recommended style guide as a bonus artifact.

5. **Are there SDKs or client libraries?** SDKs can paper over some API inconsistencies, but they also amplify naming problems across languages.

6. **What is the expected call volume and latency sensitivity?** High-volume APIs need pagination, rate limiting, and caching headers reviewed more carefully.

7. **How are long-running operations handled?** APIs with async operations (generation, processing) need specific review of polling patterns, webhooks, and timeout behavior.

## Common Mistakes

1. **Reviewing only the happy path**
   Most API design reviews test the success case and skip error scenarios. Developers spend more time debugging errors than celebrating successes. Allocate at least 30% of review time to error handling and edge cases.

2. **Confusing REST purity with good design**
   Strict REST adherence (HATEOAS, hypermedia controls) is not always the right goal. Many excellent APIs are "pragmatic REST" or RPC-style. Score the API against its own stated design philosophy, not an abstract ideal.

3. **Ignoring the async operation pattern**
   APIs that trigger long-running work (world generation, video processing, ML inference) need a distinct review of their operation lifecycle. Treating a `POST /worlds:generate` the same as a `POST /users` misses the most complex part of the API surface.

4. **Bikeshedding naming without impact analysis**
   Not all naming inconsistencies are equal. A casing mismatch on a rarely-used field matters far less than inconsistent error codes on a high-traffic endpoint. Tie every finding to developer impact.

5. **Skipping the versioning conversation**
   Teams often defer versioning strategy until the first breaking change forces the issue. By then, the options are constrained. Every API review should assess versioning readiness even if no breaking changes are planned.

6. **Reviewing the API in isolation from its docs**
   An API and its documentation are a single product. A perfectly designed endpoint with no documentation is worse than an imperfect endpoint with great examples. Review both together.

## Context Integration

| Context Directory | Feeds Step | How It's Used |
|---|---|---|
| `context/products/` | Step 1, Step 6 | Product descriptions provide the API's purpose, user base, and technical architecture. Informs which endpoints are highest-traffic and which developer personas to optimize for. |
| `context/competitive/` | Step 2, Step 5 | Competitor API designs provide benchmarks for conventions, error formats, and versioning strategies. Grounds recommendations in industry norms rather than abstract ideals. |
| `context/verticals/` | Step 3, Step 7 | Vertical-specific conventions (e.g., gaming APIs use different patterns than fintech APIs) inform which naming and design norms to apply. |
| `context/signals/` | Step 6, Step 7 | Developer community feedback (GitHub issues, Discord discussions, forum posts) reveals which API pain points are most frequently reported. Prioritizes recommendations by real developer friction. |
| `context/company/` | Step 5 | Organizational context (team size, release cadence, engineering culture) informs how ambitious the versioning and deprecation recommendations should be. |
