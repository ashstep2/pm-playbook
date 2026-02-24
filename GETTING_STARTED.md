# Getting Started

You have 30 skills. Don't read them all — pick a journey that matches your situation and run it.

## Pick Your Journey

### 1. "We're launching something new"
**Start here if:** You have an idea or early product and need to validate, spec, and ship it.

```
customer-discovery          → Do users have this problem?
   ↓
prototype-driven-validation → Does our solution work? (test 2-3 variations)
   ↓
writing-prds-for-ai         → Spec it (grounded in prototype findings)
   ↓
zero-to-one-product-launch  → Ship it (checklist, channels, metrics, rollback plan)
   ↓
north-star-metrics          → Measure it (metric tree + dashboard design)
```

**Time:** Run one skill per session. Full journey takes 5 sessions.
**See it in action:** [Customer Discovery Example](examples/customer-discovery-example.md)

---

### 2. "Growth has stalled — what's the lever?"
**Start here if:** The product exists but metrics are flat. You need to find what moves the needle.

```
north-star-metrics          → Are we measuring the right thing?
   ↓
user-segmentation           → Which segment has the most upside?
   ↓
experiment-design           → Design the test (A/B, fake door, beta cohort)
   ↓
user-onboarding-optimization → Fix the first experience (biggest drop-off)
   ↓
measuring-product-market-fit → Are we actually there yet?
```

**Time:** 4-5 sessions. Start with `north-star-metrics` — everything else follows from knowing what to measure.

---

### 3. "We need a competitive strategy"
**Start here if:** A competitor just launched, you're entering a crowded market, or you need to defend your position.

```
competitive-response        → Map the landscape, assess threats, build response playbook
   ↓
feature-prioritization      → Prioritize based on competitive + customer signals
   ↓
product-narrative-strategy  → Craft the "why us, why now" story
   ↓
pricing-and-monetization    → Price against alternatives
```

**Time:** 3-4 sessions. Start with `competitive-response` — it grounds everything else.
**See it in action:** [Competitive Response Example](examples/competitive-response-example.md), [Feature Prioritization Example](examples/feature-prioritization-example.md)

---

### 4. "We need to get aligned and ship faster"
**Start here if:** The team has ideas but no shared direction, meetings feel unproductive, or planning cycles are too long.

```
product-narrative-strategy  → Write the vision + strategy narrative
   ↓
stakeholder-alignment       → Map stakeholders, build RACI, design comms plan
   ↓
iteration-cadence-design    → Design the operating rhythm (cycles, rituals, decisions)
   ↓
feature-prioritization      → Prioritize the backlog with shared criteria
```

**Time:** 3-4 sessions. Start with `product-narrative-strategy` — alignment is impossible without a shared story.

---

### 5. "We're building for agents / AI distribution"
**Start here if:** Your product has an API and you want it to be discoverable and usable by AI agents (Claude, GPT, Cursor, etc.).

```
agent-surface-audit         → How agent-accessible is your product today?
   ↓
mcp-design-review           → Review/design your MCP server
   ↓
agent-journey-mapping       → Map the agent user journey end-to-end
   ↓
agent-integration-design    → Design I/O specs + orchestration compatibility
   ↓
agent-ready-gtm             → Position for agent buyers (trust center, pricing surface)
```

**Time:** 4-5 sessions. Start with `agent-surface-audit` — it tells you where you stand.

---

## How to Run a Skill

Open the repo in Claude Code and say the skill name:

```
> Run customer-discovery for my product
```

That's it. The skill will:
1. Ask you diagnostic questions to calibrate the approach
2. Walk through each step, producing artifacts
3. Save output to `applied/`
4. Suggest what to run next (based on `skill-graph.yaml`)

### With Company Context (Better Outputs)

If you add files to `context/`, skills read them automatically — no prompting needed:

```
context/
├── company/       ← Team size, stage, funding, org structure
├── competitive/   ← Competitor analyses, battle cards
├── products/      ← Product descriptions, pricing, architecture
├── verticals/     ← Target markets, TAM/SAM/SOM, use cases
├── founders/      ← Leadership vision, founding thesis
└── signals/       ← Auto-collected data (GitHub, HN, Reddit, news)
```

**No context? No problem.** Skills ask for what they need conversationally.

---

## Your First 10 Minutes

1. **Clone the repo** and open in Claude Code
2. **Pick a journey** from above (or just pick one skill)
3. **Run it** — say the skill name and describe your product
4. **Read the output** — it'll be in `applied/`
5. **Follow the chain** — the skill suggests what to run next

Want to see what the output looks like before running anything? Check the [examples](examples/).

---

## All 30 Skills at a Glance

| Category | Skills |
|---|---|
| **Strategic** (7) | product-portfolio-strategy, measuring-product-market-fit, competitive-response, research-to-product-pipeline, platform-vs-application, vertical-market-assessment, product-narrative-strategy |
| **Planning** (6) | zero-to-one-product-launch, feature-prioritization, pricing-and-monetization, north-star-metrics, writing-prds-for-ai, experiment-design |
| **Execution** (6) | customer-discovery, developer-experience-audit, user-onboarding-optimization, stakeholder-alignment, prototype-driven-validation, iteration-cadence-design |
| **Agent-First** (6) | agent-surface-audit, mcp-design-review, agent-journey-mapping, agent-ready-gtm, agent-integration-design, agent-consumer-experience |
| **Analysis** (5) | user-segmentation, ecosystem-health, api-design-review, partnership-evaluation, product-quality-review |

Full details for each skill: [README.md](README.md)
