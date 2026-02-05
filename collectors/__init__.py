"""Signal collectors for pm-playbooks.

Provides a registry of all available collectors and a helper to
instantiate them from a signals.yaml config.
"""

from __future__ import annotations

from typing import Any

from .base import BaseCollector, CollectorResult, SignalItem

# Lazy imports to avoid hard dependency on optional packages
_COLLECTOR_CLASSES: dict[str, str] = {
    "github": "collectors.github_collector:GitHubCollector",
    "hackernews": "collectors.hn_collector:HackerNewsCollector",
    "reddit": "collectors.reddit_collector:RedditCollector",
    "news": "collectors.news_collector:NewsCollector",
    "discord": "collectors.discord_collector:DiscordCollector",
    "twitter": "collectors.twitter_collector:TwitterCollector",
}


def _import_class(dotted_path: str) -> type[BaseCollector]:
    """Import a collector class from a dotted module:class path."""
    module_path, class_name = dotted_path.rsplit(":", 1)
    import importlib
    module = importlib.import_module(module_path)
    return getattr(module, class_name)


def get_collector(name: str, config: dict[str, Any]) -> BaseCollector:
    """Instantiate a collector by name with the given config."""
    if name not in _COLLECTOR_CLASSES:
        raise ValueError(f"Unknown collector: {name}. Available: {list(_COLLECTOR_CLASSES.keys())}")
    cls = _import_class(_COLLECTOR_CLASSES[name])
    return cls(config)


def get_all_collectors(config: dict[str, Any]) -> list[BaseCollector]:
    """Instantiate all collectors that are enabled in config."""
    collectors = []
    for name in _COLLECTOR_CLASSES:
        try:
            collector = get_collector(name, config)
            if collector.is_enabled():
                collectors.append(collector)
        except Exception as e:
            import logging
            logging.getLogger(__name__).warning("Could not load collector %s: %s", name, e)
    return collectors


__all__ = [
    "BaseCollector",
    "CollectorResult",
    "SignalItem",
    "get_collector",
    "get_all_collectors",
]
