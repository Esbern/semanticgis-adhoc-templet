# SemanticGIS AI Governance Adapter (Copilot)

Use the canonical, platform-agnostic governance source in `ai/governance/`.

## Load order

1. Read `ai/governance/root-policy.md` first.
2. Apply domain instructions from `ai/governance/instructions/*.instructions.md`.
3. Use defaults from `ai/governance/workflow-preferences.yaml`.
4. Use website machine-readable contracts from `semanticgis.dk` and `semanticgis.org` for data-specific semantics.

## Local override guardrails

Allow local override only when all are true:

1. The user explicitly approves the override.
2. Reason, scope, and rollback criteria are logged in `Design_Rationale.md`.
3. Override scope is limited to the current task/job unless the user explicitly broadens it.

## Compatibility note

`.github/instructions/` and `.github/workflow-preferences.yaml` are compatibility mirrors during migration.
