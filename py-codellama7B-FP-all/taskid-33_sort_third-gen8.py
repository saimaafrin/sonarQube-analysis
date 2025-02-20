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

    l1, l2, l3 = [], [], []
    for i, x in enumerate(l):
        if i % 3 == 0:
            l1.append(x)
        elif i % 3 == 1:
            l2.append(x)
        else:
            l3.append(x)
    l1.sort()
    l2.sort()
    l3.sort()
    return l1 + l2 + l3
