# Raspberry Pi TV Control Roadmap

## Goal

Turn the FastMCP scaffold into a Raspberry Pi service that can send infrared commands to a TV.

## Primary Use Case

Mute the TV during commercial breaks and restore audio when the program resumes.

## Behavior Model

1. Expose a mute toggle so audio can be silenced quickly when ads begin.
2. Expose an unmute or restore-audio action so the previous volume state can be brought back.
3. Keep the command surface small at first so the ad-break workflow is reliable before adding more controls.

## Phase 1: Hardware and OS baseline

1. Pick a Raspberry Pi model and install a supported Raspberry Pi OS release.
2. Attach an IR transmitter extension or GPIO-driven IR LED circuit.
3. Confirm the Pi can power the transmitter reliably and that the TV can receive a test signal.

## Phase 2: Core IR control

1. Choose the IR control stack, likely `lirc` or a GPIO-based IR library.
2. Capture and verify the TV's remote codes.
3. Build a small Python adapter layer that exposes actions like `mute`, `restore_audio`, `volume_up`, and `volume_down`.

## Phase 3: MCP server API

1. Add MCP tools for `mute_audio`, `restore_audio`, and related TV actions.
2. Add a generic `send_ir_command` tool for custom codes.
3. Add validation and clear error messages for unsupported commands.

## Phase 4: Raspberry Pi deployment

1. Package the server for installation on the Pi.
2. Run it as a systemd service.
3. Make configuration adjustable through environment variables or a config file.

## Phase 5: Reliability and testing

1. Add unit tests for command mapping.
2. Add a hardware test mode that can run without sending real IR.
3. Log each command sent to the TV for troubleshooting.

## Suggested first implementation step

Start with a single working mute and restore-audio flow, then expand to power, volume, and input selection.
