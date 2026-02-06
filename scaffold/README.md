# Company Playground Scaffold

Use this template to create a company-specific repo that pairs with pm-playbooks. Three paths from zero to running skills — pick the one that fits your time budget.

## Path A: Zero-Config (30 seconds)

Clone pm-playbooks directly and start using skills. No company context, no submodule — skills ask for information interactively.

```bash
git clone https://github.com/ashstep2/pm-playbooks.git
# Open in Claude Code → invoke any skill by name
```

## Path B: Project Integration (5 minutes)

Add pm-playbooks as a submodule in your project and run the install script to symlink skills.

```bash
# From your project root
git init  # skip if already a git repo
git submodule add https://github.com/ashstep2/pm-playbooks.git

# Install skills + generate CLAUDE.md
bash pm-playbooks/scaffold/install.sh
```

That's it. The install script:
1. Creates `.claude/skills/` directory
2. Symlinks all 19 pm-playbooks skills
3. Symlinks any company-specific skills from `skills/` if present
4. Copies `CLAUDE.md.template` → `CLAUDE.md` if none exists

## Path C: Full Company Setup (30 minutes)

For the richest, most grounded outputs — add company context and signal collectors.

```bash
# 1. Submodule + install
git submodule add https://github.com/ashstep2/pm-playbooks.git
bash pm-playbooks/scaffold/install.sh

# 2. Create context directories
mkdir -p context/{company,competitive,products,verticals,founders,signals}

# 3. Fill in context (see guidance below)
# Add markdown files to each directory with your company's data

# 4. Set up signal collectors (optional)
cp pm-playbooks/signals.yaml.example signals.yaml
# Edit signals.yaml with your repos, keywords, competitors
cp pm-playbooks/.env.example .env
# Add API keys to .env

# 5. Install collector dependencies and run
pip install pyyaml requests PyGithub praw
cd pm-playbooks && python3 -m collectors.run --config ../signals.yaml

# 6. Add company-specific skills (optional)
mkdir -p skills/my-custom-skill
# Create skills/my-custom-skill/SKILL.md following SKILL_FORMAT.md
bash pm-playbooks/scaffold/install.sh  # re-run to pick up new skills
```

## Graceful Degradation

Skills work at every setup level. More context produces more grounded output, but nothing breaks without it.

| Setup Level | What Happens |
|---|---|
| **No `context/`** | Skills ask for company information interactively |
| **Partial `context/`** | Use what's available, ask conversationally for the rest |
| **Full `context/`** | Outputs are fully grounded in company data |
| **Full `context/` + signals** | Outputs are grounded + enriched with live market data |

## Context Directory Guide

| Directory | What to Put Here | Example Files |
|---|---|---|
| `context/company/` | Company intel, funding, org structure, hiring signals | `overview.md`, `investor-thesis.md` |
| `context/competitive/` | Competitive landscape, competitor analyses | `landscape.md`, `competitor-x.md` |
| `context/products/` | Product descriptions, architectures, user data | `main-product.md`, `api.md` |
| `context/verticals/` | Target market descriptions, TAM estimates | `gaming.md`, `enterprise.md` |
| `context/founders/` | Founder backgrounds, public statements, vision | `ceo.md`, `cto.md` |
| `context/signals/` | Auto-populated by collectors — don't edit manually | (auto-generated) |

## Directory Structure

```
my-company-playground/
├── .claude/skills/        # Symlinks to all skills (auto-created by install.sh)
├── pm-playbooks/          # Git submodule (general skills + collectors)
├── context/               # Your company's knowledge base
│   ├── company/
│   ├── competitive/
│   ├── products/
│   ├── verticals/
│   ├── founders/
│   └── signals/           # Auto-collected signals (from collectors/)
├── skills/                # Company-specific skill sources (optional)
├── signals.yaml           # Signal collection config
├── .env                   # API keys for collectors (not committed)
├── applied/               # Outputs from running skills
│   └── _reflections.md    # Post-run reflections (from /improve)
└── CLAUDE.md              # Configures Claude Code behavior
```

## Updating pm-playbooks

```bash
git submodule update --remote pm-playbooks
bash pm-playbooks/scaffold/install.sh  # re-run to pick up new skills
git add pm-playbooks .claude/skills/
git commit -m "Update pm-playbooks submodule"
```
