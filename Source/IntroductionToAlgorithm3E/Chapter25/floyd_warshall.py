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

    for mid in vertices:
        for src in vertices:
            for dst in vertices:
                new_distance = distances.loc[src, mid] + distances.loc[mid, dst]
                if distances.loc[src, dst] > new_distance:
                    distances.loc[src, dst] = new_distance
                    paths.loc[src, dst] = mid

    return distances, paths


def get_shortest_path_from_to(paths, source, destination):
    start = str(source)
    path = start
    next_hop = paths.loc[source, destination]

    while next_hop != start:
        path += ' -> ' + str(next_hop)
        start = next_hop
        next_hop = paths.loc[start, destination]

    path += ' -> ' + str(destination)
    return path


def has_negative_weight_cycle(graph):
    distances, paths = get_all_pair_shortest_paths_fw(graph)
    vertices = graph.nodes()

    for vertex in vertices:
        if distances.loc[vertex, vertex] < 0:
            return True

    return False
