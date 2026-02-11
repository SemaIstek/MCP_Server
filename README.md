# MCP_Server

A Model Context Protocol (MCP) Server implementation for training purposes.

## Overview

This project demonstrates how to create and integrate an MCP Server with various components including:
- RAG (Retrieval-Augmented Generation) implementation
- LangChain integration
- Ollama model support
- Data preprocessing and embedding storage

## Project Structure

```
MCP_Server/
├── MCP/
│   ├── load_data.py          # Data loading utilities
│   ├── preprocess.py         # Data preprocessing pipeline
│   ├── embedding_store.py    # Vector embedding storage and retrieval
│   ├── rag_query.py          # RAG query interface
│   └── main.py               # Main entry point
├── MCP_Server/
│   ├── dummy_mcp_server.py   # MCP Server implementation
│   └── test_client.py        # Test client for MCP Server
├── Notebooks/
│   ├── ollama_course.ipynb   # Ollama course materials
│   └── langchain_retrieval.ipynb
├── assets/
│   ├── filtered_dataset.csv  # Training data
│   └── retrieval_resources/
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.8+
- Ollama (for model inference)
- LangChain
- langchain-mcp-adapters
- Required dependencies listed below

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd MCP_Server
```

2. Install dependencies:
```bash
pip install langchain-ollama langchain-mcp-adapters langchain
```

3. Set up Ollama and pull a model:
```bash
ollama pull llama3.2:1b
```

## Usage

### Running the MCP Server

Start the MCP server:
```bash
python MCP_Server/dummy_mcp_server.py
```

### Testing with the Client

Run the test client to verify the server:
```bash
python MCP_Server/test_client.py
```

This will:
- Load available tools from the MCP server
- Demonstrate LLM agent integration with tools
- Show direct tool invocation

### Running RAG Queries

Use the RAG implementation to perform retrieval-augmented generation:
```bash
python MCP/rag_query.py
```
Perform retrieval-augmented generation using embeddings

Uses custom National Disaster dataset for demonstration

ℹ️ Note: The National Disaster dataset used in this project is included in assets/filtered_dataset.csv. You can access and explore it directly for experimentation.
## Available Tools

The MCP server provides the following tools for LLM integration:

### Utility Tools
- **random_number(min_val: int = 0, max_val: int = 100) -> int**: Generates a random integer between specified bounds
- **reverse_string(text: str) -> str**: Reverses the input string
- **is_even(n: int) -> bool**: Checks if a number is even
- **get_country_capital(country: str) -> str**: Returns the capital of a given country (supports Switzerland, France, Germany)

### Mathematical Tools
- **calculate(expression: str) -> float**: Evaluates simple mathematical expressions safely
- **list_operations(numbers: list[int]) -> dict**: Returns statistics (sum, average, min, max, count) for a list of numbers

### Text Processing Tools
- **word_count(text: str) -> dict**: Returns word count statistics including total words, characters, and average word length

### Conversion Tools
- **convert_temperature(temp: float, from_unit: str, to_unit: str) -> float**: Converts temperature between Celsius, Fahrenheit, and Kelvin

### Date/Time Tools
- **get_current_datetime() -> str**: Returns the current date and time as a formatted string

## Key Features

- **MCP Server Implementation**: Stdio-based transport for tool communication
- **Comprehensive Tool Set**: 9 different tools covering various utility functions
- **LangChain Agent**: LLM-powered agent using ChatOllama
- **RAG Support**: Retrieval-augmented generation with embeddings
- **Data Pipeline**: Complete data loading and preprocessing workflow

## Troubleshooting

### Import Error: `langchain_mcp_adapters`

Ensure the package is installed:
```bash
pip install langchain-mcp-adapters
```

Restart the Python interpreter in VS Code:
- Press `Ctrl+Shift+P`
- Search for "Python: Restart Language Server"

## License


