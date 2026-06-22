from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".codex-tmp" / "lecture_chapters" / "12_Korrelation_Kausalitaet" / "pages"
DST = ROOT / "分章节讲义" / "中文讲义" / "12_Korrelation_Kausalitaet" / "assets"


FIGURES = [
    (3, "correlation_causality_photo", (300, 90, 735, 600)),
    (4, "fork_collider_pipe", (125, 70, 930, 670)),
    (5, "fork_collider_pipe_association", (125, 70, 930, 670)),
    (11, "nachhilfe_marginal", (130, 85, 930, 675)),
    (12, "nachhilfe_by_groups", (115, 80, 950, 680)),
    (13, "nachhilfe_simpson_groups", (70, 65, 985, 700)),
    (16, "titanic_marginal", (70, 85, 950, 675)),
    (17, "titanic_conditioned_gender", (55, 75, 980, 700)),
    (18, "berkeley_marginal", (55, 75, 975, 700)),
    (19, "berkeley_departments", (25, 65, 1000, 705)),
    (20, "berkeley_applications_plot", (115, 75, 930, 690)),
    (25, "income_childmortality_regions", (85, 80, 945, 690)),
    (26, "income_childmortality_countries", (85, 80, 945, 690)),
    (27, "income_childmortality_labeled", (85, 80, 945, 690)),
    (28, "income_childmortality_facets", (25, 65, 1000, 705)),
    (31, "collider_students_negative", (95, 75, 945, 700)),
    (32, "collider_population_none", (95, 75, 945, 700)),
    (33, "collider_student_selection", (95, 75, 945, 700)),
    (36, "selection_x_plus_y", (75, 80, 965, 690)),
    (37, "selection_abs_difference", (75, 80, 965, 690)),
]


def crop_all() -> list[Path]:
    DST.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for page, slug, box in FIGURES:
        src = SRC / f"page-{page:02d}.png"
        out = DST / f"fig-12-{page:02d}-{slug}.png"
        img = Image.open(src).convert("RGB")
        img.crop(box).save(out, optimize=True)
        outputs.append(out)
    return outputs


def make_contact_sheet(paths: list[Path]) -> Path:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((360, 230))
        canvas = Image.new("RGB", (380, 270), "white")
        x = (380 - img.width) // 2
        canvas.paste(img, (x, 10))
        draw = ImageDraw.Draw(canvas)
        draw.text((10, 242), path.name, fill=(30, 30, 30))
        thumbs.append(canvas)

    cols = 2
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 380, rows * 270), "white")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 380, (i // cols) * 270))
    out = DST / "fig-12-contact-sheet.png"
    sheet.save(out, quality=90)
    return out


if __name__ == "__main__":
    paths = crop_all()
    contact = make_contact_sheet(paths)
    print(f"cropped {len(paths)} figures")
    print(contact)
