"""MCP server wrapping signal collectors for real-time Claude Code queries.

Run as: python -m collectors.mcp_server
Or configure in .claude/mcp.json for automatic loading.

Provides 4 tools:
  - query_signals: Search across all sources for a topic
  - get_signal_summary: Get latest metrics for configured company
  - check_competitor: Get recent signals about a specific competitor
  - refresh_signals: Run collectors and update context/signals/ files
"""

from __future__ import annotations

import json
import logging
import os
import sys
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


def create_server():
    """Create and configure the MCP server with all tools."""
    try:
        from mcp.server.fastmcp import FastMCP
    except ImportError:
        print(
            "Error: mcp package not installed. Run: pip install mcp",
            file=sys.stderr,
        )
        sys.exit(1)

    from .config import load_config
    from . import get_collector, get_all_collectors
    from .synthesizer import Synthesizer

    mcp = FastMCP(
        "pm-playbooks-signals",
        description="Public signal collectors for PM playbooks. "
        "Query GitHub, HN, Reddit, and news sources for competitive intelligence.",
    )

    def _load_config() -> dict[str, Any]:
        """Load config, looking in CWD and parent dirs."""
        return load_config()

    @mcp.tool()
    def query_signals(topic: str, sources: str = "all") -> str:
        """Search across signal sources for a specific topic.

        Args:
            topic: The topic or keyword to search for (e.g., "gaussian splatting", "World Labs")
            sources: Comma-separated list of sources to search, or "all" (default).
                     Options: github, hackernews, reddit, news

        Returns:
            Markdown-formatted results from matching sources.
        """
        config = _load_config()

        # Override keywords with the search topic
        config["company"]["keywords"] = [topic]

        source_list = (
            ["github", "hackernews", "reddit", "news"]
            if sources == "all"
            else [s.strip() for s in sources.split(",")]
        )

        results_md: list[str] = [f"# Signal Query: \"{topic}\"\n"]

        for source_name in source_list:
            try:
                collector = get_collector(source_name, config)
                if not collector.is_enabled():
                    continue
                issues = collector.preflight()
                if issues:
                    results_md.append(f"\n## {source_name}\n*Skipped: {'; '.join(issues)}*\n")
                    continue

                result = collector.collect()
                if result.success:
                    results_md.append(f"\n## {source_name} ({result.item_count} results)\n")
                    for item in result.items[:10]:
                        results_md.append(f"- [{item.title}]({item.url}) — {item.summary} [SIGNAL]\n")
                elif result.errors:
                    results_md.append(f"\n## {source_name}\n*Errors: {'; '.join(result.errors)}*\n")
            except Exception as e:
                results_md.append(f"\n## {source_name}\n*Error: {e}*\n")

        return "\n".join(results_md)

    @mcp.tool()
    def get_signal_summary() -> str:
        """Get a summary of the latest collected signals for the configured company.

        Reads from context/signals/ files if they exist, or runs a quick collection.

        Returns:
            Markdown-formatted summary of all available signals.
        """
        config = _load_config()
        output_dir = config.get("_output_dir", Path("context/signals"))

        # Check for existing signal files
        if output_dir.exists():
            synthesis_path = output_dir / "_synthesis.md"
            if synthesis_path.exists():
                return synthesis_path.read_text(encoding="utf-8")

            # No synthesis but signal files exist — read them
            signal_files = sorted(output_dir.glob("*.md"))
            if signal_files:
                sections = ["# Signal Summary\n"]
                for path in signal_files:
                    content = path.read_text(encoding="utf-8")
                    # Extract first 20 lines as preview
                    preview = "\n".join(content.splitlines()[:20])
                    sections.append(f"\n## {path.stem}\n{preview}\n...\n")
                return "\n".join(sections)

        return (
            "No signal files found. Run `refresh_signals` to collect data, "
            "or run `python -m collectors.run` from the terminal."
        )

    @mcp.tool()
    def check_competitor(competitor_name: str) -> str:
        """Get recent signals about a specific competitor.

        Args:
            competitor_name: Name of the competitor to check (e.g., "Google Genie", "Runway")

        Returns:
            Markdown-formatted signals mentioning this competitor.
        """
        config = _load_config()
        output_dir = config.get("_output_dir", Path("context/signals"))

        results: list[str] = [f"# Competitor Check: {competitor_name}\n"]

        # Search existing signal files
        if output_dir.exists():
            for path in sorted(output_dir.glob("*.md")):
                content = path.read_text(encoding="utf-8")
                if competitor_name.lower() in content.lower():
                    # Extract matching lines
                    matches = [
                        line for line in content.splitlines()
                        if competitor_name.lower() in line.lower()
                        and line.strip().startswith("-")
                    ]
                    if matches:
                        results.append(f"\n## {path.stem}\n")
                        results.extend(matches[:10])
                        results.append("")

        if len(results) == 1:
            # No matches in files — do a live search
            results.append("\n*No cached results. Running live search...*\n")
            live = query_signals(competitor_name, sources="hackernews,news")
            results.append(live)

        return "\n".join(results)

    @mcp.tool()
    def refresh_signals(collector_name: str = "all") -> str:
        """Run signal collectors and update context/signals/ files.

        Args:
            collector_name: Which collector to run. "all" runs all enabled collectors.
                           Options: all, github, hackernews, reddit, news

        Returns:
            Summary of what was collected and written.
        """
        config = _load_config()
        output_dir = config.get("_output_dir", Path("context/signals"))

        if collector_name == "all":
            collectors = get_all_collectors(config)
        else:
            try:
                collectors = [get_collector(collector_name, config)]
            except ValueError as e:
                return f"Error: {e}"

        summary_lines = ["# Signal Refresh Results\n"]

        for collector in collectors:
            result = collector.run(output_dir, dry_run=False)
            status = "OK" if result.success else "FAILED"
            summary_lines.append(
                f"- **{collector.name}**: {status} "
                f"({result.item_count} items, {len(result.errors)} errors)"
            )
            for err in result.errors:
                summary_lines.append(f"  - {err}")

        # Run synthesis if multiple collectors succeeded
        results_ok = [c for c in collectors if True]  # placeholder
        if len(collectors) > 1:
            try:
                synth = Synthesizer(config)
                synth.synthesize(output_dir)
                summary_lines.append("- **synthesis**: OK → _synthesis.md")
            except Exception as e:
                summary_lines.append(f"- **synthesis**: FAILED — {e}")

        return "\n".join(summary_lines)

    return mcp


def main():
    """Run the MCP server."""
    logging.basicConfig(level=logging.INFO)
    server = create_server()
    server.run()


if __name__ == "__main__":
    main()
