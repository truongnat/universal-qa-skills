# Domain playbook — logic-concurrency-tester

## Mission

Find **race conditions**, **invalid state transitions**, and **broken invariants** under timing and parallelism.

## Modeling

Draw state machine from code/spec. List **illegal transitions**—each becomes a negative case.

## Concurrency harness (bounded)

- Parallel workers N=2–5 on same resource.
- Double-submit within ms window.
- Reorder async callbacks if test hooks exist.

## Clock & ordering

- TTL expiry, scheduled jobs, leap seconds/DST if time-based logic.
- Out-of-order message delivery for event-driven flows.

## Evidence

Logs with correlation IDs showing interleaving; final DB state vs expected invariant.

## Pairing

`security-privacy-auditor` for TOCTOU on auth; `performance-reliability-tester` under load.
