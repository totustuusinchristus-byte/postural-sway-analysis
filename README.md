# Postural Sway / Centre-of-Pressure Analysis in Python

A reproducible learning project for quantitative analysis of synthetic force-plate-like centre-of-pressure (CoP) data.

## Scientific question
How can quiet-standing CoP trajectories be summarized with interpretable spatial and temporal sway metrics across simulated sensory conditions?

## Measures
Total CoP path length, mean CoP velocity, mediolateral (ML) and anteroposterior (AP) RMS displacement, resultant RMS displacement, and covariance-based 95% ellipse area.

## Reproduce
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python generate_synthetic_data.py
python analysis.py
pytest -q
```

## Repository structure
- `analysis.py` — trial-level metrics, condition summaries and plotting.
- `generate_synthetic_data.py` — reproducible simulated CoP trajectories.
- `src/cop_metrics.py` — reusable CoP metric functions.
- `tests/` — basic automated checks.
- `LEARNING_GUIDE.md` — concepts and exercises.
- `.github/workflows/` — automated Python checks.

## Skills demonstrated
Python, NumPy, pandas, Matplotlib, quantitative balance analysis, repeated-trial summaries, reproducibility and basic testing.

## Interpretation and limitations
CoP is related to but is not the same as centre of mass. Sway metrics depend on trial duration, sampling and preprocessing, and a larger value is not automatically synonymous with poorer balance. The conditions and differences here are simulated; they are not experimental findings and do **not** claim force-platform laboratory experience.

## Development goals
Complete duration/parameter sensitivity analyses and extend the workflow to an appropriately licensed open balance dataset.


## Real-data extension: PhysioNet HBEDB
The repository now includes `real_data_analysis.py`, a separate workflow for the **Human Balance Evaluation Database (HBEDB)** on PhysioNet (Santos & Duarte; DOI: 10.13026/C2WW2W). HBEDB contains public force-platform stabilography recordings with CoP channels. The database reports 1-minute trials sampled at 100 Hz under eyes-open/eyes-closed and rigid/unstable-surface conditions.

Run a record with:
```bash
python real_data_analysis.py --record BDS00001
```

The script downloads the selected record through WFDB, identifies documented CoP channels from their labels, computes the project's sway metrics, and saves a stabilogram, CoP time series and metrics table in `real_data_outputs/`. It deliberately fails rather than guessing if two CoP channels cannot be identified.

**Data provenance:** the source data are not redistributed in this repository. They remain hosted by PhysioNet under the Open Data Commons Attribution License v1.0. Results from the real-data workflow should not be described as validated until the selected record, channel mapping, units and outputs have been inspected.
