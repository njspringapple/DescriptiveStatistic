#!/usr/bin/env python3
"""Create a complete grading JSON template for one registered GOP sheet."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from common import GradingValidationError, load_rubric


def build_template(sheet_id: str) -> dict:
    rubric = load_rubric(sheet_id)
    return {
        "schema_version": "1.0",
        "sheet_id": sheet_id,
        "aufgaben": [
            {
                "id": str(task["id"]),
                "teilaufgaben": [
                    {
                        "id": str(part["id"]),
                        "maximal": part["max_points"],
                        "erreicht": None,
                        "begruendung": "",
                        "kommentar": "",
                        "flags": [],
                    }
                    for part in task["parts"]
                ],
            }
            for task in rubric["tasks"]
        ],
        "wiederkehrende_fehler": "",
        "formale_hinweise": [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Erzeugt eine vollständige Bewertungsdatei für ein GOP-Blatt."
    )
    parser.add_argument("sheet_id", help="Blatt-ID aus references/blattregister.json")
    parser.add_argument("output", type=Path, help="Zielpfad der JSON-Datei")
    args = parser.parse_args()
    try:
        template = build_template(args.sheet_id)
    except GradingValidationError as exc:
        parser.error(str(exc))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        json.dump(template, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"Bewertungsvorlage erstellt: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

