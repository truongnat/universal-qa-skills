# Scenario catalog — clean-code-architecture-auditor

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** SOLID, coupling metrics, ADRs, ISO 25010 maintainability  
**Typical environment:** Static analysis tools read-only; no refactor unless asked  
**P0 deep specs in this skill:** none (use generic rows)

### CLEA-001 — Intent-revealing naming

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *intent-revealing naming* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-001a` happy, `CLEA-001b` negative, `CLEA-001c` boundary or auth) before PASS |

### CLEA-002 — Module cohesion

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *module cohesion* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-002a` happy, `CLEA-002b` negative, `CLEA-002c` boundary or auth) before PASS |

### CLEA-003 — Single responsibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *single responsibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-003a` happy, `CLEA-003b` negative, `CLEA-003c` boundary or auth) before PASS |

### CLEA-004 — Hidden side effects

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *hidden side effects* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-004a` happy, `CLEA-004b` negative, `CLEA-004c` boundary or auth) before PASS |

### CLEA-005 — Dependency direction

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dependency direction* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-005a` happy, `CLEA-005b` negative, `CLEA-005c` boundary or auth) before PASS |

### CLEA-006 — Circular imports

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *circular imports* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-006a` happy, `CLEA-006b` negative, `CLEA-006c` boundary or auth) before PASS |

### CLEA-007 — Duplicated logic

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *duplicated logic* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-007a` happy, `CLEA-007b` negative, `CLEA-007c` boundary or auth) before PASS |

### CLEA-008 — Over-abstraction

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *over-abstraction* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-008a` happy, `CLEA-008b` negative, `CLEA-008c` boundary or auth) before PASS |

### CLEA-009 — Conditional complexity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *conditional complexity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-009a` happy, `CLEA-009b` negative, `CLEA-009c` boundary or auth) before PASS |

### CLEA-010 — Explicit error handling

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *explicit error handling* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-010a` happy, `CLEA-010b` negative, `CLEA-010c` boundary or auth) before PASS |

### CLEA-011 — Unhandled panics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unhandled panics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-011a` happy, `CLEA-011b` negative, `CLEA-011c` boundary or auth) before PASS |

### CLEA-012 — Resource cleanup

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *resource cleanup* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-012a` happy, `CLEA-012b` negative, `CLEA-012c` boundary or auth) before PASS |

### CLEA-013 — Thread safety

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *thread safety* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-013a` happy, `CLEA-013b` negative, `CLEA-013c` boundary or auth) before PASS |

### CLEA-014 — Validation boundaries

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *validation boundaries* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-014a` happy, `CLEA-014b` negative, `CLEA-014c` boundary or auth) before PASS |

### CLEA-015 — Public API compatibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *public api compatibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-015a` happy, `CLEA-015b` negative, `CLEA-015c` boundary or auth) before PASS |

### CLEA-016 — Dead code

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dead code* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-016a` happy, `CLEA-016b` negative, `CLEA-016c` boundary or auth) before PASS |

### CLEA-017 — Useful invariants in comments

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *useful invariants in comments* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-017a` happy, `CLEA-017b` negative, `CLEA-017c` boundary or auth) before PASS |

### CLEA-018 — Testability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *testability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-018a` happy, `CLEA-018b` negative, `CLEA-018c` boundary or auth) before PASS |

### CLEA-019 — Dependency hygiene

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dependency hygiene* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-019a` happy, `CLEA-019b` negative, `CLEA-019c` boundary or auth) before PASS |

### CLEA-020 — Secret-safe logging

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *secret-safe logging* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-020a` happy, `CLEA-020b` negative, `CLEA-020c` boundary or auth) before PASS |

### CLEA-021 — Configuration defaults

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *configuration defaults* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-021a` happy, `CLEA-021b` negative, `CLEA-021c` boundary or auth) before PASS |

### CLEA-022 — Abstraction leakage

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *abstraction leakage* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-022a` happy, `CLEA-022b` negative, `CLEA-022c` boundary or auth) before PASS |

### CLEA-023 — Avoiding quadratic loops

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *avoiding quadratic loops* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-023a` happy, `CLEA-023b` negative, `CLEA-023c` boundary or auth) before PASS |

### CLEA-024 — Serialization evolution

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *serialization evolution* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Dependency analysis, boundary violations, change-impact tracing |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | SOLID, coupling metrics, ADRs, ISO 25010 maintainability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `CLEA-024a` happy, `CLEA-024b` negative, `CLEA-024c` boundary or auth) before PASS |

