from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from plot_utils import configure_plot_style, ensure_results_dir


def plot_rag_accuracy(output_dir: Path | None = None, show: bool = True) -> Path:
    """Generate the RAG compliance accuracy figure."""
    configure_plot_style()
    kb_size = np.array([100, 500, 1000, 5000, 10000])
    acc_baseline = np.array([0.65, 0.66, 0.65, 0.64, 0.65])
    acc_rag = np.array([0.70, 0.82, 0.89, 0.94, 0.96])

    plt.figure(figsize=(8, 6))
    plt.plot(
        kb_size,
        acc_baseline * 100,
        "k--x",
        label="Standard LLM (Baseline)",
        linewidth=2,
    )
    plt.plot(
        kb_size,
        acc_rag * 100,
        "b-o",
        label="Proposed Compliance Agent (RAG)",
        linewidth=2,
    )

    plt.xlabel("Size of Industrial Standards KB", fontweight="bold")
    plt.ylabel("Compliance Verification Accuracy (%)", fontweight="bold")
    plt.legend(loc="lower right")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.ylim(50, 100)
    plt.tight_layout()

    target_dir = output_dir or ensure_results_dir()
    output_path = target_dir / "Fig5_Accuracy.png"
    plt.savefig(output_path, dpi=300)
    if show:
        plt.show()
    plt.close()
    return output_path


if __name__ == "__main__":
    plot_rag_accuracy()
