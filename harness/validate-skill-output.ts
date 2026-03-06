#!/usr/bin/env npx tsx
/**
 * validate-skill-output.ts
 *
 * Validates a skill output file against quality criteria from the skill registry.
 *
 * Usage: npx tsx validate-skill-output.ts <skill-name> <output-file> [registry-path]
 *
 * Outputs a JSON validation result to stdout.
 */

import { readFileSync, existsSync, statSync } from "fs";
import { dirname, resolve } from "path";

// ── Types ─────────────────────────────────────────────────────────────────

interface QualityCriteria {
  min_word_count: number;
  required_sections: string[];
  no_placeholders: string[];
  min_sections: number;
}

interface SkillEntry {
  name: string;
  description: string;
  version: string;
  category: string;
  skill_path: string;
  output_dir: string;
  output_pattern: string;
  expected_artifacts: string[];
  quality: QualityCriteria;
  feeds_into: string[];
  reads_from: string[];
}

interface Registry {
  skills: Record<string, SkillEntry>;
  collectors: Record<string, { script: string; output: string }>;
  generated_at: string;
}

interface CheckResult {
  passed: boolean;
  [key: string]: unknown;
}

interface ValidationResult {
  skill: string;
  file: string;
  passed: boolean;
  checks: Record<string, CheckResult>;
  failure_category: string | null;
}

// ── Validation Checks ─────────────────────────────────────────────────────

function checkFileExists(filePath: string): CheckResult {
  return { passed: existsSync(filePath) };
}

function checkNotEmpty(filePath: string): CheckResult {
  if (!existsSync(filePath)) return { passed: false, bytes: 0 };
  const stats = statSync(filePath);
  return { passed: stats.size > 0, bytes: stats.size };
}

function checkMinWords(content: string, minWords: number): CheckResult {
  const words = content
    .replace(/[#*_\-|`>]/g, " ")
    .split(/\s+/)
    .filter((w) => w.length > 0);
  return {
    passed: words.length >= minWords,
    actual: words.length,
    required: minWords,
  };
}

function checkRequiredSections(
  content: string,
  sections: string[]
): CheckResult {
  if (sections.length === 0) return { passed: true, missing: [] };

  const missing: string[] = [];
  for (const section of sections) {
    // Check for section as a markdown header (## or ###) or as bold text
    const escapedSection = section.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
    const headerPattern = new RegExp(
      `^#{1,4}\\s+.*${escapedSection}`,
      "im"
    );
    const boldPattern = new RegExp(`\\*\\*${escapedSection}\\*\\*`, "i");

    if (!headerPattern.test(content) && !boldPattern.test(content)) {
      missing.push(section);
    }
  }

  return { passed: missing.length === 0, missing };
}

function checkNoPlaceholders(
  content: string,
  placeholders: string[]
): CheckResult {
  const found: string[] = [];
  for (const placeholder of placeholders) {
    if (content.includes(placeholder)) {
      found.push(placeholder);
    }
  }
  return { passed: found.length === 0, found };
}

function checkNoEmptyHeaders(content: string): CheckResult {
  const lines = content.split("\n");
  const emptyHeaders: string[] = [];

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i].trim();
    if (!line.match(/^#{1,6}\s+/)) continue;

    // Look ahead: skip blank lines, check if next non-blank is another header or EOF
    let j = i + 1;
    while (j < lines.length && lines[j].trim() === "") j++;

    if (j >= lines.length) {
      // Header at end of file with no content after
      emptyHeaders.push(line);
    } else if (lines[j].trim().match(/^#{1,6}\s+/)) {
      // Next non-blank line is another header
      emptyHeaders.push(line);
    }
  }

  return { passed: emptyHeaders.length === 0, empty_headers: emptyHeaders };
}

function checkMinSections(content: string, minSections: number): CheckResult {
  const headers = content.match(/^#{1,6}\s+.+/gm) || [];
  return {
    passed: headers.length >= minSections,
    actual: headers.length,
    required: minSections,
  };
}

// ── Failure Category ──────────────────────────────────────────────────────

function determineFailureCategory(
  checks: Record<string, CheckResult>,
  filePath: string
): string | null {
  if (!checks.file_exists.passed) {
    const dir = dirname(filePath);
    if (!existsSync(dir)) return "missing_dir";
    return "missing_file";
  }
  if (!checks.not_empty?.passed) return "missing_file";
  if (!checks.no_placeholders.passed) return "placeholder_text";
  if (!checks.no_empty_headers.passed) return "empty_headers";
  if (!checks.required_sections.passed) return "missing_sections";
  if (!checks.min_words.passed) return "thin_output";
  if (!checks.min_sections.passed) return "missing_sections";
  return null;
}

// ── Main ──────────────────────────────────────────────────────────────────

function validate(
  skillName: string,
  outputFile: string,
  registryPath: string
): ValidationResult {
  // Load registry
  const registry: Registry = JSON.parse(readFileSync(registryPath, "utf-8"));
  const skill = registry.skills[skillName];

  if (!skill) {
    return {
      skill: skillName,
      file: outputFile,
      passed: false,
      checks: {
        registry_lookup: { passed: false, error: `Skill '${skillName}' not found in registry` },
      },
      failure_category: "missing_file",
    };
  }

  const quality = skill.quality;
  const filePath = resolve(outputFile);

  // Run all checks
  const checks: Record<string, CheckResult> = {};

  checks.file_exists = checkFileExists(filePath);

  if (!checks.file_exists.passed) {
    // Can't run content checks without a file
    checks.not_empty = { passed: false, bytes: 0 };
    checks.min_words = { passed: false, actual: 0, required: quality.min_word_count };
    checks.required_sections = { passed: quality.required_sections.length === 0, missing: quality.required_sections };
    checks.no_placeholders = { passed: true };
    checks.no_empty_headers = { passed: true };
    checks.min_sections = { passed: false, actual: 0, required: quality.min_sections };
  } else {
    const content = readFileSync(filePath, "utf-8");
    checks.not_empty = checkNotEmpty(filePath);
    checks.min_words = checkMinWords(content, quality.min_word_count);
    checks.required_sections = checkRequiredSections(content, quality.required_sections);
    checks.no_placeholders = checkNoPlaceholders(content, quality.no_placeholders);
    checks.no_empty_headers = checkNoEmptyHeaders(content);
    checks.min_sections = checkMinSections(content, quality.min_sections);
  }

  const passed = Object.values(checks).every((c) => c.passed);
  const failure_category = passed ? null : determineFailureCategory(checks, filePath);

  return {
    skill: skillName,
    file: outputFile,
    passed,
    checks,
    failure_category,
  };
}

// ── CLI Entry Point ───────────────────────────────────────────────────────

const args = process.argv.slice(2);
if (args.length < 2) {
  console.error(
    "Usage: npx tsx validate-skill-output.ts <skill-name> <output-file> [registry-path]"
  );
  process.exit(2);
}

const [skillName, outputFile] = args;
const registryPath = args[2] || resolve(dirname(new URL(import.meta.url).pathname), "skill-registry.json");

const result = validate(skillName, outputFile, registryPath);
console.log(JSON.stringify(result, null, 2));
process.exit(result.passed ? 0 : 1);
