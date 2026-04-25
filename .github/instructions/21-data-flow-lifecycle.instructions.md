---
description: "Workflow recommendation for phase-gated, documentation-first data lifecycles across all sources."
applyTo: "**/*.{py,ipynb,md,yml,yaml}"
---

# Data Flow Lifecycle Recommendation

Recommended
- Use a documentation-first, phase-gated lifecycle for all data sources:
  - acquire raw source
  - document raw provenance
  - sanitize into project-ready dataset
  - document sanitized dataset and lineage
  - request human approval checkpoint
  - **write design brief for analysis logic** (in `04_Analytics/Analytical_Recipe.md`) for multi-step analysis tasks
  - **request human approval of design brief**
  - implement and run analysis from sanitized dataset
  - document analysis outputs
  - request human approval checkpoint
  - produce final visualizations/outputs
- Prefer one stage at a time unless the user asks for a full pipeline.
- Include quick validation info at each checkpoint (output paths + at least one sanity metric).
- Keep checkpoint reporting consistent with the shared field contract:
  - `stage_name`, `status`, `outputs`, `sanity_metrics`, `next_expected_input`, `notes_for_user_validation`
  - output format may vary (plain text, table, JSON/YAML, structured logs)

Required
- Do not skip provenance documentation for raw sources.
- Do not run analysis on undocumented raw data when a sanitized stage is expected.
- Keep stage boundaries explicit in script naming or orchestration.

Fallback
- If a task requires combining stages (time-critical or tiny scope), document why in `Design_Rationale.md` and still emit stage-like checkpoints.
