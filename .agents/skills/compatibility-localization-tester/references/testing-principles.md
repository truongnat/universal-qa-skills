# Testing Principles (ISTQB-aligned)

Summaries for agent guidance—not a substitute for formal ISTQB or ISO training or certification.

## Seven foundational principles

| # | Principle | Agent implication |
|---|-----------|-------------------|
| 1 | Testing shows presence of defects, not their absence | Never claim “fully tested” or “no bugs”; report coverage and residual risk. |
| 2 | Exhaustive testing is impossible | Use risk, prioritization, and sampling; document what was **not** run and why. |
| 3 | Early testing saves time and money | Start with static review of requirements, contracts, and architecture before runtime. |
| 4 | Defects cluster | Focus extra depth on hot modules, complex integrations, and prior failure areas. |
| 5 | Tests wear out (pesticide paradox) | Vary data, paths, and oracles; add exploratory passes; keep regression for stability only. |
| 6 | Testing is context-dependent | Adapt depth, tools, and evidence to domain (safety-critical vs internal admin vs mobile consumer). |
| 7 | Absence-of-defects fallacy | Verify requirements **and** validate fitness for user/business goals; usability and value matter. |

## Verification vs validation

| | Verification | Validation |
|---|--------------|------------|
| Question | “Did we build it right?” | “Did we build the right thing?” |
| Basis | Specs, contracts, code | User needs, tasks, outcomes |
| Typical activities | Contract tests, unit/integration checks, AC mapping | Journey tests, usability probes, stakeholder review |

Report both: **spec conformance gaps** and **fitness / UX / business misalignment**.

## Static vs dynamic testing

| Type | Examples | Counts as runtime PASS? |
|------|----------|---------------------------|
| Static | Requirements review, threat modeling, lint, architecture review | No |
| Dynamic | Executed UI/API/load/chaos in a running environment | Yes (when oracle satisfied) |

Label evidence source in every matrix row.

## Shift-left and testability

- Prefer finding ambiguity, missing NFRs, and untestable ACs **before** implementation freeze.
- Flag **testability** issues: missing observability, no stable test IDs, flaky env, secret coupling.
- Recommend **fast feedback** layers (unit → contract → smoke → targeted E2E) without pretending one layer replaces another.

## Completion and exit (conceptual)

Exit is **risk-informed**, not “all cases green”:

- Agreed residual risk accepted by accountable role
- Critical requirements covered with executed evidence
- Open S0/S1 defects disposition documented
- Performance/security/a11y gates explicit (PASS / FAIL / NOT TESTED)

See `risk-based-testing.md` and `quality-attribute-model.md`.
