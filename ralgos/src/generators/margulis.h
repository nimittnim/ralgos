#ifndef MARGULIS_GENERATOR_H
#define MARGULIS_GENERATOR_H

#include <vector>

class MargulisGenerator {
public:
    MargulisGenerator(int v, int m);
    std::vector<int> sample(int n) const;

private:
    int v, m;
};

#endif // MARGULIS_GENERATOR_H
