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
        return lst

    def get_min_max(remaining: List[int]) -> List[int]:
        min_val = min(remaining)
        max_val = max(remaining)
        return [min_val, max_val]

    sorted_list = []
    remaining = lst[:]
    while len(remaining) > 0:
        min_max = get_min_max(remaining)
        sorted_list.extend(min_max)
        remaining.remove(min_max[0])
        remaining.remove(min_max[1])
    return sorted_list
