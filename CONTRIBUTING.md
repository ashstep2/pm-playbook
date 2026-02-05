# Contributing

## Adding a New Skill

1. Create a directory under `skills/` with a kebab-case name
2. Add a `SKILL.md` following the format in [SKILL_FORMAT.md](SKILL_FORMAT.md)
3. Add an `examples/` directory (examples optional but encouraged)

### Skill Quality Checklist

- [ ] Description starts with "Help users [verb]..."
- [ ] 6-10 Core Principles, each with an attributed quote and source URL
- [ ] Instructions produce concrete artifacts (not just "think about X")
- [ ] 5-8 Diagnostic Questions
- [ ] 4-6 Common Mistakes with avoidance strategies
- [ ] Context Integration section explains how `context/` is used
- [ ] Under 500 lines total

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

## Reporting Issues

Open an issue describing what's wrong or what's missing.
