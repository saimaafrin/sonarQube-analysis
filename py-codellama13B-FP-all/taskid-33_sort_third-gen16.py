from typing import List

def sort_third(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """

    # Your code here
    l_sorted = sorted(l)
    l_sorted_indices = []
    for i in range(len(l)):
        if i % 3 == 0:
            l_sorted_indices.append(i)
    l_indices = [i for i in range(len(l))]
    l_indices_not_sorted = [i for i in l_indices if i not in l_sorted_indices]
    l_sorted_not_indices = [l_sorted[i] for i in l_indices_not_sorted]
    l_sorted_all = [l_sorted[i] for i in l_sorted_indices] + l_sorted_not_indices
    return l_sorted_all
