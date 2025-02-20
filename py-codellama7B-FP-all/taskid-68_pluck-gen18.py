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

    # 1. Find even nodes
    # 2. Select the smallest value
    # 3. Select the first value that has the same value as the smallest value
    # 4. Return the value and index
    if len(arr) == 0:
        return []

    # Find even nodes
    even_nodes = [node for node in arr if node % 2 == 0]

    if len(even_nodes) == 0:
        return []

    # Select the smallest value
    smallest_value = min(even_nodes)

    # Select the first value that has the same value as the smallest value
    smallest_node = [node for node in even_nodes if node == smallest_value][0]

    return [smallest_node, arr.index(smallest_node)]
