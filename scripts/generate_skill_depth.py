#!/usr/bin/env python3
"""Generate domain-playbook.md, scenario-catalog.md, and refresh SKILL.md bodies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

OVERRIDES_PATH = Path(__file__).resolve().parent / "skill_depth" / "scenario_overrides.json"

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".agents" / "skills"
PLAYBOOK_SRC = Path(__file__).resolve().parent / "skill_depth" / "playbooks"

# Import shared meta from maintain_repo
sys.path.insert(0, str(ROOT / "scripts"))
from maintain_repo import (  # noqa: E402
    ORCHESTRATOR_TAIL,
    SKILL_META,
    SKILLS as SKILLS_DIR,
    parse_scenarios,
    PURPOSE_RE,
    FRONT_NAME_RE,
)

DOMAIN_PROFILE: dict[str, dict[str, str]] = {
    "security-privacy-auditor": {
        "anchors": "OWASP ASVS 4.0, OWASP Top 10 (2021), CWE, GDPR-style privacy checks where applicable",
        "techniques": "Abuse-case modeling, authZ matrix (horizontal/vertical), injection negative suites, session state machine, secrets/static review, config review",
        "env": "Isolated staging, synthetic users per role, no real PII; burp/mitm only with scope approval",
    },
    "functional-tester": {
        "anchors": "Acceptance criteria, domain invariants, ISO 25010 functional suitability",
        "techniques": "Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters",
        "env": "Seed data per persona; capture DB/API state for oracles",
    },
    "qa-orchestrator": {
        "anchors": "ISO 29119 risk-based strategy, release exit criteria, traceability",
        "techniques": "Risk workshops, gate reviews, coverage reconciliation, multi-agent merge",
        "env": "Access to change list, environments matrix, stakeholder priorities",
    },
    "api-contract-tester": {
        "anchors": "OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP",
        "techniques": "Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants",
        "env": "Mock downstreams or recorded fixtures; versioned API base URL",
    },
    "ux-accessibility-auditor": {
        "anchors": "WCAG 2.2 A/AA, ISO 9241, APG patterns",
        "techniques": "Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom",
        "env": "Real browsers + assistive tech when possible; design tokens reference",
    },
    "ui-visual-tester": {
        "anchors": "Design system, responsive breakpoints, platform HIG/Material",
        "techniques": "Visual diff, layout stress (long text/RTL), state screenshots, component matrix",
        "env": "Pinned browser/OS; stable viewport; disable flaky animations where needed",
    },
    "performance-reliability-tester": {
        "anchors": "SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability",
        "techniques": "Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis",
        "env": "Dedicated perf env; metrics dashboards; never default-load production",
    },
    "data-integrity-tester": {
        "anchors": "ACID expectations, migration notes, backup/restore runbooks",
        "techniques": "Invariant checks, migration dry-run, crash/recovery, referential integrity probes",
        "env": "Disposable DB clone; point-in-time snapshots",
    },
    "logic-concurrency-tester": {
        "anchors": "State machines, locking docs, idempotency contracts",
        "techniques": "Race harness (bounded), double-submit, clock skew simulation, property checks",
        "env": "Controllable parallelism; feature flags for timing hooks",
    },
    "compatibility-localization-tester": {
        "anchors": "Supported matrix doc, CLDR/locale rules, store policies",
        "techniques": "Config matrix, pseudo-locale, RTL, timezone/DST edges",
        "env": "Device farm or emulators per matrix row",
    },
    "exploratory-bug-hunter": {
        "anchors": "Charters, FEW HICCUPPS, session notes",
        "techniques": "Timeboxed tours, SFDPOT, error guessing from change log",
        "env": "Fresh build; logging elevated; safe data",
    },
    "requirements-test-designer": {
        "anchors": "User stories, NFRs, ISO 29119-4 technique mapping",
        "techniques": "Ambiguity mining, testability review, traceability matrix authoring",
        "env": "Access to specs, mocks, and historical defects",
    },
    "test-automation-auditor": {
        "anchors": "Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas",
        "techniques": "Suite audit, mutation sanity, fixture review, pipeline gate analysis",
        "env": "CI history, local reproduce of failed jobs",
    },
    "clean-code-architecture-auditor": {
        "anchors": "SOLID, coupling metrics, ADRs, ISO 25010 maintainability",
        "techniques": "Dependency analysis, boundary violations, change-impact tracing",
        "env": "Static analysis tools read-only; no refactor unless asked",
    },
    "release-readiness-auditor": {
        "anchors": "Exit criteria, change advisory, incident history",
        "techniques": "Evidence aggregation, defect trend, go/no-go workshop structure",
        "env": "RC build ID, signed artifacts list, open risk register",
    },
}

TITLE_HINTS: list[tuple[str, str, str, str]] = [
    (r"auth|session|login|credential", "AuthN/AuthZ abuse cases", "Lockout BVA, MFA bypass attempts, session fixation", "ASVS V2–V4"),
    (r"inject|SQL|command|XSS|escape", "Injection & encoding", "Payload catalog (safe), context-aware encoding oracle", "ASVS V5"),
    (r"CSRF|SSRF|traversal|deserial", "Web abuse", "Cross-origin, URL fetch, path canonicalization", "OWASP Top 10"),
    (r"authoriz|privilege|tenant|unauthor", "Access control", "IDOR grid two users × N objects", "ASVS V4"),
    (r"performance|load|cold start|budget", "Measured execution", "Baseline + % regression threshold", "SLO doc"),
    (r"accessib|WCAG|keyboard|screen", "Inclusive interaction", "Keyboard path, name/role/value, contrast", "WCAG 2.2"),
    (r"API|contract|schema|pagination", "Contract conformance", "Schema validation, error shape, versioning", "OpenAPI + RFC 7231"),
    (r"migrat|persist|integrity|atomic", "Data correctness", "Before/after snapshots, checksums", "Schema + invariants"),
    (r"concurr|race|lock|idempot", "Timing & invariants", "Parallel workers N=2..5 bounded", "Design spec"),
    (r"locale|i18n|Unicode|RTL|timezone", "Locale matrix", "Pseudo-loc, RTL mirror, DST boundary", "CLDR / matrix doc"),
    (r"visual|layout|hierarchy", "Perceptual consistency", "Breakpoint sweep, overflow strings", "Design system"),
    (r"explor|tour|charter", "Session-based ET", "90-min charter, debrief table", "Charter template"),
    (r"traceab|requirement|ambiguous", "Testability", "Given-when-then rewrite, measurable AC", "Req IDs"),
    (r"automation|CI|flake|regression suite", "Automation health", "Quarantine list, flake rate, runtime budget", "Pipeline config"),
    (r"architect|coupling|maintain", "Structure review", "Forbidden dependency rules", "ADRs"),
    (r"release|ship|exit|readiness", "Gate evidence", "Residual risk table, sign-offs", "Exit criteria doc"),
]


def load_scenario_overrides() -> dict[str, dict]:
    if not OVERRIDES_PATH.is_file():
        return {}
    return json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))


def hint_for_title(title: str) -> tuple[str, str, str]:
    t = title.lower()
    for pattern, focus, variants, anchor in TITLE_HINTS:
        if re.search(pattern, t):
            return focus, variants, anchor
    return (
        "Core behavior vs documented intent",
        "Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable",
        "Requirements + domain rules",
    )


def scenario_section(
    skill: str, case_id: str, title: str, overrides: dict[str, dict]
) -> str:
    profile = DOMAIN_PROFILE.get(skill, {})
    ov = overrides.get(case_id)
    if ov:
        badge = "**Tier:** P0 manual override (high-risk catalog)\n\n"
        objective = ov["objective"]
        techniques = ov["primary_techniques"]
        focus = ov["scenario_focus"]
        variants = ov["variant_matrix"]
        anchors = ov["oracle_anchor"]
        failures = ov["failure_signals"]
        evidence = ov["evidence"]
        minimum = ov["minimum_atomic_cases"]
    else:
        badge = ""
        focus, variants, anchor = hint_for_title(title)
        techniques = profile.get("techniques", "See test-design-techniques.md")
        anchors = profile.get("anchors", anchor)
        objective = (
            f"Prove or disprove that *{title.lower()}* holds under realistic "
            "abuse and normal use within scope."
        )
        failures = (
            "Wrong HTTP/business code, data leak across tenants, silent corruption, "
            "misleading UX, missing audit event"
        )
        evidence = (
            "Redacted request/response, HAR snippet, screenshot + DOM snapshot, "
            "SQL row count, log correlation ID"
        )
        minimum = (
            f"≥3 derived IDs (e.g. `{case_id}a` happy, `{case_id}b` negative, "
            f"`{case_id}c` boundary or auth) before PASS"
        )

    section = f"""### {case_id} — {title}

{badge}| Dimension | Guidance |
|-----------|----------|
| **Objective** | {objective} |
| **Primary techniques** | {techniques} |
| **Scenario focus** | {focus} |
| **Variant matrix** | {variants} |
| **Oracle / anchor** | {anchors} |
| **Failure signals** | {failures} |
| **Evidence** | {evidence} |
| **Minimum atomic cases** | {minimum} |

"""
    if ov and ov.get("atomic_examples"):
        section += "**Example atomic breakdown:**\n"
        for line in ov["atomic_examples"]:
            section += f"- {line}\n"
        section += "\n"
    return section


def build_scenario_catalog(
    skill: str, scenarios: list[tuple[str, str]], overrides: dict[str, dict]
) -> str:
    profile = DOMAIN_PROFILE.get(skill, {})
    override_ids = [cid for cid, _ in scenarios if cid in overrides]
    header = f"""# Scenario catalog — {skill}

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** {profile.get("anchors", "Project specs + quality-attribute-model.md")}  
**Typical environment:** {profile.get("env", "Staging or local with approved fixtures")}  
**P0 deep specs in this skill:** {", ".join(override_ids) if override_ids else "none (use generic rows)"}

"""
    body = "".join(
        scenario_section(skill, cid, title, overrides) for cid, title in scenarios
    )
    return header + body


def build_skill_md_rich(
    name: str,
    purpose: str,
    scenarios: list[tuple[str, str]],
    extra: str,
    overrides: dict[str, dict],
) -> str:
    tagline, focus = SKILL_META.get(name, (purpose.rstrip("."), name.replace("-", " ")))
    profile = DOMAIN_PROFILE.get(name, {})
    p0_ids = [cid for cid, _ in scenarios if cid in overrides]
    p0_line = (
        f"\n**P0 scenarios (manual deep specs):** {', '.join(p0_ids)}\n"
        if p0_ids
        else ""
    )
    desc = (
        f"{tagline} Deep playbooks and per-scenario specs in references/. "
        f"Use for {focus}. Structured markdown reports required."
    )
    scenario_lines = "\n".join(
        f"| {cid} | {title} | `scenario-catalog.md#{cid.lower()}` |"
        for cid, title in scenarios
    )
    return f"""---
name: {name}
description: "{desc}"
---

# {name}

**Purpose:** {purpose}

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** {profile.get("anchors", "See domain-playbook.md")}
{p0_line}
## Operating procedure

| Step | Action |
|------|--------|
| 1 | Intake scope, change diff, environments, and data classification |
| 2 | Build risk table (impact × likelihood) tagged with ISO 25010 characteristic |
| 3 | Map risks → catalog IDs → atomic test IDs with technique column filled |
| 4 | Prepare fixtures; block destructive/out-of-scope actions |
| 5 | Execute highest risk first; log commands, builds, and correlation IDs |
| 6 | Classify each result with evidence tier (CONFIRMED / LIKELY / NOT TESTED / …) |
| 7 | File defects with independent oracle cited; separate speculative risks |
| 8 | Summarize gaps, blocked items, and regression candidates in tables |
| 9 | Copy `verification-checklist.md` with honest marks |
| 10 | Deliver per `execution-report-template.md` |

## Report presentation (required)

Matrices, defects, and gates must use **`references/report-output-format.md`**. No prose-only reports.

## Scenario index

| Case | Focus | Deep specification |
|------|-------|-------------------|
{scenario_lines}

## Verification checklist

Copy `references/verification-checklist.md` into the final report.
{extra}
"""


def generate_for_skill(skill_dir: Path) -> None:
    skill = skill_dir.name
    skill_path = skill_dir / "SKILL.md"
    if not skill_path.is_file():
        return
    text = skill_path.read_text(encoding="utf-8")
    scenarios = parse_scenarios(text)
    if not scenarios:
        return

    refs = skill_dir / "references"
    refs.mkdir(parents=True, exist_ok=True)

    playbook_src = PLAYBOOK_SRC / f"{skill}.md"
    if playbook_src.is_file():
        (refs / "domain-playbook.md").write_text(
            playbook_src.read_text(encoding="utf-8"), encoding="utf-8"
        )

    overrides = load_scenario_overrides()
    (refs / "scenario-catalog.md").write_text(
        build_scenario_catalog(skill, scenarios, overrides), encoding="utf-8"
    )

    name_m = FRONT_NAME_RE.search(text)
    purpose_m = PURPOSE_RE.search(text)
    name = name_m.group(1) if name_m else skill
    purpose = purpose_m.group(1).strip() if purpose_m else SKILL_META.get(skill, ("", ""))[0]
    extra = ORCHESTRATOR_TAIL if name == "qa-orchestrator" else ""
    skill_path.write_text(
        build_skill_md_rich(name, purpose, scenarios, extra, overrides),
        encoding="utf-8",
    )


def main() -> int:
    overrides = load_scenario_overrides()
    if len(overrides) < 50:
        print(f"expected >=50 scenario overrides, found {len(overrides)}")
        return 1
    missing = []
    for skill_dir in sorted(SKILLS.iterdir()):
        if not skill_dir.is_dir() or skill_dir.name.startswith("_"):
            continue
        pb = PLAYBOOK_SRC / f"{skill_dir.name}.md"
        if not pb.is_file():
            missing.append(skill_dir.name)
        generate_for_skill(skill_dir)
    if missing:
        print("missing playbooks:", ", ".join(missing))
        return 1
    print("generate_skill_depth: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
