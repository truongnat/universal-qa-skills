---
name: ux-accessibility-auditor
description: "Usability, WCAG-oriented accessibility, and inclusive UX. Use for UX and accessibility in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# ux-accessibility-auditor

**Purpose:** Usability and accessible interaction. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| UX-001 | Task discoverability |
| UX-002 | Information architecture |
| UX-003 | Feedback latency |
| UX-004 | Undo and cancel |
| UX-005 | Destructive action prevention |
| UX-006 | Validation clarity |
| UX-007 | Keyboard-only flow |
| UX-008 | Logical focus sequence |
| UX-009 | Focus visibility |
| UX-010 | Focus restoration |
| UX-011 | Accessible names |
| UX-012 | Roles and values |
| UX-013 | Screen reader announcements |
| UX-014 | Heading hierarchy |
| UX-015 | Text alternatives |
| UX-016 | Color-independent status |
| UX-017 | Text resizing |
| UX-018 | Reflow |
| UX-019 | Pointer alternatives |
| UX-020 | Reduced motion |
| UX-021 | Touch targets |
| UX-022 | Shortcut discoverability |
| UX-023 | Localized errors |
| UX-024 | Assistance and help |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

