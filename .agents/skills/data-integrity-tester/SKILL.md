---
name: data-integrity-tester
description: "Persistence, migration, and data recovery correctness. Use for data integrity and persistence in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# data-integrity-tester

**Purpose:** Persistence correctness and recovery. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| DATA-001 | Atomic mutation |
| DATA-002 | Isolation anomalies |
| DATA-003 | Durability after crash |
| DATA-004 | Constraint enforcement |
| DATA-005 | Null default uniqueness |
| DATA-006 | Precision fidelity |
| DATA-007 | Timezone round trip |
| DATA-008 | Unicode round trip |
| DATA-009 | Binary and JSON round trip |
| DATA-010 | Large object truncation |
| DATA-011 | Concurrent pagination |
| DATA-012 | Forward migration |
| DATA-013 | Interrupted migration |
| DATA-014 | Version compatibility |
| DATA-015 | Backup integrity |
| DATA-016 | Restore rehearsal |
| DATA-017 | Import invalid records |
| DATA-018 | CSV formula injection |
| DATA-019 | Referential cleanup |
| DATA-020 | Soft delete semantics |
| DATA-021 | Retention enforcement |
| DATA-022 | Index cache consistency |
| DATA-023 | Idempotent retries |
| DATA-024 | Audit trail integrity |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

