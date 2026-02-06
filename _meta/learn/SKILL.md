---
name: learn
description: "Ingest external PM content (articles, podcasts, transcripts) and propose targeted improvements to existing skills."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Learn

Ingest external PM content — articles, podcast transcripts, conference talks, book excerpts — and propose targeted improvements to existing pm-playbooks skills. Proposals are always written to a file for human review; they are never auto-applied.

## Instructions

### Step 1: Receive Content

Accept one of these input types from the user:
- **URL** — fetch and extract the main content
- **Pasted text** — article body, transcript, or notes
- **File path** — read the local file

Record the source metadata:
- Title
- Author(s)
- Publication date (if available)
- Source URL

### Step 2: Extract Candidate Insights

Read the content and extract **3–10 candidate insights** that could improve existing skills.

For each candidate, record:
- **Insight** — one-sentence summary
- **Direct quote** — the exact words from the source (with surrounding context)
- **Source attribution** — author, context, URL
- **Relevant skill(s)** — which skill(s) in `skills/` this would improve

### Step 3: Apply Novelty Filter

Score each candidate against this tier system:

| Tier | Label | Action |
|---|---|---|
| 1 | **Generic knowledge** — Claude already knows this without a skill | EXCLUDE |
| 2 | **Implementation-specific** — concrete how-to with a named method or metric | Include |
| 3 | **Architectural trade-off** — explains *why* with evidence from real products | Include (high priority) |
| 4 | **Counter-intuitive** — contradicts common PM assumptions with evidence | Include (highest priority) |

Drop all Tier 1 candidates. Keep Tier 2–4 with their tier label.

### Step 4: Map to Skill Sections

For each surviving insight, identify exactly where it belongs:
- **Core Principles** — if it's a new attributed principle with a quotable source
- **Instructions** — if it adds or refines a step in the workflow
- **Common Mistakes** — if it describes a failure mode with avoidance strategy
- **Diagnostic Questions** — if it adds a question that changes how a PM assesses the situation

### Step 5: Draft Proposed Edits

For each insight, write a concrete edit proposal:

```markdown
### Proposal: [short title]

**Skill:** [skill-name]
**Section:** [Core Principles | Instructions | Common Mistakes | Diagnostic Questions]
**Tier:** [2 | 3 | 4]

**Current state:** [quote the current text, or "New addition"]

**Proposed change:**
[The exact markdown to add or replace]

**Rationale:** [Why this improves the skill — 1-2 sentences]

**Source:** [Author, Context](URL)
```

### Step 6: Write Proposal File

Write all proposals to a single file:
```
_meta/proposals/{YYYY-MM-DD}-{source-slug}.md
```

The file should include:
1. Source metadata (title, author, URL, date)
2. Summary of what was ingested (1-2 sentences)
3. Number of candidates extracted vs. number that passed the novelty filter
4. All proposal entries from Step 5
5. A "Requires Human Review" notice at the top

### Step 7: Prompt Review

Tell the user:
- How many proposals were generated and for which skills
- Where the proposal file was written
- That proposals require human review before being applied
- Suggest the user review with: `cat _meta/proposals/{filename}`

## Diagnostic Questions

1. Is the source from a practitioner (shipped products) or purely theoretical?
2. Does the source provide specific metrics, thresholds, or named frameworks?
3. Are there direct quotes suitable for attributed principles?
4. Does any insight contradict what an existing skill currently recommends?
5. Is the source recent enough to reflect current industry practice?

## Common Mistakes

1. **Accepting generic advice** — "Talk to your users" is Tier 1. "Run a 40% 'very disappointed' survey with n>100 before declaring PMF" is Tier 2+.
2. **Losing attribution** — Every insight needs a direct quote and source. Paraphrased insights without quotes are not accepted.
3. **Proposing additions to the wrong section** — A principle without a quote goes in Common Mistakes, not Core Principles.
4. **Auto-applying changes** — Proposals are always written to `_meta/proposals/` for human review. Never directly edit a SKILL.md during a learn run.
5. **Ignoring version bumps** — Each proposal should note which version field would need updating (minor for new principles/instructions, patch for fixes).
