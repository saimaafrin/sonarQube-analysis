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


    # sort the list in ascending order
    lst.sort()

    # create an empty list to store the sorted elements
    result = []

    # traverse the list in ascending order
    for i in range(0, len(lst), 2):
        # add the smallest element in the list to the result
        result.append(lst[i])

    # traverse the list in descending order
    for i in range(len(lst)-1, 0, -2):
        # add the largest element in the list to the result
        result.append(lst[i])

    return result
