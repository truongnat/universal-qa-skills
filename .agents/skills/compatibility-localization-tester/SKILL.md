---
name: compatibility-localization-tester
description: "Platform matrix, locale, and internationalization checks. Deep playbooks and per-scenario specs in references/. Use for compatibility and i18n/l10n. Structured markdown reports required."
---

# compatibility-localization-tester

**Purpose:** Supported matrix and internationalization. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Supported matrix doc, CLDR/locale rules, store policies

## Operating procedure

| Step | Action |
|------|--------|
| 1 | Intake scope, change diff, environments, and data classification |
| 2 | Build risk table (impact × likelihood) tagged with ISO 25010 characteristic |
| 3 | Map risks → catalog IDs → atomic test IDs with technique column filled |
| 4 | Prepare fixtures; block destructive/out-of-scope actions |
| 5 | Execute highest risk first; log commands, builds, and correlation IDs |
| 6 | Classify each result with evidence tier (CONFIRMED / LIKELY / NOT TESTED / …) |
| 7 | File defects with independent oracle cited; separate speculative risks |
| 8 | Summarize gaps, blocked items, and regression candidates in tables |
| 9 | Copy `verification-checklist.md` with honest marks |
| 10 | Deliver per `execution-report-template.md` |

## Report presentation (required)

Matrices, defects, and gates must use **`references/report-output-format.md`**. No prose-only reports.

## Scenario index

| Case | Focus | Deep specification |
|------|-------|-------------------|
| COMP-001 | Operating system versions | `scenario-catalog.md#comp-001` |
| COMP-002 | Browser engine support | `scenario-catalog.md#comp-002` |
| COMP-003 | Device form factors | `scenario-catalog.md#comp-003` |
| COMP-004 | DPI scaling | `scenario-catalog.md#comp-004` |
| COMP-005 | Multi-monitor movement | `scenario-catalog.md#comp-005` |
| COMP-006 | Viewport bounds | `scenario-catalog.md#comp-006` |
| COMP-007 | Keyboard layouts | `scenario-catalog.md#comp-007` |
| COMP-008 | Input methods | `scenario-catalog.md#comp-008` |
| COMP-009 | RTL layout | `scenario-catalog.md#comp-009` |
| COMP-010 | CJK text | `scenario-catalog.md#comp-010` |
| COMP-011 | Emoji grapheme clusters | `scenario-catalog.md#comp-011` |
| COMP-012 | Long translations | `scenario-catalog.md#comp-012` |
| COMP-013 | Pseudo-localization | `scenario-catalog.md#comp-013` |
| COMP-014 | Timezone display | `scenario-catalog.md#comp-014` |
| COMP-015 | DST rollover | `scenario-catalog.md#comp-015` |
| COMP-016 | Number formatting | `scenario-catalog.md#comp-016` |
| COMP-017 | Currency formatting | `scenario-catalog.md#comp-017` |
| COMP-018 | Locale sorting | `scenario-catalog.md#comp-018` |
| COMP-019 | Filesystem portability | `scenario-catalog.md#comp-019` |
| COMP-020 | Proxy and VPN | `scenario-catalog.md#comp-020` |
| COMP-021 | Clean installation | `scenario-catalog.md#comp-021` |
| COMP-022 | Version upgrades | `scenario-catalog.md#comp-022` |
| COMP-023 | Rollback behavior | `scenario-catalog.md#comp-023` |
| COMP-024 | Platform assistive technology | `scenario-catalog.md#comp-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

