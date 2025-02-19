from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    n = len(arr)
    max_index = -1

    # use a hash table to keep track of the elements and their indices
    d = {arr[i]: i for i in range(n)}

    # iterate over the array from last to first
    for i in range(n-1, -1, -1):
        # if the current element is not the maximum value in the hash table
        # and the index of the current element is greater than the maximum
        # index found so far, update the max index found so far
        if arr[i] != max(d) and d[arr[i]] > max_index:
            max_index = d[arr[i]]

    # return the max index found so far
    return max_index
