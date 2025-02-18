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

    # your code here
    if len(lst) == 0:
        return []
    lst.sort()
    n = len(lst)
    new_lst = [lst[0]]
    for i in range(1, n - 1):
        new_lst.append(lst[i])
        new_lst.append(lst[-1])
        lst.pop(-1)
        lst.pop(0)
    return new_lst
