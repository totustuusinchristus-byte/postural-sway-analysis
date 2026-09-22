"""Basic centre-of-pressure metrics for a teaching portfolio project."""
import numpy as np

def path_length(x_mm, y_mm):
    x = np.asarray(x_mm, dtype=float)
    y = np.asarray(y_mm, dtype=float)
    return float(np.sum(np.hypot(np.diff(x), np.diff(y))))

def mean_velocity(x_mm, y_mm, duration_s):
    return path_length(x_mm, y_mm) / float(duration_s)

def rms_displacement(signal_mm):
    x = np.asarray(signal_mm, dtype=float)
    x = x - np.mean(x)
    return float(np.sqrt(np.mean(x**2)))

def resultant_rms(x_mm, y_mm):
    x = np.asarray(x_mm, dtype=float) - np.mean(x_mm)
    y = np.asarray(y_mm, dtype=float) - np.mean(y_mm)
    return float(np.sqrt(np.mean(x**2 + y**2)))

def confidence_ellipse_area(x_mm, y_mm, chi2_95=5.991):
    """Covariance-based 95% confidence ellipse area in mm^2."""
    xy = np.column_stack([np.asarray(x_mm, float), np.asarray(y_mm, float)])
    cov = np.cov(xy, rowvar=False)
    eigvals = np.maximum(np.linalg.eigvalsh(cov), 0)
    semi_axes = np.sqrt(chi2_95 * eigvals)
    return float(np.pi * semi_axes[0] * semi_axes[1])
