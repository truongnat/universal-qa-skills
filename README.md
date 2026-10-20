# Universal QA Skills

**One-command installable, technology-agnostic quality engineering skills**, with risk-based test methodology and embedded multi-agent delegation prompts.

## Install

```bash
npx skills add truongnat/universal-qa-skills
```

To install all 15 skills without interactive selection:

```bash
npx skills add truongnat/universal-qa-skills --skill '*' -y
```

## Included
- 15 installable `SKILL.md` specialist skills, each with its own bundled standards guidance and test/report templates.
- 356 catalog scenario prompts across 15 domains (20 QA coordination scenarios plus 14 × 24 specialist scenarios).
- 9 embedded QA roles, including QA Lead and eight specialist workers, under `.agents/skills/qa-orchestrator/agents/`.
- Delegation and evidence handoff protocols under `.agents/skills/qa-orchestrator/workflows/`.

## Usage

> Use the **qa-orchestrator** skill, inspect the requirements and architecture, build a risk-based plan and delegate applicable specialist roles. Use native subagent tools if available, otherwise run sequentially. Collect reproducible evidence, distinguish actual bugs from assumptions and issue a release assessment. Keep all tests non-destructive by default.

**Important:** `npx skills` installs skill folders and their bundled resources. It does not itself register or spawn native subagents. Whether workers run concurrently depends on the host agent's delegation capabilities.

## Standards
Based on principles and techniques from ISO/IEC/IEEE 29119, ISO/IEC 25010, ISTQB CTFL, WCAG 2.2, OWASP ASVS/MASVS and ISO 9241, when applicable. These references do not confer certification.

## Verification expectations
A scenario catalog is not a suite of automated tests. Record preconditions, input data, independent expected result, actual result, tool output and environment before marking any case PASS. Explicitly identify NOT TESTED, BLOCKED and N/A cases. Never run destructive operations against live user environments.
