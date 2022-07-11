import pandas

from src.introduction_to_algorithm_3e.chapter25.transitive_closure import get_transitive_closure
from tests.unit_test_template import UnitTestTemplate


class TransitiveClosureTest(UnitTestTemplate):
    def test_get_transitive_closure(self):
        vertices = [1, 2, 3, 4]
        edges = [(4, 1), (2, 4), (2, 3), (3, 2), (4, 3)]
        expected_data = [[1, 0, 0, 0],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1],
                         [1, 1, 1, 1]]
        expected = pandas.DataFrame(data=expected_data, columns=vertices, index=vertices)
        actual = get_transitive_closure(vertices, edges)
        self.assertTrue(expected.astype('int').equals(actual.astype('int')))

    def test_get_transitive_closure_2(self):
        vertices = [1, 2, 3, 4, 5]
        edges = [(4, 1), (1, 2), (3, 2), (2, 4), (3, 4), (4, 5)]
        expected_data = [[1, 1, 0, 1, 1],
                         [1, 1, 0, 1, 1],
                         [1, 1, 1, 1, 1],
                         [1, 1, 0, 1, 1],
                         [0, 0, 0, 0, 1]]
        expected = pandas.DataFrame(data=expected_data, columns=vertices, index=vertices)
        actual = get_transitive_closure(vertices, edges)
        self.assertTrue(expected.astype('int').equals(actual.astype('int')))
