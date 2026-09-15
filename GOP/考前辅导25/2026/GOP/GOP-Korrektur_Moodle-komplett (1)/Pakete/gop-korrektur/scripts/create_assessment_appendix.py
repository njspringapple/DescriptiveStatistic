#!/usr/bin/env python3
"""Render a validated GOP grading record as a polished PDF appendix."""

from __future__ import annotations

import argparse
from pathlib import Path
from xml.sax.saxutils import escape

from common import (
    GradingValidationError,
    format_points,
    read_json,
    validate_grading,
)


def _load_reportlab():
    try:
        import reportlab
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_CENTER, TA_LEFT
        from reportlab.lib.pagesizes import A4
        from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
        from reportlab.lib.units import mm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.platypus import (
            KeepTogether,
            PageBreak,
            Paragraph,
            SimpleDocTemplate,
            Spacer,
            Table,
            TableStyle,
        )
    except ImportError as exc:
        raise RuntimeError(
            "Das Python-Paket 'reportlab' fehlt. Installiere es mit "
            "'python -m pip install reportlab'."
        ) from exc
    return {
        "reportlab": reportlab,
        "colors": colors,
        "TA_CENTER": TA_CENTER,
        "TA_LEFT": TA_LEFT,
        "A4": A4,
        "ParagraphStyle": ParagraphStyle,
        "getSampleStyleSheet": getSampleStyleSheet,
        "mm": mm,
        "pdfmetrics": pdfmetrics,
        "TTFont": TTFont,
        "KeepTogether": KeepTogether,
        "PageBreak": PageBreak,
        "Paragraph": Paragraph,
        "SimpleDocTemplate": SimpleDocTemplate,
        "Spacer": Spacer,
        "Table": Table,
        "TableStyle": TableStyle,
    }


def _register_fonts(rl: dict) -> tuple[str, str]:
    package_dir = Path(rl["reportlab"].__file__).resolve().parent
    regular = package_dir / "fonts" / "Vera.ttf"
    bold = package_dir / "fonts" / "VeraBd.ttf"
    if regular.exists() and bold.exists():
        rl["pdfmetrics"].registerFont(rl["TTFont"]("GOP-Regular", str(regular)))
        rl["pdfmetrics"].registerFont(rl["TTFont"]("GOP-Bold", str(bold)))
        return "GOP-Regular", "GOP-Bold"
    return "Helvetica", "Helvetica-Bold"


def _p(text: str, style, Paragraph):
    return Paragraph(escape(text).replace("\n", "<br/>"), style)


def build_appendix(grading_path: Path, output_path: Path) -> dict:
    result = validate_grading(read_json(grading_path))
    rl = _load_reportlab()
    colors = rl["colors"]
    mm = rl["mm"]
    font, bold_font = _register_fonts(rl)

    navy = colors.HexColor("#243B64")
    blue = colors.HexColor("#DDE8F5")
    pale = colors.HexColor("#F3F6FA")
    line = colors.HexColor("#AAB4C3")
    text_color = colors.HexColor("#1E2630")

    styles = rl["getSampleStyleSheet"]()
    title_style = rl["ParagraphStyle"](
        "GOPTitle",
        parent=styles["Title"],
        fontName=bold_font,
        fontSize=19,
        leading=23,
        textColor=navy,
        alignment=rl["TA_CENTER"],
        spaceAfter=8,
    )
    subtitle_style = rl["ParagraphStyle"](
        "GOPSubtitle",
        parent=styles["Normal"],
        fontName=font,
        fontSize=10,
        leading=14,
        alignment=rl["TA_CENTER"],
        textColor=text_color,
        spaceAfter=12,
    )
    heading_style = rl["ParagraphStyle"](
        "GOPHeading",
        parent=styles["Heading2"],
        fontName=bold_font,
        fontSize=13,
        leading=16,
        textColor=navy,
        spaceBefore=7,
        spaceAfter=5,
    )
    body_style = rl["ParagraphStyle"](
        "GOPBody",
        parent=styles["BodyText"],
        fontName=font,
        fontSize=9.2,
        leading=12.3,
        textColor=text_color,
        alignment=rl["TA_LEFT"],
    )
    small_style = rl["ParagraphStyle"](
        "GOPSmall",
        parent=body_style,
        fontSize=8,
        leading=10.2,
    )
    table_head_style = rl["ParagraphStyle"](
        "GOPTableHead",
        parent=small_style,
        fontName=bold_font,
        textColor=colors.white,
    )
    table_body_style = rl["ParagraphStyle"](
        "GOPTableBody",
        parent=small_style,
        fontSize=8.2,
        leading=10.5,
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = rl["SimpleDocTemplate"](
        str(output_path),
        pagesize=rl["A4"],
        rightMargin=16 * mm,
        leftMargin=16 * mm,
        topMargin=17 * mm,
        bottomMargin=17 * mm,
        title="Bewertungsanhang GOP-Übungsblatt",
        author="Automatisiertes GOP-Feedback",
    )

    def footer(canvas, document):
        canvas.saveState()
        canvas.setStrokeColor(line)
        canvas.setLineWidth(0.4)
        canvas.line(16 * mm, 12 * mm, 194 * mm, 12 * mm)
        canvas.setFont(font, 7.5)
        canvas.setFillColor(colors.HexColor("#596575"))
        canvas.drawString(16 * mm, 8 * mm, "Unverbindliches automatisiertes Übungsfeedback")
        canvas.drawRightString(194 * mm, 8 * mm, f"Bewertungsanhang · Seite {document.page}")
        canvas.restoreState()

    story = []
    sheet = result["sheet"]
    story.append(rl["Paragraph"]("Bewertungsanhang", title_style))
    story.append(_p(sheet["title"], subtitle_style, rl["Paragraph"]))
    story.append(
        _p(
            "Die Originalseiten der Abgabe wurden nicht verändert. Die folgende Bewertung ist "
            "automatisiertes, unverbindliches Übungsfeedback und keine offizielle Prüfungsentscheidung.",
            body_style,
            rl["Paragraph"],
        )
    )
    story.append(rl["Spacer"](1, 5 * mm))

    for task in result["tasks"]:
        block = [
            _p(
                f"Aufgabe {task['id']}",
                heading_style,
                rl["Paragraph"],
            )
        ]
        rows = [
            [
                _p("Teilaufgabe", table_head_style, rl["Paragraph"]),
                _p("Punkte", table_head_style, rl["Paragraph"]),
                _p("Begründung / Kommentar", table_head_style, rl["Paragraph"]),
            ]
        ]
        uncertain_in_task = False
        for part in task["parts"]:
            flags = set(part["flags"])
            uncertain = "unsicher" in flags
            uncertain_in_task = uncertain_in_task or uncertain
            points = (
                f"{format_points(part['erreicht'])}"
                f"{'*' if uncertain else ''}/"
                f"{format_points(part['maximal'])}"
            )
            notes = []
            if part["begruendung"]:
                notes.append(part["begruendung"])
            if part["kommentar"]:
                notes.append(part["kommentar"])
            flag_labels = []
            if "folgefehler" in flags:
                flag_labels.append("Folgefehler berücksichtigt")
            if "nicht_lesbar" in flags:
                flag_labels.append("nicht lesbar")
            if "nicht_bearbeitet" in flags:
                flag_labels.append("nicht bearbeitet")
            if "nicht_eingereicht" in flags:
                flag_labels.append("nicht eingereicht")
            if flag_labels:
                notes.append("Kennzeichnung: " + ", ".join(flag_labels) + ".")
            if uncertain:
                notes.append("In der Einsicht diskutieren.")
            note_text = " ".join(notes) if notes else "–"
            rows.append(
                [
                    _p(f"{task['id']}({part['id']})", table_body_style, rl["Paragraph"]),
                    _p(points, table_body_style, rl["Paragraph"]),
                    _p(note_text, table_body_style, rl["Paragraph"]),
                ]
            )
        task_points = (
            f"{format_points(task['erreicht'])}"
            f"{'*' if uncertain_in_task else ''}/"
            f"{format_points(task['maximal'])}"
        )
        rows.append(
            [
                _p(f"Summe Aufgabe {task['id']}", table_head_style, rl["Paragraph"]),
                _p(task_points, table_head_style, rl["Paragraph"]),
                "",
            ]
        )
        table = rl["Table"](rows, colWidths=[29 * mm, 25 * mm, 120 * mm], repeatRows=1)
        table.setStyle(
            rl["TableStyle"](
                [
                    ("BACKGROUND", (0, 0), (-1, 0), navy),
                    ("BACKGROUND", (0, -1), (-1, -1), navy),
                    ("TEXTCOLOR", (0, -1), (-1, -1), colors.white),
                    ("FONTNAME", (0, -1), (-1, -1), bold_font),
                    ("GRID", (0, 0), (-1, -1), 0.45, line),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, pale]),
                ]
            )
        )
        block.extend([table, rl["Spacer"](1, 2.5 * mm)])
        story.append(rl["KeepTogether"](block))

    story.append(rl["PageBreak"]())
    story.append(_p("Gesamtübersicht", heading_style, rl["Paragraph"]))
    summary_rows = [
        [
            _p("Aufgabe", table_head_style, rl["Paragraph"]),
            _p("Erreicht", table_head_style, rl["Paragraph"]),
            _p("Maximum", table_head_style, rl["Paragraph"]),
        ]
    ]
    for task in result["tasks"]:
        summary_rows.append(
            [
                _p(f"Aufgabe {task['id']}", table_body_style, rl["Paragraph"]),
                _p(format_points(task["erreicht"]), table_body_style, rl["Paragraph"]),
                _p(format_points(task["maximal"]), table_body_style, rl["Paragraph"]),
            ]
        )
    summary_rows.append(
        [
            _p("Gesamt", table_head_style, rl["Paragraph"]),
            _p(format_points(result["overall_awarded"]), table_head_style, rl["Paragraph"]),
            _p(format_points(result["overall_max"]), table_head_style, rl["Paragraph"]),
        ]
    )
    summary = rl["Table"](summary_rows, colWidths=[90 * mm, 42 * mm, 42 * mm], repeatRows=1)
    summary.setStyle(
        rl["TableStyle"](
            [
                ("BACKGROUND", (0, 0), (-1, 0), navy),
                ("BACKGROUND", (0, -1), (-1, -1), navy),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("TEXTCOLOR", (0, -1), (-1, -1), colors.white),
                ("GRID", (0, 0), (-1, -1), 0.45, line),
                ("ROWBACKGROUNDS", (0, 1), (-1, -2), [colors.white, blue]),
                ("ALIGN", (1, 1), (-1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    story.append(summary)
    story.append(rl["Spacer"](1, 4 * mm))
    story.append(
        _p(
            f"Gesamt: {format_points(result['overall_awarded'])}/"
            f"{format_points(result['overall_max'])} Punkte, entsprechend "
            f"{float(result['percentage']):.1f} %.",
            heading_style,
            rl["Paragraph"],
        )
    )

    story.append(_p("Typische oder wiederholte Fehler", heading_style, rl["Paragraph"]))
    story.append(_p(result["feedback"], body_style, rl["Paragraph"]))

    story.append(_p("Formale Hinweise", heading_style, rl["Paragraph"]))
    if result["formal_notes"]:
        for note in result["formal_notes"]:
            story.append(_p(f"• {note}", body_style, rl["Paragraph"]))
    else:
        story.append(_p("Keine besonderen formalen Hinweise.", body_style, rl["Paragraph"]))

    story.append(_p("Legende", heading_style, rl["Paragraph"]))
    story.append(
        _p(
            "Folgefehler: Ein früheres falsches Ergebnis wurde bei methodisch richtiger Weiterrechnung "
            "nicht mehrfach vollständig abgezogen. *: Unsichere, tendenziell niedrigere Wertung; "
            "in der Einsicht diskutieren.",
            small_style,
            rl["Paragraph"],
        )
    )

    doc.build(story, onFirstPage=footer, onLaterPages=footer)
    if not output_path.exists() or output_path.stat().st_size == 0:
        raise RuntimeError(f"Bewertungsanhang wurde nicht erzeugt: {output_path}")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Erstellt den GOP-Bewertungsanhang.")
    parser.add_argument("grading", type=Path, help="Validierte Bewertungsdatei")
    parser.add_argument("output", type=Path, help="Ziel-PDF des Anhangs")
    args = parser.parse_args()
    try:
        build_appendix(args.grading, args.output)
    except (GradingValidationError, RuntimeError) as exc:
        parser.error(str(exc))
    print(f"Bewertungsanhang erstellt: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

