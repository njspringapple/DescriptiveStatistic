from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / ".codex-tmp" / "lecture_chapters" / "06_Statistische_Grafiken" / "pages"
DST = ROOT / "分章节讲义" / "中文讲义" / "06_Statistische_Grafiken" / "assets"


FIGURES = [
    (7, "geometries_examples", (55, 85, 980, 640)),
    (8, "aesthetics_examples", (55, 85, 980, 640)),
    (11, "perception_graph_types", (55, 95, 980, 620)),
    (12, "perception_experiment", (60, 85, 975, 690)),
    (17, "infoviz_beer_jugs", (60, 85, 980, 660)),
    (18, "beer_plot_zero_axis", (110, 90, 900, 690)),
    (19, "beer_plot_truncated_axis", (110, 90, 900, 690)),
    (20, "infoviz_bubbles", (80, 85, 965, 650)),
    (21, "students_stacked_bar", (85, 85, 930, 690)),
    (22, "students_grouped_bar", (85, 85, 930, 690)),
    (23, "infoviz_people_bubbles", (75, 85, 960, 650)),
    (24, "statistical_alternative_plot", (105, 90, 930, 690)),
    (29, "color_vision_simulation", (70, 80, 970, 690)),
    (31, "hcl_color_space", (180, 100, 850, 610)),
    (32, "color_hue_examples", (65, 90, 980, 630)),
    (33, "luminance_saturation_examples", (65, 90, 980, 630)),
    (34, "hcl_color_wheel_variants", (75, 90, 955, 660)),
    (35, "color_scale_types", (80, 100, 945, 610)),
    (36, "nominal_color_scales", (80, 100, 945, 650)),
    (37, "map_color_scale_bad_good", (65, 90, 970, 690)),
    (38, "sequential_color_scales", (80, 100, 945, 620)),
    (39, "sequential_map_examples", (65, 90, 970, 690)),
    (40, "diverging_color_scales", (80, 100, 945, 620)),
    (41, "diverging_map_examples", (65, 90, 970, 690)),
    (42, "diverging_bad_example", (190, 95, 825, 690)),
    (47, "stacked_vs_grouped_bar", (85, 90, 945, 690)),
    (50, "stacked_bar_mietspiegel", (100, 90, 925, 690)),
    (52, "pie_chart_klein_kalt", (90, 85, 945, 690)),
    (53, "pie_vs_stacked_bar", (90, 85, 945, 690)),
    (56, "dotplot_example", (95, 85, 940, 690)),
    (57, "grouped_dotplot", (95, 85, 940, 690)),
    (58, "conditional_dotplot", (95, 85, 940, 690)),
    (59, "bad_scatter_plot", (95, 85, 940, 690)),
    (61, "histogram_bad_binning", (80, 85, 960, 690)),
    (67, "histogram_density_example_1", (90, 85, 940, 690)),
    (68, "histogram_density_example_2", (90, 85, 940, 690)),
    (69, "histogram_density_example_3", (90, 85, 940, 690)),
    (72, "kernel_density_example", (100, 85, 930, 690)),
    (73, "kernel_density_histogram", (80, 85, 960, 690)),
    (74, "kernel_density_shifted", (80, 85, 960, 690)),
    (75, "bandwidth_examples", (70, 80, 970, 690)),
    (76, "kernel_density_bandwidth", (90, 85, 940, 690)),
    (80, "scatter_positive", (90, 85, 940, 690)),
    (81, "scatter_negative", (90, 85, 940, 690)),
    (82, "large_scatter_overplotting", (70, 85, 970, 690)),
    (83, "alpha_density_2d", (70, 85, 970, 690)),
    (84, "3d_density_bad", (80, 85, 960, 690)),
    (85, "scatter_discrete_third_variable", (70, 85, 970, 690)),
    (86, "scatter_discrete_third_variable_facets", (70, 85, 970, 690)),
    (87, "scatter_discrete_third_variable_density", (70, 85, 970, 690)),
    (88, "scatter_continuous_third_variable", (70, 85, 970, 690)),
    (89, "scatter_continuous_third_variable_colored", (70, 85, 970, 690)),
    (90, "scatter_grouped_third_variable", (70, 85, 970, 690)),
    (91, "scatter_grouped_third_variable_density", (70, 85, 970, 690)),
]


def crop_all() -> list[Path]:
    DST.mkdir(parents=True, exist_ok=True)
    outputs = []
    for page, slug, box in FIGURES:
        img = Image.open(SRC / f"page-{page:02d}.png").convert("RGB")
        out = DST / f"fig-06-{page:02d}-{slug}.png"
        img.crop(box).save(out, optimize=True)
        outputs.append(out)
    return outputs


def make_contact_sheet(paths: list[Path]) -> Path:
    thumbs = []
    for path in paths:
        img = Image.open(path).convert("RGB")
        img.thumbnail((310, 205))
        canvas = Image.new("RGB", (330, 245), "white")
        canvas.paste(img, ((330 - img.width) // 2, 8))
        ImageDraw.Draw(canvas).text((8, 220), path.name, fill=(25, 25, 25))
        thumbs.append(canvas)
    cols = 3
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * 330, rows * 245), "white")
    for i, thumb in enumerate(thumbs):
        sheet.paste(thumb, ((i % cols) * 330, (i // cols) * 245))
    out = DST / "fig-06-contact-sheet.png"
    sheet.save(out, quality=90)
    return out


if __name__ == "__main__":
    paths = crop_all()
    contact = make_contact_sheet(paths)
    print(f"cropped {len(paths)} figures")
    print(contact)
