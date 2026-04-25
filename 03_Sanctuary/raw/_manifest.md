# Raw Data Manifest

This file is a logical provenance register for raw datasets.
- Unmodified source binaries are stored in `00_Binary/raw/` exactly as downloaded or received.
- No reprojection, column filtering, or geometry transformation occurs in the raw stage.
- All original attributes and the original CRS are preserved in the binary raw copy.
- Each raw binary file is logged in the table below before any processing begins.

Derived binary layers are stored in `00_Binary/derived/` (optionally via `00_Binary/staging/`).
The Sanctuary Index (`03_Sanctuary/Sanctuary_Index.md`) records transformation lineage from raw binaries to derived outputs.
`03_Sanctuary/` remains logical-only (manifests, lineage, semantic descriptors) and must not contain binary payloads.

## Provenance Log

Document each raw binary file with full source provenance. Include original CRS, attributes, and metadata.
For attribute-level detail and NOIR levels, see the corresponding processed manifest in `03_Sanctuary/processed/`.

| Filename | Binary Path | Source | Download date | Original CRS | Tool / method | Licence | Notes |
|---|---|---|---|---|---|---|---|
| `network_raw.shp` | `00_Binary/raw/network_raw.shp` | *example:* https://download.example.org/network_v1.zip | 2026-04-01 | EPSG:4326 | `curl` + unzip | CC-BY 4.0 | Original attributes: `id`, `name`, `road_type`, `speed_limit`, `surface` |
| | | | | | | | |
