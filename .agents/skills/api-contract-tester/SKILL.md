---
name: api-contract-tester
description: "Protocol and integration contract verification. Use for API contracts, schemas, and integration boundaries in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# api-contract-tester

**Purpose:** Protocol and integration contracts. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| API-001 | Required schema fields |
| API-002 | Unknown schema fields |
| API-003 | Null semantics |
| API-004 | Status and error envelope |
| API-005 | Authentication failure |
| API-006 | Authorization ownership |
| API-007 | Content negotiation |
| API-008 | Pagination cursor |
| API-009 | Stable ordering |
| API-010 | Filter escaping |
| API-011 | Idempotency keys |
| API-012 | Conditional updates |
| API-013 | Rate limits |
| API-014 | Timeout |
| API-015 | Cancellation |
| API-016 | Compatibility evolution |
| API-017 | Payload size limits |
| API-018 | Unicode and encoding |
| API-019 | Streaming uploads |
| API-020 | Webhook signatures |
| API-021 | Webhook replay |
| API-022 | Event schema compatibility |
| API-023 | Batch partial failure |
| API-024 | Cache privacy |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

