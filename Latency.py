from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import configure_plot_style, ensure_results_dir


def plot_latency(output_dir: Path | None = None, show: bool = True) -> Path:
    """Generate the negotiation latency comparison figure."""
    configure_plot_style()
    requests = np.array([10, 50, 100, 500, 1000])
    time_manual = requests * 1440
    time_agentic = requests * 0.5

    plt.figure(figsize=(8, 6))
    width = 0.35
    x = np.arange(len(requests))

    plt.bar(
        x - width / 2,
        time_manual,
        width,
        label="Manual Verification",
        color="#ff9999",
        edgecolor="black",
    )
    plt.bar(
        x + width / 2,
        time_agentic,
        width,
        label="Autonomous Negotiation",
        color="#66b3ff",
        edgecolor="black",
    )

    plt.xticks(x, requests)
    plt.yscale("log")
    plt.xlabel("Concurrent Transaction Volume", fontweight="bold")
    plt.ylabel("Total Processing Time (Minutes) [Log Scale]", fontweight="bold")
    plt.legend()
    plt.grid(True, axis="y", linestyle=":", alpha=0.6)

    for i in range(len(requests)):
        improvement = time_manual[i] / time_agentic[i]
        plt.text(
            i,
            time_manual[i] * 1.1,
            f"{int(improvement)}x",
            ha="center",
            va="bottom",
            fontsize=9,
        )

    plt.tight_layout()
    target_dir = output_dir or ensure_results_dir()
    output_path = target_dir / "Fig4_Latency.png"
    plt.savefig(output_path, dpi=300)
    if show:
        plt.show()
    plt.close()
    return output_path


if __name__ == "__main__":
    plot_latency()
