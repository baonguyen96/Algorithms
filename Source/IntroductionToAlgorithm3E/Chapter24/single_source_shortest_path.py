"""
Dijkstra's algorithm to find the shortest path from a particular node
    to every other nodes in the graph. The graph cannot contain
    negative weight or cycle.

Bellman-Ford's algorithm to find the shortest path from a particular node
    to every other nodes in the graph. The graph can contain
    negative weight or cycle.
"""
import pandas as pd


def get_shortest_paths_using_dijkstra(graph, from_vertex):
    vertices = sorted(graph.nodes())
    distances = pd.DataFrame(columns=vertices)
    distances.loc[from_vertex] = [float('inf') for v in vertices]
    paths = pd.DataFrame(columns=vertices)
    paths.loc[from_vertex] = [None for v in vertices]

    distances[from_vertex] = 0
    paths[from_vertex] = str(from_vertex)

    while len(vertices) > 0:
        start = distances[vertices].idxmin(axis=1)[0]
        neighbors = graph.neighbors(start)

        for vertex in neighbors:
            if vertex not in vertices:
                continue

            d = distances.loc[from_vertex, start] + graph[start][vertex]['weight']

            if distances.loc[from_vertex, vertex] > d:
                distances.loc[from_vertex, vertex] = d
                paths.loc[from_vertex, vertex] = str(start)

        vertices.remove(start)

    return distances, paths


def get_shortest_paths_using_bellman_ford(graph, from_vertex):
    pass


def get_shortest_path(paths, source, destination):
    if paths.loc[0, destination] == destination:
        return str(source)
    else:
        return get_shortest_path(paths, source, paths.loc[0, destination]) + ' -> ' + str(destination)
