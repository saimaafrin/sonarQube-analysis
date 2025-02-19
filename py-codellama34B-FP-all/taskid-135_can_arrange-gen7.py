from typing import List

def can_arrange(arr: List[int]) -> int:
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    >>> can_arrange([1, 2, 4, 3, 5])
    3
    >>> can_arrange([1, 2, 3])
    -1
    """

    # Find the maximum value in the list
    max_value = max(arr)

    # Initialise a dictionary of lists
    # where the key is the value and the
    # list contains the indexes of the value
    value_to_indexes = {
        value: [] for value in range(1, max_value + 1)
    }

    # Populate the dictionary
    for i, value in enumerate(arr):
        value_to_indexes[value].append(i)

    # Get the list of indexes which are not in
    # ascending order
    bad_indexes = []
    for value, indexes in value_to_indexes.items():
        if len(indexes) > 1:
            bad_indexes.extend(indexes[1:])

    # Return the maximum index
    if bad_indexes:
        return max(bad_indexes)

    return -1
