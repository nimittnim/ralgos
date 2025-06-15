class Generator():
    def __init__(self, sampling_function=None, pdf=None, mean=None,variance=None,k=None, type=None, lower_bound=None, upper_bound=None):
        self.sample = sampling_function
        self.pdf = pdf
        self.mean = mean
        self.variance = variance
        self.k = k
        self.type = type
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound