#!/usr/bin/env python3
"""Shared registry loading and grading validation for the GOP skill."""

from __future__ import annotations

import json
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


SKILL_ROOT = Path(__file__).resolve().parents[1]
REFERENCES = SKILL_ROOT / "references"
REGISTRY_PATH = REFERENCES / "blattregister.json"

ALLOWED_FLAGS = {
    "folgefehler",
    "unsicher",
    "nicht_lesbar",
    "nicht_bearbeitet",
    "nicht_eingereicht",
}
ZERO_FLAGS = {"nicht_lesbar", "nicht_bearbeitet", "nicht_eingereicht"}

INK_DEDUCTION_PATTERNS = [
    re.compile(r"schriftfarbe", re.IGNORECASE),
    re.compile(r"tintenfarbe", re.IGNORECASE),
    re.compile(r"stiftfarbe", re.IGNORECASE),
    re.compile(
        r"mit\s+(?:einem\s+)?(?:gr[üu]n\w*|rot\w*|blau\w*|schwarz\w*)\s+"
        r"(?:stift|kuli|kugelschreiber|f[üu]ller|marker)",
        re.IGNORECASE,
    ),
    re.compile(
        r"wegen\s+(?:der\s+)?(?:gr[üu]n\w*|rot\w*|blau\w*|schwarz\w*)\s+"
        r"(?:schrift|tinte|farbe)",
        re.IGNORECASE,
    ),
    re.compile(
        r"(?:gr[üu]n\w*|rot\w*|blau\w*|schwarz\w*)\s+geschrieben",
        re.IGNORECASE,
    ),
]


class GradingValidationError(ValueError):
    """Raised when a grading file violates the closed grading contract."""

    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("\n".join(errors))


def read_json(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise GradingValidationError([f"Datei nicht gefunden: {path}"]) from exc
    except json.JSONDecodeError as exc:
        raise GradingValidationError(
            [f"Ungültiges JSON in {path}: Zeile {exc.lineno}, Spalte {exc.colno}"]
        ) from exc
    if not isinstance(value, dict):
        raise GradingValidationError([f"JSON-Wurzel muss ein Objekt sein: {path}"])
    return value


def load_registry() -> dict[str, Any]:
    registry = read_json(REGISTRY_PATH)
    sheets = registry.get("sheets")
    if not isinstance(sheets, list) or len(sheets) != 5:
        raise GradingValidationError(
            ["Das Blattregister muss genau fünf Blätter enthalten."]
        )
    ids = [sheet.get("id") for sheet in sheets if isinstance(sheet, dict)]
    if len(set(ids)) != 5 or any(not value for value in ids):
        raise GradingValidationError(["Blatt-IDs müssen eindeutig und vollständig sein."])
    return registry


def sheet_entry(sheet_id: str) -> dict[str, Any]:
    registry = load_registry()
    for sheet in registry["sheets"]:
        if sheet["id"] == sheet_id:
            return sheet
    allowed = ", ".join(sheet["id"] for sheet in registry["sheets"])
    raise GradingValidationError(
        [f"Unbekannte Blatt-ID '{sheet_id}'. Erlaubt sind: {allowed}"]
    )


def load_rubric(sheet_id: str) -> dict[str, Any]:
    entry = sheet_entry(sheet_id)
    rubric_path = REFERENCES / entry["folder"] / "korrekturschema.json"
    rubric = read_json(rubric_path)
    if rubric.get("sheet_id") != sheet_id:
        raise GradingValidationError(
            [f"Blatt-ID im Korrekturschema stimmt nicht: {rubric_path}"]
        )
    return rubric


def _number(value: Any, location: str, errors: list[str]) -> Decimal | None:
    if isinstance(value, bool) or value is None:
        errors.append(f"{location}: 'erreicht' muss eine Zahl sein.")
        return None
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError):
        errors.append(f"{location}: ungültige Punktzahl {value!r}.")
        return None
    if not number.is_finite():
        errors.append(f"{location}: Punktzahl muss endlich sein.")
        return None
    if number * 2 != (number * 2).to_integral_value():
        errors.append(f"{location}: nur ganze oder halbe Punkte sind zulässig.")
    return number


def format_points(value: Decimal | float | int) -> str:
    number = Decimal(str(value))
    if number == number.to_integral_value():
        return str(int(number))
    return format(number.normalize(), "f").replace(".", ",")


def _ink_based_deduction(text: str) -> bool:
    return any(pattern.search(text) for pattern in INK_DEDUCTION_PATTERNS)


def validate_grading(data: dict[str, Any]) -> dict[str, Any]:
    """Validate grading data and return computed totals and normalized rows."""

    errors: list[str] = []
    sheet_id = data.get("sheet_id")
    if not isinstance(sheet_id, str) or not sheet_id:
        raise GradingValidationError(["'sheet_id' fehlt oder ist ungültig."])
    rubric = load_rubric(sheet_id)

    actual_tasks = data.get("aufgaben")
    if not isinstance(actual_tasks, list):
        raise GradingValidationError(["'aufgaben' muss eine Liste sein."])

    expected_tasks = rubric["tasks"]
    actual_task_ids = [str(task.get("id")) for task in actual_tasks if isinstance(task, dict)]
    expected_task_ids = [str(task["id"]) for task in expected_tasks]
    if actual_task_ids != expected_task_ids:
        errors.append(
            "Aufgabenliste ist unvollständig oder falsch sortiert. "
            f"Erwartet: {expected_task_ids}; gefunden: {actual_task_ids}."
        )

    actual_by_id = {
        str(task.get("id")): task for task in actual_tasks if isinstance(task, dict)
    }
    normalized_tasks: list[dict[str, Any]] = []
    overall_awarded = Decimal("0")
    overall_max = Decimal("0")

    for expected_task in expected_tasks:
        task_id = str(expected_task["id"])
        actual_task = actual_by_id.get(task_id)
        if actual_task is None:
            continue
        actual_parts = actual_task.get("teilaufgaben")
        if not isinstance(actual_parts, list):
            errors.append(f"Aufgabe {task_id}: 'teilaufgaben' muss eine Liste sein.")
            continue

        expected_parts = expected_task["parts"]
        actual_part_ids = [
            str(part.get("id")) for part in actual_parts if isinstance(part, dict)
        ]
        expected_part_ids = [str(part["id"]) for part in expected_parts]
        if actual_part_ids != expected_part_ids:
            errors.append(
                f"Aufgabe {task_id}: Teilaufgaben unvollständig oder falsch sortiert. "
                f"Erwartet: {expected_part_ids}; gefunden: {actual_part_ids}."
            )

        actual_parts_by_id = {
            str(part.get("id")): part
            for part in actual_parts
            if isinstance(part, dict)
        }
        task_awarded = Decimal("0")
        task_max = Decimal("0")
        normalized_parts: list[dict[str, Any]] = []

        for expected_part in expected_parts:
            part_id = str(expected_part["id"])
            maximum = Decimal(str(expected_part["max_points"]))
            task_max += maximum
            actual_part = actual_parts_by_id.get(part_id)
            location = f"Aufgabe {task_id}({part_id})"
            if actual_part is None:
                continue

            if Decimal(str(actual_part.get("maximal", maximum))) != maximum:
                errors.append(
                    f"{location}: Maximalpunkte dürfen nicht geändert werden "
                    f"({format_points(maximum)} erwartet)."
                )
            awarded = _number(actual_part.get("erreicht"), location, errors)
            if awarded is None:
                continue
            if awarded < 0 or awarded > maximum:
                errors.append(
                    f"{location}: {format_points(awarded)} liegt außerhalb von "
                    f"0 bis {format_points(maximum)}."
                )

            reason = actual_part.get("begruendung", "")
            comment = actual_part.get("kommentar", "")
            if not isinstance(reason, str):
                errors.append(f"{location}: 'begruendung' muss Text sein.")
                reason = ""
            if not isinstance(comment, str):
                errors.append(f"{location}: 'kommentar' muss Text sein.")
                comment = ""
            reason = reason.strip()
            comment = comment.strip()
            if awarded < maximum and not reason:
                errors.append(f"{location}: Bei Punktabzug fehlt die Begründung.")
            if awarded < maximum and _ink_based_deduction(reason):
                errors.append(
                    f"{location}: Schrift- oder Tintenfarbe darf kein Punktabzugsgrund sein. "
                    "Bewerte den Inhalt normal und verschiebe den Hinweis nach 'formale_hinweise'."
                )

            flags = actual_part.get("flags", [])
            if not isinstance(flags, list) or any(not isinstance(flag, str) for flag in flags):
                errors.append(f"{location}: 'flags' muss eine Liste von Textwerten sein.")
                flags = []
            unknown_flags = sorted(set(flags) - ALLOWED_FLAGS)
            if unknown_flags:
                errors.append(f"{location}: unbekannte Flags {unknown_flags}.")
            duplicate_flags = len(flags) != len(set(flags))
            if duplicate_flags:
                errors.append(f"{location}: Flags dürfen nicht doppelt vorkommen.")
            zero_flags = set(flags) & ZERO_FLAGS
            if len(zero_flags) > 1:
                errors.append(
                    f"{location}: nur eines von {sorted(ZERO_FLAGS)} darf gesetzt sein."
                )
            if zero_flags and awarded != 0:
                errors.append(
                    f"{location}: {sorted(zero_flags)} erfordert 0 erreichte Punkte."
                )

            task_awarded += awarded
            normalized_parts.append(
                {
                    "id": part_id,
                    "erreicht": awarded,
                    "maximal": maximum,
                    "begruendung": reason,
                    "kommentar": comment,
                    "flags": flags,
                }
            )

        declared_task_max = Decimal(str(expected_task["max_points"]))
        if task_max != declared_task_max:
            errors.append(
                f"Korrekturschema Aufgabe {task_id}: Teilpunkte ergeben "
                f"{format_points(task_max)}, Aufgabenkopf nennt "
                f"{format_points(declared_task_max)}."
            )
        overall_awarded += task_awarded
        overall_max += task_max
        normalized_tasks.append(
            {
                "id": task_id,
                "parts": normalized_parts,
                "erreicht": task_awarded,
                "maximal": task_max,
            }
        )

    feedback = data.get("wiederkehrende_fehler")
    if not isinstance(feedback, str) or not feedback.strip():
        errors.append("'wiederkehrende_fehler' muss als Fließtext ausgefüllt sein.")
        feedback = ""

    formal_notes = data.get("formale_hinweise", [])
    if not isinstance(formal_notes, list) or any(
        not isinstance(note, str) or not note.strip() for note in formal_notes
    ):
        errors.append("'formale_hinweise' muss eine Liste nichtleerer Texte sein.")
        formal_notes = []

    declared_total = Decimal(str(rubric["total_points"]))
    if overall_max != declared_total:
        errors.append(
            f"Korrekturschema: Aufgabensummen ergeben {format_points(overall_max)}, "
            f"Blattsumme nennt {format_points(declared_total)}."
        )

    if errors:
        raise GradingValidationError(errors)

    percentage = Decimal("0") if overall_max == 0 else overall_awarded / overall_max * 100
    return {
        "sheet": rubric,
        "tasks": normalized_tasks,
        "overall_awarded": overall_awarded,
        "overall_max": overall_max,
        "percentage": percentage,
        "feedback": feedback.strip(),
        "formal_notes": [note.strip() for note in formal_notes],
    }
