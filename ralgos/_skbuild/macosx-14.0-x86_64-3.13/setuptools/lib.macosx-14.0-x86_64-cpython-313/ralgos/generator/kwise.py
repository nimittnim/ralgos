from ralgos.ralgos_cpp import KwiseGenerator 
from .Generator import Generator

class kwise(Generator):
    def __init__(self,k,p=104729,m=100,seed=1048):
        gen = KwiseGenerator(k,p,m,seed)
        super().__init__(sampling_function=gen.sample, k=k)