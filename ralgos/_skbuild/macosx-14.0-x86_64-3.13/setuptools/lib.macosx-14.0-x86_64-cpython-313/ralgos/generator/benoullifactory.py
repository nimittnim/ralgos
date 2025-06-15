from .Generator import Generator

class bernoulliFactory(Generator):
    def __init__(self, genp, f):
        if f == "p^2":
            def sample(n):
                outputs = []
                for i in range(n):
                    samples = genp.sample(2)
                    if samples == [1,1]:
                        outputs.append(1)
                    else: 
                        outputs.append(0)

        if f == "2p":
            def sample(n):
                outputs = []
                for i in range(n):
                    while True:
                        sampled = genp.sample
                        if (a, b) in [(0, 1), (1, 0)]:
                            return 1
                        elif (a, b) == (0, 0):
                            return 0