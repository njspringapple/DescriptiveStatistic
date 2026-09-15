#!/usr/bin/env python3
"""Deterministic smoke tests for registry, validation, and PDF finalization."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

from append_assessment import append_pdfs
from common import GradingValidationError, load_registry, validate_grading
from create_assessment_appendix import build_appendix
from create_blank_grading import build_template


def full_score(sheet_id: str) -> dict:
    grading = build_template(sheet_id)
    for task in grading["aufgaben"]:
        for part in task["teilaufgaben"]:
            part["erreicht"] = part["maximal"]
    grading["wiederkehrende_fehler"] = (
        "Keine auffälligen wiederholten Fehlermuster erkennbar."
    )
    return grading


def assert_rejected(data: dict, fragment: str) -> None:
    try:
        validate_grading(data)
    except GradingValidationError as exc:
        if fragment not in str(exc):
            raise AssertionError(
                f"Validierung schlug aus falschem Grund fehl: {exc}"
            ) from exc
    else:
        raise AssertionError("Ungültige Bewertung wurde akzeptiert.")


def create_source_pdf(path: Path) -> None:
    from reportlab.lib.pagesizes import A4
    from reportlab.pdfgen import canvas

    pdf = canvas.Canvas(str(path), pagesize=A4)
    pdf.setFont("Helvetica", 12)
    pdf.drawString(72, A4[1] - 72, "Testabgabe - Originalseite")
    pdf.save()


def main() -> int:
    registry = load_registry()
    assert len(registry["sheets"]) == 5
    for sheet in registry["sheets"]:
        grading = full_score(sheet["id"])
        result = validate_grading(grading)
        assert result["overall_awarded"] == result["overall_max"]

    incomplete = full_score("masstheorie")
    incomplete["aufgaben"].pop()
    assert_rejected(incomplete, "Aufgabenliste ist unvollständig")

    color_penalty = full_score("grafikaufgaben")
    part = color_penalty["aufgaben"][0]["teilaufgaben"][0]
    part["erreicht"] = 0
    part["begruendung"] = "0 Punkte, weil mit grünem Stift geschrieben."
    assert_rejected(color_penalty, "Schrift- oder Tintenfarbe")

    missing_reason = full_score("dichte-transformation")
    missing_reason["aufgaben"][0]["teilaufgaben"][0]["erreicht"] = 0
    assert_rejected(missing_reason, "Bei Punktabzug fehlt die Begründung")

    sample = full_score("zufallsvektoren-grenzwerte")
    first = sample["aufgaben"][0]["teilaufgaben"][0]
    first["erreicht"] = first["maximal"] - 1
    first["begruendung"] = "Die Normierungskonstante wurde falsch berechnet."
    first["flags"] = ["unsicher"]
    sample["wiederkehrende_fehler"] = (
        "Bei mehreren Ergebnissen fehlte eine kurze Prüfung der Voraussetzungen."
    )
    sample["formale_hinweise"] = [
        "Bitte verwende möglichst eine einheitliche schwarze oder blaue Schriftfarbe."
    ]

    with tempfile.TemporaryDirectory(prefix="gop-self-test-") as tmp:
        root = Path(tmp)
        grading_path = root / "grading.json"
        grading_path.write_text(
            json.dumps(sample, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )
        source = root / "source.pdf"
        appendix = root / "appendix.pdf"
        output = root / "result.pdf"
        create_source_pdf(source)
        build_appendix(grading_path, appendix)
        counts = append_pdfs(source, appendix, output)
        assert counts[0] == 1
        assert counts[1] >= 2
        assert counts[2] == counts[0] + counts[1]

    print("Selbsttest bestanden: 5 Blätter, Validator und PDF-Anhang funktionieren.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

