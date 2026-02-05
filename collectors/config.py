"""Load and validate signals.yaml configuration."""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any

import yaml

logger = logging.getLogger(__name__)

REQUIRED_KEYS = ["company"]

DEFAULT_CONFIG: dict[str, Any] = {
    "company": {"name": "Unknown", "keywords": []},
    "competitors": [],
    "collectors": {},
    "output": {
        "directory": "context/signals",
        "evidence_tag": "SIGNAL",
    },
}


def find_config(start_dir: Path | None = None) -> Path | None:
    """Search for signals.yaml in start_dir, then parent dirs up to home."""
    if start_dir is None:
        start_dir = Path.cwd()
    current = start_dir.resolve()
    home = Path.home()

    while current >= home:
        candidate = current / "signals.yaml"
        if candidate.exists():
            return candidate
        if current == current.parent:
            break
        current = current.parent
    return None


def load_config(config_path: Path | str | None = None) -> dict[str, Any]:
    """Load and validate a signals.yaml file.

    If config_path is None, searches for signals.yaml automatically.
    Returns a merged config dict with defaults applied for missing keys.
    """
    if config_path is None:
        found = find_config()
        if found is None:
            logger.warning("No signals.yaml found; using defaults")
            return dict(DEFAULT_CONFIG)
        config_path = found

    config_path = Path(config_path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config not found: {config_path}")

    logger.info("Loading config from %s", config_path)
    with open(config_path, encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    config = dict(DEFAULT_CONFIG)
    config.update(raw)

    # Validate
    issues = validate_config(config)
    for issue in issues:
        logger.warning("Config issue: %s", issue)

    # Resolve output directory relative to config file location
    output_dir = config["output"]["directory"]
    if not Path(output_dir).is_absolute():
        config["_output_dir"] = config_path.parent / output_dir
    else:
        config["_output_dir"] = Path(output_dir)

    config["_config_path"] = config_path
    return config


def validate_config(config: dict[str, Any]) -> list[str]:
    """Return a list of warnings about the config."""
    issues: list[str] = []

    if not config.get("company", {}).get("name"):
        issues.append("company.name is missing")

    if not config.get("company", {}).get("keywords"):
        issues.append("company.keywords is empty — collectors will have nothing to search for")

    collectors = config.get("collectors", {})
    if not collectors:
        issues.append("No collectors configured — all defaults will be used")

    return issues
