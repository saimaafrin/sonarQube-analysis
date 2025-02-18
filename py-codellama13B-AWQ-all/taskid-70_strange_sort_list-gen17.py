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

    if len(lst) == 1:
        return lst
    elif len(lst) == 0:
        return []
    else:
        sorted_list = [lst[0]]
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                sorted_list.append(lst[i])
            elif lst[i] < lst[i - 1]:
                sorted_list.append(lst[i - 1])
        return sorted_list
