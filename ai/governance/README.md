# AI Governance (Canonical)

This directory is the canonical, platform-agnostic source for AI workflow governance in this template.

## Purpose

- Keep policy independent of Git hosting platform (`github.com`, self-hosted GitLab, or other servers).
- Keep policy independent of assistant provider (Copilot, Claude, Gemini, and others).
- Provide one place to maintain governance so adapters do not drift.

## Precedence

1. Root policy in `ai/governance/root-policy.md`
2. Domain packs in `ai/governance/instructions/*.instructions.md`
3. Defaults in `ai/governance/workflow-preferences.yaml`
4. Website machine-readable contracts (`semanticgis.dk` / `semanticgis.org`) for data-specific semantics

Local override is allowed only when explicitly user-approved and logged in `Design_Rationale.md` with reason, scope, and rollback criteria.

## Layout

- `root-policy.md`: cross-cutting hard policy
- `instructions/`: domain-specific operational packs
- `workflow-preferences.yaml`: tunable defaults

## Compatibility

- `copilot-instructions.md`, `CLAUDE.md`, and `GEMINI.md` are thin adapters.
- `.github/instructions/` and `.github/workflow-preferences.yaml` are compatibility mirrors during migration.
