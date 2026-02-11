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

# Tool 6: Basic calculator
@mcp.tool()
def calculate(expression: str) -> float:
    """Evaluates a simple mathematical expression and returns the result."""
    try:
        # Only allow safe operations
        allowed_names = {"__builtins__": {}}
        result = eval(expression, allowed_names)
        return float(result)
    except:
        return 0.0

# Tool 7: Word count
@mcp.tool()
def word_count(text: str) -> dict:
    """Returns word count statistics for the given text."""
    words = text.split()
    return {
        "total_words": len(words),
        "total_characters": len(text),
        "average_word_length": sum(len(word) for word in words) / len(words) if words else 0
    }

# Tool 8: Temperature converter
@mcp.tool()
def convert_temperature(temp: float, from_unit: str, to_unit: str) -> float:
    """Converts temperature between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == to_unit:
        return temp
    
    # Convert to Celsius first
    if from_unit == "F":
        celsius = (temp - 32) * 5/9
    elif from_unit == "K":
        celsius = temp - 273.15
    else:  # C
        celsius = temp
    
    # Convert from Celsius to target
    if to_unit == "F":
        return celsius * 9/5 + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:  # C
        return celsius

# Tool 9: List operations
@mcp.tool()
def list_operations(numbers: list[int]) -> dict:
    """Returns statistics for a list of numbers."""
    if not numbers:
        return {"error": "Empty list"}
    
    return {
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers),
        "count": len(numbers)
    }

# Tool 10: Current date and time
@mcp.tool()
def get_current_datetime() -> str:
    """Returns the current date and time as a string."""
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    # Run the MCP server (stdio transport)
    mcp.run()
