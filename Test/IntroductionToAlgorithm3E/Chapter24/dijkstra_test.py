import networkx as nx
import pandas as pd

import IntroductionToAlgorithm3E.Chapter24.dijkstra as ds
from Test.unit_test_template import UnitTestTemplate


class DijkstraTest(UnitTestTemplate):
    def test_get_shortest_path(self):
        graph = nx.Graph()
        graph.add_edges_from([('a', 'b')], weight=4)
        graph.add_edges_from([('a', 'c')], weight=2)
        graph.add_edges_from([('b', 'c')], weight=1)
        graph.add_edges_from([('b', 'd')], weight=5)
        graph.add_edges_from([('c', 'd')], weight=8)
        graph.add_edges_from([('c', 'e')], weight=10)
        graph.add_edges_from([('d', 'e')], weight=2)
        graph.add_edges_from([('d', 'z')], weight=6)
        graph.add_edges_from([('e', 'z')], weight=3)

        actual_distances, actual_paths = ds.get_shortest_paths_from_ds(graph, 'a')
        vertices = ['a', 'b', 'c', 'd', 'e', 'z']
        expected_distances = pd.DataFrame(columns=vertices)
        expected_distances.loc[0] = [0, 3, 2, 8, 10, 13]
        expected_paths = pd.DataFrame(columns=vertices)
        expected_paths.loc[0] = ['a', 'c', 'a', 'b', 'd', 'e']
        self.assertTrue(expected_distances.astype(float).equals(actual_distances.astype(float)))
        self.assertTrue(expected_paths.astype(str).equals(actual_paths.astype(str)))

    def test_get_shortest_path_from_to(self):
        paths = pd.DataFrame(columns=['a', 'b', 'c', 'd', 'e', 'z'])
        paths.loc[0] = ['a', 'c', 'a', 'b', 'd', 'e']

        expected = 'a -> c'
        actual = ds.get_shortest_path_from_to(paths, 'a', 'c')
        self.assertEqual(expected, actual)

        expected = 'a -> c -> b -> d'
        actual = ds.get_shortest_path_from_to(paths, 'a', 'd')
        self.assertEqual(expected, actual)

        expected = 'a -> c -> b -> d -> e -> z'
        actual = ds.get_shortest_path_from_to(paths, 'a', 'z')
        self.assertEqual(expected, actual)
