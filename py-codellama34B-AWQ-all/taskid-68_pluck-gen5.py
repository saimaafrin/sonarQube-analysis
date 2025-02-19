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

    def sort_even_indexes(arr):
        even_indexes = []
        odd_indexes = []

        for i in range(len(arr)):
            if i % 2 == 0:
                even_indexes.append(arr[i])
            else:
                odd_indexes.append(arr[i])

        return sorted(even_indexes) + sorted(odd_indexes)
    
    # base case
    if len(arr) == 0:
        return []

    # find smallest even value
    min_val = min(filter(lambda x: x % 2 == 0, arr))

    # find smallest even value index
    min_index = arr.index(min_val)

    return [min_val, min_index]
