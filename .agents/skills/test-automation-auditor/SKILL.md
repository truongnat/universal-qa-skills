---
name: test-automation-auditor
description: "Test automation quality, CI signals, and flake resistance. Deep playbooks and per-scenario specs in references/. Use for test automation and CI. Structured markdown reports required."
---

# test-automation-auditor

**Purpose:** Reliable testing and CI quality. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas

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
| TEST-001 | Test portfolio risk fit | `scenario-catalog.md#test-001` |
| TEST-002 | Unit invariant coverage | `scenario-catalog.md#test-002` |
| TEST-003 | Integration boundary coverage | `scenario-catalog.md#test-003` |
| TEST-004 | End to end critical journeys | `scenario-catalog.md#test-004` |
| TEST-005 | Deterministic random seed | `scenario-catalog.md#test-005` |
| TEST-006 | Frozen clocks | `scenario-catalog.md#test-006` |
| TEST-007 | Order independence | `scenario-catalog.md#test-007` |
| TEST-008 | Fixture cleanup | `scenario-catalog.md#test-008` |
| TEST-009 | Parallel isolation | `scenario-catalog.md#test-009` |
| TEST-010 | Behavioral assertions | `scenario-catalog.md#test-010` |
| TEST-011 | Failure diagnostics | `scenario-catalog.md#test-011` |
| TEST-012 | Flaky retry policy | `scenario-catalog.md#test-012` |
| TEST-013 | Quarantine ownership | `scenario-catalog.md#test-013` |
| TEST-014 | Coverage quality limits | `scenario-catalog.md#test-014` |
| TEST-015 | Mutation testing | `scenario-catalog.md#test-015` |
| TEST-016 | Contract drift | `scenario-catalog.md#test-016` |
| TEST-017 | Snapshot review | `scenario-catalog.md#test-017` |
| TEST-018 | CI gating | `scenario-catalog.md#test-018` |
| TEST-019 | Runtime budget | `scenario-catalog.md#test-019` |
| TEST-020 | Secrets in test data | `scenario-catalog.md#test-020` |
| TEST-021 | Build reproducibility | `scenario-catalog.md#test-021` |
| TEST-022 | Captured artifacts | `scenario-catalog.md#test-022` |
| TEST-023 | Release artifact targeting | `scenario-catalog.md#test-023` |
| TEST-024 | Regression for known bugs | `scenario-catalog.md#test-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

