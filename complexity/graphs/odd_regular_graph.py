"""Creates a regular graph with 12 nodes and 3 neighbors per node."""
import networkx as nx
import matplotlib.pyplot as plt


class OddRegularGraph:
    """Creates a regular graph with k edges.

    Args:
        n: number of nodes, must be even
        k: number of neighbors, must be odd and less than n
    """

    def __init__(self, n: int, k: int):
        if k % 2 == 0:
            raise ValueError('k must be odd')
        if n % 2:
            raise ValueError('n must be even')
        if k > n:
            raise ValueError('k must be less than n')

        self.graph: nx.Graph = self.create_graph(n, k)

        self.generate_edges(n, k)

    def create_graph(self, n: int, k: int) -> nx.Graph:
        """Generate the graph."""
        graph = nx.Graph()
        nodes = range(n)
        graph.add_nodes_from(nodes)
        return graph

    def generate_edges(self, n: int, k: int):
        """Generates k edges for n nodes."""
        # First pass
        for x in self.graph:
            for y in range(n + 1):
                y %= n
                if x == y:
                    continue
                if len(self.graph[x]) < 1 and len(self.graph[y]) < 1:
                    self.graph.add_edge(x, y)

        # Second pass
        for i in range(n // k, n // k + k):
            for x in self.graph:
                if len(self.graph[x]) < k and len(self.graph[(x + i) % n]) < k:
                    self.graph.add_edge(x, (x + i) % n)

    def draw_circular_graph(self):
        """Draw and save the graph."""
        nx.draw_circular(self.graph, node_color="pink", node_size=1000, with_labels=True)
        plt.savefig("odd_regular_graph.png")


if __name__ == "__main__":
    org = OddRegularGraph(12, 3)
    org.draw_circular_graph()
