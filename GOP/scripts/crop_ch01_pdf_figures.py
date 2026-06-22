from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".codex-tmp" / "lecture_chapters" / "01_Einfuehrung" / "pages"
DST = ROOT / "分章节讲义" / "中文讲义" / "01_Einfuehrung" / "assets"


FIGURES = [
    (3, "bundestagswahl_result", (250, 170, 990, 635)),
    (5, "wahlfaelschung_heatmap", (450, 145, 930, 600)),
    (7, "koala_poll_chart", (70, 105, 960, 655)),
    (8, "koala_simulation_chart", (70, 105, 960, 655)),
    (10, "isar_hazelnut_price_blue", (260, 205, 950, 645)),
    (11, "isar_hazelnut_price_alert", (260, 205, 950, 645)),
    (15, "umweltzone_prinzregentenstrasse", (80, 95, 950, 675)),
    (16, "umweltzone_lothstrasse", (80, 95, 950, 675)),
    (43, "big_data_velocity_volume_variety", (105, 70, 925, 690)),
    (55, "theory_reality_empirie_triangle", (170, 110, 860, 600)),
    (56, "theory_empirie_statistics_diagram", (100, 85, 930, 665)),
    (58, "math_formalism_empirie_table", (20, 95, 980, 640)),
]


def crop_all() -> list[Path]:
    DST.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for page, slug, box in FIGURES:
        img = Image.open(SRC / f"page-{page:02d}.png").convert("RGB")
        out = DST / f"fig-01-{page:02d}-{slug}.png"
        img.crop(box).save(out, optimize=True)
        outputs.append(out)
    return outputs


def make_contact_sheet(paths: list[Path]) -> Path:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((360, 230))
        canvas = Image.new("RGB", (380, 270), "white")
        canvas.paste(img, ((380 - img.width) // 2, 10))
        ImageDraw.Draw(canvas).text((10, 242), path.name, fill=(25, 25, 25))
        thumbs.append(canvas)
    cols = 2
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 380, rows * 270), "white")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 380, (i // cols) * 270))
    out = DST / "fig-01-contact-sheet.png"
    sheet.save(out, quality=90)
    return out


if __name__ == "__main__":
    paths = crop_all()
    contact = make_contact_sheet(paths)
    print(f"cropped {len(paths)} figures")
    print(contact)
