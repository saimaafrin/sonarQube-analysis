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

    l1 = [i for i in l if i % 2 == 0]
    l1 = sorted(l1)
    l2 = [i for i in l if i % 2 != 0]
    l2 = sorted(l2)
    for i in range(len(l2)):
        l2[i] = l1[i]
    return l2
