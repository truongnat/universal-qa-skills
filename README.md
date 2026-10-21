# Universal QA Skills

**One-command installable, technology-agnostic quality engineering skills**, with risk-based test methodology and embedded multi-agent delegation prompts.

## Install

Requires **Node.js** (for `npx`) and an **agent host that supports skills** (e.g. Cursor Agent Skills).

Install into the **project you want to test** (not only this repo):

```bash
npx skills add truongnat/universal-qa-skills
```

Install all 15 skills without interactive selection:

```bash
npx skills add truongnat/universal-qa-skills --skill '*' -y
```

After install, confirm skills appear in your host (e.g. Cursor **Settings → Skills**): `qa-orchestrator`, `functional-tester`, `security-privacy-auditor`, etc.

**Local development:** clone this repository and run `python3 scripts/maintain_repo.py sync` after editing shared references (see [Contributing](#contributing)).

## Included

- 15 installable `SKILL.md` specialist skills, each with bundled standards, report templates, and shared contracts.
- 356 catalog scenario prompts across 15 domains (20 QA coordination scenarios plus 14 × 24 specialist scenarios).
- 9 embedded QA roles (QA Lead + eight workers) under `.agents/skills/qa-orchestrator/agents/`.
- Delegation and evidence handoff under `.agents/skills/qa-orchestrator/workflows/`.

## Quick start

1. Install skills into your target project (`npx skills add … --skill '*' -y`).
2. Open that project in your agent IDE.
3. Invoke **`qa-orchestrator`** and send a scoped prompt (examples below).

## Usage

### Recommended: `qa-orchestrator` (risk-based full QA)

Use the **qa-orchestrator** skill: inspect requirements and architecture, build a risk-based plan, delegate specialist roles when the host supports subagents (otherwise run sequentially and say so). Collect reproducible evidence, separate confirmed bugs from assumptions, and issue a release assessment. Keep tests **non-destructive** by default.

**Example prompt (feature / PR scope):**

```text
Use the qa-orchestrator skill. Read agents/qa-lead.md and workflows/multi-agent-protocol.md.
Analyze this repo, plan QA by risk, delegate specialists if subagents are available.
Non-destructive only; do not change production or source without approval.
Report per references/report-output-format.md (execution matrix, defects, release gates).
Scope: [feature, PR, or paths]. Environment: [local / staging URL, test accounts redacted].
```

Bundled one-liner: `.agents/skills/qa-orchestrator/workflows/master-prompt.md`.

### Single specialist (narrow scope)

| Need | Skill |
|------|--------|
| User journeys, CRUD, business rules | `functional-tester` |
| API / contracts | `api-contract-tester` |
| Security & privacy | `security-privacy-auditor` |
| UX & accessibility | `ux-accessibility-auditor` |
| UI / visual | `ui-visual-tester` |
| Performance & reliability | `performance-reliability-tester` |
| Ship / no-ship | `release-readiness-auditor` |

```text
Use skill security-privacy-auditor on [module/path]. Select scenarios by risk;
expand per references/scenario-expansion-guide.md.
Output tables per references/report-output-format.md. Staging/local only.
```

### Full release sweep (“quét hết”)

The **356 scenarios are design prompts**, not 356 automated tests. A full sweep means **whole product/release scope**, **all QA domains**, **all orchestrator workers**, and **maximum catalog coverage** with honest **N/A**, **NOT TESTED**, and **BLOCKED** where applicable.

```text
Use qa-orchestrator (qa-lead.md + multi-agent-protocol.md).

Goal: FULL RELEASE SWEEP — entire codebase and deployable artifacts on [branch/tag].

1. Dispatch all workers: qa-functional, qa-ui-ux, qa-security, qa-data,
   qa-performance, qa-code-quality, qa-regression, qa-bug-hunter
   (parallel if subagents exist; else sequential and disclose).
2. Each worker loads its specialist skills; map catalog rows to atomic tests.
3. Per catalog family (ORCH, FUNC, SECU, API, …): list selected, N/A (reason),
   NOT TESTED/BLOCKED (reason).
4. Non-destructive; no production attacks or data writes.
5. Final report: executive summary, execution counts, master matrix, confirmed defects,
   hypothetical risks, coverage gaps vs catalog intent, GO / CONDITIONAL / NO-GO.

Environment: [local/staging]. Time budget: [optional].
```

Worker ↔ skill routing: [`docs/skill-worker-map.md`](docs/skill-worker-map.md).

## Report format

Deliverables must use **structured markdown**: **tables** for matrices, defects, and gates; **headings** and **bullet lists** for narrative—not wall-of-text only.

- Bundled spec: `references/report-output-format.md` (in any installed skill).
- Example: [`docs/sample-release-assessment.md`](docs/sample-release-assessment.md).

## Host limitations

`npx skills` installs skill folders and bundled resources. It does **not** register or spawn native subagents. Parallel workers depend on your host (e.g. Cursor Task/subagents).

## Contributing

- [`CONTRIBUTING.md`](CONTRIBUTING.md) — edit shared references, sync, validate.
- Canonical shared files: `.agents/skills/_shared/references/` (copied into each skill via `python3 scripts/maintain_repo.py sync`).
- CI: `python3 scripts/maintain_repo.py validate` (also runs on push via GitHub Actions).

## Standards

Based on principles and techniques from ISO/IEC/IEEE 29119, ISO/IEC 25010, ISTQB CTFL, WCAG 2.2, OWASP ASVS/MASVS and ISO 9241, when applicable. These references do not confer certification.

## Verification expectations

A scenario catalog is not a suite of automated tests. Record preconditions, input data, independent expected result, actual result, tool output and environment before marking any case PASS. Explicitly identify NOT TESTED, BLOCKED and N/A cases. Never run destructive operations against live user environments.
