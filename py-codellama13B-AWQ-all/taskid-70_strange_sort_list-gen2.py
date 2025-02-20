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
    
    min_val = min(lst)
    max_val = max(lst)
    lst.remove(min_val)
    lst.remove(max_val)
    
    return [min_val] + [max_val] + strange_sort_list(lst)
