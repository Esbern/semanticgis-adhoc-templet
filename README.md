# SemanticGIS Project Template

This repository is a reusable template for starting a SemanticGIS project with consistent structure, secure credential handling, and intent-first stewardship.

## Included Scaffold

- `Design_Rationale.md`
- `copilot-instructions.md`
- `.gitignore`
- `.env.example`
- `.cache/` — Package cache directory (OSMnx, raster tiles, temporary downloads; gitignored)
- `00_Binary/raw/`, `staging/`, `derived/`
- `01_Scoping/` — Project outline, research questions, stakeholder map
- `02_Modelling/` — Data model diagram, NOIR attribute catalog, ontology
- `03_Sanctuary/` — Logical layer with manifests and lineage
  - `raw/` — Raw data source provenance
  - `processed/` — Processing lineage and NOIR documentation
  - `intake/` — One intake record per query run (routing + contract + artifact declaration)
  - `semanticgisdk_interface_contract.v1.md` — explicit boundary between semanticgis.dk contracts and local project execution
  - `semanticgis_hub_routing.contract.v1.json` — deterministic routing rules between semanticgis.dk and semanticgis.org
  - `processed/query_artifact_manifest.template.json` — repeatable schema for query outputs (results, GeoJSON, map)
- `04_Analytics/` — Analytical recipe and analysis plan
- `05_Outputs/` — Output narrative and visualisation spec
- `10_scripts/` — Reusable project-local scripts

## Design Philosophy

This template is built for **agentic AI-assisted GIS work** and is designed for both ad-hoc users (exploring a question for the first time) and professional analysts (running structured, reproducible workflows).

Core principles:

- **Intention first.** Start by describing what you want to understand or analyze. The project structure guides you from scoping through to outputs — you do not need to know the tooling up front.
- **Agent autonomy with guardrails.** The AI agent chooses its own tools and libraries within a set of reproducible best-practice constraints. Hard rules (local Python environments, no secrets in committed files, binary-logical separation) are enforced. Everything else is a recommendation the agent can override with a logged rationale.
- **Reproducible by default.** Every data acquisition is manifested, every transformation is logged, and all analysis runs inside a project-local environment — never the global Python.
- **Low floor, high ceiling.** Ad-hoc users can clone this template, open it with an AI-enabled editor, and start working immediately. Power users can extend the instruction packs, add custom preferences, and wire in CI/CD.

## Quick Start

1. Create a new repository from this template.
2. Copy `.env.example` to `.env` and fill local values.
3. Keep `.env` local only (never commit secrets).
4. Open the project in an AI-enabled editor (VS Code with GitHub Copilot, Cursor, etc.).
5. Paste the **onboarding prompt** below to orient the agent.
6. Then describe your intent — see the example prompts for inspiration.

### Onboarding Prompt (paste this first)

> Please read through this entire repository — every file, every instruction pack, and the workflow preferences. Verify that you understand the SemanticGIS intent-first project structure, the binary-logical separation protocol, the NOIR attribute documentation requirements, and the two-layer instruction model (governance rules vs. modular recommendations). Summarise what you understand and flag anything that looks incomplete or inconsistent before we begin work.

This ensures the agent loads all governance context and instruction packs before taking any action. You only need to do this once per conversation.

### Example: Ad-Hoc User Prompt

An ad-hoc user who has never done GIS work might start with a prompt like this:

> I want to map schools, kindergartens, and other children's institutions in Rødovre Municipality using OSM data. For each institution I want to know how much green area is within 15 minutes walking distance. The municipality has some large roads that act as barriers — mark those clearly in red. Show the results as an interactive web map.

This works because it is **intention-first**: it names the geographic entities, specifies a concrete metric (green area within 15-minute walk), calls out a spatial relationship (barrier roads), picks a data source, and requests a tangible output format — but leaves all tooling, environment, and protocol decisions to the agent.

### Example: Professional Analyst Prompt

A professional user might be more specific about method:

> Set up a network analysis for Rødovre Municipality. Pull the walkable and cycleable OSM network via OSMnx. Geocode all schools and kindergartens from the Danish institution register (use the Datafordeler API key in .env). Compute isochrone polygons at 5, 10, and 15 minute walk/cycle times from each institution. Overlay green area polygons and flag institutions where no green area falls within the 10-minute cycling isochrone. Export the result as a GeoPackage and produce a static map with classified symbology.

Both prompts will trigger the same underlying governance — local environments, manifested data, binary-logical separation, NOIR documentation — but the agent adapts its workflow to the user's level of specificity.

### Secrets Handling (Required)

- `.env.example` is the required template for secret/config variable names.
- Real values must be stored only in local `.env` (never in git).
- Do not place secrets in sanctuary manifests, markdown documentation, scripts, or notebooks.

### Data Separation (Required)

- `03_Sanctuary/` is logical-only: manifests, lineage, NOIR attribute semantics, source descriptors, and transformation rationale.
  - `raw/_manifest.md` logs source provenance and original attributes.
  - `processed/` contains processed-layer manifests with attribute-level NOIR levels and transformation detail.
  - `Sanctuary_Index.md` tracks lineage from raw to derived binaries.
- `00_Binary/` is binary-only and local: raw downloads, staging files, derived binary artifacts.
- Binary files remain inside the project workspace for sandboxing, but are gitignored.
- The scaffold includes placeholder `.keep` files so binary folders exist after clone.
- Agents must not write outside the project folder unless explicitly requested by the user.

### NOIR Attribute Documentation (Required)

- For each dataset, document attribute-level NOIR levels (Nominal, Ordinal, Interval, Ratio) in the corresponding processed manifest.
- Link attribute semantics to the ontology in `02_Modelling/Ontology.md`.
- Use `03_Sanctuary/Sanctuary_Index.md` to track which processed manifest covers each transformation.

### Script Boundaries And Stage Validation (Required)

- Agents should separate major workflow responsibilities into clear script domains:
  - data acquisition/download
  - analysis/modeling
  - visualisation/export
- If an orchestrator script is used, it should call stage scripts and keep stage boundaries explicit.
- Default workflow is phase-gated: complete and validate one stage before creating the next stage script.
- Agents should wait for user confirmation between stages.
- Full pipeline creation is only expected when the user explicitly asks for it, or after all prior stages are complete and the user requests consolidation.
- After each stage, scripts should provide user-readable completion info so users can validate progress:
  - output path(s)
  - a simple sanity metric (for example feature count, CRS, or file-exists check)
  - a clear failure message if the stage did not complete
- Use a consistent checkpoint field contract across stages while allowing any output format:
  - `stage_name`, `status`, `outputs`, `sanity_metrics`, `next_expected_input`, `notes_for_user_validation`
  - accepted formats: plain text, table, JSON/YAML, or structured logs

### Recommended Data Lifecycle (All Sources)

- Use this default lifecycle for any source type (API, OSM, file download, register, raster, survey):
  - acquire raw data
  - document raw provenance
  - sanitize into project-ready data
  - document sanitized data and lineage
  - pause for user approval (optionally with quick visualization)
  - run analysis on sanitized data
  - document analysis outputs
  - pause for user approval
  - produce final visualization/communication outputs
- This is a recommendation, not a hard lock: the AI can adapt the sequence when justified by the task.
- When deviating, record the rationale in `Design_Rationale.md`.

### GIS-Focused Script Documentation (Required)

- Write script documentation for GIS users, emphasizing workflow logic over code mechanics.
- Document where core logic is implemented (script and function/section), so users can trace behavior quickly.
- For OSM-based tasks, explicitly document:
  - selected tags/query scope
  - network assumptions (walk/bike/drive)
  - clipping and boundary rules

### Logging Modes For Scripts (Recommended)

- Default to informative terminal output so users can follow progress during normal runs.
- Support a quiet mode for quick low-noise operations.
- Support file logging for long runs and debugging (recommended log directory: `.cache/logs/`).
- Keep logger implementation flexible (standard `logging`, structured logger, or equivalent), as long as mode selection is explicit and user-controllable.

## Required Environment Variables

Add project-specific secrets and configuration to `.env`. The `.env.example` file shows the expected variable names — replace or extend them for your project.

The template ships with one example placeholder:

- `DATAFORDELER_API_KEY` — Danish public-register access (remove if not needed)

## Canonical References

Human-oriented references:

- SemanticGIS Project Bootstrap Manifest (semanticgis.org)
- Intent-First Copilot Instructions Template (semanticgis.org)
- Introduction: The SemanticGIS Manifesto (semanticgis.org)

These are not machine-readable service/data contracts and must not be used as contract endpoints for runtime acquisition logic.

## semanticgis Hub Interface (Project Startup)

Every new project should treat semanticgis.dk and semanticgis.org as shared source-contract hubs and this template as the local execution layer.

- Read and apply first: `03_Sanctuary/semanticgis_hub_contract_index.v1.json`
- Read and apply: `03_Sanctuary/semanticgisdk_interface_contract.v1.md`
- Read and apply: `03_Sanctuary/semanticgis_hub_routing.contract.v1.json`
- Instantiate output contract from: `03_Sanctuary/processed/query_artifact_manifest.template.json`

Contract resolution rule:

- Start from declared contract artifacts and contract records, not general website pages.
- Human-readable hub pages may explain the system, but they do not count as machine-readable contracts unless they are explicit contract files.

Hub-routing rule:

- Use semanticgis.dk for Danish register/service contracts.
- Use semanticgis.org for international sources (including OSM and satellite imagery contracts).
- Danish projects may combine both hubs in a single workflow.

This prevents runtime rediscovery of service type, geometry fields, hub selection, and auth semantics.

## Query Run Intake (Required)

Create one intake file per query run before implementation:

- Template: `03_Sanctuary/intake/query_run_intake.template.json`
- Guidance: `03_Sanctuary/intake/README.md`

The intake file enforces required startup fields:

- `question_id`
- `selected_hub`
- `contract_ref`
- `service_family`
- `planned_artifacts`

## Modular AI Workflow Recommendations

This template supports a two-layer instruction model:

1. `copilot-instructions.md` for compact, non-negotiable governance and safety constraints.
2. `.github/instructions/*.instructions.md` for modular workflow recommendations (tool preferences, environment defaults, fallback patterns).

Why this pattern:

- Keeps the global instruction file short and stable.
- Lets users extend or swap recommendations without editing core policy.
- Preserves agent autonomy by expressing defaults as recommendations unless explicitly required.

Included starter packs:

- `.github/instructions/10-python-local-env.instructions.md`
- `.github/instructions/11-python-env-selection-from-config.instructions.md`
- `.github/instructions/12-script-location-and-rationale.instructions.md`
- `.github/instructions/20-osm-workflow-recommendation.instructions.md`
- `.github/instructions/21-data-flow-lifecycle.instructions.md`
- `.github/instructions/30-recommendation-deviation-log.instructions.md`

Add your own packs by creating new files in `.github/instructions/` with clear `description` and `applyTo` frontmatter.

Organization-level defaults can be configured in `.github/workflow-preferences.yaml`.
