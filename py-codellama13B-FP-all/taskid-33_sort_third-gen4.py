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

    # return l
    length = len(l)
    copy = l.copy()
    # loop through all indicies of the copy
    for i in range(length):
        # if the index is divisible by 3
        if (i % 3 == 0):
            # swap the value at the index with the value at the index that is three more than the index
            copy[i], copy[i+3] = copy[i+3], copy[i]
    return copy
