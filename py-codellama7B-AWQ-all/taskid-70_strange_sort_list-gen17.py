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

    min_num = min(lst)
    max_num = max(lst)
    result = []
    if min_num == max_num:
        result.append(min_num)
        return result
    i = 0
    while i < len(lst):
        if lst[i] == min_num:
            result.append(min_num)
            lst.pop(i)
        elif lst[i] == max_num:
            result.append(max_num)
            lst.pop(i)
        else:
            i += 1
    result.append(min_num)
    result.append(max_num)
    return result
