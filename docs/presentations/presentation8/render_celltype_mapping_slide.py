#!/usr/bin/env python3
"""Render a 16:9 presentation slide from spatial_breast_celltype_mapping.py."""

import os
import subprocess
from xml.sax.saxutils import escape

HERE = os.path.dirname(os.path.abspath(__file__))
MAPPING_FILE = os.path.join(HERE, "spatial_breast_celltype_mapping.py")
BASENAME = os.path.join(HERE, "spatial_breast_celltype_mapping_slide")

W, H = 1920, 1080
M = 80                      # page margin
CONTENT_R = W - M           # 1840

FONT = "Arial, Helvetica, sans-serif"
FS_TITLE, FS_SUB, FS_STAT = 40, 22, 18
FS_PILL, FS_PILL_SUB = 21, 13
FS_CHIP, FS_NOTE = 19, 15

# coarse type -> (fill, tint)
GROUPS = [
    ("Epithelial cell",      "#7E57C2", "#F1EAFA"),
    ("T cell",               "#1E88E5", "#E6F1FC"),
    ("Natural killer cell",  "#00838F", "#DEF2F4"),
    ("B cell",               "#2E7D32", "#E7F4E8"),
    ("Plasma cell",          "#6D4C41", "#F1EBE8"),
    ("Myeloid cell",         "#E65100", "#FFF0E3"),
    ("Stromal cell",         "#C2185B", "#FAE6EE"),
    ("Endothelial cell",     "#D32F2F", "#FCE9E9"),
]

PILL_W, PILL_H = 296, 68
ARROW_LEN = 52
CONT_X = M + PILL_W + ARROW_LEN + 24      # 452
CONT_W = CONTENT_R - CONT_X               # 1388
CONT_PAD_X, CONT_PAD_Y = 22, 14
CHIP_H, CHIP_GAP, LINE_GAP = 42, 10, 10
CHIP_PAD_X = 15
EPS_ANNOT = "17 Subcluster (epi_0 … epi_low_ent) → ein Label · coarse = fine"


def load_mapping():
    ns = {}
    with open(MAPPING_FILE, encoding="utf-8") as fh:
        exec(compile(fh.read(), MAPPING_FILE, "exec"), ns)
    return ns["mapping"]


def text_w(s, size, bold=False):
    """Rough advance width for Arial-like fonts."""
    narrow = "iljtfrI.,:;'|!()[]- "
    wide = "MWmw@%"
    w = 0.0
    for ch in s:
        if ch in narrow:
            w += 0.30
        elif ch in wide:
            w += 0.86
        elif ch.isupper():
            w += 0.68
        elif ch.isdigit():
            w += 0.56
        else:
            w += 0.53
    return w * size * (1.05 if bold else 1.0)


def wrap(chips, max_w):
    lines, cur, cur_w = [], [], 0
    for c in chips:
        add = c["w"] if not cur else c["w"] + CHIP_GAP
        if cur and cur_w + add > max_w:
            lines.append(cur)
            cur, cur_w = [c], c["w"]
        else:
            cur.append(c)
            cur_w += add
    if cur:
        lines.append(cur)
    return lines


def chip_svg(c, x, y, color):
    return (
        f'<rect x="{x}" y="{y}" width="{c["w"]}" height="{CHIP_H}" rx="10" '
        f'fill="#FFFFFF" stroke="{color}" stroke-opacity="0.45" stroke-width="1.4"/>'
        f'<text x="{x + c["w"] / 2:.1f}" y="{y + CHIP_H / 2 + FS_CHIP * 0.35:.1f}" '
        f'font-family="{FONT}" font-size="{FS_CHIP}" fill="{color}" '
        f'text-anchor="middle">{escape(c["label"])}</text>'
    )


def main():
    mapping = load_mapping()
    fine_by_coarse = {}
    for _key, (coarse, fine) in mapping.items():
        fine_by_coarse.setdefault(coarse, [])
        if fine not in fine_by_coarse[coarse]:
            fine_by_coarse[coarse].append(fine)

    total_fine = sum(len(v) for v in fine_by_coarse.values())
    max_chip_w = CONT_W - 2 * CONT_PAD_X

    rows = []
    for name, color, tint in GROUPS:
        chips = [
            {"label": f, "w": max(72, text_w(f, FS_CHIP) + 2 * CHIP_PAD_X)}
            for f in fine_by_coarse[name]
        ]
        lines = wrap(chips, max_chip_w)
        nlab = len(fine_by_coarse[name])
        sub = (
            "17 Subcluster → 1 Label"
            if name == "Epithelial cell"
            else f"{nlab} fine-grained label" + ("" if nlab == 1 else "s")
        )
        natural = max(
            PILL_H,
            CONT_PAD_Y * 2 + len(lines) * CHIP_H + (len(lines) - 1) * LINE_GAP,
        )
        rows.append(
            {"name": name, "color": color, "tint": tint,
             "lines": lines, "sub": sub, "h": natural}
        )

    top, bottom = 176, 1012
    avail = bottom - top
    gap = (avail - sum(r["h"] for r in rows)) / (len(rows) - 1)
    gap = max(10.0, min(gap, 26.0))

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}">',
        f'<rect width="{W}" height="{H}" fill="#FFFFFF"/>',
        # Title block
        f'<text x="{M}" y="66" font-family="{FONT}" font-size="{FS_TITLE}" '
        f'font-weight="bold" fill="#1F2933">Spatial Breast – Cell-Type Mapping</text>',
        f'<text x="{M}" y="104" font-family="{FONT}" font-size="{FS_SUB}" '
        f'fill="#616E7C">Coarse cell types → fine-grained cell types</text>',
        f'<text x="{CONTENT_R}" y="104" font-family="{FONT}" font-size="{FS_STAT}" '
        f'fill="#9AA5B1" text-anchor="end">'
        f'{len(GROUPS)} coarse cell types · {total_fine} fine-grained labels</text>',
        f'<line x1="{M}" y1="126" x2="{CONTENT_R}" y2="126" '
        f'stroke="#E4E7EB" stroke-width="2"/>',
        f'<text x="{M}" y="154" font-family="{FONT}" font-size="12" '
        f'letter-spacing="1.6" fill="#9AA5B1">COARSE CELL TYPE</text>',
        f'<text x="{CONT_X + CONT_PAD_X}" y="154" font-family="{FONT}" font-size="12" '
        f'letter-spacing="1.6" fill="#9AA5B1">FINE-GRAINED CELL TYPES</text>',
    ]

    y = top
    for row in rows:
        name, color, tint, h = row["name"], row["color"], row["tint"], row["h"]
        cy = y + h / 2

        # container
        out.append(
            f'<rect x="{CONT_X}" y="{y}" width="{CONT_W}" height="{h}" rx="16" '
            f'fill="{tint}" stroke="{color}" stroke-opacity="0.28" stroke-width="1.2"/>'
        )

        # coarse pill
        py = cy - PILL_H / 2
        out.append(
            f'<rect x="{M}" y="{py}" width="{PILL_W}" height="{PILL_H}" rx="14" fill="{color}"/>'
        )
        if row["sub"]:
            out.append(
                f'<text x="{M + PILL_W / 2}" y="{cy - 2}" font-family="{FONT}" '
                f'font-size="{FS_PILL}" font-weight="bold" fill="#FFFFFF" '
                f'text-anchor="middle">{escape(name)}</text>'
                f'<text x="{M + PILL_W / 2}" y="{cy + 17}" font-family="{FONT}" '
                f'font-size="{FS_PILL_SUB}" fill="#FFFFFF" fill-opacity="0.85" '
                f'text-anchor="middle">{escape(row["sub"])}</text>'
            )
        else:
            out.append(
                f'<text x="{M + PILL_W / 2}" y="{cy + 7}" font-family="{FONT}" '
                f'font-size="{FS_PILL}" font-weight="bold" fill="#FFFFFF" '
                f'text-anchor="middle">{escape(name)}</text>'
            )

        # arrow
        ax1, ax2 = M + PILL_W + 10, CONT_X - 12
        out.append(
            f'<line x1="{ax1}" y1="{cy}" x2="{ax2}" y2="{cy}" stroke="{color}" '
            f'stroke-width="2.2" stroke-opacity="0.75" marker-end="url(#arrow-{color[1:]})"/>'
        )

        # chips
        lines = row["lines"]
        block_h = len(lines) * CHIP_H + (len(lines) - 1) * LINE_GAP
        line_y = y + (h - block_h) / 2
        first_chip_x = CONT_X + CONT_PAD_X
        for line in lines:
            cx = first_chip_x
            for c in line:
                out.append(chip_svg(c, cx, line_y, color))
                cx += c["w"] + CHIP_GAP
            line_y += CHIP_H + LINE_GAP

        if name == "Epithelial cell":
            note_x = first_chip_x + row["lines"][0][0]["w"] + 18
            out.append(
                f'<text x="{note_x}" y="{cy + FS_NOTE * 0.35:.1f}" font-family="{FONT}" '
                f'font-size="{FS_NOTE}" fill="#7B8794">{escape(EPS_ANNOT)}</text>'
            )

        y += h + gap

    # footnote
    out.append(
        f'<text x="{M}" y="1056" font-family="{FONT}" font-size="15" fill="#9AA5B1">'
        f'Hinweis: 17 epitheliale Subcluster (epi_0 … epi_low_ent) werden zu einem '
        f'gemeinsamen Label »Epithelial cell« zusammengefasst (coarse = fine).</text>'
    )

    markers = "".join(
        f'<marker id="arrow-{c[1:]}" viewBox="0 0 10 10" refX="9" refY="5" '
        f'markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
        f'<path d="M 0 0 L 10 5 L 0 10 z" fill="{c}" fill-opacity="0.75"/></marker>'
        for _, c, _ in GROUPS
    )
    out.insert(1, f"<defs>{markers}</defs>")
    out.append("</svg>")

    with open(BASENAME + ".svg", "w", encoding="utf-8") as fh:
        fh.write("\n".join(out))

    subprocess.run(
        ["rsvg-convert", "-w", str(W), "-h", str(H),
         "-o", BASENAME + ".png", BASENAME + ".svg"],
        check=True,
    )
    subprocess.run(
        ["rsvg-convert", "-f", "pdf", "-o", BASENAME + ".pdf", BASENAME + ".svg"],
        check=True,
    )
    print("wrote", BASENAME + ".svg")
    print("wrote", BASENAME + ".png")
    print("wrote", BASENAME + ".pdf")


if __name__ == "__main__":
    main()
