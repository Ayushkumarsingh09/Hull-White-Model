import numpy as np

class HullWhiteModel:
    def __init__(self, a: float, sigma: float, r0: float):
        """
        Initialize the Hull-White Model parameters.
        :param a: Mean reversion speed
        :param sigma: Volatility
        :param r0: Initial short rate
        """
        self.a = a
        self.sigma = sigma
        self.r0 = r0

    def simulate_short_rate(self, T: float, dt: float, n_paths: int):
        """
        Simulates the short rate process under the Hull-White model.
        :param T: Time horizon (years)
        :param dt: Time step
        :param n_paths: Number of simulation paths
        :return: Simulated short rates
        """
        n_steps = int(T / dt)
        rates = np.zeros((n_paths, n_steps + 1))
        rates[:, 0] = self.r0

        for t in range(1, n_steps + 1):
            z = np.random.normal(0, 1, n_paths)
            rates[:, t] = rates[:, t - 1] + self.a * (0 - rates[:, t - 1]) * dt + self.sigma * np.sqrt(dt) * z

        return rates
