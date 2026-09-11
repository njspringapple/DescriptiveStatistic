#!/usr/bin/env python3
"""Append assessment pages to a student PDF without modifying the source."""

from __future__ import annotations

import argparse
from pathlib import Path


def _pypdf():
    try:
        from pypdf import PdfReader, PdfWriter
    except ImportError as exc:
        raise RuntimeError(
            "Das Python-Paket 'pypdf' fehlt. Installiere es mit "
            "'python -m pip install pypdf'."
        ) from exc
    return PdfReader, PdfWriter


def append_pdfs(source: Path, appendix: Path, output: Path) -> tuple[int, int, int]:
    if source.resolve() == output.resolve():
        raise ValueError("Die Original-PDF darf nicht überschrieben werden.")
    if not source.is_file():
        raise FileNotFoundError(f"Abgabe nicht gefunden: {source}")
    if not appendix.is_file():
        raise FileNotFoundError(f"Bewertungsanhang nicht gefunden: {appendix}")
    PdfReader, PdfWriter = _pypdf()
    source_reader = PdfReader(str(source))
    if source_reader.is_encrypted and source_reader.decrypt("") == 0:
        raise ValueError("Die Abgabe ist verschlüsselt und kann nicht verarbeitet werden.")
    appendix_reader = PdfReader(str(appendix))
    if appendix_reader.is_encrypted and appendix_reader.decrypt("") == 0:
        raise ValueError("Der Bewertungsanhang ist unerwartet verschlüsselt.")
    if len(source_reader.pages) == 0:
        raise ValueError("Die Abgabe enthält keine PDF-Seiten.")
    if len(appendix_reader.pages) == 0:
        raise ValueError("Der Bewertungsanhang enthält keine PDF-Seiten.")

    writer = PdfWriter()
    writer.append(source_reader)
    writer.append(appendix_reader)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("wb") as handle:
        writer.write(handle)

    final_reader = PdfReader(str(output))
    expected = len(source_reader.pages) + len(appendix_reader.pages)
    if len(final_reader.pages) != expected:
        raise RuntimeError(
            f"Seitenzahlprüfung fehlgeschlagen: {len(final_reader.pages)} statt {expected}."
        )
    return len(source_reader.pages), len(appendix_reader.pages), len(final_reader.pages)


def main() -> int:
    parser = argparse.ArgumentParser(description="Hängt einen Bewertungsbericht an eine PDF an.")
    parser.add_argument("source", type=Path, help="Unveränderte Originalabgabe")
    parser.add_argument("appendix", type=Path, help="Bewertungsanhang")
    parser.add_argument("output", type=Path, help="Neue Ergebnis-PDF")
    args = parser.parse_args()
    try:
        source_pages, appendix_pages, final_pages = append_pdfs(
            args.source, args.appendix, args.output
        )
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        parser.error(str(exc))
    print(
        f"PDF erstellt: {args.output} "
        f"({source_pages} Originalseiten + {appendix_pages} Bewertungsseiten = {final_pages})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

