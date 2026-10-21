# Oracles and Heuristics

**Oracle:** source to determine **expected** results to compare with actual behavior (ISTQB glossary).  
**Heuristic:** fallible rule of thumb that helps find problems or guide exploration—not a guarantee.

Never use **only** the implementation under test as the oracle for behavioral correctness.

## Independent oracle sources (priority)

1. Written requirements, AC, contracts, OpenAPI, legal/regulatory text
2. Prior production or legacy system (benchmark) with known-good scope
3. Domain rules (math, accounting, standards)
4. Comparable products (careful: not all differences are bugs)
5. Stakeholder claims in docs/marketing (Claims oracle)

Record **which oracle** justified each expected result in the matrix.

## FEW HICCUPPS (consistency heuristics)

Use to **suspect** problems during exploration; confirm with a stronger oracle before CONFIRMED defect.

| Letter | Heuristic | Example prompt |
|--------|-----------|----------------|
| **F**amiliarity | Unlike known good patterns | “This error format differs from every other API here.” |
| **E**xplainability | Behavior hard to articulate | “I cannot explain why this total changes on refresh.” |
| **W**orld | Violates real-world rules | “Negative inventory with no backorder flag.” |
| **H**istory | Breaks past behavior without notice | “v2 API dropped field clients still send.” |
| **I**mage | Unprofessional vs brand/UX standards | “Broken layout on first screen.” |
| **C**omparable products | Differs from peer apps users expect | “No undo on destructive action unlike competitors.” |
| **C**laims | Contradicts spec or help text | “Help says unlimited; UI caps at 10.” |
| **U**ser expectations | Reasonable user surprise | “Enter submits form without warning.” |
| **P**roduct | Inconsistent within same product | “Delete works in list view but not detail.” |
| **P**urpose | Undermines feature goal | “Export button produces empty file.” |
| **S**tandards/statutes | WCAG, OWASP, locale law | “Focus trap in modal fails WCAG 2.2.” |

## SFDPOT (coverage guidewords)

Structure exploratory tours and gap analysis:

| Guideword | Focus |
|-----------|--------|
| **S**tructure | Code, modules, DOM, schema |
| **F**unction | Features, interactions |
| **D**ata | Inputs, persistence, migration |
| **P**latform | OS, browser, device, locale |
| **O**perations | Deploy, config, monitoring, backup |
| **T**ime | Timeouts, TTL, cron, ordering, clock skew |

## Session-based exploratory (mechanism)

1. **Charter** — mission, risk hypothesis, timebox (`exploratory-session-template.md`)
2. **Execute** — note timestamped actions
3. **Debrief** — findings, suspected risks, regression candidates

## Stopping heuristics

Stop a session or cycle when:

- Charter mission satisfied or timebox ended
- New findings rate drops and high-risk areas covered
- Blocker prevents meaningful progress (document BLOCKED)

Do not stop solely because “happy path passed once.”
