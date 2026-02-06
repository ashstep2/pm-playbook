# Contributing

## Adding a New Skill

1. Create a directory under `skills/` with a kebab-case name
2. Add a `SKILL.md` following the format in [SKILL_FORMAT.md](SKILL_FORMAT.md)
3. Add an `examples/` directory (examples optional but encouraged)

### Skill Quality Checklist

- [ ] Description starts with "Help users [verb]..."
- [ ] Frontmatter includes `version: "1.0.0"` and `last_updated` (ISO date)
- [ ] 6-10 Core Principles, each with an attributed quote and source URL
- [ ] Instructions produce concrete artifacts (not just "think about X")
- [ ] 5-8 Diagnostic Questions
- [ ] 4-6 Common Mistakes with avoidance strategies
- [ ] Context Integration section explains how `context/` is used
- [ ] Under 500 lines total
- [ ] Skill added to `skill-graph.yaml` with `category`, `feeds_into`, and `reads_from`

### Principles Must Be Attributed

Every principle needs:
- A **direct quote** from a named source
- The **person's name and context** (role, company, podcast, book)
- A **source URL** when available

Good:
```markdown
1. **Measure the "must-have" score**
   "Ask users 'How would you feel if you could no longer use this product?' — if 40%+ say 'very disappointed,' you have PMF."
   — *Rahul Vohra, CEO of Superhuman* ([First Round Review](https://review.firstround.com/...))
```

Not acceptable:
```markdown
1. **Measure satisfaction**
   Survey your users to understand if they find your product valuable.
```

## Improving an Existing Skill

- Add better attributed principles with sources
- Improve instructions for clarity and concreteness
- Add examples
- Fix broken source URLs

## Self-Improvement Workflow

Two meta-skills in `_meta/` help the system improve over time:

- **`/learn`** (`_meta/learn/SKILL.md`) — Ingest external PM content (articles, podcasts, transcripts) and generate skill improvement proposals. Proposals are written to `_meta/proposals/` and always require human review before being applied.
- **`/improve`** (`_meta/improve/SKILL.md`) — Run after completing any skill to reflect on what worked and what didn't. Reflections accumulate in `applied/_reflections.md` and surface recurring issues.

### How proposals become PRs

1. Run `/learn` with a source URL or pasted content
2. Review the generated proposal in `_meta/proposals/`
3. If the proposal looks good, apply the edits to the relevant SKILL.md
4. Bump the `version` field (minor for new principles/instructions, patch for fixes)
5. Update `last_updated` to today's date
6. Open a PR with the proposal file as context for reviewers

## Reporting Issues

Open an issue describing what's wrong or what's missing.
