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
    result: List[int] = [min(lst)]
    while len(lst) > 0:
        current_min = min(lst)
        lst.remove(current_min)
        if len(lst) > 0:
            result.append(max(lst))
        else:
            result.append(current_min)
    return result
