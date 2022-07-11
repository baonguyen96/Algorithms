from src.hacker_rank.electronic_shop import get_max_spending_possible
from tests.unit_test_template import UnitTestTemplate


class ElectronicShopTest(UnitTestTemplate):
    def test_get_max_spending_possible_within_budget(self):
        keyboards = [3, 1]
        drives = [5, 2, 8]
        budget = 10

        expected = 9
        actual = get_max_spending_possible(keyboards, drives, budget)
        self.assertEqual(expected, actual)

    def test_get_max_spending_possible_none(self):
        keyboards = [4]
        drives = [5]
        budget = 5

        expected = -1
        actual = get_max_spending_possible(keyboards, drives, budget)
        self.assertEqual(expected, actual)

    def test_get_max_spending_possible_within_budget_large(self):
        keyboards = [100 for i in range(10000)] + [9]
        drives = [100 for i in range(10000)] + [1, 2, 3]
        budget = 10

        expected = 10
        actual = get_max_spending_possible(keyboards, drives, budget)
        self.assertEqual(expected, actual)
