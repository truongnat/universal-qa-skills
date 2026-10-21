---
name: release-readiness-auditor
description: "Evidence-backed ship / no-ship assessment. Deep playbooks and per-scenario specs in references/. Use for release readiness. Structured markdown reports required."
---

# release-readiness-auditor

**Purpose:** Evidence-backed ship/no-ship. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Exit criteria, change advisory, incident history

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
| RELE-001 | Artifact identity | `scenario-catalog.md#rele-001` |
| RELE-002 | Reproducible build | `scenario-catalog.md#rele-002` |
| RELE-003 | Package launch | `scenario-catalog.md#rele-003` |
| RELE-004 | Install and uninstall | `scenario-catalog.md#rele-004` |
| RELE-005 | Upgrade smoke test | `scenario-catalog.md#rele-005` |
| RELE-006 | Critical journey evidence | `scenario-catalog.md#rele-006` |
| RELE-007 | Outstanding critical defects | `scenario-catalog.md#rele-007` |
| RELE-008 | Dependency security checks | `scenario-catalog.md#rele-008` |
| RELE-009 | Privacy checks | `scenario-catalog.md#rele-009` |
| RELE-010 | Accessibility target | `scenario-catalog.md#rele-010` |
| RELE-011 | Performance budget | `scenario-catalog.md#rele-011` |
| RELE-012 | Backup restore readiness | `scenario-catalog.md#rele-012` |
| RELE-013 | Monitoring readiness | `scenario-catalog.md#rele-013` |
| RELE-014 | Incident response ownership | `scenario-catalog.md#rele-014` |
| RELE-015 | Release notes accuracy | `scenario-catalog.md#rele-015` |
| RELE-016 | Feature flag rollback | `scenario-catalog.md#rele-016` |
| RELE-017 | Data migration readiness | `scenario-catalog.md#rele-017` |
| RELE-018 | Skipped tests reviewed | `scenario-catalog.md#rele-018` |
| RELE-019 | Cross-platform evidence | `scenario-catalog.md#rele-019` |
| RELE-020 | Formal exception sign-off | `scenario-catalog.md#rele-020` |
| RELE-021 | Rollout monitoring | `scenario-catalog.md#rele-021` |
| RELE-022 | Rollback thresholds | `scenario-catalog.md#rele-022` |
| RELE-023 | Code signing | `scenario-catalog.md#rele-023` |
| RELE-024 | Post-release verification | `scenario-catalog.md#rele-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

