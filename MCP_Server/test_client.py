# dummy_llm_client.py
"""
A simple LLM client demonstrating MCP integration.
Uses LangChain's MultiServerMCPClient to call tools from the dummy MCP server.
"""

import asyncio
import sys
from pathlib import Path
from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
import json

def extract_text(result):
    """
    Clean MCP tool output to plain Python types.
    MCP returns a list of dicts with metadata, we only extract the 'text'.
    If the text is a JSON string, parse it.
    """
    if not result:
        return None
    text = result[0].get("text")
    try:
        return json.loads(text)  # convert JSON string to Python dict
    except Exception:
        return text

async def main():
    here = Path(__file__).resolve().parent
    mcp_server_path = here / "dummy_mcp_server.py"

    # Configure MCP client to start the server using stdio transport
    client = MultiServerMCPClient(
        {
            "dummy": {
                "transport": "stdio",
                "command": sys.executable,
                "args": [str(mcp_server_path)],
            }
        }
    )

    # Load all available tools from the MCP server
    tools = await client.get_tools()
    print("Loaded tools:", [t.name for t in tools])

    # Create LLM agent (ChatOllama) using the loaded tools
    llm = ChatOllama(model="llama3.2:1b", temperature=0)
    agent = create_agent(llm, tools)

    # Example 1: Ask the LLM agent to use a tool
    response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "Use the reverse_string tool on 'MCP' and tell me the result."}]}
    )
    print("LLM agent response:", response["messages"][-1].content)

    # Example 2: Directly call a tool (without LLM)
    reverse_tool = next(t for t in tools if t.name == "reverse_string")
    result = await reverse_tool.ainvoke({"text": "SEMAISTEK"})
    print("Direct tool result:", extract_text(result))

if __name__ == "__main__":
    asyncio.run(main())
