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


    # sorting the list
    lst.sort()

    # reversing the list if its length is odd
    if len(lst) % 2 != 0:
        lst.reverse()

    # creating result list
    result = []

    # adding first element to result list
    result.append(lst[0])

    # adding rest of the elements
    for i in range(1, len(lst)):

        # if its odd index, then add maximum of remaining integers
        if i % 2 != 0:
            result.append(max(lst[i:]))

        # if its even index, then add minimum of remaining integers
        else:
            result.append(min(lst[i:]))

    return result
