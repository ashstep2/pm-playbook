"""Base classes for all signal collectors."""

from __future__ import annotations

import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


@dataclass
class SignalItem:
    """A single data point collected from a source."""

    title: str
    url: str = ""
    source: str = ""
    timestamp: str = ""
    score: float = 0.0
    sentiment: str = ""  # positive, negative, neutral, mixed
    summary: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class CollectorResult:
    """Output of a collector run."""

    collector_name: str
    collected_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    )
    items: list[SignalItem] = field(default_factory=list)
    metrics: dict[str, Any] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)
    raw_query_count: int = 0

    @property
    def success(self) -> bool:
        return len(self.items) > 0 or len(self.metrics) > 0

    @property
    def item_count(self) -> int:
        return len(self.items)


class BaseCollector(ABC):
    """Abstract base for all signal collectors.

    Subclasses implement collect() and format_markdown().
    The framework handles config loading, error capture, and file writing.
    """

    name: str = "base"
    requires_auth: bool = False
    default_enabled: bool = True

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.collector_config = config.get("collectors", {}).get(self.name, {})
        self.company_name = config.get("company", {}).get("name", "Unknown")
        self.keywords = config.get("company", {}).get("keywords", [])
        self.competitors = config.get("competitors", [])

    @abstractmethod
    def collect(self) -> CollectorResult:
        """Run the collection. Returns structured data.

        Implementations should catch their own exceptions and record them
        in CollectorResult.errors rather than raising.
        """
        ...

    @abstractmethod
    def format_markdown(self, result: CollectorResult) -> str:
        """Convert a CollectorResult into context/-compatible markdown."""
        ...

    def is_enabled(self) -> bool:
        """Check if this collector is enabled in config."""
        explicit = self.collector_config.get("enabled")
        if explicit is not None:
            return bool(explicit)
        return self.default_enabled

    def has_auth(self) -> bool:
        """Check if required auth credentials are present.

        Override in subclasses that need specific env vars.
        """
        return True

    def preflight(self) -> list[str]:
        """Validate that this collector can run. Returns list of issues."""
        issues: list[str] = []
        if not self.is_enabled():
            issues.append(f"{self.name}: disabled in config")
        if self.requires_auth and not self.has_auth():
            issues.append(f"{self.name}: missing required authentication")
        return issues

    def write_output(self, result: CollectorResult, output_dir: Path) -> Path:
        """Write formatted markdown to the output directory."""
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = self.collector_config.get("output_file", f"{self.name}.md")
        output_path = output_dir / filename
        content = self.format_markdown(result)
        output_path.write_text(content, encoding="utf-8")
        logger.info("Wrote %s (%d items)", output_path, result.item_count)
        return output_path

    def run(self, output_dir: Path, dry_run: bool = False) -> CollectorResult:
        """Full pipeline: preflight → collect → write."""
        issues = self.preflight()
        if issues:
            return CollectorResult(
                collector_name=self.name,
                errors=issues,
            )

        logger.info("Running %s collector...", self.name)
        result = self.collect()

        if not dry_run and result.success:
            self.write_output(result, output_dir)
        elif dry_run:
            logger.info("[dry-run] %s: %d items, %d metrics",
                        self.name, result.item_count, len(result.metrics))

        if result.errors:
            for err in result.errors:
                logger.warning("%s: %s", self.name, err)

        return result
