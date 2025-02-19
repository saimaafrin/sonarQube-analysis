from typing import List

def sort_even(l: List[int]) -> List[int]:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """

    even_indicies = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indicies]
    sorted_values = sorted(even_values)
    sorted_indicies = even_indicies.copy()
    for i in range(len(even_values)):
        sorted_indicies[i] = sorted_values[i]
    return sorted_indicies
