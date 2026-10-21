# Domain playbook — clean-code-architecture-auditor

## Mission

Evaluate **maintainability and architectural integrity**—boundaries, coupling, testability—for release risk, not style wars.

## Focus areas

| Signal | Investigation |
|--------|----------------|
| Layer violation | UI calling DB; domain importing infra |
| God modules | High churn + high fan-in |
| Duplication | Same business rule in 3 services |
| Testability | Heavy static/singleton blocking tests |
| ADR drift | Code contradicts documented decisions |

## Techniques

- Dependency graph (tool or manual import trace).
- Change-impact: follow one feature across modules.
- Smell list with **concrete file references**—no vague “needs refactor.”

## Output

Design concerns (severity) separate from functional bugs. Suggest **test seam** or boundary fix.

## Pairing

`test-automation-auditor` when architecture blocks reliable tests.
