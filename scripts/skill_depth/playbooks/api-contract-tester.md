# Domain playbook — api-contract-tester

## Mission

Prove APIs **match contracts** and **HTTP semantics** for consumers—schema, errors, auth, pagination, idempotency, evolution, webhooks.

## P0 scenario set

**API-004, 005, 006, 008, 011, 012, 016, 020, 021, 023** — full override text in `scenario-catalog.md`. Required for any public or partner API change.

## Contract inventory

| Artifact | Version | Owner |
|----------|---------|-------|
| OpenAPI / GraphQL SDL | | |
| Postman/consumer tests | | |
| Error catalog | | |
| Deprecation policy | | |

## Per-endpoint worksheet

For each operationId:

| Check | Pass criterion |
|-------|----------------|
| Request schema | Validator rejects unknown required violations |
| Response schema | 2xx matches; enums stable |
| Status codes | Match spec + RFC 7231 |
| Auth | Scheme per securitySchemes |
| AuthZ | **API-006** matrix row |
| Errors | **API-004** envelope |
| Pagination | **API-008** if list |
| Idempotency | **API-011** if documented |

## HTTP semantics quick reference

| Situation | Expected |
|-----------|----------|
| Validation | 400 or 422 (per spec), not 500 |
| Not authenticated | 401 |
| Authenticated, forbidden | 403 |
| Missing resource | 404 (policy on existence leak) |
| Conflict | 409 |
| Precondition failed | 412 |

## Negative protocol suite

- Malformed JSON, wrong Content-Type.
- Missing required headers (Accept, API-Version).
- Oversized body (**API-017**).
- Unicode in paths and bodies (**API-018**).

## Versioning & compatibility (**API-016**)

- Run **old client** scenarios against new server (record version pair).
- Deprecated fields: still present with sunset header?
- Breaking change requires version bump per policy.

## Webhooks

| Test | ID |
|------|-----|
| Valid signature | API-020 |
| Tamper reject | API-020 |
| Duplicate event_id | API-021 |
| Schema version | API-022 |

## Batch & partial failure (**API-023**)

Document whether API is all-or-nothing or per-item errors. Verify DB matches documented semantics.

## Caching & privacy (**API-024**)

- `Cache-Control` on sensitive GETs.
- No auth token in URL.
- CDN cache key excludes private data.

## Tools (examples)

- Schema: openapi-diff, graphql-inspector.
- Runtime: curl/httpie + jsonschema validation.
- Contract tests: existing CI job output (cite job URL/id).

## Evidence table (required)

| Test ID | Method | Path | Status | Schema valid | Notes |
|---------|--------|------|--------|--------------|-------|

## False positives

- 200 with `{success:false}` counted as PASS.
- Ignoring optional fields that break strict clients.

## Pairing

| Skill | When |
|-------|------|
| `security-privacy-auditor` | API-005/006 depth, SSRF in callbacks |
| `performance-reliability-tester` | API-013/014 timeouts |
| `data-integrity-tester` | Transactional batch semantics |

## Report minimum

P0 API summary, endpoint coverage %, breaking-change assessment, webhook tests, blocked env list.
