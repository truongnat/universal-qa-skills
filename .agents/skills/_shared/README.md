# Shared QA references (maintainer source)

Not an installable skill. Canonical templates and contracts live in `references/`.

After editing files here, run from the repository root:

```bash
python3 scripts/maintain_repo.py sync
python3 scripts/maintain_repo.py validate
```

This copies shared files into each skill's `references/` folder so `npx skills` installs remain self-contained.
