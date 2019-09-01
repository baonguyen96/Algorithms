from Source.IntroductionToAlgorithm3E.Chapter2.elements_with_sum import exist_elements_with_sum
from Source.Utitilies.utility import get_random_array
from Test.unit_test_template import UnitTestTemplate


class ElementsWithSumTest(UnitTestTemplate):

    def test_exist_elements_with_sum_found_short(self):
        a = [2, 5, 1, 4]
        found = exist_elements_with_sum(a, 7)
        self.assertTrue(found)

    def test_exist_elements_with_sum_found_long(self):
        a = get_random_array(100000, -20, 30)
        found = exist_elements_with_sum(a, a[0] + a[1])
        self.assertTrue(found)

    def test_exist_elements_with_sum_not_found_short(self):
        a = [2, 5, 1, 4]
        found = exist_elements_with_sum(a, 0)
        self.assertFalse(found)
