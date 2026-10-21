---
name: ui-visual-tester
description: "Native and web visual integrity and layout regression. Deep playbooks and per-scenario specs in references/. Use for UI and visual quality. Structured markdown reports required."
---

# ui-visual-tester

**Purpose:** Native and web visual integrity. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** Design system, responsive breakpoints, platform HIG/Material

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
| UI-001 | Visual hierarchy | `scenario-catalog.md#ui-001` |
| UI-002 | Spacing alignment | `scenario-catalog.md#ui-002` |
| UI-003 | Typography legibility | `scenario-catalog.md#ui-003` |
| UI-004 | Text wrapping | `scenario-catalog.md#ui-004` |
| UI-005 | Truncation policy | `scenario-catalog.md#ui-005` |
| UI-006 | Color contrast | `scenario-catalog.md#ui-006` |
| UI-007 | Light theme | `scenario-catalog.md#ui-007` |
| UI-008 | Dark theme | `scenario-catalog.md#ui-008` |
| UI-009 | High contrast | `scenario-catalog.md#ui-009` |
| UI-010 | Zoom and text scaling | `scenario-catalog.md#ui-010` |
| UI-011 | Minimum viewport | `scenario-catalog.md#ui-011` |
| UI-012 | Maximum viewport | `scenario-catalog.md#ui-012` |
| UI-013 | Narrow height | `scenario-catalog.md#ui-013` |
| UI-014 | Long translations | `scenario-catalog.md#ui-014` |
| UI-015 | RTL rendering | `scenario-catalog.md#ui-015` |
| UI-016 | Empty state | `scenario-catalog.md#ui-016` |
| UI-017 | Loading state | `scenario-catalog.md#ui-017` |
| UI-018 | Error state | `scenario-catalog.md#ui-018` |
| UI-019 | Selected and disabled state | `scenario-catalog.md#ui-019` |
| UI-020 | Modal positioning | `scenario-catalog.md#ui-020` |
| UI-021 | Overlay clipping | `scenario-catalog.md#ui-021` |
| UI-022 | Table overflow | `scenario-catalog.md#ui-022` |
| UI-023 | Pixel density | `scenario-catalog.md#ui-023` |
| UI-024 | Visual regression baseline | `scenario-catalog.md#ui-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

