# Scripts

Use this folder for reusable project scripts.

Guidelines
- Keep scripts task-focused and named by intent.
- Prefer domain separation in multi-stage workflows:
	- `fetch_*.py` for acquisition/download
	- `analyze_*.py` for analysis/modeling
	- `visualize_*.py` for maps/charts/exports
- Prefer idempotent behavior where practical.
- Document script purpose and logic in `Design_Rationale.md`.
- After each stage, print a short completion summary with output paths and one sanity metric.

Completion checkpoint contract (all scripts)
- Use these fields after each stage:
	- `stage_name`
	- `status` (`success` or `failed`)
	- `outputs` (one or more paths)
	- `sanity_metrics` (key-value checks)
	- `next_expected_input`
	- `notes_for_user_validation`
- Keep the same fields across scripts, but choose any output style:
	- plain text
	- table
	- JSON or YAML
	- structured logger output

Example (plain text)
- stage_name: sanitize_network
- status: success
- outputs: ["00_Binary/derived/network_clean.gpkg"]
- sanity_metrics: {"feature_count": 12453, "crs": "EPSG:25832"}
- next_expected_input: "00_Binary/derived/network_clean.gpkg"
- notes_for_user_validation: "Confirm major roads are preserved and pedestrian-only paths were filtered as intended."

Example (JSON)
```json
{
	"stage_name": "analyze_accessibility",
	"status": "success",
	"outputs": ["00_Binary/derived/accessibility_scores.gpkg"],
	"sanity_metrics": {
		"row_count": 342,
		"null_ratio_access_score": 0.0
	},
	"next_expected_input": "00_Binary/derived/accessibility_scores.gpkg",
	"notes_for_user_validation": "Check whether high-barrier zones align with expected arterial roads."
}
```

Documentation expectations (GIS users)
- Explain the workflow logic and why each stage exists.
- Point to where key task logic lives (file and function/section).
- For OSM scripts, document query/tag scope, network assumptions, and clipping/boundary rules.

Logging expectations
- Default output should be verbose enough for users to validate progress.
- Provide a quiet mode for simple runs.
- Provide file logging for long/debug runs (prefer `.cache/logs/`).
- Recommended CLI switches: `--log-level`, `--quiet`, `--log-file`.

Examples
- `fetch_osm_data.py`
- `prepare_network_layers.py`
- `run_accessibility_analysis.py`
