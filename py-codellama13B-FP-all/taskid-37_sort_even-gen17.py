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

    # sort the even indices
    l_sorted = [x for x in l if x % 2 == 0]
    l_sorted.sort()
    # build a new list by iterating over the original list and putting the
    # elements of the sorted list into its even indices
    l_new = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l_new.append(l_sorted.pop(0))
        else:
            l_new.append(l[i])
    return l_new
