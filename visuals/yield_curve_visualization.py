import matplotlib.pyplot as plt
import numpy as np

def plot_yield_curve(times, yields):
    """
    Plots the yield curve.
    :param times: Array of time to maturity
    :param yields: Array of yields
    """
    plt.figure(figsize=(10, 6))
    plt.plot(times, yields, label="Yield Curve", marker="o")
    plt.title("Yield Curve")
    plt.xlabel("Time to Maturity (Years)")
    plt.ylabel("Yield (%)")
    plt.grid()
    plt.legend()
    plt.show()

def plot_short_rate_simulation(times, rates):
    """
    Plots short-rate simulations.
    :param times: Time steps
    :param rates: Matrix of simulated short rates
    """
    plt.figure(figsize=(12, 6))
    for i in range(min(rates.shape[0], 20)):  # Plot up to 20 paths for clarity
        plt.plot(times, rates[i, :], alpha=0.7)
    plt.title("Simulated Short Rates under Hull-White Model")
    plt.xlabel("Time (Years)")
    plt.ylabel("Short Rate (%)")
    plt.grid()
    plt.show()
