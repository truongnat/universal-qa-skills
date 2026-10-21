# Scenario catalog — requirements-test-designer

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** User stories, NFRs, ISO 29119-4 technique mapping  
**Typical environment:** Access to specs, mocks, and historical defects  
**P0 deep specs in this skill:** none (use generic rows)

### REQU-001 — Ambiguous acceptance criteria

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *ambiguous acceptance criteria* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Testability |
| **Variant matrix** | Given-when-then rewrite, measurable AC |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-001a` happy, `REQU-001b` negative, `REQU-001c` boundary or auth) before PASS |

### REQU-002 — Mandatory optional fields

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *mandatory optional fields* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-002a` happy, `REQU-002b` negative, `REQU-002c` boundary or auth) before PASS |

### REQU-003 — Empty null missing values

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *empty null missing values* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-003a` happy, `REQU-003b` negative, `REQU-003c` boundary or auth) before PASS |

### REQU-004 — Whitespace and trim policy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *whitespace and trim policy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-004a` happy, `REQU-004b` negative, `REQU-004c` boundary or auth) before PASS |

### REQU-005 — Input min boundary

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *input min boundary* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-005a` happy, `REQU-005b` negative, `REQU-005c` boundary or auth) before PASS |

### REQU-006 — Input max boundary

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *input max boundary* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-006a` happy, `REQU-006b` negative, `REQU-006c` boundary or auth) before PASS |

### REQU-007 — Off-by-one errors

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *off-by-one errors* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-007a` happy, `REQU-007b` negative, `REQU-007c` boundary or auth) before PASS |

### REQU-008 — Equivalent valid classes

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *equivalent valid classes* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-008a` happy, `REQU-008b` negative, `REQU-008c` boundary or auth) before PASS |

### REQU-009 — Equivalent invalid classes

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *equivalent invalid classes* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-009a` happy, `REQU-009b` negative, `REQU-009c` boundary or auth) before PASS |

### REQU-010 — Decision table interactions

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *decision table interactions* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-010a` happy, `REQU-010b` negative, `REQU-010c` boundary or auth) before PASS |

### REQU-011 — State transition validity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *state transition validity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-011a` happy, `REQU-011b` negative, `REQU-011c` boundary or auth) before PASS |

### REQU-012 — Role and permission matrix

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *role and permission matrix* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-012a` happy, `REQU-012b` negative, `REQU-012c` boundary or auth) before PASS |

### REQU-013 — Idempotency expectations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *idempotency expectations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-013a` happy, `REQU-013b` negative, `REQU-013c` boundary or auth) before PASS |

### REQU-014 — Duplicate submission

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *duplicate submission* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-014a` happy, `REQU-014b` negative, `REQU-014c` boundary or auth) before PASS |

### REQU-015 — Date and time rules

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *date and time rules* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-015a` happy, `REQU-015b` negative, `REQU-015c` boundary or auth) before PASS |

### REQU-016 — Timezone and DST

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *timezone and dst* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Locale matrix |
| **Variant matrix** | Pseudo-loc, RTL mirror, DST boundary |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-016a` happy, `REQU-016b` negative, `REQU-016c` boundary or auth) before PASS |

### REQU-017 — Decimal and rounding

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *decimal and rounding* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-017a` happy, `REQU-017b` negative, `REQU-017c` boundary or auth) before PASS |

### REQU-018 — Unicode normalization

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unicode normalization* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-018a` happy, `REQU-018b` negative, `REQU-018c` boundary or auth) before PASS |

### REQU-019 — Feature flag behavior

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *feature flag behavior* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-019a` happy, `REQU-019b` negative, `REQU-019c` boundary or auth) before PASS |

### REQU-020 — Migration acceptance

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *migration acceptance* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Data correctness |
| **Variant matrix** | Before/after snapshots, checksums |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-020a` happy, `REQU-020b` negative, `REQU-020c` boundary or auth) before PASS |

### REQU-021 — Partial success semantics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *partial success semantics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-021a` happy, `REQU-021b` negative, `REQU-021c` boundary or auth) before PASS |

### REQU-022 — Interrupted operations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *interrupted operations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-022a` happy, `REQU-022b` negative, `REQU-022c` boundary or auth) before PASS |

### REQU-023 — Test oracle independence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *test oracle independence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-023a` happy, `REQU-023b` negative, `REQU-023c` boundary or auth) before PASS |

### REQU-024 — Traceability completeness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *traceability completeness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Ambiguity mining, testability review, traceability matrix authoring |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | User stories, NFRs, ISO 29119-4 technique mapping |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `REQU-024a` happy, `REQU-024b` negative, `REQU-024c` boundary or auth) before PASS |

