"""Plot the exported SSPquadUP and Tri31UP free-field meshes side by side.

Run: python freeField2D_meshes.py
Reads results/sspquadup_freeField2D.flavia.msh and
results/tri31UP_freeField2D.flavia.msh; writes figures/freeField2D_meshes.png.
"""

from pathlib import Path
import re

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np


HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGURES = HERE / "figures"
MODELS = (
    ("SSPquadUP", "sspquadup_freeField2D.flavia.msh", "quadrilateral", 4),
    ("Tri31UP", "tri31UP_freeField2D.flavia.msh", "triangle", 3),
)
MATERIALS = {
    1: ("tab:blue", "Material 1: 0-20 m"),
    2: ("tab:orange", "Material 2: 20-28 m"),
    3: ("tab:purple", "Material 3: 28-30 m"),
}


def read_mesh(path: Path, topology: str, node_count: int):
    """Read actual coordinates, connectivity and material tags from GiD."""
    nodes, elements = {}, {}
    section = None
    header_found = False
    for line_number, line in enumerate(path.read_text().splitlines(), 1):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if line.upper().startswith("MESH "):
            header = re.search(r"dimension\s+2\s+ElemType\s+(\w+)\s+Nnode\s+(\d+)", line, re.I)
            if header is None or (header[1].lower(), int(header[2])) != (topology, node_count):
                raise ValueError(f"{path}:{line_number}: unexpected 2D mesh header")
            header_found = True
            section = None
        elif line.lower() in ("coordinates", "elements"):
            section = line.lower()
        elif line.lower().startswith("end "):
            section = None
        elif section == "coordinates":
            fields = line.split()
            tag = int(fields[0])
            xy = tuple(map(float, fields[1:3]))
            if tag in nodes or len(xy) != 2 or not np.isfinite(xy).all():
                raise ValueError(f"{path}:{line_number}: invalid or duplicate node")
            nodes[tag] = xy
        elif section == "elements":
            fields = list(map(int, line.split()))
            if len(fields) != node_count + 2 or fields[0] in elements:
                raise ValueError(f"{path}:{line_number}: invalid or duplicate element")
            elements[fields[0]] = (tuple(fields[1:-1]), fields[-1])
    if not header_found or not nodes or not elements:
        raise ValueError(f"{path}: incomplete mesh")
    for tag, (connectivity, material) in elements.items():
        if len(set(connectivity)) != node_count or any(node not in nodes for node in connectivity):
            raise ValueError(f"{path}: element {tag} has invalid connectivity")
        if material not in MATERIALS:
            raise ValueError(f"{path}: unsupported material {material}")
        xy = np.asarray([nodes[node] for node in connectivity])
        area = 0.5 * np.sum(xy[:, 0] * np.roll(xy[:, 1], -1) - xy[:, 1] * np.roll(xy[:, 0], -1))
        if area <= 0:
            raise ValueError(f"{path}: element {tag} has nonpositive area")
    return nodes, elements


def main() -> None:
    meshes = [read_mesh(RESULTS / filename, topology, count)
              for _, filename, topology, count in MODELS]
    all_xy = np.asarray([xy for nodes, _ in meshes for xy in nodes.values()])
    lower, upper = all_xy.min(axis=0), all_xy.max(axis=0)
    figure, axes = plt.subplots(1, 2, figsize=(7, 12), sharex=True, sharey=True,
                                constrained_layout=True)
    for axis, (label, _, _, _), (nodes, elements) in zip(axes, MODELS, meshes):
        for material, (color, _) in MATERIALS.items():
            edges = set()
            for connectivity, layer in elements.values():
                if layer == material:
                    for a, b in zip(connectivity, connectivity[1:] + connectivity[:1]):
                        edges.add(tuple(sorted((a, b))))
            if edges:
                segments = [(nodes[a], nodes[b]) for a, b in sorted(edges)]
                axis.add_collection(LineCollection(segments, colors=color, linewidths=0.9))
        xy = np.asarray(list(nodes.values()))
        axis.scatter(xy[:, 0], xy[:, 1], s=6, color="tab:red", zorder=3)
        axis.set_title(f"{label}\n{len(elements)} elements, {len(nodes)} nodes")
        axis.set_xlabel("x [m]")
        axis.set_xlim(lower[0] - 0.25, upper[0] + 0.25)
        axis.set_ylim(lower[1] - 0.5, upper[1] + 0.5)
        axis.set_xticks((lower[0], upper[0]))
        axis.set_yticks(np.arange(lower[1], upper[1] + 0.1, 5.0))
        axis.set_aspect("equal", adjustable="box")
        print(f"{label}: {len(elements)} elements, {len(nodes)} three-DOF nodes")
    axes[0].set_ylabel("Elevation y [m]")
    handles = [Patch(facecolor=color, label=label) for color, label in MATERIALS.values()]
    handles.append(Line2D([], [], color="tab:red", marker="o", linestyle="none",
                          markersize=4, label="Node: $u_x,u_y,p$"))
    figure.legend(handles=handles, loc="outside lower center", ncol=2, fontsize=9)
    figure.suptitle("2D plane-strain free-field meshes (true geometric aspect ratio)")
    FIGURES.mkdir(parents=True, exist_ok=True)
    output = FIGURES / "freeField2D_meshes.png"
    figure.savefig(output, dpi=220)
    plt.close(figure)
    print(f"Wrote {output}")


if __name__ == "__main__":
    main()
