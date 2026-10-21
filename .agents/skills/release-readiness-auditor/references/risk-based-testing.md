# Risk-Based Testing Mechanisms

Aligned with ISO/IEC/IEEE 29119-1/29119-2 risk-based approach and ISTQB risk-based test strategy.

## Risk formula

**Risk level = Impact × Likelihood** (use 1–5 scales or Low/Med/High consistently in the report).

| Impact | Guideline |
|--------|-----------|
| 5 | Safety, data loss, legal, auth bypass, revenue stop |
| 4 | Major journey broken, corrupt data, breach class issues |
| 3 | Degraded core feature, workaround exists |
| 2 | Minor feature, edge case |
| 1 | Cosmetic, rare edge |

Document **assumptions** when likelihood is estimated without production data.

## Product vs project risk

| Kind | Examples | Test response |
|------|----------|---------------|
| Product | Wrong calculation, IDOR, data loss | Design cases targeting failure modes |
| Project | Late env, missing spec, skill gap | BLOCKED / NOT TESTED, escalate, narrow scope |

## Risk-based workflow

1. **Identify** quality risks from requirements, architecture, changes, incidents, regulations.
2. **Assess** impact and likelihood; assign risk ID (R-001…).
3. **Mitigate via testing** — select techniques, levels, and depth (see `test-design-techniques.md`).
4. **Execute** and record evidence per case.
5. **Re-evaluate** residual risk for release (orchestrator / release-readiness).

## Prioritization rules

- Cover **all** risk IDs rated at or above the project threshold (define threshold in plan).
- Map each selected risk to ≥1 test ID in the traceability table.
- When timeboxed: run highest risk first; never silently drop high risk without NOT TESTED + owner.

## Regression selection

Prioritize regression for:

- Areas touched by the change set (diff-informed)
- Historical defect clusters
- Shared components and integration boundaries
- Security and data paths

## Residual risk statement (release)

Include in release assessment:

| Risk ID | Residual level | Rationale | Accepted by |
|---------|----------------|-----------|-------------|
| | | | |

Use `risk-register-template.csv` for machine-friendly export when helpful.
