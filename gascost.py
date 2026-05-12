from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import configure_plot_style, ensure_results_dir


def plot_gas_cost(output_dir: Path | None = None, show: bool = True) -> Path:
    """Generate the cumulative gas cost comparison figure."""
    configure_plot_style()
    transactions = np.arange(0, 2100, 100)

    cost_per_tx_manual = 5000
    cost_per_tx_agentic = 5100
    valid_rate = 0.8

    total_cost_traditional = transactions * cost_per_tx_manual
    total_cost_agentic = (
        transactions * valid_rate * cost_per_tx_agentic
    ) + (transactions * (1 - valid_rate) * 100)

    plt.figure(figsize=(8, 6))
    plt.plot(
        transactions,
        total_cost_traditional,
        "r--o",
        label="Baseline System",
        linewidth=2,
        markersize=5,
    )
    plt.plot(
        transactions,
        total_cost_agentic,
        "g-s",
        label="Proposed Architecture",
        linewidth=2,
        markersize=5,
    )

    plt.xlabel("Number of Transaction Requests", fontweight="bold")
    plt.ylabel("Cumulative Gas Consumption (Cost Units)", fontweight="bold")
    plt.legend()
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()

    target_dir = output_dir or ensure_results_dir()
    output_path = target_dir / "Fig3_Gas_Cost.png"
    plt.savefig(output_path, dpi=300)
    if show:
        plt.show()
    plt.close()
    return output_path


if __name__ == "__main__":
    plot_gas_cost()
