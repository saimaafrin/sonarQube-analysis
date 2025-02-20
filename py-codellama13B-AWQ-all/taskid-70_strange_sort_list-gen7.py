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

    # check if the input list is empty
    if not lst:
        return []

    # sort the list using the minimum value
    lst.sort()

    # create a new list to store the result
    result = []

    # iterate through the sorted list and append the minimum value
    # then append the maximum value of the remaining integers
    # then append the minimum value of the remaining integers
    # repeat this process until the input list is empty
    while lst:
        result.append(lst[0])
        lst.remove(lst[0])
        lst.sort(reverse=True)
        result.append(lst[0])
        lst.remove(lst[0])
        lst.sort()

    # return the result
    return result
