from IntroductionToAlgorithm3E.Chapter5.random_generator import get_random_number_brute_force, get_random_number_advance
from Test.unit_test_template import UnitTestTemplate


class MyTestCase(UnitTestTemplate):
    def test_get_random_number_same(self):
        x = get_random_number_brute_force(1, 1)
        self.assertEqual(1, x)

        x = get_random_number_advance(1, 1)
        self.assertEqual(1, x)

    def test_get_random_number_consecutive(self):
        x = get_random_number_brute_force(1, 2)
        self.assertTrue(1 <= x <= 2)

        x = get_random_number_advance(1, 2)
        self.assertTrue(1 <= x <= 2)

    def test_get_random_number_small_range(self):
        x = get_random_number_brute_force(10, 20)
        self.assertTrue(10 <= x <= 20)

        x = get_random_number_advance(10, 20)
        self.assertTrue(10 <= x <= 20)

    def test_get_random_number_brute_force_huge_range(self):
        x = get_random_number_brute_force(10000000, 1000000000)
        self.assertTrue(10000000 <= x <= 1000000000)
        self.assertEqual(10000000, x)

    def test_get_random_number_advance_huge_range(self):
        x = get_random_number_advance(10000000, 1000000000)
        self.assertTrue(10000000 <= x <= 1000000000)
