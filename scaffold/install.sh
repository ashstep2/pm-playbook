#!/usr/bin/env bash
# install.sh — Symlink pm-playbooks skills into .claude/skills/
#
# Usage: bash pm-playbooks/scaffold/install.sh
# Run from the root of your project (the parent repo, not pm-playbooks itself).

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLAYBOOKS_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
PROJECT_DIR="$(pwd)"

# Verify pm-playbooks is present
if [ ! -d "$PLAYBOOKS_DIR/skills" ]; then
  echo "Error: Cannot find pm-playbooks/skills/. Run this from your project root."
  exit 1
fi

# Create .claude/skills/ directory
mkdir -p "$PROJECT_DIR/.claude/skills"

# Calculate relative path from .claude/skills/ to pm-playbooks/skills/
RELATIVE_PLAYBOOKS="$(python3 -c "import os.path; print(os.path.relpath('$PLAYBOOKS_DIR/skills', '$PROJECT_DIR/.claude/skills'))")"

# Symlink all pm-playbooks skills
count=0
for skill_dir in "$PLAYBOOKS_DIR/skills"/*/; do
  name="$(basename "$skill_dir")"
  if [ -f "$skill_dir/SKILL.md" ]; then
    ln -sf "$RELATIVE_PLAYBOOKS/$name/SKILL.md" "$PROJECT_DIR/.claude/skills/$name.md"
    count=$((count + 1))
  fi
done
echo "Linked $count pm-playbooks skills"

# Symlink company-specific skills if they exist
company_count=0
if [ -d "$PROJECT_DIR/skills" ]; then
  RELATIVE_COMPANY="$(python3 -c "import os.path; print(os.path.relpath('$PROJECT_DIR/skills', '$PROJECT_DIR/.claude/skills'))")"
  for skill_dir in "$PROJECT_DIR/skills"/*/; do
    name="$(basename "$skill_dir")"
    if [ -f "$skill_dir/SKILL.md" ]; then
      ln -sf "$RELATIVE_COMPANY/$name/SKILL.md" "$PROJECT_DIR/.claude/skills/$name.md"
      company_count=$((company_count + 1))
    fi
  done
  echo "Linked $company_count company-specific skills"
fi

# Copy CLAUDE.md template if none exists
if [ ! -f "$PROJECT_DIR/CLAUDE.md" ]; then
  cp "$PLAYBOOKS_DIR/scaffold/CLAUDE.md.template" "$PROJECT_DIR/CLAUDE.md"
  echo "Created CLAUDE.md from template (edit with your company details)"
else
  echo "CLAUDE.md already exists (skipped)"
fi

total=$((count + company_count))
echo ""
echo "Done. $total skills installed in .claude/skills/"
echo "Open this project in Claude Code and invoke any skill by name."
