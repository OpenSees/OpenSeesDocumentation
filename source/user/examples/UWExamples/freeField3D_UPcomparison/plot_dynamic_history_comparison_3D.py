"""Compare dynamic histories including the mixed brick/tetrahedron column.

Run: python plot_dynamic_history_comparison_3D.py
Reads results/ and writes figures/dynamic_<quantity>_history_comparison_3D.png.
"""

from pathlib import Path

from freefield_plot_utils import (
    LEVELS, N_C3D10_NODES, N_PRESSURE_NODES, RESULTS,
    common_histories, corner_average, load_complete_rows, np, plt,
)


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
MODELS = (
    ("SSPbrickUP", "sspbrickup_displacement.out", "sspbrickup_porePressure.out",
     N_PRESSURE_NODES, "tab:blue", "-"),
    ("BrickUP", "displacement_BrickUP.out", "porePressure_BrickUP.out",
     N_PRESSURE_NODES, "tab:green", "-."),
    ("10NodeTetrahedronUP", "c3d10UP_displacement.out", "c3d10UP_porePressure.out",
     N_C3D10_NODES, "tab:orange", "--"),
    ("SSPtetUP", "ssptetUP_displacement.out", "ssptetUP_porePressure.out",
     N_PRESSURE_NODES, "tab:red", ":"),
    ("Mixed SSPbrickUP / SSPtetUP", "mixed_displacement.out", "mixed_porePressure.out",
     N_PRESSURE_NODES, "tab:purple", (0, (5, 1, 1, 1))),
)


def plot_histories(histories: list[np.ndarray], pressure: bool) -> Path:
    times, *aligned = common_histories(*histories)
    components = 1 if pressure else 3
    figure, axes = plt.subplots(
        len(LEVELS), components, figsize=(11, 8) if pressure else (15, 9),
        sharex=True, squeeze=False, constrained_layout=True,
    )
    labels = ("$p$ [kPa]",) if pressure else ("$u_x$ [m]", "$u_y$ [m]", "$u_z$ [m]")
    for row, (location, level) in enumerate(LEVELS.items()):
        for model, history in zip(MODELS, aligned):
            label, _, _, _, color, linestyle = model
            values = corner_average(history, components, level)
            for component, axis in enumerate(axes[row]):
                axis.plot(times, values[:, component], color=color,
                          linestyle=linestyle, lw=1.6, label=label)
        for component, axis in enumerate(axes[row]):
            axis.set_ylabel(f"{location}\n{labels[component]}")
            axis.grid(alpha=0.3)
            if row == len(LEVELS) - 1:
                axis.set_xlabel("Time [s]")
    axes[0, 0].legend(loc="best")
    quantity = "pore_pressure" if pressure else "displacement"
    figure.suptitle(f"Free-field {quantity.replace('_', ' ')} histories including mixed mesh")
    output = FIGURES / f"dynamic_{quantity}_history_comparison_3D.png"
    figure.savefig(output, dpi=200)
    plt.close(figure)
    print(f"{quantity}: {len(times)} shared recorded times through t={times[-1]:g} s")
    return output


def main() -> None:
    displacements, pressures = [], []
    for label, displacement_file, pressure_file, node_count, _, _ in MODELS:
        displacement = load_complete_rows(RESULTS / displacement_file, 1 + 3 * node_count)
        pressure = load_complete_rows(RESULTS / pressure_file, 1 + N_PRESSURE_NODES)
        displacements.append(displacement)
        pressures.append(pressure)
        print(f"{label}: {len(displacement)} displacement rows, {len(pressure)} pressure rows")
    for output in (plot_histories(displacements, False), plot_histories(pressures, True)):
        print(f"Wrote {output}")


if __name__ == "__main__":
    main()
