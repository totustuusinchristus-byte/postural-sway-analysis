import numpy as np
from types import SimpleNamespace
from unittest.mock import patch

import real_data_analysis


def test_hbedb_cop_is_converted_from_cm_to_mm():
    fake = SimpleNamespace(
        sig_name=["Force_x", "Force_y", "Force_z", "Moment_x", "Moment_y", "Moment_z", "COP_x", "COP_y"],
        p_signal=np.array([[0,0,0,0,0,0,1.2,-0.5],[0,0,0,0,0,0,1.3,-0.4]], dtype=float),
        fs=100.0,
    )
    with patch("real_data_analysis.wfdb.rdrecord", return_value=fake):
        x, y, fs, xlab, ylab = real_data_analysis.load_hbedb_record("BDS00001")
    assert np.allclose(x, [12.0, 13.0])
    assert np.allclose(y, [-5.0, -4.0])
    assert fs == 100.0
    assert "COP" in xlab.upper()
    assert "COP" in ylab.upper()
