"""Generate reproducible synthetic centre-of-pressure data."""
from pathlib import Path
import numpy as np
import pandas as pd

FS=100; DURATION=30
rng=np.random.default_rng(20260922)
conditions={"eyes_open_firm":(2.2,2.6,.18),"eyes_closed_firm":(2.8,3.2,.22),
"eyes_open_compliant":(3.5,4.0,.28),"eyes_closed_compliant":(4.8,5.5,.34)}
rows=[]
for cond,(sx,sy,noise) in conditions.items():
    for trial in range(1,4):
        t=np.arange(0,DURATION,1/FS); wx=rng.normal(0,noise,len(t)); wy=rng.normal(0,noise,len(t))
        x=np.zeros_like(t); y=np.zeros_like(t)
        for i in range(1,len(t)):
            x[i]=.985*x[i-1]+wx[i]; y[i]=.985*y[i-1]+wy[i]
        x=x/np.std(x)*sx+.8*np.sin(2*np.pi*.12*t+rng.uniform(0,6))
        y=y/np.std(y)*sy+1*np.sin(2*np.pi*.09*t+rng.uniform(0,6))
        rows.extend((cond,trial,ti,xi,yi) for ti,xi,yi in zip(t,x,y))
Path("data").mkdir(exist_ok=True)
pd.DataFrame(rows,columns=["condition","trial","time_s","cop_ml_mm","cop_ap_mm"]).to_csv(
"data/synthetic_cop.csv",index=False)
print("Created data/synthetic_cop.csv")
