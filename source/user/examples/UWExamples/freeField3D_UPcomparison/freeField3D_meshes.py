"""Plot SSPbrickUP, 10NodeTetrahedronUP, SSPtetUP and the mixed mesh side by side."""

from pathlib import Path
import re

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
from mpl_toolkits.mplot3d.art3d import Line3DCollection
import numpy as np


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
RESULTS = HERE / "results"
WIDTH_X = 2.0
WIDTH_Z = 2.0
HEIGHT = 30.0
N_CELLS = 60
DY = HEIGHT / N_CELLS

# Hexahedron corner numbering used in the Tcl mesh. Each tuple is reordered to
# have positive orientation after using global y as the column's vertical axis.
LOCAL_TETS = (
    (0, 2, 1, 6),
    (0, 3, 2, 6),
    (0, 7, 3, 6),
    (0, 4, 7, 6),
    (0, 5, 4, 6),
    (0, 1, 5, 6),
)
TET_EDGES = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
BRICK_EDGES = ((0, 1), (1, 2), (2, 3), (3, 0),
               (4, 5), (5, 6), (6, 7), (7, 4),
               (0, 4), (1, 5), (2, 6), (3, 7))
MATERIALS = (
    (1, 0, 40, "tab:blue", "Material 1: 0–20 m"),
    (2, 40, 56, "tab:orange", "Material 2: 20–28 m"),
    (3, 56, 60, "tab:purple", "Material 3: 28–30 m"),
)


def corners_by_level() -> list[tuple[float, float, float]]:
    nodes = []
    for level in range(N_CELLS + 1):
        y = level * DY
        nodes.extend(((0.0, y, 0.0), (WIDTH_X, y, 0.0),
                      (WIDTH_X, y, WIDTH_Z), (0.0, y, WIDTH_Z)))
    return nodes


def hexahedra() -> list[tuple[int, ...]]:
    cells = []
    for level in range(N_CELLS):
        lower = tuple(4 * level + i for i in range(4))
        upper = tuple(4 * (level + 1) + i for i in range(4))
        cells.append(lower + upper)
    return cells


def c3d10_mesh():
    nodes = corners_by_level()
    edge_midpoints: dict[tuple[int, int], int] = {}
    tetrahedra = []
    for hexahedron in hexahedra():
        for local_tet in LOCAL_TETS:
            corners = tuple(hexahedron[index] for index in local_tet)
            midsides = []
            # Tcl/OpenSees order: 12, 23, 13, 14, 34, 24.
            for first_local, second_local in ((0, 1), (1, 2), (0, 2),
                                               (0, 3), (2, 3), (1, 3)):
                edge = tuple(sorted((corners[first_local], corners[second_local])))
                if edge not in edge_midpoints:
                    first = np.asarray(nodes[edge[0]])
                    second = np.asarray(nodes[edge[1]])
                    edge_midpoints[edge] = len(nodes)
                    nodes.append(tuple(0.5 * (first + second)))
                midsides.append(edge_midpoints[edge])
            tetrahedra.append(corners + tuple(midsides))
    return np.asarray(nodes), tetrahedra


def unique_segments(connectivities, local_edges):
    edge_keys = set()
    for connectivity in connectivities:
        for first, second in local_edges:
            edge_keys.add(tuple(sorted((connectivity[first], connectivity[second]))))
    return sorted(edge_keys)


def read_mixed_mesh(path: Path):
    """Read shared coordinates and both topology blocks from a GiD mesh."""
    coordinates = {}
    elements = []
    element_tags = set()
    section = None
    topology = None
    node_count = None
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.upper().startswith("MESH "):
            match = re.search(r"ElemType\s+(\w+)\s+Nnode\s+(\d+)", line, re.I)
            if match is None:
                raise ValueError(f"{path}:{line_number}: invalid mesh header")
            topology, node_count = match.group(1).lower(), int(match.group(2))
            if (topology, node_count) not in (("hexahedra", 8), ("tetrahedra", 4)):
                raise ValueError(f"{path}:{line_number}: unsupported topology")
            section = None
        elif line.lower() in ("coordinates", "elements"):
            section = line.lower()
        elif line.lower().startswith("end "):
            section = None
        elif section == "coordinates":
            fields = line.split()
            tag, xyz = int(fields[0]), tuple(map(float, fields[1:4]))
            if tag in coordinates and coordinates[tag] != xyz:
                raise ValueError(f"{path}:{line_number}: conflicting coordinates for node {tag}")
            coordinates[tag] = xyz
        elif section == "elements":
            fields = list(map(int, line.split()))
            if len(fields) != node_count + 2 or fields[0] in element_tags:
                raise ValueError(f"{path}:{line_number}: invalid or duplicate element")
            element_tags.add(fields[0])
            elements.append((topology, fields[-1], tuple(fields[1:-1])))
    if not coordinates or not elements:
        raise ValueError(f"{path}: no mesh coordinates or elements found")
    tags = sorted(coordinates)
    indices = {tag: index for index, tag in enumerate(tags)}
    nodes = np.asarray([coordinates[tag] for tag in tags])
    indexed_elements = [
        (topology, material, tuple(indices[tag] for tag in connectivity))
        for topology, material, connectivity in elements
    ]
    return nodes, indexed_elements


def ssptet_mesh():
    """Read the exported SSPtetUP mesh, or reproduce its Tcl connectivity."""
    path = RESULTS / "ssptetUP_freeField3D.flavia.msh"
    if path.is_file():
        return read_mixed_mesh(path)
    # SSPtetUP Tcl corner tags run around each level in the z direction first.
    nodes = np.asarray(corners_by_level())[:, (2, 1, 0)]
    local_tets = ((0, 1, 2, 6), (0, 2, 3, 6), (0, 3, 7, 6),
                  (0, 7, 4, 6), (0, 4, 5, 6), (0, 5, 1, 6))
    elements = []
    for cell, hex_nodes in enumerate(hexahedra()):
        material = next(tag for tag, first, last, _, _ in MATERIALS if first <= cell < last)
        elements.extend(("tetrahedra", material, tuple(hex_nodes[i] for i in tet))
                        for tet in local_tets)
    return nodes, elements


def add_segments(axis, nodes, segments, *, color, linewidth, alpha):
    if not segments:
        return
    lines = [(nodes[first], nodes[second]) for first, second in segments]
    axis.add_collection3d(
        Line3DCollection(lines, colors=color, linewidths=linewidth, alpha=alpha)
    )


def format_axis(axis, title):
    axis.set_title(title, pad=12)
    axis.set_xlabel("x [m]")
    axis.set_ylabel("z [m]")
    axis.set_zlabel("elevation y [m]")
    axis.set_xlim(0.0, WIDTH_X)
    axis.set_ylim(0.0, WIDTH_Z)
    axis.set_zlim(0.0, HEIGHT)
    axis.set_box_aspect((WIDTH_X, WIDTH_Z, HEIGHT))
    axis.set_xticks((0.0, 2.0))
    axis.set_yticks((0.0, 2.0))
    axis.set_zticks(np.arange(0.0, HEIGHT + 0.1, 5.0))
    axis.view_init(elev=12, azim=-55)


def main() -> None:
    brick_nodes = np.asarray(corners_by_level())
    bricks = hexahedra()
    brick_edges = unique_segments(
        bricks,
        ((0, 1), (1, 2), (2, 3), (3, 0),
         (4, 5), (5, 6), (6, 7), (7, 4),
         (0, 4), (1, 5), (2, 6), (3, 7)),
    )

    tet_nodes, tetrahedra = c3d10_mesh()
    tet_corner_connectivity = [tet[:4] for tet in tetrahedra]
    tet_edges = unique_segments(tet_corner_connectivity, TET_EDGES)
    pressure_count = len(brick_nodes)
    # Display elevation vertically while retaining the model's global axes in
    # labels: plotting coordinates are (global x, global z, global y).
    brick_plot_nodes = brick_nodes[:, (0, 2, 1)]
    tet_plot_nodes = tet_nodes[:, (0, 2, 1)]
    mixed_nodes, mixed_elements = read_mixed_mesh(RESULTS / "mixed_freeField3D.flavia.msh")
    mixed_plot_nodes = mixed_nodes[:, (0, 2, 1)]
    ssp_nodes, ssp_elements = ssptet_mesh()
    ssp_plot_nodes = ssp_nodes[:, (0, 2, 1)]

    figure = plt.figure(figsize=(20, 12), constrained_layout=True)
    brick_axis = figure.add_subplot(1, 4, 1, projection="3d")
    tet_axis = figure.add_subplot(1, 4, 2, projection="3d")
    ssp_axis = figure.add_subplot(1, 4, 3, projection="3d")
    mixed_axis = figure.add_subplot(1, 4, 4, projection="3d")

    for _, first_cell, last_cell, color, _ in MATERIALS:
        material_edges = unique_segments(
            bricks[first_cell:last_cell],
            ((0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)),
        )
        add_segments(brick_axis, brick_plot_nodes, material_edges,
                     color=color, linewidth=0.9, alpha=0.85)
    brick_axis.scatter(brick_plot_nodes[:, 0], brick_plot_nodes[:, 1], brick_plot_nodes[:, 2],
                       s=3, color="0.2", depthshade=False)
    format_axis(brick_axis, f"SSPbrickUP\n{len(bricks)} elements, {len(brick_nodes)} nodes")

    for _, first_cell, last_cell, color, _ in MATERIALS:
        material_tets = tet_corner_connectivity[6 * first_cell:6 * last_cell]
        material_edges = unique_segments(material_tets, TET_EDGES)
        add_segments(tet_axis, tet_plot_nodes, material_edges,
                     color=color, linewidth=0.55, alpha=0.62)
    tet_axis.scatter(tet_plot_nodes[:pressure_count, 0], tet_plot_nodes[:pressure_count, 1],
                     tet_plot_nodes[:pressure_count, 2], s=5, color="tab:red",
                     label="corner: $u_x,u_y,u_z,p$", depthshade=False)
    tet_axis.scatter(tet_plot_nodes[pressure_count:, 0], tet_plot_nodes[pressure_count:, 1],
                     tet_plot_nodes[pressure_count:, 2], s=2, color="tab:green", alpha=0.48,
                     label="midside: $u_x,u_y,u_z$", depthshade=False)
    format_axis(
        tet_axis,
        f"10NodeTetrahedronUP\n{len(tetrahedra)} elements, {len(tet_nodes)} nodes",
    )
    for material, _, _, color, _ in MATERIALS:
        connectivity = [nodes for kind, layer, nodes in ssp_elements
                        if kind == "tetrahedra" and layer == material]
        add_segments(ssp_axis, ssp_plot_nodes, unique_segments(connectivity, TET_EDGES),
                     color=color, linewidth=0.55, alpha=0.7)
    ssp_axis.scatter(ssp_plot_nodes[:, 0], ssp_plot_nodes[:, 1], ssp_plot_nodes[:, 2],
                     s=4, color="tab:red", depthshade=False)
    format_axis(ssp_axis, f"SSPtetUP\n{len(ssp_elements)} elements, {len(ssp_nodes)} nodes")

    for material, _, _, color, _ in MATERIALS:
        for topology, edges in (("hexahedra", BRICK_EDGES), ("tetrahedra", TET_EDGES)):
            connectivity = [nodes for kind, layer, nodes in mixed_elements
                            if kind == topology and layer == material]
            add_segments(mixed_axis, mixed_plot_nodes, unique_segments(connectivity, edges),
                         color=color, linewidth=0.8, alpha=0.8)
    mixed_axis.scatter(mixed_plot_nodes[:, 0], mixed_plot_nodes[:, 1], mixed_plot_nodes[:, 2],
                       s=4, color="tab:red", depthshade=False)
    mixed_bricks = sum(kind == "hexahedra" for kind, _, _ in mixed_elements)
    mixed_tets = sum(kind == "tetrahedra" for kind, _, _ in mixed_elements)
    format_axis(mixed_axis, f"Mixed SSPbrickUP / SSPtetUP\n"
                f"{mixed_bricks} bricks + {mixed_tets} tets, {len(mixed_nodes)} nodes")
    material_legend = [Patch(facecolor=color, label=label) for _, _, _, color, label in MATERIALS]
    node_legend = [
        Line2D([], [], marker="o", linestyle="none", color="tab:red", markersize=5,
               label="corner: $u_x,u_y,u_z,p$"),
        Line2D([], [], marker="o", linestyle="none", color="tab:green", markersize=4,
               label="midside: $u_x,u_y,u_z$"),
    ]
    figure.legend(handles=material_legend, loc="lower center", ncol=3,
                  bbox_to_anchor=(0.5, 0.075), title="Soil layers")
    tet_axis.legend(handles=node_legend, loc="upper center",
                    bbox_to_anchor=(0.5, -0.02), fontsize=8)

    figure.suptitle("3D free-field meshes: 2 m × 30 m × 2 m", fontsize=15)
    output = FIGURES / "freeField3D_meshes.png"
    figure.savefig(output, dpi=220)
    print(f"SSPbrickUP: {len(bricks)} elements, {len(brick_nodes)} four-DOF nodes")
    print(
        f"10NodeTetrahedronUP: {len(tetrahedra)} elements, {pressure_count} four-DOF corner nodes, "
        f"{len(tet_nodes) - pressure_count} three-DOF midside nodes"
    )
    print(f"Wrote {output}")
    print(f"Mixed: {mixed_bricks} bricks, {mixed_tets} tetrahedra, {len(mixed_nodes)} four-DOF nodes")
    print(f"SSPtetUP: {len(ssp_elements)} tetrahedra, {len(ssp_nodes)} four-DOF nodes")
    plt.close(figure)


if __name__ == "__main__":
    main()
