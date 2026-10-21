---
name: qa-orchestrator
description: "Risk-based QA coordination, delegation, and release gates. Use for end-to-end QA orchestration in any software project. Deliverables must use markdown tables, headings, and bullet lists per bundled report-output-format."
---

# qa-orchestrator

**Purpose:** Risk-based QA coordinator. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

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
| ORCH-001 | Intake and test basis |
| ORCH-002 | Quality attribute coverage |
| ORCH-003 | Stakeholder risk alignment |
| ORCH-004 | Requirements traceability |
| ORCH-005 | Release exit criteria |
| ORCH-006 | Environment readiness |
| ORCH-007 | Fixture safety |
| ORCH-008 | Static versus dynamic evidence |
| ORCH-009 | Functional suite strategy |
| ORCH-010 | Accessibility gate |
| ORCH-011 | Security gate |
| ORCH-012 | Reliability gate |
| ORCH-013 | Performance budget |
| ORCH-014 | Cross-platform matrix |
| ORCH-015 | High-severity review |
| ORCH-016 | Defect deduplication |
| ORCH-017 | Cross-agent conflict resolution |
| ORCH-018 | Regression ownership |
| ORCH-019 | Blocked-test escalation |
| ORCH-020 | Release decision |

## Verification checklist
Copy items from `references/verification-checklist.md` into the final report with honest checkbox marks.

## Multi-agent orchestration
Read **bundled** `agents/qa-lead.md`, `workflows/multi-agent-protocol.md`, `workflows/dispatch-template.md` (paths relative to this skill). The orchestrator owns dispatch, reconciliation, and release gate review. Use real native subagent tools when available. If the host does not support subagent spawning, execute specialists sequentially and disclose this. **Do not claim native agent registration**: agent definitions are bundled role prompts, not automatically installed CLI agents. Delegate bounded read-only tasks with independent evidence paths, and challenge high-severity findings in a second pass. Workers should read installed specialist skills via host skill discovery, not hard-coded project paths. Final merged output must follow `references/report-output-format.md` (tables for matrices, gates, and handoffs).

