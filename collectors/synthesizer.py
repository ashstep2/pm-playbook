"""Cross-source signal synthesizer.

Reads all signal markdown files from the output directory and produces
a _synthesis.md summary with trending topics, sentiment overview,
competitor mentions, and a composite health score.
"""

from __future__ import annotations

import logging
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .formatters import signal_header, metrics_table

logger = logging.getLogger(__name__)


class Synthesizer:
    """Reads signal files and produces a cross-source synthesis."""

    def __init__(self, config: dict[str, Any]) -> None:
        self.config = config
        self.company_name = config.get("company", {}).get("name", "Unknown")
        self.competitors = config.get("competitors", [])

    def synthesize(self, output_dir: Path) -> Path:
        """Read all signal files and write _synthesis.md."""
        signal_files = sorted(output_dir.glob("*.md"))
        signal_files = [f for f in signal_files if f.name != "_synthesis.md"]

        if not signal_files:
            logger.warning("No signal files found in %s", output_dir)
            return output_dir / "_synthesis.md"

        # Parse each file
        source_summaries: list[dict[str, Any]] = []
        all_items: list[dict[str, str]] = []
        competitor_mentions: dict[str, int] = {}

        for path in signal_files:
            content = path.read_text(encoding="utf-8")
            summary = self._parse_signal_file(path.stem, content)
            source_summaries.append(summary)
            all_items.extend(summary.get("items", []))

            # Count competitor mentions
            for comp in self.competitors:
                comp_name = comp.get("name", "") if isinstance(comp, dict) else str(comp)
                if comp_name:
                    count = content.lower().count(comp_name.lower())
                    if count > 0:
                        competitor_mentions[comp_name] = competitor_mentions.get(comp_name, 0) + count

        # Build synthesis
        output_path = output_dir / "_synthesis.md"
        content = self._build_synthesis(source_summaries, all_items, competitor_mentions)
        output_path.write_text(content, encoding="utf-8")
        logger.info("Wrote synthesis to %s", output_path)
        return output_path

    def _parse_signal_file(self, source_name: str, content: str) -> dict[str, Any]:
        """Extract key data from a signal markdown file."""
        summary: dict[str, Any] = {
            "source": source_name,
            "item_count": 0,
            "items": [],
        }

        # Count [SIGNAL] tagged items
        signal_count = content.count("[SIGNAL]")
        summary["item_count"] = signal_count

        # Extract linked items (markdown links)
        link_pattern = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
        for match in link_pattern.finditer(content):
            title, url = match.group(1), match.group(2)
            if url.startswith("http"):
                summary["items"].append({
                    "title": title,
                    "url": url,
                    "source": source_name,
                })

        # Extract metrics table values
        metric_pattern = re.compile(r"\|\s*(.+?)\s*\|\s*(.+?)\s*\|")
        for match in metric_pattern.finditer(content):
            key, value = match.group(1).strip(), match.group(2).strip()
            if key not in ("Metric", "---", ""):
                summary.setdefault("metrics", {})[key] = value

        return summary

    def _build_synthesis(
        self,
        sources: list[dict[str, Any]],
        all_items: list[dict[str, str]],
        competitor_mentions: dict[str, int],
    ) -> str:
        now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
        sections = [
            signal_header(
                "Cross-Source Signal Synthesis",
                "synthesizer",
                now,
                refresh_days=7,
            ),
        ]

        # Overview metrics
        total_items = sum(s["item_count"] for s in sources)
        overview = {
            "Sources collected": len(sources),
            "Total signal items": total_items,
            "Unique URLs": len({i["url"] for i in all_items if i.get("url")}),
        }
        sections.append(metrics_table(overview, title="Collection Overview"))

        # Per-source breakdown
        sections.append("\n## Source Breakdown\n")
        sections.append("| Source | Items | Key Metrics |")
        sections.append("|---|---|---|")
        for source in sources:
            name = source["source"]
            count = source["item_count"]
            metrics = source.get("metrics", {})
            top_metrics = ", ".join(f"{k}: {v}" for k, v in list(metrics.items())[:3])
            sections.append(f"| {name} | {count} | {top_metrics} |")
        sections.append("")

        # Competitor radar
        if competitor_mentions:
            sections.append("\n## Competitor Radar\n")
            sections.append("| Competitor | Mentions Across Sources |")
            sections.append("|---|---|")
            for comp, count in sorted(competitor_mentions.items(), key=lambda x: -x[1]):
                sections.append(f"| {comp} | {count} |")
            sections.append("")

        # Top items across sources
        if all_items:
            sections.append("\n## Top Signals (Cross-Source)\n")
            seen_titles: set[str] = set()
            shown = 0
            for item in all_items:
                if item["title"] in seen_titles:
                    continue
                seen_titles.add(item["title"])
                sections.append(
                    f"- [{item['title']}]({item['url']}) — *{item['source']}* [SIGNAL]"
                )
                shown += 1
                if shown >= 15:
                    break
            sections.append("")

        # Guidance for skills
        sections.append("\n## Usage Notes\n")
        sections.append(
            "This synthesis is auto-generated from individual signal files. "
            "Skills should reference specific source files for detailed data.\n\n"
            "- **competitive-response**: Use Competitor Radar + individual source files for Steps 1, 2, 6\n"
            "- **ecosystem-health**: Use Source Breakdown + github-ecosystem.md for community metrics\n"
            "- **measuring-product-market-fit**: Use Top Signals for organic growth evidence\n"
        )

        return "\n".join(sections) + "\n"
