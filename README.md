# MCP Server Deploy

A demo Model Context Protocol (MCP) server built with [FastMCP](https://github.com/modelcontextprotocol/python-sdk). This project exposes simple tools (add, echo) over the MCP protocol, making them callable by any MCP-compatible client such as Kiro, Claude Desktop, or Cursor.

## Features

| Tool | Description | Parameters | Returns |
|------|-------------|------------|---------|
| `add` | Add two numbers together | `a: int`, `b: int` | `int` |
| `echo` | Repeat back the provided text | `text: str` | `str` |

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) (recommended package manager)

## Project Structure

```
mcpServerDeploy/
├── main.py                  # Standalone entry point (hello world)
├── pyproject.toml           # Project metadata and dependencies
├── .python-version          # Python version pin (3.13)
├── uv.lock                  # Locked dependencies
└── src/
    └── mcpserver/
        ├── __init__.py      # Package marker
        ├── __main__.py      # CLI entry point — runs the MCP server
        └── deployment.py    # MCP tool definitions (add, echo)
```

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd mcpServerDeploy

# Create virtual environment and install dependencies
uv sync
```

## Running the Server

### Using uv (recommended)

```bash
uv run mcp-server
```

### Using the installed script

After installation, the `mcp-server` console script is available:

```bash
mcp-server
```

### Directly via Python

```bash
python -m mcpserver
```

The server starts and communicates over stdio by default, which is the standard transport for local MCP servers.

## Configuration for MCP Clients

### Kiro / VS Code

Add to your `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "demo-server": {
      "command": "uv",
      "args": ["run", "--directory", "<path-to-mcpServerDeploy>", "mcp-server"],
      "disabled": false,
      "autoApprove": ["add", "echo"]
    }
  }
}
```

### Using uvx from GitHub (no local clone needed)

```json
{
  "mcpServers": {
    "demo-server": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/lokeshjangle/mcp-server-example.git", "mcp-server"],
      "autoApprove": ["*"]
    }
  }
}
```

This installs and runs the server directly from the GitHub repository without needing to clone it locally.

### Claude Desktop

Add to your Claude Desktop config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "demo-server": {
      "command": "uv",
      "args": ["run", "--directory", "<path-to-mcpServerDeploy>", "mcp-server"]
    }
  }
}
```

Replace `<path-to-mcpServerDeploy>` with the absolute path to this project directory.

## Adding New Tools

Define new tools in `src/mcpserver/deployment.py` using the `@mcp.tool()` decorator:

```python
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```

The tool's docstring becomes its description in the MCP protocol, and type hints define the parameter schema automatically.

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `mcp[cli]` | >=1.27.2 | MCP SDK with CLI support (includes FastMCP) |

## Development

```bash
# Install in editable mode
uv pip install -e .

# Run the server with hot reload (if supported)
uv run mcp-server

# Inspect available tools via MCP Inspector
npx @modelcontextprotocol/inspector uv run mcp-server
```

## License

This project is for learning and demonstration purposes.
>