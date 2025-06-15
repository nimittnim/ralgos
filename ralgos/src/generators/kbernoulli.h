#ifndef KBERNOULLI_GENERATOR_H
#define KBERNOULLI_GENERATOR_H

#include <vector>

class KBernoulliGenerator {
    int k;
    double p_;
    int p;

public:
    KBernoulliGenerator(int k, double p_, int p);
    std::vector<int> sample(int n) const;
};

#endif // KBERNOULLI_GENERATOR_H
