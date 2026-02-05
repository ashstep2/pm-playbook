"""Twitter/X signal collector (disabled by default).

Requires Twitter API v2 Bearer Token ($200/mo Basic plan minimum).
Set TWITTER_BEARER_TOKEN to enable.

This collector is a stub — the auth cost makes it opt-in only.
"""

from __future__ import annotations

import logging
import os

from .base import BaseCollector, CollectorResult

logger = logging.getLogger(__name__)


class TwitterCollector(BaseCollector):
    name = "twitter"
    requires_auth = True
    default_enabled = False  # $200/mo API cost

    def has_auth(self) -> bool:
        return bool(os.environ.get("TWITTER_BEARER_TOKEN"))

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        if not self.has_auth():
            result.errors.append(
                "Twitter collector requires TWITTER_BEARER_TOKEN. "
                "Twitter API v2 Basic plan ($200/mo) is required for search. "
                "See https://developer.x.com/en/portal/petition/essential/basic-info"
            )
            return result

        try:
            import tweepy  # noqa: F401
        except ImportError:
            result.errors.append("tweepy not installed. Run: pip install tweepy")
            return result

        # TODO: Implement tweet search using tweepy.Client
        # Pattern:
        #   client = tweepy.Client(bearer_token=token)
        #   for query in queries:
        #       tweets = client.search_recent_tweets(query, max_results=10)
        #       ...
        result.errors.append(
            "Twitter collector is a stub. Implement search when "
            "TWITTER_BEARER_TOKEN is configured ($200/mo Basic plan)."
        )
        return result

    def format_markdown(self, result: CollectorResult) -> str:
        from .formatters import signal_header, errors_section
        return (
            signal_header("Twitter/X Signals", self.name, result.collected_at)
            + "\n*Twitter collector not yet fully implemented (requires $200/mo API plan).*\n"
            + errors_section(result.errors)
        )
