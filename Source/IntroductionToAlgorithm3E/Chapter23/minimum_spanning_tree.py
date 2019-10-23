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

        for c_i, column in row.items():
            if mst.loc[c_i, 'p'] == r_i:
                continue

            if graph.loc[c_i, r_i] < mst.loc[r_i, 'd']:
                mst.loc[r_i, 'd'] = graph.loc[c_i, r_i]
                mst.loc[r_i, 'p'] = c_i

        mst.loc[r_i, 'known'] = True

    return mst


def get_mst_using_kruskal(graph):
    pass
