# Modular Workflow Recommendations

This folder lets template users add workflow recommendations without modifying the root `copilot-instructions.md`.

## Design intent

- Keep `copilot-instructions.md` focused on non-negotiable governance and safety rules.
- Put tool and method preferences in small, replaceable `*.instructions.md` files.
- Treat recommendations as defaults, not hard locks, unless explicitly marked as required.

## How to add a recommendation pack

1. Create a new file in this folder, e.g. `30-your-topic.instructions.md`.
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

Use `.github/workflow-preferences.yaml` for organization-level defaults (for example Python manager priority, GIS-specific preference, and OSM retrieval defaults).

- Keep hard constraints in instruction files (`Required`).
- Keep tunable defaults in the preferences YAML.
- Let agents follow YAML defaults unless they conflict with a hard constraint.

Current configurable domains include Python environment selection, OSM workflow defaults, and script location/rationale behavior.
