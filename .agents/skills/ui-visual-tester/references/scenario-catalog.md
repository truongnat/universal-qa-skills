# Scenario catalog — ui-visual-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Design system, responsive breakpoints, platform HIG/Material  
**Typical environment:** Pinned browser/OS; stable viewport; disable flaky animations where needed  
**P0 deep specs in this skill:** none (use generic rows)

### UI-001 — Visual hierarchy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *visual hierarchy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Perceptual consistency |
| **Variant matrix** | Breakpoint sweep, overflow strings |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-001a` happy, `UI-001b` negative, `UI-001c` boundary or auth) before PASS |

### UI-002 — Spacing alignment

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *spacing alignment* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-002a` happy, `UI-002b` negative, `UI-002c` boundary or auth) before PASS |

### UI-003 — Typography legibility

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *typography legibility* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-003a` happy, `UI-003b` negative, `UI-003c` boundary or auth) before PASS |

### UI-004 — Text wrapping

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *text wrapping* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-004a` happy, `UI-004b` negative, `UI-004c` boundary or auth) before PASS |

### UI-005 — Truncation policy

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *truncation policy* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-005a` happy, `UI-005b` negative, `UI-005c` boundary or auth) before PASS |

### UI-006 — Color contrast

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *color contrast* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-006a` happy, `UI-006b` negative, `UI-006c` boundary or auth) before PASS |

### UI-007 — Light theme

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *light theme* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-007a` happy, `UI-007b` negative, `UI-007c` boundary or auth) before PASS |

### UI-008 — Dark theme

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dark theme* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-008a` happy, `UI-008b` negative, `UI-008c` boundary or auth) before PASS |

### UI-009 — High contrast

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *high contrast* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-009a` happy, `UI-009b` negative, `UI-009c` boundary or auth) before PASS |

### UI-010 — Zoom and text scaling

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *zoom and text scaling* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-010a` happy, `UI-010b` negative, `UI-010c` boundary or auth) before PASS |

### UI-011 — Minimum viewport

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *minimum viewport* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-011a` happy, `UI-011b` negative, `UI-011c` boundary or auth) before PASS |

### UI-012 — Maximum viewport

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *maximum viewport* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-012a` happy, `UI-012b` negative, `UI-012c` boundary or auth) before PASS |

### UI-013 — Narrow height

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *narrow height* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-013a` happy, `UI-013b` negative, `UI-013c` boundary or auth) before PASS |

### UI-014 — Long translations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *long translations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-014a` happy, `UI-014b` negative, `UI-014c` boundary or auth) before PASS |

### UI-015 — RTL rendering

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rtl rendering* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-015a` happy, `UI-015b` negative, `UI-015c` boundary or auth) before PASS |

### UI-016 — Empty state

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *empty state* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-016a` happy, `UI-016b` negative, `UI-016c` boundary or auth) before PASS |

### UI-017 — Loading state

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *loading state* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Measured execution |
| **Variant matrix** | Baseline + % regression threshold |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-017a` happy, `UI-017b` negative, `UI-017c` boundary or auth) before PASS |

### UI-018 — Error state

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *error state* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-018a` happy, `UI-018b` negative, `UI-018c` boundary or auth) before PASS |

### UI-019 — Selected and disabled state

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *selected and disabled state* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-019a` happy, `UI-019b` negative, `UI-019c` boundary or auth) before PASS |

### UI-020 — Modal positioning

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *modal positioning* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-020a` happy, `UI-020b` negative, `UI-020c` boundary or auth) before PASS |

### UI-021 — Overlay clipping

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *overlay clipping* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-021a` happy, `UI-021b` negative, `UI-021c` boundary or auth) before PASS |

### UI-022 — Table overflow

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *table overflow* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-022a` happy, `UI-022b` negative, `UI-022c` boundary or auth) before PASS |

### UI-023 — Pixel density

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *pixel density* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-023a` happy, `UI-023b` negative, `UI-023c` boundary or auth) before PASS |

### UI-024 — Visual regression baseline

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *visual regression baseline* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Visual diff, layout stress (long text/RTL), state screenshots, component matrix |
| **Scenario focus** | Perceptual consistency |
| **Variant matrix** | Breakpoint sweep, overflow strings |
| **Oracle / anchor** | Design system, responsive breakpoints, platform HIG/Material |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `UI-024a` happy, `UI-024b` negative, `UI-024c` boundary or auth) before PASS |

