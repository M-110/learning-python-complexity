import networkx as nx


def make_odd_regular_graph(n, k):
    if k%2 == 0:
        raise ValueError('k must be odd')
    if n%2:
        raise ValueError('n must be even')
    if k > n:
        raise ValueError('k must be less than n')
        
    graph = nx.Graph()
    nodes = range(n)
    graph.add_nodes_from(nodes)
    
    for x in graph:
        for y in range(n+1):
            y %= n
            if x == y:
                continue
            if len(graph[x]) < 1 and len(graph[y]) < 1:
                graph.add_edge(x, y)
                
    for i in range(n//k, n//k + k):
        for x in graph:
            if len(graph[x]) < k and len(graph[(x+i)%n]) < k:
                graph.add_edge(x, (x+i)%n)
    return graph


graph = make_odd_regular_graph(8, 3)

nx.draw_circular(graph, node_color="pink", node_size=1000, with_labels=True)
    