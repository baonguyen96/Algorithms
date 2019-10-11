"""
Problem 25.2-7

Floyd-Warshall algorithm with modification to capture paths along side values.
Assume no negative cycle.
"""

import pandas as pd


def get_all_pair_shortest_paths_fw(graph):
    vertices = sorted(graph.nodes())
    d = [[float('inf') for i in range(len(vertices))] for j in range(len(vertices))]
    p = [[None for i in range(len(vertices))] for j in range(len(vertices))]
    distances = pd.DataFrame(d, columns=vertices, index=vertices)
    paths = pd.DataFrame(p, columns=vertices, index=vertices)

    for vertex in vertices:
        distances[vertex][vertex] = 0
        paths[vertex][vertex] = vertex

    for edge in list(graph.edges()):
        from_vertex = edge[0]
        to_vertex = edge[1]
        distances.loc[from_vertex, to_vertex] = graph[from_vertex][to_vertex]['weight']
        paths.loc[from_vertex, to_vertex] = from_vertex

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if distances.loc[i, j] > distances.loc[i, k] + distances.loc[k, j]:
                    distances.loc[i, j] = distances.loc[i, k] + distances.loc[k, j]
                    paths.loc[i, j] = k

    return distances, paths


def get_shortest_path_from_to(paths, i, j):
    start = str(i)
    path = start
    next_hop = paths.loc[i, j]

    while next_hop != start:
        path += ' -> ' + str(next_hop)
        start = next_hop
        next_hop = paths.loc[start, j]

    path += ' -> ' + str(j)
    return path


def has_negative_weight_cycle(graph):
    distances, paths = get_all_pair_shortest_paths_fw(graph)
    vertices = graph.nodes()

    for vertex in vertices:
        if distances.loc[vertex, vertex] < 0:
            return True

    return False

