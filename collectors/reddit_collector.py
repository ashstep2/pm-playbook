"""Reddit signal collector using PRAW.

Requires Reddit API OAuth credentials:
  REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

Free tier: 100 requests/minute.
"""

from __future__ import annotations

import logging
import os
from typing import Any

from .base import BaseCollector, CollectorResult, SignalItem
from .formatters import signal_header, metrics_table, errors_section

logger = logging.getLogger(__name__)


class RedditCollector(BaseCollector):
    name = "reddit"
    requires_auth = True
    default_enabled = True

    def has_auth(self) -> bool:
        return all(os.environ.get(k) for k in [
            "REDDIT_CLIENT_ID",
            "REDDIT_CLIENT_SECRET",
        ])

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        try:
            import praw
        except ImportError:
            result.errors.append("praw not installed. Run: pip install praw")
            return result

        if not self.has_auth():
            result.errors.append("Missing REDDIT_CLIENT_ID or REDDIT_CLIENT_SECRET")
            return result

        reddit = praw.Reddit(
            client_id=os.environ["REDDIT_CLIENT_ID"],
            client_secret=os.environ["REDDIT_CLIENT_SECRET"],
            user_agent=os.environ.get("REDDIT_USER_AGENT", "pm-playbooks-collector/1.0"),
        )

        subreddits = self.collector_config.get("subreddits", [])
        queries = self.collector_config.get("queries", self.keywords)
        max_per_sub = self.collector_config.get("max_per_subreddit", 10)
        time_filter = self.collector_config.get("time_filter", "month")

        if not subreddits:
            result.errors.append("No subreddits configured in collectors.reddit.subreddits")
            return result

        all_items: list[SignalItem] = []
        total_score = 0
        seen_ids: set[str] = set()

        for sub_name in subreddits:
            for query in queries:
                try:
                    subreddit = reddit.subreddit(sub_name)
                    result.raw_query_count += 1
                    for post in subreddit.search(query, time_filter=time_filter, limit=max_per_sub):
                        if post.id in seen_ids:
                            continue
                        seen_ids.add(post.id)
                        total_score += post.score

                        from datetime import datetime, timezone
                        created = datetime.fromtimestamp(post.created_utc, tz=timezone.utc)

                        all_items.append(SignalItem(
                            title=post.title,
                            url=f"https://reddit.com{post.permalink}",
                            source=f"r/{sub_name}",
                            timestamp=created.strftime("%Y-%m-%d"),
                            score=float(post.score),
                            summary=f"{post.score} upvotes, {post.num_comments} comments",
                            metadata={
                                "subreddit": sub_name,
                                "upvote_ratio": post.upvote_ratio,
                                "num_comments": post.num_comments,
                                "query": query,
                            },
                        ))
                except Exception as e:
                    result.errors.append(f"Reddit search r/{sub_name} for '{query}': {e}")

        all_items.sort(key=lambda x: x.score, reverse=True)
        result.items = all_items

        result.metrics = {
            "Subreddits searched": len(subreddits),
            "Unique posts found": len(all_items),
            "Total combined score": total_score,
            "Top post score": int(all_items[0].score) if all_items else 0,
        }

        return result

    def format_markdown(self, result: CollectorResult) -> str:
        sections = [
            signal_header(
                "Reddit Discussion Signals",
                self.name,
                result.collected_at,
            ),
            metrics_table(result.metrics),
        ]

        # Group by subreddit
        by_sub: dict[str, list[SignalItem]] = {}
        for item in result.items:
            sub = item.metadata.get("subreddit", "other")
            by_sub.setdefault(sub, []).append(item)

        for sub, items in by_sub.items():
            sections.append(f"\n### r/{sub}\n")
            for item in items[:10]:
                upvotes = int(item.score)
                comments = item.metadata.get("num_comments", 0)
                ratio = item.metadata.get("upvote_ratio", 0)
                sections.append(
                    f"- [{item.title}]({item.url}) — {upvotes} upvotes "
                    f"({ratio:.0%} ratio), {comments} comments "
                    f"`{item.timestamp}` [SIGNAL]\n"
                )

        sections.append(errors_section(result.errors))
        return "".join(sections)
