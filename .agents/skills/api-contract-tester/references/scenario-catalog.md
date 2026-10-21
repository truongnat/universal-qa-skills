# Scenario catalog — api-contract-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP  
**Typical environment:** Mock downstreams or recorded fixtures; versioned API base URL  
**P0 deep specs in this skill:** API-004, API-005, API-006, API-008, API-011, API-012, API-016, API-020, API-021, API-023

### API-001 — Required schema fields

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *required schema fields* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-001a` happy, `API-001b` negative, `API-001c` boundary or auth) before PASS |

### API-002 — Unknown schema fields

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unknown schema fields* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-002a` happy, `API-002b` negative, `API-002c` boundary or auth) before PASS |

### API-003 — Null semantics

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *null semantics* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-003a` happy, `API-003b` negative, `API-003c` boundary or auth) before PASS |

### API-004 — Status and error envelope

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Error responses use stable envelope (code, message, details[]) and correct HTTP status. |
| **Primary techniques** | Negative cases per endpoint; schema validate error body. |
| **Scenario focus** | Status and error envelope |
| **Variant matrix** | 400 vs 422; 401 vs 403; 500 never for validation; problem+json if RFC7807. |
| **Oracle / anchor** | OpenAPI error schema + RFC 7231 |
| **Failure signals** | Stack trace in body; inconsistent codes across endpoints. |
| **Evidence** | Collection of error JSON samples. |
| **Minimum atomic cases** | API-004a validation error shape; API-004b auth error shape. |

### API-005 — Authentication failure

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Authentication failures never grant partial data or ambiguous success. |
| **Primary techniques** | Missing token, expired, wrong scheme, malformed JWT. |
| **Scenario focus** | Authentication failure |
| **Variant matrix** | Bearer, cookie, API key header; clock skew on JWT. |
| **Oracle / anchor** | OpenAPI securitySchemes |
| **Failure signals** | 200 with empty list on bad auth; different body leaks user existence. |
| **Evidence** | 401/403 responses redacted. |
| **Minimum atomic cases** | API-005a no auth; API-005b bad token; API-005c expired. |

### API-006 — Authorization ownership

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Contract-level ownership: resource IDs in path/body cannot access other principals' data. |
| **Primary techniques** | Pairwise token A + resource B tests on all CRUD. |
| **Scenario focus** | Authorization ownership |
| **Variant matrix** | Nested resources; batch endpoints; GraphQL aliases. |
| **Oracle / anchor** | OpenAPI + authz matrix |
| **Failure signals** | 200 on foreign ID; inconsistent 404/403. |
| **Evidence** | Auth matrix table in report. |
| **Minimum atomic cases** | API-006a own resource; API-006b foreign denied. |

### API-007 — Content negotiation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *content negotiation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-007a` happy, `API-007b` negative, `API-007c` boundary or auth) before PASS |

### API-008 — Pagination cursor

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Cursor/limit pagination stable under inserts/deletes; no skipped/duplicate rows. |
| **Primary techniques** | Walk all pages; mutate data between pages; empty last page. |
| **Scenario focus** | Pagination cursor |
| **Variant matrix** | limit=1; max limit; invalid cursor; sort tie-breaker. |
| **Oracle / anchor** | Pagination section of API guide |
| **Failure signals** | Duplicate items across pages; cursor never ends. |
| **Evidence** | Ordered ID list merged from pages. |
| **Minimum atomic cases** | API-008a full walk; API-008b invalid cursor 400. |

### API-009 — Stable ordering

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *stable ordering* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-009a` happy, `API-009b` negative, `API-009c` boundary or auth) before PASS |

### API-010 — Filter escaping

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *filter escaping* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-010a` happy, `API-010b` negative, `API-010c` boundary or auth) before PASS |

### API-011 — Idempotency keys

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Idempotency-Key header prevents duplicate side effects on retry. |
| **Primary techniques** | Duplicate POST with same key; different body same key; key expiry. |
| **Scenario focus** | Idempotency keys |
| **Variant matrix** | Network timeout retry simulation; parallel duplicate requests. |
| **Oracle / anchor** | Idempotency contract in OpenAPI |
| **Failure signals** | Double charge/double row; 500 on replay instead of cached 201. |
| **Evidence** | Two identical requests; single resource count. |
| **Minimum atomic cases** | API-011a replay same response; API-011b new key new resource. |

### API-012 — Conditional updates

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | ETag/If-Match or version field enforces conditional updates. |
| **Primary techniques** | PUT with stale version → 409/412. |
| **Scenario focus** | Conditional updates |
| **Variant matrix** | PATCH partial; delete If-Match. |
| **Oracle / anchor** | HTTP conditional request docs |
| **Failure signals** | Stale update applied silently. |
| **Evidence** | Sequence of version numbers. |
| **Minimum atomic cases** | API-012a match succeeds; API-012b stale fails. |

### API-013 — Rate limits

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rate limits* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-013a` happy, `API-013b` negative, `API-013c` boundary or auth) before PASS |

### API-014 — Timeout

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *timeout* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-014a` happy, `API-014b` negative, `API-014c` boundary or auth) before PASS |

### API-015 — Cancellation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cancellation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-015a` happy, `API-015b` negative, `API-015c` boundary or auth) before PASS |

### API-016 — Compatibility evolution

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Backward/forward compatibility: deprecated fields, version headers, sunset dates. |
| **Primary techniques** | Schema diff between v1/v2; consumer old client against new server. |
| **Scenario focus** | Compatibility evolution |
| **Variant matrix** | Optional new fields ignored by old client; breaking change flagged. |
| **Oracle / anchor** | API changelog + deprecation policy |
| **Failure signals** | Required field added without version bump. |
| **Evidence** | Contract test output; changelog link. |
| **Minimum atomic cases** | API-016a v1 client on v2 server; API-016b deprecated header present. |

### API-017 — Payload size limits

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *payload size limits* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-017a` happy, `API-017b` negative, `API-017c` boundary or auth) before PASS |

### API-018 — Unicode and encoding

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *unicode and encoding* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-018a` happy, `API-018b` negative, `API-018c` boundary or auth) before PASS |

### API-019 — Streaming uploads

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *streaming uploads* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-019a` happy, `API-019b` negative, `API-019c` boundary or auth) before PASS |

### API-020 — Webhook signatures

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Webhook HMAC/signature validated; timestamp tolerance prevents replay. |
| **Primary techniques** | Sign payload with wrong secret; mutate body; replay old timestamp. |
| **Scenario focus** | Webhook signatures |
| **Variant matrix** | sha256 vs sha1; multiple signatures; encoding edge cases. |
| **Oracle / anchor** | Webhook security doc |
| **Failure signals** | Unsigned delivery accepted; replay within window succeeds. |
| **Evidence** | Receiver log accept/reject. |
| **Minimum atomic cases** | API-020a valid sig; API-020b tamper reject. |

### API-021 — Webhook replay

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Webhook delivery idempotency and event ID deduplication. |
| **Primary techniques** | Send same event_id twice; out-of-order delivery. |
| **Scenario focus** | Webhook replay |
| **Variant matrix** | Retry after 500; at-least-once semantics. |
| **Oracle / anchor** | Event catalog spec |
| **Failure signals** | Duplicate side effects on replay. |
| **Evidence** | Handler invocation count. |
| **Minimum atomic cases** | API-021a duplicate event ignored; API-021b new event processed. |

### API-022 — Event schema compatibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *event schema compatibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Contract conformance |
| **Variant matrix** | Schema validation, error shape, versioning |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-022a` happy, `API-022b` negative, `API-022c` boundary or auth) before PASS |

### API-023 — Batch partial failure

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Batch APIs report per-item status; partial failure does not commit unintended subset. |
| **Primary techniques** | Batch with mixed valid/invalid items; transactional boundary check. |
| **Scenario focus** | Batch partial failure |
| **Variant matrix** | All-or-nothing vs item-level error array. |
| **Oracle / anchor** | Batch endpoint OpenAPI |
| **Failure signals** | Silent skip; whole batch 500. |
| **Evidence** | Response items[] status; DB state per item. |
| **Minimum atomic cases** | API-023a partial errors returned; API-023b valid items committed per spec. |

### API-024 — Cache privacy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cache privacy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Schema diff, contract tests, negative protocol cases, idempotency keys, pagination invariants |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | OpenAPI/AsyncAPI/GraphQL schema, consumer contracts, RFC semantics for HTTP |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `API-024a` happy, `API-024b` negative, `API-024c` boundary or auth) before PASS |

