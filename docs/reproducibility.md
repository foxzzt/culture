# Reproducibility

This repository provides a lightweight public reproduction workflow based on processed data.

## Environment

Recommended Python version: 3.10 or newer.

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

From the repository root:

```bash
python analysis/reproduce_public_figures.py
```

Generated files are written to:

```text
output/reproduced_figures/
```

## Scope

The public reproduction script regenerates selected non-map figures from the processed data. The map images in `figures/` are included as static final exports because the public repository does not include geographic boundary files or raw spatial inputs.

The private working repository contains the full raw-data pipeline, robustness tickets, and manuscript-facing revision outputs.

