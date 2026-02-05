"""CLI entry point for running signal collectors.

Usage:
    python -m collectors.run                         # Run all enabled collectors
    python -m collectors.run --collector github       # Run one collector
    python -m collectors.run --dry-run                # Collect but don't write files
    python -m collectors.run --config path/to.yaml    # Use specific config
"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

from .config import load_config
from . import get_collector, get_all_collectors
from .synthesizer import Synthesizer


def setup_logging(verbose: bool = False) -> None:
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Collect public signals into context/signals/ markdown files.",
        prog="python -m collectors.run",
    )
    parser.add_argument(
        "--collector", "-c",
        help="Run a specific collector (e.g., github, hackernews, reddit, news)",
    )
    parser.add_argument(
        "--config",
        help="Path to signals.yaml (auto-detected if omitted)",
    )
    parser.add_argument(
        "--dry-run", "-n",
        action="store_true",
        help="Collect data but don't write output files",
    )
    parser.add_argument(
        "--no-synthesize",
        action="store_true",
        help="Skip cross-source synthesis step",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable debug logging",
    )
    args = parser.parse_args(argv)
    setup_logging(args.verbose)
    logger = logging.getLogger("collectors")

    # Load config
    try:
        config = load_config(args.config)
    except FileNotFoundError as e:
        logger.error(str(e))
        return 1

    output_dir = config.get("_output_dir", Path("context/signals"))

    # Determine which collectors to run
    if args.collector:
        try:
            collectors = [get_collector(args.collector, config)]
        except ValueError as e:
            logger.error(str(e))
            return 1
    else:
        collectors = get_all_collectors(config)

    if not collectors:
        logger.warning("No collectors enabled. Check your signals.yaml.")
        return 0

    # Run collectors
    results = []
    for collector in collectors:
        try:
            result = collector.run(output_dir, dry_run=args.dry_run)
            results.append(result)
            status = "OK" if result.success else "PARTIAL" if result.errors else "EMPTY"
            logger.info(
                "  %s: %s (%d items, %d metrics, %d errors)",
                collector.name, status,
                result.item_count, len(result.metrics), len(result.errors),
            )
        except Exception as e:
            logger.error("  %s: FAILED — %s", collector.name, e)

    # Synthesize
    if not args.no_synthesize and not args.dry_run and len(results) > 1:
        try:
            synth = Synthesizer(config)
            synth.synthesize(output_dir)
            logger.info("  synthesis: OK → _synthesis.md")
        except Exception as e:
            logger.warning("  synthesis: FAILED — %s", e)

    # Summary
    succeeded = sum(1 for r in results if r.success)
    total_items = sum(r.item_count for r in results)
    logger.info(
        "Done. %d/%d collectors succeeded, %d total items collected.",
        succeeded, len(results), total_items,
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
