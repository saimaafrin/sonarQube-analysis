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

    # Create an empty list, l_even, to store the even values
    # of the list l
    l_even = []
    # Iterate through the list l and append values to l_even
    # if they are at even indicies
    for i in range(len(l)):
        if i % 2 == 0:
            l_even.append(l[i])
    # Sort the list l_even
    l_even.sort()
    # Iterate through the list l and replace values at even indicies
    # with the values of the sorted list l_even
    for i in range(len(l)):
        if i % 2 == 0:
            l[i] = l_even[i // 2]
    # Return the list l
    return l
