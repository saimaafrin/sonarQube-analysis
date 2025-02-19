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


    # Find all the minimum and maximum values
    min_val = min(lst)
    max_val = max(lst)

    # Create a new empty list
    result: List[int] = []

    # While there are still values left in the original list
    while len(lst) > 0:
        # Find the index of the minimum value
        min_index = lst.index(min_val)

        # Add the minimum value to the result list
        result.append(min_val)

        # Remove the minimum value from the original list
        lst.pop(min_index)

        # If the original list is not empty
        if len(lst) > 0:
            # Find the index of the maximum value
            max_index = lst.index(max_val)

            # Add the maximum value to the result list
            result.append(max_val)

            # Remove the maximum value from the original list
            lst.pop(max_index)

    # Return the result list
    return result
