import src.introduction_to_algorithm_3e.chapter16.activity_selection as act
from tests.unit_test_template import UnitTestTemplate


class ActivitySelectionTest(UnitTestTemplate):
    def test_get_max_activities_select_first_to_finish(self):
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
        expected_max_activities = [1, 4, 8, 11]
        actual_max_activities = act.get_max_activities_select_first_to_finish(activities)
        self.assertEqual(expected_max_activities, actual_max_activities)

    def test_get_max_activities_select_last_to_start(self):
        activities = [[3, 0, 6],
                      [1, 1, 4],
                      [10, 2, 14],
                      [2, 3, 5],
                      [4, 5, 7],
                      [5, 3, 9],
                      [6, 5, 9],
                      [7, 6, 10],
                      [8, 8, 11],
                      [9, 8, 12],
                      [11, 12, 16]]
        expected_max_activities = [1, 4, 8, 11]
        actual_max_activities = act.get_max_activities_select_last_to_start(activities)
        self.assertEqual(expected_max_activities, actual_max_activities)
