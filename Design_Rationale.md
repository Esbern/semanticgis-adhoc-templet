# Design Rationale

Use this file as a living argumentation log for project decisions.

## Phase Protocol Focus (Start Here)

Use this section to guide what to document in each project phase.

### Phase 1: Scoping Protocol

- Deconstruct the brief into grounded geospatial questions.
- Classify epistemic mode: heuristic or teleological.
- Identify omissions and likely biases (the "invisible" phenomena).
- Map stakeholders, tooling constraints, and delivery constraints.
- Record governance, ethics, and privacy strategy.

### Phase 2: Data Modelling Protocol

- Identify entities (tangible and functional).
- Define representation (object vs field).
- Resolve boundary rules for fuzzy social or spatial entities.
- Assign NOIR levels for key attributes.
- Define temporality (seasonal/hourly/existence rules).

### Phase 3: Data Sanctuary Protocol

- Inventory candidate sources (registers, field notes, external sources).
- Apply the evaluation matrix: Accept, Transform, Reject.
- Document sanitisation rituals (joins, geocoding, overlays, recoding).
- Record procurement of primary data when source gaps remain.
- Manifest each grounded dataset with provenance and rationale.
- Follow the two-stage pipeline with strict separation of concerns:
	- Store unmodified source binaries in `00_Binary/raw/` first.
	- Derive analysis-ready binaries into `00_Binary/derived/` (optionally via `00_Binary/staging/`).
	- Keep `03_Sanctuary/` logical-only (manifests, lineage, semantic descriptors), with no binary payloads.
	- Log raw provenance in `03_Sanctuary/raw/_manifest.md` and record transformation lineage in `03_Sanctuary/Sanctuary_Index.md`.

### Protocol Logging Template

Use this template for each phase pass:

#### Phase Log Entry

- Phase:
- Date:
- Issue:
- Protocol steps applied:
- Decision:
- Evidence / sources:
- Consequences:
- Backflow triggered (yes/no):
- If yes, which prior phase is affected:

## Problem Frame

- Project semantic id:
- Project title:
- Scientific intent:
- Practical intent:

## Key Decisions

### Decision 001
- Issue:
- Position:
- Arguments:
- Consequences:

## Assumptions

- 

## Open Questions

- 

## Script Logic Registry

Use this section when adding or changing reusable scripts.

### Script Entry Template

- Date:
- Script path:
- Purpose:
- Inputs:
- Outputs:
- Core logic:
- Dependencies / environment assumptions:
- Reusability notes:
