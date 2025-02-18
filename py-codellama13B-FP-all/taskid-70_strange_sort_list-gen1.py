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

    # Base case: empty list
    if not lst:
        return []

    # Find minimum element and remove it from the list
    minimum = min(lst)
    lst.remove(minimum)

    # Find maximum element and remove it from the list
    maximum = max(lst)
    lst.remove(maximum)

    # Append minimum element to the new list
    new_list = [minimum]

    # Append maximum element to the new list
    new_list.append(maximum)

    # Recursive call for rest of the list
    new_list.extend(strange_sort_list(lst))

    return new_list
