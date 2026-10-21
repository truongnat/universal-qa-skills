---
name: ui-visual-tester
description: "Native and web visual integrity and layout regression. Use for UI and visual quality in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# ui-visual-tester

**Purpose:** Native and web visual integrity. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| UI-001 | Visual hierarchy |
| UI-002 | Spacing alignment |
| UI-003 | Typography legibility |
| UI-004 | Text wrapping |
| UI-005 | Truncation policy |
| UI-006 | Color contrast |
| UI-007 | Light theme |
| UI-008 | Dark theme |
| UI-009 | High contrast |
| UI-010 | Zoom and text scaling |
| UI-011 | Minimum viewport |
| UI-012 | Maximum viewport |
| UI-013 | Narrow height |
| UI-014 | Long translations |
| UI-015 | RTL rendering |
| UI-016 | Empty state |
| UI-017 | Loading state |
| UI-018 | Error state |
| UI-019 | Selected and disabled state |
| UI-020 | Modal positioning |
| UI-021 | Overlay clipping |
| UI-022 | Table overflow |
| UI-023 | Pixel density |
| UI-024 | Visual regression baseline |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

