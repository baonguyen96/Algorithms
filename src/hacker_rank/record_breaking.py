"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

Maria plays college basketball and wants to go pro. Each season she maintains a record of her play.
    She tabulates the number of times she breaks her season record for most points and least points in a game.
    Points scored in the first game establish her record for the season, and she begins counting from there.
    Given Maria's scores for a season, find and print the number of times
    she breaks her records for most and least points scored during the season.

    First score does not count as either max or min.
"""


def count_records(scores):
    lowest_record_count = 0
    highest_record_count = 0
    current_lowest = scores[0]
    current_highest = scores[0]

    for score in scores[1:]:
        if score < current_lowest:
            current_lowest = score
            lowest_record_count += 1
        elif score > current_highest:
            current_highest = score
            highest_record_count += 1

    return [highest_record_count, lowest_record_count]
