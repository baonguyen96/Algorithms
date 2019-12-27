"""
https://www.hackerrank.com/challenges/electronics-shop/problem

Monica wants to buy a keyboard and a USB drive from her favorite electronics store.
    The store has several models of each. Monica wants to spend as much as possible for the  items, given her budget.
    Given the price lists for the store's keyboards and USB drives, and Monica's budget,
    find and print the amount of money Monica will spend.
    If she doesn't have enough money to both a keyboard and a USB drive, print -1 instead.
    She will buy only the two required items.
"""


def get_max_spending_possible(keyboards, drives, budget):
    keyboards = [k for k in keyboards if k <= budget]
    drives = [d for d in drives if d <= budget]
    max_cost = -1

    for keyboard in keyboards:
        for drive in drives:
            current_cost = keyboard + drive

            if max_cost < current_cost <= budget:
                max_cost = current_cost

    return max_cost
