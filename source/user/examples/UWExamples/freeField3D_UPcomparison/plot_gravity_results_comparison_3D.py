"""Compare gravity profiles including the mixed brick/tetrahedron column.

Run: python plot_gravity_results_comparison_3D.py
Writes figures/gravity_<quantity>_comparison_3D.png.
Mixed element-to-cell mapping comes from results/mixed_elementInfo.dat.
"""

from pathlib import Path

from freefield_plot_utils import (
    ELEVATION_CELLS, ELEVATION_NODES, N_CELLS, N_CORNER_NODES, N_TETS_PER_CELL,
    RESULTS, displacement_profile, element_profile, final_row,
    np, plt, pore_pressure_profile, profile_limits, style_axis,
)


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
MODELS = (
    ("SSPbrickUP", "sspbrickup_", "", N_CORNER_NODES, 1, 7, "tab:blue", "-"),
    ("BrickUP", "", "_BrickUP", N_CORNER_NODES, 1, 7, "tab:green", "-."),
    ("10NodeTetrahedronUP", "c3d10UP_", "", 1089, N_TETS_PER_CELL, 7, "tab:orange", "--"),
    ("SSPtetUP", "ssptetUP_", "", N_CORNER_NODES, N_TETS_PER_CELL, 6, "tab:red", ":"),
    ("Mixed SSPbrickUP / SSPtetUP", "mixed_", "", N_CORNER_NODES, None, 6,
     "tab:purple", (0, (5, 1, 1, 1))),
)


def mixed_element_profile(name: str) -> tuple[float, np.ndarray]:
    """Average one brick or six equal-volume tetrahedra in each original cell."""
    metadata = RESULTS / "mixed_elementInfo.dat"
    entries = []
    for line in metadata.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            fields = line.split()
            entries.append((int(fields[0]), int(fields[2]), fields[3]))
    entries.sort()
    if [tag for tag, _, _ in entries] != list(range(1, len(entries) + 1)):
        raise ValueError(f"{metadata}: expected consecutive element tags starting at 1")
    if {cell for _, cell, _ in entries} != set(range(1, N_CELLS + 1)):
        raise ValueError(f"{metadata}: expected all {N_CELLS} original cells")
    history = final_row(name, 1 + 6 * len(entries))
    values = history[1:].reshape(len(entries), 6)
    profiles = []
    for cell in range(1, N_CELLS + 1):
        indices = [i for i, (_, cell_tag, _) in enumerate(entries) if cell_tag == cell]
        types = [entries[i][2] for i in indices]
        if types != ["SSPbrickUP"] and types != ["SSPtetUP"] * N_TETS_PER_CELL:
            raise ValueError(f"{metadata}: unexpected topology in cell {cell}")
        profiles.append(values[indices].mean(axis=0))
    return history[0], np.asarray(profiles)


def plot_profiles(profiles: list[np.ndarray], quantity: str,
                  labels: tuple[str, ...], nodal: bool) -> Path:
    count = len(labels)
    shape = (2, 3) if count == 6 else (1, count)
    shared_scale = quantity in ("displacement", "pore_pressure", "stress")
    limits = profile_limits(*profiles) if shared_scale else None
    figure, axes = plt.subplots(
        *shape, figsize=(13, 10) if count == 6 else ((7, 8) if count == 1 else (13, 7)),
        sharex=shared_scale, sharey=True, squeeze=False, constrained_layout=True,
    )
    elevations = ELEVATION_NODES if nodal else ELEVATION_CELLS
    for component, axis in enumerate(axes.flat):
        for model, values in zip(MODELS, profiles):
            axis.plot(values[:, component], elevations, color=model[-2],
                      linestyle=model[-1], lw=2, label=model[0])
        style_axis(axis, labels[component])
        if limits is not None:
            axis.set_xlim(limits)
        for interface in (20.0, 28.0):
            axis.axhline(interface, color="0.6", ls=":", lw=0.8)
    axes.flat[0].legend(loc="best")
    figure.suptitle(f"Final gravity {quantity.replace('_', ' ')} profiles including mixed mesh")
    output = FIGURES / f"gravity_{quantity}_comparison_3D.png"
    figure.savefig(output, dpi=220)
    plt.close(figure)
    return output


def main() -> None:
    displacements, pressures, stresses, strains = [], [], [], []
    for label, prefix, suffix, nodes, per_cell, stress_components, _, _ in MODELS:
        dt, displacement = displacement_profile(f"{prefix}Gdisplacement{suffix}.out", nodes)
        pt, pressure = pore_pressure_profile(f"{prefix}GporePressure{suffix}.out")
        if prefix == "mixed_":
            st, stress = mixed_element_profile("mixed_Gstress.out")
            et, strain = mixed_element_profile("mixed_Gstrain.out")
        else:
            gp = "_gp1" if prefix == "c3d10UP_" else ""
            st, stress = element_profile(f"{prefix}Gstress{suffix}{gp}.out", stress_components, per_cell)
            et, strain = element_profile(f"{prefix}Gstrain{suffix}{gp}.out", 6, per_cell)
        displacements.append(displacement)
        pressures.append(pressure[:, None])
        stresses.append(stress[:, :6])
        strains.append(strain)
        print(f"{label}: final displacement/pressure/stress/strain times = {dt:g}/{pt:g}/{st:g}/{et:g}")
    outputs = [
        plot_profiles(displacements, "displacement", ("$u_x$ [m]", "$u_y$ [m]", "$u_z$ [m]"), True),
        plot_profiles(pressures, "pore_pressure", ("$p$ [kPa]",), True),
        plot_profiles(stresses, "stress",
                      (r"$\sigma_{xx}$ [kPa]", r"$\sigma_{yy}$ [kPa]", r"$\sigma_{zz}$ [kPa]",
                       r"$\tau_{xy}$ [kPa]", r"$\tau_{yz}$ [kPa]", r"$\tau_{xz}$ [kPa]"), False),
        plot_profiles(strains, "strain",
                      (r"$\epsilon_{xx}$", r"$\epsilon_{yy}$", r"$\epsilon_{zz}$",
                       r"$\gamma_{xy}$", r"$\gamma_{yz}$", r"$\gamma_{xz}$"), False),
    ]
    for label, profiles in (("displacement", displacements), ("pore pressure", pressures),
                            ("stress", stresses), ("strain", strains)):
        print(f"Mixed maximum {label} difference from SSPbrickUP: "
              f"{np.max(np.abs(profiles[-1] - profiles[0])):.6e}")
    for output in outputs:
        print(f"Wrote {output}")


if __name__ == "__main__":
    main()
