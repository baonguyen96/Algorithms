import SampleInterviewQuestions.subset as ss
from Test.unit_test_template import UnitTestTemplate


class SubSetTest(UnitTestTemplate):
    def test_get_all_subsets_empty_set(self):
        s = []
        expected = [[]]
        actual = ss.get_all_subsets(s)
        self.assertEqual(expected, actual)

    def test_get_all_subsets_single(self):
        s = [1]
        expected = [[], [1]]
        actual = ss.get_all_subsets(s)
        self.assertEqual(expected, actual)

    def test_get_all_subsets_multiple(self):
        s = [1, 2]
        expected = [[],
                    [1], [2],
                    [1, 2]]
        actual = ss.get_all_subsets(s)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_get_all_subsets_multiple_bigger(self):
        s = [1, 2, 3]
        expected = [[],
                    [1], [2], [3],
                    [1, 2], [1, 3], [2, 3],
                    [1, 2, 3]]
        actual = ss.get_all_subsets(s)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_get_all_subsets_performance(self):
        s = [i for i in range(20)]
        actual = ss.get_all_subsets(s)
        self.assertEqual(2 ** len(s), len(actual))

    def test_count_subsets_with_sum_empty(self):
        array = [1, 2, 3, 4]
        s = 0
        expected = 1
        actual = ss.count_subsets_with_sum(array, s)
        self.assertEqual(expected, actual)

        array = []
        s = 0
        expected = 1
        actual = ss.count_subsets_with_sum(array, s)
        self.assertEqual(expected, actual)

    def test_count_subsets_with_sum(self):
        array = [2, 4, 6, 10]
        s = 16
        expected = 2
        actual = ss.count_subsets_with_sum(array, s)
        self.assertEqual(expected, actual)