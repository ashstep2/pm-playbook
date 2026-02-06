---
name: zero-to-one-product-launch
description: "Help users plan and execute a 0-to-1 product launch with a launch checklist, channel strategy, success metrics, and rollback plan."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Zero-to-One Product Launch

Produces a complete launch plan for a brand-new product — from positioning brief through channel strategy, success metrics with thresholds, rollback/pivot criteria, and a post-launch retrospective framework — tailored to the unique challenge of launching something that has no existing users, no existing distribution, and an unproven value proposition.

## Core Principles

1. **Position deliberately before you launch**
   "Positioning is the act of deliberately defining how you are the best at something that a defined market cares a lot about."
   — *April Dunford, B2B positioning consultant and author of Obviously Awesome* ([source](https://www.goodreads.com/en/book/show/45166937))

   For 0-to-1 launches, positioning cannot be an afterthought. You have no existing market perception to lean on. Your positioning thesis will be wrong in places — write it down anyway, then treat it as a hypothesis to validate in the first 30 days.

2. **Work backwards from the customer**
   "We innovate by starting with the customer and working backwards. That becomes the touchstone for how we invent."
   — *Jeff Bezos, Founder of Amazon* ([source](https://quotefancy.com/quote/1093271/Jeff-Bezos-We-innovate-by-starting-with-the-customer-and-working-backwards-That-becomes))

   Write the press release before you write the launch plan. If you cannot articulate who the customer is and why they care in a single page, the launch will not land. The Working Backwards PR/FAQ process forces clarity before execution.

3. **Launch before you are ready**
   "If you are not embarrassed by the first version of your product, you've launched too late."
   — *Reid Hoffman, Co-founder of LinkedIn* ([source](https://x.com/reidhoffman/status/847142924240379904))

   The cost of launching late always exceeds the cost of launching imperfect. In a 0-to-1 context, every week without real users is a week of building on assumptions. Ship the minimum remarkable product and learn from contact with reality.

4. **Build something 100 people love**
   "Build something 100 people love, not something 1 million people kind of like."
   — *Brian Chesky, Co-founder and CEO of Airbnb, citing advice from Paul Graham* ([source](https://www.brainyquote.com/quotes/brian_chesky_529560))

   New products fail when they try to serve everyone on day one. Identify your beachhead segment — the 100 people with the most acute version of the problem — and build obsessively for them. Breadth comes after depth.

5. **Do things that don't scale**
   "It's not enough just to do something extraordinary initially. You have to make an extraordinary effort initially."
   — *Paul Graham, Co-founder of Y Combinator* ([source](https://paulgraham.com/ds.html))

   At launch, your growth engine is manual. Personally onboard users. Hand-write welcome emails. Do the Collison installation — when someone agrees to try your product, set them up on the spot. These unscalable acts generate the signal you need to know what scales.

6. **Sell the transformation, not the product**
   "What we are selling is not the software product — the set of all the features, in their specific implementation — because there are just not many buyers for this software product."
   — *Stewart Butterfield, Co-founder of Slack, from the internal memo "We Don't Sell Saddles Here"* ([source](https://medium.com/@stewart/we-dont-sell-saddles-here-4c59524d650d))

   Especially for developer products: you are not launching an API. You are launching the capability that API unlocks. Frame every launch message around what the user can now do, not what you built.

7. **Validate with the Build-Measure-Learn loop**
   "The fundamental activity of a startup is to turn ideas into products, measure how customers respond, and then learn whether to pivot or persevere."
   — *Eric Ries, Author of The Lean Startup* ([source](https://theleanstartup.com/principles))

   A 0-to-1 launch is not a single event — it is the first iteration of a feedback loop. Define what you are measuring before you ship so you know whether the signal says "double down" or "change course."

8. **Create buzz worth remarking about**
   "I spent the past few weeks collecting and categorizing the buzziest launches I could find. You'll find the ten most common strategies for launching something worth remarking about."
   — *Lenny Rachitsky, Author of Lenny's Newsletter* ([source](https://www.lennysnewsletter.com/p/creating-buzz-at-launch-preview))

   For a brand-new product with no existing distribution, your launch moment is your one shot at concentrated attention. Invest in making it remarkable — a compelling demo, an unexpected angle, a constraint that becomes a story. But remember: buzz without retention is waste.

9. **Start before you feel ready**
   "Start before you feel ready. Start today."
   — *Sahil Lavingia, Founder of Gumroad and author of The Minimalist Entrepreneur* ([source](https://www.amazon.com/Minimalist-Entrepreneur-Great-Founders-More/dp/0593192397))

   For 0-to-1 products, perfectionism is the enemy. Scope down to the smallest version that solves one real problem for one real person. Ship it to that person. Then iterate.

## Instructions

### Step 1: Write the Launch Brief (the "Working Backwards" document)

Before any tactical planning, produce a one-page launch brief that answers:

- **Who is the customer?** Name the specific beachhead segment. Not "developers" — which developers, building what, blocked by what?
- **What can they do now that they could not do before?** One sentence. This is the transformation, not the feature list.
- **Why should they care today?** What is the urgency or catalyst? A pain point that just got worse, a new capability that just became possible, a competitor gap.
- **What does success look like in 30 days?** A single leading indicator.
- **What is the one-line positioning statement?** Use April Dunford's format: "For [target customer] who [need], [product] is a [category] that [key differentiator]."

**Output:** A launch brief document (1-2 pages) saved as `applied/launch-brief-{product}.md`.

If `context/products/` files exist, pull the product description and pricing from there. If `context/verticals/` files exist, pull the beachhead segment and use cases from there.

### Step 2: Map the Channel Strategy

Identify 3-5 launch channels and rank them by expected signal quality (not reach). For each channel, define:

| Channel | Why this channel for day-one | Target action | Expected volume | Cost |
|---------|------------------------------|---------------|-----------------|------|
| e.g., Targeted developer Discord communities | High-intent builders already discussing the problem space | Sign up and generate first world | 50-100 sign-ups | $0 (time) |

**Channel categories to evaluate:**

- **Owned channels:** Product Hunt, your blog/changelog, email list, social accounts, documentation site
- **Community channels:** Discord servers, Slack groups, Reddit communities, Hacker News, Twitter/X developer circles
- **Partner channels:** Integration partners, ecosystem players, launch partners with overlapping audiences
- **Content channels:** Demo video, tutorial, live stream, guest post on a high-traffic blog
- **Developer-specific channels:** GitHub (README, examples repo, awesome list), Stack Overflow, dev.to, documentation-first launch (ship the docs before the product)

**For developer/API product launches specifically:**
- Lead with documentation, not marketing. The docs page IS your landing page.
- Ship a working code example alongside the announcement. Developers evaluate products by trying them, not by reading about them.
- Provide a free tier or generous trial credits so the first experience has zero friction.
- Consider a "build in public" pre-launch to generate anticipation among early adopters.

**Output:** A channel strategy table with timing (pre-launch, launch day, post-launch week 1).

### Step 3: Define Success Metrics with Thresholds

Define 4-6 metrics across three tiers. Every metric must have a concrete threshold for "on track," "concerning," and "pivot trigger."

**Tier 1 — Activation (Day 1-7):**
- Sign-ups or API key creations
- First meaningful action (e.g., first API call, first world generated, first project created)
- Time-to-first-value (from sign-up to "aha moment")

**Tier 2 — Engagement (Day 7-30):**
- Return usage rate (% of activated users who come back in week 2)
- Depth of usage (e.g., number of API calls per user, number of projects created)
- Organic sharing or referral signals

**Tier 3 — Signal (Day 30-90):**
- Retention rate (weekly or monthly, depending on expected usage cadence)
- Net Promoter Score or qualitative sentiment
- Conversion to paid (if applicable)
- Inbound interest from outside the beachhead segment

For each metric, produce a table:

| Metric | On Track | Concerning | Pivot Trigger |
|--------|----------|------------|---------------|
| Week 1 sign-ups | >200 | 50-200 | <50 |
| Time-to-first-value | <10 min | 10-30 min | >30 min |

**Output:** A metrics scorecard with thresholds, saved as part of the launch plan.

### Step 4: Build the Launch Checklist

Produce a time-sequenced checklist organized into three phases:

**T-minus 2 weeks (Pre-launch):**
- [ ] Launch brief reviewed and approved by key stakeholders
- [ ] Positioning statement tested with 5+ people in the target segment
- [ ] Documentation complete and reviewed for first-run experience
- [ ] Demo/sample project built and tested end-to-end
- [ ] Success metrics and thresholds agreed upon
- [ ] Monitoring and alerting set up (error rates, latency, capacity)
- [ ] Support channel established (Discord, email, in-app)
- [ ] Rollback plan documented and tested
- [ ] Launch assets prepared (blog post, demo video, social posts, code examples)
- [ ] Beta testers briefed and ready to provide day-one signal

**T-zero (Launch day):**
- [ ] Announce on primary channel
- [ ] Cross-post to secondary channels with 2-4 hour spacing
- [ ] Monitor error rates and support channels in real-time
- [ ] Respond to every early piece of feedback within 2 hours
- [ ] Share early wins and user stories on social channels
- [ ] Track activation funnel in real-time dashboard

**T-plus 1 week (Post-launch):**
- [ ] First metrics review against scorecard thresholds
- [ ] Synthesize qualitative feedback into themes
- [ ] Prioritize top 3 friction points for immediate fixes
- [ ] Reach out personally to highest-engagement users
- [ ] Publish a "what we learned in week 1" update (internal or external)
- [ ] Decide: accelerate, iterate, or investigate

**Output:** A markdown checklist with owners and dates assigned.

### Step 5: Write the Rollback and Pivot Plan

A 0-to-1 launch carries existential uncertainty. Before launching, document:

**Rollback triggers (technical):**
- Error rate exceeds X% for Y minutes
- P0 data integrity or security issue discovered
- Infrastructure cost exceeds Z budget threshold

**Rollback procedure:**
- How to disable public access without data loss
- Communication template for users if rollback is needed
- Timeline for re-launch after rollback

**Pivot triggers (product/market):**
- Activation rate below pivot threshold for 2 consecutive weeks
- Qualitative feedback reveals a fundamental misunderstanding of the value proposition
- Beachhead segment shows no organic sharing or word-of-mouth

**Pivot options (pre-defined):**
- Reposition for a different segment (keep product, change audience)
- Reduce scope to the single most-loved feature (keep audience, change product)
- Change the business model (keep product and audience, change pricing/packaging)
- Sunset and apply learnings to next product

**Output:** A rollback and pivot plan document with clear trigger conditions and pre-agreed actions.

### Step 6: Design the Post-Launch Retrospective Framework

Schedule the retrospective for 30 days post-launch. Define the structure now so the team knows what data to collect:

**Retrospective agenda:**

1. **Metrics review** — Walk through the scorecard. Which thresholds did we hit? Which did we miss? What surprised us?
2. **Positioning audit** — Did users describe the product the way we positioned it? Pull exact quotes from support tickets, social mentions, and feedback forms. Where positioning and perception diverge, positioning needs to change.
3. **Channel effectiveness** — For each launch channel, report: impressions, click-through, sign-ups, activations, cost. Identify the top 2 channels by signal quality (not volume).
4. **Qualitative synthesis** — Group feedback into: "love" (keep), "confused by" (clarify), "want next" (roadmap signal), "blocked by" (fix immediately).
5. **Decision** — Based on the above, declare one of: Scale (invest more in what is working), Iterate (fix the top 3 issues and re-measure in 2 weeks), Pivot (trigger the pivot plan), or Sunset (stop and redirect resources).

**Output:** A retrospective template with pre-filled sections and instructions for data collection.

### Step 7: Compile the Full Launch Plan

Assemble all artifacts from Steps 1-6 into a single launch plan document:

1. Launch Brief (from Step 1)
2. Channel Strategy (from Step 2)
3. Success Metrics Scorecard (from Step 3)
4. Launch Checklist (from Step 4)
5. Rollback and Pivot Plan (from Step 5)
6. Retrospective Framework (from Step 6)

**Output:** A complete launch plan saved as `applied/launch-plan-{product}.md`.

## Diagnostic Questions

Ask these before beginning the launch plan to calibrate the approach:

1. **Who are the first 10 users?** Can you name them? If not, you are not ready to plan a launch — you need customer discovery first. Use the `customer-discovery` skill.

2. **What is the single action that proves value?** If a user does one thing with your product, what is it? If you cannot answer this, scope the product down until you can.

3. **Does the product work end-to-end today?** A launch plan for something that does not yet work is a distraction. If the answer is no, finish building, then return.

4. **How will users find you without paid acquisition?** If the only path to users is paid ads, the value proposition may not be strong enough to generate organic pull. Reconsider positioning.

5. **What is the competitive alternative?** Not "who are your competitors" — what does the target user do today to solve this problem? Your launch message must be framed against this alternative, not against your product's feature set.

6. **What would make you pull the product from the market after launch?** If you do not have a clear answer, write the rollback plan now.

7. **Is this a developer product?** If yes, the launch plan must lead with documentation, working code examples, and a zero-friction first experience. Marketing copy is secondary to a great `README.md`.

## Common Mistakes

1. **Launching to everyone instead of someone**
   A 0-to-1 product has no brand equity, no word-of-mouth, and no distribution. Launching broadly means your message reaches many people weakly instead of a few people powerfully. Pick one beachhead segment and go deep. Breadth is a Series B problem.

2. **Confusing launch day with product-market fit**
   A successful launch day (traffic spike, sign-ups, press coverage) tells you almost nothing about whether the product will survive. The real signal comes in week 2-4: do people come back? Treat launch day as the start of measurement, not the finish line.

3. **Skipping the rollback plan**
   First launches carry the highest risk of unexpected technical failure, reputational damage, or cost overruns. Teams skip rollback planning because it feels pessimistic. In reality, having a plan makes you more willing to launch boldly because you know you can recover.

4. **Optimizing for vanity metrics**
   Sign-ups, page views, and social impressions are easy to measure and feel good. But for a 0-to-1 product, the only metric that matters early is activation: did the user complete the core action that proves value? Measure that first, everything else second.

5. **Launching the feature list instead of the transformation**
   New products fail when they describe themselves in terms of what they are ("an API for generating 3D environments") instead of what they enable ("turn a text description into a navigable 3D world in 30 seconds"). Lead with the outcome, especially in developer marketing.

6. **Waiting for perfect documentation before shipping**
   Documentation is critical for developer products — but "perfect" documentation for a product that has not been used by real users is documentation built on assumptions. Ship good-enough docs, then rewrite the top 3 friction points after real users get stuck.

## Context Integration

This skill uses the `context/` directory to accelerate and ground the launch plan:

- **`context/products/`** — Pulls the product description, pricing tiers, key capabilities, and technical architecture to populate the launch brief (Step 1) and shape the positioning statement. If product files exist, the skill uses them directly rather than asking the user to describe the product.

- **`context/verticals/`** — Pulls target market information (TAM/SAM/SOM, key players, use cases, adoption barriers) to identify the beachhead segment in the launch brief (Step 1) and to prioritize launch channels in the channel strategy (Step 2). Each vertical file maps to a potential beachhead; the skill recommends starting with the vertical that has the shortest path to activation.

- **`context/competitive/`** — Pulls the competitive landscape and per-competitor analyses to inform the "competitive alternative" framing in the positioning statement (Step 1) and to calibrate success metric thresholds (Step 3). If a competitor recently launched a similar product, the metrics thresholds should reflect the need to establish differentiation quickly.

- **`context/founders/`** — Pulls key themes and attributed quotes from leadership to ensure the launch messaging aligns with the company's stated mission and values.

- **`context/company/`** — Pulls company stage, funding, and team composition to calibrate the ambition of the launch plan. A 10-person seed-stage company gets a different channel strategy than a 200-person Series C company.

If no `context/` directory exists, the skill prompts the user with the diagnostic questions (above) to gather the minimum required context before proceeding.
