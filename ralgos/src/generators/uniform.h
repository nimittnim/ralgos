#ifndef UNIFORM_GENERATOR_H
#define UNIFORM_GENERATOR_H

#include <vector>

class UniformGenerator {
    int m;

public:
    UniformGenerator(int m);
    std::vector<int> sample(int n) const;
};

#endif // UNIFORM_GENERATOR_H
