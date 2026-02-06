# Skill Format Reference

Skills follow the [Anthropic Agent Skills specification](https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview) with attributed principles inspired by [Lenny's Newsletter](https://www.lennysnewsletter.com/) skill format.

## File Structure

```
skills/<skill-name>/
├── SKILL.md                    # Main skill file (everything in one place)
└── examples/
    └── <example-output>.md     # Filled example demonstrating the skill
```

## SKILL.md Format

### YAML Frontmatter (required)

```yaml
---
name: skill-name
description: "One-sentence description of what the skill does and when to use it."
version: "1.0.0"
last_updated: "2026-02-06"
---
```

| Field | Required | Description |
|---|---|---|
| `name` | Yes | Kebab-case skill identifier |
| `description` | Yes | One sentence starting with "Help users [verb]..." — this is what Claude reads to decide whether to invoke the skill |
| `version` | Yes | Semver. Major = restructured skill. Minor = new principles/instructions. Patch = typos/URL fixes. |
| `last_updated` | Yes | ISO date of last modification |

### Body Sections

#### 1. Title + Summary
```markdown
# Skill Name

One-sentence summary of what this skill produces and when a PM should reach for it.
```

#### 2. Core Principles
Attributed insights from PM leaders, founders, and domain experts. Each principle has a direct quote and source — not generic advice. 6-10 principles per skill.

```markdown
## Core Principles

1. **Principle name**
   "[Direct quote from source]"
   — *Source Name, Context* ([source](url))
```

#### 3. Instructions
Step-by-step process Claude follows when the skill is invoked. Each step produces a concrete artifact.

```markdown
## Instructions

### Step 1: [Name]
- What to do
- What to produce
- Where to look for data (reference `context/` if available)
```

#### 4. Diagnostic Questions
5-8 questions that help the user assess their situation before or during the skill.

#### 5. Common Mistakes
4-6 things PMs get wrong when doing this work. Each with a name and how to avoid it.

#### 6. Context Integration
How the skill uses the `context/` directory when available. Lists which context subdirectories feed which steps. If no context/ exists, the skill asks the user for the information.

### Constraints

- SKILL.md should be under 500 lines
- Instructions should be executable: Claude should be able to follow them without ambiguity
- Each step should produce a concrete output, not just "think about X"
- Every principle must have an attributed source with a direct quote
- Use progressive disclosure: link to examples for detailed methodology

## Examples

Each skill can include filled examples in the `examples/` directory. Examples:
- Demonstrate the full output the skill produces
- Are self-contained and readable without the SKILL.md
- Use evidence tags: `[PUBLIC]`, `[TESTED]`, `[ILLUSTRATIVE]`, `[SIGNAL]`

## Evidence Tags

| Tag | Meaning | When to Use |
|---|---|---|
| `[PUBLIC]` | Derived from publicly available information | Manual research, public docs, press releases |
| `[TESTED]` | Verified through direct testing or experimentation | Hands-on product testing, API calls, benchmarks |
| `[ILLUSTRATIVE]` | Hypothetical example used to demonstrate a pattern | Example outputs, scenario modeling |
| `[SIGNAL]` | Auto-collected by `collectors/` framework | Data from GitHub, HN, Reddit, news APIs. Includes collection timestamp. Check freshness before citing. |

## Signal Files (`context/signals/`)

When the `collectors/` framework is configured, it writes auto-collected data to `context/signals/`:

```
context/signals/
├── github-ecosystem.md       # Repo stats, issues, PRs
├── hackernews-sentiment.md   # HN stories and discussions
├── reddit-discussions.md     # Reddit posts from relevant subreddits
├── news-coverage.md          # News articles from NewsAPI
└── _synthesis.md             # Cross-source summary
```

Skills should reference `context/signals/` in their Context Integration table when applicable. Signal data supplements manual context — it never replaces it. Skills should check the collection timestamp in each file header and warn when data is older than 14 days.
