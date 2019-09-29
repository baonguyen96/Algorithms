"""
15.1-5

Find Fibonacci sequence
"""


def fibonacci_recursive(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 2) + fibonacci_recursive(n - 1)


def fibonacci_loop(n):
    if n == 0 or n == 1:
        return 1

    first = 1
    second = 1
    third = first + second

    for i in range(1, n):
        third = first + second
        first = second
        second = third

    return third
