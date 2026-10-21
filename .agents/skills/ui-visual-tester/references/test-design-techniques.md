# Test Design Techniques (ISO/IEC/IEEE 29119-4 aligned)

Select techniques based on **risk**, **test basis** (spec, code, experience), and **test item** type. Record the **technique per test ID** in the execution matrix.

## Specification-based (black-box)

| Technique | When to use | Typical output |
|-----------|-------------|----------------|
| Equivalence partitioning | Inputs with classes of valid/invalid data | One case per class + invalid class |
| Boundary value analysis | Ordered ranges, lengths, counts | min, min+1, max-1, max, just outside |
| Decision table | Business rules with combinations | Table of conditions → actions |
| State transition | FSM, workflows, status fields | Valid/invalid transitions, n-switch |
| Use case / scenario | End-to-end journeys | Steps + oracles per actor |
| Pairwise / combinatorial | Many independent parameters | Reduced combination set |
| Metamorphic | Multiple outputs related by known relation | Property checks across inputs |
| Requirements-based | AC / user stories | Traceable cases per requirement ID |

## Structure-based (white-box / gray-box)

| Technique | When to use | Notes |
|-----------|-------------|-------|
| Statement / branch coverage | Unit or critical logic | Coverage % is a means, not a goal alone |
| Path (limited) | High-risk modules | Avoid exponential path explosion |
| API/route surface | Controllers, handlers | Map endpoints to cases |

Use structure techniques to **supplement**, not replace, specification-based tests for user-visible behavior.

## Experience-based

| Technique | When to use | Artifacts |
|-----------|-------------|-----------|
| Exploratory testing | Unknown areas, integration surprises | Charter (`exploratory-session-template.md`) |
| Error guessing | Historical bug patterns | Checklist from past incidents |
| Checklist-based | Standards gates (a11y, OWASP) | Criterion ID per row |

## Technique selection heuristic

```
IF clear rules with many factors → decision table + pairwise
IF workflow / status → state transition + use case
IF numeric limits → BVA + equivalence
IF new or opaque area → exploratory charter + SFDPOT (oracles-and-heuristics.md)
IF security → OWASP ASVS mapping + negative abuse cases
IF performance → load model + budgets (measured, not guessed)
```

## Test case minimum (29119-style)

Each derived case includes:

- **Preconditions** (environment, data, auth)
- **Inputs / actions**
- **Expected results** from an **independent oracle** (not only “code says so”)
- **Postconditions / cleanup**

## Coverage items

State what is covered: requirement IDs, states, branches, WCAG criteria, ASVS controls, platforms—not vague “feature tested.”
