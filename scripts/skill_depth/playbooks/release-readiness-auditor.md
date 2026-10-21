# Domain playbook — release-readiness-auditor

## Mission

Produce **evidence-backed ship / no-ship** judgment aggregating QA, open defects, risks, and operational readiness.

## Inputs required

| Input | If missing |
|-------|------------|
| RC build identity | BLOCKED |
| Test execution summaries | NOT TESTED |
| Open defect list with sev | Escalate |
| Known migrations/ops steps | Flag in conditions |
| Rollback plan | CONDITIONAL at best |

## Exit criteria table

Map each organizational gate to **PASS/FAIL/NOT TESTED** with evidence link.

## Trend analysis

- New Sev-1/2 in RC window.
- Flake spike in CI.
- Unresolved BLOCKED from specialists.

## Decision wording

**GO** / **CONDITIONAL GO** (numbered conditions + owners) / **NO-GO** (blockers).

Never GO with undocumented residual S1.

## Pairing

Owned by `qa-orchestrator` merge; uses all specialist artifacts.
