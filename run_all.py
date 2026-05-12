from gascost import plot_gas_cost
from Latency import plot_latency
from rag_compliance import plot_rag_accuracy


def main() -> None:
    plot_gas_cost(show=False)
    plot_latency(show=False)
    plot_rag_accuracy(show=False)
    try:
        from comparison import run_simulation_advanced
    except ModuleNotFoundError as exc:
        missing_module = exc.name or "unknown dependency"
        raise SystemExit(
            f"Missing dependency: {missing_module}. Install requirements with "
            "`pip install -r requirements.txt` before running all figures."
        ) from exc

    run_simulation_advanced(show=False)


if __name__ == "__main__":
    main()
