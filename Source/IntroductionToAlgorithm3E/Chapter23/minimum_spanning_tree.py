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

    for r_i, row in graph.iterrows():
        if r_i == mst['v'].iloc[0]:
            mst.loc[r_i, 'd'] = 0.0
            mst.loc[r_i, 'known'] = True
            continue

        min_distance = float('inf')
        parent_vertex = None

        for c_i, column in row.items():
            if mst['p'][c_i] == r_i:
                continue

            if graph[r_i][c_i] < min_distance:
                min_distance = graph[r_i][c_i]
                parent_vertex = c_i

        mst.loc[r_i, 'known'] = True
        mst.loc[r_i, 'd'] = min_distance
        mst.loc[r_i, 'p'] = parent_vertex

    return mst


def get_mst_using_kruskal(graph):
    pass
