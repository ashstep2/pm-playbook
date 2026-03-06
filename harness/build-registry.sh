#!/usr/bin/env bash
# build-registry.sh — Scans all SKILL.md files and generates skill-registry.json
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REGISTRY="$SCRIPT_DIR/skill-registry.json"
SKILL_GRAPH="$PROJECT_ROOT/skill-graph.yaml"

# ── Helpers ────────────────────────────────────────────────────────────────

# Extract YAML frontmatter value by key from a SKILL.md file
frontmatter_val() {
  local file="$1" key="$2"
  sed -n '/^---$/,/^---$/p' "$file" | grep "^${key}:" | head -1 | sed -E "s/^${key}:[[:space:]]*\"?//;s/\"[[:space:]]*$//"
}

# Extract step names (### Step N: <name>) from a SKILL.md
extract_steps() {
  local file="$1"
  grep -E '^### Step [0-9]+:' "$file" | sed -E 's/^### Step [0-9]+:[[:space:]]*//' || true
}

# Extract artifact names from "**Artifact produced**" lines
# Handles both "**Artifact produced**:" and "**Artifact produced:**" formats
extract_artifacts() {
  local file="$1"
  grep -E '\*\*Artifact produced\*?\*?:?\*?\*?' "$file" | \
    sed -E 's/^.*\*\*Artifact produced:?\*\*:?[[:space:]]*//' | \
    sed -E 's/[[:space:]]*\(.*$//' | \
    sed -E 's/\.$//;s/^- //' | \
    sed -E 's/ saved as .*$//' | \
    grep -v '^$' || true
}

# Get category from skill-graph.yaml for a given skill name
get_category() {
  local skill="$1"
  if [[ -f "$SKILL_GRAPH" ]]; then
    awk -v s="$skill:" '
      $0 ~ "^  " s { found=1; next }
      found && /category:/ { gsub(/.*category:[[:space:]]*/, ""); print; exit }
      found && /^  [a-z]/ { exit }
    ' "$SKILL_GRAPH"
  fi
}

# Get feeds_into list from skill-graph.yaml
get_feeds_into() {
  local skill="$1"
  if [[ -f "$SKILL_GRAPH" ]]; then
    awk -v s="$skill:" '
      $0 ~ "^  " s { found=1; next }
      found && /feeds_into:/ { in_list=1; next }
      found && in_list && /^      - / { gsub(/^[[:space:]]*- /, ""); items = items (items ? "," : "") $0; next }
      found && in_list && !/^      -/ { in_list=0 }
      found && /^  [a-z]/ { exit }
      END { print items }
    ' "$SKILL_GRAPH"
  fi
}

# Get reads_from list from skill-graph.yaml
get_reads_from() {
  local skill="$1"
  if [[ -f "$SKILL_GRAPH" ]]; then
    awk -v s="$skill:" '
      $0 ~ "^  " s { found=1; next }
      found && /reads_from:/ { in_list=1; next }
      found && in_list && /^      - / { gsub(/^[[:space:]]*- /, ""); items = items (items ? "," : "") $0; next }
      found && in_list && !/^      -/ { in_list=0 }
      found && /^  [a-z]/ { exit }
      END { print items }
    ' "$SKILL_GRAPH"
  fi
}

# Convert comma-separated string to JSON array
csv_to_json_array() {
  local csv="$1"
  if [[ -z "$csv" ]]; then
    echo "[]"
    return
  fi
  echo "$csv" | tr ',' '\n' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//' | \
    awk 'BEGIN{printf "["} NR>1{printf ","} {printf "\"%s\"", $0} END{printf "]"}'
}

# Escape string for JSON
json_escape() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\n'/\\n}"
  s="${s//$'\t'/\\t}"
  printf '%s' "$s"
}

# ── Build Skills Registry ──────────────────────────────────────────────────

echo "Building skill registry..."
echo "Project root: $PROJECT_ROOT"

# Start JSON
{
  printf '{\n  "skills": {\n'

  first_skill=true

  # Process skills/ and _meta/ directories
  for skill_dir in "$PROJECT_ROOT"/skills/*/  "$PROJECT_ROOT"/_meta/*/; do
    # Normalize path (remove trailing double slashes)
    skill_dir="${skill_dir%/}/"
    skill_file="${skill_dir}SKILL.md"
    [[ -f "$skill_file" ]] || continue

    skill_name=$(frontmatter_val "$skill_file" "name")
    [[ -z "$skill_name" ]] && continue

    description=$(frontmatter_val "$skill_file" "description")
    version=$(frontmatter_val "$skill_file" "version")

    # Get category and dependencies from skill graph
    category=$(get_category "$skill_name")
    [[ -z "$category" ]] && category="meta"
    feeds_into=$(get_feeds_into "$skill_name")
    reads_from=$(get_reads_from "$skill_name")

    # Determine skill path relative to project root
    skill_path="${skill_file#$PROJECT_ROOT/}"

    # Extract steps and artifacts
    steps_raw=$(extract_steps "$skill_file")
    artifacts_raw=$(extract_artifacts "$skill_file")
    step_count=$(echo "$steps_raw" | grep -c . 2>/dev/null || echo "0")

    # Build required_sections JSON array from artifact names
    required_sections="["
    first_section=true
    while IFS= read -r artifact; do
      [[ -z "$artifact" ]] && continue
      escaped=$(json_escape "$artifact")
      if $first_section; then
        first_section=false
      else
        required_sections+=","
      fi
      required_sections+="\"$escaped\""
    done <<< "$artifacts_raw"
    required_sections+="]"

    # Build expected_artifacts (same as required_sections)
    expected_artifacts="$required_sections"

    # Output pattern
    output_pattern="applied/*${skill_name}*.md"

    # Comma handling
    if $first_skill; then
      first_skill=false
    else
      printf ',\n'
    fi

    # Write skill entry
    cat <<ENTRY
    "$(json_escape "$skill_name")": {
      "name": "$(json_escape "$skill_name")",
      "description": "$(json_escape "$description")",
      "version": "$(json_escape "$version")",
      "category": "$(json_escape "$category")",
      "skill_path": "$(json_escape "$skill_path")",
      "output_dir": "applied",
      "output_pattern": "$(json_escape "$output_pattern")",
      "expected_artifacts": $expected_artifacts,
      "quality": {
        "min_word_count": 500,
        "required_sections": $required_sections,
        "no_placeholders": ["TODO", "TBD", "PLACEHOLDER", "[INSERT"],
        "min_sections": $step_count
      },
      "feeds_into": $(csv_to_json_array "$feeds_into"),
      "reads_from": $(csv_to_json_array "$reads_from")
    }
ENTRY
  done

  printf '\n  },\n'

  # ── Build Collectors Registry ──────────────────────────────────────────
  printf '  "collectors": {\n'

  first_collector=true
  for cname in github hn reddit news; do
    script="collectors/${cname}_collector.py"
    case "$cname" in
      github) output="context/signals/github-ecosystem.md" ;;
      hn)     output="context/signals/hackernews-sentiment.md" ;;
      reddit) output="context/signals/reddit-discussions.md" ;;
      news)   output="context/signals/news-coverage.md" ;;
    esac

    if [[ ! -f "$PROJECT_ROOT/$script" ]]; then
      continue
    fi

    if $first_collector; then
      first_collector=false
    else
      printf ',\n'
    fi

    cat <<CENTRY
    "$cname": {
      "script": "$script",
      "output": "$output"
    }
CENTRY
  done

  printf '\n  },\n'
  printf '  "generated_at": "%s"\n' "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
  printf '}\n'

} > "$REGISTRY"

echo "Registry written to: $REGISTRY"

# Validate JSON
if command -v python3 &>/dev/null; then
  if python3 -c "import json; json.load(open('$REGISTRY'))" 2>/dev/null; then
    skill_count=$(python3 -c "import json; d=json.load(open('$REGISTRY')); print(len(d['skills']))")
    collector_count=$(python3 -c "import json; d=json.load(open('$REGISTRY')); print(len(d['collectors']))")
    echo "Valid JSON. Skills: $skill_count, Collectors: $collector_count"
  else
    echo "ERROR: Generated JSON is invalid!" >&2
    exit 1
  fi
else
  echo "Warning: python3 not found, skipping JSON validation"
fi
