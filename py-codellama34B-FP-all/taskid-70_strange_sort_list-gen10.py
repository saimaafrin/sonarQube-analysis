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

    result = []
    while lst:
        # find minimum
        minimum = min(lst)
        result.append(minimum)
        # remove minimum from the list
        lst.remove(minimum)
        if not lst:
            break
        # find maximum of the remaining list
        maximum = max(lst)
        result.append(maximum)
        # remove maximum from the list
        lst.remove(maximum)

    return result
