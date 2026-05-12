from pathlib import Path

import matplotlib.pyplot as plt


RESULTS_DIR = Path("results")


def configure_plot_style() -> None:
    """Apply a consistent plotting style across figures."""
    plt.style.use("default")
    plt.rcParams["font.family"] = "serif"
    plt.rcParams["font.size"] = 12


def ensure_results_dir() -> Path:
    """Create the output directory if it does not exist."""
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return RESULTS_DIR
