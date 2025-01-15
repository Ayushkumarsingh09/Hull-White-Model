import numpy as np

def zero_coupon_bond_price(a, sigma, r0, T, time_to_maturity):
    """
    Calculate the price of a zero-coupon bond using the Hull-White model.
    :param a: Mean reversion speed
    :param sigma: Volatility
    :param r0: Initial short rate
    :param T: Current time
    :param time_to_maturity: Time to maturity of the bond
    :return: Bond price
    """
    B = (1 - np.exp(-a * time_to_maturity)) / a
    A = np.exp((B - time_to_maturity) * (sigma**2 / (2 * a**2)))
    return A * np.exp(-B * r0)
