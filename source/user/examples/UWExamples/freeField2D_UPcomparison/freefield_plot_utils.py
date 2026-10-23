"""Shared result readers and formatting for the 2D and 3D plotting scripts."""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


RESULTS = Path(__file__).resolve().parent / "results"
N_CELLS = 60
N_LEVELS = N_CELLS + 1
N_CORNERS_PER_LEVEL = 4
N_CORNER_NODES = N_CORNERS_PER_LEVEL * N_LEVELS
N_PRESSURE_NODES = N_CORNER_NODES
N_C3D10_NODES = 1089
N_TETS_PER_CELL = 6
LEVELS = {"Mid-column (y = 15 m)": 30, "Top (y = 30 m)": 60}
ELEVATION_NODES = np.linspace(0.0, 30.0, N_LEVELS)
ELEVATION_CELLS = 0.5 * (ELEVATION_NODES[:-1] + ELEVATION_NODES[1:])


def load_complete_rows(path: Path, expected_columns: int) -> np.ndarray:
    """Read complete numeric rows, tolerating a result still being written."""
    if not path.is_file():
        raise FileNotFoundError(f"Required dynamic result not found: {path}")
    rows = []
    with path.open("r", encoding="utf-8", errors="replace") as stream:
        for line_number, line in enumerate(stream, 1):
            fields = line.split()
            if len(fields) != expected_columns:
                if line_number == 1:
                    raise ValueError(f"{path.name}: expected {expected_columns} columns, "
                                     f"found {len(fields)} in its first row")
                continue
            try:
                rows.append(np.asarray(fields, dtype=float))
            except ValueError:
                continue
    if not rows:
        raise ValueError(f"No complete rows are available in {path}")
    return np.vstack(rows)


def corner_average(history: np.ndarray, values_per_node: int, level: int) -> np.ndarray:
    first = 1 + values_per_node * N_CORNERS_PER_LEVEL * level
    last = first + values_per_node * N_CORNERS_PER_LEVEL
    return history[:, first:last].reshape(len(history), N_CORNERS_PER_LEVEL, values_per_node).mean(axis=1)


def common_histories(*histories: np.ndarray):
    common_times = np.round(histories[0][:, 0], 9)
    for history in histories[1:]:
        common_times = np.intersect1d(common_times, np.round(history[:, 0], 9))
    if common_times.size == 0:
        raise ValueError("The histories currently have no common recorded times")
    aligned = []
    for history in histories:
        lookup = {round(time, 9): index for index, time in enumerate(history[:, 0])}
        rows = np.asarray([lookup[float(time)] for time in common_times])
        aligned.append(history[rows])
    return common_times, *aligned


def final_row(name: str, expected_columns: int) -> np.ndarray:
    path = RESULTS / name
    if not path.is_file():
        raise FileNotFoundError(f"Required gravity result not found: {path}")
    data = np.loadtxt(path, ndmin=2)
    if data.shape[1] != expected_columns:
        raise ValueError(f"{path.name}: expected {expected_columns} columns, found {data.shape[1]}")
    return data[-1]


def displacement_profile(name: str, node_count: int):
    history = final_row(name, 1 + 3 * node_count)
    corners = history[1:1 + 3 * N_CORNER_NODES]
    return history[0], corners.reshape(N_LEVELS, N_CORNERS_PER_LEVEL, 3).mean(axis=1)


def pore_pressure_profile(name: str):
    history = final_row(name, 1 + N_CORNER_NODES)
    return history[0], history[1:].reshape(N_LEVELS, N_CORNERS_PER_LEVEL).mean(axis=1)


def element_profile(name: str, values_per_element: int, elements_per_cell: int):
    history = final_row(name, 1 + N_CELLS * elements_per_cell * values_per_element)
    values = history[1:].reshape(N_CELLS, elements_per_cell, values_per_element).mean(axis=1)
    return history[0], values


def style_axis(axis, xlabel: str):
    axis.set_xlabel(xlabel)
    axis.set_ylabel("Elevation y [m]")
    axis.grid(alpha=0.3)


def profile_limits(*profiles: np.ndarray) -> tuple[float, float]:
    """Use all models/components, include zero, and add 5% padding."""
    lower = min(0.0, *(float(np.min(values)) for values in profiles))
    upper = max(0.0, *(float(np.max(values)) for values in profiles))
    padding = 0.05 * (upper - lower) if upper > lower else 1.0e-12
    return lower - padding, upper + padding
