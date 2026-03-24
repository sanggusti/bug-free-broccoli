# Migrations

Database migration scripts for the FHIR-compliant PostgreSQL schema.

## Tool

Migrations are managed with [Alembic](https://alembic.sqlalchemy.org/).

## Usage

```bash
# Apply all pending migrations
alembic upgrade head

# Create a new migration
alembic revision --autogenerate -m "describe_change"

# Downgrade one step
alembic downgrade -1
```

## Conventions

- Each migration file must include a human-readable description in the `docstring`.
- FHIR resource tables follow the `fhir_<resource_type>` naming convention
  (e.g., `fhir_patient`, `fhir_observation`).
- Never modify an existing migration that has already been applied to production.
