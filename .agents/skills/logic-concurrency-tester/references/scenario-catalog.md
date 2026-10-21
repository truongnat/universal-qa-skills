# Scenario catalog — logic-concurrency-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** State machines, locking docs, idempotency contracts  
**Typical environment:** Controllable parallelism; feature flags for timing hooks  
**P0 deep specs in this skill:** none (use generic rows)

### LOGI-001 — Invalid state transition

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *invalid state transition* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-001a` happy, `LOGI-001b` negative, `LOGI-001c` boundary or auth) before PASS |

### LOGI-002 — Repeated event

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *repeated event* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-002a` happy, `LOGI-002b` negative, `LOGI-002c` boundary or auth) before PASS |

### LOGI-003 — Stale asynchronous response

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *stale asynchronous response* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-003a` happy, `LOGI-003b` negative, `LOGI-003c` boundary or auth) before PASS |

### LOGI-004 — Cancel versus complete race

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cancel versus complete race* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-004a` happy, `LOGI-004b` negative, `LOGI-004c` boundary or auth) before PASS |

### LOGI-005 — Concurrent writes

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *concurrent writes* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-005a` happy, `LOGI-005b` negative, `LOGI-005c` boundary or auth) before PASS |

### LOGI-006 — Partial transaction failure

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *partial transaction failure* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-006a` happy, `LOGI-006b` negative, `LOGI-006c` boundary or auth) before PASS |

### LOGI-007 — Lost update

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *lost update* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-007a` happy, `LOGI-007b` negative, `LOGI-007c` boundary or auth) before PASS |

### LOGI-008 — Optimistic lock conflict

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *optimistic lock conflict* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-008a` happy, `LOGI-008b` negative, `LOGI-008c` boundary or auth) before PASS |

### LOGI-009 — TOCTOU

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *toctou* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-009a` happy, `LOGI-009b` negative, `LOGI-009c` boundary or auth) before PASS |

### LOGI-010 — Resource lifecycle race

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *resource lifecycle race* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-010a` happy, `LOGI-010b` negative, `LOGI-010c` boundary or auth) before PASS |

### LOGI-011 — Out of order events

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *out of order events* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-011a` happy, `LOGI-011b` negative, `LOGI-011c` boundary or auth) before PASS |

### LOGI-012 — Replay processing

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *replay processing* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-012a` happy, `LOGI-012b` negative, `LOGI-012c` boundary or auth) before PASS |

### LOGI-013 — Retry amplification

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *retry amplification* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-013a` happy, `LOGI-013b` negative, `LOGI-013c` boundary or auth) before PASS |

### LOGI-014 — Queue saturation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *queue saturation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-014a` happy, `LOGI-014b` negative, `LOGI-014c` boundary or auth) before PASS |

### LOGI-015 — Deadlock

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *deadlock* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-015a` happy, `LOGI-015b` negative, `LOGI-015c` boundary or auth) before PASS |

### LOGI-016 — Starvation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *starvation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-016a` happy, `LOGI-016b` negative, `LOGI-016c` boundary or auth) before PASS |

### LOGI-017 — Cache invalidation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cache invalidation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-017a` happy, `LOGI-017b` negative, `LOGI-017c` boundary or auth) before PASS |

### LOGI-018 — Integer overflow

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *integer overflow* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-018a` happy, `LOGI-018b` negative, `LOGI-018c` boundary or auth) before PASS |

### LOGI-019 — Decimal rounding

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *decimal rounding* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-019a` happy, `LOGI-019b` negative, `LOGI-019c` boundary or auth) before PASS |

### LOGI-020 — Null semantics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *null semantics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-020a` happy, `LOGI-020b` negative, `LOGI-020c` boundary or auth) before PASS |

### LOGI-021 — Clock skew

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *clock skew* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-021a` happy, `LOGI-021b` negative, `LOGI-021c` boundary or auth) before PASS |

### LOGI-022 — Restart recovery

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *restart recovery* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-022a` happy, `LOGI-022b` negative, `LOGI-022c` boundary or auth) before PASS |

### LOGI-023 — Mid-operation feature flag

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *mid-operation feature flag* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-023a` happy, `LOGI-023b` negative, `LOGI-023c` boundary or auth) before PASS |

### LOGI-024 — Exactly-once cleanup

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *exactly-once cleanup* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Race harness (bounded), double-submit, clock skew simulation, property checks |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | State machines, locking docs, idempotency contracts |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `LOGI-024a` happy, `LOGI-024b` negative, `LOGI-024c` boundary or auth) before PASS |

