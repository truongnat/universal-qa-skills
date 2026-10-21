---
name: security-privacy-auditor
description: "Security verification and privacy-sensitive flows. Deep playbooks and per-scenario specs in references/. Use for security and privacy. Structured markdown reports required."
---

# security-privacy-auditor

**Purpose:** Security verification and privacy. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** OWASP ASVS 4.0, OWASP Top 10 (2021), CWE, GDPR-style privacy checks where applicable

**P0 scenarios (manual deep specs):** SECU-001, SECU-002, SECU-003, SECU-004, SECU-005, SECU-006, SECU-007, SECU-008, SECU-009, SECU-010, SECU-011, SECU-012, SECU-013, SECU-014, SECU-015, SECU-016, SECU-017, SECU-018, SECU-019, SECU-020, SECU-021, SECU-022, SECU-023, SECU-024

## Operating procedure

| Step | Action |
|------|--------|
| 1 | Intake scope, change diff, environments, and data classification |
| 2 | Build risk table (impact × likelihood) tagged with ISO 25010 characteristic |
| 3 | Map risks → catalog IDs → atomic test IDs with technique column filled |
| 4 | Prepare fixtures; block destructive/out-of-scope actions |
| 5 | Execute highest risk first; log commands, builds, and correlation IDs |
| 6 | Classify each result with evidence tier (CONFIRMED / LIKELY / NOT TESTED / …) |
| 7 | File defects with independent oracle cited; separate speculative risks |
| 8 | Summarize gaps, blocked items, and regression candidates in tables |
| 9 | Copy `verification-checklist.md` with honest marks |
| 10 | Deliver per `execution-report-template.md` |

## Report presentation (required)

Matrices, defects, and gates must use **`references/report-output-format.md`**. No prose-only reports.

## Scenario index

| Case | Focus | Deep specification |
|------|-------|-------------------|
| SECU-001 | Authentication limits | `scenario-catalog.md#secu-001` |
| SECU-002 | Session fixation | `scenario-catalog.md#secu-002` |
| SECU-003 | Session revocation | `scenario-catalog.md#secu-003` |
| SECU-004 | Object authorization | `scenario-catalog.md#secu-004` |
| SECU-005 | Privilege escalation | `scenario-catalog.md#secu-005` |
| SECU-006 | SQL injection | `scenario-catalog.md#secu-006` |
| SECU-007 | Command injection | `scenario-catalog.md#secu-007` |
| SECU-008 | Output escaping | `scenario-catalog.md#secu-008` |
| SECU-009 | Cross-site request forgery | `scenario-catalog.md#secu-009` |
| SECU-010 | Server-side request forgery | `scenario-catalog.md#secu-010` |
| SECU-011 | Path traversal | `scenario-catalog.md#secu-011` |
| SECU-012 | Unsafe deserialization | `scenario-catalog.md#secu-012` |
| SECU-013 | Untrusted file upload | `scenario-catalog.md#secu-013` |
| SECU-014 | Secrets in logs | `scenario-catalog.md#secu-014` |
| SECU-015 | Credential storage | `scenario-catalog.md#secu-015` |
| SECU-016 | Transport validation | `scenario-catalog.md#secu-016` |
| SECU-017 | Crypto key lifecycle | `scenario-catalog.md#secu-017` |
| SECU-018 | Sensitive temporary files | `scenario-catalog.md#secu-018` |
| SECU-019 | Dependency provenance | `scenario-catalog.md#secu-019` |
| SECU-020 | Insecure debug settings | `scenario-catalog.md#secu-020` |
| SECU-021 | Tenant isolation | `scenario-catalog.md#secu-021` |
| SECU-022 | Audit logging | `scenario-catalog.md#secu-022` |
| SECU-023 | Resource exhaustion | `scenario-catalog.md#secu-023` |
| SECU-024 | Deletion and consent | `scenario-catalog.md#secu-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

