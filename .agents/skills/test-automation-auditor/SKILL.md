---
name: test-automation-auditor
description: "Test automation quality, CI signals, and flake resistance. Use for test automation and CI in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# test-automation-auditor

**Purpose:** Reliable testing and CI quality. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| TEST-001 | Test portfolio risk fit |
| TEST-002 | Unit invariant coverage |
| TEST-003 | Integration boundary coverage |
| TEST-004 | End to end critical journeys |
| TEST-005 | Deterministic random seed |
| TEST-006 | Frozen clocks |
| TEST-007 | Order independence |
| TEST-008 | Fixture cleanup |
| TEST-009 | Parallel isolation |
| TEST-010 | Behavioral assertions |
| TEST-011 | Failure diagnostics |
| TEST-012 | Flaky retry policy |
| TEST-013 | Quarantine ownership |
| TEST-014 | Coverage quality limits |
| TEST-015 | Mutation testing |
| TEST-016 | Contract drift |
| TEST-017 | Snapshot review |
| TEST-018 | CI gating |
| TEST-019 | Runtime budget |
| TEST-020 | Secrets in test data |
| TEST-021 | Build reproducibility |
| TEST-022 | Captured artifacts |
| TEST-023 | Release artifact targeting |
| TEST-024 | Regression for known bugs |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

