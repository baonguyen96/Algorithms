"""
Problem 23.2-2

Suppose that we represent the graph G(V,E) as an adjacency matrix.
    Give a simple implementation of Prim’s algorithm for this case
    that runs in O(V^2) time.
"""

import pandas as pd


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

    return mst, edges


def get_mst_using_kruskal(graph):
    pass
