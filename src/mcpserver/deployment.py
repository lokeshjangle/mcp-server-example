from mcp.server.fastmcp import FastMCP


mcp = FastMCP("Demo")


@mcp.tool()
def add(a: int, b: int) -> int:
    
    """Add two numbers together."""
    return a + b

@mcp.tool()
def echo(text: str) -> str:
    """Repeat back the provided text."""
    return text
