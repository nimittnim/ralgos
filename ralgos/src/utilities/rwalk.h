#ifndef RWALK_H
#define RWALK_H

#include "graph.h"
#include <vector>
#include <random>
#include <stdexcept>

template <typename T>
class RandomWalk {
public:
    RandomWalk(const Graph<T>& g, int seed = std::random_device{}())
        : graph(g), rng(seed) {}

        std::vector<T> walk(const T& start, int steps) {
        std::vector<T> path;
        T current = start;

        if (current == T{-1, -1}) {
            // Pick a random start node from graph
            if (graph.empty()) throw std::runtime_error("Graph is empty.");
            const auto& all = graph.vertices();
            std::uniform_int_distribution<> dist(0, all.size() - 1);
            current = all[dist(rng)];
        }

        path.push_back(current);

        for (int i = 0; i < steps; ++i) {
            const auto& neighbors = graph.neighbors(current);
            if (neighbors.empty()) break;

            std::uniform_int_distribution<> dist(0, neighbors.size() - 1);
            current = neighbors[dist(rng)];
            path.push_back(current);
        }

        return path;
    }


private:
    const Graph<T>& graph;
    std::mt19937 rng;
};

#endif // RWALK_H
