"""Shared markdown formatting utilities for signal files."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import Any


def signal_header(
    title: str,
    collector_name: str,
    collected_at: str | None = None,
    refresh_days: int = 7,
) -> str:
    """Generate the standard header for a signal markdown file."""
    if collected_at is None:
        collected_at = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Parse collected_at to compute next refresh
    try:
        dt = datetime.fromisoformat(collected_at.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        dt = datetime.now(timezone.utc)
    next_refresh = (dt + timedelta(days=refresh_days)).strftime("%Y-%m-%d")

    return (
        f"# {title}\n\n"
        f"> Auto-collected by pm-playbooks/collectors ({collector_name}) on {collected_at[:10]}. "
        f"Tagged [SIGNAL].\n"
        f"> Next recommended refresh: {next_refresh}\n"
    )


def metrics_table(metrics: dict[str, Any], title: str = "Summary") -> str:
    """Format a metrics dict as a markdown table."""
    if not metrics:
        return ""
    lines = [
        f"\n## {title}\n",
        "| Metric | Value |",
        "|---|---|",
    ]
    for key, value in metrics.items():
        lines.append(f"| {key} | {value} |")
    return "\n".join(lines) + "\n"


def items_table(
    items: list[dict[str, Any]],
    columns: list[str],
    title: str = "Items",
) -> str:
    """Format a list of dicts as a markdown table with given columns."""
    if not items:
        return ""
    lines = [
        f"\n## {title}\n",
        "| " + " | ".join(columns) + " |",
        "|" + "|".join(["---"] * len(columns)) + "|",
    ]
    for item in items:
        row = "| " + " | ".join(str(item.get(c, "")) for c in columns) + " |"
        lines.append(row)
    return "\n".join(lines) + "\n"


def items_list(
    items: list[dict[str, str]],
    title: str = "Items",
    max_items: int = 25,
) -> str:
    """Format items as a bulleted markdown list with title, url, summary."""
    if not items:
        return ""
    lines = [f"\n## {title}\n"]
    for item in items[:max_items]:
        title_text = item.get("title", "Untitled")
        url = item.get("url", "")
        summary = item.get("summary", "")
        link = f"[{title_text}]({url})" if url else title_text
        line = f"- {link}"
        if summary:
            line += f" — {summary}"
        lines.append(line)
    if len(items) > max_items:
        lines.append(f"\n*...and {len(items) - max_items} more items.*")
    return "\n".join(lines) + "\n"


def errors_section(errors: list[str]) -> str:
    """Format collection errors as a markdown section."""
    if not errors:
        return ""
    lines = ["\n## Collection Notes\n"]
    for err in errors:
        lines.append(f"- {err}")
    return "\n".join(lines) + "\n"


def separator() -> str:
    return "\n---\n"
