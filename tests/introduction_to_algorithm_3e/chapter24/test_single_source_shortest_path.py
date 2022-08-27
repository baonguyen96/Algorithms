from unittest import skip

import networkx as nx
import pandas as pd

import src.introduction_to_algorithm_3e.chapter24.single_source_shortest_path as sssp
from tests.unit_test_template import UnitTestTemplate


class SingleSourceShortestPathTest(UnitTestTemplate):
    @staticmethod
    def get_test_params():
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

        vertices = ['a', 'b', 'c', 'd', 'e', 'z']
        expected_distances = pd.DataFrame(columns=vertices)
        expected_distances.loc['a'] = [0, 3, 2, 8, 10, 13]
        expected_paths = pd.DataFrame(columns=vertices)
        expected_paths.loc['a'] = ['a', 'c', 'a', 'b', 'd', 'e']

        return graph, expected_distances, expected_paths

    def test_get_shortest_paths_using_dijkstra(self):
        graph, expected_distances, expected_paths = SingleSourceShortestPathTest.get_test_params()
        actual_distances, actual_paths = sssp.get_shortest_paths_using_dijkstra(graph, 'a')

        self.assertTrue(expected_distances.astype(float).equals(actual_distances.astype(float)))
        self.assertTrue(expected_paths.astype(str).equals(actual_paths.astype(str)))

    @skip('Need to check')
    def test_get_shortest_paths_using_bellman_ford(self):
        graph, expected_distances, expected_paths = SingleSourceShortestPathTest.get_test_params()
        actual_distances, actual_paths = sssp.get_shortest_paths_using_bellman_ford(graph, 'a')

        self.assertTrue(expected_distances.astype(float).equals(actual_distances.astype(float)))
        self.assertTrue(expected_paths.astype(str).equals(actual_paths.astype(str)))

    def test_get_shortest_path_from_to(self):
        graph, distances, paths = SingleSourceShortestPathTest.get_test_params()

        expected = 'a -> c'
        actual = sssp.get_shortest_path(paths, 'a', 'c')
        self.assertEqual(expected, actual)

        expected = 'a -> c -> b -> d'
        actual = sssp.get_shortest_path(paths, 'a', 'd')
        self.assertEqual(expected, actual)

        expected = 'a -> c -> b -> d -> e -> z'
        actual = sssp.get_shortest_path(paths, 'a', 'z')
        self.assertEqual(expected, actual)
