# Domain playbook — compatibility-localization-tester

## Mission

Validate **supported platform matrix** and **locale correctness**—not every device on earth, but every **claimed** combination.

## Matrix document

Rows: OS × browser/device × app version. Columns: smoke test status, defects, N/A reason.

## i18n / l10n

| Check | Detail |
|-------|--------|
| Translation | No truncated keys; plural rules |
| Formats | Date, number, currency per locale |
| RTL | Layout mirror, icons, scroll |
| Timezone | DST boundaries for scheduling features |
| Encoding | Unicode names, emoji, combining chars |

## Co-existence

- Install alongside conflicting apps if relevant.
- OS permissions (camera, files) per platform policy.

## Evidence

Screenshots per matrix cell; locale code in report row.

## Pairing

`ui-visual-tester` for layout; `functional-tester` for locale-specific rules.
