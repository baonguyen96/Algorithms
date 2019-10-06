"""
The Tower Hopper problem gives us an array of values representing heights that express how far we can jump
    from a certain tower, and asks whether there's a way to get from tower[0] (0 indexed) to outside of the array.
    For example, if we have towers = [4, 2, 0, 0, 2, 0], we can jump from towers[0] to towers[4] and then
    outside of the bounds of the array.
    Or we could jump from towers[0] to towers[1] to towers[4] and then out of the array.
    But if we had towers = [4, 2, 0, 0, 1, 0], there would be no way to hop out of the array and we should return False.
"""
from queue import Queue


def is_hoppable(array):
    towers = []
    tower_index = 0
    tower_floor = 1
    found_solution = False

    for i in range(len(array)):
        towers += [[i, array[i]]]

    queue = Queue()
    queue.put(towers[0])

    while not queue.empty():
        tower = queue.get()

        if tower[tower_floor] == 0:
            continue

        for length in range(1, tower[tower_floor] + 1):
            if tower[tower_index] + length > len(towers) - 1:
                found_solution = True
                break
            else:
                queue.put(towers[tower[tower_index] + length])

    return found_solution
