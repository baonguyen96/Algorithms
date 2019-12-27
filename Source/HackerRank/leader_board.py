"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

e.g.
    existing_scores = [100, 90, 90, 80, 75, 60]     # sorted desc
    player_scores   = [50, 65, 77, 90, 102]         # sorted asc
    expected_ranks  = [6, 5, 4, 2, 1]
"""


def climb_leader_board(existing_scores, player_scores):
    ranks = []
    rank = None

    for i in range(len(player_scores)):
        score = player_scores[i]

        # optimize for duplication
        if rank is not None and player_scores[i] == player_scores[i - 1]:
            pass
        else:
            rank = find_rank(existing_scores, score)

        ranks += [rank]

    return ranks


def find_rank(existing_scores, current_score):
    rank = 1

    for i in range(len(existing_scores)):
        if current_score >= existing_scores[i]:
            break
        elif i > 0 and existing_scores[i] == existing_scores[i - 1]:
            continue
        else:
            rank += 1

    return rank
