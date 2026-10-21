---
name: functional-tester
description: "Critical user journey and business-flow verification. Deep playbooks and per-scenario specs in references/. Use for functional user journeys. Structured markdown reports required."
---

# functional-tester

**Purpose:** Critical user journey verification. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Acceptance criteria, domain invariants, ISO 25010 functional suitability

**P0 scenarios (manual deep specs):** FUNC-003, FUNC-006, FUNC-008, FUNC-009, FUNC-010, FUNC-019, FUNC-020, FUNC-021, FUNC-023, FUNC-024

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
| FUNC-001 | First run and onboarding | `scenario-catalog.md#func-001` |
| FUNC-002 | Create valid entity | `scenario-catalog.md#func-002` |
| FUNC-003 | Create invalid entity | `scenario-catalog.md#func-003` |
| FUNC-004 | Duplicate record handling | `scenario-catalog.md#func-004` |
| FUNC-005 | Read missing record | `scenario-catalog.md#func-005` |
| FUNC-006 | Read unauthorized record | `scenario-catalog.md#func-006` |
| FUNC-007 | Update valid record | `scenario-catalog.md#func-007` |
| FUNC-008 | Update conflict | `scenario-catalog.md#func-008` |
| FUNC-009 | Delete confirmation | `scenario-catalog.md#func-009` |
| FUNC-010 | Delete recovery | `scenario-catalog.md#func-010` |
| FUNC-011 | Search exact case | `scenario-catalog.md#func-011` |
| FUNC-012 | Search Unicode | `scenario-catalog.md#func-012` |
| FUNC-013 | Filter combinations | `scenario-catalog.md#func-013` |
| FUNC-014 | Sorting stability | `scenario-catalog.md#func-014` |
| FUNC-015 | Pagination boundaries | `scenario-catalog.md#func-015` |
| FUNC-016 | Bulk actions | `scenario-catalog.md#func-016` |
| FUNC-017 | Import malformed rows | `scenario-catalog.md#func-017` |
| FUNC-018 | Export fidelity | `scenario-catalog.md#func-018` |
| FUNC-019 | Unsaved state protection | `scenario-catalog.md#func-019` |
| FUNC-020 | Session expiry | `scenario-catalog.md#func-020` |
| FUNC-021 | Offline to online recovery | `scenario-catalog.md#func-021` |
| FUNC-022 | Background cancellation | `scenario-catalog.md#func-022` |
| FUNC-023 | Restart persistence | `scenario-catalog.md#func-023` |
| FUNC-024 | Multi-user collaboration | `scenario-catalog.md#func-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

