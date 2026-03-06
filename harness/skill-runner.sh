#!/usr/bin/env bash
# skill-runner.sh — Self-healing skill execution harness
# Usage:
#   ./harness/skill-runner.sh run <skill-name> "<input params>"
#   ./harness/skill-runner.sh batch [--category strategic|planning|execution|agent-first|analysis]
#   ./harness/skill-runner.sh collectors "<topic>"
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
REGISTRY="$SCRIPT_DIR/skill-registry.json"
REPORTS_DIR="$SCRIPT_DIR/reports"
MAX_RETRIES=3

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# ── Helpers ────────────────────────────────────────────────────────────────

log_info()  { echo -e "${BLUE}[INFO]${NC} $*"; }
log_ok()    { echo -e "${GREEN}[PASS]${NC} $*"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} $*"; }
log_err()   { echo -e "${RED}[FAIL]${NC} $*"; }

ensure_registry() {
  if [[ ! -f "$REGISTRY" ]]; then
    log_info "Registry not found. Building..."
    bash "$SCRIPT_DIR/build-registry.sh"
  fi
}

# Read a skill field from registry using python3 (reliable JSON parsing)
registry_get() {
  local skill="$1" field="$2"
  python3 -c "
import json, sys
d = json.load(open('$REGISTRY'))
s = d['skills'].get('$skill')
if not s:
    sys.exit(1)
val = s
for key in '$field'.split('.'):
    val = val[key]
if isinstance(val, (list, dict)):
    print(json.dumps(val))
else:
    print(val)
" 2>/dev/null
}

# List all skills, optionally filtered by category
list_skills() {
  local category="${1:-}"
  python3 -c "
import json
d = json.load(open('$REGISTRY'))
for name, s in d['skills'].items():
    cat = s.get('category', '')
    if not '$category' or cat == '$category':
        print(name)
"
}

# Sanitize input params for use in filenames
sanitize_filename() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | sed -E 's/[^a-z0-9]+/-/g;s/^-+|-+$//g' | head -c 60
}

# Get elapsed time in human-readable format
format_duration() {
  local seconds=$1
  if (( seconds < 60 )); then
    echo "${seconds}s"
  else
    local mins=$((seconds / 60))
    local secs=$((seconds % 60))
    echo "${mins}m ${secs}s"
  fi
}

# ── Smart Retry Instructions ──────────────────────────────────────────────

retry_instruction() {
  local category="$1" attempt="$2" details="$3"
  local instruction=""

  case "$category" in
    missing_dir)
      instruction="" ;; # handled by creating the dir before retry
    missing_file)
      instruction="You MUST write your full output directly. Do not skip any sections." ;;
    thin_output)
      instruction="Your previous output was only ${details} words. Be more comprehensive. Each section needs detailed analysis with specific examples, data points, and actionable recommendations." ;;
    missing_sections)
      instruction="Your output was missing these required sections: ${details}. You MUST include all of these sections with substantive content." ;;
    placeholder_text)
      instruction="Do NOT use placeholder text like TODO, TBD, or [INSERT]. Fill in every section with real analysis." ;;
    empty_headers)
      instruction="Every section header must have substantive content beneath it. No empty sections." ;;
  esac

  # Escalate with each retry
  if (( attempt >= 2 )); then
    instruction="$instruction This is attempt $attempt of $MAX_RETRIES. Be thorough."
  fi
  if (( attempt >= 3 )); then
    # Get all required sections and list them explicitly
    local sections
    sections=$(registry_get "$4" "quality.required_sections" 2>/dev/null || echo "[]")
    instruction="$instruction You MUST include ALL of these sections: $sections"
  fi

  echo "$instruction"
}

# ── Single Skill Execution ────────────────────────────────────────────────

run_skill() {
  local skill_name="$1"
  local input_params="${2:-}"

  ensure_registry

  # Look up skill in registry
  local skill_path
  skill_path=$(registry_get "$skill_name" "skill_path") || {
    log_err "Skill '$skill_name' not found in registry"
    return 1
  }

  local full_skill_path="$PROJECT_ROOT/$skill_path"
  if [[ ! -f "$full_skill_path" ]]; then
    log_err "SKILL.md not found at: $full_skill_path"
    return 1
  fi

  # Determine output file
  local sanitized
  sanitized=$(sanitize_filename "${input_params:-batch}")
  local output_file="$PROJECT_ROOT/applied/${skill_name}-${sanitized}.md"

  # Ensure output directory exists
  mkdir -p "$(dirname "$output_file")"

  log_info "Running skill: $skill_name"
  log_info "Input: ${input_params:-<none>}"
  log_info "Output: $output_file"

  local start_time attempt=0 success=false
  start_time=$(date +%s)

  while (( attempt <= MAX_RETRIES )); do
    if (( attempt > 0 )); then
      log_warn "Retry $attempt/$MAX_RETRIES for $skill_name"
    fi

    # Build prompt
    local skill_content
    skill_content=$(cat "$full_skill_path")

    local prompt="You are a PM executing a structured skill. Follow the instructions below exactly and produce all required artifacts.

$skill_content

---

"
    if [[ -n "$input_params" ]]; then
      prompt+="Apply this skill to the following topic/context: $input_params

"
    fi

    # Add retry instructions if this is a retry
    if (( attempt > 0 )); then
      local retry_msg
      retry_msg=$(retry_instruction "$last_failure_category" "$attempt" "$last_failure_details" "$skill_name")
      if [[ -n "$retry_msg" ]]; then
        prompt+="IMPORTANT INSTRUCTIONS FOR THIS ATTEMPT:
$retry_msg

"
      fi
    fi

    prompt+="Write your complete output now. Include all required sections with substantive content."

    # Execute via claude CLI
    log_info "Executing claude -p (attempt $((attempt + 1))/$((MAX_RETRIES + 1)))..."
    if ! claude -p --output-format text "$prompt" > "$output_file" 2>/dev/null; then
      log_err "claude CLI execution failed"
      (( attempt++ )) || true
      last_failure_category="missing_file"
      last_failure_details=""
      continue
    fi

    # Validate output
    log_info "Validating output..."
    local validation_result
    if validation_result=$(npx tsx "$SCRIPT_DIR/validate-skill-output.ts" "$skill_name" "$output_file" "$REGISTRY" 2>/dev/null); then
      local end_time duration
      end_time=$(date +%s)
      duration=$((end_time - start_time))
      if (( attempt > 0 )); then
        log_ok "$skill_name PASSED after $attempt retries ($(format_duration $duration))"
      else
        log_ok "$skill_name PASSED ($(format_duration $duration))"
      fi
      success=true
      break
    else
      # Parse failure details
      last_failure_category=$(echo "$validation_result" | python3 -c "import json,sys; print(json.load(sys.stdin).get('failure_category','unknown'))" 2>/dev/null || echo "unknown")
      last_failure_details=$(echo "$validation_result" | python3 -c "
import json, sys
r = json.load(sys.stdin)
checks = r.get('checks', {})
cat = r.get('failure_category', '')
if cat == 'thin_output':
    print(checks.get('min_words', {}).get('actual', '?'))
elif cat == 'missing_sections':
    missing = checks.get('required_sections', {}).get('missing', [])
    print(', '.join(missing))
elif cat == 'placeholder_text':
    found = checks.get('no_placeholders', {}).get('found', [])
    print(', '.join(found))
else:
    print('')
" 2>/dev/null || echo "")

      log_warn "Validation failed: $last_failure_category"
      if [[ -n "$last_failure_details" ]]; then
        log_warn "Details: $last_failure_details"
      fi

      # Handle missing_dir specifically
      if [[ "$last_failure_category" == "missing_dir" ]]; then
        mkdir -p "$(dirname "$output_file")"
      fi

      (( attempt++ )) || true
    fi
  done

  local end_time duration
  end_time=$(date +%s)
  duration=$((end_time - start_time))

  if ! $success; then
    log_err "$skill_name FAILED after $MAX_RETRIES retries ($(format_duration $duration))"
    log_err "Last output: $output_file"
    return 1
  fi

  # Return result as JSON for batch mode to consume
  echo "{\"skill\":\"$skill_name\",\"status\":\"$(if (( attempt > 0 )); then echo "retry_pass"; else echo "pass"; fi)\",\"retries\":$attempt,\"duration\":$duration}"
}

# ── Batch Mode ─────────────────────────────────────────────────────────────

run_batch() {
  local category="${1:-}"
  ensure_registry

  local skills
  skills=$(list_skills "$category")
  local total
  total=$(echo "$skills" | wc -l | tr -d ' ')

  log_info "Starting batch run: $total skills${category:+ (category: $category)}"

  local batch_start results=() passed=0 failed=0 retry_passed=0
  batch_start=$(date +%s)

  local timestamp
  timestamp=$(date +"%Y%m%d-%H%M%S")
  local report_file="$REPORTS_DIR/batch-${timestamp}.md"
  mkdir -p "$REPORTS_DIR"

  local results_json="["
  local first=true

  while IFS= read -r skill; do
    [[ -z "$skill" ]] && continue

    local result_json
    if result_json=$(run_skill "$skill" "" 2>&1 | tail -1) && echo "$result_json" | python3 -c "import json,sys; json.load(sys.stdin)" &>/dev/null; then
      local status
      status=$(echo "$result_json" | python3 -c "import json,sys; print(json.load(sys.stdin)['status'])")
      if [[ "$status" == "pass" ]]; then
        (( passed++ )) || true
      else
        (( retry_passed++ )) || true
      fi
    else
      result_json="{\"skill\":\"$skill\",\"status\":\"fail\",\"retries\":$MAX_RETRIES,\"duration\":0}"
      (( failed++ )) || true
    fi

    if $first; then
      first=false
    else
      results_json+=","
    fi
    results_json+="$result_json"
  done <<< "$skills"

  results_json+="]"

  local batch_end batch_duration
  batch_end=$(date +%s)
  batch_duration=$((batch_end - batch_start))

  # Generate report
  generate_report "$report_file" "$timestamp" "$total" "$passed" "$failed" "$retry_passed" "$batch_duration" "$results_json"

  log_info "Report written to: $report_file"
  echo ""
  log_info "Summary: Total: $total | Passed: $passed | Failed: $failed | Passed with retries: $retry_passed"
  log_info "Duration: $(format_duration $batch_duration)"
}

generate_report() {
  local file="$1" timestamp="$2" total="$3" passed="$4" failed="$5" retry_passed="$6" duration="$7" results_json="$8"

  python3 -c "
import json, sys

results = json.loads('''$results_json''')
total = $total
passed = $passed
failed = $failed
retry_passed = $retry_passed
duration = $duration

mins = duration // 60
secs = duration % 60

report = f'''# Batch Run Report — $timestamp

## Summary
- Total: {total} | Passed: {passed} | Failed: {failed} | Passed with retries: {retry_passed}
- Duration: {mins}m {secs}s

## Results
| Skill | Status | Retries | Duration | Notes |
|---|---|---|---|---|
'''

for r in results:
    skill = r.get('skill', '?')
    status = r.get('status', 'unknown').upper().replace('_', ' ')
    retries = r.get('retries', 0)
    dur = r.get('duration', 0)
    dur_str = f'{dur // 60}m {dur % 60}s' if dur >= 60 else f'{dur}s'
    notes = ''
    if status == 'RETRY PASS':
        notes = f'Passed after {retries} retries'
    elif status == 'FAIL':
        notes = 'Retries exhausted'
    report += f'| {skill} | {status} | {retries} | {dur_str} | {notes} |\n'

# Add failures section
failures = [r for r in results if r.get('status') == 'fail']
if failures:
    report += '\n## Failures\n'
    for r in failures:
        skill = r.get('skill', '?')
        report += f'''### {skill}
- Retries exhausted ({$MAX_RETRIES}/{$MAX_RETRIES})
- Last output: applied/{skill}-batch.md
'''

print(report)
" > "$file"
}

# ── Collectors Mode ────────────────────────────────────────────────────────

run_collectors() {
  local topic="$1"
  ensure_registry

  log_info "Running signal collectors for topic: $topic"

  local attempt=0 max_collector_retries=2
  while (( attempt <= max_collector_retries )); do
    if (( attempt > 0 )); then
      log_warn "Retry $attempt/$max_collector_retries (waiting 5s...)"
      sleep 5
    fi

    if python3 -m collectors --topic "$topic" 2>&1; then
      log_ok "Collectors completed successfully"

      # Verify output files
      local all_exist=true
      python3 -c "
import json
d = json.load(open('$REGISTRY'))
for name, c in d['collectors'].items():
    print(c['output'])
" | while IFS= read -r output_file; do
        if [[ ! -f "$PROJECT_ROOT/$output_file" ]]; then
          log_warn "Expected output missing: $output_file"
          all_exist=false
        else
          log_ok "Found: $output_file"
        fi
      done

      return 0
    fi

    (( attempt++ )) || true
  done

  log_err "Collectors failed after $max_collector_retries retries"
  return 1
}

# ── CLI Entry Point ───────────────────────────────────────────────────────

usage() {
  cat <<EOF
Usage:
  $(basename "$0") run <skill-name> "<input params>"    Run a single skill with validation
  $(basename "$0") batch [--category <category>]        Run all skills (or filtered by category)
  $(basename "$0") collectors "<topic>"                  Run signal collectors
  $(basename "$0") list [--category <category>]          List available skills

Categories: strategic, planning, execution, agent-first, analysis, meta
EOF
}

main() {
  if (( $# < 1 )); then
    usage
    exit 1
  fi

  local cmd="$1"
  shift

  case "$cmd" in
    run)
      if (( $# < 1 )); then
        log_err "Usage: skill-runner.sh run <skill-name> [input-params]"
        exit 1
      fi
      local skill_name="$1"
      local input_params="${2:-}"
      run_skill "$skill_name" "$input_params"
      ;;
    batch)
      local category=""
      while (( $# > 0 )); do
        case "$1" in
          --category) category="$2"; shift 2 ;;
          *) log_err "Unknown option: $1"; exit 1 ;;
        esac
      done
      run_batch "$category"
      ;;
    collectors)
      if (( $# < 1 )); then
        log_err "Usage: skill-runner.sh collectors <topic>"
        exit 1
      fi
      run_collectors "$1"
      ;;
    list)
      local category=""
      while (( $# > 0 )); do
        case "$1" in
          --category) category="$2"; shift 2 ;;
          *) log_err "Unknown option: $1"; exit 1 ;;
        esac
      done
      ensure_registry
      list_skills "$category"
      ;;
    *)
      usage
      exit 1
      ;;
  esac
}

main "$@"
