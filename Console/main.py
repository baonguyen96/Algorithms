import operator
import random
import statistics

import networkx as nx

import IntroductionToAlgorithm3E.Chapter15.matrix_multiplication as mat
from IntroductionToAlgorithm3E.Chapter25.floyd_warshall import get_all_pair_shortest_paths_fw
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


def get_median():
    a = list(range(10))
    print(statistics.median(a))

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


def get_array():
    a = [1, 2]
    b = a * 3
    c = [1.5] * 3
    print(a)
    print(b)
    print(c)


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


def get_decimal_places():
    i = 10
    decimal_places = str(i)[::-1].find('.')
    print(decimal_places)

    f1 = 10.0
    decimal_places = str(f1)[::-1].find('.')
    print(decimal_places)

    f2 = 10.01
    decimal_places = str(f2)[::-1].find('.')
    print(decimal_places)


def test_array_reference():
    a = [1, 2, 3]
    b = a

    print(a)
    print(b)

    b[0] = 0

    print(a)
    print(b)


def test_aray_contain():
    a = [[1, 1], [2, 3]]
    x = [1, 1]
    y = [1, 0]
    print(x in a)
    print(y in a)
    print(a[1][1])

    dimensions = 3
    matrix_costs = [[None for c in range(dimensions - 1)] for r in range(dimensions - 1)]
    print(matrix_costs[1][1])


def test_print_optimal_parenthesize():
    dimensions = [5, 10, 3, 12, 5, 50, 6]
    matrix_costs, matrix_splits = mat.find_optimal_matrix_chain_order(dimensions)
    s = mat.get_optimal_chain_as_string(matrix_splits, 0, len(dimensions) - 2)
    print(s)


def test_sub_2d():
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    print(array)

    x = [r.pop(0) for r in array].pop(0)
    print(x)

    print(array)


def get_fw_graph():
    graph = nx.DiGraph()
    graph.add_edges_from([('1', '3')], weight=-2)
    graph.add_edges_from([('3', '4')], weight=-2)
    graph.add_edges_from([('4', '2')], weight=-1)
    graph.add_edges_from([('2', '1')], weight=4)
    graph.add_edges_from([('2', '3')], weight=-3)

    actual_distances, actual_paths = get_all_pair_shortest_paths_fw(graph)
    print(actual_distances)
    print()
    print(actual_paths)


def main():
    print('hello world')


if __name__ == '__main__':
    main()
