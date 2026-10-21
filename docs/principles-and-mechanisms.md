# Principles & Mechanisms (overview)

Research-backed QA concepts embedded in every skill under `.agents/skills/_shared/references/`. After install, the same files appear in each skill’s `references/` folder.

## Layered model

```text
Principles (why)     → testing-principles.md
Risk (what first)    → risk-based-testing.md
Techniques (how)     → test-design-techniques.md
Oracles (expected)   → oracles-and-heuristics.md
Quality tags (what)  → quality-attribute-model.md
Agent safety (who)   → agent-qa-mechanisms.md
Standards map        → standards-mapping.md
```

## Quick reference

| Topic | Key idea |
|-------|----------|
| ISTQB 7 principles | No proof of zero bugs; prioritize; early static+dynamic; clusters; vary tests; context; validate fitness |
| ISO 29119-4 | Equivalence, BVA, decision tables, state transition, combinatorial, structure-based, exploratory |
| ISO 25010 | Nine product characteristics to tag risks and gates |
| Risk-based testing | Impact × likelihood → depth, technique choice, residual risk at release |
| Oracles | Independent expected results; FEW HICCUPPS for exploration hints |
| SFDPOT | Structure, Function, Data, Platform, Operations, Time |
| Agent QA | Untrusted files, evidence tiers, no fabricated runs, merge/challenge for multi-agent |

## Sources (public summaries)

- ISTQB Certified Tester Foundation Level Syllabus (principles, oracles)
- ISO/IEC/IEEE 29119 series (process, techniques, keyword-driven testing)
- ISO/IEC 25010 product quality model
- James Bach / Michael Bolton — FEW HICCUPPS, SFDPOT, session-based exploratory testing

Official standards and syllabi remain authoritative; this repo provides **operational prompts for AI agents**, not certification.

## Maintainer

Add or edit shared references, then:

```bash
python3 scripts/maintain_repo.py sync
python3 scripts/maintain_repo.py validate
```
