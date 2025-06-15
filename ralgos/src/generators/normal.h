#ifndef NORMAL_GENERATOR_H
#define NORMAL_GENERATOR_H

#include <vector>

class NormalGenerator {
    double mean;
    double stddev;

public:
    NormalGenerator(double mean, double stddev);
    std::vector<double> sample(int n) const;
};

#endif // NORMAL_GENERATOR_H
