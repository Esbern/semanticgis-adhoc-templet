# SemanticGIS Hub Interface Contract (v1)

This contract defines the boundary between a project created from this template and shared knowledge hosted in semanticgis.dk and semanticgis.org.

## Purpose

A project should not rediscover service type, auth mode, geometry fields, or query execution patterns at runtime. Those belong to shared source contracts on semanticgis hubs and are consumed as inputs by the local project.

## Interface Boundary

### Hub roles (shared, canonical)

- semanticgis.dk is the canonical hub for Danish register and Danish service contracts.
- semanticgis.org is the canonical hub for international and cross-country source contracts.
- OSM and satellite imagery contracts are normally resolved from semanticgis.org, even in a fully Danish project.
- A single project may use both hubs in the same workflow.

### What must live in shared hubs (canonical)

- Dataset capability catalog with service family per dataset (GraphQL, WMS, WMTS, WFS, file download), canonical endpoint URLs, and register codes/versioning.
- Query execution contracts covering pagination style and limits, required temporal arguments, filterability rules, and known error classes.
- Map-ready geometry contracts describing geometry field paths, geometry encoding, native CRS, target CRS, and transformation notes.
- Auth contracts by service type, including GraphQL conventions, map-service conventions, and token-scope caveats.
- Semantic decomposition linking leaf to dataset to service with reusable query anchors.

### What must live in the project template instance (local, execution-specific)

- User intent and scoping, including research question, area/time scope, and assumptions.
- Local credentials and runtime configuration in .env only.
- Binary data and derived artifacts under 00_Binary/.
- Local run lineage and decisions in sanctuary manifests and design rationale logs.
- Experiment outputs such as result tables, GeoJSON, web maps, and narrative exports.

## Startup Handshake (required for each new project)

At project start, the agent should resolve these checks before coding extraction logic:

1. Local hub contract index check.
2. Hub routing check.
3. Dataset capability check.
4. Query contract check.
5. Geometry contract check.
6. Geometry representation selection — enumerate available representations, present to user if multiple exist, record chosen representation and rationale.
7. Auth contract check.
8. Artifact contract check.

Expected check outputs:

- Local hub contract index check confirms which machine-readable contract endpoints are valid to fetch and which remote page classes are prohibited.
- Hub routing check assigns a source hub per source type (semanticgis.dk or semanticgis.org).
- Dataset capability check confirms service family and endpoint from hub contracts.
- Query contract check confirms pagination, required temporal args, and allowed filters.
- Geometry contract check confirms geometry field and CRS handling for map outputs.
- Geometry representation selection confirms which geometric encoding was chosen and why (point vs polygon, centroid vs footprint, point vs network centerline). If multiple representations exist and the choice materially affects downstream use, the agent must ask before proceeding.
- Auth contract check confirms auth parameter semantics per service.
- Artifact contract check predeclares expected output artifacts and schema in 03_Sanctuary/processed/.

## Minimum Project Intake Record

Create a project-local intake note that stores:

- question_id
- selected_leaf
- selected_dataset
- selected_hub
- selected_service_type
- contract_refs (URLs or local mirrored files)
- planned_outputs

## Geometry Representation Selection (required before extraction)

A single leaf may be realised by more than one dataset, and a single dataset may expose more than one geometric encoding of the same concept. These representations are not interchangeable and may be incompatible for downstream use cases.

The agent must not silently default to the first available geometry. Before writing extraction code, the representation must be declared in the intake record.

**Known representation conflicts:**

| Leaf | Representation A | Representation B | Conflict |
| --- | --- | --- | --- |
| Buildings | BBR centroid point (`byg404Koordinat`) | GeoDanmark footprint polygon | Area calculation and overlap analysis require polygons; point maps do not |
| Addresses | DAR address point | Street network centerline (DAR/DAGI) | Proximity routing requires network geometry; point snapping alone is insufficient |
| Transport networks | Road centreline (GeoDanmark) | OSM way geometry | Topology, directionality, and attribute schemas differ substantially |
| Land parcels | MAT cadastral polygon | BBR parcel centroid | Area, adjacency, and boundary analysis require polygon |
| Water bodies | Hydrosphere polygon extent | Hydrosphere centreline network | Catchment analysis requires network; coverage requires polygon |

**Required intake fields** (in `geometry_representation`):

- `available_representations` — enumerate all known alternatives from the leaf contract on the hub.
- `selected_representation_id` — the ID of the chosen representation.
- `selection_rationale` — explicit justification (e.g., "polygon required for area statistics").
- `use_case_warnings` — document what this representation cannot reliably support.

**The startup handshake must include representation selection as a confirmed step** (`representation_selection_confirmed: true`) before the geometry contract check is signed off.

## Cross-Hub Leaf Synchronisation

Leaves represent cognitive existences — conceptual entities that humans reason about (buildings, addresses, water bodies) — and are independent of any specific national data register. The same leaf concept must exist on both semanticgis.dk and semanticgis.org, linked to different realisations per hub.

Rules:

- Leaf filenames are the canonical leaf identity (`buildings.md`, `addresses.md`). Filenames must match across hubs.
- When a new leaf is created on either hub, it must be registered in `commen/leaf-registry.json` and mirrored to the other hub (even as a stub with `draft: true`).
- Realisations listed in a leaf frontmatter are hub-local. A leaf on dk lists Danish register realisations; the same leaf on org lists OSM, Copernicus, or other international realisations.
- Geometry representation tables in a leaf are also hub-local and should reflect only sources available on that hub.

## Anti-Patterns

Do not:

- Infer service type by trial-and-error during core execution.
- Probe unknown geometry fields repeatedly per project.
- Mix auth assumptions across GraphQL and map services.
- Leave output schemas implicit.

## Related Local Files

- 03_Sanctuary/semanticgis_hub_contract_index.v1.json
- 03_Sanctuary/Sanctuary_Index.md
- 03_Sanctuary/raw/_manifest.md
- 03_Sanctuary/intake/query_run_intake.template.json
- 03_Sanctuary/intake/README.md
- commen/leaf-registry.json (cross-hub leaf sync registry)
- 03_Sanctuary/processed/query_artifact_manifest.template.json
- 04_Analytics/Analytical_Recipe.md
