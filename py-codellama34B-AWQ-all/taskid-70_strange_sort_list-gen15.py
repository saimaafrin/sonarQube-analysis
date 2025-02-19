from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    >>> strange_sort_list([1, 2, 3, 4])
    [1, 4, 2, 3]
    >>> strange_sort_list([5, 5, 5, 5])
    [5, 5, 5, 5]
    >>> strange_sort_list([])
    []
    """

    # YOUR CODE HERE
    # Please print out which line of the test case causes the error
    # so that we can debug the cause more easily.
    if len(lst) == 0:
        return lst
    if len(lst) == 1:
        return [lst[0]]
    result = []
    while len(lst) > 0:
        result.append(min(lst))
        lst.remove(min(lst))
        result.append(max(lst))
        lst.remove(max(lst))
    return result
