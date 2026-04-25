---
description: "Workflow recommendation for script placement and rationale logging. Use when creating Python, shell, SQL, or utility scripts for project workflows."
applyTo: "**/*.{py,sh,sql,md,yml,yaml}"
---

# Script Location And Rationale

Recommended
- Save reusable project scripts in the configured script folder from `.github/workflow-preferences.yaml`.
- Use a clear filename that signals purpose, for example `fetch_osm_data.py` or `build_network_graph.py`.
- Use domain-separated script names for major workflows:
	- acquisition stage (for example `fetch_*.py`)
	- analysis stage (for example `analyze_*.py`)
	- visualisation stage (for example `visualize_*.py`)
- Default to phase-gated delivery: finish one stage and validate it before writing the next stage script.
- For multi-step analysis scripts, apply the design-before-code gate: write a design brief in `04_Analytics/Analytical_Recipe.md` and get user approval before implementing code.
- Simple single-operation tasks (a straightforward fetch, format conversion, quick plot) may skip the design brief and proceed directly to implementation.
- Follow this recommended lifecycle across all data flows:
	- raw access/download
	- raw documentation
	- sanitization to project-ready dataset
	- sanitized documentation
	- human approval checkpoint
	- **design brief for analysis logic** (in Analytical Recipe)
	- **human approval of design brief**
	- analysis implementation from sanitized dataset
	- analysis output documentation
	- human approval checkpoint
	- final visualization/output stage
- Default to user-friendly verbose terminal output unless the user requests quiet mode.
- Prefer configurable logging controls (for example `--log-level`, `--quiet`, `--log-file`) so the same script supports:
	- interactive verbose runs
	- long-running debug sessions with file logs
	- quick low-noise operations

Required
- Keep scripts inside the workspace boundary.
- For multi-step analysis scripts, write a design brief in `04_Analytics/Analytical_Recipe.md` and obtain user approval before writing code. Simple single-operation tasks are exempt.
- Document the overall script logic and intended use in `Design_Rationale.md`.
- Keep script responsibilities clear: do not merge data download, analysis, and visualisation into one opaque stage.
- Do not author all stage scripts in advance unless the user explicitly asks for a full pipeline.
- After each stage checkpoint, wait for user confirmation before proceeding to the next stage.
- Emit a user-readable completion checkpoint after each stage with output paths and at least one sanity metric.
- Use a stable completion-checkpoint field contract across scripts:
	- `stage_name`
	- `status`
	- `outputs`
	- `sanity_metrics`
	- `next_expected_input`
	- `notes_for_user_validation`
- The field contract is required, but output format is flexible (plain text, table, JSON/YAML, structured logs).
- Logging behavior must be explicit and configurable; scripts should not hardcode a single verbosity mode.
- Include GIS-user-oriented documentation in script headers or companion docs:
	- workflow purpose in domain language
	- where core logic is implemented (module/function names)
	- assumptions used in spatial filtering, CRS handling, and attribute derivation

Fallback
- If the configured script folder is missing, create it and add a short local README.
- If a script is one-off and intentionally not reusable, note that decision in `Design_Rationale.md`.
