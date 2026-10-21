# Scenario catalog — performance-reliability-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability  
**Typical environment:** Dedicated perf env; metrics dashboards; never default-load production  
**P0 deep specs in this skill:** none (use generic rows)

### PERF-001 — Cold start

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cold start* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-001a` happy, `PERF-001b` negative, `PERF-001c` boundary or auth) before PASS |

### PERF-002 — Warm start

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *warm start* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-002a` happy, `PERF-002b` negative, `PERF-002c` boundary or auth) before PASS |

### PERF-003 — First meaningful result

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *first meaningful result* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-003a` happy, `PERF-003b` negative, `PERF-003c` boundary or auth) before PASS |

### PERF-004 — Median latency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *median latency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-004a` happy, `PERF-004b` negative, `PERF-004c` boundary or auth) before PASS |

### PERF-005 — P95 latency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *p95 latency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-005a` happy, `PERF-005b` negative, `PERF-005c` boundary or auth) before PASS |

### PERF-006 — P99 latency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *p99 latency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-006a` happy, `PERF-006b` negative, `PERF-006c` boundary or auth) before PASS |

### PERF-007 — Peak throughput

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *peak throughput* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-007a` happy, `PERF-007b` negative, `PERF-007c` boundary or auth) before PASS |

### PERF-008 — Concurrency scaling

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *concurrency scaling* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-008a` happy, `PERF-008b` negative, `PERF-008c` boundary or auth) before PASS |

### PERF-009 — Load ramp

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *load ramp* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-009a` happy, `PERF-009b` negative, `PERF-009c` boundary or auth) before PASS |

### PERF-010 — Burst recovery

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *burst recovery* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-010a` happy, `PERF-010b` negative, `PERF-010c` boundary or auth) before PASS |

### PERF-011 — Soak stability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *soak stability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-011a` happy, `PERF-011b` negative, `PERF-011c` boundary or auth) before PASS |

### PERF-012 — Memory leaks

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *memory leaks* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-012a` happy, `PERF-012b` negative, `PERF-012c` boundary or auth) before PASS |

### PERF-013 — Large payloads

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *large payloads* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-013a` happy, `PERF-013b` negative, `PERF-013c` boundary or auth) before PASS |

### PERF-014 — Slow dependency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *slow dependency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-014a` happy, `PERF-014b` negative, `PERF-014c` boundary or auth) before PASS |

### PERF-015 — Timeout cascade

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *timeout cascade* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-015a` happy, `PERF-015b` negative, `PERF-015c` boundary or auth) before PASS |

### PERF-016 — Retry storm

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *retry storm* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-016a` happy, `PERF-016b` negative, `PERF-016c` boundary or auth) before PASS |

### PERF-017 — Pool exhaustion

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *pool exhaustion* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-017a` happy, `PERF-017b` negative, `PERF-017c` boundary or auth) before PASS |

### PERF-018 — Backpressure

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *backpressure* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-018a` happy, `PERF-018b` negative, `PERF-018c` boundary or auth) before PASS |

### PERF-019 — CPU saturation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cpu saturation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-019a` happy, `PERF-019b` negative, `PERF-019c` boundary or auth) before PASS |

### PERF-020 — Disk saturation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *disk saturation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-020a` happy, `PERF-020b` negative, `PERF-020c` boundary or auth) before PASS |

### PERF-021 — Frame time and UI jank

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *frame time and ui jank* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-021a` happy, `PERF-021b` negative, `PERF-021c` boundary or auth) before PASS |

### PERF-022 — Network reconnection

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *network reconnection* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-022a` happy, `PERF-022b` negative, `PERF-022c` boundary or auth) before PASS |

### PERF-023 — Crash recovery

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *crash recovery* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-023a` happy, `PERF-023b` negative, `PERF-023c` boundary or auth) before PASS |

### PERF-024 — Measured regression

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *measured regression* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Load/stress/soak (approved), fault injection, chaos-lite, retry/timeout analysis |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SLO/SLA, capacity model, ISO 25010 performance efficiency & reliability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `PERF-024a` happy, `PERF-024b` negative, `PERF-024c` boundary or auth) before PASS |

