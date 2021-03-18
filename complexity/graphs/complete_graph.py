"""Complete network of nodes with a printed circular graph."""
import networkx as nx
from typing import Tuple, Iterator, List, Set
import matplotlib.pyplot as plt

Node = int
Edge = Tuple[Node, Node]


class CompleteGraph:
    """Graph with all nodes connected."""

    def __init__(self, n: int):
        self.graph: nx.Graph = self.create_graph(n)

    def pair_all(self, nodes: Tuple[Node, ...]) -> Iterator[Edge]:
        """Generates all consecutive pairs of nodes."""
        return ((x, y)
                for i, x in enumerate(nodes)
                for j, y in enumerate(nodes)
                if i > j)

    def create_graph(self, n: int) -> nx.Graph:
        """Create a graph with n nodes."""
        graph = nx.Graph()
        nodes = tuple(range(n))
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.pair_all(nodes))
        return graph

    def reachable_nodes(self, starting_node: Node) -> Set[Node]:
        """Get all nodes reachable from starting_node in graph."""
        done = set()
        stack: List[Node, ...] = [starting_node]
        while stack:
            node: Node = stack.pop()
            if node not in done:
                done.add(node)
                stack.extend(self.graph.neighbors(node))
        return done

    def is_connected(self) -> bool:
        """Returns True if all nodes in graph are connected."""
        start: Node = next(iter(self.graph))
        reachable_nodes: List[Node, ...] = list(self.reachable_nodes(start))
        # print(len(reachable_nodes),len(self.graph))
        return len(reachable_nodes) == len(self.graph)

    def draw_circular_graph(self, node_color='pink', node_size=1000, save=False, filename='output'):
        """Draw a circular graph of the current nodes/edges and save as a png file."""
        nx.draw_circular(self.graph, node_color=node_color, node_size=node_size, with_labels=True)
        if save:
            plt.savefig(filename)
            print(f'Saved graph as {filename!r}')


if __name__ == "__main__":
    # Create a graph with 10 nodes and a 34% probability that any two pairs of nodes are connected.
    cg = CompleteGraph(10)
    cg.draw_circular_graph(save=True, filename="complete_graph.png")
