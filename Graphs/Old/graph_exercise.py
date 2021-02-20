"""
1. Write a function called m_pairs that takes a list of nodes and the number 
of edges, m, and returns a random selection of m edges. A simple way to do 
that is to generate a list of all possible edges and use random.sample.

2. Write a function called make_m_graph that takes n and m and returns a 
random graph with n nodes and m edges.

3. Make a version of prob_connected that uses make_m_graph instead of 
make_random_graph.

4. Compute the probability of connectivity for a range of values of m.
"""

import networkx as nx
import random
import numpy as np
import matplotlib.pyplot as plt


def create_graph(n):
    graph = nx.Graph()
    graph.add_nodes_from(range(n))
    return graph


def all_possible_edges(nodes):
    return ((a, b) 
            for i, a in enumerate(nodes)
            for j, b in enumerate(nodes)
            if i > j)


complete_graph = create_graph(10)


def m_pairs(nodes, m):
    return random.sample(list(all_possible_edges(nodes)), m)


def make_m_graph(n, m):
    graph = create_graph(n)
    graph.add_edges_from(m_pairs(range(n), m))
    return graph


def is_connected(g):
    start = next(iter(g))
    reachable = reachable_nodes(g, start)
    return len(reachable) == len(g)
    

def prob_connected(n, m, iters=1000):
    tf = [is_connected(make_m_graph(n, m))
         for i in range(iters)]
    return np.mean(tf)

# nx.draw_circular(make_m_graph(10, 15), node_color="pink", node_size=1000, with_labels=True)

x = list(range(8,25))
y = [prob_connected(10, i) for i in x]

plt.plot(x,y)