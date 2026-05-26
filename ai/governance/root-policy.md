# Root Policy

This file defines cross-cutting hard policy for all AI assistants used in this repository.

## Core principles

1. Clarify user intent before creating code or downloads when intent is ambiguous.
2. Prefer semantic alignment over tool convenience.
3. Embrace human-in-the-loop workflows and stop when manual GIS edits are required.
4. Keep public source manifests external (`semanticgis.dk` / `semanticgis.org`).
5. Never print, persist, or commit real credentials.

## Hard requirements

- Contract-first behavior: resolve machine-readable contract guidance before designing data access logic.
- No-guessing behavior: do not invent endpoint/query styles when contract guidance exists.
- Data Genesis behavior: each dataset under `data/raw/` or `data/edits/` requires a matching `<filename>-dg.md` provenance file.
- Local Python only: use a project-local Python environment; do not install to global/system Python.

## Logging split

- `-dg.md` files store dataset provenance, lineage, layers, and edit history.
- `Design_Rationale.md` stores decision logs, deviations, fallback evidence, and override rationale.

## Local override policy

Local instruction overrides are allowed only when all conditions are met:

1. The user explicitly approves the override.
2. Reason, scope, and rollback criteria are recorded in `Design_Rationale.md`.
3. The override applies only to the current task/job unless the user explicitly broadens scope.

## Canonical details

Detailed operational rules live in `ai/governance/instructions/*.instructions.md`.
Defaults live in `ai/governance/workflow-preferences.yaml`.
