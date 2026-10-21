# Domain playbook — data-integrity-tester

## Mission

Verify **persistence correctness**: transactions, migrations, backups, referential integrity, and recovery—no silent corruption.

## Invariants

Document per entity:

- Uniqueness constraints.
- Foreign keys and cascade rules.
- Monotonic fields (version, sequence).
- Soft-delete visibility rules.

## Migration testing

1. Snapshot source schema + sample rows.
2. Run migration on clone.
3. Compare row counts, checksums, spot joins.
4. Rollback path if claimed.

## Failure injection

- Kill process mid-transaction (approved env).
- Disk full simulation if feasible.
- Duplicate delivery of messages (idempotency).

## Evidence

SQL queries (redacted), before/after exports, migration logs.

## Pairing

`api-contract-tester` for write APIs; `functional-tester` for user-visible outcomes.
