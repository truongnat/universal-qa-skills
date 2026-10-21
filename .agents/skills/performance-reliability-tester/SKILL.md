---
name: performance-reliability-tester
description: "Measured performance, resilience, and failure handling. Use for performance and reliability in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# performance-reliability-tester

**Purpose:** Measured performance and failure handling. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Mandatory testing contract
Read and apply bundled `references/mandatory-contract.md`, `references/quality-standard.md`, and `references/report-output-format.md` before testing or reporting.

## Report presentation (required)
All results, matrices, defect logs, gap analyses, and release assessments must follow **`references/report-output-format.md`** and, when executing a run, **`references/execution-report-template.md`**. Use **markdown tables** for counts and traceability, **headed sections** for narrative, and **bullets or numbered lists** for steps and actions. Do not deliver wall-of-text-only output.

## Output artifacts
| Artifact | Format |
|---|---|
| Risk & scope inventory | Table + short bullets |
| Test design / execution matrix | Table (see report-output-format) |
| Confirmed findings | Defect table + repro steps |
| Hypothetical risks | Separate table or subsection |
| Coverage gaps / blockers | Table |
| Regression backlog | Prioritized table |
| Final checklist | From `references/verification-checklist.md` |

## Scenario catalog

Each row is a scenario-design prompt, **not** an executed test. Expand using `references/scenario-expansion-guide.md` before marking PASS.

| Case | Scenario focus |
|---|---|
| PERF-001 | Cold start |
| PERF-002 | Warm start |
| PERF-003 | First meaningful result |
| PERF-004 | Median latency |
| PERF-005 | P95 latency |
| PERF-006 | P99 latency |
| PERF-007 | Peak throughput |
| PERF-008 | Concurrency scaling |
| PERF-009 | Load ramp |
| PERF-010 | Burst recovery |
| PERF-011 | Soak stability |
| PERF-012 | Memory leaks |
| PERF-013 | Large payloads |
| PERF-014 | Slow dependency |
| PERF-015 | Timeout cascade |
| PERF-016 | Retry storm |
| PERF-017 | Pool exhaustion |
| PERF-018 | Backpressure |
| PERF-019 | CPU saturation |
| PERF-020 | Disk saturation |
| PERF-021 | Frame time and UI jank |
| PERF-022 | Network reconnection |
| PERF-023 | Crash recovery |
| PERF-024 | Measured regression |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

