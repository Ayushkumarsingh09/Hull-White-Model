import pytest
import numpy as np
from src.hull_white_model import HullWhiteModel

def test_short_rate_simulation():
    model = HullWhiteModel(a=0.1, sigma=0.02, r0=0.03)
    rates = model.simulate_short_rate(T=1.0, dt=0.01, n_paths=100)
    assert rates.shape == (100, 101), "Simulation output shape mismatch"
    assert np.all(rates >= 0), "Negative rates found in simulation"
