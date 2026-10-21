#!/usr/bin/env python3
"""Sync shared references and reshape SKILL.md files. Run from repo root."""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
SHARED_REFS = SKILLS / "_shared" / "references"

SKILL_META: dict[str, tuple[str, str]] = {
    "api-contract-tester": (
        "Protocol and integration contract verification.",
        "API contracts, schemas, and integration boundaries",
    ),
    "clean-code-architecture-auditor": (
        "Maintainability, coupling, and architectural boundary review.",
        "code structure and architecture",
    ),
    "compatibility-localization-tester": (
        "Platform matrix, locale, and internationalization checks.",
        "compatibility and i18n/l10n",
    ),
    "data-integrity-tester": (
        "Persistence, migration, and data recovery correctness.",
        "data integrity and persistence",
    ),
    "exploratory-bug-hunter": (
        "Session-based exploratory testing and defect discovery.",
        "exploratory testing",
    ),
    "functional-tester": (
        "Critical user journey and business-flow verification.",
        "functional user journeys",
    ),
    "logic-concurrency-tester": (
        "State machines, timing, races, and invariants.",
        "logic and concurrency",
    ),
    "performance-reliability-tester": (
        "Measured performance, resilience, and failure handling.",
        "performance and reliability",
    ),
    "qa-orchestrator": (
        "Risk-based QA coordination, delegation, and release gates.",
        "end-to-end QA orchestration",
    ),
    "release-readiness-auditor": (
        "Evidence-backed ship / no-ship assessment.",
        "release readiness",
    ),
    "requirements-test-designer": (
        "Standards-informed requirements analysis and test design.",
        "requirements and test design",
    ),
    "security-privacy-auditor": (
        "Security verification and privacy-sensitive flows.",
        "security and privacy",
    ),
    "test-automation-auditor": (
        "Test automation quality, CI signals, and flake resistance.",
        "test automation and CI",
    ),
    "ui-visual-tester": (
        "Native and web visual integrity and layout regression.",
        "UI and visual quality",
    ),
    "ux-accessibility-auditor": (
        "Usability, WCAG-oriented accessibility, and inclusive UX.",
        "UX and accessibility",
    ),
}

ORCHESTRATOR_TAIL = """
## Multi-agent orchestration
Read **bundled** `agents/qa-lead.md`, `workflows/multi-agent-protocol.md`, `workflows/dispatch-template.md` (paths relative to this skill). The orchestrator owns dispatch, reconciliation, and release gate review. Use real native subagent tools when available. If the host does not support subagent spawning, execute specialists sequentially and disclose this. **Do not claim native agent registration**: agent definitions are bundled role prompts, not automatically installed CLI agents. Delegate bounded read-only tasks with independent evidence paths, and challenge high-severity findings in a second pass. Workers should read installed specialist skills via host skill discovery, not hard-coded project paths. Final merged output must follow `references/report-output-format.md` (tables for matrices, gates, and handoffs).
"""

SCENARIO_RE = re.compile(
    r"^\|\s*([A-Z]+-\d+)\s*\|\s*([^|]+?)\s*\|",
    re.MULTILINE,
)
FRONT_NAME_RE = re.compile(r"^name:\s*(\S+)\s*$", re.MULTILINE)
PURPOSE_RE = re.compile(r"\*\*Purpose:\*\*\s*(.+)", re.MULTILINE)


def sync_shared_references() -> list[str]:
    errors: list[str] = []
    if not SHARED_REFS.is_dir():
        errors.append(f"Missing {SHARED_REFS}")
        return errors
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        dest = skill_dir / "references"
        dest.mkdir(parents=True, exist_ok=True)
        for src in sorted(SHARED_REFS.iterdir()):
            if src.is_file():
                target = dest / src.name
                data = src.read_bytes()
                if target.exists() and target.read_bytes() == data:
                    continue
                target.write_bytes(data)
    return errors


def parse_scenarios(text: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for m in SCENARIO_RE.finditer(text):
        case_id, title = m.group(1), m.group(2).strip()
        if case_id == "Case":
            continue
        rows.append((case_id, title))
    return rows


def build_skill_md(name: str, purpose: str, scenarios: list[tuple[str, str]], extra: str) -> str:
    tagline, focus = SKILL_META.get(
        name,
        (purpose.rstrip("."), name.replace("-", " ")),
    )
    desc = (
        f"{tagline} Use for {focus} in any software project. "
        "Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
    )
    scenario_lines = "\n".join(f"| {cid} | {title} |" for cid, title in scenarios)
    return f"""---
name: {name}
description: "{desc}"
---

# {name}

**Purpose:** {purpose}

## Mandatory testing contract
Read and apply bundled `references/mandatory-contract.md`, `references/quality-standard.md`, and `references/report-output-format.md` before testing or reporting.

## Report presentation (required)
All results, matrices, defect logs, gap analyses, and release assessments must follow **`references/report-output-format.md`** and, when executing a run, **`references/execution-report-template.md`**. Use **markdown tables** for counts and traceability, **headed sections** for narrative, and **bullets or numbered lists** for steps and actions. Do not deliver wall-of-text-only output.

## Output artifacts
| Artifact | Format |
|---|---|
| Risk & scope inventory | Table + short bullets |
| Test design / execution matrix | Table (see report-output-format) |
| Confirmed findings | Defect table + repro steps |
| Hypothetical risks | Separate table or subsection |
| Coverage gaps / blockers | Table |
| Regression backlog | Prioritized table |
| Final checklist | From `references/verification-checklist.md` |

## Scenario catalog

Each row is a scenario-design prompt, **not** an executed test. Expand using `references/scenario-expansion-guide.md` before marking PASS.

| Case | Scenario focus |
|---|---|
{scenario_lines}

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.
{extra}
"""


def reshape_skills() -> list[str]:
    errors: list[str] = []
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        skill_path = skill_dir / "SKILL.md"
        if not skill_path.is_file():
            errors.append(f"No SKILL.md in {skill_dir.name}")
            continue
        text = skill_path.read_text(encoding="utf-8")
        name_m = FRONT_NAME_RE.search(text)
        purpose_m = PURPOSE_RE.search(text)
        if not name_m or not purpose_m:
            errors.append(f"Could not parse name/purpose in {skill_path}")
            continue
        name = name_m.group(1)
        purpose = purpose_m.group(1).strip()
        scenarios = parse_scenarios(text)
        if not scenarios:
            errors.append(f"No scenarios in {skill_path}")
            continue
        extra = ORCHESTRATOR_TAIL if name == "qa-orchestrator" else ""
        skill_path.write_text(
            build_skill_md(name, purpose, scenarios, extra),
            encoding="utf-8",
        )
    return errors


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    expected_scenarios = 356
    total = 0
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        skill_path = skill_dir / "SKILL.md"
        text = skill_path.read_text(encoding="utf-8")
        if "report-output-format.md" not in text:
            errors.append(f"{skill_dir.name}: missing report-output-format reference")
        if "mandatory-contract.md" not in text:
            errors.append(f"{skill_dir.name}: missing mandatory-contract reference")
        n = len(parse_scenarios(text))
        total += n
        refs = skill_dir / "references"
        for src in SHARED_REFS.iterdir():
            if not src.is_file():
                continue
            dest = refs / src.name
            if not dest.is_file():
                errors.append(f"{skill_dir.name}: missing reference {src.name}")
            elif file_hash(src) != file_hash(dest):
                errors.append(f"{skill_dir.name}: stale reference {src.name} (run sync)")
    if total != expected_scenarios:
        errors.append(f"Scenario count {total} != {expected_scenarios}")
    readme = ROOT / "README.md"
    if readme.is_file() and str(expected_scenarios) not in readme.read_text():
        errors.append("README missing scenario count 356")
    return errors


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "all"
    if cmd in ("sync", "all"):
        for e in sync_shared_references():
            print("sync:", e)
    if cmd in ("reshape", "all"):
        for e in reshape_skills():
            print("reshape:", e)
    if cmd in ("validate", "all"):
        errs = validate()
        if errs:
            for e in errs:
                print("validate:", e)
            return 1
        print("validate: OK (356 scenarios, shared references in sync)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
