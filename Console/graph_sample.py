import matplotlib.pyplot as plt
import networkx as nx
import pylab


def get_simple_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([('1', '2')], weight=3)
    graph.add_edges_from([('1', '3')], weight=8)
    graph.add_edges_from([('2', '3')], weight=3)
    graph.add_edges_from([('3', '4')], weight=1)
    print('Vertices')
    print(graph.nodes())
    print('Edges')
    print(graph.edges())

    print(graph['1']['2']['weight'])

    for edge in graph.edges():
        print(edge)
        print(graph[edge]['weight'])

    nx.draw(graph, with_labels=True)
    plt.show()


def draw_simple_graph():
    graph = nx.petersen_graph()
    plt.subplot(121)

    nx.draw(graph, with_labels=True, font_weight='bold')
    plt.subplot(122)

    nx.draw_shell(graph, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()


def draw_weighted_directed_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([('1', '2')], weight=3)
    graph.add_edges_from([('1', '3')], weight=8)
    graph.add_edges_from([('1', '5')], weight=-4)
    graph.add_edges_from([('2', '4')], weight=1)
    graph.add_edges_from([('2', '5')], weight=7)
    graph.add_edges_from([('3', '2')], weight=4)
    graph.add_edges_from([('4', '1')], weight=2)
    graph.add_edges_from([('4', '3')], weight=-5)
    graph.add_edges_from([('5', '6')], weight=6)

    val_map = {'A': 1.0,
               'D': 0.5714285714285714,
               'H': 0.0}

    values = [val_map.get(node, 0.45) for node in graph.nodes()]
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in graph.edges(data=True)])
    red_edges = [('1', '3'), ('1', '5')]
    edge_colors = ['black' if edge not in red_edges else 'red' for edge in graph.edges()]

    pos = nx.spring_layout(graph)

    node_labels = {node:node for node in graph.nodes()}
    nx.draw_networkx_labels(graph, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
    nx.draw(graph, pos, node_color=values, node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
    pylab.show()


get_simple_graph()
# draw_weighted_directed_graph()
