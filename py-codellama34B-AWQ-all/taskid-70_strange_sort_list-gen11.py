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

    # If the list is empty, return it.
    if not lst:
        return lst

    # Set two lists.
    # `left` contains all the minimum values,
    # `right` contains all the maximum values.
    left, right = [], []

    # Pop the minimum value to `left`
    # and maximum to `right`.
    left.append(min(lst))
    lst.remove(min(lst))
    right.append(max(lst))
    lst.remove(max(lst))

    # Iterate until the list is empty.
    while lst:
        # Get the minimum value.
        min_value = min(lst)
        left.append(min_value)
        lst.remove(min_value)
        # Get the maximum value.
        max_value = max(lst)
        right.append(max_value)
        lst.remove(max_value)

    # Return the joined list.
    return left + right
