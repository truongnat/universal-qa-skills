---
name: ux-accessibility-auditor
description: "Usability, WCAG-oriented accessibility, and inclusive UX. Deep playbooks and per-scenario specs in references/. Use for UX and accessibility. Structured markdown reports required."
---

# ux-accessibility-auditor

**Purpose:** Usability and accessible interaction. Technology agnostic: web, native, mobile, API, CLI, infrastructure and data workloads are in scope only when applicable.

## Start here (depth)

1. Read **`references/domain-playbook.md`** — domain workflow, rubrics, pitfalls (not optional).
2. For each scenario you select, implement **`references/scenario-catalog.md`** (techniques, variants, evidence).
3. Apply shared contracts: `mandatory-contract.md`, `quality-standard.md`, `report-output-format.md`.
4. Apply principles: `testing-principles.md`, `risk-based-testing.md`, `test-design-techniques.md`, `oracles-and-heuristics.md`, `agent-qa-mechanisms.md`.

**Domain anchors:** WCAG 2.2 A/AA, ISO 9241, APG patterns

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
| UX-001 | Task discoverability | `scenario-catalog.md#ux-001` |
| UX-002 | Information architecture | `scenario-catalog.md#ux-002` |
| UX-003 | Feedback latency | `scenario-catalog.md#ux-003` |
| UX-004 | Undo and cancel | `scenario-catalog.md#ux-004` |
| UX-005 | Destructive action prevention | `scenario-catalog.md#ux-005` |
| UX-006 | Validation clarity | `scenario-catalog.md#ux-006` |
| UX-007 | Keyboard-only flow | `scenario-catalog.md#ux-007` |
| UX-008 | Logical focus sequence | `scenario-catalog.md#ux-008` |
| UX-009 | Focus visibility | `scenario-catalog.md#ux-009` |
| UX-010 | Focus restoration | `scenario-catalog.md#ux-010` |
| UX-011 | Accessible names | `scenario-catalog.md#ux-011` |
| UX-012 | Roles and values | `scenario-catalog.md#ux-012` |
| UX-013 | Screen reader announcements | `scenario-catalog.md#ux-013` |
| UX-014 | Heading hierarchy | `scenario-catalog.md#ux-014` |
| UX-015 | Text alternatives | `scenario-catalog.md#ux-015` |
| UX-016 | Color-independent status | `scenario-catalog.md#ux-016` |
| UX-017 | Text resizing | `scenario-catalog.md#ux-017` |
| UX-018 | Reflow | `scenario-catalog.md#ux-018` |
| UX-019 | Pointer alternatives | `scenario-catalog.md#ux-019` |
| UX-020 | Reduced motion | `scenario-catalog.md#ux-020` |
| UX-021 | Touch targets | `scenario-catalog.md#ux-021` |
| UX-022 | Shortcut discoverability | `scenario-catalog.md#ux-022` |
| UX-023 | Localized errors | `scenario-catalog.md#ux-023` |
| UX-024 | Assistance and help | `scenario-catalog.md#ux-024` |

## Verification checklist

Copy `references/verification-checklist.md` into the final report.

