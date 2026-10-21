---
name: qa-orchestrator
description: "Risk-based QA coordination, delegation, and release gates. Deep playbooks and per-scenario specs in references/. Use for end-to-end QA orchestration. Structured markdown reports required."
---

# qa-orchestrator

**Purpose:** Risk-based QA coordinator. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** ISO 29119 risk-based strategy, release exit criteria, traceability

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
| ORCH-001 | Intake and test basis | `scenario-catalog.md#orch-001` |
| ORCH-002 | Quality attribute coverage | `scenario-catalog.md#orch-002` |
| ORCH-003 | Stakeholder risk alignment | `scenario-catalog.md#orch-003` |
| ORCH-004 | Requirements traceability | `scenario-catalog.md#orch-004` |
| ORCH-005 | Release exit criteria | `scenario-catalog.md#orch-005` |
| ORCH-006 | Environment readiness | `scenario-catalog.md#orch-006` |
| ORCH-007 | Fixture safety | `scenario-catalog.md#orch-007` |
| ORCH-008 | Static versus dynamic evidence | `scenario-catalog.md#orch-008` |
| ORCH-009 | Functional suite strategy | `scenario-catalog.md#orch-009` |
| ORCH-010 | Accessibility gate | `scenario-catalog.md#orch-010` |
| ORCH-011 | Security gate | `scenario-catalog.md#orch-011` |
| ORCH-012 | Reliability gate | `scenario-catalog.md#orch-012` |
| ORCH-013 | Performance budget | `scenario-catalog.md#orch-013` |
| ORCH-014 | Cross-platform matrix | `scenario-catalog.md#orch-014` |
| ORCH-015 | High-severity review | `scenario-catalog.md#orch-015` |
| ORCH-016 | Defect deduplication | `scenario-catalog.md#orch-016` |
| ORCH-017 | Cross-agent conflict resolution | `scenario-catalog.md#orch-017` |
| ORCH-018 | Regression ownership | `scenario-catalog.md#orch-018` |
| ORCH-019 | Blocked-test escalation | `scenario-catalog.md#orch-019` |
| ORCH-020 | Release decision | `scenario-catalog.md#orch-020` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

## Multi-agent orchestration
Read **bundled** `agents/qa-lead.md`, `workflows/multi-agent-protocol.md`, `workflows/dispatch-template.md` (paths relative to this skill). The orchestrator owns dispatch, reconciliation, and release gate review. Use real native subagent tools when available. If the host does not support subagent spawning, execute specialists sequentially and disclose this. **Do not claim native agent registration**: agent definitions are bundled role prompts, not automatically installed CLI agents. Delegate bounded read-only tasks with independent evidence paths, and challenge high-severity findings in a second pass. Workers should read installed specialist skills via host skill discovery, not hard-coded project paths. Final merged output must follow `references/report-output-format.md` (tables for matrices, gates, and handoffs).

