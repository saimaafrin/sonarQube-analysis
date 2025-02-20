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

    res = []

    while lst:
        # Find minimum and add it to result
        minimum = min(lst)
        res.append(minimum)
        lst.remove(minimum)

        # If more than one element left, find max and add it to result
        if len(lst) > 1:
            maximum = max(lst)
            res.append(maximum)
            lst.remove(maximum)

    return res
