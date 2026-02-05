"""Discord signal collector (disabled by default).

Requires a Discord bot token with message read permissions.
Set DISCORD_BOT_TOKEN to enable.

This collector is a stub — it demonstrates the interface and can be
extended when a bot token is available.
"""

from __future__ import annotations

import logging
import os

from .base import BaseCollector, CollectorResult

logger = logging.getLogger(__name__)


class DiscordCollector(BaseCollector):
    name = "discord"
    requires_auth = True
    default_enabled = False  # Requires bot token setup

    def has_auth(self) -> bool:
        return bool(os.environ.get("DISCORD_BOT_TOKEN"))

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        if not self.has_auth():
            result.errors.append(
                "Discord collector requires DISCORD_BOT_TOKEN. "
                "Create a bot at https://discord.com/developers/applications "
                "and add it to the target server with message read permissions."
            )
            return result

        try:
            import discord  # noqa: F401
        except ImportError:
            result.errors.append("discord.py not installed. Run: pip install discord.py")
            return result

        # TODO: Implement async message collection from configured channels
        # This requires running an async event loop, which is handled differently
        # from the other collectors. The pattern would be:
        #
        #   channels = self.collector_config.get("channels", [])
        #   for channel_id in channels:
        #       messages = await channel.history(limit=100, after=cutoff)
        #       ...
        #
        # For now, return an informative message.
        result.errors.append(
            "Discord collector is a stub. Implement async message collection "
            "when bot token and channel IDs are configured."
        )
        return result

    def format_markdown(self, result: CollectorResult) -> str:
        from .formatters import signal_header, errors_section
        return (
            signal_header("Discord Community Signals", self.name, result.collected_at)
            + "\n*Discord collector not yet fully implemented.*\n"
            + errors_section(result.errors)
        )
