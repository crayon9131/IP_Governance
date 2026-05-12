# ISJ Code

This repository contains the simulation and visualization scripts used to compare a baseline workflow with an agentic architecture for IP transaction processing and compliance analysis.

## Files

- `comparison.py`: SimPy-based end-to-end transaction simulation.
- `gascost.py`: cumulative gas cost comparison figure.
- `Latency.py`: negotiation latency comparison figure.
- `rag_compliance.py`: compliance accuracy comparison figure.
- `run_all.py`: generates every figure in one run.

## Requirements

- Python 3.10+
- Dependencies listed in `requirements.txt`

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

Generate all figures:

```bash
python run_all.py
```

Generate individual figures:

```bash
python gascost.py
python Latency.py
python rag_compliance.py
python comparison.py
```

Generated images are written to `results/`.

## GitHub Upload

```bash
git init
git add .
git commit -m "Initial project cleanup"
git branch -M main
git remote add origin <your-repository-url>
git push -u origin main
```
