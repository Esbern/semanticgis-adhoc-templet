# Modular Workflow Recommendations (Compatibility Mirror)

This folder is a compatibility mirror during migration.

Canonical source: `ai/governance/instructions/`

## Design intent

- Keep adapter files focused on load order and guardrails.
- Keep tool and method preferences in canonical `ai/governance/instructions/*.instructions.md` files.
- Treat recommendations as defaults, not hard locks, unless explicitly marked as required.

## How to add a recommendation pack

1. Create or update files in `ai/governance/instructions/`, not this mirror.
2. Add YAML frontmatter with `description` and `applyTo`.
3. Use concise language and priority levels:
   - `Required`: hard constraints.
   - `Recommended`: preferred default, may be overridden with rationale.
   - `Fallback`: what to do when the preferred route fails.
4. Keep each pack short and single-purpose.

## Frontmatter template

```md
---
description: "Use when ..."
applyTo: "**/*"
---
```

## Naming convention

- Prefix with two digits to control reading order: `10-...`, `20-...`, `30-...`.
- One topic per file to avoid giant instruction documents.

## Repository Preferences File

Canonical defaults live in `ai/governance/workflow-preferences.yaml`.

Use `.github/workflow-preferences.yaml` as a compatibility mirror only.

- Keep hard constraints in instruction files (`Required`).
- Keep tunable defaults in the preferences YAML.
- Let agents follow YAML defaults unless they conflict with a hard constraint.

Current configurable domains include Python environment selection, OSM workflow defaults, and script location/rationale behavior.
