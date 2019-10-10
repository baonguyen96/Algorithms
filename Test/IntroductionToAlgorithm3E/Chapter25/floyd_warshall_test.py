import networkx as nx
import pandas as pd

import IntroductionToAlgorithm3E.Chapter25.floyd_warshall as fw
from Test.unit_test_template import UnitTestTemplate


class FloydWarshallTest(UnitTestTemplate):
    def test_get_all_pair_shortest_paths_fw(self):
        graph = nx.DiGraph()
        graph.add_edges_from([('1', '3')], weight=-2)
        graph.add_edges_from([('3', '4')], weight=2)
        graph.add_edges_from([('4', '2')], weight=-1)
        graph.add_edges_from([('2', '1')], weight=4)
        graph.add_edges_from([('2', '3')], weight=3)

        vertices = ['1', '2', '3', '4']
        distances = [[0, -1, -2, 0],
                     [4, 0, 2, 4],
                     [5, 1, 0, 2],
                     [3, -1, 1, 0]]
        paths = [['1', '4', '1', '3'],
                 ['2', '2', '1', '3'],
                 ['4', '4', '3', '3'],
                 ['2', '4', '2', '4']]
        expected_distances = pd.DataFrame(distances, columns=vertices, index=vertices)
        expected_paths = pd.DataFrame(paths, columns=vertices, index=vertices)
        actual_distances, actual_paths = fw.get_all_pair_shortest_paths_fw(graph)
        self.assertTrue(expected_distances.astype(float).equals(actual_distances.astype(float)))
        self.assertTrue(expected_paths.astype(str).equals(actual_paths.astype(str)))

    def test_get_shortest_path_from_to(self):
        vertices = ['1', '2', '3', '4']
        p = [['1', '4', '1', '3'],
             ['2', '2', '1', '3'],
             ['4', '4', '3', '3'],
             ['2', '4', '2', '4']]
        paths = pd.DataFrame(p, columns=vertices, index=vertices)

        expected = '1 -> 3'
        actual = fw.get_shortest_path_from_to(paths, '1', '3')
        self.assertEqual(expected, actual)

        expected = '2 -> 1 -> 3'
        actual = fw.get_shortest_path_from_to(paths, '2', '3')
        self.assertEqual(expected, actual)

        expected = '4 -> 2 -> 1 -> 3'
        actual = fw.get_shortest_path_from_to(paths, '4', '3')
        self.assertEqual(expected, actual)
