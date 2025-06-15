import math
from ralgos.make.rvnode import RV

def chernoff(rv, t):
    if not isinstance(rv, RV):
        raise ValueError("Chernoff bound only implemented for base RVs.")

    generator = rv.generator
    gen_type = getattr(generator, "type", None)

    if gen_type != "normal":
        raise ValueError("Chernoff bound currently only supports normal distribution.")

    mu = getattr(generator, "mean", None)
    sigma = getattr(generator, "std", None)

    if mu is None or sigma is None:
        raise ValueError("Normal generator must have mean and std attributes.")

    bound = math.exp(- (t ** 2) / (2 * sigma ** 2))
    return bound