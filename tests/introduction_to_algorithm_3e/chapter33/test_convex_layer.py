from src.introduction_to_algorithm_3e.chapter33.convex_layer import find_convex_layers
from tests.unit_test_template import UnitTestTemplate


class ConvexLayerTest(UnitTestTemplate):
    def test_find_convex_layers_small(self):
        points = [[0, 3], [2, 2], [1, 1], [2, 1],
                  [3, 0], [0, 0], [3, 3]]
        actual_cl = find_convex_layers(points)
        expected_cl = [[[0, 0], [3, 0], [3, 3], [0, 3]],
                       [[1, 1], [2, 1], [2, 2]]]
        self.assertEqual(expected_cl, actual_cl)

    def test_find_convex_layers_big(self):
        expected_layers = []
        points = []
        size = 30

        for i in range(size // 2):
            layer = [[i, i],
                     [size - i - 1, i],
                     [size - i - 1, size - i - 1],
                     [i, size - i - 1]]
            expected_layers += [layer]
            points += layer

        actual_cl = find_convex_layers(points)
        self.assertEqual(expected_layers, actual_cl)
