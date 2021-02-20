import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Iterator, List

Node = int
Edge = Tuple[Node, Node]


class WattsStogatz:
    """Watts Stogatz Graph."""

    def __init__(self, n: int, k: int, p: float):
        graph = self.create_ring_lattice(n, k)

    def create_ring_lattice(n: int, k: int) -> nx.Graph:
        """Create a ring lattice graph."""
        graph = nx.Graph()
        nodes = range(n)
        graph.add_nodes_from(nodes)
        graph.add_edges_from((node, (node + i) % n)
                             for node in range(n)
                             for i in range(k // 2 + 1))
        return graph

    def rewire_nodes(self, p: float):
        """Randomly change edges of each node based on probability p."""
        nodes = set(graph)

        for a, b in graph.edges():
            if p >= random.random():
                possible_nodes = nodes - {a} - set(graph[b])
                new_b = random.choice(list(possible_nodes))
                graph.remove_edge(a, b)
                graph.add_edge(a, new_b)

            graph.add_edge(a, new_b)

    def pair_all(self, nodes: Tuple[Node, ...]) -> Iterator[Edge]:
        """Generates all consecutive pairs of nodes."""
        return ((x, y)
                for i, x in enumerate(nodes)
                for j, y in enumerate(nodes)
                if i > j)




def node_clustering(graph, node):
    neighbors = graph[node]
    k = len(neighbors)
    if k < 2:
        return np.nan
    possible = k * (k - 1) / 2
    exist = sum(1 for v, w in all_pairs(neighbors) if graph.has_edge(v, w))
    return exist / possible


def clustering_coefficient(graph):
    return np.nanmean([node_clustering(graph, node) for node in graph])


def path_lengths(graph):
    length_map = list(nx.shortest_path_length(graph))
    lengths = [length_map[a][1][b] for a, b in all_pairs(graph)]
    return lengths


def characteristic_path_length(graph):
    return np.mean(path_lengths(graph))


def analyze_graph(n, k, p):
    graph = watts_stogatz_graph(n, k, p)
    cpl = characteristic_path_length(graph)
    cc = clustering_coefficient(graph)
    return cpl, cc


def watts_stogatz_experiment(ps, n=1000, k=10, iters=20):
    results = []
    for p in ps:
        graph_results = [analyze_graph(n, k, p) for _ in range(iters)]
        means = np.array(graph_results).mean(axis=0)
        results.append(means)
    return np.array(results)
  
ps = np.logspace(-4, 0, 9)
      
results = watts_stogatz_experiment(ps) 

L, C = np.transpose(results)


L /= L[0]
C /= C[0]

plt.plot(L)
plt.plot(C)

