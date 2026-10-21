# Skill ↔ Worker Map

Use this when running **qa-orchestrator** multi-agent flows. Workers are bundled under `qa-orchestrator/agents/`; they load **installed specialist skills** by name (not repo paths).

## Routing (from `multi-agent-protocol.md`)

| Worker agent | Primary skills to load | Focus |
|---|---|---|
| `qa-lead` | `qa-orchestrator`, `requirements-test-designer`, `release-readiness-auditor` | Triage, dispatch, merge, release gate |
| `qa-functional` | `functional-tester`, `requirements-test-designer` | Journeys, business rules, state |
| `qa-ui-ux` | `ui-visual-tester`, `ux-accessibility-auditor` | Layout, visual, WCAG-oriented UX |
| `qa-code-quality` | `clean-code-architecture-auditor` | Maintainability, boundaries |
| `qa-security` | `security-privacy-auditor` | AuthZ, injection, secrets, privacy |
| `qa-data` | `data-integrity-tester`, `api-contract-tester`, `logic-concurrency-tester` | Data, contracts, concurrency |
| `qa-performance` | `performance-reliability-tester` | Load, latency, resilience |
| `qa-regression` | `test-automation-auditor`, `release-readiness-auditor` | CI, automation health, ship decision |
| `qa-bug-hunter` | `exploratory-bug-hunter` | Cross-feature exploratory sessions |

## Specialist skills (installable)

| Skill | Scenario prefix | Count |
|---|---|---:|
| `qa-orchestrator` | ORCH | 20 |
| `functional-tester` | FUNC | 24 |
| `requirements-test-designer` | REQU | 24 |
| `api-contract-tester` | API | 24 |
| `security-privacy-auditor` | SECU | 24 |
| `ux-accessibility-auditor` | UX | 24 |
| `ui-visual-tester` | UI | 24 |
| `data-integrity-tester` | DATA | 24 |
| `logic-concurrency-tester` | LOGI | 24 |
| `performance-reliability-tester` | PERF | 24 |
| `compatibility-localization-tester` | COMP | 24 |
| `exploratory-bug-hunter` | EXPL | 24 |
| `test-automation-auditor` | TEST | 24 |
| `clean-code-architecture-auditor` | CLEA | 24 |
| `release-readiness-auditor` | RELE | 24 |

Orchestrator **gates** (ORCH-009–014) set scope; workers produce **depth** and evidence tables.

## Shared references

Canonical copies live in `.agents/skills/_shared/references/`. Run `python3 scripts/maintain_repo.py sync` after editing shared files so each skill bundle stays self-contained for `npx skills` install.
