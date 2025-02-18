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

    # TODO - implement the function
    # sort the list
    lst.sort()
    # create a new list to return
    return_list = []
    # append the minimum value
    return_list.append(lst[0])
    # if there are more than one minimum value, append all of them
    for i in range(1, len(lst)):
        if lst[i] == lst[0]:
            return_list.append(lst[i])
    # append the maximum value
    return_list.append(lst[-1])
    # if there are more than one maximum value, append all of them
    for i in range(len(lst)-2, -1, -1):
        if lst[i] == lst[-1]:
            return_list.append(lst[i])
    # return the list
    return return_list
