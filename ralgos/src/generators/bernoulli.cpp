#include "bernoulli.h"
#include <random>

BernoulliGenerator::BernoulliGenerator(double p)
    : p(p) {}

std::vector<int> BernoulliGenerator::sample(int n) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::bernoulli_distribution dist(p);

    std::vector<int> output(n);
    for (int i = 0; i < n; ++i) {
        output[i] = dist(gen);
    }
    return output;
}
