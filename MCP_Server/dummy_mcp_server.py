# dummy_mcp_server.py
"""
A dummy MCP server with multiple tools to demonstrate LLM integration.
All outputs are basic Python types: int, str, bool, dict.
"""

import random
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("dummy-llm-mcp")

# Tool 1: Generate a random integer
@mcp.tool()
def random_number(min_val: int = 0, max_val: int = 100) -> int:
    """Returns a random number between min_val and max_val."""
    return random.randint(min_val, max_val)

# Tool 2: Reverse a string
@mcp.tool()
def reverse_string(text: str) -> str:
    """Returns the reversed string."""
    return text[::-1]

# Tool 3: Check if a number is even
@mcp.tool()
def is_even(n: int) -> bool:
    """Returns True if the number is even, False otherwise."""
    return n % 2 == 0

# Tool 4: Look up country capital
@mcp.tool()
def get_country_capital(country: str) -> str:
    """Returns the capital of a given country."""
    capitals = {"Switzerland": "Bern", "France": "Paris", "Germany": "Berlin"}
    return capitals.get(country, "Unknown")

# Tool 5: Analyze a string and return metadata
@mcp.tool()
def analyze_text(text: str) -> dict:
    """Returns a dictionary with length and whether 'MCP' is contained in the text."""
    return {"length": len(text), "contains_MCP": "MCP" in text}

if __name__ == "__main__":
    # Run the MCP server (stdio transport)
    mcp.run()
