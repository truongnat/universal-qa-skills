# Product Quality Model (ISO/IEC 25010)

Use to tag risks and coverage—not as a certification checklist. Prefer **25010:2023** naming where possible.

## Nine characteristics (mapping to skills)

| Characteristic | Sub-focus (examples) | Typical skill / gate |
|----------------|----------------------|----------------------|
| Functional suitability | Completeness, correctness, appropriateness | `functional-tester`, `requirements-test-designer` |
| Performance efficiency | Time behaviour, resource use, capacity | `performance-reliability-tester` |
| Compatibility | Co-existence, interoperability | `compatibility-localization-tester`, `api-contract-tester` |
| Interaction capability | Learnability, operability, user error protection, accessibility | `ux-accessibility-auditor`, `ui-visual-tester` |
| Reliability | Availability, fault tolerance, recoverability | `performance-reliability-tester`, `data-integrity-tester` |
| Security | Confidentiality, integrity, authenticity, resistance | `security-privacy-auditor` |
| Maintainability | Modularity, analysability, modifiability, testability | `clean-code-architecture-auditor`, `test-automation-auditor` |
| Flexibility (portability) | Adaptability, installability, replaceability | `compatibility-localization-tester` |
| Safety | Harm avoidance where applicable | Domain-specific; escalate when in scope |

*Note: 2011 edition used “Usability” and “Portability” as top-level names; map older docs to Interaction capability / Flexibility when reviewing.*

## Quality-in-use (brief)

When validating user outcomes, consider:

- Effectiveness, efficiency, satisfaction, freedom from risk, context coverage

Tie to **real tasks**, not only unit-level green tests.

## Reporting

In risk inventory, add column **Quality characteristic** (25010) for traceability to release gates.
