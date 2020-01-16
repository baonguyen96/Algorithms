"""
https://www.hackerrank.com/challenges/build-a-string/problem

Greg wants to build a string,  of length . Starting with an empty string, he can perform  operations:
    - Add a character to the end of  for  dollars.
    - Copy any substring of , and then add it to the end of  for  dollars.
Calculate minimum amount of money Greg needs to build.
"""


def build_string(target_string, cost_to_create, cost_to_copy):
    string_so_far = ''
    cost = 0
    temp = ''
    i = 0

    while i < len(target_string):
        temp += target_string[i]

        if temp in string_so_far:
            i += 1

            if i < len(target_string):
                continue

        if len(temp) > 1:
            i -= 1
            temp = temp[:-1]

            if temp in string_so_far and len(temp) == 1:
                new_cost_to_add = min(cost_to_copy, cost_to_create)
            elif len(temp) > 1:
                new_cost_to_add = cost_to_copy
            else:
                new_cost_to_add = cost_to_create
        else:
            new_cost_to_add = cost_to_create

        string_so_far += temp
        cost += new_cost_to_add
        temp = ''
        i += 1

    return cost
