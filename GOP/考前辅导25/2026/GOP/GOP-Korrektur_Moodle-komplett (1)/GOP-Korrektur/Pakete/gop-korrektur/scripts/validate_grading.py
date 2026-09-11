#!/usr/bin/env python3
"""Validate completeness and grading invariants for a GOP assessment."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import GradingValidationError, format_points, read_json, validate_grading


def main() -> int:
    parser = argparse.ArgumentParser(description="Validiert eine GOP-Bewertungsdatei.")
    parser.add_argument("grading", type=Path, help="Bewertungsdatei im JSON-Format")
    args = parser.parse_args()
    try:
        result = validate_grading(read_json(args.grading))
    except GradingValidationError as exc:
        print("Bewertung ungültig:")
        for error in exc.errors:
            print(f"- {error}")
        return 1
    print(
        "Bewertung vollständig und gültig: "
        f"{format_points(result['overall_awarded'])}/"
        f"{format_points(result['overall_max'])} Punkte "
        f"({float(result['percentage']):.1f} %)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

