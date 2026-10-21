# Domain playbook — ux-accessibility-auditor

## Mission

Evaluate **task success**, **inclusive interaction**, and **WCAG 2.2** conformance for applicable UI—keyboard, screen reader, vision, cognitive load—not cosmetic polish alone.

## WCAG workflow

1. Define **scope** (A vs AA) with stakeholder.
2. Pick **representative tasks** (signup, checkout, settings).
3. For each task, test **keyboard-only** path start-to-finish.
4. Sample **screen reader** (NVDA/VoiceOver) on critical controls.
5. Record criterion ID per finding (e.g. 2.4.7 Focus Visible).

## Heuristic UX (ISO 9241)

| Dimension | Probe |
|-----------|--------|
| Discoverability | Can new user find primary action in <30s guided? |
| Error prevention | Destructive actions confirmed? |
| Recovery | Clear error messages with fix steps? |
| Consistency | Same terms/icons as rest of product |

## Common failure patterns

- Focus trap in modal; focus lost on route change.
- Icon-only buttons without accessible name.
- Color-only status indicators.
- Time limits without extension.

## Evidence

Screenshot + DOM node, axe/ WAVE output as **supplement** not sole oracle—manual task proof required for PASS.

## Pairing

`ui-visual-tester` for layout; `functional-tester` for journey logic.
