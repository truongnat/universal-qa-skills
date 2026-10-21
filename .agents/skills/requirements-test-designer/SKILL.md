---
name: requirements-test-designer
description: "Standards-informed requirements analysis and test design. Use for requirements and test design in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# requirements-test-designer

**Purpose:** Standards-informed test design. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| REQU-001 | Ambiguous acceptance criteria |
| REQU-002 | Mandatory optional fields |
| REQU-003 | Empty null missing values |
| REQU-004 | Whitespace and trim policy |
| REQU-005 | Input min boundary |
| REQU-006 | Input max boundary |
| REQU-007 | Off-by-one errors |
| REQU-008 | Equivalent valid classes |
| REQU-009 | Equivalent invalid classes |
| REQU-010 | Decision table interactions |
| REQU-011 | State transition validity |
| REQU-012 | Role and permission matrix |
| REQU-013 | Idempotency expectations |
| REQU-014 | Duplicate submission |
| REQU-015 | Date and time rules |
| REQU-016 | Timezone and DST |
| REQU-017 | Decimal and rounding |
| REQU-018 | Unicode normalization |
| REQU-019 | Feature flag behavior |
| REQU-020 | Migration acceptance |
| REQU-021 | Partial success semantics |
| REQU-022 | Interrupted operations |
| REQU-023 | Test oracle independence |
| REQU-024 | Traceability completeness |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

