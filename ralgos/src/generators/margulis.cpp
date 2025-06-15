#include "../expanders/margulis.h"
#include "../utilities/rwalk.h"
#include "margulis.h"

MargulisGenerator::MargulisGenerator(int v, int m)
    : v(v), m(m) {}

std::vector<int> MargulisGenerator::sample(int n) const {
    MargulisGraph graph(v);
    const auto& g = graph.getGraph();

    using Vertex = std::pair<int, int>;
    RandomWalk<Vertex> walker(g);

    Vertex start = {-1, -1}; // use (-1, -1) to pick a random starting node
    std::vector<Vertex> path = walker.walk(start, n);

    std::vector<int> output(n);
    for (int i = 0; i < n; ++i) {
        int x = path[i].first;
        int y = path[i].second;
        int id = x * v + y;
        output[i] = id % m;
    }

    return output;
}
