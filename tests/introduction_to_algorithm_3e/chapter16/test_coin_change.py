import src.introduction_to_algorithm_3e.chapter16.coin_change as cc
from tests.unit_test_template import UnitTestTemplate


class CoinChangeTest(UnitTestTemplate):
    def test_make_coin_change_single_quarter(self):
        amount = 0.25
        expected = [1, 0, 0, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_single_dime(self):
        amount = 0.1
        expected = [0, 1, 0, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_single_nickel(self):
        amount = 0.05
        expected = [0, 0, 1, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_single_penny(self):
        amount = 0.01
        expected = [0, 0, 0, 1]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_one_of_each(self):
        amount = 0.41
        expected = [1, 1, 1, 1]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_none(self):
        amount = 0
        expected = [0, 0, 0, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_multiple(self):
        amount = 0.43
        expected = [1, 1, 1, 3]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

        amount = 0.5
        expected = [2, 0, 0, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

        amount = 0.65
        expected = [2, 1, 1, 0]
        actual = cc.make_coin_change(amount)
        self.assertEqual(expected, actual)

    def test_make_coin_change_large_loop(self):
        amount = 1000000
        actual = cc.make_coin_change_loop(amount)
        self.assertTrue(True)

    def test_make_coin_change_large(self):
        amount = 1000000
        actual = cc.make_coin_change(amount)
        self.assertTrue(True)
