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

    even = []
    for i in range(len(l)):
        if i % 2 == 0:
            even.append(l[i])
    even.sort()
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = even.pop(0)
    return l
