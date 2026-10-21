# Scenario catalog — qa-orchestrator

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** ISO 29119 risk-based strategy, release exit criteria, traceability  
**Typical environment:** Access to change list, environments matrix, stakeholder priorities  
**P0 deep specs in this skill:** none (use generic rows)

### ORCH-001 — Intake and test basis

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *intake and test basis* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-001a` happy, `ORCH-001b` negative, `ORCH-001c` boundary or auth) before PASS |

### ORCH-002 — Quality attribute coverage

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *quality attribute coverage* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-002a` happy, `ORCH-002b` negative, `ORCH-002c` boundary or auth) before PASS |

### ORCH-003 — Stakeholder risk alignment

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *stakeholder risk alignment* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-003a` happy, `ORCH-003b` negative, `ORCH-003c` boundary or auth) before PASS |

### ORCH-004 — Requirements traceability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *requirements traceability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-004a` happy, `ORCH-004b` negative, `ORCH-004c` boundary or auth) before PASS |

### ORCH-005 — Release exit criteria

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *release exit criteria* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-005a` happy, `ORCH-005b` negative, `ORCH-005c` boundary or auth) before PASS |

### ORCH-006 — Environment readiness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *environment readiness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-006a` happy, `ORCH-006b` negative, `ORCH-006c` boundary or auth) before PASS |

### ORCH-007 — Fixture safety

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *fixture safety* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-007a` happy, `ORCH-007b` negative, `ORCH-007c` boundary or auth) before PASS |

### ORCH-008 — Static versus dynamic evidence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *static versus dynamic evidence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-008a` happy, `ORCH-008b` negative, `ORCH-008c` boundary or auth) before PASS |

### ORCH-009 — Functional suite strategy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *functional suite strategy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-009a` happy, `ORCH-009b` negative, `ORCH-009c` boundary or auth) before PASS |

### ORCH-010 — Accessibility gate

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *accessibility gate* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-010a` happy, `ORCH-010b` negative, `ORCH-010c` boundary or auth) before PASS |

### ORCH-011 — Security gate

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *security gate* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-011a` happy, `ORCH-011b` negative, `ORCH-011c` boundary or auth) before PASS |

### ORCH-012 — Reliability gate

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *reliability gate* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-012a` happy, `ORCH-012b` negative, `ORCH-012c` boundary or auth) before PASS |

### ORCH-013 — Performance budget

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *performance budget* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-013a` happy, `ORCH-013b` negative, `ORCH-013c` boundary or auth) before PASS |

### ORCH-014 — Cross-platform matrix

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cross-platform matrix* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-014a` happy, `ORCH-014b` negative, `ORCH-014c` boundary or auth) before PASS |

### ORCH-015 — High-severity review

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *high-severity review* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-015a` happy, `ORCH-015b` negative, `ORCH-015c` boundary or auth) before PASS |

### ORCH-016 — Defect deduplication

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *defect deduplication* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-016a` happy, `ORCH-016b` negative, `ORCH-016c` boundary or auth) before PASS |

### ORCH-017 — Cross-agent conflict resolution

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cross-agent conflict resolution* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-017a` happy, `ORCH-017b` negative, `ORCH-017c` boundary or auth) before PASS |

### ORCH-018 — Regression ownership

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *regression ownership* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-018a` happy, `ORCH-018b` negative, `ORCH-018c` boundary or auth) before PASS |

### ORCH-019 — Blocked-test escalation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *blocked-test escalation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-019a` happy, `ORCH-019b` negative, `ORCH-019c` boundary or auth) before PASS |

### ORCH-020 — Release decision

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *release decision* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Risk workshops, gate reviews, coverage reconciliation, multi-agent merge |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | ISO 29119 risk-based strategy, release exit criteria, traceability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `ORCH-020a` happy, `ORCH-020b` negative, `ORCH-020c` boundary or auth) before PASS |

