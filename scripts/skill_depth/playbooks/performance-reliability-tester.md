# Domain playbook — performance-reliability-tester

## Mission

Measure **time behavior**, **resource use**, and **failure handling** against documented SLOs—never guess timings.

## Preconditions

- Approved load target (staging).
- Metrics source (APM, logs, k6/Gatling output).
- Baseline from last good release if available.

## Test types

| Type | When | Stop conditions |
|------|------|-----------------|
| Smoke load | Every RC | Error rate < threshold |
| Stress | Major release | Find breaking point in staging |
| Soak | Long-running services | Memory leak over N hours |
| Failover | HA claims | Kill node; verify recovery |

## Reliability

- Retry storms, circuit breakers, timeout cascades.
- Graceful degradation messages to users.
- Queue backlog behavior.

## Evidence

Tables: p50/p95/p99, error %, CPU/mem, test duration, tool version. BLOCKED if no metrics access.

## Pairing

`logic-concurrency-tester` for race under load; `qa-orchestrator` for gate ORCH-013.
