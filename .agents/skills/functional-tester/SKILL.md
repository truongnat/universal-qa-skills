---
name: functional-tester
description: "Critical user journey and business-flow verification. Use for functional user journeys in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# functional-tester

**Purpose:** Critical user journey verification. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| FUNC-001 | First run and onboarding |
| FUNC-002 | Create valid entity |
| FUNC-003 | Create invalid entity |
| FUNC-004 | Duplicate record handling |
| FUNC-005 | Read missing record |
| FUNC-006 | Read unauthorized record |
| FUNC-007 | Update valid record |
| FUNC-008 | Update conflict |
| FUNC-009 | Delete confirmation |
| FUNC-010 | Delete recovery |
| FUNC-011 | Search exact case |
| FUNC-012 | Search Unicode |
| FUNC-013 | Filter combinations |
| FUNC-014 | Sorting stability |
| FUNC-015 | Pagination boundaries |
| FUNC-016 | Bulk actions |
| FUNC-017 | Import malformed rows |
| FUNC-018 | Export fidelity |
| FUNC-019 | Unsaved state protection |
| FUNC-020 | Session expiry |
| FUNC-021 | Offline to online recovery |
| FUNC-022 | Background cancellation |
| FUNC-023 | Restart persistence |
| FUNC-024 | Multi-user collaboration |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

