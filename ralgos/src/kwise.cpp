#include <vector>
#include <random>

const int MOD = 104729; 

class KwiseGenerator {
    std::vector<int> coefficients;
    int seed;

public:
    KwiseGenerator(int k, int seed) : seed(seed) {
        std::mt19937 gen(seed);
        std::uniform_int_distribution<int> dist(0, MOD - 1);
        coefficients.resize(k);
        for (int i = 0; i < k; ++i)
            coefficients[i] = dist(gen);
    }

    int evaluate(int x) const {
        int result = 0;
        int power = 1;
        for (int coeff : coefficients) {
            result = (result + (1LL * coeff * power) % MOD) % MOD;
            power = (1LL * power * x) % MOD;
        }
        return result;
    }

    std::vector<int> sample(int n) const {
        std::vector<int> output(n);
        for (int i = 0; i < n; ++i)
            output[i] = evaluate(i + 1); // Avoid x = 0 for simplicity
        return output;
    }
};
