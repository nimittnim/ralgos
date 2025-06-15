#ifndef KUNIFORM_GENERATOR_H
#define KUNIFORM_GENERATOR_H

#include <vector>

class KUniformGenerator {
    int k;
    int p;
    int m;

public:
    KUniformGenerator(int k, int p, int m);
    std::vector<int> sample(int n) const;

private:
    int evaluate(const std::vector<int>& coefficients, int x) const;
};

#endif // KUNIFORM_GENERATOR_H
