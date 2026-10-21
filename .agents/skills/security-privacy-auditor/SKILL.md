---
name: security-privacy-auditor
description: "Security verification and privacy-sensitive flows. Use for security and privacy in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# security-privacy-auditor

**Purpose:** Security verification and privacy. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| SECU-001 | Authentication limits |
| SECU-002 | Session fixation |
| SECU-003 | Session revocation |
| SECU-004 | Object authorization |
| SECU-005 | Privilege escalation |
| SECU-006 | SQL injection |
| SECU-007 | Command injection |
| SECU-008 | Output escaping |
| SECU-009 | Cross-site request forgery |
| SECU-010 | Server-side request forgery |
| SECU-011 | Path traversal |
| SECU-012 | Unsafe deserialization |
| SECU-013 | Untrusted file upload |
| SECU-014 | Secrets in logs |
| SECU-015 | Credential storage |
| SECU-016 | Transport validation |
| SECU-017 | Crypto key lifecycle |
| SECU-018 | Sensitive temporary files |
| SECU-019 | Dependency provenance |
| SECU-020 | Insecure debug settings |
| SECU-021 | Tenant isolation |
| SECU-022 | Audit logging |
| SECU-023 | Resource exhaustion |
| SECU-024 | Deletion and consent |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

