# Domain playbook — exploratory-bug-hunter

## Mission

Discover **unknown unknowns** via **timeboxed, chartered** exploration—especially cross-feature interactions and recent change areas.

## Session design

Use `exploratory-session-template.md` every session:

- **Mission** one sentence.
- **Risk hypothesis** (“merge X+Y might break Z”).
- **SFDPOT** tour plan.
- **Oracle plan** (FEW HICCUPPS).

## Tactics

| Tactic | Use |
|--------|-----|
| Change-based | Diff-informed tours first |
| Interruption | Pause sync, rotate device, switch network |
| Data variety | Garbage, unicode, huge payloads |
| Role switching | Same flow as two users |

## Debrief outputs

Confirmed defects, suspected risks (labeled), regression candidates, **unexplored questions** for next charter.

## Stopping

Timebox end OR mission satisfied OR blocked—never “done” because happy path once.

## Pairing

`qa-orchestrator` assigns charters after intake; specialists deep-dive confirmations.
