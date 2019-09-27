"""
Problem 15.1-3

Implement rod-cutting problem using Divide-and-Conquer and Dynamic Programming
Modify rod-cutting problem by also consider the cost to cut
"""


def cut_rod_brute_force(prices, n):
    if n == 0:
        return 0
    revenue = - float('inf')

    for i in range(n):
        revenue = max(revenue, prices[i] + cut_rod_brute_force(prices, n - i))

    return revenue


def cut_rod_enhanced(prices, n):
    if n == 0:
        return 0

    optimal_prices = [- float('inf') for i in range(len(prices))]
    return _cut_rod_memoized(prices, n, optimal_prices)


def _cut_rod_memoized(prices, n, optimal_prices):
    if optimal_prices[n] >= 0:
        return optimal_prices[n]

    if n == 0:
        revenue = 0
    else:
        revenue = - float('inf')
        for i in range(n):
            revenue = max(revenue, prices[i] + _cut_rod_memoized(prices, n - i, optimal_prices))

    optimal_prices[n] = revenue

    return revenue


def cut_rod_nonrecursive(prices, n):
    revenues = [0 for i in range(len(prices) + 1)]

    for i in range(1, n + 1):
        revenue = 0

        for j in range(i):
            revenue = max(revenue, prices[j] + revenues[i - j - 1])

        revenues[i] = revenue

    return revenues[n]


def cut_rod_nonrecursive_with_cost(prices, n, cost_per_cut):
    revenues = [0 for i in range(len(prices) + 1)]

    for i in range(1, n + 1):
        revenue = prices[i]

        for j in range(1, i - 1):
            revenue = max(revenue, prices[j] + revenues[i - j] - cost_per_cut)

        revenues[i] = revenue

    return revenues[n]
