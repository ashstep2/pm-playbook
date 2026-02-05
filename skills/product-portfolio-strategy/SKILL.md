---
name: product-portfolio-strategy
description: "Help users define and prioritize a multi-product portfolio by mapping product surfaces, allocating resources across bets, and designing a sequenced roadmap."
---

# Product Portfolio Strategy

Produces a multi-product roadmap with resource allocation across bets, sequencing logic, and kill criteria — for companies managing more than one product surface simultaneously.

## Core Principles

1. **Manage a portfolio of bets, not a single product roadmap**
   "The best product leaders think in portfolios. You need horizon 1 (core business), horizon 2 (emerging bets), and horizon 3 (options on the future). Most teams over-invest in H1 and starve H2/H3."
   — *Shreyas Doshi, former PM at Stripe/Twitter/Google* ([Lenny's Podcast](https://www.lennysnewsletter.com/p/the-art-of-decision-making-shreyas))

2. **Sequence by learning, not by revenue**
   "At the earliest stages, your job is to maximize the rate of learning, not the rate of revenue. Sequence your bets to answer the biggest unknowns first."
   — *Rahul Vohra, CEO of Superhuman* ([First Round Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit))

3. **Every product surface must have a clear job**
   "Each product you ship should have a crisp answer to: what job does this do in the portfolio? Is it an acquisition engine, a monetization engine, a retention engine, or a platform play?"
   — *Gibson Biddle, former VP Product at Netflix* ([Lenny's Podcast](https://www.lennysnewsletter.com/p/the-dhm-model))

4. **Kill criteria prevent zombie products**
   "The hardest product decision is what NOT to do. Define kill criteria upfront — the conditions under which you'll shut something down — or you'll end up with a portfolio of zombie products draining resources."
   — *Marty Cagan, SVPG* ([Inspired](https://www.svpg.com/inspired-how-to-create-tech-products-customers-love/))

5. **Spatial intelligence is a platform, not a feature**
   "The whole history of deep learning is in some sense the history of scaling up compute. We believe spatial intelligence is the next frontier — and it requires thinking in platforms, not products."
   — *Justin Johnson, Co-Founder of World Labs* ([Latent Space Podcast](https://open.spotify.com/episode/50zuUtx9QeEcaBA63slq8w))

6. **Consumer and developer products are symbiotic**
   "The most powerful platform companies run both a consumer product and a developer product. The consumer product generates demand and validates the technology. The developer product captures the long tail and builds the ecosystem."
   — *Elad Gil, Author of High Growth Handbook* ([High Growth Handbook](https://press.stripe.com/high-growth-handbook))

7. **Resource allocation reveals actual strategy**
   "Strategy is what you do, not what you say. If you want to know a company's real strategy, look at where they allocate engineers and budget. Everything else is aspiration."
   — *Ben Horowitz, Andreessen Horowitz* ([The Hard Thing About Hard Things](https://a16z.com/books/the-hard-thing-about-hard-things/))

8. **Cross-surface feedback loops are your competitive moat**
   "When your consumer product generates training data that improves your API, which powers your partners, who bring users back to your consumer product — that's a flywheel. That's the moat."
   — *Casey Winters, former Growth Lead at Pinterest/Grubhub* ([Reforge](https://www.reforge.com/blog/growth-loops))

## Instructions

### Step 1: Map Current Product Surfaces
- List every product the company ships or is building (consumer apps, APIs, SDKs, open-source tools, enterprise offerings)
- For each surface, document: target user, pricing model, current stage (concept/alpha/beta/GA), team size, revenue/usage metrics
- Check `context/products/` if available for existing product analyses
- **Output:** Product surface inventory table

### Step 2: Define the Job of Each Surface
- For each product surface, answer: What job does this do in the portfolio?
  - **Acquisition engine** — brings new users/developers into the ecosystem
  - **Monetization engine** — generates revenue
  - **Retention engine** — keeps users engaged and prevents churn
  - **Platform play** — enables third parties to build on top
  - **Learning engine** — generates data/insights that improve other surfaces
- Identify surfaces with unclear or overlapping jobs
- **Output:** Portfolio job matrix

### Step 3: Assess Cross-Surface Feedback Loops
- Map how each product surface feeds the others (data flows, user flows, technology flows)
- Identify the strongest loop (the flywheel) and the weakest links
- Score each feedback loop: Strong (proven), Emerging (showing signs), Theoretical (hoped-for)
- **Output:** Cross-surface feedback loop diagram with strength ratings

### Step 4: Classify Bets by Horizon
- Assign each product surface to a horizon:
  - **H1 (Core):** Generating revenue/users today, needs optimization
  - **H2 (Growth):** Showing early traction, needs investment to scale
  - **H3 (Exploration):** Unproven, needs experimentation to validate
- Check `context/competitive/` for competitive pressure that may shift priorities
- **Output:** Horizon classification with rationale

### Step 5: Allocate Resources
- Propose a resource allocation across horizons (typical healthy split: 60-70% H1, 20-30% H2, 5-10% H3)
- For each surface, specify: team headcount, engineering investment, strategic priority (primary/secondary/experimental)
- Flag any surface that's over-invested or starved relative to its horizon
- **Output:** Resource allocation proposal with trade-off analysis

### Step 6: Define Kill Criteria and Success Metrics
- For each H2 and H3 bet, define:
  - **Success criteria:** What signals would justify doubling down? (specific metrics + thresholds)
  - **Kill criteria:** What signals would trigger shutting it down or pivoting? (specific metrics + timeframes)
  - **Review cadence:** How often to evaluate (monthly/quarterly)
- **Output:** Kill criteria table

### Step 7: Produce Sequenced Roadmap
- Sequence product investments across a 6-12 month timeline
- Identify dependencies between surfaces (e.g., "API needs to be stable before enterprise launch")
- Mark decision points where the portfolio strategy should be re-evaluated based on kill criteria
- Check `context/verticals/` for market timing considerations
- **Output:** Sequenced portfolio roadmap with decision gates

## Diagnostic Questions

1. How many distinct product surfaces does the company currently ship or plan to ship?
2. Can you articulate the specific job each product surface does in the portfolio?
3. Is there a feedback loop between your consumer product and your developer product? How strong is it?
4. What percentage of engineering resources goes to each product surface?
5. Do you have explicit kill criteria for any of your bets?
6. When was the last time the company killed or deprioritized a product surface?
7. Are any product surfaces competing with each other for the same users?
8. What's the biggest unknown that, if answered, would change your entire portfolio strategy?

## Common Mistakes

1. **Peanut-butter spreading** — Distributing resources equally across all surfaces instead of making hard bets. A 41-person company cannot meaningfully staff 4 product surfaces. Pick 1-2 to win, resource the rest for learning only.

2. **Confusing consumer traction with platform strategy** — A popular consumer app doesn't automatically become a platform. Platform value comes from enabling third parties, not from first-party usage.

3. **No kill criteria** — Without explicit conditions for shutting down a bet, every product becomes a zombie. The cost of maintaining an unfocused portfolio is invisible until it's crushing.

4. **Ignoring the cross-surface flywheel** — Treating each product as independent when the real value comes from how they feed each other. Map the loops or you'll optimize surfaces in isolation.

5. **Over-indexing on competition** — Launching a product surface because a competitor did, rather than because it serves your portfolio strategy. Reactive portfolio moves are almost always wrong.

## Context Integration

How this skill uses the `context/` directory when available:
- `context/products/` → Product surface inventory and current metrics
- `context/company/` → Team size and resource constraints
- `context/competitive/` → Competitive pressure on each surface
- `context/verticals/` → Market timing for sequencing decisions
- `context/founders/` → Strategic vision and founder priorities for alignment

If no context/ directory exists, the skill asks the user for product surface details, team size, and strategic priorities.
