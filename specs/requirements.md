# Requirements

## Functional Requirements

### FR-01 — FHIR Database
- The system must store and retrieve clinical data using a FHIR R4-compliant schema.
- Supported resource types (initial scope): `Patient`, `Observation`, `Condition`,
  `MedicationRequest`, `Encounter`.

### FR-02 — MCP Server
- The MCP server must expose FHIR resources as tools consumable by ADK agents.
- Tools must support read, search, and write operations on FHIR resources.

### FR-03 — ADK Agents
- At least one ADK agent must be able to query and reason over FHIR resources via MCP.
- The agent must produce structured outputs aligned with FHIR data models.

### FR-04 — Database Migrations
- All schema changes must be version-controlled via migration scripts in `packages/migrations/`.
- Migrations must be idempotent and reversible.

### FR-05 — Scripts
- Evaluation scripts must benchmark agent outputs against curated FHIR test cases.
- Run scripts must persist experiment metadata for reproducibility.

---

## Non-Functional Requirements

### NFR-01 — Security
- No PHI (Protected Health Information) must be committed to source control.
- All secrets must be managed via environment variables or a secrets manager.

### NFR-02 — Observability
- All agent runs must emit structured logs and metrics.

### NFR-03 — Reproducibility
- Every experiment run must be fully reproducible given the same config and seed data.

### NFR-04 — Interoperability
- The FHIR schema must conform to the HL7 FHIR R4 specification.
