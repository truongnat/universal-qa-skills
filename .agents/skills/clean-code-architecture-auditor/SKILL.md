---
name: clean-code-architecture-auditor
description: "Maintainability, coupling, and architectural boundary review. Use for code structure and architecture in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# clean-code-architecture-auditor

**Purpose:** Maintainability and architectural boundaries. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| CLEA-001 | Intent-revealing naming |
| CLEA-002 | Module cohesion |
| CLEA-003 | Single responsibility |
| CLEA-004 | Hidden side effects |
| CLEA-005 | Dependency direction |
| CLEA-006 | Circular imports |
| CLEA-007 | Duplicated logic |
| CLEA-008 | Over-abstraction |
| CLEA-009 | Conditional complexity |
| CLEA-010 | Explicit error handling |
| CLEA-011 | Unhandled panics |
| CLEA-012 | Resource cleanup |
| CLEA-013 | Thread safety |
| CLEA-014 | Validation boundaries |
| CLEA-015 | Public API compatibility |
| CLEA-016 | Dead code |
| CLEA-017 | Useful invariants in comments |
| CLEA-018 | Testability |
| CLEA-019 | Dependency hygiene |
| CLEA-020 | Secret-safe logging |
| CLEA-021 | Configuration defaults |
| CLEA-022 | Abstraction leakage |
| CLEA-023 | Avoiding quadratic loops |
| CLEA-024 | Serialization evolution |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

