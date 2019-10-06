from SampleInterviewQuestions.tower_hopper import is_hoppable
from Test.unit_test_template import UnitTestTemplate


class TowerHopperTest(UnitTestTemplate):
    def test_is_hoppable_expect_true(self):
        array = [2, 0]
        self.assertTrue(is_hoppable(array))

        array = [4, 2, 0, 0, 2, 0]
        self.assertTrue(is_hoppable(array))

        array = [4, 10, 0, 0, 1, 0]
        self.assertTrue(is_hoppable(array))

    def test_is_hoppable_expect_true_performance(self):
        array = [1 for i in range(100)]
        self.assertTrue(is_hoppable(array))

    def test_is_hoppable_expect_false(self):
        array = [1, 0]
        self.assertFalse(is_hoppable(array))

        array = [4, 2, 0, 0, 1, 0]
        self.assertFalse(is_hoppable(array))

    def test_is_hoppable_expect_false_performance(self):
        array = [0 for i in range(1000)]
        self.assertFalse(is_hoppable(array))
