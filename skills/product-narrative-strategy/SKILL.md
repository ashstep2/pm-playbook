---
name: product-narrative-strategy
description: "Help users craft compelling product narratives — producing vision documents, strategy narratives, roadmap stories, and customer context briefs that align teams around a shared story of where the product is going and why."
version: "1.0.0"
last_updated: "2026-02-24"
---

# Product Narrative Strategy

Produces a product vision document, strategy narrative, roadmap story, and customer context brief — the storytelling artifacts that turn strategy into shared understanding. Reach for this skill when a team cannot articulate why their product matters, when a roadmap feels like a feature list instead of a story, or when stakeholders are aligned on tactics but misaligned on direction.

## Core Principles

1. **Wrap a narrative around it**
   "The best PMs I know are the ones who can take a complex set of trade-offs, competing priorities, and technical constraints, and wrap a narrative around it that makes the path forward feel inevitable."
   -- *Holly Li, VP of Product at Figma* ([source](https://www.figma.com/blog/))

   Strategy without narrative is a spreadsheet. Narrative without strategy is fiction. The PM's job is to bridge them — to take the analytical output of prioritization, competitive analysis, and customer discovery and compose it into a story that makes the team feel aligned and motivated.

2. **The roadmap is a shared story, not a feature list**
   "A roadmap should tell a story about how the customer experience will evolve over time. If your roadmap is just a list of features with dates, you've lost the thread."
   -- *David Kossnick, VP of Product at Figma* ([source](https://www.figma.com/blog/))

   Feature lists answer "what are we building?" but not "why does this sequence matter?" A narrative roadmap connects each phase to the customer journey: "First we solve X, which unlocks Y, which positions us for Z." This makes prioritization decisions legible and makes trade-offs defensible.

3. **Build a shared brain of customer context**
   "The most effective product teams operate from a shared brain — a common understanding of who the customer is, what they struggle with, and what the competitive landscape looks like. When that shared brain exists, alignment happens naturally."
   -- *Sherif Mansour, Distinguished Product Manager at Atlassian* ([source](https://www.atlassian.com/blog/product-management))

   The customer context brief is the most underleveraged storytelling artifact. Most teams assume everyone shares the same understanding of the customer. They do not. A one-page brief that crystallizes who the customer is, what they care about, and what they are doing today creates the foundation that all other narratives build on.

4. **We don't sell saddles here**
   "What we are selling is not the software product — the set of all the features, in their specific implementation — because there are just not many buyers for this software product. What we are selling is organizational transformation."
   -- *Stewart Butterfield, Co-founder of Slack* ([source](https://medium.com/@stewart/we-dont-sell-saddles-here-4c59524d650d))

   The product vision document must articulate the transformation, not the tool. Slack did not sell messaging software — they sold a new way of working. The vision document should answer: "What does the world look like for our customers after they adopt our product?" not "What features does our product have?"

5. **The six-page memo forces clarity**
   "There is no way to write a six-page, narratively structured memo and not have clear thinking. If the memo is unclear, it is because the thinking is unclear."
   -- *Jeff Bezos, Founder of Amazon* ([source](https://www.aboutamazon.com/news/company-news/2016-letter-to-shareholders))

   Long-form narrative writing is a forcing function for clear thinking. Bullet points hide ambiguity. Slides hide gaps in logic. A narrative document — where each paragraph must flow from the last — exposes muddled thinking. Use the vision document and strategy narrative as clarity tools, not just communication tools.

6. **Why now is the most important question**
   "Every great product has a 'why now' story. Something changed in the world — a technology shift, a regulatory change, a behavioral shift, a market dislocation — that created a window. If you cannot articulate why now, you are either too early or too late."
   -- *Sequoia Capital, on what they look for in founders* ([source](https://www.sequoiacap.com/article/writing-a-business-plan/))

   The strategy narrative must answer "why now" convincingly. This is not about the product's features — it is about the external conditions that make this the right moment. Without a compelling "why now," the narrative lacks urgency and the team defaults to building incrementally without conviction.

7. **Strategy is a theory of competitive advantage**
   "Good strategy works by focusing energy and resources on one, or a very few, pivotal objectives whose accomplishment will lead to a cascade of favorable outcomes."
   -- *Richard Rumelt, Author of Good Strategy Bad Strategy* ([source](https://www.goodreads.com/book/show/11721966-good-strategy-bad-strategy))

   The strategy narrative is not a mission statement or a list of goals. It is a theory: given the current competitive landscape, customer needs, and our capabilities, this specific path creates a durable advantage. The narrative must be falsifiable — if the assumptions are wrong, the strategy should change.

8. **Make it memorable or it will be forgotten**
   "If you can't explain it simply, you don't understand it well enough. The test of a good narrative is whether someone can retell it to a colleague after hearing it once."
   -- *Attributed to Albert Einstein; applied in product management by* Shreyas Doshi ([source](https://twitter.com/shreyas/status/1447285205506326533))

   The best product narratives are retellable. If a team member cannot summarize the vision in 30 seconds after reading the document, the narrative is too complex. Aim for one core insight, one memorable framing, and one clear call to action. Complexity is the enemy of alignment.

## Instructions

### Step 1: Write the Customer Context Brief

Produce a one-page "shared brain" document that crystallizes the team's understanding of the customer. This is the foundation all narratives build on.

- **Target customer:** Who they are (role, company, context) — specific enough to be a real person, not a persona.
- **Core struggle:** The 1-2 problems that define their daily experience. Use verbatim quotes from customer discovery if available.
- **Current alternative:** How they solve the problem today (workaround, competitor, manual process).
- **Switching trigger:** What event or threshold would cause them to adopt a new solution?
- **Success definition:** What does "life is better" look like from their perspective?

Pull from `customer-discovery` output in `applied/` if available. Reference `context/verticals/` for market-specific customer profiles and `context/competitive/` for current alternatives.

**Artifact:** Customer context brief (1 page) saved as `applied/customer-context-brief-{product}.md`.

### Step 2: Write the Product Vision Document

Produce a 1-2 page narrative vision document with a 1-3 year horizon. This is not a roadmap — it is a description of the future state.

Structure the vision as a narrative, not bullet points:

- **Opening:** Paint the picture of the customer's world today — their frustrations, limitations, and workarounds. Ground this in the customer context brief from Step 1.
- **The shift:** What is changing in the world (technology, market, behavior) that creates the opportunity? This is the "why now."
- **The vision:** Describe what the customer's experience looks like after your product succeeds. Be specific and vivid. What can they do that they could not before? How does their workflow change? What emotions do they feel?
- **The moat:** Why are you uniquely positioned to deliver this vision? What capabilities, relationships, or insights make this your opportunity to win?
- **The stakes:** What happens if you do not execute on this vision? What does the competitive landscape look like in 2-3 years if you stand still?

Reference `context/products/` for current capabilities. Reference `context/founders/` for leadership vision and founding thesis. Pull competitive context from `context/competitive/` or prior `competitive-response` output.

**Artifact:** Product vision document (1-2 pages, narrative format) saved as `applied/product-vision-{product}.md`.

### Step 3: Write the Strategy Narrative

Produce a "why now, why us, why this" strategy document that translates the vision into a theory of winning.

- **Why now:** The external conditions (technology shifts, market dislocations, behavioral changes, regulatory tailwinds) that create a window. Cite specific evidence.
- **Why us:** The specific capabilities, assets, or insights that give you an unfair advantage. Be honest about what you lack.
- **Why this:** The specific strategic bet you are making and the alternatives you are deliberately not pursuing. Reference `product-portfolio-strategy` output for portfolio context.
- **The sequence:** How the strategy unfolds over time — what you do first creates the conditions for what comes next. This is the narrative bridge between strategy and roadmap.
- **Key assumptions:** The 3-5 assumptions that must be true for the strategy to work. For each, state how you will test it and what changes if it is wrong.
- **Competitive positioning:** How this strategy positions you against alternatives. Reference `competitive-response` output for competitive context.

**Artifact:** Strategy narrative (2-3 pages) saved as `applied/strategy-narrative-{product}.md`.

### Step 4: Write the Roadmap Narrative

Transform the feature roadmap into a story of evolving customer experience. This is not a replacement for the feature roadmap — it is the companion document that explains why the sequence matters.

For each roadmap phase (use the horizons from `feature-prioritization` if available):

- **Phase name:** A memorable label (not "Q3" — something like "Foundation" or "Expand the Loop").
- **Customer story:** At the end of this phase, the customer can do [X] that they could not before. Describe the experience, not the feature.
- **Why this phase now:** What makes this the right next step? What did the previous phase unlock? What external factor creates urgency?
- **Key bets:** The 2-3 most important things shipping in this phase and the assumptions behind each.
- **Success signal:** How you know this phase worked — one metric or qualitative signal that indicates the customer story is real.
- **What we are NOT doing in this phase:** Explicit exclusions with brief rationale.

End with a **narrative thread** — a 2-3 sentence summary of how the phases connect: "First we [X], which teaches us [Y], which positions us to [Z]."

**Artifact:** Roadmap narrative saved as `applied/roadmap-narrative-{product}.md`.

### Step 5: Compile the Narrative Package

Assemble all four artifacts into a single narrative package:

1. Customer Context Brief (from Step 1)
2. Product Vision Document (from Step 2)
3. Strategy Narrative (from Step 3)
4. Roadmap Narrative (from Step 4)

Add an **executive summary** (one paragraph, under 100 words) that captures the core narrative: who the customer is, what the vision is, why now, and what you are doing first.

Review the package for narrative consistency:
- Does the vision follow from the customer context?
- Does the strategy follow from the vision?
- Does the roadmap follow from the strategy?
- Can a new team member read this top-to-bottom and understand where the product is going and why?

**Artifact:** Complete narrative package saved as `applied/narrative-package-{product}.md`.

## Diagnostic Questions

1. **Can you describe your product's purpose in one sentence without mentioning features?** If not, you need the vision document (Step 2) before anything else. The sentence should describe a transformation, not a capability.

2. **When you present your roadmap, do stakeholders ask "why?"** If the response to your roadmap is consistently "why this order?" or "why not X instead?" — the roadmap lacks narrative context. The roadmap narrative (Step 4) is the cure.

3. **Could a new hire explain your strategy after one week?** If new team members take months to "get" the strategy, the narrative is too implicit. Write it down in plain language. If you cannot, the strategy may not be clear even to you.

4. **Do different team members describe the customer differently?** If engineering, design, and marketing have divergent mental models of who the customer is, every decision will require re-alignment. The customer context brief (Step 1) creates the shared brain.

5. **Is your "why now" compelling to a skeptic?** If you cannot convince someone outside the company that this is the right moment, the strategy narrative needs work. "Why now" should reference external evidence, not internal ambition.

6. **Does your vision survive a "so what?" test?** Read your vision document aloud. After each paragraph, ask "so what?" If the answer is not obvious, the narrative is not connecting the vision to customer impact.

7. **Is your roadmap retellable?** Can someone who reads the roadmap narrative retell the story to a colleague? If it requires the full document to make sense, simplify. The best roadmap narratives compress into a single memorable sentence.

## Common Mistakes

1. **Writing the vision as a feature list in narrative form**
   "We will build X, then Y, then Z" is not a vision — it is a roadmap in disguise. The vision document describes the end state, not the journey. Start with the customer's transformed experience, not your engineering plan.

2. **Confusing strategy with goals**
   "Grow revenue 3x" is a goal, not a strategy. A strategy explains how you will achieve the goal given the competitive landscape and your specific advantages. The strategy narrative must contain a theory of winning, not a list of targets.

3. **Writing for yourself instead of for the audience**
   The customer context brief is for the whole team. The vision document is for leadership and the team. The roadmap narrative is for stakeholders who need to understand sequencing. Each document has a different audience — adjust the level of detail, jargon, and emphasis accordingly.

4. **Skipping "why now"**
   Many strategy narratives describe what the company will do without explaining why this is the right moment. Without "why now," the strategy feels arbitrary. Anchor it in specific external changes.

5. **Updating the roadmap without updating the narrative**
   When priorities shift, teams update the feature list but forget to update the narrative. This creates a disconnect: the roadmap says one thing, the narrative says another, and stakeholders lose trust. Treat the narrative as a living document that evolves with the roadmap.

6. **Making the narrative unfalsifiable**
   "We will be the best platform for X" is not falsifiable. A good strategy narrative includes key assumptions that can be tested and conditions under which the strategy would change. This makes the narrative a tool for learning, not just persuasion.

## Context Integration

| Context Directory | How It Feeds This Skill |
|---|---|
| `context/products/` | **Step 2-4**: Grounds the vision and roadmap in current product capabilities and architecture. Prevents the narrative from becoming disconnected from what exists today. |
| `context/verticals/` | **Step 1, 4**: Provides market-specific customer profiles and use cases for the customer context brief. Informs phase targeting in the roadmap narrative. |
| `context/competitive/` | **Step 2-3**: Shapes the "why now" and competitive positioning sections. The strategy narrative must account for what competitors are doing and where gaps exist. |
| `context/company/` | **Step 3**: Calibrates the strategy narrative to the company's stage, resources, and capabilities. A seed-stage narrative differs from a Series C narrative. |
| `context/founders/` | **Step 2-3**: Surfaces the founding thesis and leadership vision. The product vision should build on and extend the founder's original insight, not contradict it. |
| `context/signals/` | **Step 2-3**: Provides external evidence for the "why now" section — market trends, community sentiment, and ecosystem shifts. Check collection timestamps for freshness. |
