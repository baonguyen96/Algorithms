import Source.Utitilies.utility as util
from Test.unit_test_template import UnitTestTemplate


class UtilityTest(UnitTestTemplate):

    def test_get_random_array(self):
        array = util.get_random_array(10, -10, 10)
        array.sort()
        self.assertEqual(len(array), 10)
        self.assertTrue(array[0] >= -10)
        self.assertTrue(array[9] <= 10)

    def test_binary_search(self):
        array = [-1, 0, 1, 2, 3]
        self.assertEqual(0, util.binary_search(array, -1))
        self.assertEqual(1, util.binary_search(array, 0))
        self.assertEqual(-1, util.binary_search(array, 9))

    def test_is_even(self):
        even = 2
        self.assertTrue(util.is_even(even))

        odd = 1
        self.assertFalse(util.is_even(even))

    def test_get_difference(self):
        x = 1
        y = 2
        self.assertEqual(1, util.get_difference(x, y))

        x = 1
        y = -1
        self.assertEqual(2, util.get_difference(x, y))
