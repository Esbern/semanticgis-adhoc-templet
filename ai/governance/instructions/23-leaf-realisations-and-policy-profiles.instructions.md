---
description: "Selecting datasets from leaves with alternative realisations, including human decision gates and optional low-touch policy profiles."
applyTo: "**/*.{py,ipynb,md,yml,yaml,json}"
---

# Leaf Realisations and Policy Profiles

Required
- Resolve candidate realisations for the target SPHERE leaf from contract-backed sources first.
- Do not reduce multiple viable realisations to a single dataset by default.
- Present the user with a recommendation table when alternatives exist.
- Label any non-contract candidate as assumption-derived.
- Record final dataset-selection rationale in `Design_Rationale.md`.
- Treat an explicit user-stated dataset or realisation choice as satisfying the dataset-selection gate for that choice.

Recommendation table (minimum columns)
- realisation_id
- source_collection
- access_method
- semantic_fit_summary
- geometry_mode
- quality_or_currency_notes
- operational_risk
- recommendation_level

Decision flow
1. Discover contract-backed candidates.
2. Add assumption-derived candidates only if helpful and clearly labeled.
3. Apply policy profile from `.github/workflow-preferences.yaml`.
4. If profile is human-first, request user decision unless the user already made that decision explicitly.
5. If profile is auto-select, apply profile rule, report skipped alternatives, and allow override.

Low-touch municipal profile guidance
- For municipal workflows, policy profile `municipality_grunddata_first` may auto-prefer Grunddataprogrammet realisations.
- This profile must still report alternatives and maintain override support.

Fallback
- If contract-backed candidates cannot be resolved, continue with local template guidance and explicit uncertainty notes.
- If no documented solution works, propose alternative acquisition methods and request user confirmation before execution.

Notes
- Explicit dataset choice does not bypass access-contract rules.
- Explicit dataset choice does not bypass geometry review when materially different geometry modes remain unresolved.
