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

    assert all(isinstance(i, int) for i in lst), "List contains non-integer values"

    # return empty list for empty list
    if not lst:
        return lst

    # get min and max indices
    min_index = lst.index(min(lst))
    max_index = lst.index(max(lst))

    # initalize result list with min and max
    result = [lst[min_index], lst[max_index]]

    # loop through list
    for i in range(len(lst)-2):
        min_index = lst.index(min(lst))
        max_index = lst.index(max(lst))
        result.append(lst[min_index])
        result.append(lst[max_index])
        del lst[min_index]
        del lst[max_index-1]

    # return result list
    return result
