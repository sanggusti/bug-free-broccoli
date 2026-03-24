# Development Stages

## Stage 0 — Project Bootstrap ✅
**Goal:** Establish the project skeleton and repository structure.

- [x] Create top-level directories: `app/`, `web/`, `packages/`, `scripts/`, `specs/`
- [x] Add README files for every directory
- [x] Define initial requirements and stages
- [x] Set up `.gitignore` for Python projects

---

## Stage 1 — Database Foundation 🔲
**Goal:** Stand up a FHIR-compliant database with migration tooling.

- [ ] Choose database backend (PostgreSQL recommended)
- [ ] Scaffold Alembic migration environment in `packages/migrations/`
- [ ] Author initial migration: core FHIR resource tables
- [ ] Write integration tests for migrations

---

## Stage 2 — MCP Server 🔲
**Goal:** Expose FHIR resources over the Model Context Protocol.

- [ ] Select and install MCP SDK
- [ ] Implement MCP tools: `get_patient`, `search_observations`, `create_resource`, etc.
- [ ] Implement MCP resources: FHIR bundles as readable resources
- [ ] Write unit tests for each tool
- [ ] Document tool schema in `app/mcp/README.md`

---

## Stage 3 — ADK Agent Integration 🔲
**Goal:** Build an ADK agent that reasons over FHIR data via MCP.

- [ ] Scaffold ADK project structure
- [ ] Configure ADK to use the MCP server as a tool provider
- [ ] Develop prompt templates in `scripts/prompt/`
- [ ] Author first agent: clinical data summarisation
- [ ] Evaluate agent performance with `scripts/eval/`

---

## Stage 4 — Web Frontend 🔲
**Goal:** Provide a minimal web UI for interacting with the ADK agent.

- [ ] Choose frontend framework
- [ ] Implement chat / query interface
- [ ] Connect frontend to MCP / ADK backend

---

## Stage 5 — Hardening & Observability 🔲
**Goal:** Make the system production-ready.

- [ ] Add structured logging across all components
- [ ] Set up metrics and tracing
- [ ] Security review (PHI handling, auth, secrets)
- [ ] Performance benchmarking with the eval harness
- [ ] Documentation pass
