# SemanticGIS Intent-First Copilot Instructions

## Priorities

1. Clarify user intent before creating code or downloads when intent is ambiguous.
2. Prefer semantic alignment over tool convenience.
3. Record assumptions and decisions in `Design_Rationale.md`.
4. Keep public source manifests external (semanticgis.dk).
5. Keep logical sanctuary content separate from binary data storage.
6. Never print, persist, or commit real credentials.

## Contract Resolution Order (Hard Policy)

For dataset access behavior, use this resolution order before implementing fetch logic:
1. Read the local hub contract index and routing contracts declared in `.github/workflow-preferences.yaml`.
2. Resolve machine-readable contract from the mapped website hub (`semanticgis.dk` or `semanticgis.org`) only through explicitly declared contract endpoints.
3. If website contract is unavailable, use local contract snapshot if present.
4. If no snapshot exists, follow local template recommendations.
5. Only if no contract-backed solution works, design an exploratory alternative and label it explicitly as non-contract fallback.

Required
1. Do not guess endpoint/query style when a machine-readable contract is available.
2. Record contract-resolution outcome in `Design_Rationale.md` before running acquisition scripts.
3. If contract retrieval fails, record failure evidence and continue with local fallback rules.
4. Treat machine-readable contract entrypoints as contract artifacts only when they match declared contract files or dataset/service contract records.
5. Do not treat README pages, manifesto pages, bootstrap manifests, or general appendix pages as machine-readable contracts.
6. Do not probe undocumented website URLs for contracts when the local hub contract index does not declare them.

Allowed flexibility
1. The model may propose alternative methods when contracts are unavailable or contract approach fails operationally.
2. Alternative methods must include rationale, risk notes, and a path back to contract-compliant behavior.

## Leaf Realisation Selection (Hard Policy)

Many SPHERE leaves have multiple valid realisations. These must not be collapsed to one dataset automatically unless an explicit policy profile allows it.

Required
1. For a target leaf, discover realisation candidates from contract/SPHERE sources first.
2. The model may add assumption-derived candidates, but these must be clearly labeled as assumption-derived.
3. If more than one viable realisation exists, present alternatives to the user before final dataset selection.
4. Record final selection rationale in `Design_Rationale.md`.
5. An explicit user-stated dataset or realisation choice in the prompt satisfies the dataset-selection confirmation gate for that choice.

Human decision default
1. The default policy is human selection after recommendation.
2. Recommendation output must summarize semantic fit, access method, geometry implications, quality limits, and operational risk.
3. If the user already selected the dataset or realisation explicitly, do not ask again for that same decision unless a conflict or ambiguity is discovered.

Low-touch policy profiles
1. If `.github/workflow-preferences.yaml` enables a policy profile with auto-selection, the model may apply rule-based prioritization.
2. Example: municipality profile may prefer Grunddataprogrammet realisations when available.
3. Even in auto-selection mode, report alternative candidates and allow user override.

## OSM Acquisition Guardrail (Hard Policy)

For OpenStreetMap retrieval tasks, this repository enforces an OSMnx-first policy.

Required order:
1. Use OSMnx first.
2. Let OSMnx/library defaults choose endpoint behavior for normal runs.
3. Use raw Overpass only as a last resort after documented OSMnx failure evidence.

Raw Overpass fallback is allowed only when all are true:
1. OSMnx was attempted and retried according to `.github/workflow-preferences.yaml`.
2. Failure evidence is logged in `Design_Rationale.md`.
3. Fallback scope is limited to the blocked step and not made the default path.

Disallowed by default:
1. Starting with raw Overpass for standard OSM feature/network retrieval.
2. Hardcoding manual Overpass endpoints for normal runs.
3. Leaving fallback code as the primary path when OSMnx is available.

## Geometry Mode Selection (Human Decision Gate)

When multiple geometry implementations are possible (for example identity object vs geometry provider split), the model must:
1. Extract geometry options from contract sources first.
2. Present a concise recommendation table to the user with:
  - geometry option
  - semantic meaning
  - analytical implications
  - known risks/limitations
  - recommended use cases
3. Wait for user confirmation before committing to a geometry mode when options are materially different.
4. If the user has already explicitly selected a geometry mode, that satisfies the geometry confirmation gate unless the selected mode conflicts with contract semantics or task requirements.

If contract geometry guidance is unavailable, local template guidance may be used with explicit uncertainty notes.

## Project Structure Contract

- `.cache/`: ephemeral package caches (OSMnx, raster tiles, temporary downloads; gitignored)
- `00_Binary`: local binary data root (gitignored) with `raw/`, `staging/`, `derived/`
- `01_Scoping`: outline, stakeholder map, research questions
- `02_Modelling`: ontology, NOIR attribute catalog, data model diagram
- `03_Sanctuary`: logical manifests and lineage (`raw/` + `processed/` descriptors, no binary payloads)
- `04_Analytics`: analytical recipe and analysis plan
- `05_Outputs`: narrative and visual specs
- `10_scripts`: reusable project-local scripts (see `workflow-preferences.yaml` for default folder)

## Binary-Logical Separation Protocol

All projects must keep logic and binaries separate.
Never store binary dataset payloads in `03_Sanctuary`.

## Recommended Data Flow Lifecycle (All Sources)

Default lifecycle for any data source (registers, APIs, OSM, CSV, rasters, field data):
1. Download/access raw source first.
2. Document the raw source provenance.
3. Sanitize into a project-ready version (filtered, normalized, reprojected as needed).
4. Document the sanitized dataset and lineage.
5. Pause for human approval (optional quick visualization/check).
6. For multi-step analysis: write a design brief in `04_Analytics/Analytical_Recipe.md` and wait for user approval before coding.
7. Implement and run analysis from sanitized data.
8. Document analysis outputs and assumptions.
9. Pause for human approval.
10. Produce final visualizations/communication outputs.

This is the recommended default, not a hard lock.
Agents may adapt sequence or combine steps when appropriate, but should explain the rationale in `Design_Rationale.md`.

### Logical Layer (`03_Sanctuary/`)

- `03_Sanctuary/raw/` stores raw-source manifests and provenance descriptors.
- `03_Sanctuary/processed/` stores processed-layer manifests and transformation lineage.
- Logical sanctuary content may include source references (URLs, table names, connector aliases), but no secrets.

### Binary Layer (`00_Binary/`)

- `00_Binary/raw/` stores unmodified binary source data downloaded or extracted for local processing.
- `00_Binary/staging/` stores intermediate binary artifacts.
- `00_Binary/derived/` stores project-local, analysis-ready binary artifacts.
- All `00_Binary/` contents are local and gitignored except placeholder `.keep` files.

### Stage 1 — Raw

- Store the unmodified source download in `00_Binary/raw/` exactly as received.
- No reprojection, no column filtering, no geometry transformation.
- Preserve the original CRS and all original attributes.
- For each raw dataset, update or create `03_Sanctuary/raw/_manifest.md` with:
  - Filename
  - Local binary path under `00_Binary/raw/`
  - Source (URL, API, or register name)
  - Download date
  - Original CRS
  - Download tool / method
  - Licence
  - Notes (e.g., list of original attributes as they appear in the raw source)
- Raw binaries must never be overwritten by processed outputs.
- Do not document NOIR levels at the raw stage; NOIR assignment occurs during processing.

### Stage 2 — Processed

- Derive processed binaries from `00_Binary/raw/` into `00_Binary/derived/` (optionally via `00_Binary/staging/`).
- Apply reprojection, column selection, geometry normalisation, and filter rules in this stage.
- Create a processed manifest in `03_Sanctuary/processed/[dataset]_manifest.md` for each derived dataset. Include:
  - Transformation applied (e.g., CRS change, column selection, filtering rules).
  - Attribute-level NOIR levels (Nominal, Ordinal, Interval, Ratio) for all output columns.
  - Link to raw manifest row that fed this transformation.
  - Link to ontology definitions in `02_Modelling/Ontology.md`.
  - Binary path under `00_Binary/derived/`.
- Update `03_Sanctuary/Sanctuary_Index.md` to record the lineage row.
- The Sanctuary Index must record: raw manifest reference, transformation applied, processed manifest reference, NOIR coverage, and binary path.

### Enforcement rule for AI-generated scripts

Any fetch or download script must:
1. Save raw binaries to `00_Binary/raw/` first.
2. Update `03_Sanctuary/raw/_manifest.md` for provenance.
3. Transform into `00_Binary/derived/` in a separate step (may be the same script, but clearly staged).
4. Append a provenance row to `03_Sanctuary/raw/_manifest.md`.

Script responsibility boundaries must be explicit:
1. Data acquisition logic belongs in fetch/download scripts only.
2. Analytical computation belongs in analysis scripts only.
3. Mapping/chart rendering belongs in visualisation scripts only.
4. If a single orchestrator is used, it must call these stage scripts and keep stage boundaries visible.

Phase-gated delivery is required by default:
1. Do not generate all stage scripts at once unless the user explicitly requests a full pipeline.
2. Complete one stage first (script, run, checkpoint, and documentation) before authoring the next stage.
3. Wait for user confirmation after each stage checkpoint before proceeding to the next stage.
4. If downstream script design depends on upstream outputs, inspect validated outputs rather than assuming them.
5. Full end-to-end pipeline generation is allowed only when explicitly requested by the user, or after all prior stages have completed successfully and the user asks to consolidate.

Design-before-code gate for multi-step analysis:
1. Before writing any script that involves multi-step analysis, spatial joins, network modelling, or aggregation logic, first write a concise design brief in `04_Analytics/Analytical_Recipe.md`.
2. The design brief must state: what data is consumed, what operation is performed, what output is produced, and what assumptions are made.
3. Present the design brief to the user and wait for approval before implementing code.
4. Simple single-operation tasks (a straightforward fetch, a single format conversion, a quick plot) are exempt and may proceed directly to implementation.
5. After implementation, update the design brief with any deviations that occurred during coding.
6. The purpose of this gate is to give non-programmer users a readable checkpoint before code is written, since code itself is not a meaningful review artifact for this audience.

User validation checkpoints are required after each stage:
1. Print or return a concise completion summary with key output paths.
2. Include a basic sanity check signal (for example, row count, feature count, CRS, or file-exists status).
3. Stop on stage failure and report the failing stage clearly.

Checkpoint format must be consistent but format-agnostic:
1. Every stage report must include the same minimum fields:
  - stage_name
  - status (success|failed)
  - outputs (paths)
  - sanity_metrics (key-value)
  - next_expected_input (for next stage)
  - notes_for_user_validation
2. Output format is flexible (plain text block, table, JSON, YAML, or structured logs).
3. Scripts must not assume a single process framework; they should only preserve the field contract.

Script documentation for GIS users is required:
1. Explain workflow logic in domain terms (not only implementation details).
2. State where each core task is implemented (file and function/section).
3. For OSM workflows, document task logic such as key tag filters, network type assumptions, and boundary rules.

Logging behavior must support different run contexts:
1. Default to informative/verbose terminal progress for GIS users unless quiet mode is requested.
2. Allow redirecting logs to a file for long runs or debugging.
3. Allow low-noise execution for quick operations.
4. Implementation details are flexible (for example `logging` module, structured logger, or equivalent), but mode selection must be explicit.

If a script writes binary payloads into `03_Sanctuary/` or outside the workspace without explicit user request, it violates this protocol.

## Python Environment Governance

- Always use a project-local Python environment (`.venv`, `micromamba`, `conda`, or similar).
- Never install packages into the global or system Python.
- Consult `.github/workflow-preferences.yaml` for preferred manager and priority order.
- Record environment decisions in `Design_Rationale.md` when they materially affect reproducibility.

## Modular Instruction Packs

Workflow recommendations live in `.github/instructions/*.instructions.md`. These express defaults as recommendations, preserving agent autonomy. Only items marked **Required** in those packs are hard constraints. Agents may deviate from **Recommended** defaults and should log the rationale in `Design_Rationale.md`.

For OSM specifically, the rule above in "OSM Acquisition Guardrail (Hard Policy)" is a hard constraint and takes precedence over generic recommendation flexibility.

## Safety Rules

- Ask before destructive actions.
- Do not expose restricted data in outputs.
- Treat `.env` as local-only.
- Secrets policy: keep credentials, tokens, connection passwords, and private DSNs in `.env` only. Use `.env.example` as the required template for which variables must be provided.
- Never store real secrets in manifests, markdown files, scripts, notebooks, or committed config files.
- Write-boundary policy: do not write files outside the project workspace unless the user explicitly requests it.
