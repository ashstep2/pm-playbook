"""Hacker News signal collector using the Algolia HN Search API.

Free, no auth required, no rate limits documented.
API docs: https://hn.algolia.com/api
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

from .base import BaseCollector, CollectorResult, SignalItem
from .formatters import signal_header, metrics_table, items_list, errors_section

logger = logging.getLogger(__name__)

HN_SEARCH_URL = "https://hn.algolia.com/api/v1/search"
HN_ITEM_URL = "https://news.ycombinator.com/item?id={}"


class HackerNewsCollector(BaseCollector):
    name = "hackernews"
    requires_auth = False
    default_enabled = True

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        queries = self.collector_config.get("queries", self.keywords)
        if not queries:
            result.errors.append("No search queries configured for hackernews")
            return result

        lookback_days = self.collector_config.get("lookback_days", 30)
        cutoff_ts = int((datetime.now(timezone.utc) - timedelta(days=lookback_days)).timestamp())
        max_results_per_query = self.collector_config.get("max_per_query", 10)

        all_items: list[SignalItem] = []
        total_hits = 0
        seen_ids: set[str] = set()

        for query in queries:
            try:
                resp = requests.get(
                    HN_SEARCH_URL,
                    params={
                        "query": query,
                        "tags": "story",
                        "numericFilters": f"created_at_i>{cutoff_ts}",
                        "hitsPerPage": max_results_per_query,
                    },
                    timeout=15,
                )
                result.raw_query_count += 1
                resp.raise_for_status()
                data = resp.json()
                total_hits += data.get("nbHits", 0)

                for hit in data.get("hits", []):
                    hn_id = hit.get("objectID", "")
                    if hn_id in seen_ids:
                        continue
                    seen_ids.add(hn_id)

                    points = hit.get("points", 0) or 0
                    num_comments = hit.get("num_comments", 0) or 0
                    created = hit.get("created_at", "")[:10]

                    all_items.append(SignalItem(
                        title=hit.get("title", "Untitled"),
                        url=hit.get("url") or HN_ITEM_URL.format(hn_id),
                        source="Hacker News",
                        timestamp=created,
                        score=float(points),
                        summary=f"{points} pts, {num_comments} comments",
                        metadata={
                            "hn_id": hn_id,
                            "points": points,
                            "num_comments": num_comments,
                            "query": query,
                            "hn_url": HN_ITEM_URL.format(hn_id),
                        },
                    ))

            except requests.RequestException as e:
                result.errors.append(f"HN search failed for '{query}': {e}")

        # Sort by score descending
        all_items.sort(key=lambda x: x.score, reverse=True)
        result.items = all_items

        result.metrics = {
            "Queries searched": len(queries),
            "Total HN hits": total_hits,
            "Unique stories found": len(all_items),
            "Top story points": all_items[0].score if all_items else 0,
        }

        return result

    def format_markdown(self, result: CollectorResult) -> str:
        sections = [
            signal_header(
                "Hacker News Sentiment Signals",
                self.name,
                result.collected_at,
            ),
            metrics_table(result.metrics),
        ]

        # Group by query
        by_query: dict[str, list[SignalItem]] = {}
        for item in result.items:
            q = item.metadata.get("query", "other")
            by_query.setdefault(q, []).append(item)

        for query, items in by_query.items():
            sections.append(f"\n### Query: \"{query}\"\n")
            for item in items[:10]:
                hn_url = item.metadata.get("hn_url", "")
                pts = item.metadata.get("points", 0)
                comments = item.metadata.get("num_comments", 0)
                link = f"[{item.title}]({item.url})"
                discussion = f" ([discussion]({hn_url}))" if hn_url and hn_url != item.url else ""
                sections.append(
                    f"- {link}{discussion} — {pts} pts, {comments} comments "
                    f"`{item.timestamp}` [SIGNAL]\n"
                )

        sections.append(errors_section(result.errors))
        return "".join(sections)
