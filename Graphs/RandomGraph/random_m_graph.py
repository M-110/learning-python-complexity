"""Plot the probability of a 7 node graph being connected given different numbers of rando medges."""
import networkx as nx
import numpy as np
import random
import matplotlib.pyplot as plt
from typing import Tuple, Iterator, List
from complete_graph import CompleteGraph

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
        nodes = range(n)
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.create_m_edges(nodes, m))
        return graph

    @staticmethod
    def prob_connected(n: int, m: int, iters: int = 10000) -> float:
        """Iterate through a series of random graphs and track what percent of them are fully connected."""
        connected_graphs: List[bool] = [RandomMGraph(n, m).is_connected() for i in range(iters)]
        return np.mean(connected_graphs)

if __name__ == "__main__":
    m_probs: List[float] = [RandomMGraph.prob_connected(7, m) for m in range(20)]
    
    plt.plot(m_probs)
    
    # rg = RandomMGraph(10, 5)
    # rg.draw_circular_graph()
