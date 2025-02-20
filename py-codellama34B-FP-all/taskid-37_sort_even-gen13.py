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

    l_even = sorted(l[0::2])
    l_odd = l[1::2]
    return [x for p in zip(l_even, l_odd) for x in p] + l_odd if len(l_even) < len(l_odd) else [x for p in zip(l_even, l_odd) for x in p]
