from fastmcp import FastMCP

from tv_mcp.ir_adapter import RaspberryPiIRAdapter


mcp = FastMCP("tv-mcp")
ir_adapter = RaspberryPiIRAdapter()


@mcp.tool()
def ping() -> str:
    """Simple health check for the server scaffold."""
    return "tv-mcp is running"


@mcp.tool()
def mute_audio() -> str:
    """Mute the TV for a commercial break."""
    return ir_adapter.mute_audio()


@mcp.tool()
def restore_audio() -> str:
    """Restore TV audio after a commercial break."""
    return ir_adapter.restore_audio()


@mcp.tool()
def send_ir_command(command: str) -> str:
    """Send a raw IR command through the Raspberry Pi adapter stub."""
    return ir_adapter.send_ir_command(command)


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
