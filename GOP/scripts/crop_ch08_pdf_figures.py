from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".codex-tmp" / "lecture_chapters" / "08_Wichtige_parametrische_Verteilungen" / "pages"
DST = ROOT / "分章节讲义" / "中文讲义" / "08_Wichtige_parametrische_Verteilungen" / "assets"


FIGURES = [
    (8, "geometric_distribution", (105, 80, 940, 675)),
    (10, "binomial_distribution", (80, 70, 970, 700)),
    (13, "sampling_with_without_replacement_i", (80, 70, 970, 695)),
    (14, "sampling_with_without_replacement_ii", (80, 70, 970, 695)),
    (18, "poisson_distribution", (105, 80, 940, 675)),
    (20, "binomial_poisson_n10", (80, 70, 970, 695)),
    (21, "binomial_poisson_n100", (80, 70, 970, 695)),
    (22, "binomial_poisson_comparison", (80, 70, 970, 695)),
    (28, "exponential_distribution", (105, 80, 940, 675)),
    (30, "gamma_distribution", (105, 80, 940, 675)),
    (31, "gamma_distribution_shape", (105, 80, 940, 675)),
    (32, "gamma_distribution_more", (105, 80, 940, 675)),
    (35, "normal_distribution", (105, 80, 940, 675)),
    (38, "beta_distribution", (105, 80, 940, 675)),
    (40, "cauchy_vs_normal", (105, 80, 940, 675)),
    (44, "density_transformation_idea_1", (55, 65, 995, 705)),
    (45, "density_transformation_idea_2", (55, 65, 995, 705)),
    (46, "density_transformation_idea_3", (55, 65, 995, 705)),
    (53, "inverse_method_exponential", (90, 80, 950, 695)),
    (54, "inverse_method_normal", (90, 80, 950, 695)),
    (55, "inverse_method_nonmonotone", (90, 80, 950, 695)),
]


def crop_all() -> list[Path]:
    DST.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []
    for page, slug, box in FIGURES:
        src = SRC / f"page-{page:02d}.png"
        out = DST / f"fig-08-{page:02d}-{slug}.png"
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
        canvas.paste(img, ((380 - img.width) // 2, 10))
        draw = ImageDraw.Draw(canvas)
        draw.text((10, 242), path.name, fill=(25, 25, 25))
        thumbs.append(canvas)
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 380, rows * 270), "white")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 380, (i // cols) * 270))
    out = DST / "fig-08-contact-sheet.png"
    sheet.save(out, quality=90)
    return out


if __name__ == "__main__":
    paths = crop_all()
    contact = make_contact_sheet(paths)
    print(f"cropped {len(paths)} figures")
    print(contact)
