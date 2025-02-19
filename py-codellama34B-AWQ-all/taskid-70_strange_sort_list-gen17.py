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

    # Sort list
    lst.sort()

    # Create new list
    new_list = []
    n = len(lst)

    # Append values
    for i in range(n):
        new_list.append(lst[i])

        if i % 2 == 0:
            new_list.append(lst[-1])
            del lst[-1]

    return new_list
