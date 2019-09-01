import unittest
from Source.Utitilies.utility import binary_search, get_random_array


class UtilityTest(unittest.TestCase):

    def test_get_random_array(self):
        array = get_random_array(10, -10, 10)
        array.sort()
        self.assertEqual(len(array), 10)
        self.assertTrue(array[0] >= -10)
        self.assertTrue(array[9] <= 10)

    def test_binary_search(self):
        array = [-1, 0, 1, 2, 3]
        self.assertEqual(0, binary_search(array, -1))
        self.assertEqual(1, binary_search(array, 0))
        self.assertEqual(-1, binary_search(array, 9))
