# Processed Data

Processed outputs suitable for analysis and reproducible workflows.

## How to use this folder

For each derived dataset, create a manifest file named `[dataset]_manifest.md` that documents:

- **Transformation applied** — CRS reprojection, column selection, filtering rules, geometry normalisation.
- **Attribute-level NOIR levels** — Classify every output column as Nominal, Ordinal, Interval, or Ratio.
- **Raw manifest link** — Reference the source row in `03_Sanctuary/raw/_manifest.md`.
- **Ontology link** — Map attribute semantics to definitions in `02_Modelling/Ontology.md`.
- **Binary path** — Location of the derived file under `00_Binary/derived/`.

After creating a processed manifest, add a lineage row to `03_Sanctuary/Sanctuary_Index.md`.

### Template

```markdown
# [Dataset Name] — Processed Manifest

## Source
- Raw manifest ref: `raw/_manifest.md` row N
- Raw binary path: `00_Binary/raw/[filename]`

## Transformation
- Reprojected from EPSG:XXXX to EPSG:XXXX
- Columns selected: ...
- Filter rules: ...

## Attributes (NOIR)

| Attribute | Type | NOIR Level | Ontology Ref |
|---|---|---|---|
| `column_name` | text / int / float / geometry | Nominal / Ordinal / Interval / Ratio | `Ontology.md#entity` |

## Output
- Binary path: `00_Binary/derived/[filename]`
- CRS: EPSG:XXXX
- Row count: N
```
