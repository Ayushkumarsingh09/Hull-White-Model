import numpy as np
from scipy.stats import norm
from src.bond_pricing import zero_coupon_bond_price

def european_option_price(a, sigma, r0, T, time_to_maturity, strike, option_type="call"):
    """
    Price a European option on a zero-coupon bond.
    :param a: Mean reversion speed
    :param sigma: Volatility
    :param r0: Initial short rate
    :param T: Current time
    :param time_to_maturity: Time to maturity of the bond
    :param strike: Strike price of the option
    :param option_type: "call" or "put"
    :return: Option price
    """
    bond_price = zero_coupon_bond_price(a, sigma, r0, T, time_to_maturity)
    bond_vol = sigma * np.sqrt((1 - np.exp(-2 * a * time_to_maturity)) / (2 * a))
    d1 = (np.log(bond_price / strike) + 0.5 * bond_vol**2) / bond_vol
    d2 = d1 - bond_vol

    if option_type == "call":
        return bond_price * norm.cdf(d1) - strike * np.exp(-r0 * T) * norm.cdf(d2)
    elif option_type == "put":
        return strike * np.exp(-r0 * T) * norm.cdf(-d2) - bond_price * norm.cdf(-d1)
    else:
        raise ValueError("Option type must be 'call' or 'put'")
