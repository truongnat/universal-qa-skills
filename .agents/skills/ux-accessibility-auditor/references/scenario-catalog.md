# Scenario catalog — ux-accessibility-auditor

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** WCAG 2.2 A/AA, ISO 9241, APG patterns  
**Typical environment:** Real browsers + assistive tech when possible; design tokens reference  
**P0 deep specs in this skill:** none (use generic rows)

### UX-001 — Task discoverability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *task discoverability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-001a` happy, `UX-001b` negative, `UX-001c` boundary or auth) before PASS |

### UX-002 — Information architecture

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *information architecture* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Structure review |
| **Variant matrix** | Forbidden dependency rules |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-002a` happy, `UX-002b` negative, `UX-002c` boundary or auth) before PASS |

### UX-003 — Feedback latency

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *feedback latency* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-003a` happy, `UX-003b` negative, `UX-003c` boundary or auth) before PASS |

### UX-004 — Undo and cancel

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *undo and cancel* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-004a` happy, `UX-004b` negative, `UX-004c` boundary or auth) before PASS |

### UX-005 — Destructive action prevention

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *destructive action prevention* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-005a` happy, `UX-005b` negative, `UX-005c` boundary or auth) before PASS |

### UX-006 — Validation clarity

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *validation clarity* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-006a` happy, `UX-006b` negative, `UX-006c` boundary or auth) before PASS |

### UX-007 — Keyboard-only flow

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *keyboard-only flow* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-007a` happy, `UX-007b` negative, `UX-007c` boundary or auth) before PASS |

### UX-008 — Logical focus sequence

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *logical focus sequence* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-008a` happy, `UX-008b` negative, `UX-008c` boundary or auth) before PASS |

### UX-009 — Focus visibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *focus visibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-009a` happy, `UX-009b` negative, `UX-009c` boundary or auth) before PASS |

### UX-010 — Focus restoration

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *focus restoration* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-010a` happy, `UX-010b` negative, `UX-010c` boundary or auth) before PASS |

### UX-011 — Accessible names

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *accessible names* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-011a` happy, `UX-011b` negative, `UX-011c` boundary or auth) before PASS |

### UX-012 — Roles and values

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *roles and values* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-012a` happy, `UX-012b` negative, `UX-012c` boundary or auth) before PASS |

### UX-013 — Screen reader announcements

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *screen reader announcements* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-013a` happy, `UX-013b` negative, `UX-013c` boundary or auth) before PASS |

### UX-014 — Heading hierarchy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *heading hierarchy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Perceptual consistency |
| **Variant matrix** | Breakpoint sweep, overflow strings |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-014a` happy, `UX-014b` negative, `UX-014c` boundary or auth) before PASS |

### UX-015 — Text alternatives

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *text alternatives* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-015a` happy, `UX-015b` negative, `UX-015c` boundary or auth) before PASS |

### UX-016 — Color-independent status

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *color-independent status* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-016a` happy, `UX-016b` negative, `UX-016c` boundary or auth) before PASS |

### UX-017 — Text resizing

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *text resizing* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-017a` happy, `UX-017b` negative, `UX-017c` boundary or auth) before PASS |

### UX-018 — Reflow

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *reflow* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-018a` happy, `UX-018b` negative, `UX-018c` boundary or auth) before PASS |

### UX-019 — Pointer alternatives

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *pointer alternatives* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-019a` happy, `UX-019b` negative, `UX-019c` boundary or auth) before PASS |

### UX-020 — Reduced motion

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *reduced motion* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-020a` happy, `UX-020b` negative, `UX-020c` boundary or auth) before PASS |

### UX-021 — Touch targets

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *touch targets* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-021a` happy, `UX-021b` negative, `UX-021c` boundary or auth) before PASS |

### UX-022 — Shortcut discoverability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *shortcut discoverability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-022a` happy, `UX-022b` negative, `UX-022c` boundary or auth) before PASS |

### UX-023 — Localized errors

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *localized errors* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-023a` happy, `UX-023b` negative, `UX-023c` boundary or auth) before PASS |

### UX-024 — Assistance and help

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *assistance and help* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Task-based review, keyboard-only paths, screen reader spot checks, reflow/zoom |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | WCAG 2.2 A/AA, ISO 9241, APG patterns |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UX-024a` happy, `UX-024b` negative, `UX-024c` boundary or auth) before PASS |

