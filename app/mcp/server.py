"""
MCP server entry-point for the FHIR-ADK project.

This module wires up MCP tools and resources so that ADK agents can
interact with a FHIR-compliant database via the Model Context Protocol.

Usage:
    python -m app.mcp.server
"""

from __future__ import annotations


def create_server():
    """Create and configure the MCP server instance.

    Returns:
        A configured MCP server ready to be run.
    """
    # TODO: initialise MCP server with FHIR tools and resources
    raise NotImplementedError("MCP server not yet implemented")


if __name__ == "__main__":
    server = create_server()
    server.run()
