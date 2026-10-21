---
name: data-integrity-tester
description: "Persistence, migration, and data recovery correctness. Deep playbooks and per-scenario specs in references/. Use for data integrity and persistence. Structured markdown reports required."
---

# data-integrity-tester

**Purpose:** Persistence correctness and recovery. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** ACID expectations, migration notes, backup/restore runbooks

**P0 scenarios (manual deep specs):** DATA-001, DATA-002, DATA-003, DATA-012, DATA-015, DATA-024

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
| DATA-001 | Atomic mutation | `scenario-catalog.md#data-001` |
| DATA-002 | Isolation anomalies | `scenario-catalog.md#data-002` |
| DATA-003 | Durability after crash | `scenario-catalog.md#data-003` |
| DATA-004 | Constraint enforcement | `scenario-catalog.md#data-004` |
| DATA-005 | Null default uniqueness | `scenario-catalog.md#data-005` |
| DATA-006 | Precision fidelity | `scenario-catalog.md#data-006` |
| DATA-007 | Timezone round trip | `scenario-catalog.md#data-007` |
| DATA-008 | Unicode round trip | `scenario-catalog.md#data-008` |
| DATA-009 | Binary and JSON round trip | `scenario-catalog.md#data-009` |
| DATA-010 | Large object truncation | `scenario-catalog.md#data-010` |
| DATA-011 | Concurrent pagination | `scenario-catalog.md#data-011` |
| DATA-012 | Forward migration | `scenario-catalog.md#data-012` |
| DATA-013 | Interrupted migration | `scenario-catalog.md#data-013` |
| DATA-014 | Version compatibility | `scenario-catalog.md#data-014` |
| DATA-015 | Backup integrity | `scenario-catalog.md#data-015` |
| DATA-016 | Restore rehearsal | `scenario-catalog.md#data-016` |
| DATA-017 | Import invalid records | `scenario-catalog.md#data-017` |
| DATA-018 | CSV formula injection | `scenario-catalog.md#data-018` |
| DATA-019 | Referential cleanup | `scenario-catalog.md#data-019` |
| DATA-020 | Soft delete semantics | `scenario-catalog.md#data-020` |
| DATA-021 | Retention enforcement | `scenario-catalog.md#data-021` |
| DATA-022 | Index cache consistency | `scenario-catalog.md#data-022` |
| DATA-023 | Idempotent retries | `scenario-catalog.md#data-023` |
| DATA-024 | Audit trail integrity | `scenario-catalog.md#data-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

