# Report Output Format (Required)

Every QA response—plan, execution summary, defect log, gap analysis, or release decision—must be **scannable** in chat or exported markdown. Use the patterns below unless the user requests a specific template file.

## Global rules

- Start with a **one-line verdict or scope** (bold), then structured detail.
- Use **level-2/3 headings** (`##`, `###`) to separate topics; avoid long unbroken paragraphs.
- Prefer **markdown tables** for matrices, counts, traceability, and comparisons.
- Use **bullet or numbered lists** for steps, risks, actions, and assumptions.
- Use **blockquotes** only for escalations, blockers, or release gates.
- Keep status values consistent: `PASS` | `FAIL` | `BLOCKED` | `NOT TESTED` | `N/A`.
- Separate **confirmed findings** from **hypothetical risks** (different subsections).

## Required sections (adapt titles to task)

### 1. Executive summary

| Field | Value |
|---|---|
| Scope | Product / feature / RC |
| Environment | Version, OS, browser, API base URL (redact secrets) |
| Verdict | PASS / FAIL / CONDITIONAL / NOT RUN |
| Top risks | 1–3 bullets max |

### 2. Risk & scope inventory

| Risk ID | Area | Impact (1–5) | Likelihood (1–5) | Mitigation / test focus |
|---|---|---|---|---|

### 3. Test design / execution matrix

| Test ID | Technique | Preconditions | Steps (summary) | Expected (oracle) | Status | Evidence |
|---|---|---|---|---|---|---|

### 4. Defects (confirmed)

| ID | Severity | Component | Summary | Repro (short) | Evidence |
|---|---|---|---|---|---|

### 5. Gaps & blocked items

| Item | Reason | Owner / next action |
|---|---|---|

### 6. Regression backlog

| Priority | Test ID / title | Rationale |
|---|---|---|

## Release assessment (orchestrator / release-readiness)

```markdown
## Release readiness

| Gate | Status | Notes |
|---|---|---|
| Functional | PASS / FAIL / … | |
| Security | … | |
| Accessibility | … | |
| Performance | … | |

> **Decision:** GO / CONDITIONAL GO / NO-GO — _one sentence rationale_

### Conditions (if conditional)

- [ ] Item — owner — due
```

## Worker handoff packet (multi-agent)

| Field | Content |
|---|---|
| Task ID | |
| Role | |
| Status summary | PASS/FAIL counts |
| Findings table | Link or inline mini-table |
| Blockers | Bullets |
| Evidence paths | Commands, logs, files |

## Anti-patterns (do not)

- Single paragraph with no headings for a full test run.
- Claiming PASS without a row in the execution matrix.
- Mixing confirmed bugs and speculative risks in one undifferentiated list.
- Plain-text tables (align with pipes `|`).

See also: `execution-report-template.md`, `defect-template.md`, `test-case-template.md`.
