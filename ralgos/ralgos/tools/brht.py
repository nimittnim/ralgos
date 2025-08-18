import numpy as np
from scipy.linalg import hadamard

class BlockRandomizedTransform:
    def __init__(self, d, b, e):
        """
        d : int
            Dimension (must be power of 2 for Hadamard transform)
        b : int
            Number of blocks (must divide d)
        R : float
            Desired L2 norm of input vector
        """
        assert d % b == 0, "d must be divisible by b"
        self.d = d
        self.b = b
        self.block_size = d // b
        self.e = e
        self.H = hadamard(d) / np.sqrt(d)

    def generate_vector(self):
        """Generate a random vector with L2 norm = R"""
        x = np.random.randn(self.d)
        return self.e * x / np.linalg.norm(x)

    def transform(self, x):
        """
        Apply block randomized transform to vector x.
        """
        assert len(x) == self.d, "Input vector must have dimension d"

        # Generate block-wise Rademacher vector
        epsilons = np.random.choice([-1, 1], size=self.b)

        # Apply block-wise sign flips
        Dx = np.zeros_like(x)
        for i in range(self.b):
            Dx[i*self.block_size:(i+1)*self.block_size] = (
                epsilons[i] * x[i*self.block_size:(i+1)*self.block_size]
            )

        # Apply normalized Hadamard transform
        y = self.H @ Dx

        return y
    
