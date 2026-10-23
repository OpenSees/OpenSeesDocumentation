"""Compare SSPquadUP and Tri31UP plane-strain dynamic histories.

Run: python plot_dynamic_history_comparison_2D.py
Reads results/sspquadup_*.out and results/tri31UP_*.out.
Writes displacement and pore-pressure comparison plots into figures/.
Profiles average the left and right nodes at y=15 m and y=30 m.
"""

from pathlib import Path

from freefield_plot_utils import (
    LEVELS, N_LEVELS, RESULTS, common_histories, load_complete_rows, np, plt,
)


HERE = Path(__file__).resolve().parent
FIGURES = HERE / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
NODES_PER_LEVEL = 2
N_NODES = NODES_PER_LEVEL * N_LEVELS
MODELS = (
    ("SSPquadUP", "sspquadup_", "tab:blue", "-"),
    ("Tri31UP", "tri31UP_", "tab:red", "--"),
)


def level_average(history: np.ndarray, components: int, level: int) -> np.ndarray:
    """Average both nodes' recorded components at one elevation."""
    start = 1 + level * NODES_PER_LEVEL * components
    stop = start + NODES_PER_LEVEL * components
    return history[:, start:stop].reshape(len(history), NODES_PER_LEVEL, components).mean(axis=1)


def plot_histories(histories: list[np.ndarray], pressure: bool) -> Path:
    times, *aligned = common_histories(*histories)
    components = 1 if pressure else 2
    labels = ("$p$ [kPa]",) if pressure else ("$u_x$ [m]", "$u_y$ [m]")
    figure, axes = plt.subplots(
        len(LEVELS), components, figsize=(11, 8) if pressure else (13, 9),
        sharex=True, squeeze=False, constrained_layout=True,
    )
    for row, (location, level) in enumerate(LEVELS.items()):
        for model, history in zip(MODELS, aligned):
            label, _, color, linestyle = model
            values = level_average(history, components, level)
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
    figure.suptitle(f"2D free-field {quantity.replace('_', ' ')} histories: SSPquadUP vs Tri31UP")
    output = FIGURES / f"dynamic_{quantity}_history_comparison_2D.png"
    figure.savefig(output, dpi=200)
    plt.close(figure)
    print(f"{quantity}: {len(times)} shared recorded times through t={times[-1]:g} s")
    return output


def main() -> None:
    displacements, pressures = [], []
    for label, prefix, _, _ in MODELS:
        displacement = load_complete_rows(RESULTS / f"{prefix}displacement.out", 1 + 2 * N_NODES)
        pressure = load_complete_rows(RESULTS / f"{prefix}porePressure.out", 1 + N_NODES)
        displacements.append(displacement)
        pressures.append(pressure)
        print(f"{label}: {len(displacement)} displacement rows, {len(pressure)} pressure rows")
    for output in (plot_histories(displacements, False), plot_histories(pressures, True)):
        print(f"Wrote {output}")


if __name__ == "__main__":
    main()
