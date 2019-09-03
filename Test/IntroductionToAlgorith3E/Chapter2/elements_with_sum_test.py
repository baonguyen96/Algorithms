import Source.IntroductionToAlgorithm3E.Chapter2.elements_with_sum as ews
from Source.Utitilies.utility import get_random_array
from Test.unit_test_template import UnitTestTemplate


class ElementsWithSumTest(UnitTestTemplate):

    def test_exist_elements_with_sum_found_short(self):
        a = [2, 5, 1, 4]
        found = ews.exist_elements_with_sum_brute_force(a, 7)
        self.assertTrue(found)

        a = [2, 5, 1, 4]
        found = ews.exist_elements_with_sum_enhance(a, 7)
        self.assertTrue(found)

    def test_exist_elements_with_sum_not_found_short(self):
        a = [2, 5, 1, 4]
        found = ews.exist_elements_with_sum_brute_force(a, 0)
        self.assertFalse(found)

        a = [2, 5, 1, 4]
        found = ews.exist_elements_with_sum_enhance(a, 0)
        self.assertFalse(found)

    def test_exist_elements_with_sum_found_long_brute_force(self):
        a = get_random_array(10000, -20, 30)
        found = ews.exist_elements_with_sum_brute_force(a, a[0] + a[1])
        self.assertTrue(found)

    def test_exist_elements_with_sum_found_long_enhance(self):
        a = get_random_array(10000, -20, 30)
        found = ews.exist_elements_with_sum_enhance(a, a[0] + a[1])
        self.assertTrue(found)
