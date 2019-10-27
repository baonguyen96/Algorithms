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

        prim_data = [
            ['v1', True, 0.0, None],
            ['v2', True, 2.0, 'v1'],
            ['v3', True, 2.0, 'v4'],
            ['v4', True, 1.0, 'v1'],
            ['v5', True, 6.0, 'v7'],
            ['v6', True, 1.0, 'v7'],
            ['v7', True, 4.0, 'v4']
        ]
        mst_prim = pd.DataFrame(prim_data, columns=['v', 'known', 'd', 'p'], index=vertices)

        kruskal_data = [
            ['v1', True, 0.0, None],
            ['v2', True, 2.0, 'v1'],
            ['v3', True, 2.0, 'v4'],
            ['v4', True, 1.0, 'v1'],
            ['v5', True, 6.0, 'v7'],
            ['v6', True, 1.0, 'v7'],
            ['v7', True, 4.0, 'v4']
        ]
        mst_kruskal = pd.DataFrame(prim_data, columns=['v', 'known', 'd', 'p'], index=vertices)

        edges = [('v1', 'v2'),
                 ('v1', 'v4'),
                 ('v4', 'v3'),
                 ('v4', 'v7'),
                 ('v7', 'v5'),
                 ('v7', 'v6')]

        return graph, mst_prim, mst_kruskal, edges

    def test_get_mst_using_prim(self):
        graph, mst_prim, mst_kruskal, edges = MinimumSpanningTreeTest.get_test_graph()
        actual_mst, actual_edges = mst.get_mst_using_prim(graph)
        print(actual_mst)
        print(actual_edges)
        self.assertTrue(mst_prim.equals(actual_mst))
        self.assertEqual(set(edges), set(actual_edges))

    def test_get_mst_using_kruskal(self):
        graph, mst_prim, mst_kruskal, edges = MinimumSpanningTreeTest.get_test_graph()
        actual_mst, actual_edges = mst.get_mst_using_kruskal(graph)
        print(actual_mst)
        print(actual_edges)
        self.assertTrue(mst_kruskal.equals(actual_mst))
        self.assertEqual(set(edges), set(actual_edges))
