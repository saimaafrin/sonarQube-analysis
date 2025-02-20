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
        return []

    sorted_lst = []
    while lst:
        # minimum value
        sorted_lst.append(min(lst))
        # remove the minimum value
        lst.remove(min(lst))

        # maximum of the remaining integers
        sorted_lst.append(max(lst))
        # remove the maximum of the remaining integers
        lst.remove(max(lst))
    return sorted_lst
