from HackerRank.bowling_pin import is_winning
from Test.unit_test_template import UnitTestTemplate


class BowlingPinTest(UnitTestTemplate):
    def test_is_winning_win_1(self):
        pins = 'XIIX'
        expected = True
        actual = is_winning(pins)
        self.assertEqual(expected, actual)

    def test_is_winning_win_2(self):
        pins = 'IIIII'
        expected = True
        actual = is_winning(pins)
        self.assertEqual(expected, actual)

    def test_is_winning_lose_1(self):
        pins = 'IXXI'
        expected = False
        actual = is_winning(pins)
        self.assertEqual(expected, actual)

    def test_is_winning_lose_2(self):
        pins = 'IIXII'
        expected = False
        actual = is_winning(pins)
        self.assertEqual(expected, actual)
