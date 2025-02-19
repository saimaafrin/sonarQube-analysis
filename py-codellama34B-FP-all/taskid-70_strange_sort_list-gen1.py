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

    min_value = min(lst)
    max_value = max(lst)
    result = []
    while min_value <= max_value:
        for item in lst:
            if min_value <= item <= max_value:
                result.append(item)
                min_value = item + 1
                break
        for item in reversed(lst):
            if min_value <= item <= max_value:
                result.append(item)
                max_value = item - 1
                break
    return result
