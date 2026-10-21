# Scenario catalog — data-integrity-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** ACID expectations, migration notes, backup/restore runbooks  
**Typical environment:** Disposable DB clone; point-in-time snapshots  
**P0 deep specs in this skill:** DATA-001, DATA-002, DATA-003, DATA-012, DATA-015, DATA-024

### DATA-001 — Atomic mutation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Multi-step mutations commit or roll back atomically—no torn state. |
| **Primary techniques** | Inject failure mid-transaction (staging); verify invariants. |
| **Scenario focus** | Atomic mutation |
| **Variant matrix** | Transfer funds pattern; parent-child insert; saga vs ACID. |
| **Oracle / anchor** | Transaction design doc |
| **Failure signals** | Debit without credit; orphan rows. |
| **Evidence** | DB constraint queries before/after. |
| **Minimum atomic cases** | DATA-001a success all committed; DATA-001b failure none partial. |

### DATA-002 — Isolation anomalies

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Isolation level prevents dirty read, lost update, phantom where specified. |
| **Primary techniques** | Parallel sessions (bounded); repeatable read check. |
| **Scenario focus** | Isolation anomalies |
| **Variant matrix** | READ COMMITTED vs SERIALIZABLE claims. |
| **Oracle / anchor** | DB isolation documentation |
| **Failure signals** | Uncommitted data visible; double spend. |
| **Evidence** | Two-connection timeline log. |
| **Minimum atomic cases** | DATA-002a dirty read blocked; DATA-002b concurrent update behavior. |

### DATA-003 — Durability after crash

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | After crash/kill mid-write, DB recovers to consistent state (WAL/replica). |
| **Primary techniques** | Kill -9 db app during write (approved env); restart verify. |
| **Scenario focus** | Durability after crash |
| **Variant matrix** | Single node vs clustered failover. |
| **Oracle / anchor** | RPO/RTO runbook |
| **Failure signals** | Corrupt index; partial page write visible. |
| **Evidence** | Checksum/count after recovery. |
| **Minimum atomic cases** | DATA-003a clean recovery; DATA-003b no torn committed row. |

### DATA-004 — Constraint enforcement

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *constraint enforcement* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-004a` happy, `DATA-004b` negative, `DATA-004c` boundary or auth) before PASS |

### DATA-005 — Null default uniqueness

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *null default uniqueness* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-005a` happy, `DATA-005b` negative, `DATA-005c` boundary or auth) before PASS |

### DATA-006 — Precision fidelity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *precision fidelity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-006a` happy, `DATA-006b` negative, `DATA-006c` boundary or auth) before PASS |

### DATA-007 — Timezone round trip

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *timezone round trip* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Locale matrix |
| **Variant matrix** | Pseudo-loc, RTL mirror, DST boundary |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-007a` happy, `DATA-007b` negative, `DATA-007c` boundary or auth) before PASS |

### DATA-008 — Unicode round trip

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unicode round trip* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-008a` happy, `DATA-008b` negative, `DATA-008c` boundary or auth) before PASS |

### DATA-009 — Binary and JSON round trip

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *binary and json round trip* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-009a` happy, `DATA-009b` negative, `DATA-009c` boundary or auth) before PASS |

### DATA-010 — Large object truncation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *large object truncation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-010a` happy, `DATA-010b` negative, `DATA-010c` boundary or auth) before PASS |

### DATA-011 — Concurrent pagination

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *concurrent pagination* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-011a` happy, `DATA-011b` negative, `DATA-011c` boundary or auth) before PASS |

### DATA-012 — Forward migration

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Forward migration applies cleanly on copy of prod volume; rollback plan tested. |
| **Primary techniques** | migrate up on snapshot; row counts; index presence. |
| **Scenario focus** | Forward migration |
| **Variant matrix** | Long migration batched; lock timeout. |
| **Oracle / anchor** | Migration files + release notes |
| **Failure signals** | Data truncation; failed migration half-applied. |
| **Evidence** | schema_migrations version; sample row hash. |
| **Minimum atomic cases** | DATA-012a migrate up; DATA-012b down or forward-only documented. |

### DATA-013 — Interrupted migration

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *interrupted migration* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Data correctness |
| **Variant matrix** | Before/after snapshots, checksums |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-013a` happy, `DATA-013b` negative, `DATA-013c` boundary or auth) before PASS |

### DATA-014 — Version compatibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *version compatibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-014a` happy, `DATA-014b` negative, `DATA-014c` boundary or auth) before PASS |

### DATA-015 — Backup integrity

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Backups complete, encrypted, restorable—not just backup job green. |
| **Primary techniques** | Verify backup artifact exists; checksum; permission. |
| **Scenario focus** | Backup integrity |
| **Variant matrix** | Full vs incremental; cross-region copy. |
| **Oracle / anchor** | Backup policy |
| **Failure signals** | Empty backup file; wrong DB included. |
| **Evidence** | Backup manifest metadata (no secret paths). |
| **Minimum atomic cases** | DATA-015a backup job success evidence; DATA-015b integrity check. |

### DATA-016 — Restore rehearsal

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *restore rehearsal* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-016a` happy, `DATA-016b` negative, `DATA-016c` boundary or auth) before PASS |

### DATA-017 — Import invalid records

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *import invalid records* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-017a` happy, `DATA-017b` negative, `DATA-017c` boundary or auth) before PASS |

### DATA-018 — CSV formula injection

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *csv formula injection* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Injection & encoding |
| **Variant matrix** | Payload catalog (safe), context-aware encoding oracle |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-018a` happy, `DATA-018b` negative, `DATA-018c` boundary or auth) before PASS |

### DATA-019 — Referential cleanup

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *referential cleanup* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-019a` happy, `DATA-019b` negative, `DATA-019c` boundary or auth) before PASS |

### DATA-020 — Soft delete semantics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *soft delete semantics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-020a` happy, `DATA-020b` negative, `DATA-020c` boundary or auth) before PASS |

### DATA-021 — Retention enforcement

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *retention enforcement* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-021a` happy, `DATA-021b` negative, `DATA-021c` boundary or auth) before PASS |

### DATA-022 — Index cache consistency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *index cache consistency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-022a` happy, `DATA-022b` negative, `DATA-022c` boundary or auth) before PASS |

### DATA-023 — Idempotent retries

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *idempotent retries* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Invariant checks, migration dry-run, crash/recovery, referential integrity probes |
| **Scenario focus** | Timing & invariants |
| **Variant matrix** | Parallel workers N=2..5 bounded |
| **Oracle / anchor** | ACID expectations, migration notes, backup/restore runbooks |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `DATA-023a` happy, `DATA-023b` negative, `DATA-023c` boundary or auth) before PASS |

### DATA-024 — Audit trail integrity

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Audit trail append-only, tamper-evident, correlates to actor and request. |
| **Primary techniques** | Perform auditable actions; verify log immutability controls. |
| **Scenario focus** | Audit trail integrity |
| **Variant matrix** | Delete user still retains audit; clock ordering. |
| **Oracle / anchor** | Compliance retention spec |
| **Failure signals** | Mutable audit rows; missing actor on sensitive change. |
| **Evidence** | Audit table query; hash chain if used. |
| **Minimum atomic cases** | DATA-024a event recorded; DATA-024b delete does not remove audit. |

