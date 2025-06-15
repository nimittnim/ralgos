#ifndef MARGULIS_GRAPH_H
#define MARGULIS_GRAPH_H

#include "../utilities/graph.h"
#include <utility>

class MargulisGraph {
public:
    using Vertex = std::pair<int, int>;

    MargulisGraph(int n);

    const Graph<Vertex>& getGraph() const;
    int size() const;
    int degree() const;

private:
    int n;
    Graph<Vertex> g;

    int mod(int a, int m) const;
};

#endif // MARGULIS_GRAPH_H
