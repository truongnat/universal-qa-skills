# Scenario catalog — exploratory-bug-hunter

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Charters, FEW HICCUPPS, session notes  
**Typical environment:** Fresh build; logging elevated; safe data  
**P0 deep specs in this skill:** none (use generic rows)

### EXPL-001 — New user tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *new user tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-001a` happy, `EXPL-001b` negative, `EXPL-001c` boundary or auth) before PASS |

### EXPL-002 — Expert workflow tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *expert workflow tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-002a` happy, `EXPL-002b` negative, `EXPL-002c` boundary or auth) before PASS |

### EXPL-003 — Error recovery tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *error recovery tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-003a` happy, `EXPL-003b` negative, `EXPL-003c` boundary or auth) before PASS |

### EXPL-004 — Input boundary tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *input boundary tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-004a` happy, `EXPL-004b` negative, `EXPL-004c` boundary or auth) before PASS |

### EXPL-005 — Interrupt and retry tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *interrupt and retry tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-005a` happy, `EXPL-005b` negative, `EXPL-005c` boundary or auth) before PASS |

### EXPL-006 — Rapid navigation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rapid navigation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-006a` happy, `EXPL-006b` negative, `EXPL-006c` boundary or auth) before PASS |

### EXPL-007 — Permission switching

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *permission switching* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-007a` happy, `EXPL-007b` negative, `EXPL-007c` boundary or auth) before PASS |

### EXPL-008 — Data lifecycle

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *data lifecycle* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-008a` happy, `EXPL-008b` negative, `EXPL-008c` boundary or auth) before PASS |

### EXPL-009 — Malformed inputs

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *malformed inputs* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-009a` happy, `EXPL-009b` negative, `EXPL-009c` boundary or auth) before PASS |

### EXPL-010 — Large dataset

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *large dataset* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-010a` happy, `EXPL-010b` negative, `EXPL-010c` boundary or auth) before PASS |

### EXPL-011 — Localization tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *localization tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-011a` happy, `EXPL-011b` negative, `EXPL-011c` boundary or auth) before PASS |

### EXPL-012 — Keyboard-only exploration

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *keyboard-only exploration* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-012a` happy, `EXPL-012b` negative, `EXPL-012c` boundary or auth) before PASS |

### EXPL-013 — Offline tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *offline tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-013a` happy, `EXPL-013b` negative, `EXPL-013c` boundary or auth) before PASS |

### EXPL-014 — Multi-session tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *multi-session tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | AuthN/AuthZ abuse cases |
| **Variant matrix** | Lockout BVA, MFA bypass attempts, session fixation |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-014a` happy, `EXPL-014b` negative, `EXPL-014c` boundary or auth) before PASS |

### EXPL-015 — Upgrade tour

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *upgrade tour* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Session-based ET |
| **Variant matrix** | 90-min charter, debrief table |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-015a` happy, `EXPL-015b` negative, `EXPL-015c` boundary or auth) before PASS |

### EXPL-016 — Unexpected combinations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unexpected combinations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-016a` happy, `EXPL-016b` negative, `EXPL-016c` boundary or auth) before PASS |

### EXPL-017 — Repeated cancellation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *repeated cancellation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-017a` happy, `EXPL-017b` negative, `EXPL-017c` boundary or auth) before PASS |

### EXPL-018 — Time anomalies

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *time anomalies* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-018a` happy, `EXPL-018b` negative, `EXPL-018c` boundary or auth) before PASS |

### EXPL-019 — Resource exhaustion

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *resource exhaustion* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-019a` happy, `EXPL-019b` negative, `EXPL-019c` boundary or auth) before PASS |

### EXPL-020 — Cross-feature integration

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cross-feature integration* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-020a` happy, `EXPL-020b` negative, `EXPL-020c` boundary or auth) before PASS |

### EXPL-021 — State switching

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *state switching* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-021a` happy, `EXPL-021b` negative, `EXPL-021c` boundary or auth) before PASS |

### EXPL-022 — Random replayable sequence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *random replayable sequence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-022a` happy, `EXPL-022b` negative, `EXPL-022c` boundary or auth) before PASS |

### EXPL-023 — Visual consistency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *visual consistency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Perceptual consistency |
| **Variant matrix** | Breakpoint sweep, overflow strings |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-023a` happy, `EXPL-023b` negative, `EXPL-023c` boundary or auth) before PASS |

### EXPL-024 — Unexpected data loss

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unexpected data loss* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Timeboxed tours, SFDPOT, error guessing from change log |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Charters, FEW HICCUPPS, session notes |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `EXPL-024a` happy, `EXPL-024b` negative, `EXPL-024c` boundary or auth) before PASS |

