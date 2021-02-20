import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Iterator

Node = int

class Graph:
    """Node-based graph."""
    def __init__(self, n: int):
        self.graph: nx.Graph = self.create_graph(n)

    def pair_all(nodes: Tuple[Node, ...]) -> Iterator[Tuple[Node, Node]]:
        """Generates all consecutive pairs of nodes."""
        return ((x, y) for i, x in enumerate(nodes)
               for j, y in enumerate(nodes)
               if i > j)

    def create_graph(n: int) -> nx.Graph:
        """Create a graph with n nodes"""
        graph = nx.Graph()
        nodes = range(length)
        graph.add_nodes_from(nodes)
        graph.add_edges_from(self.pair_all(nodes))
        return graph

    def reachable_nodes(start: int) -> 





def pair_all(nodes):
    """Generator"""
    for i, x in enumerate(nodes):
        for j, y in enumerate(nodes):
            if i > j:
                yield u, v

def pair_all(nodes):
    return ((x, y) for i, x in enumerate(nodes) for j, y in enumerate(nodes) 
            if i>j)

def create_complete_graph(n):
    g = nx.Graph()
    nodes = range(n)
    g.add_nodes_from(nodes)
    g.add_edges_from(pair_all(nodes))
    return g

complete_graph = create_complete_graph(10)



def reachable_nodes(g, start):
    done = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in done:
            done.add(node)
            stack.extend(g.neighbors(node))
    return done

def is_connected(g):
    start = next(iter(g))
    reachable = reachable_nodes(g, start)
    return len(reachable) == len(g)

print(reachable_nodes(complete_graph, 0))

print(f'Is connected? {is_connected(complete_graph)}')

def random_pairs(nodes, probability):
    for edge in pair_all(nodes):
        if np.random.random() < probability:
            yield edge
            
def make_random_graph(n, p):
    g = nx.Graph()
    nodes = range(n)
    g.add_nodes_from(nodes)
    g.add_edges_from(random_pairs(nodes, p))
    return g

random_graph = make_random_graph(10, 0.3)

# nx.draw_circular(random_graph, node_color="pink", node_size=1000, with_labels=True)

def prob_connected(n, p, iters=100):
    tf = [is_connected(make_random_graph(n, p))
          for i in range(iters)]
    return np.mean(tf)

print(prob_connected(10, .23, iters=10000))

n=10
ps = np.logspace(-2.5, 0, 11)
ys = [prob_connected(n, p) for p in ps]

plt.plot(ys)



