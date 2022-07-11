import src.introduction_to_algorithm_3e.chapter15.rod_cutting as rc
from tests.unit_test_template import UnitTestTemplate


class RodCuttingTest(UnitTestTemplate):
    def test_cut_rod_brute_force(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 4
        expected_price = 10
        actual_price = rc.cut_rod_brute_force(prices, n)
        self.assertEqual(expected_price, actual_price)

    def test_cut_rod_enhanced(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 4
        expected_price = 10
        actual_price = rc.cut_rod_enhanced(prices, n)
        self.assertEqual(expected_price, actual_price)

    def test_cut_rod_nonrecursive(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        n = 0
        expected_price = 0
        actual_price = rc.cut_rod_nonrecursive(prices, n)
        self.assertEqual(expected_price, actual_price)

        n = 6
        expected_price = 17
        actual_price = rc.cut_rod_nonrecursive(prices, n)
        self.assertEqual(expected_price, actual_price)

        n = 10
        expected_price = 30
        actual_price = rc.cut_rod_nonrecursive(prices, n)
        self.assertEqual(expected_price, actual_price)

    def test_cut_rod_nonrecursive_with_cost_per_cut(self):
        prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
        cost_per_cut = 0
        n = 0
        expected_price = 0
        actual_price = rc.cut_rod_nonrecursive(prices, n, cost_per_cut)
        self.assertEqual(expected_price, actual_price)

        n = 6
        expected_price = 17
        actual_price = rc.cut_rod_nonrecursive(prices, n)
        self.assertEqual(expected_price, actual_price)

        n = 10
        expected_price = 30
        actual_price = rc.cut_rod_nonrecursive(prices, n, cost_per_cut)
        self.assertEqual(expected_price, actual_price)

        cost_per_cut = 1
        n = 4
        expected_price = 9
        actual_price = rc.cut_rod_nonrecursive(prices, n, cost_per_cut)
        self.assertEqual(expected_price, actual_price)

        n = 5
        expected_price = 12
        actual_price = rc.cut_rod_nonrecursive(prices, n, cost_per_cut)
        self.assertEqual(expected_price, actual_price)
