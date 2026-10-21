---
name: clean-code-architecture-auditor
description: "Maintainability, coupling, and architectural boundary review. Deep playbooks and per-scenario specs in references/. Use for code structure and architecture. Structured markdown reports required."
---

# clean-code-architecture-auditor

**Purpose:** Maintainability and architectural boundaries. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** SOLID, coupling metrics, ADRs, ISO 25010 maintainability

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
| CLEA-001 | Intent-revealing naming | `scenario-catalog.md#clea-001` |
| CLEA-002 | Module cohesion | `scenario-catalog.md#clea-002` |
| CLEA-003 | Single responsibility | `scenario-catalog.md#clea-003` |
| CLEA-004 | Hidden side effects | `scenario-catalog.md#clea-004` |
| CLEA-005 | Dependency direction | `scenario-catalog.md#clea-005` |
| CLEA-006 | Circular imports | `scenario-catalog.md#clea-006` |
| CLEA-007 | Duplicated logic | `scenario-catalog.md#clea-007` |
| CLEA-008 | Over-abstraction | `scenario-catalog.md#clea-008` |
| CLEA-009 | Conditional complexity | `scenario-catalog.md#clea-009` |
| CLEA-010 | Explicit error handling | `scenario-catalog.md#clea-010` |
| CLEA-011 | Unhandled panics | `scenario-catalog.md#clea-011` |
| CLEA-012 | Resource cleanup | `scenario-catalog.md#clea-012` |
| CLEA-013 | Thread safety | `scenario-catalog.md#clea-013` |
| CLEA-014 | Validation boundaries | `scenario-catalog.md#clea-014` |
| CLEA-015 | Public API compatibility | `scenario-catalog.md#clea-015` |
| CLEA-016 | Dead code | `scenario-catalog.md#clea-016` |
| CLEA-017 | Useful invariants in comments | `scenario-catalog.md#clea-017` |
| CLEA-018 | Testability | `scenario-catalog.md#clea-018` |
| CLEA-019 | Dependency hygiene | `scenario-catalog.md#clea-019` |
| CLEA-020 | Secret-safe logging | `scenario-catalog.md#clea-020` |
| CLEA-021 | Configuration defaults | `scenario-catalog.md#clea-021` |
| CLEA-022 | Abstraction leakage | `scenario-catalog.md#clea-022` |
| CLEA-023 | Avoiding quadratic loops | `scenario-catalog.md#clea-023` |
| CLEA-024 | Serialization evolution | `scenario-catalog.md#clea-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

