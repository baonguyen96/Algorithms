"""
Problem 25-1 Transitive closure of a dynamic graph

Suppose that we wish to maintain the transitive closure of a directed graph G(V,E)
    as we insert edges into E. That is, after each edge has been inserted,
    we want to update the transitive closure of the edges inserted so far.
    Assume that the graph G has no edges initially and that we represent
    the transitive closure as a boolean matrix.
    Describe an efficient algorithm for updating the transitive closure as edges are
    inserted into the graph. For any sequence of n insertions, your algorithm should
    run in total time O(v^3), where ti is the time to update the transitive
    closure upon inserting the i th edge.
"""
import pandas as pd

'''
This seem to run in O(v^2), even better than required
'''


def get_transitive_closure(vertices, edges):
    tc = pd.DataFrame(columns=vertices)

    # vertex can reach itself and nothing else by default
    for vertex in vertices:
        tc.loc[vertex] = [0 for i in range(len(vertices))]
        tc.loc[vertex, vertex] = 1

    for edge in edges:
        from_vertex = edge[0]
        to_vertex = edge[1]

        # 'from' reaches 'to'
        tc.loc[from_vertex, to_vertex] = 1

        # anything that can reach 'from' can also reach 'to'
        for vertex in vertices:
            if tc.loc[vertex, from_vertex] == 1:
                tc.loc[vertex, to_vertex] = 1

        # anything that 'to' can reach, 'from' can also reach
        for vertex in vertices:
            if tc.loc[to_vertex, vertex] == 1:
                tc.loc[from_vertex, vertex] = 1

    return tc
