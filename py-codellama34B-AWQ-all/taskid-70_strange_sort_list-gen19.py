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

    result = []
    while len(lst) > 0:
        min_index = 0
        max_index = 0
        for i in range(len(lst)):
            if lst[i] < lst[min_index]:
                min_index = i
            elif lst[i] > lst[max_index]:
                max_index = i
        if len(result) % 2 == 0:
            result.append(lst[min_index])
        else:
            result.append(lst[max_index])
        lst.pop(max(min_index, max_index))
        lst.pop(min(min_index, max_index))
    return result
