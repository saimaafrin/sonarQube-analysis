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

    result: List[int] = []
    while lst:
        min_idx = min(range(len(lst)), key=lst.__getitem__)
        result.append(lst[min_idx])
        lst = lst[:min_idx] + lst[min_idx+1:]

    return result
