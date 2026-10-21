---
name: requirements-test-designer
description: "Standards-informed requirements analysis and test design. Deep playbooks and per-scenario specs in references/. Use for requirements and test design. Structured markdown reports required."
---

# requirements-test-designer

**Purpose:** Standards-informed test design. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** User stories, NFRs, ISO 29119-4 technique mapping

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
| REQU-001 | Ambiguous acceptance criteria | `scenario-catalog.md#requ-001` |
| REQU-002 | Mandatory optional fields | `scenario-catalog.md#requ-002` |
| REQU-003 | Empty null missing values | `scenario-catalog.md#requ-003` |
| REQU-004 | Whitespace and trim policy | `scenario-catalog.md#requ-004` |
| REQU-005 | Input min boundary | `scenario-catalog.md#requ-005` |
| REQU-006 | Input max boundary | `scenario-catalog.md#requ-006` |
| REQU-007 | Off-by-one errors | `scenario-catalog.md#requ-007` |
| REQU-008 | Equivalent valid classes | `scenario-catalog.md#requ-008` |
| REQU-009 | Equivalent invalid classes | `scenario-catalog.md#requ-009` |
| REQU-010 | Decision table interactions | `scenario-catalog.md#requ-010` |
| REQU-011 | State transition validity | `scenario-catalog.md#requ-011` |
| REQU-012 | Role and permission matrix | `scenario-catalog.md#requ-012` |
| REQU-013 | Idempotency expectations | `scenario-catalog.md#requ-013` |
| REQU-014 | Duplicate submission | `scenario-catalog.md#requ-014` |
| REQU-015 | Date and time rules | `scenario-catalog.md#requ-015` |
| REQU-016 | Timezone and DST | `scenario-catalog.md#requ-016` |
| REQU-017 | Decimal and rounding | `scenario-catalog.md#requ-017` |
| REQU-018 | Unicode normalization | `scenario-catalog.md#requ-018` |
| REQU-019 | Feature flag behavior | `scenario-catalog.md#requ-019` |
| REQU-020 | Migration acceptance | `scenario-catalog.md#requ-020` |
| REQU-021 | Partial success semantics | `scenario-catalog.md#requ-021` |
| REQU-022 | Interrupted operations | `scenario-catalog.md#requ-022` |
| REQU-023 | Test oracle independence | `scenario-catalog.md#requ-023` |
| REQU-024 | Traceability completeness | `scenario-catalog.md#requ-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

