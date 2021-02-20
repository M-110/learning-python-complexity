from collections import deque
import networkx as nx


def create_graph(n):
    graph = nx.Graph()
    nodes = range(n)
    graph.add_nodes_from(nodes)
    return graph
                         

def shortest_path_dijkstra(graph, source):
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





graph = create_graph(5)

shortest_path_dijkstra(graph, 0)

nx.draw_circular(graph, node_color="pink", node_size=1000, with_labels=True)
