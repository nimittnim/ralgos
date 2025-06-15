#ifndef BERNOULLI_GENERATOR_H
#define BERNOULLI_GENERATOR_H

#include <vector>

class BernoulliGenerator {
    double p;

public:
    BernoulliGenerator(double p);

    std::vector<int> sample(int n) const;
};

#endif // BERNOULLI_GENERATOR_H
