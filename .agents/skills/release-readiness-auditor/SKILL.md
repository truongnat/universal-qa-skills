---
name: release-readiness-auditor
description: "Evidence-backed ship / no-ship assessment. Use for release readiness in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# release-readiness-auditor

**Purpose:** Evidence-backed ship/no-ship. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| RELE-001 | Artifact identity |
| RELE-002 | Reproducible build |
| RELE-003 | Package launch |
| RELE-004 | Install and uninstall |
| RELE-005 | Upgrade smoke test |
| RELE-006 | Critical journey evidence |
| RELE-007 | Outstanding critical defects |
| RELE-008 | Dependency security checks |
| RELE-009 | Privacy checks |
| RELE-010 | Accessibility target |
| RELE-011 | Performance budget |
| RELE-012 | Backup restore readiness |
| RELE-013 | Monitoring readiness |
| RELE-014 | Incident response ownership |
| RELE-015 | Release notes accuracy |
| RELE-016 | Feature flag rollback |
| RELE-017 | Data migration readiness |
| RELE-018 | Skipped tests reviewed |
| RELE-019 | Cross-platform evidence |
| RELE-020 | Formal exception sign-off |
| RELE-021 | Rollout monitoring |
| RELE-022 | Rollback thresholds |
| RELE-023 | Code signing |
| RELE-024 | Post-release verification |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

