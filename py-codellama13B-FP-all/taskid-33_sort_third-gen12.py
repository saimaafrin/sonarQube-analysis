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


    n: int = len(l)

    l_third: List[int] = [l[i] for i in range(n) if i % 3 == 2]

    l_third.sort()

    l_out: List[int] = [0] * n

    for i in range(n):
        if i % 3 == 0:
            l_out[i] = l[i]
        elif i % 3 == 1:
            l_out[i] = l_third.pop()

    return l_out
