# SemanticGIS Small Template

This repository is a lightweight template designed for students and ad-hoc GIS work. It supports many isolated analyses running in a single repository and embraces "Human-in-the-Loop" workflows (mixing AI scripts with manual QGIS editing).

## Included Scaffold

- `README.md`
- `ai/governance/` — Canonical AI governance, instruction packs, and workflow defaults
- `copilot-instructions.md`, `CLAUDE.md`, `GEMINI.md` — Thin AI-specific adapters to the canonical governance
- `.gitignore`
- `.env.example`
- `data/`
  - `raw/` — AI downloads raw SemanticGIS data here
  - `edits/` — Processed data and human-edited QGIS shapes go here
- `jobs/` — Directory for independent analysis tasks

## Design Philosophy

This template is built for **agile, ad-hoc agentic AI-assisted GIS work**.

- **Many Jobs, One Repo:** You can create many independent folders inside `jobs/` (e.g., `jobs/refshaleoen_cultural_hub`, `jobs/park_buffers`).
- **Human-in-the-Loop:** We encourage workflows where the AI downloads data, you manually edit it in QGIS, and the AI picks it up for further analysis.
- **Data Genesis Protocol:** Instead of a complex central data model, we use a decentralized `-dg.md` protocol. Every dataset inside `data/` must have a corresponding `<filename>-dg.md` describing its provenance, layer structure, and edits.
- **SemanticGIS Enforced:** The AI will still consult the official `semanticgis.dk` and `semanticgis.org` indexes to find appropriate datasets and join logic.

## Quick Start

1. Create a new repository from this template.
2. Copy `.env.example` to `.env` and fill local values.
3. Open the project in an AI-enabled editor or assistant environment.
4. Start a chat with the AI, pasting the Onboarding Prompt below.
5. Ask the AI to start a new job in the `jobs/` directory.

### Onboarding Prompt (paste this first)

> Please read `ai/governance/root-policy.md`, the relevant adapter file for your assistant, and `README.md` thoroughly. Ensure you understand the Data Genesis (`-dg.md`) protocol, the human-in-the-loop workflow, and how you must use the SemanticGIS indexes. Acknowledge that you are ready to start.

### Example Human-in-the-Loop Workflow

**User:** "Download the OSM polygons for Refshaleøen and save it to `data/raw`. I will then manually delineate the cultural hub in QGIS and save it to `data/edits`."

*AI downloads the data, generates the `-dg.md` file, and pauses.*

**User:** "I have saved the edited shape to `data/edits/cultural_hub.gpkg`. Now, query the Danish CVR for all businesses within this shape."

*AI detects the new file, asks the user to describe what edits were made so it can generate the `-dg.md` file, and then writes the python script to perform the join.*
