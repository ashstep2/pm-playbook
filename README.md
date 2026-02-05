# PM Playbooks

19 reusable product management skills structured as [Anthropic Agent Skills](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview). Each skill is a repeatable decision-making workflow that produces structured artifacts (scorecards, frameworks, roadmaps, and analyses) grounded in attributed insights from product leaders.

## How It Works

**Skills** are portable PM frameworks. Drop them into any repo's `.claude/skills/` directory and invoke via Claude Code.

**Context** makes skills specific. Point skills at a `context/` directory with company data (founders, products, competitive landscape) and they produce grounded, company-specific analysis instead of generic advice.

**Applied outputs** are what skills produce. These are the deliverables a PM would use to make decisions.

```
pm-playbooks/skills/  → copy to  →  your-project/.claude/skills/
                                    your-project/context/     ← optional: company data
                                    your-project/applied/     ← outputs go here
```

## Skills

### Strategic: Deciding WHAT to build

| Skill | What It Produces |
|---|---|
| [product-portfolio-strategy](skills/product-portfolio-strategy/SKILL.md) | Multi-product roadmap + resource allocation across bets |
| [measuring-product-market-fit](skills/measuring-product-market-fit/SKILL.md) | PMF scorecard + signal tracking + pivot/persevere framework |
| [competitive-response](skills/competitive-response/SKILL.md) | Threat assessment + response playbook + moat analysis |
| [research-to-product-pipeline](skills/research-to-product-pipeline/SKILL.md) | Translation framework: research breakthroughs → shipped products |
| [platform-vs-application](skills/platform-vs-application/SKILL.md) | Build/buy/partner analysis + platform economics + ecosystem design |
| [vertical-market-assessment](skills/vertical-market-assessment/SKILL.md) | TAM/SAM/SOM + vertical prioritization matrix + entry strategy |

### Planning: Deciding HOW to build

| Skill | What It Produces |
|---|---|
| [zero-to-one-product-launch](skills/zero-to-one-product-launch/SKILL.md) | Launch checklist + channel strategy + success metrics + rollback plan |
| [feature-prioritization](skills/feature-prioritization/SKILL.md) | Weighted scoring matrix + sequenced roadmap + trade-off analysis |
| [pricing-and-monetization](skills/pricing-and-monetization/SKILL.md) | Pricing model analysis + willingness-to-pay + packaging strategy |
| [north-star-metrics](skills/north-star-metrics/SKILL.md) | Metric tree + leading/lagging indicators + dashboard design |
| [writing-prds-for-ai](skills/writing-prds-for-ai/SKILL.md) | PRD template + uncertainty handling + eval criteria for AI outputs |

### Execution: Building and shipping

| Skill | What It Produces |
|---|---|
| [customer-discovery](skills/customer-discovery/SKILL.md) | Interview guide + synthesis framework + discovery report |
| [developer-experience-audit](skills/developer-experience-audit/SKILL.md) | Friction scorecard + prioritized DX recommendations |
| [user-onboarding-optimization](skills/user-onboarding-optimization/SKILL.md) | Onboarding flow audit + activation metrics + improvement roadmap |
| [stakeholder-alignment](skills/stakeholder-alignment/SKILL.md) | RACI matrix + communication plan + research-product interface |

### Analysis: Measuring and learning

| Skill | What It Produces |
|---|---|
| [user-segmentation](skills/user-segmentation/SKILL.md) | Segment profiles + prioritization matrix + cross-segment insights |
| [ecosystem-health](skills/ecosystem-health/SKILL.md) | Ecosystem scorecard + benchmark comparison + growth playbook |
| [api-design-review](skills/api-design-review/SKILL.md) | Per-endpoint assessment + standards compliance + recommendations |
| [partnership-evaluation](skills/partnership-evaluation/SKILL.md) | Partner scorecards + deal structures + comparative assessment |

## Using with a Company Context

Skills get smarter when paired with a company-specific knowledge base. See [scaffold/](scaffold/) for a template to create your own company repo.

```bash
# 1. Create a company repo from the scaffold
cp -r scaffold/ my-company-playground/

# 2. Add pm-playbooks as a submodule
cd my-company-playground
git submodule add https://github.com/ashstep2/pm-playbooks.git

# 3. Fill in context/ with your company's data
# 4. Run skills — they'll automatically use your context
```

## Skill Format

See [SKILL_FORMAT.md](SKILL_FORMAT.md) for the format specification. Each skill includes:
- **Core Principles** — attributed insights from product leaders with direct quotes
- **Instructions** — step-by-step process producing concrete artifacts
- **Diagnostic Questions** — help assess the situation before diving in
- **Common Mistakes** — what PMs get wrong and how to avoid it
- **Context Integration** — how the skill uses company data when available

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add or improve skills.

## License

MIT
