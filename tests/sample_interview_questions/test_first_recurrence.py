from src.sample_interview_questions.first_recurrence import get_first_recurrence
from tests.unit_test_template import UnitTestTemplate


class FirstRecurrenceTest(UnitTestTemplate):
    def test_get_first_recurrence_none(self):
        s = 'abc'
        expected = None
        self.assertIsNone(expected)

    def test_get_first_recurrence(self):
        s = 'abca'
        expected = 'a'
        actual = get_first_recurrence(s)
        self.assertEqual(expected, actual)

        s = 'babca'
        expected = 'b'
        actual = get_first_recurrence(s)
        self.assertEqual(expected, actual)

        s = 'bacab'
        expected = 'a'
        actual = get_first_recurrence(s)
        self.assertEqual(expected, actual)

    def test_get_first_recurrence_performance(self):
        s = [1] + [i for i in range(2, 100000)] + [2, 1]
        expected = 1
        self.assertEqual(1, expected)
