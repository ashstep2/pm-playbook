---
name: developer-experience-audit
description: "Help users audit the developer experience of an API or developer product — producing a friction scorecard, time-to-hello-world analysis, documentation quality assessment, and prioritized DX improvement roadmap."
---

# Developer Experience Audit

Produces a scored audit of an API or developer product's end-to-end developer experience — from first-encounter discovery through production deployment — delivering a friction scorecard, time-to-hello-world analysis, documentation quality assessment, error experience review, and a prioritized DX improvement roadmap.

## Core Principles

1. **The best developer experience is one where the developer never thinks about the tool**
   "The best thing a payment system can do is get completely out of the way. The measure of a great developer experience is the absence of friction, not the presence of features."
   — *Patrick Collison, Co-founder and CEO of Stripe* ([source](https://www.wired.com/2012/01/online-payments-stripe/))

2. **A README is the most important document in a project**
   "A perfect implementation of the wrong specification is worthless. By the same principle, a beautifully designed library with no documentation is also damn near worthless. If your software can't be used by other people, it's almost as if it doesn't exist."
   — *Tom Preston-Werner, Co-founder of GitHub, "Readme Driven Development"* ([source](https://tom.preston-werner.com/2010/08/23/readme-driven-development.html))

3. **Ask your developer — they are the new kingmaker**
   "The companies that understand developers and treat them as first-class customers will win. Developers are the new kingmakers because software is eating the world and they are the ones writing it. If you want developers to adopt your platform, you need to understand them deeply, not just market to them."
   — *Jeff Lawson, Co-founder and former CEO of Twilio, Author of Ask Your Developer* ([source](https://www.askyourdeveloper.com/))

4. **Time-to-hello-world is the only metric that matters at first**
   "Developer marketing is really developer experience. Everything a developer does from first discovering your product to getting their first 'hello world' running — that's what determines whether they stay or leave. If you can't get a developer to value in under 5 minutes, you've lost them."
   — *Adam DuVander, Developer experience consultant and author of Developer Marketing Does Not Exist* ([source](https://www.developermarketing.io/))

5. **Good error messages are a feature, not a detail**
   "Every time a developer hits an error that doesn't tell them what went wrong and how to fix it, you've broken a promise. The error message is the interface at the moment the developer needs you most. Treat error messages as a first-class product surface."
   — *Jean Yang, Founder of Akita Software* ([source](https://future.com/the-case-for-developer-experience/))

6. **Developer tools win by being discovered at the moment of need**
   "Developers have become the most important buying group in enterprise software. They don't respond to traditional marketing — they discover tools through documentation, Stack Overflow answers, and peer recommendations. Your developer experience IS your go-to-market."
   — *James Governor, Co-founder of RedMonk* ([source](https://redmonk.com/jgovernor/2020/01/13/the-new-kingmakers-how-developers-conquered-the-world/))

7. **Copy-paste-ability is an underrated DX superpower**
   "The best documentation has working code that developers can copy, paste, run, and see results immediately. Every extra step between reading the docs and seeing something work is a place where a developer might give up. Optimize for copy-paste-run, not for elegance."
   — *Orta Therox, Developer experience lead and former TypeScript team member at Microsoft* ([source](https://artsy.github.io/blog/2019/05/16/team-working-agreement/))

8. **Progressive disclosure prevents overwhelm**
   "The biggest mistake API companies make is showing developers everything at once. Great DX is about progressive disclosure — show the simplest thing first, let the developer succeed quickly, then reveal complexity as they need it. Your getting-started guide should be five steps, not fifty."
   — *Cristiano Betta, Developer experience advocate and API design consultant* ([source](https://betta.io/blog/2017/02/13/12-ways-to-improve-developer-experience/))

## Instructions

### Step 1: Map the Developer Journey

Walk through the entire developer journey from first discovery to production deployment, documenting every touchpoint. Complete the journey as a real developer would — do not skip steps or use insider knowledge.

**Journey stages to map:**

| Stage | What to Document |
|-------|-----------------|
| **Discovery** | How does a developer first learn this product exists? Google search results, landing page clarity, "what is this?" comprehension time |
| **Evaluation** | Can the developer understand what this does and whether it solves their problem within 60 seconds of landing? Is there a live demo, interactive playground, or video? |
| **Signup / Access** | How many steps from "I want to try this" to "I have an API key"? Are there unnecessary gates (required credit card, sales call, approval queue)? |
| **First API Call** | How long from "I have my key" to "I made a successful request and got a meaningful response"? This is the time-to-hello-world. |
| **Integration** | How well does the product fit into a developer's existing workflow? SDKs, package managers, framework integrations, CI/CD support. |
| **Production** | What does it take to go from prototype to production? Rate limits, SLAs, monitoring, billing transparency. |

For each stage, record: time spent, number of steps, points of confusion, moments of delight, and whether you had to leave the product's own ecosystem (e.g., searching Stack Overflow, reading source code).

**Artifact produced:** Developer Journey Map (a table with all six stages documented with timestamps and observations).

### Step 2: Measure Time-to-Hello-World

Perform a timed, clean-room test of the product's first-run experience. Use a fresh environment (new browser profile, no cached credentials, no prior knowledge beyond what the landing page provides).

**Measurement protocol:**
1. Start the timer when you first land on the product's homepage or documentation
2. Follow only the official getting-started guide — no shortcuts
3. Record every friction point: unclear instruction, missing prerequisite, broken link, ambiguous error, required context switch
4. Stop the timer when you receive a meaningful, successful response from the API or see the product's core value delivered

**Scoring rubric:**

| Time-to-Hello-World | Grade | Benchmark |
|---------------------|-------|-----------|
| Under 5 minutes | A | Stripe, Twilio — gold standard |
| 5-15 minutes | B | Acceptable for complex products |
| 15-30 minutes | C | Friction is costing you adoption |
| 30-60 minutes | D | Most developers will abandon before success |
| Over 60 minutes | F | Broken first-run experience |

Document the critical path (minimum steps to success) versus the actual path a new developer follows. The gap between these reveals unnecessary friction.

**Artifact produced:** Time-to-Hello-World Report (timed walkthrough, grade, critical path vs. actual path, and annotated friction log).

### Step 3: Assess Documentation Quality

Evaluate the product's documentation across six dimensions. Score each dimension 1-5 and provide specific evidence.

| Dimension | What to Evaluate | Score (1-5) |
|-----------|-----------------|-------------|
| **Completeness** | Does every endpoint/feature have documentation? Are there undocumented behaviors, parameters, or error codes? | |
| **Accuracy** | Do the code examples actually work when copied and run? Are the request/response schemas correct and up to date? | |
| **Discoverability** | Can a developer find the answer to their question within 2 minutes? Is there effective search, logical navigation, and cross-linking? | |
| **Copy-paste-ability** | Can code examples be copied and run with minimal modification? Do they include realistic values, not just `{placeholder}`? | |
| **Progressive disclosure** | Does the docs start simple and build complexity? Is there a clear getting-started path separate from the full reference? | |
| **Error documentation** | Are error codes documented with causes and remediation steps? Can a developer debug a failed request using only the docs? | |

For each dimension scoring 3 or below, provide a specific example of the problem and a concrete fix.

**Artifact produced:** Documentation Quality Scorecard (6 dimensions, scores, evidence, and recommendations).

### Step 4: Evaluate the Error Experience

Deliberately trigger errors and evaluate how well the product helps the developer recover. Test at least these error categories:

- **Authentication errors** — Invalid key, expired key, missing key, wrong header format
- **Validation errors** — Missing required fields, wrong types, out-of-range values
- **Rate limit errors** — What happens when limits are exceeded? Is there a Retry-After header?
- **Server errors** — 500s: is there a request ID for support? Is the error message helpful or generic?
- **Edge cases** — Empty inputs, very large inputs, unsupported formats, Unicode/special characters

**For each error encountered, evaluate:**

| Criterion | Question |
|-----------|----------|
| **Specificity** | Does the error message say exactly what went wrong? |
| **Actionability** | Does it tell the developer how to fix it? |
| **Consistency** | Do errors follow a consistent schema across all endpoints? |
| **Documentation link** | Does the error reference a docs page with more detail? |
| **HTTP semantics** | Are the status codes correct (e.g., 400 vs 422 vs 403)? |

**Artifact produced:** Error Experience Audit (table of triggered errors, messages received, scores on each criterion, and recommended improvements).

### Step 5: Score the Friction Scorecard

Using findings from Steps 1-4, produce a composite friction scorecard. Score each category 1-10 (10 = frictionless).

| Category | Score (1-10) | Weight | Weighted Score | Key Finding |
|----------|-------------|--------|---------------|-------------|
| Discovery and evaluation | | 10% | | |
| Signup and access | | 10% | | |
| Time-to-hello-world | | 25% | | |
| Documentation quality | | 20% | | |
| Error experience | | 15% | | |
| SDK and integration support | | 10% | | |
| Production readiness | | 10% | | |
| **Overall DX Score** | | **100%** | | |

The weighting reflects that time-to-hello-world and documentation quality are the two highest-leverage areas for developer adoption. Adjust weights if the product's stage warrants it (e.g., a pre-launch product should weight discovery lower).

**Grading thresholds:**
- **80-100:** Best-in-class DX (Stripe, Twilio tier)
- **60-79:** Good DX with clear improvement areas
- **40-59:** Significant friction reducing adoption
- **Below 40:** DX is actively deterring developers

**Artifact produced:** Friction Scorecard (weighted scores across all categories with an overall DX grade).

### Step 6: Build the Prioritized DX Improvement Roadmap

From all friction points identified in Steps 1-5, build a prioritized improvement backlog. Rank each improvement by impact and effort.

**Prioritization framework:**

| Priority | Impact | Effort | Examples |
|----------|--------|--------|----------|
| **P0 — Fix now** | High | Low | Broken code examples, missing error messages, dead links in getting-started guide |
| **P1 — Fix this quarter** | High | Medium | Rewrite getting-started guide, add SDK for popular language, improve error schemas |
| **P2 — Plan for next quarter** | Medium | Medium-High | Interactive API explorer, comprehensive error code reference, community examples |
| **P3 — Backlog** | Low-Medium | High | Full SDK coverage for all languages, video tutorials, developer community forum |

For each item, specify:
- The friction point it addresses (reference the step where it was identified)
- The expected impact on time-to-hello-world or the friction scorecard
- The estimated effort (T-shirt size: S/M/L/XL)
- The owner or team responsible

**Artifact produced:** DX Improvement Roadmap (prioritized table of improvements with impact, effort, and ownership).

### Step 7: Compile the DX Audit Report

Assemble all artifacts from Steps 1-6 into a single executive-ready document:

1. Executive Summary (one paragraph: overall DX grade, top 3 strengths, top 3 weaknesses)
2. Developer Journey Map (Step 1)
3. Time-to-Hello-World Report (Step 2)
4. Documentation Quality Scorecard (Step 3)
5. Error Experience Audit (Step 4)
6. Friction Scorecard (Step 5)
7. DX Improvement Roadmap (Step 6)
8. Recommended immediate actions (top 3 things to fix this week)

**Artifact produced:** Complete DX Audit Report saved as `applied/dx-audit-{product}.md`.

## Diagnostic Questions

1. **Can a developer go from zero to a successful API call in under 5 minutes using only your documentation?** If you are unsure, you have not tested it recently enough. Run the time-to-hello-world test yourself on a fresh machine.

2. **What happens when a developer makes their first mistake?** The error experience at the moment of first failure is the single highest-leverage DX surface. If your error messages say "Bad Request" with no further detail, developers will leave.

3. **How many tabs does a developer need open to complete the getting-started guide?** If the answer is more than two (your docs + their code editor), your documentation has a self-containment problem.

4. **Do your code examples actually work when copied and pasted?** Test them quarterly. Code examples rot faster than any other form of documentation because they depend on API versions, SDK versions, and environment assumptions that change constantly.

5. **Where do developers get stuck, and how do you know?** If you cannot answer this with data (support tickets, analytics, user session recordings), you are guessing about your DX problems instead of measuring them.

6. **Is your getting-started guide optimized for the 80th-percentile developer or the 20th?** Most getting-started guides are written by experts for experts. The developers who need the guide most are the ones who know the least about your product.

7. **What is the last DX improvement you shipped, and when?** If you cannot remember, DX has become an afterthought. Developer experience degrades by default — it requires continuous investment.

## Common Mistakes

1. **Auditing from the insider perspective**
   The most common mistake is evaluating DX as someone who already understands the product. Insider knowledge masks friction that new developers experience acutely. Always test with a clean-room setup: fresh browser, no cached credentials, no context beyond what the public documentation provides. Ideally, have someone outside the team run the audit.

2. **Optimizing the reference docs before the getting-started guide**
   Teams often invest heavily in comprehensive API references while neglecting the getting-started guide. But developers encounter the getting-started guide first, and if they bounce there, the reference docs never get read. Fix the first 5 minutes before polishing the encyclopedia.

3. **Treating documentation as a one-time deliverable**
   Documentation rots. Code examples break when APIs change. Getting-started guides accumulate steps as new prerequisites are added. Links die. Treating docs as "done" guarantees that DX degrades over time. Build a recurring audit cadence — monthly for code examples, quarterly for the full journey.

4. **Ignoring the error experience**
   Error messages are the interface developers interact with most frequently during integration, yet they receive the least design attention. A developer who encounters a clear, actionable error message builds trust. A developer who encounters "Internal Server Error" three times in a row files a support ticket or switches to a competitor.

5. **Measuring success by API call volume instead of time-to-value**
   High API call volume can mask terrible DX — developers may be making many calls because the API is confusing, not because they are productive. Time-to-hello-world and activation rate (percentage of developers who reach a successful outcome) are better leading indicators of DX health than raw volume.

6. **Building SDKs for every language before perfecting the HTTP experience**
   SDKs are expensive to build and maintain. If the raw HTTP experience is poor (bad error messages, inconsistent schemas, unclear auth), SDKs will paper over problems without fixing them. Get the HTTP API right first, then invest in SDKs for the top 2-3 languages your developers actually use.

## Context Integration

This skill uses the `context/` directory to ground the audit in the specific product and competitive landscape:

| Context Directory | Steps Used In | What It Provides |
|---|---|---|
| `context/products/` | Steps 1, 2, 3, 5 | Product descriptions, API endpoint lists, pricing tiers, and technical architecture. Provides the product surface area to audit and helps identify which endpoints and flows to prioritize in the time-to-hello-world test. |
| `context/competitive/` | Steps 2, 5, 6 | Competitor DX benchmarks. If competitor products have been audited, their time-to-hello-world and friction scores provide calibration points for grading and help prioritize improvements that close competitive DX gaps. |
| `context/verticals/` | Steps 1, 6 | Target developer segments and their use cases. Different verticals have different DX expectations (game developers tolerate more complexity than web developers). Vertical context helps calibrate the friction scorecard weights and prioritize roadmap items by segment. |
| `context/company/` | Steps 6, 7 | Team size, engineering resources, and product stage. Informs the effort estimates and prioritization in the DX improvement roadmap — a 5-person team gets a different P0 list than a 50-person team. |
| `context/founders/` | Step 7 | Founder and leadership priorities. Helps frame the executive summary in terms that resonate with decision-makers and align DX recommendations with stated company strategy. |
| `context/signals/` | Steps 1, 4, 6 | Auto-collected signals from GitHub issues, HN discussions, Reddit threads, and developer community sentiment. [SIGNAL] tagged. Use `github-ecosystem.md` for open issues and developer complaints that reveal DX friction points. Use `reddit-discussions.md` and `hackernews-sentiment.md` for unfiltered developer sentiment about the product's DX. Check freshness before citing. |

If no `context/` directory is present, the skill will ask the user to provide:
1. The name and URL of the API or developer product to audit
2. A link to the product's documentation
3. The primary developer audience (e.g., web developers, data scientists, game developers)
4. Any known DX pain points or recent developer feedback
