from src.sample_interview_questions.sum import find_sum
from tests.unit_test_template import UnitTestTemplate


class SumTest(UnitTestTemplate):
    def test_find_sum(self):
        n = 27
        self.assertEqual(261, find_sum(n))

        n = 19
        self.assertEqual(139, find_sum(n))

        n = 7
        self.assertEqual(19, find_sum(n))
