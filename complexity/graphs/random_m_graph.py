"""Plot the probability of a 7 node graph being connected given different numbers of random edges."""
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from typing import Tuple, List
from complexity.graphs.complete_graph import CompleteGraph

Node = int
Edge = Tuple[Node, Node]


class RandomMGraph(CompleteGraph):
    """Graph with randomly connected nodes."""

    def __init__(self, n: int, m: int):
        self.graph: nx.Graph = self.create_graph(n, m)

    def create_m_edges(self, nodes: List[Node], m: int) -> List[Edge]:
        """Randomly generates m edges from nodes."""
        return random.sample(list(self.pair_all(nodes)), m)

    def create_graph(self, n: int, m: int) -> nx.Graph:
        """Create a random graph with n nodes, and m randomly assigned edges."""
        graph = nx.Graph()
        nodes = tuple(range(n))
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.create_m_edges(nodes, m))
        return graph

    @staticmethod
    def prob_connected(n: int, m: int, iters: int = 10000) -> float:
        """Iterate through a series of random graphs and track what percent of them are fully connected."""
        connected_graphs: List[bool] = [RandomMGraph(n, m).is_connected() for i in range(iters)]
        return float(np.mean(connected_graphs))


if __name__ == "__main__":
    m_probabilities: List[float] = [RandomMGraph.prob_connected(7, m) for m in range(20)]
    
    plt.plot(m_probabilities)
    plt.ylabel("Probability a 7 node graph is complete")
    plt.xlabel("Number of edges")
    plt.title("Probability a 7 node graph is complete vs number of edges")
    plt.savefig("random_m_graph_complete_probability_graph.png")

