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

    length = len(lst)
    sorted_list = []

    if length == 0:
        return sorted_list

    min_idx = lst.index(min(lst))
    sorted_list.append(lst[min_idx])
    lst.pop(min_idx)

    while lst:
        max_idx = lst.index(max(lst))
        sorted_list.append(lst[max_idx])
        lst.pop(max_idx)

        if not lst:
            break

        min_idx = lst.index(min(lst))
        sorted_list.append(lst[min_idx])
        lst.pop(min_idx)

    return sorted_list
