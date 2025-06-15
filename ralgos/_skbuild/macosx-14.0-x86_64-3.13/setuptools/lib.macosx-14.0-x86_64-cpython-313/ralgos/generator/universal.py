from ralgos.ralgos_cpp import UniversalGenerator
from .Generator import Generator

class universal(Generator):
    def __init__(self,p=104729,m=100,seed=1048):
        gen = UniversalGenerator(p,m,seed)
        super().__init__(sampling_function=gen.sample, k="u")