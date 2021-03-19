"""Run the Watts Strogatz experiment to demonstrate the small world
phenomenon.py

The plot shows that there is a large range of probabilities for which the
graph demonstrates high clustering and low path lengths which are
characteristics of the small world phenomenon.
"""
import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


class WattsStrogatz:
    """Watts Strogatz Graph."""

    def __init__(self, n: int, k: int, p: float):
        self.graph = self.create_ring_lattice(n, k)
        self.rewire_nodes(p)

    def create_ring_lattice(self, n: int, k: int):
        """Create a ring lattice graph."""
        graph = nx.Graph()
        nodes = range(n)
        graph.add_nodes_from(nodes)
        graph.add_edges_from((node, (node + i) % n)
                             for node in range(n)
                             for i in range(k // 2 + 1))
        return graph

    def rewire_nodes(self, p: float):
        """Randomly rewire nodes based on random probability p."""
        nodes = set(self.graph)
        for a, b in self.graph.edges():
            if p >= random.random():
                possible_nodes = nodes - {a} - set(self.graph[b])
                new_b = random.choice(list(possible_nodes))
                self.graph.remove_edge(a, b)
                self.graph.add_edge(a, new_b)

    def all_pairs(self, nodes):
        """Get all node pairs in the graph."""
        return ((x, y) for i, x in enumerate(nodes) for j, y in enumerate(nodes)
                if i > j)

    def node_clustering(self, node):
        """Calculate the clustering around a specific node."""
        neighbors = self.graph[node]
        k = len(neighbors)
        if k < 2:
            return np.nan
        possible = k * (k - 1) / 2
        exist = sum(1 for v, w in self.all_pairs(neighbors) if self.graph.has_edge(v, w))
        return exist / possible

    def clustering_coefficient(self):
        """Calculate the clustering coefficient of the entire graph."""
        return np.nanmean([self.node_clustering(node) for node in self.graph])

    def path_lengths(self):
        """Calculate all path lengths on the graph."""
        length_map = list(nx.shortest_path_length(self.graph))
        lengths = [length_map[a][1][b]
                   for a, b in self.all_pairs(self.graph)]
        return lengths

    def characteristic_path_length(self):
        """Calculate the average path length on the graph."""
        return np.mean(self.path_lengths())


def analyze_graph(n: int, k: int, p: float):
    """Create a graph of n nodes with k edges and p probability of 
    rewiring and return the characteristic path length and
    clustering coefficient."""
    graph = WattsStrogatz(n, k, p)
    cpl = graph.characteristic_path_length()
    cc = graph.clustering_coefficient()
    return cpl, cc


def watts_strogatz_experiment(ps, n=1000, k=10, iters=20):
    """Run the Watts Strogatz experiment using probabilities from 
    ps, with a graph of n nodes and k edges. Iterate iters times.
    
    Graph and save the results as 'watts_strogatz.png'.
    """
    results = []
    for p in ps:
        graph_results = [analyze_graph(n, k, p) for _ in range(iters)]
        means = np.array(graph_results).mean(axis=0)
        results.append(means)
    results_array = np.array(results)
    L, C = np.transpose(results_array)
    L /= L[0]
    C /= C[0]
    plt.title("Normalized clustering coefficient and path length vs rewiring probability")
    plt.xlabel("Rewiring probability")
    plt.ylabel("Clustering coefficient")
    plt.plot(C, '*-', label="Normalized Clustering Coefficient")
    plt.plot(L, 'o-', label="Normalized Path Length")
    plt.xscale = 'log'
    plt.savefig("watts_strogatz.png")
    print("Saved figure as 'watts_strogatz.png'")


if __name__ == '__main__':
    ps = np.logspace(-4, 0, 9)
    watts_strogatz_experiment(ps)
