---
name: logic-concurrency-tester
description: "State machines, timing, races, and invariants. Deep playbooks and per-scenario specs in references/. Use for logic and concurrency. Structured markdown reports required."
---

# logic-concurrency-tester

**Purpose:** State, timing and invariant testing. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** State machines, locking docs, idempotency contracts

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
| LOGI-001 | Invalid state transition | `scenario-catalog.md#logi-001` |
| LOGI-002 | Repeated event | `scenario-catalog.md#logi-002` |
| LOGI-003 | Stale asynchronous response | `scenario-catalog.md#logi-003` |
| LOGI-004 | Cancel versus complete race | `scenario-catalog.md#logi-004` |
| LOGI-005 | Concurrent writes | `scenario-catalog.md#logi-005` |
| LOGI-006 | Partial transaction failure | `scenario-catalog.md#logi-006` |
| LOGI-007 | Lost update | `scenario-catalog.md#logi-007` |
| LOGI-008 | Optimistic lock conflict | `scenario-catalog.md#logi-008` |
| LOGI-009 | TOCTOU | `scenario-catalog.md#logi-009` |
| LOGI-010 | Resource lifecycle race | `scenario-catalog.md#logi-010` |
| LOGI-011 | Out of order events | `scenario-catalog.md#logi-011` |
| LOGI-012 | Replay processing | `scenario-catalog.md#logi-012` |
| LOGI-013 | Retry amplification | `scenario-catalog.md#logi-013` |
| LOGI-014 | Queue saturation | `scenario-catalog.md#logi-014` |
| LOGI-015 | Deadlock | `scenario-catalog.md#logi-015` |
| LOGI-016 | Starvation | `scenario-catalog.md#logi-016` |
| LOGI-017 | Cache invalidation | `scenario-catalog.md#logi-017` |
| LOGI-018 | Integer overflow | `scenario-catalog.md#logi-018` |
| LOGI-019 | Decimal rounding | `scenario-catalog.md#logi-019` |
| LOGI-020 | Null semantics | `scenario-catalog.md#logi-020` |
| LOGI-021 | Clock skew | `scenario-catalog.md#logi-021` |
| LOGI-022 | Restart recovery | `scenario-catalog.md#logi-022` |
| LOGI-023 | Mid-operation feature flag | `scenario-catalog.md#logi-023` |
| LOGI-024 | Exactly-once cleanup | `scenario-catalog.md#logi-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

