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

    n = len(lst)
    if n == 0:
        return lst

    result = []
    for i in range(n):
        if i % 2 == 0:
            # Find the minimum value
            min_value = min(lst)
            result.append(min_value)
            lst.remove(min_value)
        else:
            # Find the maximum value
            max_value = max(lst)
            result.append(max_value)
            lst.remove(max_value)
    return result
