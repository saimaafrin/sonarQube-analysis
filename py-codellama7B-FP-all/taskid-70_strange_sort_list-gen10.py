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

    # Write your code here
    if len(lst) == 0:
        return []

    # Sort the list using the standard method
    lst.sort()

    # Start with the minimum value
    sorted_list = [lst[0]]

    # Then the maximum of the remaining integers
    sorted_list.append(max(lst[1:]))

    # Then the minimum and so on.
    sorted_list.extend(lst[2:])

    return sorted_list
