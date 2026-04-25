# Query Run Intake Records

Use one intake file per query run to lock key routing and execution choices before coding.

## Required workflow

1. Copy `query_run_intake.template.json`.
2. Save as `query_run_intake.<question_id>.<run_id>.json`.
3. Fill required fields before script implementation.
4. Set startup check flags to `true` only after each check is confirmed.
5. Keep intake files in this folder for traceability.

## Minimum required fields

- `question_id`
- `selected_hub`
- `contract_ref`
- `service_family`
- `planned_artifacts`

## Example filename

`query_run_intake.q-2026-04-22-lejre-residential.v1.json`
