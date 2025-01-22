import matplotlib.pyplot as plt
import numpy as np

def plot_option_prices(strikes, prices, option_type="call"):
    """
    Plots option prices against strike prices.
    :param strikes: Array of strike prices
    :param prices: Array of option prices
    :param option_type: Type of option ("call" or "put")
    """
    plt.figure(figsize=(10, 6))
    plt.plot(strikes, prices, label=f"{option_type.capitalize()} Option Prices", marker="o")
    plt.title(f"Option Prices vs Strike Prices ({option_type.capitalize()})")
    plt.xlabel("Strike Price")
    plt.ylabel("Option Price")
    plt.grid()
    plt.legend()
    plt.show()
