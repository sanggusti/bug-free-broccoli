# Runs

Scripts for launching, monitoring, and recording ADK agent experiment runs.

## Purpose

- Provide a reproducible entry-point for each experiment
- Persist run metadata (parameters, timestamps, results) for later analysis
- Integrate with the evaluation harness in `scripts/eval/`

## Usage

```bash
python scripts/runs/start_run.py --config scripts/configs/run_config.yaml
```
