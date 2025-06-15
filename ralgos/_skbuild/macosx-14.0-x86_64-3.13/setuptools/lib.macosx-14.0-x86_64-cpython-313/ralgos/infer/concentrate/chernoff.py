import math
from ralgos.make.rvnode import RV, Sum, Product, Constant

def chernoff(rv, t):
    # Check if rv is a base rv
    if isinstance(rv, RV):

        generator = rv.generator
        gen_type = getattr(generator, "type", None)

        if gen_type == "normal":
            mu = getattr(generator, "mean", None)
            sigma = getattr(generator, "std", None)
            if mu is None or sigma is None:
                raise ValueError("Normal generator must have mean and std attributes.")
            bound = math.exp(- (t ** 2) / (2 * sigma ** 2))
            return bound
        
        elif gen_type=="uniform":
            pass

        elif gen_type == "kuniform":
            pass

        elif gen_type == "uuniform":
            pass

        elif gen_type == "bernoulli":
            pass

        elif gen_type == "kbernoulli":
            pass
    
    elif isinstance(rv, Sum):
        pass

    elif isinstance(rv, Product):
        pass

    elif isinstance(rv,Constant):
        if (rv.value < t):
            return 0
        return 1
    
    return "Not Implmeneted or Applicable Yet!"
    
