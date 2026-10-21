# Contributing

## Editing skills

1. **Shared templates and contracts** — edit `.agents/skills/_shared/references/`, then run:
   ```bash
   python3 scripts/maintain_repo.py sync
   ```
2. **Scenario catalogs** — edit the `SKILL.md` under each skill (or adjust `scripts/maintain_repo.py` if reshaping all skills). Keep total scenario count at **356** unless README is updated.
3. **Reshape all SKILL bodies** from current files (parses scenarios, rewrites sections):
   ```bash
   python3 scripts/maintain_repo.py reshape
   ```

## Validation

```bash
python3 scripts/maintain_repo.py validate
```

Checks: shared reference checksums per skill, scenario count, report-format references in every `SKILL.md`.

## Report output

New QA behavior or templates should align with `report-output-format.md`. See `docs/sample-release-assessment.md` for an example deliverable.
