#include "uniform.h"
#include <random>

UniformGenerator::UniformGenerator(int m)
    : m(m) {}

std::vector<int> UniformGenerator::sample(int n) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, m - 1);

    std::vector<int> output(n);
    for (int i = 0; i < n; ++i)
        output[i] = dist(gen);
    return output;
}
