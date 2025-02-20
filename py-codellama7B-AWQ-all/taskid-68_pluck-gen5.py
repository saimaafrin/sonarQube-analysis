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

    nodes_with_even_value = [node for index, node in enumerate(arr) if node % 2 == 0]

    if not nodes_with_even_value:
        return []

    min_value = min(nodes_with_even_value)
    nodes_with_same_value = [node for node in nodes_with_even_value if node == min_value]
    node_index = min(nodes_with_same_value, key=lambda node: nodes_with_same_value.index(node))

    return [min_value, arr.index(node_index)]
