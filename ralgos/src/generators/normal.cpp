#include "normal.h"
#include <random>

NormalGenerator::NormalGenerator(double mean, double stddev)
    : mean(mean), stddev(stddev) {}

std::vector<double> NormalGenerator::sample(int n) const {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::normal_distribution<double> dist(mean, stddev);

    std::vector<double> output(n);
    for (int i = 0; i < n; ++i) {
        output[i] = dist(gen);
    }
    return output;
}
