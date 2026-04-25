---
description: "Workflow recommendation for Python execution isolation in this template. Use when running Python scripts, notebooks, package installs, or geospatial analysis code."
applyTo: "**/*.{py,ipynb,md}"
---

# Python Environment Recommendation

Required
- Use a project-local Python environment only (for example `.venv`, `micromamba`, `conda`, `poetry`, or similar).
- Never install packages into the global/system Python for this project.

Recommended
- Default to lightweight `.venv` for general tasks.
- For recurring GIS-heavy workflows, prefer `micromamba` or `conda` when available.
- Let the agent choose the best manager within repository preferences in `.github/workflow-preferences.yaml`.
- Keep dependency installation scoped to the selected local environment.
- Record environment decisions in `Design_Rationale.md` when they materially affect reproducibility.

Fallback
- If preferred tooling fails, switch to another local environment strategy rather than using global Python.
