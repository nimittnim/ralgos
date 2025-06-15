#ifndef GRAPH_H
#define GRAPH_H

#include <unordered_map>
#include <vector>
#include <iostream>
#include <utility>
#include <functional>

// Specialize std::hash for std::pair<int, int>
namespace std {
    template <>
    struct hash<std::pair<int, int>> {
        std::size_t operator()(const std::pair<int, int>& p) const noexcept {
            std::size_t h1 = std::hash<int>{}(p.first);
            std::size_t h2 = std::hash<int>{}(p.second);
            return h1 ^ (h2 << 1); // XOR + shift to combine
        }
    };
}

template <typename T>
class Graph {
public:
    Graph() {}

    void addEdge(const T& u, const T& v, bool bidirectional = true) {
        adj[u].push_back(v);
        if (bidirectional) {
            adj[v].push_back(u);
        }
    }

    void print() const {
        for (const auto& [node, neighbors] : adj) {
            std::cout << node << " -> ";
            for (const auto& neigh : neighbors) {
                std::cout << neigh << " ";
            }
            std::cout << std::endl;
        }
    }

    bool empty() const {
        return adj.empty();
    }

    std::vector<T> vertices() const {
        std::vector<T> result;
        for (const auto& [node, _] : adj) {
            result.push_back(node);
        }
        return result;
    }


    const std::vector<T>& neighbors(const T& node) const {
        return adj.at(node);
    }

private:
    std::unordered_map<T, std::vector<T>> adj;
};

#endif // GRAPH_H
