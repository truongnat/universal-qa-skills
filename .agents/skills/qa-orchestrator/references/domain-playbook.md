# Domain playbook — qa-orchestrator

## Mission

Coordinate **risk-based QA** across specialists: intake → plan → delegate → merge evidence → **release recommendation**. You own **traceability**, **deduplication**, and **honest coverage accounting**—not doing every test alone.

## Intake packet (ORCH-001)

Collect before dispatch:

| Item | Source |
|------|--------|
| Release candidate ID | CI, tag, build number |
| Change scope | Diff, changelog, feature flags |
| Test basis | Specs, contracts, ADRs |
| Environments | URLs, credentials class, data policy |
| Stakeholder priorities | Must-ship vs nice-to-have |
| Known incidents / debt | Past Sev-1/2 |

Gap in intake → BLOCKED or NOT TESTED with owner.

## Quality attribute coverage (ORCH-002)

Map release to **ISO 25010** characteristics. For each, assign **owner skill/worker** and gate status:

| Characteristic | Worker route | Minimum evidence |
|----------------|--------------|------------------|
| Functional suitability | qa-functional | Journey matrix |
| Security | qa-security | AuthZ + abuse sample |
| Interaction/a11y | qa-ui-ux | WCAG spot + task success |
| Performance | qa-performance | Measured budget or NOT TESTED |
| Reliability | qa-performance / qa-data | Recovery scenario |
| Compatibility | compatibility skill | Matrix row executed |

## Delegation rules

- **Parallelize** read-only independent scopes when host supports subagents.
- **Packet** each worker using `dispatch-template.md` (paths, risks, forbidden actions, evidence format).
- **Never** merge worker PASS without spot-checking evidence for S0/S1 claims.

## Gate vs depth

| ORCH gate | Orchestrator asks | Specialist delivers |
|-----------|-------------------|---------------------|
| ORCH-009 Functional | Strategy & coverage % of risks | Deep FUNC/API cases |
| ORCH-010 Accessibility | WCAG scope level | Criterion-level table |
| ORCH-011 Security | Top abuse paths tested | Repro + ASVS mapping |
| ORCH-012 Reliability | Failover/recovery | Logs, metrics |
| ORCH-013 Performance | SLO comparison | Numbers or BLOCKED |

## Merge & conflict (ORCH-016–017)

- Deduplicate by **root cause + repro**, not symptom count.
- Conflicting severity → **challenge pass** (second method or peer worker).
- Document disagreements in table; QA Lead rules final wording.

## Release decision (ORCH-020)

**NO-GO** if any open S0/S1 without accepted waiver. **CONDITIONAL** requires:

| Condition | Owner | Due |
|-----------|-------|-----|
| | | |

Residual risk table mandatory (`risk-based-testing.md`).

## Reporting

Single merged report: executive summary, **master matrix** (all workers), defect roll-up, gates, checklist. Use `docs/sample-release-assessment.md` as shape.

## Anti-patterns

- Claiming “all 356 scenarios passed.”
- Letting workers edit product code to green tests.
- Hiding NOT TESTED behind PASS counts.
