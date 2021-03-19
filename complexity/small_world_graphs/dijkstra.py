"""Creates a ring lattice and uses the Dijkstra algorithm to find the shortest
path from node 0 to each of the 10 nodes."""
from collections import deque
import networkx as nx
from typing import Dict
from complexity.graphs.ring_lattice import RingLattice


def shortest_path_dijkstra(graph: nx.Graph, source: int) -> Dict[int, int]:
    """Finds the shortest distance from the source node to each
    node in the graph."""
    dist = {source: 0}
    queue = deque([source])
    while queue:
        node = queue.popleft()
        new_dist = dist[node] + 1

        neighbors = set(graph[node]) - set(dist.keys())
        for n in neighbors:
            dist[n] = new_dist
        queue.extend(neighbors)
    return dist


if __name__ == "__main__":
    graph = RingLattice(10, 4)
    result = shortest_path_dijkstra(graph.graph, 0)
    print(result)
