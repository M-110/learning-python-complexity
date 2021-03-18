"""Create a graph of 10 nodes with a 34% any node pairs are connected and print a graph"""
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Iterator, List
from complexity.graphs.complete_graph import CompleteGraph

Node = int
Edge = Tuple[Node, Node]


class RandomGraph(CompleteGraph):
    """Graph with randomly connected nodes."""

    def __init__(self, n: int, p: float):
        self.graph: nx.Graph = self.create_graph(n, p)

    def random_pairs(self, nodes: List[Node], p: float) -> Iterator[Edge]:
        """Generate random pairings of nodes."""
        for edge in self.pair_all(nodes):
            if np.random.random() < p:
                yield edge

    def create_graph(self, n: int, p: float) -> nx.Graph:
        """Create a random graph with n nodes, using p as the probability of each node being connected."""
        graph = nx.Graph()
        nodes = tuple(range(n))
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.random_pairs(nodes, p))
        return graph

    @staticmethod
    def log_plot(n: int = 10):
        """Plot the probability it is connected over different probabilities in log space."""
        ps: List[float] = list(np.logspace(-2.5, 0, 11))
        ys: List[float] = [RandomGraph.prob_connected(n, p) for p in ps]
        plt.plot(ys)

    @staticmethod
    def prob_connected(n: int, p: float, iters: int = 10000) -> float:
        """Iterate through a series of random graphs and track what percent of them are fully connected."""
        connected_graphs: List[bool, ...] = [RandomGraph(n, p).is_connected() for i in range(iters)]
        return float(np.mean(connected_graphs))


if __name__ == "__main__":
    rg = RandomGraph(10, .34)
    rg.draw_circular_graph(filename="random_graph.png", save=True)
