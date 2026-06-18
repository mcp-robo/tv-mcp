from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class RaspberryPiIRAdapter:
    """Stub adapter for Raspberry Pi infrared TV control."""

    sent_commands: List[str] = field(default_factory=list)
    muted: bool = False

    def send_ir_command(self, command: str) -> str:
        """Record an IR command until real hardware integration is added."""
        normalized_command = command.strip()
        if not normalized_command:
            raise ValueError("command must not be empty")

        self.sent_commands.append(normalized_command)
        return f"stub sent IR command: {normalized_command}"

    def mute_audio(self) -> str:
        """Stub mute action for commercial breaks."""
        self.muted = True
        return self.send_ir_command("mute")

    def restore_audio(self) -> str:
        """Stub restore-audio action after commercials."""
        self.muted = False
        return self.send_ir_command("unmute")
