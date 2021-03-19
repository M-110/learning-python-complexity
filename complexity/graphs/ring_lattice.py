"""Create and save a ring lattice graph with 10 nodes and 3 degrees."""

from typing import Tuple, List
import networkx as nx
import matplotlib.pyplot as plt


class RingLattice:
    def __init__(self, n: int, k: int):
        self.graph = self.create_ring_lattice(n, k)

    def create_ring_lattice(self, n: int, k: int) -> nx.Graph:
        """Create a ring lattice with n nodes and k degrees."""
        graph = nx.Graph()
        nodes = tuple(range(n))
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.adjacent_pairs(nodes, k))
        return graph

    def adjacent_pairs(self, nodes: Tuple[int], k: int) -> List[Tuple[int, int]]:
        """Returns a list of pairs of nodes which are adjacent
        by k degrees."""
        n = len(nodes)
        return [(u, nodes[j % n])
                for i, u in enumerate(nodes)
                for j in range(i + 1, i + 1 + k // 2)]

    def print_graph(self, filename='', save=False):
        """Print and optionally save the graph."""
        nx.draw_circular(self.graph, node_color='pink', node_size=1000, with_labels=True)
        if save:
            plt.savefig(filename)
            print(f'Saved graph as {filename!r}')
        else:
            plt.show()


if __name__ == '__main__':
    ring_lattice = RingLattice(10, 4)
    ring_lattice.print_graph('ring_lattice.png', save=True)
