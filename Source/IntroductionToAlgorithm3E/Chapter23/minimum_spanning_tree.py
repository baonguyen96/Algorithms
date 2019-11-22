"""
Problem 23.2-2

Suppose that we represent the graph G(V,E) as an adjacency matrix.
    Give a simple implementation of Prim’s algorithm for this case
    that runs in O(V^2) time.
"""
from heapq import heappush, heappop

import pandas as pd
from disjoint_set import DisjointSet


def get_mst_using_prim(graph):
    vertices = graph.columns.values.tolist()
    mst = pd.DataFrame(columns=['v', 'known', 'd', 'p'])

    for vertex in vertices:
        mst.loc[vertex] = [vertex, False, float('inf'), None]

    for from_vertex, row in graph.iterrows():
        if from_vertex == mst['v'].iloc[0]:
            mst.loc[from_vertex, 'd'] = 0.0
            mst.loc[from_vertex, 'known'] = True
            continue

        for to_vertex, column in row.items():
            if mst.loc[to_vertex, 'p'] == from_vertex:
                continue

            if graph.loc[to_vertex, from_vertex] < mst.loc[from_vertex, 'd']:
                mst.loc[from_vertex, 'd'] = graph.loc[to_vertex, from_vertex]
                mst.loc[from_vertex, 'p'] = to_vertex

        mst.loc[from_vertex, 'known'] = True

    edges = []

    for vertex, row in mst.iterrows():
        if mst.loc[vertex, 'p'] is not None:
            edges += [(mst.loc[vertex, 'p'], mst.loc[vertex, 'v'])]

    return edges


def get_mst_using_kruskal(graph):
    p_queue = []
    vertex_count = graph.shape[1]
    known_vertices = DisjointSet()
    mst = []

    for from_vertex_index in range(vertex_count):
        for to_vertex_index in range(from_vertex_index + 1, vertex_count):
            weight = graph.iloc[from_vertex_index, to_vertex_index]
            from_vertex_name = graph.columns[from_vertex_index]
            to_vertex_name = graph.columns[to_vertex_index]
            heappush(p_queue, (weight, from_vertex_name, to_vertex_name))

    while len(p_queue) > 0:
        min_edge = heappop(p_queue)
        from_vertex = min_edge[1]
        to_vertex = min_edge[2]

        from_set = known_vertices.find(from_vertex)
        to_set = known_vertices.find(to_vertex)

        if from_set != to_set:
            mst += [(from_vertex, to_vertex)]
            known_vertices.union(from_set, to_set)

    return mst
