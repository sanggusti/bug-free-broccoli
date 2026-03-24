# MCP — Model Context Protocol Server

This sub-directory contains the MCP server that exposes FHIR resources as tools and
resources consumable by ADK (Agent Development Kit) agents.

## Responsibilities

- Define MCP tools for CRUD operations on FHIR resources (Patient, Observation, etc.)
- Provide resource endpoints that surface FHIR bundles
- Handle authentication / authorization against the FHIR server

## Getting Started

```bash
# Install dependencies (from repo root)
pip install -r requirements.txt

# Run the MCP server
python -m app.mcp.server
```
