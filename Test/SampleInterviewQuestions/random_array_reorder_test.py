import copy

from SampleInterviewQuestions.random_array_reorder import reorder
from Test.unit_test_template import UnitTestTemplate


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
