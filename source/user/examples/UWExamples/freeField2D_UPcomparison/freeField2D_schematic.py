"""Draw the layered 2D free-field problem and history-comparison locations.

Run: python freeField2D_schematic.py
Writes PNG, SVG and PDF versions into figures/.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
INK = "#19324A"
MUTED = "#53677B"
WATER = "#008CA8"
LAYERS = (
    (1, 0, 20, "#C9DFEF", "#3D759E"),
    (2, 20, 28, "#F5D8AA", "#AA7030"),
    (3, 28, 30, "#DED5EE", "#7E629F"),
)


def dimension(axis, x, lower, upper, label, *, overall=False):
    color = INK if overall else MUTED
    axis.annotate("", (x, upper), (x, lower),
                  arrowprops=dict(arrowstyle="<->", color=color, lw=1.1,
                                  shrinkA=0, shrinkB=0))
    for y in (lower, upper):
        axis.plot([x - 0.15, -0.15], [y, y], color=color, lw=0.55, alpha=0.5)
    axis.text(x - 0.22, (lower + upper) / 2, label, color=color,
              fontsize=12 if overall else 10, rotation=90 if overall else 0,
              ha="right", va="center")


def main() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "none"})
    figure = plt.figure(figsize=(11, 10), facecolor="white")
    figure.text(0.075, 0.95, "2D FREE-FIELD SOIL COLUMN", fontsize=22,
                fontweight="bold", color=INK)
    figure.text(0.075, 0.913, "Plane strain  /  SSPquadUP or Tri31UP  /  out-of-plane thickness: 2 m",
                fontsize=11, color=MUTED)
    axis = figure.add_axes((0.075, 0.12, 0.87, 0.76))
    axis.set_xlim(-5, 12)
    axis.set_ylim(-6, 35)
    axis.axis("off")
    # The displayed width is exaggerated for readability; dimensions are actual.
    left, right = 0.0, 2.8
    for layer, bottom, top, fill, accent in LAYERS:
        axis.add_patch(Rectangle((left, bottom), right, top - bottom,
                                  facecolor=fill, edgecolor="none"))
        axis.text((left + right) / 2, (bottom + top) / 2, f"LAYER {layer}",
                  color=accent, fontsize=12 if layer != 3 else 10,
                  fontweight="bold", ha="center", va="center")
    axis.add_patch(Rectangle((left, 0), right, 30, fill=False, edgecolor=INK, lw=1.6))
    axis.plot([left, right], [20, 20], color=INK, lw=1.0)
    # Elastic half-space below the column; not an extra soil layer.
    axis.add_patch(Rectangle((-0.2, -1.1), right + 0.4, 1.1,
                              facecolor="#E6EBF0", edgecolor="#98A8B6", hatch="///", lw=0.5))
    axis.plot([left, right], [0, 0], color=INK, lw=2)

    dimension(axis, -3.0, 0, 30, "30 m", overall=True)
    for _, bottom, top, _, _ in LAYERS:
        dimension(axis, -0.9, bottom, top, f"{top-bottom} m")
    axis.annotate("", (left, 33), (right, 33),
                  arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1, shrinkA=0, shrinkB=0))
    for x in (left, right):
        axis.plot([x, x], [30.5, 33.5], color=MUTED, lw=0.6)
    axis.text((left + right) / 2, 33.5, "2 m width", ha="center", color=INK, fontsize=11)

    # Water table coincides with the layer 2 / layer 3 interface.
    axis.plot([-0.25, 5.0], [28, 28], color=WATER, lw=1.8, dashes=(5, 3))
    axis.add_patch(Polygon(((4.55, 28.5), (4.95, 28.5), (4.75, 28)),
                            closed=True, facecolor=WATER, edgecolor=WATER))
    axis.plot([4.9, 5.7], [28, 28], color=WATER, lw=1.0)
    axis.text(6.0, 28.0, "WATER TABLE", fontsize=11, color=WATER,
              va="center", fontweight="bold")
    axis.text(6.0, 26.7, "y = 28 m  ·  2 m below surface", fontsize=10, color=MUTED)

    # These are representative elevations: each history averages both end nodes.
    for name, y, text_y, title, nodes in (
        ("P1", 15, 15, "Mid-column", "61 and 62"),
        ("P2", 30, 31.3, "Ground surface", "121 and 122"),
    ):
        axis.plot([left, right], [y, y], color=INK, lw=1.1, dashes=(3, 3))
        axis.scatter([left, right], [y, y], s=52, facecolor="white",
                     edgecolor=INK, linewidth=1.6, zorder=5)
        axis.scatter([(left + right) / 2], [y], s=46, color=INK, marker="D", zorder=5)
        axis.plot([right + 0.12, 5.3, 5.7], [y, text_y, text_y], color=INK, lw=1.0)
        axis.text(6.0, text_y, f"{name}  {title}", fontsize=12, color=INK,
                  fontweight="bold", va="center")
        axis.text(6.0, text_y - 1.3, f"y = {y} m  ·  average of nodes {nodes}",
                  fontsize=9.5, color=MUTED)

    # A horizontal incident-wave load and the absorbing boundary act at the base.
    axis.annotate("", (right - 0.15, -2.4), (left + 0.15, -2.4),
                  arrowprops=dict(arrowstyle="<->", color="#BE593C", lw=2.4))
    axis.annotate("", (left, 0), (left, -2.4),
                  arrowprops=dict(arrowstyle="-", color="#BE593C", lw=1.1))
    axis.text(6.0, -0.8, "HORIZONTAL MOTION INPUT", fontsize=11,
              color="#BE593C", fontweight="bold")
    axis.text(6.0, -2.15, r"At the base: $F_x(t)=c\,v_{in}(t)$", color=MUTED, fontsize=10)
    axis.plot([right + 0.15, 5.5], [-2.4, -2.4], color="#BE593C", lw=1.0)
    axis.text((left + right) / 2, -4.0, "Elastic half-space\nHorizontal Lysmer dashpot",
              ha="center", va="center", color=MUTED, fontsize=10, linespacing=1.5)
    axis.annotate("", (10.0, 4.1), (10.0, 1.1),
                  arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    axis.annotate("", (11.4, 1.1), (10.0, 1.1),
                  arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
    axis.text(9.7, 4.3, "y", color=MUTED, fontsize=10)
    axis.text(11.5, 0.9, "x", color=MUTED, fontsize=10)

    figure.text(0.075, 0.075, "Comparison histories: horizontal displacement, vertical displacement and pore pressure.",
                fontsize=10, color=INK)
    figure.text(0.075, 0.05, "Diamonds mark comparison elevations; circles mark the two averaged nodes. Width exaggerated for clarity.",
                fontsize=9, color=MUTED)
    FIGURES.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "svg", "pdf"):
        output = FIGURES / f"freeField2D_schematic.{suffix}"
        figure.savefig(output, dpi=240, facecolor="white")
        print(f"Wrote {output}")
    plt.close(figure)


if __name__ == "__main__":
    main()
