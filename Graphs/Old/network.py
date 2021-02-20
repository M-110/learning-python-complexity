import networkx as nx

"""
G = nx.DiGraph()

G.add_node('Alicia')
G.add_node('Sally')
G.add_node('Ella')

print(G.nodes())

G.add_edge('Alicia', 'Sally')
G.add_edge('Alicia', 'Ella')
G.add_edge('Ella', 'Sally')
G.add_edge('Sally', 'Ella')

print(G.edges())

nx.draw_circular(G, node_color='cyan', node_size=2000, with_labels=True)

G.clear()

"""
positions = dict(Albany=(-74, 43),
            Boston=(-71, 42),
            NYC=(-74, 41),
            Philly=(-75, 40))

G2 = nx.Graph()

G2.add_nodes_from(positions)

drive_times = {('Albany', 'Boston'): 3,
              ('Albany', 'NYC'): 1,
              ('Boston', 'NYC'): 4,
              ('NYC', 'Philly'): 2}

G2.add_edges_from(drive_times)

nx.draw(G2, positions, node_color='pink', node_shape='s', node_size=2500, with_labels=True)