---
name: performance-reliability-tester
description: "Measured performance, resilience, and failure handling. Deep playbooks and per-scenario specs in references/. Use for performance and reliability. Structured markdown reports required."
---

# performance-reliability-tester

**Purpose:** Measured performance and failure handling. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability

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
| PERF-001 | Cold start | `scenario-catalog.md#perf-001` |
| PERF-002 | Warm start | `scenario-catalog.md#perf-002` |
| PERF-003 | First meaningful result | `scenario-catalog.md#perf-003` |
| PERF-004 | Median latency | `scenario-catalog.md#perf-004` |
| PERF-005 | P95 latency | `scenario-catalog.md#perf-005` |
| PERF-006 | P99 latency | `scenario-catalog.md#perf-006` |
| PERF-007 | Peak throughput | `scenario-catalog.md#perf-007` |
| PERF-008 | Concurrency scaling | `scenario-catalog.md#perf-008` |
| PERF-009 | Load ramp | `scenario-catalog.md#perf-009` |
| PERF-010 | Burst recovery | `scenario-catalog.md#perf-010` |
| PERF-011 | Soak stability | `scenario-catalog.md#perf-011` |
| PERF-012 | Memory leaks | `scenario-catalog.md#perf-012` |
| PERF-013 | Large payloads | `scenario-catalog.md#perf-013` |
| PERF-014 | Slow dependency | `scenario-catalog.md#perf-014` |
| PERF-015 | Timeout cascade | `scenario-catalog.md#perf-015` |
| PERF-016 | Retry storm | `scenario-catalog.md#perf-016` |
| PERF-017 | Pool exhaustion | `scenario-catalog.md#perf-017` |
| PERF-018 | Backpressure | `scenario-catalog.md#perf-018` |
| PERF-019 | CPU saturation | `scenario-catalog.md#perf-019` |
| PERF-020 | Disk saturation | `scenario-catalog.md#perf-020` |
| PERF-021 | Frame time and UI jank | `scenario-catalog.md#perf-021` |
| PERF-022 | Network reconnection | `scenario-catalog.md#perf-022` |
| PERF-023 | Crash recovery | `scenario-catalog.md#perf-023` |
| PERF-024 | Measured regression | `scenario-catalog.md#perf-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

