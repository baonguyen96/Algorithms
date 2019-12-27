from HackerRank.leader_board import climb_leader_board
from Test.unit_test_template import UnitTestTemplate


class LeaderBoardTest(UnitTestTemplate):

    def test_climb_leader_board_first(self):
        existing_scores = [100, 90, 90, 80, 75, 60]
        player_scores = [102]
        expected_ranks = [1]
        actual_ranks = climb_leader_board(existing_scores, player_scores)
        self.assertEqual(expected_ranks, actual_ranks)

    def test_climb_leader_board_last(self):
        existing_scores = [100, 90, 90, 80, 75, 60]
        player_scores = [50]
        expected_ranks = [6]
        actual_ranks = climb_leader_board(existing_scores, player_scores)
        self.assertEqual(expected_ranks, actual_ranks)

    def test_climb_leader_board_middle_duplicated(self):
        existing_scores = [100, 90, 90, 80, 75, 60]
        player_scores = [90]
        expected_ranks = [2]
        actual_ranks = climb_leader_board(existing_scores, player_scores)
        self.assertEqual(expected_ranks, actual_ranks)

    def test_climb_leader_board_middle_unique(self):
        existing_scores = [100, 90, 90, 80, 75, 60]
        player_scores = [85]
        expected_ranks = [3]
        actual_ranks = climb_leader_board(existing_scores, player_scores)
        self.assertEqual(expected_ranks, actual_ranks)

    def test_climb_leader_board_overall(self):
        existing_scores = [100, 90, 90, 80, 75, 60]
        player_scores = [50, 65, 77, 90, 90, 102]
        expected_ranks = [6, 5, 4, 2, 2, 1]
        actual_ranks = climb_leader_board(existing_scores, player_scores)
        self.assertEqual(expected_ranks, actual_ranks)