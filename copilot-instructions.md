# SemanticGIS Intent-First Copilot Instructions (Ad-Hoc Template)

## Priorities

1. Clarify user intent before creating code or downloads when intent is ambiguous.
2. Prefer semantic alignment over tool convenience.
3. Embrace **Human-in-the-Loop workflows**. Stop and wait when manual GIS edits are required.
4. Keep public source manifests external (semanticgis.dk).
5. Never print, persist, or commit real credentials.

## Contract Resolution Order (Hard Policy)

For dataset access behavior, use this resolution order before implementing fetch logic:
1. Search and read the machine-readable contract from the website hubs (`semanticgis.dk` or `semanticgis.org`).
2. Discover datasets through the SemanticGIS `sphere-index.v1.json` or by reading the `Leaf` and `Realisation` files in the hubs.
3. Do not guess endpoint/query styles. You must use the officially prescribed joins and realisations from the hubs.

## The Data Genesis Protocol (Hard Policy)

Because this template is meant for ad-hoc exploration, we do not maintain a rigid central "Common Data Model". Instead, we use a decentralized **Data Genesis Protocol** to track provenance.

1. **Every dataset** placed in `data/raw/` or `data/edits/` must have a corresponding markdown file right next to it, named `<filename>-dg.md` (e.g., `cultural_hub.gpkg-dg.md`).
2. This `-dg.md` file must document:
   - **Provenance**: Where did the data come from? (e.g., URL, SemanticGIS Realisation ID).
   - **Creation History**: Was it created by an AI script, or by a human editing in QGIS?
   - **Layers**: If it is a GeoPackage with multiple layers, list the layers.
   - **Edits made**: What specific filters or manual boundary drawings were performed?
3. **AI Generation**: If you (the AI) write a script that generates a dataset, you must also generate its `-dg.md` file.
4. **Human Injection**: If the human user drops a file into `data/edits/` and the `-dg.md` file does not exist, **you must immediately prompt the human** asking them to describe what edits they made, so that you can create the `-dg.md` file for them.

## Human-in-the-Loop Workflows

This template assumes that users will frequently drop out of the AI workflow to perform manual spatial edits (e.g., drawing buffers, deleting stray polygons, cleaning topologies) in desktop software like QGIS.

1. Do not attempt to write complex topological cleaning scripts if a human user explicitly states they want to do it manually.
2. When the user says they will edit a file, **pause your execution** and wait for them to confirm they have saved the file to `data/edits/`.
3. Do not treat `data/edits/` as exclusively AI-generated. It is a shared space.

## Project Structure Contract

- `data/`
  - `raw/`: Raw source data downloaded without modification.
  - `edits/`: Both human-edited files and AI-processed subsets go here.
- `jobs/`: Each ad-hoc analysis task must be created as its own isolated directory inside `jobs/` (e.g., `jobs/refshaleoen_hub/`).
- Scripts inside a job folder should use relative paths to reference the global `data/` directory.

## Python Environment Governance

- Always use a project-local Python environment (`.venv`, `micromamba`, `conda`, or similar) installed at the root of the repository.
- Never install packages into the global or system Python.

## Safety Rules

- Ask before destructive actions.
- Do not expose restricted data in outputs.
- Treat `.env` as local-only. Keep credentials, tokens, connection passwords, and private DSNs in `.env` only. Use `.env.example` as the required template for which variables must be provided.
- Never store real secrets in manifests, `-dg.md` files, scripts, notebooks, or committed config files.
