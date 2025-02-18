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

    # Your code here
    lst = sorted(lst)
    i = 0
    result = []
    while i < len(lst):
        result.append(lst[i])
        if i+1 < len(lst) and lst[i+1] > lst[i]:
            result.append(lst[i+1])
            i += 2
        else:
            i += 1
    return result
