# Domain playbook — ui-visual-tester

## Mission

Detect **layout breakage**, **design system drift**, and **platform-specific visual defects** across breakpoints and themes.

## Matrix

| Axis | Values to cover |
|------|-----------------|
| Viewport | min, typical, max width; mobile safe areas |
| Theme | light/dark/high-contrast if supported |
| Locale | LTR + RTL if supported |
| Content stress | long strings, empty, many items |

## States per component

Default, hover/focus (where applicable), disabled, loading, error, empty.

## Techniques

- Snapshot compare with approved baselines (note tolerance).
- Overflow/clip inspection for tables and cards.
- Font scaling / OS text size on mobile.

## Evidence

Before/after screenshots, build ID, browser/OS. Flaky animations → disable or wait stable.

## Pairing

`ux-accessibility-auditor` for focus order vs visual order mismatches.
