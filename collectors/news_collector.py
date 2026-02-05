"""News signal collector using NewsAPI.org.

Requires: NEWS_API_KEY env var.
Free tier: 100 requests/day, 1 month lookback, no commercial use.
Paid: $449/mo for Everything endpoint.
"""

from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Any

import requests

from .base import BaseCollector, CollectorResult, SignalItem
from .formatters import signal_header, metrics_table, errors_section

logger = logging.getLogger(__name__)

NEWS_API_URL = "https://newsapi.org/v2/everything"


class NewsCollector(BaseCollector):
    name = "news"
    requires_auth = True
    default_enabled = True

    def has_auth(self) -> bool:
        return bool(os.environ.get("NEWS_API_KEY"))

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        api_key = os.environ.get("NEWS_API_KEY")
        if not api_key:
            result.errors.append("Missing NEWS_API_KEY environment variable")
            return result

        queries = self.collector_config.get("queries", self.keywords)
        if not queries:
            result.errors.append("No search queries configured for news collector")
            return result

        lookback_days = self.collector_config.get("lookback_days", 30)
        from_date = (datetime.now(timezone.utc) - timedelta(days=lookback_days)).strftime("%Y-%m-%d")
        max_per_query = self.collector_config.get("max_per_query", 10)
        language = self.collector_config.get("language", "en")

        all_items: list[SignalItem] = []
        total_results = 0
        seen_urls: set[str] = set()

        for query in queries:
            try:
                resp = requests.get(
                    NEWS_API_URL,
                    params={
                        "q": query,
                        "from": from_date,
                        "language": language,
                        "sortBy": "relevancy",
                        "pageSize": max_per_query,
                        "apiKey": api_key,
                    },
                    timeout=15,
                )
                result.raw_query_count += 1
                resp.raise_for_status()
                data = resp.json()

                if data.get("status") != "ok":
                    result.errors.append(f"NewsAPI error for '{query}': {data.get('message', 'unknown')}")
                    continue

                total_results += data.get("totalResults", 0)

                for article in data.get("articles", []):
                    url = article.get("url", "")
                    if url in seen_urls or not url:
                        continue
                    seen_urls.add(url)

                    published = article.get("publishedAt", "")[:10]
                    source_name = article.get("source", {}).get("name", "Unknown")

                    all_items.append(SignalItem(
                        title=article.get("title", "Untitled"),
                        url=url,
                        source=source_name,
                        timestamp=published,
                        summary=article.get("description", ""),
                        metadata={
                            "author": article.get("author", ""),
                            "source_name": source_name,
                            "query": query,
                        },
                    ))

            except requests.RequestException as e:
                result.errors.append(f"News search failed for '{query}': {e}")

        # Sort by recency
        all_items.sort(key=lambda x: x.timestamp, reverse=True)
        result.items = all_items

        result.metrics = {
            "Queries searched": len(queries),
            "Total articles found": total_results,
            "Unique articles collected": len(all_items),
            "Sources represented": len({i.source for i in all_items}),
        }

        return result

    def format_markdown(self, result: CollectorResult) -> str:
        sections = [
            signal_header(
                "News Coverage Signals",
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
                sections.append(
                    f"- [{item.title}]({item.url}) — *{item.source}* "
                    f"`{item.timestamp}` [SIGNAL]\n"
                )
                if item.summary:
                    sections.append(f"  > {item.summary[:200]}\n")

        sections.append(errors_section(result.errors))
        return "".join(sections)
