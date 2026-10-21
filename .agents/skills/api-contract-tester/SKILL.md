---
name: api-contract-tester
description: "Protocol and integration contract verification. Deep playbooks and per-scenario specs in references/. Use for API contracts, schemas, and integration boundaries. Structured markdown reports required."
---

# api-contract-tester

**Purpose:** Protocol and integration contracts. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP

**P0 scenarios (manual deep specs):** API-004, API-005, API-006, API-008, API-011, API-012, API-016, API-020, API-021, API-023

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
| API-001 | Required schema fields | `scenario-catalog.md#api-001` |
| API-002 | Unknown schema fields | `scenario-catalog.md#api-002` |
| API-003 | Null semantics | `scenario-catalog.md#api-003` |
| API-004 | Status and error envelope | `scenario-catalog.md#api-004` |
| API-005 | Authentication failure | `scenario-catalog.md#api-005` |
| API-006 | Authorization ownership | `scenario-catalog.md#api-006` |
| API-007 | Content negotiation | `scenario-catalog.md#api-007` |
| API-008 | Pagination cursor | `scenario-catalog.md#api-008` |
| API-009 | Stable ordering | `scenario-catalog.md#api-009` |
| API-010 | Filter escaping | `scenario-catalog.md#api-010` |
| API-011 | Idempotency keys | `scenario-catalog.md#api-011` |
| API-012 | Conditional updates | `scenario-catalog.md#api-012` |
| API-013 | Rate limits | `scenario-catalog.md#api-013` |
| API-014 | Timeout | `scenario-catalog.md#api-014` |
| API-015 | Cancellation | `scenario-catalog.md#api-015` |
| API-016 | Compatibility evolution | `scenario-catalog.md#api-016` |
| API-017 | Payload size limits | `scenario-catalog.md#api-017` |
| API-018 | Unicode and encoding | `scenario-catalog.md#api-018` |
| API-019 | Streaming uploads | `scenario-catalog.md#api-019` |
| API-020 | Webhook signatures | `scenario-catalog.md#api-020` |
| API-021 | Webhook replay | `scenario-catalog.md#api-021` |
| API-022 | Event schema compatibility | `scenario-catalog.md#api-022` |
| API-023 | Batch partial failure | `scenario-catalog.md#api-023` |
| API-024 | Cache privacy | `scenario-catalog.md#api-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

