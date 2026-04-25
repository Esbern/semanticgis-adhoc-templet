# Sanctuary Index

Track project-local datasets and transformation lineage from raw to processed binaries.

## Transformation Lineage Log

This table documents each dataset journey through the processing pipeline, linking raw manifests to processed outputs and recording applied transformations.

| Raw Manifest Ref | Transformation Applied | Processed Manifest Ref | Binary Path (derived) | NOIR Coverage | Date |
|---|---|---|---|---|---|
| `raw/_manifest.md` row N | e.g. "reproject to EPSG:25832, filter by boundary, harmonize columns" | `processed/[dataset]_manifest.md` | `00_Binary/derived/[filename]` | *See processed manifest* | YYYY-MM-DD |

## Usage

- One row per dataset transformation.
- Link to specific row numbers in raw manifest.
- Reference processed manifest for attribute-level NOIR levels and lineage detail.
- Update this index whenever a new processed dataset is derived.
