import pytest
from src.option_pricing import european_option_price

def test_option_price():
    price = european_option_price(a=0.1, sigma=0.02, r0=0.03, T=0, time_to_maturity=5, strike=0.95, option_type="call")
    assert price > 0, "Option price must be positive"
