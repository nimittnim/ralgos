from ralgos.ralgos_cpp import KwiseGenerator 

class Generator():
    def __init__(self, sampling_function, k):
        self.generate = sampling_function
        self.k = k

def kwise():
    generator = KwiseGenerator(2,1048)
    return generator.sample