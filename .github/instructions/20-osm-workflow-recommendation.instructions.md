---
description: "Workflow recommendation for OpenStreetMap data acquisition and analysis in this template. Use when sourcing OSM for mobility or accessibility tasks."
applyTo: "**/*.{py,ipynb,md}"
---

# OSM Workflow Recommendation

Recommended
- Prefer `OSMnx` as the default OSM acquisition path for Python-based analysis.
- Configure OSMnx to cache into the project `.cache/` folder: `ox.settings.cache_folder = ".cache/"`.
- Let library defaults choose the Overpass endpoint unless there is a documented reason to override.
- Treat direct `curl` + raw Overpass queries as last-resort only.
- Keep OSM workflows split into stage scripts where practical:
	- fetch/download
	- analysis/modeling
	- visualisation/export
- Deliver OSM workflows stage-by-stage by default, not as a pre-authored full pipeline.

Required
- OSM acquisition order is mandatory:
	1. Use `osmnx` first.
	2. Allow OSMnx/library defaults to choose endpoint.
	3. Use raw Overpass only if OSMnx fails after required retries.
- Store raw binaries in `00_Binary/raw/` first.
- Keep `03_Sanctuary/` logical-only (manifests, lineage, descriptors), with no binary payloads.
- Log provenance in `03_Sanctuary/raw/_manifest.md` and lineage in `03_Sanctuary/Sanctuary_Index.md`.
- Do not generate downstream OSM stage scripts before the prior stage has completed and been validated.
- Wait for user confirmation between OSM stages unless the user explicitly requests full pipeline creation.
- After each OSM stage, emit a user validation checkpoint including output paths and at least one sanity metric.
- Document OSM task logic in user-facing terms, including:
	- key tag filters or query scope
	- network type assumptions (walk, bike, drive)
	- geometry/boundary clipping rules
	- where this logic is implemented in script files
- For any fallback to raw Overpass, log all of the following in `Design_Rationale.md` before writing fallback code:
	- timestamp
	- attempted OSMnx method and parameters
	- observed failure (for example 429/timeout/parse error)
	- number of retries performed
	- why fallback is necessary for this stage
	- planned return path to OSMnx-first behavior

Prohibited
- Do not start with raw Overpass when the task can be done with OSMnx.
- Do not hardcode manual Overpass endpoints for normal runs.
- Do not keep raw Overpass fallback code as the default execution path.

Fallback
- If OSMnx retrieval fails or rate limits persist:
	1. Retry using OSMnx at least twice with backoff.
	2. Capture failure evidence in `Design_Rationale.md`.
	3. Use raw Overpass only for the blocked scope, then return to OSMnx-first path.
