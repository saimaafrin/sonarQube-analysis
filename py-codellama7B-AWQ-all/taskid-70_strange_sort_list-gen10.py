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
    res = []
    min_value = min(lst)
    res.append(min_value)
    lst.remove(min_value)
    max_value = max(lst)
    res.append(max_value)
    lst.remove(max_value)
    return res + strange_sort_list(lst)
