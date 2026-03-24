# bug-free-broccoli — FHIR-ADK Starter Project

A starter project for building a FHIR-compliant clinical data platform powered by
**Google ADK** (Agent Development Kit) as the primary agentic framework.

---

## Repository Structure

```
bug-free-broccoli/
├── app/                  # Core application code
│   └── mcp/              # MCP server — exposes FHIR resources to ADK agents
├── web/                  # Web frontend (placeholder)
├── packages/             # Shared packages
│   └── migrations/       # Database migration scripts (Alembic)
├── scripts/              # Utility scripts
│   ├── eval/             # Evaluation harnesses
│   ├── runs/             # Experiment run management
│   ├── prompt/           # Prompt templates and helpers
│   └── configs/          # Configuration files
└── specs/                # Specification and tracking documents
    ├── requirements.md   # Functional & non-functional requirements
    ├── stages.md         # Development stages and milestones
    └── progress.md       # Current progress tracker
```

---

## Technology Stack

| Layer         | Technology |
|---------------|------------|
| Agentic framework | [Google ADK](https://google.github.io/adk-docs/) |
| Agent–tool protocol | [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) |
| Clinical data standard | [HL7 FHIR R4](https://hl7.org/fhir/R4/) |
| Database      | PostgreSQL (FHIR-compliant schema) |
| Migrations    | [Alembic](https://alembic.sqlalchemy.org/) |
| Language      | Python 3.11+ |

---

## Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/sanggusti/bug-free-broccoli.git
cd bug-free-broccoli

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate

# 3. Install dependencies (once requirements.txt is populated)
pip install -r requirements.txt
```

See [`specs/stages.md`](specs/stages.md) for the development roadmap and
[`specs/progress.md`](specs/progress.md) for current status.
