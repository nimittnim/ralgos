import numpy as np

class UniformityTester:
    def __init__(self, generator, epsilon, d, c=10):
        """
        generator: a generator with .sample(n) -> list/array of integers in [0, d-1]
        epsilon: distance parameter
        c: constant factor for sample complexity (tuning knob)
        """
        self.generator = generator
        self.epsilon = epsilon
        self.d
        self.c = c

    def test(self):
        # Dimension of domain (assume generator outputs ints in [0, d-1])
        d = self.d
        m = int(self.c * np.sqrt(d) / (self.epsilon ** 2))

        # Poissonize
        N = np.random.poisson(m)

        # Draw samples
        samples = self.generator.sample(N)
        counts = np.bincount(samples, minlength=d)

        # Compute χ² statistic
        expected = m / d
        Z = np.sum(((counts - expected) ** 2 - counts) / expected)

        # Threshold
        threshold = 0.5 * m * (self.epsilon ** 2)
        is_uniform = Z <= threshold

        return is_uniform, Z, threshold, counts
