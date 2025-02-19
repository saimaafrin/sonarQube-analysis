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

    # Get the length of the list
    n = len(l)
    # Initialize the new list with the same length as the original list
    l_sorted = [None] * n
    # Iterate over the indices of the original list
    for i in range(n):
        # If the index is divisible by three, get the value at the corresponding index in the new list and sort it
        if i % 3 == 0:
            l_sorted[i] = sorted(l[i])
        # Otherwise, get the value at the corresponding index in the original list and put it in the new list
        else:
            l_sorted[i] = l[i]
    # Return the new list
    return l_sorted
