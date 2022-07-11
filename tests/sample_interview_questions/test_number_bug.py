from src.sample_interview_questions.number_bug import sort_with_mappings
from tests.unit_test_template import UnitTestTemplate


class NumberBugTest(UnitTestTemplate):
    def test_sort_with_mappings(self):
        mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
        numbers = [990, 332, 32]

        expected = [332, 32, 990]
        actual = sort_with_mappings(numbers, mapping)
        self.assertEqual(expected, actual)

    def test_sort_with_mappings_unique(self):
        mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
        numbers = [3, 2, 1]

        expected = [3, 2, 1]
        actual = sort_with_mappings(numbers, mapping)
        self.assertEqual(expected, actual)

    def test_sort_with_mappings_unique_reversed(self):
        mapping = [3, 5, 4, 6, 2, 7, 9, 8, 0, 1]
        numbers = [1, 2, 3]

        expected = [3, 2, 1]
        actual = sort_with_mappings(numbers, mapping)
        self.assertEqual(expected, actual)
