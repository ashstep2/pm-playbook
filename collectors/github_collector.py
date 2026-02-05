"""GitHub signal collector using PyGithub.

Collects repo stats, recent activity, issues/PRs, and contributor data
for configured repositories.

Requires: GITHUB_TOKEN env var (free, 5000 req/hr authenticated).
"""

from __future__ import annotations

import logging
import os
from datetime import datetime, timedelta, timezone
from typing import Any

from .base import BaseCollector, CollectorResult, SignalItem
from .formatters import signal_header, metrics_table, items_table, errors_section

logger = logging.getLogger(__name__)


class GitHubCollector(BaseCollector):
    name = "github"
    requires_auth = True
    default_enabled = True

    def has_auth(self) -> bool:
        return bool(os.environ.get("GITHUB_TOKEN"))

    def collect(self) -> CollectorResult:
        result = CollectorResult(collector_name=self.name)

        try:
            from github import Github, GithubException
        except ImportError:
            result.errors.append("PyGithub not installed. Run: pip install PyGithub")
            return result

        token = os.environ.get("GITHUB_TOKEN", "")
        gh = Github(token) if token else Github()

        repos_config = self.collector_config.get("repos", [])
        if not repos_config:
            result.errors.append("No repos configured in collectors.github.repos")
            return result

        cutoff = datetime.now(timezone.utc) - timedelta(days=30)
        total_stars = 0
        total_forks = 0
        total_open_issues = 0
        repo_data: list[dict[str, Any]] = []
        recent_items: list[SignalItem] = []

        for repo_name in repos_config:
            try:
                repo = gh.get_repo(repo_name)
                result.raw_query_count += 1

                stars = repo.stargazers_count
                forks = repo.forks_count
                open_issues = repo.open_issues_count
                total_stars += stars
                total_forks += forks
                total_open_issues += open_issues

                # Last push
                pushed = repo.pushed_at.strftime("%Y-%m-%d") if repo.pushed_at else "N/A"

                repo_data.append({
                    "repo": repo_name,
                    "stars": stars,
                    "forks": forks,
                    "open_issues": open_issues,
                    "last_push": pushed,
                    "language": repo.language or "N/A",
                })

                # Recent issues and PRs (last 30 days, up to 10 per repo)
                try:
                    for issue in repo.get_issues(state="all", since=cutoff, sort="created", direction="desc"):
                        result.raw_query_count += 1
                        if len(recent_items) >= 50:
                            break
                        kind = "PR" if issue.pull_request else "Issue"
                        recent_items.append(SignalItem(
                            title=f"[{kind}] {issue.title}",
                            url=issue.html_url,
                            source=repo_name,
                            timestamp=issue.created_at.strftime("%Y-%m-%d"),
                            metadata={
                                "state": issue.state,
                                "comments": issue.comments,
                                "kind": kind,
                            },
                        ))
                        if len(recent_items) >= 50:
                            break
                except GithubException as e:
                    result.errors.append(f"Could not fetch issues for {repo_name}: {e.data.get('message', str(e))}")

            except GithubException as e:
                msg = e.data.get("message", str(e)) if hasattr(e, "data") else str(e)
                result.errors.append(f"Could not access {repo_name}: {msg}")

        result.items = recent_items
        result.metrics = {
            "Total stars (tracked repos)": total_stars,
            "Total forks": total_forks,
            "Total open issues/PRs": total_open_issues,
            "Repos tracked": len(repo_data),
        }
        result.metrics["_repo_data"] = repo_data

        return result

    def format_markdown(self, result: CollectorResult) -> str:
        sections = [
            signal_header(
                "GitHub Ecosystem Signals",
                self.name,
                result.collected_at,
            ),
        ]

        # Metrics summary (exclude internal _repo_data)
        display_metrics = {k: v for k, v in result.metrics.items() if not k.startswith("_")}
        sections.append(metrics_table(display_metrics))

        # Per-repo table
        repo_data = result.metrics.get("_repo_data", [])
        if repo_data:
            sections.append(items_table(
                repo_data,
                columns=["repo", "stars", "forks", "open_issues", "last_push", "language"],
                title="Repository Overview",
            ))

        # Recent activity
        if result.items:
            sections.append("\n## Recent Activity (Last 30 Days)\n")
            for item in result.items[:25]:
                state = item.metadata.get("state", "")
                comments = item.metadata.get("comments", 0)
                badge = f"({state}, {comments} comments)" if comments else f"({state})"
                sections.append(
                    f"- [{item.title}]({item.url}) — {item.source} {badge} `{item.timestamp}` [SIGNAL]\n"
                )

        sections.append(errors_section(result.errors))
        return "".join(sections)
