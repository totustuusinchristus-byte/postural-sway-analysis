# Postural Sway / Centre-of-Pressure Analysis in Python

A reproducible learning project for quantitative analysis of centre-of-pressure (CoP) data, combining simulated force-plate-like recordings with a validated example using a public human balance dataset.

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
- `real_data_analysis.py` — analysis of a selected public HBEDB force-platform record.\n- `.github/workflows/` — automated Python checks and real-record validation.

## Skills demonstrated
Python, NumPy, pandas, Matplotlib, quantitative balance analysis, repeated-trial summaries, reproducibility and basic testing.

## Interpretation and limitations
CoP is related to but is not the same as centre of mass. Sway metrics depend on trial duration, sampling and preprocessing, and a larger value is not automatically synonymous with poorer balance. The conditions and differences here are simulated; they are not experimental findings and do **not** claim force-platform laboratory experience.

## Development goals
Extend the real-data workflow to additional records/conditions and explore duration, preprocessing and parameter sensitivity while keeping clinical interpretation separate from descriptive sway analysis.


## Real-data extension: PhysioNet HBEDB
The repository now includes `real_data_analysis.py`, a separate workflow for the **Human Balance Evaluation Database (HBEDB)** on PhysioNet (Santos & Duarte; DOI: 10.13026/C2WW2W). HBEDB contains public force-platform stabilography recordings with CoP channels. The database reports 1-minute trials sampled at 100 Hz under eyes-open/eyes-closed and rigid/unstable-surface conditions.

Run a record with:
```bash
python real_data_analysis.py --record BDS00001
```

The script downloads the selected record through WFDB, identifies documented CoP channels from their labels, computes the project's sway metrics, and saves a stabilogram, CoP time series and metrics table in `real_data_outputs/`. HBEDB documents CoP in centimetres; the script explicitly converts these values to millimetres before calling the repository's metric functions, whose inputs and outputs are defined in millimetres. It deliberately fails rather than guessing if two CoP channels cannot be identified.

### Validated example: BDS00001
The GitHub Actions real-data workflow successfully processed public HBEDB record `BDS00001` end to end. The record contained 6,000 samples at 100 Hz (59.99 s). After the documented centimetre-to-millimetre conversion, the workflow produced:

| Metric | Result |
| --- | ---: |
| CoP path length | 372.114 mm |
| Mean CoP velocity | 6.203 mm/s |
| ML RMS displacement | 2.963 mm |
| AP RMS displacement | 1.692 mm |
| Resultant RMS displacement | 3.412 mm |
| 95% ellipse area | 94.383 mm² |

The generated stabilogram and CoP time series were visually inspected for continuity and gross processing problems. They showed continuous trajectories across the recording without obvious clipping, missing segments or isolated extreme spikes. This is a reproducibility/processing validation of the workflow, **not** a clinical classification of the participant or a claim that these values are normal or abnormal.

The workflow `.github/workflows/real-data-validation.yml` repeats this analysis on GitHub Actions and preserves the metrics CSV and plots as a workflow artifact.

**Data provenance:** the source data are not redistributed in this repository. They remain hosted by PhysioNet under the Open Data Commons Attribution License v1.0.
