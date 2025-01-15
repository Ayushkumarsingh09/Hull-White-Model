import pytest
import numpy as np
from src.calibration import calibrate_hull_white

def test_calibration():
    market_data = {"time": np.array([1, 2, 3, 5, 10]), "yield": np.array([0.02, 0.025, 0.03, 0.035, 0.04])}
    params = calibrate_hull_white(market_data, initial_guess=(0.1, 0.01))
    assert params["a"] > 0, "Mean reversion speed (a) is invalid"
    assert params["sigma"] > 0, "Volatility (sigma) is invalid"
