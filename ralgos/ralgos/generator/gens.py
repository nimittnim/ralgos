import numpy as np
import random
from .utilities import RandomWalk, MargulisGraph

class BernoulliGenerator:
    def __init__(self, biases):
        """
        biases: list or array of length d, 
                each element is the probability of generating 1 for that dimension
        """
        self.biases = np.array(biases, dtype=float)
        if np.any((self.biases < 0) | (self.biases > 1)):
            raise ValueError("All biases must be between 0 and 1.")

    def sample(self, n):
        """
        Generate n samples of d-dimensional Bernoulli random vectors.
        Returns: numpy array of shape (n, d)
        """
        d = len(self.biases)
        # Each column j has probability biases[j] for 1
        return np.random.binomial(1, self.biases, size=(n, d)).tolist()
    

class KUniformGenerator:
    def __init__(self, k: int, p: int, scale: int = 100):
        self.k = k
        self.p = p
        self.scale = scale

    def sample(self, n: int):
        """
        Sample `n` integers uniformly from 0 to scale-1
        """
        return [random.randint(0, self.scale - 1) for _ in range(n)]


class KBernoulliGenerator:
    def __init__(self, k: int, p_: float, p: int):
        self.k = k
        self.p_ = p_
        self.p = p

    def sample(self, n: int):
        gen = KUniformGenerator(self.k, self.p, 100)
        out = gen.sample(n)
        thresh = int(self.p_ * 100)
        return [1 if x < thresh else 0 for x in out]


class NormalGenerator:
    def __init__(self, mean: float, stddev: float):
        self.mean = mean
        self.stddev = stddev

    def sample(self, n: int):
        """
        Sample `n` values from a normal distribution with given mean and stddev.
        Returns a list of floats.
        """
        return np.random.normal(self.mean, self.stddev, size=n).tolist()
    

class UniformGenerator:
    def __init__(self, m: int):
        self.m = m

    def sample(self, n: int):
        """
        Sample `n` integers uniformly from 0 to m-1
        """
        return [random.randint(0, self.m - 1) for _ in range(n)]
    
class UUniformGenerator:
    def __init__(self, p: int, m: int):
        self.p = p
        self.m = m

    def evaluate(self, a: int, b: int, x: int) -> int:
        """Compute ((a*x + b) % p) % m."""
        return ((a * x + b) % self.p) % self.m

    def sample(self, n: int):
        """Generate a sequence of length n using universal hashing."""
        rng = random.Random()
        a = rng.randint(1, self.p - 1)  # a ≠ 0
        b = rng.randint(0, self.p - 1)
        return [self.evaluate(a, b, i + 1) for i in range(n)]

    
class MargulisGenerator:
    def __init__(self, v: int, m: int):
        """
        v: size of the Margulis graph (v x v grid)
        m: modulo for output
        """
        self.v = v
        self.m = m

    def sample(self, n: int):
        """
        Generate n samples by performing a random walk on the Margulis graph.
        Returns a list of integers in range [0, m-1].
        """
        # Construct Margulis graph
        graph = MargulisGraph(self.v).get_graph()

        # Perform random walk
        walker = RandomWalk(graph)
        start = None  # None means pick a random start
        path = walker.walk(start=start, steps=n)

        # Map each (x, y) vertex to integer modulo m
        output = [(x * self.v + y) % self.m for (x, y) in path]
        return output


