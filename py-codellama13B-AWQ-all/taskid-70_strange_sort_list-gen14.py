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

    if not lst:
        return lst
    n = len(lst)
    res = []
    while n:
        res.append(min(lst))
        lst.remove(min(lst))
        n -= 1
        if not n:
            break
        res.append(max(lst))
        lst.remove(max(lst))
        n -= 1
    return res
