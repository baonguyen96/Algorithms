"""
Dijkstra's algorithm to find the shortest path from a particular node
    to every other nodes in the graph. The graph cannot contain
    negative weight or cycle.
"""
import pandas as pd


def get_shortest_paths_from_ds(graph, from_vertex):
    vertices = sorted(graph.nodes())
    distances = pd.DataFrame(columns=vertices)
    distances.loc[0] = [float('inf') for v in vertices]
    paths = pd.DataFrame(columns=vertices)
    paths.loc[0] = [None for v in vertices]

    distances[from_vertex] = 0
    paths[from_vertex] = str(from_vertex)

    while len(vertices) > 0:
        start = distances[vertices].idxmin(axis=1)[0]
        neighbors = graph.neighbors(start)

        for vertex in neighbors:
            if vertex not in vertices:
                continue

            d = distances.loc[0, start] + graph[start][vertex]['weight']

            if distances.loc[0, vertex] > d:
                distances.loc[0, vertex] = d
                paths.loc[0, vertex] = str(start)

        vertices.remove(start)

    return distances, paths


def get_shortest_path_from_to(paths, i, j):
    if paths.loc[0, j] == j:
        return str(i)
    else:
        return get_shortest_path_from_to(paths, i, paths.loc[0, j]) + ' -> ' + str(j)
