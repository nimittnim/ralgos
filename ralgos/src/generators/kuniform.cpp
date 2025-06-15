#include "kuniform.h"
#include <random>

KUniformGenerator::KUniformGenerator(int k, int p, int m)
    : k(k), p(p), m(m) {}

int KUniformGenerator::evaluate(const std::vector<int>& coefficients, int x) const {
    int result = 0;
    int power = 1;
    for (int coeff : coefficients) {
        result = (result + (1LL * coeff * power) % p) % p;
        power = (1LL * power * x) % p;
    }
    return result % m;
}

std::vector<int> KUniformGenerator::sample(int n) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<int> dist(0, p - 1);

    std::vector<int> coefficients(k);
    for (int i = 0; i < k; ++i)
        coefficients[i] = dist(gen);

    std::vector<int> output(n);
    for (int i = 0; i < n; ++i)
        output[i] = evaluate(coefficients, i + 1);

    return output;
}
