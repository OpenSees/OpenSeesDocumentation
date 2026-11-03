"""Draw an axonometric schematic of the layered 3D free-field column.

Run: python freeField3D_schematic.py
Writes PNG, SVG and PDF versions into figures/.
Vertical dimensions are proportional; horizontal dimensions are exaggerated.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgb
from matplotlib.patches import Polygon


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
INK = "#19324A"
MUTED = "#53677B"
WATER = "#008CA8"
INPUT = "#BE593C"
LAYERS = (
    (1, 0, 20, "#C9DFEF", "#3D759E"),
    (2, 20, 28, "#F5D8AA", "#AA7030"),
    (3, 28, 30, "#DED5EE", "#7E629F"),
)


def project(x, y, z):
    """Oblique projection: x right, y up, z recedes up and right."""
    return 1.1 * x + 0.6 * z, y + 0.6 * z


def face(axis, coordinates, **kwargs):
    axis.add_patch(Polygon([project(*point) for point in coordinates], closed=True, **kwargs))


def ring(axis, elevation, **kwargs):
    corners = [(0, elevation, 0), (2, elevation, 0),
               (2, elevation, 2), (0, elevation, 2), (0, elevation, 0)]
    xs, ys = zip(*(project(*point) for point in corners))
    axis.plot(xs, ys, **kwargs)


def dimension(axis, x, bottom, top, text, overall=False):
    axis.annotate("", (x, top), (x, bottom),
                  arrowprops=dict(arrowstyle="<->", color=MUTED, lw=1.1,
                                  shrinkA=0, shrinkB=0))
    for y in (bottom, top):
        axis.plot([x - 0.15, -0.15], [y, y], color=MUTED, lw=0.55, alpha=0.5)
    axis.text(x - 0.2, (bottom + top) / 2, text, ha="right", va="center",
              fontsize=12 if overall else 10, color=INK if overall else MUTED,
              rotation=90 if overall else 0)


def main() -> None:
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "svg.fonttype": "none"})
    figure = plt.figure(figsize=(11, 10), facecolor="white")
    figure.text(0.075, 0.95, "3D FREE-FIELD SOIL COLUMN", fontsize=22,
                fontweight="bold", color=INK)
    figure.text(0.075, 0.913, "Three-dimensional model  /  2 m × 2 m footprint  /  horizontal input along x",
                fontsize=11, color=MUTED)
    axis = figure.add_axes((0.075, 0.12, 0.87, 0.76))
    axis.set_xlim(-5, 12)
    axis.set_ylim(-6, 36)
    axis.axis("off")

    # Filled front and right faces reveal the finite out-of-plane dimension.
    for layer, bottom, top, fill, accent in LAYERS:
        darker = tuple(channel * 0.85 for channel in to_rgb(fill))
        face(axis, [(2, bottom, 0), (2, bottom, 2), (2, top, 2), (2, top, 0)],
             facecolor=darker, edgecolor=INK, lw=1.0)
        face(axis, [(0, bottom, 0), (2, bottom, 0), (2, top, 0), (0, top, 0)],
             facecolor=fill, edgecolor=INK, lw=1.0)
        axis.text(1.1, (bottom + top) / 2, f"LAYER {layer}", ha="center", va="center",
                  fontsize=12 if layer != 3 else 9, fontweight="bold", color=accent)
    face(axis, [(0, 30, 0), (2, 30, 0), (2, 30, 2), (0, 30, 2)],
         facecolor="#EEE8F6", edgecolor=INK, lw=1.2)
    # Hidden vertical corner indicates the back of the column.
    bx, by = project(0, 0, 2)
    axis.plot([bx, bx], [by, by + 30], color=INK, lw=0.8, alpha=0.35, dashes=(3, 4))

    # Elastic base drawn as a shallow 3D plinth, rather than an extra soil layer.
    face(axis, [(-0.15, -1.1, -0.15), (2.15, -1.1, -0.15),
                (2.15, 0, -0.15), (-0.15, 0, -0.15)],
         facecolor="#E6EBF0", edgecolor="#98A8B6", hatch="///", lw=0.6)
    face(axis, [(2.15, -1.1, -0.15), (2.15, -1.1, 2.15),
                (2.15, 0, 2.15), (2.15, 0, -0.15)],
         facecolor="#CAD4DD", edgecolor="#98A8B6", lw=0.6)
    ring(axis, 0, color=INK, lw=1.5)

    dimension(axis, -3.0, 0, 30, "30 m", overall=True)
    for _, bottom, top, _, _ in LAYERS:
        dimension(axis, -0.9, bottom, top, f"{top-bottom} m")
    # Front width and receding depth dimensions, both physically 2 m.
    axis.annotate("", (0, 33.6), (2.2, 33.6),
                  arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1, shrinkA=0, shrinkB=0))
    for x in (0, 2.2):
        axis.plot([x, x], [30.5, 34], color=MUTED, lw=0.6)
    axis.text(1.1, 34.1, "2 m (x)", color=INK, ha="center", fontsize=10)
    axis.annotate("", (3.0, 32.0), (4.2, 33.2),
                  arrowprops=dict(arrowstyle="<->", color=INK, lw=1.1, shrinkA=0, shrinkB=0))
    axis.plot([2.2, 3.2], [30, 32.2], color=MUTED, lw=0.6)
    axis.plot([3.4, 4.4], [31.2, 33.4], color=MUTED, lw=0.6)
    axis.text(4.25, 33.6, "2 m (z)", color=INK, ha="center", fontsize=10)

    # A finite horizontal plane and its visible edges identify the water table.
    face(axis, [(-0.15, 28, -0.15), (2.15, 28, -0.15),
                (2.15, 28, 2.15), (-0.15, 28, 2.15)],
         facecolor=WATER, alpha=0.18, edgecolor="none")
    ring(axis, 28, color=WATER, lw=1.8, dashes=(4, 3))
    axis.plot([3.5, 5.5], [29.2, 29.2], color=WATER, lw=1.0)
    axis.text(5.9, 29.2, "WATER TABLE", color=WATER, fontsize=11,
              fontweight="bold", va="center")
    axis.text(5.9, 27.9, "y = 28 m  ·  2 m below surface", color=MUTED, fontsize=10)

    # The 3D history scripts average all four pressure-carrying corner nodes.
    for name, y, text_y, title, node_ids in (
        ("P1", 15, 16.5, "Mid-column", "121-124"),
        ("P2", 30, 32.5, "Ground surface", "241-244"),
    ):
        ring(axis, y, color=INK, lw=0.9, dashes=(3, 3))
        points = [project(x, y, z) for x, z in ((0, 0), (2, 0), (2, 2), (0, 2))]
        xs, ys = zip(*points)
        axis.scatter(xs, ys, s=42, facecolor="white", edgecolor=INK, linewidth=1.4, zorder=6)
        cx, cy = project(1, y, 1)
        axis.scatter([cx], [cy], s=45, marker="D", color=INK, zorder=6)
        axis.plot([3.55, 5.2, 5.5], [y + 1.2, text_y, text_y], color=INK, lw=1.0)
        axis.text(5.9, text_y, f"{name}  {title}", fontsize=12,
                  color=INK, fontweight="bold", va="center")
        axis.text(5.9, text_y - 1.3, f"y = {y} m  ·  average of corner nodes {node_ids}",
                  fontsize=9.3, color=MUTED)

    axis.annotate("", (2.15, -2.4), (0.05, -2.4),
                  arrowprops=dict(arrowstyle="<->", color=INPUT, lw=2.4))
    axis.plot([0, 0], [-0.15, -2.4], color=INPUT, lw=1.0)
    axis.plot([2.35, 5.5], [-2.4, -2.4], color=INPUT, lw=1.0)
    axis.text(5.9, -0.8, "HORIZONTAL MOTION INPUT", fontsize=11, color=INPUT, fontweight="bold")
    axis.text(5.9, -2.15, r"Base x direction: $F_x(t)=c\,v_{in}(t)$", fontsize=10, color=MUTED)
    axis.text(1.5, -4.0, "Elastic half-space\nHorizontal Lysmer dashpots", ha="center", va="center",
              fontsize=10, color=MUTED, linespacing=1.5)
    # A spatial triad makes the x-y-z interpretation explicit.
    for target, label, label_position in (
        ((11.3, 1.2), "x", (11.45, 1.0)),
        ((9.6, 4.5), "y", (9.4, 4.7)),
        ((10.8, 3.0), "z", (10.95, 3.1)),
    ):
        axis.annotate("", target, (9.6, 1.2),
                      arrowprops=dict(arrowstyle="->", color=MUTED, lw=1.1))
        axis.text(*label_position, label, color=MUTED, fontsize=10)

    figure.text(0.075, 0.075, "Comparison histories: three displacement components and pore pressure.",
                fontsize=10, color=INK)
    figure.text(0.075, 0.05, "Circles: four averaged corner nodes. Diamonds: comparison elevations. Horizontal dimensions exaggerated.",
                fontsize=9, color=MUTED)
    FIGURES.mkdir(parents=True, exist_ok=True)
    for suffix in ("png", "svg", "pdf"):
        output = FIGURES / f"freeField3D_schematic.{suffix}"
        figure.savefig(output, dpi=240, facecolor="white")
        print(f"Wrote {output}")
    plt.close(figure)


if __name__ == "__main__":
    main()
