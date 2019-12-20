"""
Given the numbers that the program needs to sort and the mapping (i.e. the shuffled version of the decimal digits)
    return a list of the jumbled numbers sorted by their correct decimal values, ascending.
    If multiple mapped values are equal, the values returned should be in the original order they were appeared.
"""


def sort_with_mappings(numbers, mapping):
    mapping = [str(i) for i in mapping]
    numbers = [str(i) for i in numbers]

    original_numbers = set()
    dictionary = {}

    for number in numbers:
        original = get_original_number(number, mapping)
        original_numbers.add(original)

        if original in dictionary.keys():
            dictionary[original] += [number]
        else:
            dictionary[original] = [number]

    original_numbers = sorted(original_numbers)
    sorted_list = []

    for number in original_numbers:
        sorted_list += dictionary[number]

    return [int(i) for i in sorted_list]


def get_original_number(number, mapping):
    original = ''

    for c in number:
        index = mapping.index(c)
        original += str(index)

    return int(original)
