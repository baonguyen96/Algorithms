import copy

from src.sample_interview_questions.random_array_reorder import reorder
from tests.unit_test_template import UnitTestTemplate


class RandomArrayReorderTest(UnitTestTemplate):
    def test_reorder(self):
        a = list(range(10))
        b = reorder(copy.deepcopy(a))
        self.assertEqual(len(a), len(b))
        self.assertNotEqual(a, b)
        self.assertEqual(set(a), set(b))

    def test_reorder_performance(self):
        a = list(range(100))
        b = reorder(copy.deepcopy(a))
        self.assertEqual(len(a), len(b))
        self.assertNotEqual(a, b)
        self.assertEqual(set(a), set(b))
