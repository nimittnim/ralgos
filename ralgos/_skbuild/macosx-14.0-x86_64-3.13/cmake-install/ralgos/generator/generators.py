from ralgos.ralgos_cpp import KUniformGenerator, NormalGenerator, UniformGenerator, UUniformGenerator,BernoulliGenerator,KBernoulliGenerator, MargulisGenerator
from .Generator import Generator

class kuniform(Generator):
    def __init__(self,k,p=104729,m=100):
        gen = KUniformGenerator(k,p,m)
        super().__init__(sampling_function=gen.sample,mean=m//2, k=k,type="kuniform", lower_bound=0,upper_bound=m)

class normal(Generator):
    def __init__(self,mean=0,std=1,m=100):
        gen = NormalGenerator(float(mean),float(std))
        super().__init__(sampling_function=gen.sample, k="i",type="normal",lower_bound="minus_infinity",upper_bound="plus_infinity")
        self.mean = mean
        self.std = std

class uniform(Generator):
    def __init__(self,m=100):
        gen = UniformGenerator(m)
        super().__init__(sampling_function=gen.sample, k="i",type="uniform",lower_bound=0,upper_bound=m)


class uuniform(Generator):
    def __init__(self,p=104729,m=100):
        gen = UUniformGenerator(p,m)
        super().__init__(sampling_function=gen.sample, k="u",type="uuniform",lower_bound=0,upper_bound=m)

class bernoulli(Generator):
    def __init__(self,p=0.5):
        gen = BernoulliGenerator(p)
        super().__init__(sampling_function=gen.sample,mean=p,variance=p*(1-p),k="i",type="bernoulli",lower_bound=0,upper_bound=1)
        self.p = p

class kbernoulli(Generator):
    def __init__(self,k,p_=0.5,p=104729):
        gen = KBernoulliGenerator(k,p_,p)
        super().__init__(sampling_function=gen.sample,mean=p_,variance=p_*(1-p_),k=k,type="kbernoulli",lower_bound=0,upper_bound=1)
        self.p_ = p_

class margulis(Generator):
    def __init__(self,v,m):
        gen = MargulisGenerator(v,m)
        super().__init__(sampling_function=gen.sample,type="margulis",lower_bound=0,upper_bound=m)
        self.v = v

