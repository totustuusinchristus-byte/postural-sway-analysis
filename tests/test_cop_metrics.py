import numpy as np
from src.cop_metrics import path_length, mean_velocity, rms_displacement, confidence_ellipse_area

def test_path_length_known_line():
    x=np.array([0.,3.,6.]); y=np.array([0.,4.,8.])
    assert np.isclose(path_length(x,y),10.)

def test_mean_velocity():
    assert np.isclose(mean_velocity([0,3],[0,4],2),2.5)

def test_rms_zero_for_constant_signal():
    assert np.isclose(rms_displacement([5,5,5]),0.)

def test_ellipse_area_nonnegative():
    t=np.linspace(0,2*np.pi,100)
    assert confidence_ellipse_area(np.cos(t),2*np.sin(t)) >= 0
