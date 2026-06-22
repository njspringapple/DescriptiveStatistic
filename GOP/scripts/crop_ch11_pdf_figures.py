from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".codex-tmp" / "lecture_chapters" / "11_Zusammenhangsmasse_metrische_Merkmale" / "pages"
DST = ROOT / "分章节讲义" / "中文讲义" / "11_Zusammenhangsmasse_metrische_Merkmale" / "assets"


FIGURES = [
    (4, "covariance_scatter", (120, 90, 920, 690)),
    (5, "covariance_quadrants", (120, 90, 920, 690)),
    (6, "covariance_heat_quadrants", (120, 90, 920, 690)),
    (9, "correlation_linear_only", (90, 90, 940, 690)),
    (10, "datasaurus_dozen_same_correlation", (60, 80, 980, 700)),
    (14, "scatterplot_matrix_simple", (80, 90, 950, 675)),
    (15, "scatterplot_matrix_enhanced", (80, 90, 950, 675)),
    (24, "bivariate_standard_normal_formula", (80, 95, 950, 670)),
    (25, "bivariate_normal_contours", (80, 95, 950, 660)),
    (26, "bivariate_normal_3d", (80, 95, 950, 660)),
    (27, "multivariate_normal_formula", (70, 90, 965, 675)),
    (32, "extreme_cases_rank_correlation", (140, 110, 880, 650)),
    (36, "kendall_tau_visualization", (80, 85, 950, 690)),
    (44, "deterministic_linear", (80, 85, 960, 690)),
    (45, "deterministic_nonlinear_waves", (80, 85, 960, 690)),
    (46, "deterministic_nonlinear_curves", (80, 85, 960, 690)),
    (47, "noisy_exact_relationships", (80, 85, 960, 690)),
    (48, "more_examples_correlation", (55, 80, 985, 690)),
    (55, "diagnostic_moderate_example_1", (55, 80, 985, 690)),
    (56, "diagnostic_moderate_example_2", (55, 80, 985, 690)),
    (57, "diagnostic_moderate_example_2b", (55, 80, 985, 690)),
    (58, "diagnostic_moderate_example_2c", (55, 80, 985, 690)),
    (59, "diagnostic_no_association_1", (55, 80, 985, 690)),
    (60, "diagnostic_no_association_2", (55, 80, 985, 690)),
    (61, "diagnostic_no_association_3", (55, 80, 985, 690)),
    (62, "diagnostic_strong_example", (55, 80, 985, 690)),
    (63, "roc_curve_with_ties", (155, 90, 870, 665)),
    (64, "auc_formula", (90, 95, 940, 650)),
    (67, "pima_scatterplot_matrix", (55, 80, 985, 700)),
    (68, "pima_boxplots_roc", (55, 80, 985, 700)),
    (69, "pima_boxplots_roc_more", (55, 80, 985, 700)),
    (72, "association_measures_table", (60, 90, 980, 640)),
]


def crop_all() -> list[Path]:
    DST.mkdir(parents=True, exist_ok=True)
    outputs = []
    for page, slug, box in FIGURES:
        img = Image.open(SRC / f"page-{page:02d}.png").convert("RGB")
        out = DST / f"fig-11-{page:02d}-{slug}.png"
        img.crop(box).save(out, optimize=True)
        outputs.append(out)
    return outputs


def make_contact_sheet(paths: list[Path]) -> Path:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((350, 225))
        canvas = Image.new("RGB", (370, 265), "white")
        canvas.paste(img, ((370 - img.width) // 2, 8))
        ImageDraw.Draw(canvas).text((8, 240), path.name, fill=(25, 25, 25))
        thumbs.append(canvas)
    cols = 2
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 370, rows * 265), "white")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 370, (i // cols) * 265))
    out = DST / "fig-11-contact-sheet.png"
    sheet.save(out, quality=90)
    return out


if __name__ == "__main__":
    paths = crop_all()
    contact = make_contact_sheet(paths)
    print(f"cropped {len(paths)} figures")
    print(contact)
