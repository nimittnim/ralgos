#include "uuniform.h"
#include <random>

UUniformGenerator::UUniformGenerator(int p, int m)
    : p(p), m(m) {}

int UUniformGenerator::evaluate(int a, int b, int x) const {
    return ((1LL * a * x + b) % p) % m;
}

std::vector<int> UUniformGenerator::sample(int n) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist_a(1, p - 1); // a ≠ 0
    std::uniform_int_distribution<int> dist_b(0, p - 1);

    int a = dist_a(gen);
    int b = dist_b(gen);

    std::vector<int> output(n);
    for (int i = 0; i < n; ++i)
        output[i] = evaluate(a, b, i + 1);

    return output;
}
