import math
from ralgos.make.rvnode import RV,Sum,Product,Constant
(errmessage) = "Not Implemented or Applicable Yet!"

def hoeffding(rv,t):
    if isinstance(rv,RV):
        a = rv.generator.lower_bound
        b = rv.generator.upper_bound
        if (a == "minf" or a == "pinf" or b == "minf" or b == "pinf"):
            return errmessage
        mu = rv.generator.mean
        return math.exp(-(2*(t-mu)**2)/(b-a)**2)
    elif isinstance(rv,Sum):
        c = 0
        mu = 0
        for brv in rv.children:
            if not isinstance(brv, RV):
                return errmessage       
            mu += brv.generator.mean
            a = brv.generator.lower_bound
            b = brv.generator.upper_bound
            if (a == "minf" or a == "pinf" or b == "minf" or b == "pinf"):
                return errmessage+"0"
            c += (b - a)**2
        return math.exp(-(2*(t-mu)**2)/c)
    elif isinstance(rv,Product):
        pass
    elif isinstance(rv,Constant):
        if (rv.value < t):
            return 0
        return 1

    return errmessage