import unittest

from src.introduction_to_algorithm_3e.chapter16.activity_selection_max_value import get_compatible_activities_max_values
from tests.unit_test_template import UnitTestTemplate


@unittest.skip('comments_for_skipping_unit_tests')
class ActivitySelectionMaxValueTest(UnitTestTemplate):
    def test_get_compatible_activities_max_values(self):
        activities = [[1, 1, 4],
                      [2, 3, 5],
                      [3, 0, 6],
                      [4, 5, 7],
                      [5, 3, 9],
                      [6, 5, 9],
                      [7, 6, 10],
                      [8, 8, 11],
                      [9, 8, 12],
                      [10, 2, 14],
                      [11, 12, 16]]
        expected_activities = [3, 9, 11]
        actual_activities = get_compatible_activities_max_values(activities)
        self.assertEqual(expected_activities, actual_activities)
