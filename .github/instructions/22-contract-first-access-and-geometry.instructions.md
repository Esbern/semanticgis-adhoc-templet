---
description: "Contract-first dataset access resolution and geometry option handling. Use for any data acquisition or geometry-dependent workflow."
applyTo: "**/*.{py,ipynb,md,yml,yaml,json}"
---

# Contract-First Access and Geometry

Required
- Read local contract index `03_Sanctuary/semanticgis_hub_contract_index.v1.json` first.
- Resolve dataset access strategy from machine-readable contract sources first.
- Use source-type hub routing from `.github/workflow-preferences.yaml` to decide whether to consult `semanticgis.dk` or `semanticgis.org`.
- Use declared contract entrypoints and explicit contract artifacts first; do not substitute human-oriented hub pages.
- If website contract cannot be resolved:
  - use local contract snapshot if present
  - otherwise use local template recommendations
  - only then design exploratory fallback access logic
- Log contract resolution result in `Design_Rationale.md` before implementing acquisition calls.
- When exploratory fallback is used, mark it explicitly as non-contract mode and include rollback criteria.

Required (No guessing rule)
- Do not guess API style, endpoint family, or query syntax if a contract is available.
- For Datafordeler/BBR-like sources with GraphQL contract, do not substitute guessed REST/Overpass-style access patterns.
- Do not treat bootstrap manifests, manifesto pages, README pages, or generic appendix pages as machine-readable contracts.
- Do not probe undocumented remote URLs when the local hub contract index does not declare a valid machine-readable contract endpoint.

Geometry handling
- If multiple geometry implementations exist, produce a recommendation table for human review before selecting one.
- Include at minimum:
  - option identifier
  - semantic interpretation
  - geometry type/CRS expectations
  - analysis consequences
  - known risks
  - recommended scenarios
- Wait for user confirmation when geometry choice changes analytical meaning.

Fallback
- If contract retrieval repeatedly fails due to network or missing docs, proceed using local template guidance and clearly state uncertainty boundaries.
- If documented approach fails in practice, propose an alternative with explicit risk and validation checks, then request user confirmation for that deviation.
