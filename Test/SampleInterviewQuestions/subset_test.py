from SampleInterviewQuestions.subset import get_all_subsets
from Test.unit_test_template import UnitTestTemplate


class SubSetTest(UnitTestTemplate):
    def test_get_all_subsets_empty_set(self):
        s = []
        expected = [[]]
        actual = get_all_subsets(s)
        self.assertEqual(expected, actual)

    def test_get_all_subsets_single(self):
        s = [1]
        expected = [[], [1]]
        actual = get_all_subsets(s)
        self.assertEqual(expected, actual)

    def test_get_all_subsets_multiple(self):
        s = [1, 2]
        expected = [[],
                    [1], [2],
                    [1, 2]]
        actual = get_all_subsets(s)
        self.assertEqual(expected, actual)

    def test_get_all_subsets_multiple_bigger(self):
        s = [1, 2, 3]
        expected = [[],
                    [1], [2], [3],
                    [1, 2], [1, 3], [2, 3],
                    [1, 2, 3]]
        actual = get_all_subsets(s)
        self.assertEqual(sorted(expected), sorted(actual))

    def test_get_all_subsets_performance(self):
        s = [i for i in range(10)]
        actual = get_all_subsets(s)
        self.assertEqual(2 ** len(s), len(actual))
