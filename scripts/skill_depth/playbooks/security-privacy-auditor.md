# Domain playbook — security-privacy-auditor

## Mission

Verify **confidentiality, integrity, availability, and accountability** using **authorized, non-destructive** techniques. Deliver **CONFIRMED** findings with reproduction—not scanner dumps without validation.

**In scope:** AuthN/AuthZ, sessions, input validation, crypto usage, secrets, logging, tenancy, privacy flows, dependencies, transport, headers.

**Out of scope without written approval:** Production attack, DDoS, malware, third-party targets, real credential stuffing, data exfiltration to attacker-controlled hosts.

## P0 scenario set

All **SECU-001 … SECU-024** have **manual overrides** in `scenario-catalog.md` (Tier P0). Execute P0 IDs for any release touching auth, data, APIs, or multi-tenant logic before lower-priority catalog rows.

## Phase 0 — Recon (read-only)

| Output | How |
|--------|-----|
| Route map | OpenAPI, framework routes, front-end API client |
| Auth flows | Login, refresh, SSO, API keys, service accounts |
| Data classes | PII, payment, health, secrets inventory |
| Trust boundaries | Browser, BFF, microservices, DB, cache, queue |

## Phase 1 — STRIDE snapshot

| STRIDE | Questions |
|--------|-----------|
| Spoofing | Impersonation via session, JWT, API key reuse? |
| Tampering | Unsigned webhooks, mass-assignment, weak integrity? |
| Repudiation | Missing audit on admin and data export? |
| Information disclosure | Logs, errors, caches, IDOR, timing? |
| Denial of service | Unbounded queries, uploads, regex? |
| Elevation | Vertical/horizontal authZ breaks? |

## Phase 2 — AuthZ matrix (required if >1 role)

Template:

| Role | Resource | Create | Read | Update | Delete | Notes |
|------|----------|--------|------|--------|--------|-------|
| member | own item | ✓ | ✓ | ✓ | ✓ | baseline |
| member | peer item | ✗ | ✗ | ✗ | ✗ | IDOR tests |

Minimum tests: **SECU-004**, **SECU-005**, **SECU-021** + FUNC/API ownership cases.

## Phase 3 — Injection & encoding

| Class | Surfaces | Safe staging intent |
|-------|----------|---------------------|
| SQLi | Search, sort, filters, reports | Quote, boolean, time (if approved) |
| Command | Export filename, shell wrappers | `;`, `|`, `$()` |
| XSS | Fields rendered in HTML/JS/email | Context-specific markers |
| SSRF | URL import, webhooks, PDF fetch | Internal IP block |
| Traversal | Download, unzip, template path | `../`, zip slip |

Map to **SECU-006 … SECU-013**. Never ship exploit chains to production.

## Phase 4 — Session & tokens

State machine: anonymous → authenticated → elevated → logout/revoke/timeout.

Checklist:

- [ ] New session ID after login (**SECU-002**)
- [ ] Logout invalidates server-side (**SECU-003**)
- [ ] Refresh rotation if OAuth
- [ ] Cookie flags: Secure, HttpOnly, SameSite
- [ ] CSRF on cookie-based mutations (**SECU-009**)

## Phase 5 — Secrets, crypto, transport

- Repo/config scan reasoning (**SECU-014**, **SECU-017**, **SECU-019**)
- Password hash algorithm (**SECU-015**)
- TLS/HSTS/mixed content (**SECU-016**)
- Debug endpoints off in prod-like build (**SECU-020**)

## Phase 6 — Privacy & abuse

- Export/delete/consent (**SECU-024**)
- Rate limits & expensive endpoints (**SECU-001**, **SECU-023**)
- Audit completeness (**SECU-022**)

## OWASP ASVS mapping (report column)

Tag each CONFIRMED finding with ASVS chapter (e.g. V4.1.3). Use **version of ASVS** stated in test plan.

## Evidence rubric

| Tier | Security use |
|------|----------------|
| CONFIRMED | Repro on staging with redacted HTTP/log proof |
| LIKELY | Code path review + plausible attack, not executed |
| RISK | Threat hypothesis, needs env to prove |

## Severity examples

| Sev | Examples |
|-----|----------|
| S0 | RCE, all-user auth bypass, mass PII leak |
| S1 | IDOR on sensitive object, stored XSS in auth area |
| S2 | Missing rate limit with clear abuse, verbose errors |
| S3 | Informational header, defense-in-depth |

## False positives to avoid

- Header checklist without exploit path.
- CVE cited without verifying **your** version/build.
- Different 404 vs 403 labeled IDOR without data leak.

## Pairing

| Skill | When |
|-------|------|
| `api-contract-tester` | Error shape, auth headers, webhooks |
| `logic-concurrency-tester` | TOCTOU, race on limits |
| `data-integrity-tester` | Audit immutability, retention |
| `qa-orchestrator` | Gate ORCH-011 |

## Execution report minimum

Security section must include: AuthZ matrix result summary, P0 SECU table excerpt, injection summary (tested surfaces), open S1+ list, residual risk.
