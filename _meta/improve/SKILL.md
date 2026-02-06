---
name: improve
description: "Reflect on a completed skill run, score its effectiveness, and propose one concrete improvement."
version: "1.0.0"
last_updated: "2026-02-06"
---

# Improve

Post-run reflection skill. After completing any skill, run this to record what worked, what didn't, and propose one improvement. Reflections accumulate in `applied/_reflections.md` and surface recurring issues over time.

## Instructions

### Step 1: Record Run Metadata

Capture the following from the skill run that just completed:

| Field | Value |
|---|---|
| Skill | [skill-name] |
| Date | [YYYY-MM-DD] |
| Context availability | [full / partial / none] — which `context/` directories were present |
| Artifacts produced | [list the outputs written to `applied/`] |
| Skill version | [from the SKILL.md frontmatter] |

### Step 2: Score the Run

Rate the run on three dimensions (1–5 scale):

| Dimension | 1 (Poor) | 3 (Adequate) | 5 (Excellent) |
|---|---|---|---|
| **Instruction Clarity** | Ambiguous steps, had to guess intent | Followable but some steps unclear | Every step unambiguous, produced exactly one artifact |
| **Context Sufficiency** | Critical data missing, outputs heavily caveated | Some gaps but worked around them | All needed data available, outputs fully grounded |
| **Artifact Usefulness** | Outputs too generic to act on | Useful with some manual refinement | Directly actionable, decision-ready |

### Step 3: Explain Low Scores

For any dimension scored below 4, write 1–2 sentences explaining:
- What specifically was awkward or missing
- What the user or skill author could do to fix it

### Step 4: Propose One Improvement

Based on the scores, propose exactly one change to the skill. Be specific:

- **If Instruction Clarity < 4**: Propose a reworded or restructured step
- **If Context Sufficiency < 4**: Propose a new entry in the Context Integration section
- **If Artifact Usefulness < 4**: Propose an additional artifact or a refinement to an existing one

Format the proposal as:
```markdown
**Proposed improvement:** [1-2 sentence description]
**Section to modify:** [Instructions / Context Integration / Core Principles / etc.]
**Priority:** [low / medium / high]
```

### Step 5: Append to Reflections Log

Append a new entry to `applied/_reflections.md`. Create the file if it doesn't exist.

Each entry follows this format:

```markdown
---

### [skill-name] — [YYYY-MM-DD]

| Dimension | Score |
|---|---|
| Instruction Clarity | X/5 |
| Context Sufficiency | X/5 |
| Artifact Usefulness | X/5 |

**Context:** [full / partial / none]
**Artifacts:** [list]

**Notes:** [explanation of low scores, if any]

**Proposed improvement:** [from Step 4]
```

### Step 6: Check for Recurring Themes

If `applied/_reflections.md` contains **3 or more reflections for the same skill**:

1. Read all reflections for that skill
2. Identify recurring themes (e.g., "Context Sufficiency consistently scores 2–3")
3. Write a brief summary at the end of the latest entry:
   ```
   **Recurring theme (N runs):** [pattern description + recommended action]
   ```
4. Suggest the user run `/learn` to formalize the improvement as a proposal

## Diagnostic Questions

1. Did you have to deviate from the skill's instructions at any point? Where?
2. Were there steps where you had to ask the user for information the skill should have guided you to find?
3. Did any artifact feel like it was going through the motions rather than producing genuine insight?
4. Would a different skill have been more appropriate for what the user actually needed?
5. Was there signal data available? Did it meaningfully improve the output?

## Common Mistakes

1. **Inflating scores** — Be honest. A score of 3 is fine; it means "adequate, room to improve." Reserve 5 for genuinely excellent runs.
2. **Proposing too many changes** — Exactly one improvement per reflection. This forces prioritization and makes the log actionable.
3. **Vague proposals** — "Make the skill better" is not a proposal. "Add a step between Steps 2 and 3 that asks the user to list their top 3 competitors" is.
4. **Forgetting to check for recurring themes** — The compound value of this skill comes from pattern recognition across runs.
