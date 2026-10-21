# Contributing

## Editing skills

1. **Shared templates, principles, and contracts** — edit `.agents/skills/_shared/references/` (including `testing-principles.md`, `test-design-techniques.md`, etc.), then run:
   ```bash
   python3 scripts/maintain_repo.py sync
   ```
2. **Scenario catalogs** — edit the `SKILL.md` under each skill (or adjust `scripts/maintain_repo.py` if reshaping all skills). Keep total scenario count at **356** unless README is updated.
3. **Domain depth** — edit playbooks under `scripts/skill_depth/playbooks/<skill>.md`, then regenerate catalogs + `SKILL.md`:
   ```bash
   python3 scripts/maintain_repo.py reshape
   # or: python3 scripts/generate_skill_depth.py
   ```
4. **P0 scenario overrides (50 IDs)** — edit `scripts/skill_depth/build_overrides.py`, then:
   ```bash
   python3 scripts/skill_depth/build_overrides.py
   python3 scripts/generate_skill_depth.py
   ```
   Commits `scenario_overrides.json`; catalog rows for those IDs show **Tier P0 manual override**.

## Validation

```bash
python3 scripts/maintain_repo.py validate
```

Checks: shared reference checksums per skill, scenario count, report-format references in every `SKILL.md`.

## Report output

New QA behavior or templates should align with `report-output-format.md`. See `docs/sample-release-assessment.md` for an example deliverable.
