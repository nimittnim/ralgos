import random


class Graph:
    def __init__(self):
        # adjacency list: node -> list of neighbors
        self.adj = {}

    def add_edge(self, u, v, bidirectional=True):
        """
        Add an edge from u to v. If bidirectional=True, also add edge v->u.
        """
        if u not in self.adj:
            self.adj[u] = []
        self.adj[u].append(v)

        if bidirectional:
            if v not in self.adj:
                self.adj[v] = []
            self.adj[v].append(u)

    def neighbors(self, node):
        """
        Return the list of neighbors of the node.
        Raises KeyError if node not in graph.
        """
        return self.adj[node]

    def vertices(self):
        """Return a list of all vertices in the graph."""
        return list(self.adj.keys())

    def empty(self):
        """Check if the graph has no vertices."""
        return len(self.adj) == 0

    def print_graph(self):
        """Print adjacency list of the graph."""
        for node, neighbors in self.adj.items():
            print(f"{node} -> {' '.join(map(str, neighbors))}")


class RandomWalk:
    def __init__(self, graph, seed=None):
        """
        graph: an instance of Graph
        seed: optional random seed
        """
        self.graph = graph
        self.rng = random.Random(seed)

    def walk(self, start=None, steps=10):
        """
        Perform a random walk starting from `start` for `steps` steps.
        If start is None, pick a random node from the graph.
        Returns a list of visited nodes.
        """
        if self.graph.empty():
            raise RuntimeError("Graph is empty.")

        # Pick a random start if start not provided
        if start is None:
            start = self.rng.choice(self.graph.vertices())

        path = [start]
        current = start

        for _ in range(steps):
            neighbors = self.graph.neighbors(current)
            if not neighbors:
                break
            current = self.rng.choice(neighbors)
            path.append(current)

        return path


class MargulisGraph:
    def __init__(self, n: int):
        self.n = n
        self.g = Graph()  # using the previously defined Graph class

        for x in range(n):
            for y in range(n):
                v = (x, y)
                neighbors = [
                    ((x + y) % n, y),
                    ((x - y) % n, y),
                    ((x + y + 1) % n, y),
                    ((x - y - 1) % n, y),
                    (x, (y + x) % n),
                    (x, (y - x) % n),
                    (x, (y + x + 1) % n),
                    (x, (y - x - 1) % n)
                ]

                for u in neighbors:
                    self.g.add_edge(v, u, bidirectional=False)  # directed

    def get_graph(self):
        """Return the underlying Graph object."""
        return self.g

    def size(self):
        """Return the number of vertices."""
        return self.n * self.n

    def degree(self):
        """Return the out-degree of each vertex (always 8 for Margulis)."""
        return 8
