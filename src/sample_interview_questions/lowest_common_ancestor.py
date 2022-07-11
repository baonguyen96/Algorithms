"""
Find lowest common ancestor of any 2 child node in a binary tree.

           1
         /   \
       3      2
     /  \
   4    6
       /
      5

lca(4,5) = 3
lca(3,5) = 3
etc.

Input will be index instead.
Represent the tree above as array: [1, 3, 2, 4, 6, None, None, None, None, 5]
"""


from utilities.utility import is_even


def get_lowest_common_ancestor(tree, i1, i2):
    # O(lg n) time

    lca_index = 0
    lca_value = tree[0]
    i1_ancestors = []
    i2_ancestors = []

    i = i1
    while i >= 0:
        i1_ancestors += [i]

        if i == 0:
            break

        if is_even(i):
            i = i // 2 - 1
        else:
            i = i // 2

    i = i2
    while i >= 0:
        i2_ancestors += [i]

        if i == 0:
            break

        if is_even(i):
            i = i // 2 - 1
        else:
            i = i // 2

    if len(i1_ancestors) > len(i2_ancestors):
        longer_tree = i1_ancestors
        shorter_tree = i2_ancestors
    else:
        longer_tree = i2_ancestors
        shorter_tree = i1_ancestors

    longer_tree_start_index = len(longer_tree) - len(shorter_tree)

    for i in range(0, len(shorter_tree)):
        if shorter_tree[i] == longer_tree[longer_tree_start_index + i]:
            lca_value = tree[shorter_tree[i]]
            lca_index = shorter_tree[i]
            break

    return lca_index, lca_value
