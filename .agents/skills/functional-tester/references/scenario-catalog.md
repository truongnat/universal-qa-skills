# Scenario catalog — functional-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Acceptance criteria, domain invariants, ISO 25010 functional suitability  
**Typical environment:** Seed data per persona; capture DB/API state for oracles  
**P0 deep specs in this skill:** FUNC-003, FUNC-006, FUNC-008, FUNC-009, FUNC-010, FUNC-019, FUNC-020, FUNC-021, FUNC-023, FUNC-024

### FUNC-001 — First run and onboarding

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *first run and onboarding* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-001a` happy, `FUNC-001b` negative, `FUNC-001c` boundary or auth) before PASS |

### FUNC-002 — Create valid entity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *create valid entity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-002a` happy, `FUNC-002b` negative, `FUNC-002c` boundary or auth) before PASS |

### FUNC-003 — Create invalid entity

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Invalid create payloads must fail with correct validation, no partial persist, clear user-safe errors. |
| **Primary techniques** | Equivalence classes per field; decision table for cross-field rules. |
| **Scenario focus** | Create invalid entity |
| **Variant matrix** | Missing required; wrong type; business rule violation; max length+1; forbidden enum. |
| **Oracle / anchor** | AC + API schema + domain rules |
| **Failure signals** | 500 instead of 4xx; partial row in DB; misleading success toast. |
| **Evidence** | API 4xx body; DB count unchanged; UI error text. |
| **Minimum atomic cases** | FUNC-003a single-field; FUNC-003b multi-field; FUNC-003c server-side only rule. |

### FUNC-004 — Duplicate record handling

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *duplicate record handling* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-004a` happy, `FUNC-004b` negative, `FUNC-004c` boundary or auth) before PASS |

### FUNC-005 — Read missing record

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *read missing record* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-005a` happy, `FUNC-005b` negative, `FUNC-005c` boundary or auth) before PASS |

### FUNC-006 — Read unauthorized record

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Unauthorized read must not leak existence via body, timing, or error text. |
| **Primary techniques** | Two-user IDOR matrix on read endpoints and UI deep links. |
| **Scenario focus** | Read unauthorized record |
| **Variant matrix** | 403 vs 404 policy; list vs detail; GraphQL node access. |
| **Oracle / anchor** | Security policy + AC |
| **Failure signals** | Foreign record fields visible; enumerable IDs. |
| **Evidence** | Two-session comparison table. |
| **Minimum atomic cases** | FUNC-006a owner read OK; FUNC-006b peer denied; FUNC-006c admin override if specified. |

### FUNC-007 — Update valid record

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *update valid record* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-007a` happy, `FUNC-007b` negative, `FUNC-007c` boundary or auth) before PASS |

### FUNC-008 — Update conflict

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Concurrent or stale updates handled per spec (409, ETag, version column). |
| **Primary techniques** | State transition; dual-browser edit race. |
| **Scenario focus** | Update conflict |
| **Variant matrix** | Lost update; merge UI; optimistic locking. |
| **Oracle / anchor** | API If-Match / version field docs |
| **Failure signals** | Last write silent loss; corrupt merged state. |
| **Evidence** | Two parallel PUT sequences; final DB state. |
| **Minimum atomic cases** | FUNC-008a second writer gets 409; FUNC-008b refresh resolves. |

### FUNC-009 — Delete confirmation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Destructive delete requires confirmation and matches retention/soft-delete rules. |
| **Primary techniques** | Use case; UI flow; undo window if promised. |
| **Scenario focus** | Delete confirmation |
| **Variant matrix** | Cancel confirm; keyboard shortcut; bulk delete subset. |
| **Oracle / anchor** | UX copy + data retention policy |
| **Failure signals** | One-click delete; no audit entry. |
| **Evidence** | Recording; audit log entry. |
| **Minimum atomic cases** | FUNC-009a confirm required; FUNC-009b cancel preserves data. |

### FUNC-010 — Delete recovery

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Recovery from delete (undo, trash, restore API) within documented window. |
| **Primary techniques** | State transition trash→restored. |
| **Scenario focus** | Delete recovery |
| **Variant matrix** | Restore after 1 min; expire after 30 days (or NOT TESTED). |
| **Oracle / anchor** | Product trash/retention spec |
| **Failure signals** | Restore missing relations; partial restore. |
| **Evidence** | Before/after entity graph. |
| **Minimum atomic cases** | FUNC-010a restore happy; FUNC-010b expired not restorable. |

### FUNC-011 — Search exact case

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *search exact case* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-011a` happy, `FUNC-011b` negative, `FUNC-011c` boundary or auth) before PASS |

### FUNC-012 — Search Unicode

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *search unicode* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-012a` happy, `FUNC-012b` negative, `FUNC-012c` boundary or auth) before PASS |

### FUNC-013 — Filter combinations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *filter combinations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-013a` happy, `FUNC-013b` negative, `FUNC-013c` boundary or auth) before PASS |

### FUNC-014 — Sorting stability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *sorting stability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-014a` happy, `FUNC-014b` negative, `FUNC-014c` boundary or auth) before PASS |

### FUNC-015 — Pagination boundaries

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *pagination boundaries* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-015a` happy, `FUNC-015b` negative, `FUNC-015c` boundary or auth) before PASS |

### FUNC-016 — Bulk actions

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *bulk actions* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-016a` happy, `FUNC-016b` negative, `FUNC-016c` boundary or auth) before PASS |

### FUNC-017 — Import malformed rows

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *import malformed rows* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-017a` happy, `FUNC-017b` negative, `FUNC-017c` boundary or auth) before PASS |

### FUNC-018 — Export fidelity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *export fidelity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-018a` happy, `FUNC-018b` negative, `FUNC-018c` boundary or auth) before PASS |

### FUNC-019 — Unsaved state protection

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Navigate away or close with unsaved edits prompts save/discard per spec. |
| **Primary techniques** | Interrupt testing; browser beforeunload. |
| **Scenario focus** | Unsaved state protection |
| **Variant matrix** | Back button; tab close; session timeout with draft. |
| **Oracle / anchor** | UX spec / AC |
| **Failure signals** | Silent data loss; autosave not mentioned but expected. |
| **Evidence** | Step repro; localStorage snapshot. |
| **Minimum atomic cases** | FUNC-019a prompt shown; FUNC-019b discard loses edits; FUNC-019c save persists. |

### FUNC-020 — Session expiry

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Session expiry redirects to login; return URL; no data leak on shared machine. |
| **Primary techniques** | TTL manipulation (staging); idle vs absolute timeout. |
| **Scenario focus** | Session expiry |
| **Variant matrix** | API 401 sync with UI; remember-me behavior. |
| **Oracle / anchor** | Session policy doc |
| **Failure signals** | Stale UI shows cached PII; API still works after expiry. |
| **Evidence** | Cookie exp; API after idle. |
| **Minimum atomic cases** | FUNC-020a idle logout; FUNC-020b re-auth resumes task. |

### FUNC-021 — Offline to online recovery

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Offline queue, sync, and conflict resolution when connectivity returns. |
| **Primary techniques** | Network throttling; airplane mode simulation. |
| **Scenario focus** | Offline to online recovery |
| **Variant matrix** | Duplicate submit on reconnect; server wins vs client wins. |
| **Oracle / anchor** | Offline/sync design doc |
| **Failure signals** | Lost actions; duplicate orders. |
| **Evidence** | Client queue state; server idempotency keys. |
| **Minimum atomic cases** | FUNC-021a queue while offline; FUNC-021b sync success; FUNC-021c conflict UI. |

### FUNC-022 — Background cancellation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *background cancellation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Use cases, decision tables, state transition for workflows, BVA/EP on fields, pairwise on filters |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Acceptance criteria, domain invariants, ISO 25010 functional suitability |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `FUNC-022a` happy, `FUNC-022b` negative, `FUNC-022c` boundary or auth) before PASS |

### FUNC-023 — Restart persistence

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | User data and in-progress work survive app/process restart as specified. |
| **Primary techniques** | Kill app mid-flow; restart service; persistence checks. |
| **Scenario focus** | Restart persistence |
| **Variant matrix** | Mobile background kill; browser refresh; server pod restart. |
| **Oracle / anchor** | Persistence AC |
| **Failure signals** | Cart cleared; draft lost without warning. |
| **Evidence** | State before/after restart. |
| **Minimum atomic cases** | FUNC-023a saved data remains; FUNC-023b unsaved not promised persists. |

### FUNC-024 — Multi-user collaboration

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Multi-user collaboration: presence, locks, notifications, no cross-user corruption. |
| **Primary techniques** | Two sessions real-time; concurrent edit same record. |
| **Scenario focus** | Multi-user collaboration |
| **Variant matrix** | Edit lock; comment thread; assignee change. |
| **Oracle / anchor** | Collaboration feature spec |
| **Failure signals** | Overwrites without notice; stale view infinite. |
| **Evidence** | Dual browser recording; websocket events. |
| **Minimum atomic cases** | FUNC-024a user B sees A's save; FUNC-024b conflict handled. |

