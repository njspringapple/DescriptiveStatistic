#!/usr/bin/env python3
"""Validate grading, create appendix, and append it to the original submission."""

from __future__ import annotations

import argparse
import tempfile
from pathlib import Path

from append_assessment import append_pdfs
from common import GradingValidationError, format_points
from create_assessment_appendix import build_appendix


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Erstellt eine vollständige korrigierte GOP-Abgabe."
    )
    parser.add_argument("submission", type=Path, help="Originalabgabe als PDF")
    parser.add_argument("grading", type=Path, help="Bewertungsdatei im JSON-Format")
    parser.add_argument("output", type=Path, help="Neue korrigierte PDF")
    parser.add_argument(
        "--keep-appendix",
        type=Path,
        help="Speichert den Bewertungsanhang zusätzlich separat unter diesem Pfad.",
    )
    args = parser.parse_args()

    if args.submission.resolve() == args.output.resolve():
        parser.error("Die Original-PDF darf nicht überschrieben werden.")
    try:
        if args.keep_appendix:
            appendix = args.keep_appendix
            result = build_appendix(args.grading, appendix)
            counts = append_pdfs(args.submission, appendix, args.output)
        else:
            with tempfile.TemporaryDirectory(prefix="gop-korrektur-") as tmp:
                appendix = Path(tmp) / "bewertungsanhang.pdf"
                result = build_appendix(args.grading, appendix)
                counts = append_pdfs(args.submission, appendix, args.output)
    except (FileNotFoundError, GradingValidationError, RuntimeError, ValueError) as exc:
        print("Ergebnis konnte nicht erstellt werden:")
        if isinstance(exc, GradingValidationError):
            for error in exc.errors:
                print(f"- {error}")
        else:
            print(f"- {exc}")
        return 1

    source_pages, appendix_pages, final_pages = counts
    print(f"Ergebnis erstellt: {args.output}")
    print(
        f"Punkte: {format_points(result['overall_awarded'])}/"
        f"{format_points(result['overall_max'])} "
        f"({float(result['percentage']):.1f} %)"
    )
    print(
        f"Seiten: {source_pages} Original + {appendix_pages} Bewertung = {final_pages} gesamt"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

