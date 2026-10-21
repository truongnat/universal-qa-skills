# Scenario catalog — release-readiness-auditor

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Exit criteria, change advisory, incident history  
**Typical environment:** RC build ID, signed artifacts list, open risk register  
**P0 deep specs in this skill:** none (use generic rows)

### RELE-001 — Artifact identity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *artifact identity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-001a` happy, `RELE-001b` negative, `RELE-001c` boundary or auth) before PASS |

### RELE-002 — Reproducible build

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *reproducible build* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-002a` happy, `RELE-002b` negative, `RELE-002c` boundary or auth) before PASS |

### RELE-003 — Package launch

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *package launch* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-003a` happy, `RELE-003b` negative, `RELE-003c` boundary or auth) before PASS |

### RELE-004 — Install and uninstall

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *install and uninstall* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-004a` happy, `RELE-004b` negative, `RELE-004c` boundary or auth) before PASS |

### RELE-005 — Upgrade smoke test

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *upgrade smoke test* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-005a` happy, `RELE-005b` negative, `RELE-005c` boundary or auth) before PASS |

### RELE-006 — Critical journey evidence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *critical journey evidence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-006a` happy, `RELE-006b` negative, `RELE-006c` boundary or auth) before PASS |

### RELE-007 — Outstanding critical defects

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *outstanding critical defects* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-007a` happy, `RELE-007b` negative, `RELE-007c` boundary or auth) before PASS |

### RELE-008 — Dependency security checks

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dependency security checks* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-008a` happy, `RELE-008b` negative, `RELE-008c` boundary or auth) before PASS |

### RELE-009 — Privacy checks

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *privacy checks* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-009a` happy, `RELE-009b` negative, `RELE-009c` boundary or auth) before PASS |

### RELE-010 — Accessibility target

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *accessibility target* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-010a` happy, `RELE-010b` negative, `RELE-010c` boundary or auth) before PASS |

### RELE-011 — Performance budget

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *performance budget* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-011a` happy, `RELE-011b` negative, `RELE-011c` boundary or auth) before PASS |

### RELE-012 — Backup restore readiness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *backup restore readiness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-012a` happy, `RELE-012b` negative, `RELE-012c` boundary or auth) before PASS |

### RELE-013 — Monitoring readiness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *monitoring readiness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-013a` happy, `RELE-013b` negative, `RELE-013c` boundary or auth) before PASS |

### RELE-014 — Incident response ownership

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *incident response ownership* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-014a` happy, `RELE-014b` negative, `RELE-014c` boundary or auth) before PASS |

### RELE-015 — Release notes accuracy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *release notes accuracy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-015a` happy, `RELE-015b` negative, `RELE-015c` boundary or auth) before PASS |

### RELE-016 — Feature flag rollback

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *feature flag rollback* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-016a` happy, `RELE-016b` negative, `RELE-016c` boundary or auth) before PASS |

### RELE-017 — Data migration readiness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *data migration readiness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Data correctness |
| **Variant matrix** | Before/after snapshots, checksums |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-017a` happy, `RELE-017b` negative, `RELE-017c` boundary or auth) before PASS |

### RELE-018 — Skipped tests reviewed

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *skipped tests reviewed* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-018a` happy, `RELE-018b` negative, `RELE-018c` boundary or auth) before PASS |

### RELE-019 — Cross-platform evidence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cross-platform evidence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-019a` happy, `RELE-019b` negative, `RELE-019c` boundary or auth) before PASS |

### RELE-020 — Formal exception sign-off

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *formal exception sign-off* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-020a` happy, `RELE-020b` negative, `RELE-020c` boundary or auth) before PASS |

### RELE-021 — Rollout monitoring

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rollout monitoring* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-021a` happy, `RELE-021b` negative, `RELE-021c` boundary or auth) before PASS |

### RELE-022 — Rollback thresholds

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rollback thresholds* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-022a` happy, `RELE-022b` negative, `RELE-022c` boundary or auth) before PASS |

### RELE-023 — Code signing

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *code signing* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-023a` happy, `RELE-023b` negative, `RELE-023c` boundary or auth) before PASS |

### RELE-024 — Post-release verification

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *post-release verification* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Evidence aggregation, defect trend, go/no-go workshop structure |
| **Scenario focus** | Gate evidence |
| **Variant matrix** | Residual risk table, sign-offs |
| **Oracle / anchor** | Exit criteria, change advisory, incident history |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `RELE-024a` happy, `RELE-024b` negative, `RELE-024c` boundary or auth) before PASS |

