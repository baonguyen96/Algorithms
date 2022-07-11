import pandas as pd

import src.introduction_to_algorithm_3e.chapter23.minimum_spanning_tree as mst
from tests.unit_test_template import UnitTestTemplate
from utilities.utility import are_edges_equal


class MinimumSpanningTreeTest(UnitTestTemplate):
    @staticmethod
    def get_test_graph():
        graph_data = [
            [float('inf'), 2, 4, 1, float('inf'), float('inf'), float('inf')],
            [2, float('inf'), float('inf'), 3, 10, float('inf'), float('inf')],
            [4, float('inf'), float('inf'), 2, float('inf'), 5, float('inf')],
            [1, 3, 2, float('inf'), 7, 8, 4],
            [float('inf'), 10, float('inf'), 7, float('inf'), float('inf'), 6],
            [float('inf'), float('inf'), 5, 8, float('inf'), float('inf'), 1],
            [float('inf'), float('inf'), float('inf'), 4, 6, 1, float('inf')]
        ]

        vertices = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7']
        graph = pd.DataFrame(graph_data, columns=vertices, index=vertices)

        edges = [('v1', 'v2'),
                 ('v1', 'v4'),
                 ('v4', 'v3'),
                 ('v4', 'v7'),
                 ('v7', 'v5'),
                 ('v7', 'v6')]

        return graph, edges

    def test_get_mst_using_prim(self):
        graph, edges = MinimumSpanningTreeTest.get_test_graph()
        actual_edges = mst.get_mst_using_prim(graph)
        self.assertTrue(are_edges_equal(edges, actual_edges))

    def test_get_mst_using_kruskal(self):
        graph, edges = MinimumSpanningTreeTest.get_test_graph()
        actual_edges = mst.get_mst_using_kruskal(graph)
        self.assertTrue(are_edges_equal(edges, actual_edges))

