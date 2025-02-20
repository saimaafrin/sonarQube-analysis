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


    def pluck_internal(arr: List[int]) -> List[int]:
        if not arr:
            return []

        # Find the smallest even number
        # If there are multiple, we want the one with the lowest index
        min_even_value = float('inf')
        min_even_index = None
        for i, node in enumerate(arr):
            if node % 2 == 0 and node < min_even_value:
                min_even_value = node
                min_even_index = i

        # If there are no even values, return an empty list
        if min_even_index is None:
            return []

        # Otherwise, pluck the smallest even number and return it
        plucked = arr.pop(min_even_index)
        return [plucked, min_even_index]

    # Solve the problem recursively, by first plucking from the left and right
    # half of the array and then merging the two answers.
    #
    # If we have an odd number of nodes in the array, then the first
    # pluck will be from the left half, and the second pluck will be
    # from the right half.
    #
    # If we have an even number of nodes in the array, then we will
    # pluck from both halves.
    #
    # To illustrate this, consider the following example:
    #
    #    [5, 0, 3, 0, 4, 2]
    #
    # If we pluck from the left half, we will get [5, 0, 3]
    # If we pluck from the right half, we will get [4, 2]
    # If we merge the two answers, we get [5, 4, 2]
    #
    # In general, we will pluck from the left half, then merge that
    # with the result of plucking from the right half.
    left_arr, right_arr = arr[:len(arr)//2], arr[len(arr)//2:]
    left_result = pluck_internal(left_arr)
    right_result = pluck_internal(right_arr)
    if not left_result:
        return right_result
    if not right_result:
        return left_result

    if left_result[0] < right_result[0]:
        return [left_result[0], left_result[1]]
    return [right_result[0], right_result[1]]
