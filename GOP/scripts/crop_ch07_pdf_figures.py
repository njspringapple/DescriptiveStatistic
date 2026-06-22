from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
PAGE_DIR = ROOT / ".codex-tmp" / "ch07_pages"
ASSET_DIR = ROOT / "分章节讲义" / "07_Kennwerte_Verteilungseigenschaften_assets"

# Coordinates are in pixels on 200 dpi renderings created by pdftoppm.
# Each crop keeps the plotted object plus its axis labels/caption when useful.
CROPS = [
    (9, "boxplot_5_punkte", (95, 245, 940, 625)),
    (12, "boxplot_mietspiegel_einfach_modifiziert", (145, 120, 880, 610)),
    (13, "gruppierter_boxplot_mietspiegel", (75, 95, 960, 625)),
    (47, "streuungszerlegung_nettomiete_zimmerzahl", (20, 20, 980, 720)),
    (56, "bimodale_zinssaetze", (20, 20, 1005, 700)),
    (58, "symmetrie_schiefe_verteilungen", (145, 150, 875, 535)),
    (62, "woelbung_extremwerte_dichteplots", (85, 285, 935, 715)),
    (64, "kurtosis_theoretisches_schaubild", (20, 20, 860, 720)),
    (65, "woelbung_extremwerte_praktische_beispiele", (75, 170, 945, 675)),
    (74, "lorenzkurve_gleichverteilung", (20, 20, 960, 705)),
    (75, "lorenzkurve_vollstaendige_konzentration", (20, 20, 960, 705)),
    (77, "gini_flaeche_lorenzkurve", (55, 130, 945, 575)),
    (82, "lorenzkurve_deutsche_vermoegensverteilung", (70, 125, 950, 705)),
    (83, "gini_index_vermoegen_deutschland", (135, 115, 895, 585)),
    (84, "gini_index_einkommen_deutschland", (135, 115, 895, 535)),
]


def main() -> None:
    ASSET_DIR.mkdir(parents=True, exist_ok=True)
    generated = []
    for page_no, slug, box in CROPS:
        source = PAGE_DIR / f"page-{page_no:02d}.png"
        with Image.open(source) as im:
            cropped = im.crop(box)
            out = ASSET_DIR / f"fig-07-{page_no:02d}-{slug}.png"
            cropped.save(out)
            generated.append(out)

    thumbs = []
    for out in generated:
        im = Image.open(out).convert("RGB")
        im.thumbnail((300, 220))
        thumbs.append((out.name, im.copy()))

    cols = 3
    cell_w, cell_h = 340, 260
    rows = (len(thumbs) + cols - 1) // cols
    sheet = Image.new("RGB", (cols * cell_w, rows * cell_h), "white")
    draw = ImageDraw.Draw(sheet)
    for idx, (name, thumb) in enumerate(thumbs):
        x = (idx % cols) * cell_w
        y = (idx // cols) * cell_h
        sheet.paste(thumb, (x + (cell_w - thumb.width) // 2, y + 8))
        draw.text((x + 8, y + 228), name[:48], fill=(0, 0, 0))
    contact = ROOT / ".codex-tmp" / "ch07_extract" / "figure_contact_sheet.jpg"
    sheet.save(contact, quality=90)

    print(f"generated={len(generated)}")
    for out in generated:
        print(out.relative_to(ROOT))
    print(contact.relative_to(ROOT))


if __name__ == "__main__":
    main()
