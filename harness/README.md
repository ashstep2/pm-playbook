# Self-Healing Skill Execution Harness

Automated execution, validation, and retry system for PM Playbooks skills using `claude -p`.

## Setup

```bash
cd harness && npm install
```

## Usage

### Build the skill registry

Scans all `SKILL.md` files and generates `skill-registry.json`:

```bash
./harness/build-registry.sh
```

### Run a single skill

```bash
./harness/skill-runner.sh run competitive-response "Braintrust vs Langsmith"
```

This will:
1. Read the skill's `SKILL.md` and construct a prompt
2. Execute via `claude -p --output-format text`
3. Validate the output against quality criteria (word count, required sections, placeholders, etc.)
4. Retry up to 3 times with smart, failure-specific instructions if validation fails

Output lands in `applied/<skill-name>-<sanitized-params>.md`.

### Run all skills (batch mode)

```bash
# All skills
./harness/skill-runner.sh batch

# Filter by category
./harness/skill-runner.sh batch --category strategic
```

Categories: `strategic`, `planning`, `execution`, `agent-first`, `analysis`, `meta`

Produces a summary report in `harness/reports/batch-<timestamp>.md`.

### Run signal collectors

```bash
./harness/skill-runner.sh collectors "Braintrust vs Langsmith"
```

### List available skills

```bash
./harness/skill-runner.sh list
./harness/skill-runner.sh list --category agent-first
```

## Validation Checks

Each skill output is validated against these criteria:

| Check | What it does |
|---|---|
| `file_exists` | Output file was created |
| `not_empty` | File has content (> 0 bytes) |
| `min_words` | Meets minimum word count (default: 500) |
| `required_sections` | All expected artifact sections present as markdown headers |
| `no_placeholders` | No TODO, TBD, PLACEHOLDER, or [INSERT text |
| `no_empty_headers` | Every header has content beneath it |
| `min_sections` | Meets minimum section count |

### Smart Retry Logic

When validation fails, the retry uses failure-specific instructions:

| Failure | Retry strategy |
|---|---|
| `missing_dir` | Create directory, retry |
| `missing_file` | Add explicit "write output" instruction |
| `thin_output` | Request more comprehensive analysis with word count target |
| `missing_sections` | List missing sections explicitly |
| `placeholder_text` | Instruct to fill all sections with real analysis |
| `empty_headers` | Require substantive content under every header |

Each retry escalates: attempt 2 adds urgency, attempt 3 lists all required sections explicitly.

## Files

```
harness/
├── build-registry.sh          # Generates skill-registry.json from SKILL.md files
├── skill-runner.sh            # Main runner: single skill, batch, collectors
├── validate-skill-output.ts   # TypeScript validation module
├── skill-registry.json        # Auto-generated (do not edit manually)
├── package.json               # tsx dependency
├── tsconfig.json              # TypeScript config
├── reports/                   # Batch run reports
└── README.md                  # This file
```

## Run the validator directly

```bash
npx tsx harness/validate-skill-output.ts <skill-name> <output-file> [registry-path]
```

Returns JSON with check results and a `failure_category` for programmatic use.
