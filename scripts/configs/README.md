# Configs

Configuration files and config-loading helpers for the FHIR-ADK project.

## Purpose

- Centralise all runtime configuration (database URLs, model endpoints, ADK settings)
- Provide environment-specific overrides (dev / staging / prod)
- Keep secrets out of source control — use `.env` files or a secrets manager

## Files

| File                  | Purpose |
|-----------------------|---------|
| `base_config.yaml`    | Shared defaults for all environments |
| `dev_config.yaml`     | Development overrides |
| `prod_config.yaml`    | Production overrides |

## Conventions

- Never commit secrets or credentials.
- Prefer YAML for structured config and `.env` for secrets.
