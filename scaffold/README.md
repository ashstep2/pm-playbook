# Company Playground Scaffold

Use this template to create a company-specific repo that pairs with pm-playbooks.

## Setup

```bash
# 1. Copy this scaffold to a new directory
cp -r scaffold/ ../my-company-playground/
cd ../my-company-playground/

# 2. Initialize git and add pm-playbooks as a submodule
git init
git submodule add https://github.com/ashstep2/pm-playbooks.git

# 3. Copy the CLAUDE.md template
cp CLAUDE.md.template CLAUDE.md
# Edit CLAUDE.md with your company details

# 4. Install skills into .claude/skills/ (Claude Code auto-discovers these)
mkdir -p .claude/skills
for skill in pm-playbooks/skills/*/; do
  name=$(basename "$skill")
  ln -sf "../../pm-playbooks/skills/${name}/SKILL.md" ".claude/skills/${name}.md"
done
# Also symlink any company-specific skills you create:
# ln -sf "../../skills/my-skill/SKILL.md" ".claude/skills/my-skill.md"

# 5. Set up signal collectors (optional)
cp pm-playbooks/signals.yaml.example signals.yaml
# Edit signals.yaml with your company's repos, keywords, competitors
pip install pyyaml requests PyGithub praw

# 6. Fill in context/ with your company's data
# See README.md in each context subdirectory for guidance

# 7. Run skills via Claude Code
# Open the repo in Claude Code and invoke any skill by name
```

## Directory Structure

```
my-company-playground/
├── .claude/skills/        # Symlinks to all skills (auto-discovered by Claude Code)
├── pm-playbooks/          # Git submodule (general skills + collectors)
├── context/               # Your company's knowledge base
│   ├── founders/          # Leadership quotes, themes, public content
│   ├── company/           # Size, funding, culture, org structure
│   ├── products/          # Product analyses
│   ├── verticals/         # Market verticals
│   ├── competitive/       # Competitive landscape
│   └── signals/           # Auto-collected signals (from collectors/)
├── signals.yaml           # Signal collection config
├── .env                   # API keys for collectors (not committed)
├── skills/                # Company-specific skill sources
├── applied/               # Outputs from running skills
└── CLAUDE.md              # Configures Claude Code behavior
```
