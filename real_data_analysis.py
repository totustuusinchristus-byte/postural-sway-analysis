"""Analyse one real force-platform record from PhysioNet HBEDB.

The Human Balance Evaluation Database (HBEDB) contains 1-minute force-platform
trials sampled at 100 Hz, including centre-of-pressure x/y channels. This script
downloads a user-selected public WFDB record, extracts CoP, and computes the
same transparent sway metrics used in the synthetic-data project.

Dataset: Santos & Duarte, Human Balance Evaluation Database, PhysioNet v1.0.0.
DOI: 10.13026/C2WW2W
License: Open Data Commons Attribution License v1.0.

Usage:
    python real_data_analysis.py --record BDS00001
"""
from __future__ import annotations
import argparse
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import wfdb
from src.cop_metrics import (
    path_length, mean_velocity, rms_displacement, confidence_ellipse_area
)

PN_DIR = "hbedb/1.0.0"

def load_hbedb_record(record: str):
    rec = wfdb.rdrecord(record, pn_dir=PN_DIR)
    names = [s.lower().replace("-", "").replace("_", "").replace(" ", "")
             for s in rec.sig_name]
    # HBEDB documentation specifies two centre-of-pressure channels (x and y).
    # Prefer explicit CoP labels; fail clearly rather than silently guessing.
    cop_idx = [i for i, n in enumerate(names) if "cop" in n or "centerofpressure" in n]
    if len(cop_idx) < 2:
        raise ValueError(
            f"Could not identify two CoP channels from labels: {rec.sig_name}. "
            "Inspect the record header before adapting the mapping."
        )
    x = rec.p_signal[:, cop_idx[0]].astype(float)
    y = rec.p_signal[:, cop_idx[1]].astype(float)
    return x, y, float(rec.fs), rec.sig_name[cop_idx[0]], rec.sig_name[cop_idx[1]]

def metrics(x, y, fs):
    duration = (len(x) - 1) / fs
    return {
        "n_samples": len(x),
        "sampling_frequency_hz": fs,
        "duration_s": duration,
        "path_length": path_length(x, y),
        "mean_velocity": mean_velocity(x, y, duration),
        "ml_rms": rms_displacement(x),
        "ap_rms": rms_displacement(y),
        "resultant_rms": float(np.sqrt(np.mean((x-x.mean())**2 + (y-y.mean())**2))),
        "ellipse_area_95": confidence_ellipse_area(x, y),
    }

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--record", default="BDS00001",
                   help="HBEDB WFDB record name, e.g. BDS00001")
    args = p.parse_args()

    out = Path("real_data_outputs")
    out.mkdir(exist_ok=True)
    x, y, fs, xlab, ylab = load_hbedb_record(args.record)
    result = metrics(x, y, fs)
    pd.DataFrame([{"record": args.record, **result}]).to_csv(
        out / f"{args.record}_metrics.csv", index=False
    )

    t = np.arange(len(x)) / fs
    fig, ax = plt.subplots()
    ax.plot(x, y, linewidth=0.8)
    ax.set_xlabel(f"{xlab}")
    ax.set_ylabel(f"{ylab}")
    ax.set_title(f"HBEDB stabilogram: {args.record}")
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(out / f"{args.record}_stabilogram.png", dpi=180)
    plt.close(fig)

    fig, ax = plt.subplots()
    ax.plot(t, x, label=xlab, linewidth=0.8)
    ax.plot(t, y, label=ylab, linewidth=0.8)
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Centre of pressure")
    ax.set_title(f"HBEDB CoP time series: {args.record}")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out / f"{args.record}_timeseries.png", dpi=180)
    plt.close(fig)

    print(pd.Series(result).to_string())
    print(f"Saved outputs to {out}/")

if __name__ == "__main__":
    main()
