import matplotlib.pyplot as plt
import networkx as nx

graph = nx.DiGraph(directed=True)
graph.add_weighted_edges_from([(1, 2, 3),
                               (1, 3, 8),
                               (1, 5, -4),
                               (2, 5, 7),
                               (2, 4, 1),
                               (3, 2, 4),
                               (4, 3, -5),
                               (4, 1, 2),
                               (5, 4, 6)])
options = {
    'node_color': 'blue',
    'node_size': 100,
    'width': 3,
    'arrowstyle': '-|>',
    'arrowsize': 12,
}
nx.draw_networkx(graph, arrows=True, **options)
plt.show()
