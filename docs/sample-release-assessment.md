# Sample Release Assessment (formatted output)

Example of the **required** presentation style. Agents should produce similar structure in chat.

## Executive summary

| Field | Value |
|---|---|
| Product / RC | Example App 2.4.0-rc1 |
| Environment | staging `https://staging.example.com` |
| Scope | Checkout + payment webhook |
| **Verdict** | **CONDITIONAL GO** |

**Summary:** Core checkout paths pass; one S1 authZ gap on order history; performance not run on mobile.

## Risk & scope inventory

| Risk ID | Area | Impact | Likelihood | Test focus |
|---|---|---:|---:|---|
| R-01 | Payment | 5 | 3 | FUNC-018, API-007 |
| R-02 | AuthZ | 5 | 2 | SECU-004, FUNC-006 |

## Execution counts

| Planned | Executed | PASS | FAIL | BLOCKED | NOT TESTED | N/A |
|---:|---:|---:|---:|---:|---:|---:|
| 12 | 10 | 8 | 1 | 1 | 2 | 0 |

## Test matrix (excerpt)

| Test ID | Technique | Status | Expected | Actual | Evidence |
|---|---|---|---|---|---|
| FUNC-006a | Negative | FAIL | 403 on other user's order | 200 + body | `curl` log `evidence/func-006a.txt` |
| SECU-004b | AuthZ | NOT TESTED | — | — | Staging role missing |

## Defects (confirmed)

| ID | Sev | Title | Repro |
|---|---|---|---|
| BUG-142 | S1 | IDOR on `/orders/{id}` | Login user A, GET order id from user B → 200 |

## Release gates

| Gate | Status | Notes |
|---|---|---|
| Functional | FAIL | BUG-142 blocks |
| Security | CONDITIONAL | IDOR open |
| Accessibility | PASS | UX spot checks |
| Performance | NOT TESTED | Mobile farm blocked |

> **Decision:** **NO-GO** until BUG-142 fixed and SECU-004b executed.

### Conditions to lift NO-GO

- [ ] Fix IDOR — backend — retest FUNC-006a
- [ ] Run SECU-004b with multi-tenant fixture — QA

## Verification checklist

- [x] Scope and test basis verified
- [x] Risk-based selection documented
- [x] Execution vs static inspection distinguished
- [x] Output uses tables per `report-output-format.md`
