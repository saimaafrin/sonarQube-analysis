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

    # base case
    if len(l) <= 1:
        return l

    # divide
    first = l[:len(l)//3]
    middle = l[len(l)//3:2*len(l)//3]
    last = l[2*len(l)//3:]

    # conquer
    first = sort_third(first)
    middle = sort_third(middle)
    last = sort_third(last)

    # combine
    return first + sorted(middle) + last
