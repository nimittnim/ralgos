import math
from ralgos.make.rvnode import RV, Sum, Product, Constant

def chernoff(rv, t):
    # Check if rv is a base rv
    message = "Not Implemented or Applicable Yet!"

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
        
        elif gen_type == "uniform":
            pass

        elif gen_type == "kuniform":
            pass

        elif gen_type == "uuniform":
            pass

        elif gen_type == "bernoulli":
            pass

        elif gen_type == "kbernoulli":
            pass
            
        elif gen_type == "margulis":
            pass


    elif isinstance(rv, Sum):

        rvnode0 = rv.children[0]
        if (not isinstance(rvnode0,RV)): 
                return message
        
        gen_type = rv.children[0].generator.type
        
        for rvnode in rv.children:
            if (not isinstance(rvnode,RV)): 
                return message
            if (rvnode.generator != rvnode0.generator):
                return message
        
        if (gen_type == "bernoulli"):
            p = rvnode0.generator.p
            n = len(rv.children)
            p = n*p
            return ((p/t)**t)*(((n-p)/(n-t))**(n-t))
        
        elif (gen_type == "kbernoulli"):
            return message
        
        elif (gen_type == "uuniform"):
            return message
        
        elif (gen_type == "kuniform"):
            return message
        
        elif (gen_type == "uniform"):
            return message
        
        elif (gen_type == "normal"):
            return message
        
        elif (gen_type == "margulis"):
            return message
            

    elif isinstance(rv, Product):
        pass

    elif isinstance(rv,Constant):
        if (rv.value < t):
            return 0
        return 1
    
    return message
    
