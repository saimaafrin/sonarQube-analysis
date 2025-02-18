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


    # O(n) time | O(1) space
    def pluck(arr: List[int]) -> List[int]:
        smallest = float('inf')
        smallest_index = -1

        for i, val in enumerate(arr):
            if val % 2 == 0 and val < smallest:
                smallest = val
                smallest_index = i

        if smallest_index != -1:
            return [smallest, smallest_index]
        else:
            return []

    # O(n) time | O(n) space
    def pluck(arr: List[int]) -> List[int]:
        plucked = []
        for i, val in enumerate(arr):
            if val % 2 == 0:
                if val < plucked[0][0] or (val == plucked[0][0] and i < plucked[0][1]):
                    plucked = [val, i]

        return plucked or []

    # O(n) time | O(n) space
    def pluck(arr: List[int]) -> List[int]:
        result = []
        for i, v in enumerate(arr):
            if v % 2 == 0:
                if not result or v < result[0][0] or (v == result[0][0] and i < result[0][1]):
                    result = [v, i]
        return result or []

    # O(n) time | O(n) space
    def pluck(arr: List[int]) -> List[int]:
        plucked = -1
        smallest = float('inf')
        for i, v in enumerate(arr):
            if v % 2 == 0:
                if v < smallest:
                    smallest = v
                    plucked = i
        return [smallest, plucked] if plucked != -1 else []

    # O(n) time | O(1) space
    def pluck(arr: List[int]) -> List[int]:
        smallest = float('inf')
        smallest_index = -1
        for i, v in enumerate(arr):
            if v % 2 == 0 and v < smallest:
                smallest = v
                smallest_index = i
        return [smallest, smallest_index] if smallest_index != -1 else []

    # O(n) time | O(1) space
    def pluck(arr: List[int]) -> List[int]:
        smallest = float('inf')
        smallest_index = -1
        for i, v in enumerate(arr):
            if v % 2 == 0 and v < smallest:
                smallest = v
                smallest_index = i
        return [small
