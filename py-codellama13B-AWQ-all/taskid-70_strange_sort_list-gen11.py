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
        # Find the minimum
        min_index = lst.index(min(lst))
        # Add to the result
        result.append(lst[min_index])
        # Remove the added element from the list
        lst.pop(min_index)

        # If there is one element left, just add it to the result and return
        if len(lst) == 1:
            result.append(lst[0])
            return result

        # Find the maximum of the remaining elements
        max_index = lst.index(max(lst))
        # Add to the result
        result.append(lst[max_index])
        # Remove the added element from the list
        lst.pop(max_index)

    return result
