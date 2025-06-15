#include "kbernoulli.h"
#include "kuniform.h"

KBernoulliGenerator::KBernoulliGenerator(int k, double p_, int p)
    : k(k), p_(p_), p(p) {}

std::vector<int> KBernoulliGenerator::sample(int n) const {
    KUniformGenerator gen(k, p, 100);
    std::vector<int> out = gen.sample(n);
    std::vector<int> output(n);
    int thresh = p_ * 100;

    for (int i = 0; i < n; ++i) {
        output[i] = (out[i] < thresh) ? 1 : 0;
    }

    return output;
}
