from HackerRank.record_breaking import count_records
from Test.unit_test_template import UnitTestTemplate


class RecordBreakingTest(UnitTestTemplate):
    def test_count_records_all_top(self):
        scores = list(range(10))
        expected = [9, 0]
        actual = count_records(scores)
        self.assertEqual(expected, actual)

    def test_count_records_all_bottom(self):
        scores = list(reversed((range(10))))
        expected = [0, 9]
        actual = count_records(scores)
        self.assertEqual(expected, actual)

    def test_count_records_random(self):
        scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
        expected = [2, 4]
        actual = count_records(scores)
        self.assertEqual(expected, actual)
