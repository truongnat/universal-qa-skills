---
name: exploratory-bug-hunter
description: "Session-based exploratory testing and defect discovery. Deep playbooks and per-scenario specs in references/. Use for exploratory testing. Structured markdown reports required."
---

# exploratory-bug-hunter

**Purpose:** Session-based exploratory defect discovery. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Charters, FEW HICCUPPS, session notes

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
| EXPL-001 | New user tour | `scenario-catalog.md#expl-001` |
| EXPL-002 | Expert workflow tour | `scenario-catalog.md#expl-002` |
| EXPL-003 | Error recovery tour | `scenario-catalog.md#expl-003` |
| EXPL-004 | Input boundary tour | `scenario-catalog.md#expl-004` |
| EXPL-005 | Interrupt and retry tour | `scenario-catalog.md#expl-005` |
| EXPL-006 | Rapid navigation | `scenario-catalog.md#expl-006` |
| EXPL-007 | Permission switching | `scenario-catalog.md#expl-007` |
| EXPL-008 | Data lifecycle | `scenario-catalog.md#expl-008` |
| EXPL-009 | Malformed inputs | `scenario-catalog.md#expl-009` |
| EXPL-010 | Large dataset | `scenario-catalog.md#expl-010` |
| EXPL-011 | Localization tour | `scenario-catalog.md#expl-011` |
| EXPL-012 | Keyboard-only exploration | `scenario-catalog.md#expl-012` |
| EXPL-013 | Offline tour | `scenario-catalog.md#expl-013` |
| EXPL-014 | Multi-session tour | `scenario-catalog.md#expl-014` |
| EXPL-015 | Upgrade tour | `scenario-catalog.md#expl-015` |
| EXPL-016 | Unexpected combinations | `scenario-catalog.md#expl-016` |
| EXPL-017 | Repeated cancellation | `scenario-catalog.md#expl-017` |
| EXPL-018 | Time anomalies | `scenario-catalog.md#expl-018` |
| EXPL-019 | Resource exhaustion | `scenario-catalog.md#expl-019` |
| EXPL-020 | Cross-feature integration | `scenario-catalog.md#expl-020` |
| EXPL-021 | State switching | `scenario-catalog.md#expl-021` |
| EXPL-022 | Random replayable sequence | `scenario-catalog.md#expl-022` |
| EXPL-023 | Visual consistency | `scenario-catalog.md#expl-023` |
| EXPL-024 | Unexpected data loss | `scenario-catalog.md#expl-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

