---
description: "Workflow recommendation for phase-gated, documentation-first data lifecycles across all sources."
applyTo: "**/*.{py,ipynb,md,yml,yaml}"
---

# Data Flow Lifecycle Recommendation

Required rules override Recommended defaults and Fallback accommodations. Fallback rules may relax Recommended defaults but never Required rules.

Recommended
- Use a documentation-first, phase-gated lifecycle for all data sources:
  - acquire raw source
  - document raw provenance
  - sanitize into project-ready dataset
  - document sanitized dataset and lineage
  - request human approval checkpoint
  - **write design brief for analysis logic** (in `jobs/<job_name>/Analytical_Recipe.md`) for analysis tasks that involve more than one distinct transformation, aggregation, or modeling operation on the sanitized dataset
  - **request human approval of design brief**
  - implement and run analysis from sanitized dataset
  - document analysis outputs
  - request human approval checkpoint
  - produce final visualizations/outputs
- Prefer one stage at a time; only combine stages when the Fallback rule applies, and still emit stage-like checkpoints.
- If a human approval checkpoint is declined or times out, stop progression, record the rejection or timeout reason in `Design_Rationale.md`, and await explicit user instruction before retrying or reverting the stage. Do not proceed to the next stage automatically.
- Include quick validation info at each checkpoint (output paths + at least one sanity metric).
- If any sanity metric falls outside expected bounds (for example, row count drops more than 50 percent or null rate exceeds 20 percent), halt the pipeline, report the anomaly in `notes_for_user_validation`, and do not advance without explicit user confirmation.
- Keep checkpoint reporting consistent with the shared field contract:
  - `stage_name`, `status`, `outputs`, `sanity_metrics`, `next_expected_input`, `notes_for_user_validation`
  - default to JSON/YAML for machine-readable pipelines and plain text tables for interactive sessions; only deviate when the user explicitly requests another format

Required
- Do not skip provenance documentation for raw sources.
- Do not run analysis on undocumented raw data when a sanitized stage is expected.
- Keep stage boundaries explicit in script naming or orchestration.

Fallback
- If a task requires combining stages for time-critical work or a tiny-scope task involving a single data source under 1,000 rows with no joins, aggregations, or model training, document why in `Design_Rationale.md`, create `Design_Rationale.md` at the project root with a top-level heading `# Design Rationale` if it does not exist, and still emit stage-like checkpoints.
