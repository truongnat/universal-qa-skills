# Scenario catalog — test-automation-auditor

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas  
**Typical environment:** CI history, local reproduce of failed jobs  
**P0 deep specs in this skill:** none (use generic rows)

### TEST-001 — Test portfolio risk fit

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *test portfolio risk fit* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-001a` happy, `TEST-001b` negative, `TEST-001c` boundary or auth) before PASS |

### TEST-002 — Unit invariant coverage

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unit invariant coverage* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-002a` happy, `TEST-002b` negative, `TEST-002c` boundary or auth) before PASS |

### TEST-003 — Integration boundary coverage

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *integration boundary coverage* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-003a` happy, `TEST-003b` negative, `TEST-003c` boundary or auth) before PASS |

### TEST-004 — End to end critical journeys

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *end to end critical journeys* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-004a` happy, `TEST-004b` negative, `TEST-004c` boundary or auth) before PASS |

### TEST-005 — Deterministic random seed

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *deterministic random seed* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-005a` happy, `TEST-005b` negative, `TEST-005c` boundary or auth) before PASS |

### TEST-006 — Frozen clocks

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *frozen clocks* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-006a` happy, `TEST-006b` negative, `TEST-006c` boundary or auth) before PASS |

### TEST-007 — Order independence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *order independence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-007a` happy, `TEST-007b` negative, `TEST-007c` boundary or auth) before PASS |

### TEST-008 — Fixture cleanup

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *fixture cleanup* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-008a` happy, `TEST-008b` negative, `TEST-008c` boundary or auth) before PASS |

### TEST-009 — Parallel isolation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *parallel isolation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-009a` happy, `TEST-009b` negative, `TEST-009c` boundary or auth) before PASS |

### TEST-010 — Behavioral assertions

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *behavioral assertions* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-010a` happy, `TEST-010b` negative, `TEST-010c` boundary or auth) before PASS |

### TEST-011 — Failure diagnostics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *failure diagnostics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-011a` happy, `TEST-011b` negative, `TEST-011c` boundary or auth) before PASS |

### TEST-012 — Flaky retry policy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *flaky retry policy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-012a` happy, `TEST-012b` negative, `TEST-012c` boundary or auth) before PASS |

### TEST-013 — Quarantine ownership

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *quarantine ownership* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-013a` happy, `TEST-013b` negative, `TEST-013c` boundary or auth) before PASS |

### TEST-014 — Coverage quality limits

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *coverage quality limits* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-014a` happy, `TEST-014b` negative, `TEST-014c` boundary or auth) before PASS |

### TEST-015 — Mutation testing

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *mutation testing* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-015a` happy, `TEST-015b` negative, `TEST-015c` boundary or auth) before PASS |

### TEST-016 — Contract drift

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *contract drift* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-016a` happy, `TEST-016b` negative, `TEST-016c` boundary or auth) before PASS |

### TEST-017 — Snapshot review

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *snapshot review* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-017a` happy, `TEST-017b` negative, `TEST-017c` boundary or auth) before PASS |

### TEST-018 — CI gating

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *ci gating* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-018a` happy, `TEST-018b` negative, `TEST-018c` boundary or auth) before PASS |

### TEST-019 — Runtime budget

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *runtime budget* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-019a` happy, `TEST-019b` negative, `TEST-019c` boundary or auth) before PASS |

### TEST-020 — Secrets in test data

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *secrets in test data* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-020a` happy, `TEST-020b` negative, `TEST-020c` boundary or auth) before PASS |

### TEST-021 — Build reproducibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *build reproducibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-021a` happy, `TEST-021b` negative, `TEST-021c` boundary or auth) before PASS |

### TEST-022 — Captured artifacts

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *captured artifacts* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-022a` happy, `TEST-022b` negative, `TEST-022c` boundary or auth) before PASS |

### TEST-023 — Release artifact targeting

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *release artifact targeting* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-023a` happy, `TEST-023b` negative, `TEST-023c` boundary or auth) before PASS |

### TEST-024 — Regression for known bugs

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *regression for known bugs* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Suite audit, mutation sanity, fixture review, pipeline gate analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Test pyramid, CI signals, flakiness metrics, ISO 29119-5 keyword ideas |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `TEST-024a` happy, `TEST-024b` negative, `TEST-024c` boundary or auth) before PASS |

