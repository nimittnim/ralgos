#include "margulis.h"

MargulisGraph::MargulisGraph(int n) : n(n), g() {
    for (int x = 0; x < n; ++x) {
        for (int y = 0; y < n; ++y) {
            Vertex v = {x, y};

            std::vector<Vertex> neighbors = {
                {mod(x + y, n), y},
                {mod(x - y, n), y},
                {mod(x + y + 1, n), y},
                {mod(x - y - 1, n), y},
                {x, mod(y + x, n)},
                {x, mod(y - x, n)},
                {x, mod(y + x + 1, n)},
                {x, mod(y - x - 1, n)}
            };

            for (const auto& u : neighbors) {
                g.addEdge(v, u, false);  // Margulis is directed if not made bidirectional
            }
        }
    }
}

int MargulisGraph::mod(int a, int m) const {
    return (a % m + m) % m;
}

const Graph<MargulisGraph::Vertex>& MargulisGraph::getGraph() const {
    return g;
}

int MargulisGraph::size() const {
    return n * n;
}

int MargulisGraph::degree() const {
    return 8;
}
