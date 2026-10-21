# Domain playbook — functional-tester

## Mission

Prove **business-critical journeys** and **rules** against **independent oracles** (AC, domain law, legacy benchmark)—not developer narration alone.

## P0 scenario set

Deep specs: **FUNC-003, 006, 008, 009, 010, 019, 020, 021, 023, 024** (see `scenario-catalog.md`). Run these for any release affecting users, auth, data lifecycle, or collaboration.

## Journey map template

| Journey ID | Persona | Steps | FUNC IDs | Risk |
|------------|---------|-------|----------|------|
| J-01 | new_user | signup → onboard → first action | FUNC-001 | high |

Link every executed test to **J-xx** or **FUNC-xxx** and **risk ID**.

## Personas & data

| Persona | Seed data needs |
|---------|-----------------|
| New | Empty account, defaults |
| Standard | Typical catalog/order history |
| Restricted | RBAC-limited |
| Admin | Elevated, separate tenant if multi-tenant |

Never use production PII. Document fixture version in report.

## CRUD depth (per entity)

For each business entity in scope:

1. **Create** valid / invalid (**FUNC-003**) / duplicate / boundary lengths.
2. **Read** own / unauthorized (**FUNC-006**) / not found.
3. **Update** happy / conflict (**FUNC-008**).
4. **Delete** confirm (**FUNC-009**) / recovery (**FUNC-010**).
5. **List** search, filter pairs, pagination edges (FUNC-011–015).

## Workflow & state machines

Draw states from spec. For each transition:

- Valid trigger → expected state.
- Invalid trigger → stable state + user-safe error.
- Interrupted mid-flow → resume or clean rollback.

## Resilience pack

| Pattern | FUNC / technique | Pass criteria |
|---------|------------------|---------------|
| Unsaved navigate | FUNC-019 | Prompt or autosave per spec |
| Session idle | FUNC-020 | Re-auth, no stale PII |
| Offline sync | FUNC-021 | No duplicate side effects |
| Process kill | FUNC-023 | Persisted vs ephemeral clear |
| Two users | FUNC-024 | No silent overwrite |

## Search & bulk

- Unicode and case (**FUNC-012**)
- Filter combinations — pairwise (**FUNC-013**)
- Import bad rows (**FUNC-017**) / export fidelity (**FUNC-018**)
- Bulk (**FUNC-016**) partial success rules

## Oracle hierarchy

1. Written AC / Gherkin in ticket.
2. Help/docs (Claims).
3. Domain rules (tax, inventory).
4. Legacy system sample (benchmark).
5. FEW HICCUPPS for exploration only → confirm before CONFIRMED.

Code inspection alone → **LIKELY**, not journey PASS.

## Evidence per journey

| Field | Required |
|-------|----------|
| Build/version | Yes |
| Persona | Yes |
| Steps | Numbered |
| Expected | Quote AC ID |
| Actual | Observable |
| Data snapshot | If persistence claim |

## Severity (functional)

| Sev | Example |
|-----|---------|
| S1 | Cannot pay, data loss, wrong legal total |
| S2 | Wrong validation blocking edge case with workaround |
| S3 | Copy/label |

## Anti-patterns

- One happy path per feature.
- Skipping unauthorized read after implementing create.
- PASS from mocked backend without label “mock”.

## Pairing

| Skill | When |
|-------|------|
| `requirements-test-designer` | AC ambiguous before execution |
| `security-privacy-auditor` | FUNC-006 + SECU-004 together |
| `data-integrity-tester` | Post-conditions in DB |
| `ux-accessibility-auditor` | Form errors and focus |

## Report minimum

Journey coverage table, P0 FUNC results, CRUD matrix per entity, blocked/N/A with reasons, regression list.
