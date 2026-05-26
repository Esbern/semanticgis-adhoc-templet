---
description: "Workflow recommendation for selecting Python environment manager from repository preferences. Use when creating or choosing a Python environment."
applyTo: "**/*.{py,ipynb,md,yml,yaml}"
---

# Python Environment Selection From Config

Recommended
- Read `.github/workflow-preferences.yaml` before selecting a Python environment manager.
- Use `python.default_manager` as the default selection for non-GIS tasks.
- For GIS-heavy tasks, prefer `python.gis_manager_priority` in order.

Required
- Respect `python.require_local_environment: true` as a hard constraint.
- Never install Python packages into global/system Python.

Fallback
- If a preferred manager is unavailable, move to the next manager in the configured priority list.
- Record manager choice and any deviation from config in `Design_Rationale.md`.
