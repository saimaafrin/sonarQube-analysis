from typing import List

def pluck(arr: List[int]) -> List[int]:
    """
    "Given an array representing a branch of a tree that has non-negative integer nodes
    your task is to pluck one of the nodes and return it.
    The plucked node should be the node with the smallest even value.
    If multiple nodes with the same smallest even value are found return the node that has smallest index.

    The plucked node should be returned in a list, [ smalest_value, its index ],
    If there are no even values or the given array is empty, return [].

    Example 1:
    >>> pluck([4, 2, 3])
    [2, 1]
    Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 2:
    >>> pluck([1, 2, 3])
    [2, 1]
    Explanation: 2 has the smallest even value, and 2 has the smallest index.

    Example 3:
    >>> pluck([])
    []
    
    Example 4:
    >>> pluck([5, 0, 3, 0, 4, 2])
    [0, 1]
    Explanation: 0 is the smallest value, but  there are two zeros,
                 so we will choose the first zero, which has the smallest index.

    Constraints:
        * 1 <= nodes.length <= 10000
        * 0 <= node.value
    """

    # Your code here
    # edge case: if empty array
    if not arr: return []

    # edge case: if only one item in list
    if len(arr) == 1: return arr

    # init index, even values list
    idx = 0
    evens = []

    # loop through list
    for i, val in enumerate(arr):
        # if even, add to list
        if val % 2 == 0:
            evens.append(val)

    # edge case: if no evens
    if not evens: return []

    # min even
    min_even = min(evens)

    # index of min even
    idx = arr.index(min_even)

    # return [even, index]
    return [min_even, idx]
