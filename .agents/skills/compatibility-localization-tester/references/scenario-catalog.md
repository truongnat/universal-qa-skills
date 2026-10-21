# Scenario catalog — compatibility-localization-tester

> **Mandatory:** Expand every selected ID into atomic tests. Titles alone are not sufficient for PASS.

**Domain anchors:** Supported matrix doc, CLDR/locale rules, store policies  
**Typical environment:** Device farm or emulators per matrix row  
**P0 deep specs in this skill:** none (use generic rows)

### COMP-001 — Operating system versions

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *operating system versions* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-001a` happy, `COMP-001b` negative, `COMP-001c` boundary or auth) before PASS |

### COMP-002 — Browser engine support

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *browser engine support* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-002a` happy, `COMP-002b` negative, `COMP-002c` boundary or auth) before PASS |

### COMP-003 — Device form factors

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *device form factors* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-003a` happy, `COMP-003b` negative, `COMP-003c` boundary or auth) before PASS |

### COMP-004 — DPI scaling

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dpi scaling* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-004a` happy, `COMP-004b` negative, `COMP-004c` boundary or auth) before PASS |

### COMP-005 — Multi-monitor movement

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *multi-monitor movement* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-005a` happy, `COMP-005b` negative, `COMP-005c` boundary or auth) before PASS |

### COMP-006 — Viewport bounds

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *viewport bounds* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-006a` happy, `COMP-006b` negative, `COMP-006c` boundary or auth) before PASS |

### COMP-007 — Keyboard layouts

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *keyboard layouts* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Inclusive interaction |
| **Variant matrix** | Keyboard path, name/role/value, contrast |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-007a` happy, `COMP-007b` negative, `COMP-007c` boundary or auth) before PASS |

### COMP-008 — Input methods

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *input methods* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-008a` happy, `COMP-008b` negative, `COMP-008c` boundary or auth) before PASS |

### COMP-009 — RTL layout

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rtl layout* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Perceptual consistency |
| **Variant matrix** | Breakpoint sweep, overflow strings |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-009a` happy, `COMP-009b` negative, `COMP-009c` boundary or auth) before PASS |

### COMP-010 — CJK text

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *cjk text* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-010a` happy, `COMP-010b` negative, `COMP-010c` boundary or auth) before PASS |

### COMP-011 — Emoji grapheme clusters

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *emoji grapheme clusters* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-011a` happy, `COMP-011b` negative, `COMP-011c` boundary or auth) before PASS |

### COMP-012 — Long translations

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *long translations* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-012a` happy, `COMP-012b` negative, `COMP-012c` boundary or auth) before PASS |

### COMP-013 — Pseudo-localization

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *pseudo-localization* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-013a` happy, `COMP-013b` negative, `COMP-013c` boundary or auth) before PASS |

### COMP-014 — Timezone display

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *timezone display* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Locale matrix |
| **Variant matrix** | Pseudo-loc, RTL mirror, DST boundary |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-014a` happy, `COMP-014b` negative, `COMP-014c` boundary or auth) before PASS |

### COMP-015 — DST rollover

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *dst rollover* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-015a` happy, `COMP-015b` negative, `COMP-015c` boundary or auth) before PASS |

### COMP-016 — Number formatting

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *number formatting* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-016a` happy, `COMP-016b` negative, `COMP-016c` boundary or auth) before PASS |

### COMP-017 — Currency formatting

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *currency formatting* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-017a` happy, `COMP-017b` negative, `COMP-017c` boundary or auth) before PASS |

### COMP-018 — Locale sorting

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *locale sorting* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Locale matrix |
| **Variant matrix** | Pseudo-loc, RTL mirror, DST boundary |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-018a` happy, `COMP-018b` negative, `COMP-018c` boundary or auth) before PASS |

### COMP-019 — Filesystem portability

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *filesystem portability* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-019a` happy, `COMP-019b` negative, `COMP-019c` boundary or auth) before PASS |

### COMP-020 — Proxy and VPN

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *proxy and vpn* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-020a` happy, `COMP-020b` negative, `COMP-020c` boundary or auth) before PASS |

### COMP-021 — Clean installation

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *clean installation* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-021a` happy, `COMP-021b` negative, `COMP-021c` boundary or auth) before PASS |

### COMP-022 — Version upgrades

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *version upgrades* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-022a` happy, `COMP-022b` negative, `COMP-022c` boundary or auth) before PASS |

### COMP-023 — Rollback behavior

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *rollback behavior* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-023a` happy, `COMP-023b` negative, `COMP-023c` boundary or auth) before PASS |

### COMP-024 — Platform assistive technology

| Dimension | Guidance |
|-----------|----------|
| **Objective** | Prove or disprove that *platform assistive technology* holds under realistic abuse and normal use within scope. |
| **Primary techniques** | Config matrix, pseudo-locale, RTL, timezone/DST edges |
| **Scenario focus** | Core behavior vs documented intent |
| **Variant matrix** | Valid/invalid/boundary; repeat; interrupt; resume; concurrent if applicable |
| **Oracle / anchor** | Supported matrix doc, CLDR/locale rules, store policies |
| **Failure signals** | Wrong HTTP/business code, data leak across tenants, silent corruption, misleading UX, missing audit event |
| **Evidence** | Redacted request/response, HAR snippet, screenshot + DOM snapshot, SQL row count, log correlation ID |
| **Minimum atomic cases** | ≥3 derived IDs (e.g. `COMP-024a` happy, `COMP-024b` negative, `COMP-024c` boundary or auth) before PASS |

