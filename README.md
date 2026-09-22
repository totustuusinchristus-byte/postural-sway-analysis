# Postural Sway / Centre-of-Pressure Analysis in Python

A learning-oriented project for analysing synthetic force-plate-like centre-of-pressure (CoP) data during quiet standing.

## Aim
Develop a reproducible workflow for visualising CoP trajectories and calculating descriptive sway measures: total path length, mean velocity, mediolateral and anteroposterior RMS displacement, resultant RMS displacement, and covariance-based 95% ellipse area.

## Scope
The data are synthetic. This repository does not claim force-plate laboratory or clinical balance-assessment experience.

## Simulated conditions
The teaching dataset represents eyes-open/eyes-closed and firm/compliant surface conditions with repeated trials. Differences are intentionally simulated and are not experimental evidence.

## Tools
Python, NumPy, pandas, SciPy, Matplotlib and Jupyter.

## Key concepts
CoP is related to, but not identical to, centre of mass. Sway measures depend on recording duration, sampling and preprocessing, and a larger sway value is not automatically synonymous with worse balance.

## Learning goals
- visualise ML/AP CoP trajectories;
- calculate common sway metrics;
- compare repeated trials;
- examine sensitivity to recording duration and processing choices;
- interpret descriptive balance measures cautiously.

## Next development
Complete the notebook sensitivity analysis and later reproduce the workflow with a properly licensed open balance dataset.

## Research integrity
This repository documents developing computational skills. Synthetic data and guided code are clearly distinguished from experimental research experience.