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

    # Base cases:
    # If the list has less than 2 items, return it unchanged.
    if len(l) <= 1:
        return l

    # If the list has 2 items, swap them if the first is larger than the second,
    #  and return it.
    if len(l) == 2:
        if l[0] > l[1]:
            l[0], l[1] = l[1], l[0]
        return l

    # Divide:
    # Recursively call this function on the sublist that doesn't include the first
    #  two elements of the list.
    sorted_sublist = sort_even(l[2:])

    # Conquer:
    # Swap the first two elements of the original list with the first two elements
    #  of the sublist, if the first element of the original list is larger than
    #  the first element of the sublist.
    if l[0] > sorted_sublist[0]:
        l[0], l[1] = sorted_sublist[0], sorted_sublist[1]

    # Return the sorted list.
    return l
