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

    if not lst:
        return []
    min_val = lst[0]
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < min_val:
            min_val = lst[i]
        elif lst[i] > max_val:
            max_val = lst[i]
    return [min_val, max_val] + strange_sort_list(lst[2:])
