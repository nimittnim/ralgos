#ifndef UUNIFORM_GENERATOR_H
#define UUNIFORM_GENERATOR_H

#include <vector>

class UUniformGenerator {
    int p;
    int m;

public:
    UUniformGenerator(int p, int m);
    std::vector<int> sample(int n) const;

private:
    int evaluate(int a, int b, int x) const;
};

#endif // UUNIFORM_GENERATOR_H
