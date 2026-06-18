from fastmcp import FastMCP


mcp = FastMCP("tv-mcp")


@mcp.tool()
def ping() -> str:
    """Simple health check for the server scaffold."""
    return "tv-mcp is running"


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
