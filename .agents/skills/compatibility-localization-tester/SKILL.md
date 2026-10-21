---
name: compatibility-localization-tester
description: "Platform matrix, locale, and internationalization checks. Use for compatibility and i18n/l10n in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# compatibility-localization-tester

**Purpose:** Supported matrix and internationalization. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| COMP-001 | Operating system versions |
| COMP-002 | Browser engine support |
| COMP-003 | Device form factors |
| COMP-004 | DPI scaling |
| COMP-005 | Multi-monitor movement |
| COMP-006 | Viewport bounds |
| COMP-007 | Keyboard layouts |
| COMP-008 | Input methods |
| COMP-009 | RTL layout |
| COMP-010 | CJK text |
| COMP-011 | Emoji grapheme clusters |
| COMP-012 | Long translations |
| COMP-013 | Pseudo-localization |
| COMP-014 | Timezone display |
| COMP-015 | DST rollover |
| COMP-016 | Number formatting |
| COMP-017 | Currency formatting |
| COMP-018 | Locale sorting |
| COMP-019 | Filesystem portability |
| COMP-020 | Proxy and VPN |
| COMP-021 | Clean installation |
| COMP-022 | Version upgrades |
| COMP-023 | Rollback behavior |
| COMP-024 | Platform assistive technology |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

