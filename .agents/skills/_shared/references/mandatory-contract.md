# Mandatory Testing Contract

1. Read project-level instructions, architecture, and requirements before testing. Apply `testing-principles.md` and `agent-qa-mechanisms.md` (untrusted basis, evidence tiers). Identify technology, platforms, scope, and critical risks.
2. Assess and prioritize via `risk-based-testing.md` (**impact × likelihood**). Select test design techniques from `test-design-techniques.md`. Record exclusions and N/A with reasons. Never claim that every catalog entry applies or that defects are absent.
3. For each chosen case produce **precondition, fixture, action/steps, expected result from an independent oracle** (`oracles-and-heuristics.md`), cleanup, priority, quality attribute tag (`quality-attribute-model.md`), and evidence.
4. Cover applicable variants: happy path, invalid inputs, min/max boundaries, repeated operations, interrupted/cancelled operations, concurrent access, persistence/restart, compatibility, and accessibility.
5. Run only authorized **non-destructive** checks using available tools. Block tests that could affect production, external targets, or secrets until authorized.
6. Record actual execution: version, command, environment, logs, captures, and test data. Static code inspection does **not** count as runtime visual/functional PASS.
7. Report findings with reproducibility, severity, confidence, and a candidate regression test. Use NOT TESTED or BLOCKED when evidence is missing.
8. Follow bundled reference templates. Never invent screenshots, defects, CVEs, timings, or compliance claims.
9. Present all deliverables using **structured markdown** per `report-output-format.md` (tables, sections, bullets)—not unstructured prose only.
