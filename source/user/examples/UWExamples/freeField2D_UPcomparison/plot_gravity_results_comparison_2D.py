"""Compare final SSPquadUP and Tri31UP plane-strain gravity results.

Run: python plot_gravity_results_comparison_2D.py
Reads results/sspquadup_G*.out and results/tri31UP_G*.out.
Writes figures/gravity_*_comparison_2D.png.
Average two nodes per elevation and two equal-area triangles per original cell.
"""

from pathlib import Path

from freefield_plot_utils import (
    ELEVATION_CELLS, ELEVATION_NODES, N_CELLS, element_profile, final_row,
    np, plt, profile_limits, style_axis,
)


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
MODELS = (
    ("SSPquadUP", "sspquadup_", 1, "tab:blue", "-"),
    ("Tri31UP", "tri31UP_", 2, "tab:red", "--"),
)


def nodal_profile(name: str, components: int) -> tuple[float, np.ndarray]:
    """Average the left and right nodes at each original elevation."""
    history = final_row(name, 1 + 2 * (N_CELLS + 1) * components)
    values = history[1:].reshape(N_CELLS + 1, 2, components).mean(axis=1)
    return history[0], values


def plot_profiles(profiles: list[np.ndarray], quantity: str,
                  labels: tuple[str, ...], nodal: bool) -> Path:
    shared_scale = quantity in ("displacement", "pore_pressure", "stress")
    limits = profile_limits(*profiles) if shared_scale else None
    count = len(labels)
    figure, axes = plt.subplots(
        1, count, figsize=(7, 8) if count == 1 else (5 * count, 7),
        sharex=shared_scale, sharey=True, squeeze=False, constrained_layout=True,
    )
    elevations = ELEVATION_NODES if nodal else ELEVATION_CELLS
    for component, axis in enumerate(axes.flat):
        for model, values in zip(MODELS, profiles):
            label, _, _, color, linestyle = model
            axis.plot(values[:, component], elevations, color=color,
                      linestyle=linestyle, lw=2, label=label)
        style_axis(axis, labels[component])
        if limits is not None:
            axis.set_xlim(limits)
        for interface in (20.0, 28.0):
            axis.axhline(interface, color="0.6", ls=":", lw=0.8)
    axes.flat[0].legend(loc="best")
    figure.suptitle(f"Final 2D gravity {quantity.replace('_', ' ')}: SSPquadUP vs Tri31UP")
    output = FIGURES / f"gravity_{quantity}_comparison_2D.png"
    figure.savefig(output, dpi=220)
    plt.close(figure)
    return output


def main() -> None:
    displacements, pressures, stresses, strains = [], [], [], []
    for label, prefix, elements_per_cell, _, _ in MODELS:
        dt, displacement = nodal_profile(f"{prefix}Gdisplacement.out", 2)
        pt, pressure = nodal_profile(f"{prefix}GporePressure.out", 1)
        st, stress = element_profile(f"{prefix}Gstress.out", 3, elements_per_cell)
        et, strain = element_profile(f"{prefix}Gstrain.out", 3, elements_per_cell)
        displacements.append(displacement)
        pressures.append(pressure)
        stresses.append(stress)
        strains.append(strain)
        print(f"{label}: final displacement/pressure/stress/strain times = {dt:g}/{pt:g}/{st:g}/{et:g}")
    outputs = [
        plot_profiles(displacements, "displacement", ("$u_x$ [m]", "$u_y$ [m]"), True),
        plot_profiles(pressures, "pore_pressure", ("$p$ [kPa]",), True),
        plot_profiles(stresses, "stress",
                      (r"$\sigma_{xx}$ [kPa]", r"$\sigma_{yy}$ [kPa]", r"$\tau_{xy}$ [kPa]"), False),
        plot_profiles(strains, "strain",
                      (r"$\epsilon_{xx}$", r"$\epsilon_{yy}$", r"$\gamma_{xy}$"), False),
    ]
    for quantity, profiles, units in (
        ("displacement", displacements, "m"), ("pore pressure", pressures, "kPa"),
        ("stress", stresses, "kPa"), ("strain", strains, ""),
    ):
        difference = np.max(np.abs(profiles[1] - profiles[0]))
        print(f"Maximum {quantity} difference (Tri31UP vs SSPquadUP): {difference:.6e} {units}".rstrip())
    for output in outputs:
        print(f"Wrote {output}")


if __name__ == "__main__":
    main()
