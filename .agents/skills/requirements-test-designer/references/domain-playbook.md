# Domain playbook — requirements-test-designer

## Mission

Turn ambiguous requirements into **testable, traceable** conditions and **prioritized test designs** before heavy execution.

## Review checklist

| Defect in req | Example fix |
|---------------|-------------|
| Ambiguous | “Fast” → p95 < 300ms on 4G |
| Untestable | “User-friendly” → task success metric |
| Missing NFR | Security, a11y, retention |
| Conflict | AC vs mockup |

## Deliverables

- Requirements traceability matrix (req → risk → test ID).
- Technique assignment per requirement (29119-4).
- Coverage items explicit (states, rules, platforms).

## Test design quality bar

Each proposed case has **independent oracle**, **data needs**, and **automation feasibility** note.

## Pairing

Feeds `functional-tester`, `qa-orchestrator` planning; does not replace execution PASS.
