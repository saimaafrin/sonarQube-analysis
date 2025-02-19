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

    length = len(lst)
    result = [0] * length

    # loop until length of result is equal to length of input
    # and result does not have any 0s remaining
    while length > 0 or 0 in result:
        # find minimum value of remaining input list
        min_index = lst.index(min(lst))
        # append this to result list
        result[length - 1] = lst.pop(min_index)
        # find maximum value of remaining input list
        max_index = lst.index(max(lst))
        # append this to result list
        result[length - 2] = lst.pop(max_index)

        length -= 2

    return result
