import pytest
from src.bond_pricing import zero_coupon_bond_price

def test_bond_price():
    price = zero_coupon_bond_price(a=0.1, sigma=0.02, r0=0.03, T=0, time_to_maturity=5)
    assert price > 0, "Bond price must be positive"
    assert price < 1, "Bond price exceeds face value for zero-coupon bond"
