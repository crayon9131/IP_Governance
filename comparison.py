from dataclasses import dataclass
from pathlib import Path
import random

import matplotlib.pyplot as plt
import numpy as np
import simpy

from plot_utils import configure_plot_style, ensure_results_dir


SIMULATION_TIME = 1000
LOG_INTERVAL = 10

TRADITIONAL_PARAMS = {
    "verify_time": 5.0,
    "search_time": 10.0,
    "negotiate_time": 8.0,
    "success_rate": 0.6,
}

AGENTIC_PARAMS = {
    "verify_time": 0.5,
    "search_time": 0.5,
    "negotiate_time": 0.1,
    "success_rate": 0.95,
}


@dataclass
class IPAsset:
    asset_id: str
    owner: str
    status: str = "created"


class IPEcosystem:
    def __init__(self, env: simpy.Environment, params: dict[str, float], mode_name: str):
        self.env = env
        self.params = params
        self.mode = mode_name
        self.admin_resource = simpy.Resource(env, capacity=5)
        self.total_transactions = 0
        self.avg_process_time: list[float] = []
        self.time_log: list[float] = []
        self.tx_count_log: list[int] = []

    def log_data(self):
        while True:
            self.time_log.append(self.env.now)
            self.tx_count_log.append(self.total_transactions)
            yield self.env.timeout(LOG_INTERVAL)

    def admin_process(self, asset: IPAsset):
        with self.admin_resource.request() as req:
            yield req
            yield self.env.timeout(self.params["verify_time"])
            asset.status = "verified"

    def transaction_workflow(self, creator_id: int):
        asset = IPAsset(
            asset_id=f"IP_{creator_id}_{self.env.now}",
            owner=f"Creator_{creator_id}",
        )
        start_process = self.env.now
        yield self.env.process(self.admin_process(asset))
        yield self.env.timeout(self.params["search_time"])
        yield self.env.timeout(self.params["negotiate_time"])

        if random.random() < self.params["success_rate"]:
            self.total_transactions += 1
            self.avg_process_time.append(self.env.now - start_process)


def run_simulation_advanced(output_dir: Path | None = None, show: bool = True) -> Path:
    """Generate the multi-panel comparison figure for traditional vs agentic flow."""
    configure_plot_style()
    results: dict[str, dict[str, float]] = {}
    time_series_data: dict[str, tuple[list[float], list[int]]] = {}
    modes = [("Traditional", TRADITIONAL_PARAMS), ("Agentic", AGENTIC_PARAMS)]

    for mode_name, params in modes:
        env = simpy.Environment()
        ecosystem = IPEcosystem(env, params, mode_name)
        env.process(ecosystem.log_data())

        def lifecycle(current_env: simpy.Environment, eco: IPEcosystem):
            i = 0
            while True:
                yield current_env.timeout(random.uniform(0.5, 2))
                current_env.process(eco.transaction_workflow(i))
                i += 1

        env.process(lifecycle(env, ecosystem))
        env.run(until=SIMULATION_TIME)

        results[mode_name] = {
            "count": ecosystem.total_transactions,
            "avg_time": float(np.mean(ecosystem.avg_process_time)) if ecosystem.avg_process_time else 0.0,
        }
        time_series_data[mode_name] = (ecosystem.time_log, ecosystem.tx_count_log)

    plt.figure(figsize=(14, 10))

    ax1 = plt.subplot(2, 1, 1)
    for mode, (times, counts) in time_series_data.items():
        style = "--" if mode == "Traditional" else "-"
        color = "grey" if mode == "Traditional" else "#3498db"
        ax1.plot(times, counts, label=mode, linestyle=style, color=color, linewidth=2)
    ax1.set_title("Cumulative Transactions Over Time", fontsize=14)
    ax1.set_xlabel("Simulation Time")
    ax1.set_ylabel("Total Transactions")
    ax1.legend()
    ax1.grid(True, linestyle=":", alpha=0.6)

    ax2 = plt.subplot(2, 2, 3)
    labels = list(results.keys())
    counts = [results[mode]["count"] for mode in labels]
    ax2.bar(labels, counts, color=["#bdc3c7", "#3498db"])
    ax2.set_title("Total Throughput Comparison")

    ax3 = plt.subplot(2, 2, 4)
    times = [results[mode]["avg_time"] for mode in labels]
    ax3.bar(labels, times, color=["#e74c3c", "#2ecc71"])
    ax3.set_title("Avg Transaction Latency")

    plt.tight_layout()
    target_dir = output_dir or ensure_results_dir()
    output_path = target_dir / "Fig6_Comparison.png"
    plt.savefig(output_path, dpi=300)
    if show:
        plt.show()
    plt.close()
    return output_path


if __name__ == "__main__":
    run_simulation_advanced()
