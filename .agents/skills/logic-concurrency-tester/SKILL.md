---
name: logic-concurrency-tester
description: "State machines, timing, races, and invariants. Use for logic and concurrency in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# logic-concurrency-tester

**Purpose:** State, timing and invariant testing. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| LOGI-001 | Invalid state transition |
| LOGI-002 | Repeated event |
| LOGI-003 | Stale asynchronous response |
| LOGI-004 | Cancel versus complete race |
| LOGI-005 | Concurrent writes |
| LOGI-006 | Partial transaction failure |
| LOGI-007 | Lost update |
| LOGI-008 | Optimistic lock conflict |
| LOGI-009 | TOCTOU |
| LOGI-010 | Resource lifecycle race |
| LOGI-011 | Out of order events |
| LOGI-012 | Replay processing |
| LOGI-013 | Retry amplification |
| LOGI-014 | Queue saturation |
| LOGI-015 | Deadlock |
| LOGI-016 | Starvation |
| LOGI-017 | Cache invalidation |
| LOGI-018 | Integer overflow |
| LOGI-019 | Decimal rounding |
| LOGI-020 | Null semantics |
| LOGI-021 | Clock skew |
| LOGI-022 | Restart recovery |
| LOGI-023 | Mid-operation feature flag |
| LOGI-024 | Exactly-once cleanup |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

