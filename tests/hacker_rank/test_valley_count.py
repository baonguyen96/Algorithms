from src.hacker_rank.valley_count import count_valley
from tests.unit_test_template import UnitTestTemplate


class ValleyCountTest(UnitTestTemplate):
    def test_count_valley_single(self):
        path = 'DDUUUUDD'
        expected = 1
        actual = count_valley(path)
        self.assertEqual(expected, actual)

        path = 'UDDDUDUU'
        expected = 1
        actual = count_valley(path)
        self.assertEqual(expected, actual)

    def test_count_valley_none(self):
        path = 'UUDD'
        expected = 0
        actual = count_valley(path)
        self.assertEqual(expected, actual)

        path = 'UDUD'
        expected = 0
        actual = count_valley(path)
        self.assertEqual(expected, actual)

    def test_count_valley_double(self):
        path = 'DUDUUD'
        expected = 2
        actual = count_valley(path)
        self.assertEqual(expected, actual)

        path = 'DUDU'
        expected = 2
        actual = count_valley(path)
        self.assertEqual(expected, actual)
