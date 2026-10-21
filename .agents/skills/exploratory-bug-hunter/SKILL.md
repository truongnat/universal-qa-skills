---
name: exploratory-bug-hunter
description: "Session-based exploratory testing and defect discovery. Use for exploratory testing in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# exploratory-bug-hunter

**Purpose:** Session-based exploratory defect discovery. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| EXPL-001 | New user tour |
| EXPL-002 | Expert workflow tour |
| EXPL-003 | Error recovery tour |
| EXPL-004 | Input boundary tour |
| EXPL-005 | Interrupt and retry tour |
| EXPL-006 | Rapid navigation |
| EXPL-007 | Permission switching |
| EXPL-008 | Data lifecycle |
| EXPL-009 | Malformed inputs |
| EXPL-010 | Large dataset |
| EXPL-011 | Localization tour |
| EXPL-012 | Keyboard-only exploration |
| EXPL-013 | Offline tour |
| EXPL-014 | Multi-session tour |
| EXPL-015 | Upgrade tour |
| EXPL-016 | Unexpected combinations |
| EXPL-017 | Repeated cancellation |
| EXPL-018 | Time anomalies |
| EXPL-019 | Resource exhaustion |
| EXPL-020 | Cross-feature integration |
| EXPL-021 | State switching |
| EXPL-022 | Random replayable sequence |
| EXPL-023 | Visual consistency |
| EXPL-024 | Unexpected data loss |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

