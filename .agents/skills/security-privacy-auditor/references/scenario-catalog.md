# Scenario catalog — security-privacy-auditor

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** OWASP ASVS 4.0, OWASP Top 10 (2021), CWE, GDPR-style privacy checks where applicable  
**Typical environment:** Isolated staging, synthetic users per role, no real PII; burp/mitm only with scope approval  
**P0 deep specs in this skill:** SECU-001, SECU-002, SECU-003, SECU-004, SECU-005, SECU-006, SECU-007, SECU-008, SECU-009, SECU-010, SECU-011, SECU-012, SECU-013, SECU-014, SECU-015, SECU-016, SECU-017, SECU-018, SECU-019, SECU-020, SECU-021, SECU-022, SECU-023, SECU-024

### SECU-001 — Authentication limits

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Validate account lockout, throttling, and credential-guessing resistance without enabling real user lockout in production. |
| **Primary techniques** | BVA on attempt counters; rate-limit observation; decision table per auth channel (password, OTP, magic link). |
| **Scenario focus** | Brute-force and credential stuffing mitigation |
| **Variant matrix** | N-1, N, N+1 failed attempts; per-IP vs per-account limits; parallel attempts from 2 IPs; reset window expiry; CAPTCHA/step-up trigger if specified. |
| **Oracle / anchor** | ASVS 2.2.x lockout/rate limiting; product security policy doc |
| **Failure signals** | Unlimited attempts; lock applies to wrong principal; user enumeration via different error messages. |
| **Evidence** | Timestamped attempt log (redacted passwords); HTTP 429/423 responses; account state after window. |
| **Minimum atomic cases** | SECU-001a under-threshold OK; SECU-001b at-threshold lock; SECU-001c over-threshold + recovery path. |

**Example atomic breakdown:**
- SECU-001a: 1 invalid login → generic error, no lock
- SECU-001b: At policy max → lock or delay per spec
- SECU-001c: Valid login after lock window or admin unlock

### SECU-002 — Session fixation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Ensure session ID is regenerated after authentication and not accepted pre-login. |
| **Primary techniques** | State transition: anonymous → authenticated; compare Set-Cookie before/after login. |
| **Scenario focus** | Session fixation |
| **Variant matrix** | Attacker-supplied cookie before login; login as victim; verify new session invalidates attacker token. |
| **Oracle / anchor** | ASVS 3.2 session binding |
| **Failure signals** | Pre-auth session ID still valid post-login; predictable session IDs. |
| **Evidence** | Cookie values (truncated), sequence diagram, two-browser repro. |
| **Minimum atomic cases** | SECU-002a fixation attempt fails; SECU-002b normal login rotates ID. |

**Example atomic breakdown:**
- SECU-002a: Plant session A, victim logs in, attacker A unusable
- SECU-002b: Fresh login issues new ID

### SECU-003 — Session revocation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Verify logout, admin revoke, password change, and idle timeout invalidate server-side session. |
| **Primary techniques** | State transition; replay old session cookie/token after revoke. |
| **Scenario focus** | Session revocation |
| **Variant matrix** | Logout; change password; admin disable user; idle timeout; refresh token rotation if OAuth. |
| **Oracle / anchor** | ASVS 3.3 logout and token invalidation |
| **Failure signals** | Old JWT/cookie still returns 200 on protected routes. |
| **Evidence** | API calls with stale token after each revoke action. |
| **Minimum atomic cases** | SECU-003a logout; SECU-003b password change; SECU-003c idle timeout (or NOT TESTED with reason). |

### SECU-004 — Object authorization

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove object-level authorization: subject may only access objects they own or are granted. |
| **Primary techniques** | AuthZ matrix; horizontal IDOR grid (User A × User B resources). |
| **Scenario focus** | Broken object-level authorization (BOLA/IDOR) |
| **Variant matrix** | Sequential IDs, UUIDs, encoded IDs; HTTP method swap GET/PUT/DELETE; nested routes /orgs/{o}/items/{i}. |
| **Oracle / anchor** | ASVS 4.1; OWASP API1:2023 |
| **Failure signals** | 200/204 with foreign object body; metadata leak in 404 vs 403. |
| **Evidence** | Two-session curl matrix table; response body hash compare. |
| **Minimum atomic cases** | SECU-004a own object OK; SECU-004b peer object denied; SECU-004c admin bypass only if role intended. |

### SECU-005 — Privilege escalation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Detect vertical privilege escalation (member→admin) via UI, API, or hidden parameters. |
| **Primary techniques** | Role matrix; forced browsing to admin routes; mass-assignment on role fields. |
| **Scenario focus** | Privilege escalation |
| **Variant matrix** | JWT role claim tamper (if unsigned client-side only); `isAdmin=true` in JSON body; direct /admin API. |
| **Oracle / anchor** | ASVS 4.2 function-level authorization |
| **Failure signals** | Low role executes admin-only mutation. |
| **Evidence** | Request/response per role; audit log role recorded. |
| **Minimum atomic cases** | SECU-005a member blocked; SECU-005b admin allowed; SECU-005c tampered token rejected. |

### SECU-006 — SQL injection

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Confirm parameterized queries/ORM binding for SQL injection on every query-backed input. |
| **Primary techniques** | Injection suite: quote, boolean, time-based (staging only), UNION probe on search/filter/sort. |
| **Scenario focus** | SQL injection |
| **Variant matrix** | URL params, JSON body, headers (e.g. X-Forwarded-For if logged), ORDER BY, LIKE wildcards. |
| **Oracle / anchor** | ASVS 5.3; CWE-89 |
| **Failure signals** | SQL error in response; timing delta; unauthorized rows returned. |
| **Evidence** | Payload list (safe), response diff, DB query log if available. |
| **Minimum atomic cases** | SECU-006a benign quote escaped; SECU-006b boolean blind; SECU-006c error-based (no stack trace to client). |

### SECU-007 — Command injection

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prevent OS/shell invocation from untrusted input in file paths, filenames, diagnostics, exports. |
| **Primary techniques** | Command injection metacharacters in fields passed to exec, shell, ImageMagick, ffmpeg wrappers. |
| **Scenario focus** | Command injection |
| **Variant matrix** | `;|&$()`, newline, backtick in upload name, report export filename, git hook params. |
| **Oracle / anchor** | ASVS 5.3.4; CWE-78 |
| **Failure signals** | Delayed response, DNS callback in approved canary, unexpected file created. |
| **Evidence** | Controlled payload, process list snapshot (staging). |
| **Minimum atomic cases** | SECU-007a rejected input; SECU-007b safe filename allowed. |

### SECU-008 — Output escaping

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Ensure contextual output encoding for HTML, JS, URL, CSS contexts (XSS prevention). |
| **Primary techniques** | Stored/reflected XSS probes; DOM XSS via client routes; CSP review as supplement. |
| **Scenario focus** | Output escaping / XSS |
| **Variant matrix** | <script>, event handlers, javascript: URLs, SVG, template injection in emails/PDF if applicable. |
| **Oracle / anchor** | ASVS 5.3; OWASP XSS cheat sheet |
| **Failure signals** | Unescaped user input executes in browser; HTML injection in emails. |
| **Evidence** | Screenshot + DOM; Content-Type; CSP header. |
| **Minimum atomic cases** | SECU-008a reflected; SECU-008b stored; SECU-008c encoded output safe. |

### SECU-009 — Cross-site request forgery

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Validate anti-CSRF for cookie-session state-changing requests. |
| **Primary techniques** | Cross-origin form POST; fetch with/without custom header; SameSite cookie behavior. |
| **Scenario focus** | CSRF |
| **Variant matrix** | POST/PUT/DELETE; JSON vs form; login CSRF if applicable. |
| **Oracle / anchor** | ASVS 3.5 CSRF |
| **Failure signals** | State change succeeds from attacker origin without token. |
| **Evidence** | HTML PoC page (staging), request lacking token blocked. |
| **Minimum atomic cases** | SECU-009a missing token → 403; SECU-009b valid token → success. |

### SECU-010 — Server-side request forgery

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Block server-side fetch to internal/metadata URLs (SSRF). |
| **Primary techniques** | URL parser bypass: localhost, 169.254.169.254, file://, redirect chains, DNS rebinding note. |
| **Scenario focus** | SSRF |
| **Variant matrix** | Webhook URL field, PDF renderer, import-from-URL, avatar URL. |
| **Oracle / anchor** | ASVS 5.2.6; OWASP API7 |
| **Failure signals** | Internal IP response body; cloud metadata in response. |
| **Evidence** | Collaborator/out-of-band URL hit log (approved tool). |
| **Minimum atomic cases** | SECU-010a block internal; SECU-010b allow public HTTPS if policy says so. |

### SECU-011 — Path traversal

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prevent path traversal in download, upload, archive extract, static file serve. |
| **Primary techniques** | ../, ..\, URL-encoded, Unicode normalization, zip slip. |
| **Scenario focus** | Path traversal |
| **Variant matrix** | Download?file=; S3 key; template path; log download. |
| **Oracle / anchor** | ASVS 5.2.4; CWE-22 |
| **Failure signals** | /etc/passwd or web.config contents in response. |
| **Evidence** | Requested path vs resolved path log. |
| **Minimum atomic cases** | SECU-011a traversal blocked; SECU-011b valid file served. |

### SECU-012 — Unsafe deserialization

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Reject untrusted deserialization and unsafe object graphs. |
| **Primary techniques** | Malformed serialized payloads; type confusion in JSON→object if language-specific. |
| **Scenario focus** | Unsafe deserialization |
| **Variant matrix** | Java ObjectInputStream, pickle, YAML load, .NET BinaryFormatter if stack known. |
| **Oracle / anchor** | ASVS 5.5; CWE-502 |
| **Failure signals** | RCE gadget chain; unexpected object instantiation. |
| **Evidence** | Payload hash, error type, no execution in staging canary. |
| **Minimum atomic cases** | SECU-012a reject untrusted blob; SECU-012b safe JSON schema path. |

### SECU-013 — Untrusted file upload

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Validate file upload: type, size, content, storage path, and execution risk. |
| **Primary techniques** | MIME vs extension mismatch; polyglot; AV scan if claimed; download Content-Disposition. |
| **Scenario focus** | Untrusted file upload |
| **Variant matrix** | Double extension, null byte (legacy), SVG script, zip bomb size limit. |
| **Oracle / anchor** | ASVS 5.2.3 |
| **Failure signals** | Uploaded script served as executable; oversized DoS. |
| **Evidence** | Stored object headers, served URL, scan log. |
| **Minimum atomic cases** | SECU-013a reject executable; SECU-013b accept allowed type. |

### SECU-014 — Secrets in logs

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Ensure secrets, tokens, PII not written to logs, metrics, traces, client errors. |
| **Primary techniques** | Trigger errors and auth flows; grep log sinks; sample APM spans. |
| **Scenario focus** | Secrets in logs |
| **Variant matrix** | Password field, Authorization header, reset token, credit card if in scope. |
| **Oracle / anchor** | ASVS 7.1 log protection |
| **Failure signals** | Bearer token in access log line; stack trace with connection string. |
| **Evidence** | Redacted log excerpts; logging config review. |
| **Minimum atomic cases** | SECU-014a error path; SECU-014b successful login log. |

### SECU-015 — Credential storage

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Verify password storage uses adaptive hashing; API keys stored hashed or in vault. |
| **Primary techniques** | Static review of hash algorithm; registration flow DB field format (staging). |
| **Scenario focus** | Credential storage |
| **Variant matrix** | Reset token single-use; API key rotation; no plaintext in DB export sample. |
| **Oracle / anchor** | ASVS 2.4 credential storage |
| **Failure signals** | MD5/SHA1 password; reversible encryption without need. |
| **Evidence** | Hash prefix $argon2/$2b$; schema migration notes. |
| **Minimum atomic cases** | SECU-015a hash format; SECU-015b reset token entropy. |

### SECU-016 — Transport validation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Enforce TLS for sensitive channels; validate cert chain in clients; HSTS where web. |
| **Primary techniques** | Protocol downgrade check; mixed content; certificate pinning doc vs impl. |
| **Scenario focus** | Transport validation |
| **Variant matrix** | TLS1.0 off; weak ciphers; SSL stripping mitigations. |
| **Oracle / anchor** | ASVS 9.1 transport |
| **Failure signals** | Sensitive cookie without Secure; login over HTTP allowed. |
| **Evidence** | sslyze/testssl summary (staging host). |
| **Minimum atomic cases** | SECU-016a HTTPS redirect; SECU-016b HSTS header if claimed. |

### SECU-017 — Crypto key lifecycle

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Validate key generation, rotation, separation of dev/prod keys, KMS usage. |
| **Primary techniques** | Config review; JWT alg none/HS256 with public secret; key in repo scan. |
| **Scenario focus** | Crypto key lifecycle |
| **Variant matrix** | Rotate JWT signing key; encrypted fields; envelope encryption. |
| **Oracle / anchor** | ASVS 6.2 key management |
| **Failure signals** | Hardcoded AES key; shared prod key in repo. |
| **Evidence** | KMS ARN references; no raw keys in env samples. |
| **Minimum atomic cases** | SECU-017a no secrets in git; SECU-017b rotation doc matches practice. |

### SECU-018 — Sensitive temporary files

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Ensure temp files with sensitive data are removed and not world-readable. |
| **Primary techniques** | Export/download flows; crash mid-export; shared /tmp patterns. |
| **Scenario focus** | Sensitive temporary files |
| **Variant matrix** | PDF gen, CSV export, crash during write. |
| **Oracle / anchor** | ASVS 8.2 sensitive data handling |
| **Failure signals** | Predictable temp URL; file remains after session end. |
| **Evidence** | Filesystem listing (staging); cleanup job logs. |
| **Minimum atomic cases** | SECU-018a temp cleaned; SECU-018b permissions restricted. |

### SECU-019 — Dependency provenance

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Verify dependency lockfiles, SBOM availability, and process for known CVE triage. |
| **Primary techniques** | npm audit/osv-scanner output interpreted (not invented); pin vs range policy. |
| **Scenario focus** | Dependency provenance |
| **Variant matrix** | Transitive vuln; unmaintained package; typosquat check on install scripts. |
| **Oracle / anchor** | ASVS 14.2 dependency |
| **Failure signals** | Critical CVE in shipped dep without waiver doc. |
| **Evidence** | Scanner output version, package lock entry, waiver ticket ID. |
| **Minimum atomic cases** | SECU-019a scan run; SECU-019b critical item disposition documented. |

### SECU-020 — Insecure debug settings

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Confirm debug/admin interfaces disabled or strongly protected in production builds. |
| **Primary techniques** | Probe /debug, stack traces, verbose errors, default creds, GraphQL introspection. |
| **Scenario focus** | Insecure debug settings |
| **Variant matrix** | ENV=production build; feature flags; Django DEBUG, Spring actuators. |
| **Oracle / anchor** | ASVS 14.x production config |
| **Failure signals** | Full stack trace to user; actuator /env open. |
| **Evidence** | Build flags, response body on forced 500. |
| **Minimum atomic cases** | SECU-020a no debug stack; SECU-020b actuator auth required. |

### SECU-021 — Tenant isolation

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Validate strict tenant isolation in data layer, cache, search index, and background jobs. |
| **Primary techniques** | Two-tenant parallel tests; cross-tenant ID in URL; shared cache key inspection. |
| **Scenario focus** | Tenant isolation |
| **Variant matrix** | Subdomain, header X-Tenant-ID, RLS policies, queue message routing. |
| **Oracle / anchor** | ASVS 4.1 multi-tenant |
| **Failure signals** | Tenant B data in Tenant A search results. |
| **Evidence** | Cross-tenant access matrix; DB RLS policy excerpt. |
| **Minimum atomic cases** | SECU-021a same-tenant OK; SECU-021b cross-tenant fail; SECU-021c cache isolation. |

### SECU-022 — Audit logging

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Security events logged: auth success/fail, admin actions, permission denials, data export. |
| **Primary techniques** | Trigger each event; verify immutable audit trail fields (who, what, when, where). |
| **Scenario focus** | Audit logging |
| **Variant matrix** | Clock skew; tamper attempt; log injection in username field. |
| **Oracle / anchor** | ASVS 7.2 security logging |
| **Failure signals** | Missing deny events; PII in audit log. |
| **Evidence** | SIEM query result; log line samples redacted. |
| **Minimum atomic cases** | SECU-022a failed login logged; SECU-022b admin change logged. |

### SECU-023 — Resource exhaustion

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Identify unbounded expensive operations (regex, PDF gen, report, graph query) abusable for DoS. |
| **Primary techniques** | Rate limits; payload size; concurrency caps; slowloris note for infra team. |
| **Scenario focus** | Resource exhaustion |
| **Variant matrix** | Large JSON array; ReDoS pattern; batch API size. |
| **Oracle / anchor** | ASVS 13.2 API abuse |
| **Failure signals** | Single request pegs CPU; no 413/429. |
| **Evidence** | Latency/CPU before-after; limit headers. |
| **Minimum atomic cases** | SECU-023a over limit rejected; SECU-023b under limit OK. |

### SECU-024 — Deletion and consent

**Tier:** P0 manual override (high-risk catalog)

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Verify data subject deletion/export and consent flags match privacy policy. |
| **Primary techniques** | End-to-end delete propagation; export completeness; opt-out honored in marketing/send APIs. |
| **Scenario focus** | Deletion and consent |
| **Variant matrix** | Delete then login; export after delete; consent withdraw mid-campaign. |
| **Oracle / anchor** | GDPR Arts. 17/20 style controls (jurisdiction-dependent) |
| **Failure signals** | Ghost records in analytics; email after opt-out. |
| **Evidence** | DB row count; third-party integration mock callback. |
| **Minimum atomic cases** | SECU-024a export complete; SECU-024b delete blocks access; SECU-024c consent off stops action. |

