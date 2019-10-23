import pandas as pd

import IntroductionToAlgorithm3E.Chapter23.minimum_spanning_tree as mst
from Test.unit_test_template import UnitTestTemplate


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

        mst_data = [
            ['v1', True, 0.0, None],
            ['v2', True, 2.0, 'v1'],
            ['v3', True, 2.0, 'v4'],
            ['v4', True, 1.0, 'v1'],
            ['v5', True, 6.0, 'v7'],
            ['v6', True, 1.0, 'v7'],
            ['v7', True, 4.0, 'v4']
        ]
        mst_df = pd.DataFrame(mst_data, columns=['v', 'known', 'd', 'p'], index=vertices)

        return graph, mst_df

    def test_get_mst_using_prim(self):
        graph, expected_mst = MinimumSpanningTreeTest.get_test_graph()
        actual_mst = mst.get_mst_using_prim(graph)
        # print(actual_mst)
        self.assertTrue(expected_mst.equals(actual_mst))

    def test_get_mst_using_kruskal(self):
        graph, expected_mst = MinimumSpanningTreeTest.get_test_graph()
        actual_mst = mst.get_mst_using_kruskal(graph)
        # print(actual_mst)
        self.assertEqual(expected_mst, actual_mst)
