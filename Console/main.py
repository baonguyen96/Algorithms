import math
import operator
import random

from IntroductionToAlgorithm3E.Chapter5.random_generator import get_random_number_advance
from IntroductionToAlgorithm3E.Chapter7.partition import random_partition, partition


def get_random_number():
    a = 10
    b = 100

    for i in range(20):
        rand = get_random_number_advance(a, b)
        print(rand)


def get_random_2d_array():
    points = [[random.randint(10, 100) for i in range(2)] for j in range(5)]
    print(points)


def get_partition():
    print('random partition')
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print(a)

    for i in range(3):
        pivot = random_partition(a)
        print(pivot)
        print(a)

    print()

    print('deterministic partition')
    a = [2, 8, 7, 1, 3, 5, 6, 4]
    print(a)
    for i in range(3):
        pivot = partition(a)
        print(pivot)
        print(a)


def test_median():
    a = [0.1, 0.35, 0.05, 0.1, 0.15, 0.05, 0.2]
    b = list(set(a))
    print('b = ', *b, sep=',')

    w = []

    for i in range(len(b)):
        w += [b[i]] * (i + 1)

    print(a)
    print(w)

    a.sort()
    w.sort()

    print(a)
    print(w)


def test_array():
    a = [1, 2]
    b = a * 3
    print(a)
    print(b)


def sort_2d_array():
    a = [
        [12, 18, 6, 3],
        [12, 15, 6, 3],
        [4, 3, 1, 2],
        [15, 8, 9, 6]
    ]

    print(a)
    # a.sort(key=lambda x: x[1])

    a = sorted(a, key=operator.itemgetter(0, 1))
    print(a)


def main():
    get_random_2d_array()


if __name__ == '__main__':
    main()
