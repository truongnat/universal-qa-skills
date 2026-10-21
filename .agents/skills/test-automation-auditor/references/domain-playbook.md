# Domain playbook — test-automation-auditor

## Mission

Assess whether **automated tests and CI** give trustworthy signals—coverage of risk, flake rate, runtime, and maintainability.

## Audit dimensions

| Dimension | Questions |
|-----------|-------------|
| Risk fit | Do tests map to top risks or only happy UI? |
| Pyramid balance | Too many E2E vs few unit/contract? |
| Determinism | Flakes quarantined? Root causes tracked? |
| Speed | PR feedback within team target? |
| Assertions | Strong oracles vs trivial `200 OK`? |
| Data | Fixtures isolated, parallel-safe? |

## CI gate review

- What blocks merge vs warns?
- False green history (deployed bugs with green CI).

## Recommendations

Prioritized backlog: stabilize, delete, rewrite, or add tests—with owner and effort.

## Pairing

`release-readiness-auditor` uses automation health in ship decision.
