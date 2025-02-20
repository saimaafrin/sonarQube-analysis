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

    if len(lst) == 0:
        return []

    result: List[int] = []
    current_min: int = min(lst)
    current_max: int = max(lst)
    while len(result) < len(lst):
        if current_min in lst:
            result.append(current_min)
            lst.remove(current_min)
        else:
            current_min = min(lst)

        if current_max in lst:
            result.append(current_max)
            lst.remove(current_max)
        else:
            current_max = max(lst)

    return result
