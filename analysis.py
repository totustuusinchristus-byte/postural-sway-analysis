"""Calculate trial-level CoP metrics and save summary figures."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from src.cop_metrics import path_length,mean_velocity,rms_displacement,resultant_rms,confidence_ellipse_area

FS=100
Path("figures").mkdir(exist_ok=True)
if not Path("data/synthetic_cop.csv").exists():
    exec(Path("generate_synthetic_data.py").read_text())
df=pd.read_csv("data/synthetic_cop.csv")
rows=[]
for (condition,trial),g in df.groupby(["condition","trial"]):
    x=g.cop_ml_mm.to_numpy(); y=g.cop_ap_mm.to_numpy(); duration=(len(g)-1)/FS
    rows.append({"condition":condition,"trial":trial,"path_length_mm":path_length(x,y),
    "mean_velocity_mm_s":mean_velocity(x,y,duration),"rms_ml_mm":rms_displacement(x),
    "rms_ap_mm":rms_displacement(y),"resultant_rms_mm":resultant_rms(x,y),
    "ellipse95_area_mm2":confidence_ellipse_area(x,y)})
metrics=pd.DataFrame(rows); metrics.to_csv("data/trial_metrics.csv",index=False)
summary=metrics.groupby("condition").mean(numeric_only=True)
summary.to_csv("data/condition_summary.csv")
example=df[(df.condition=="eyes_open_firm")&(df.trial==1)]
plt.figure(figsize=(6,6)); plt.plot(example.cop_ml_mm,example.cop_ap_mm,lw=.7)
plt.xlabel("CoP ML (mm)"); plt.ylabel("CoP AP (mm)"); plt.axis("equal"); plt.tight_layout()
plt.savefig("figures/example_stabilogram.png",dpi=160); plt.close()
print(summary.round(3))
