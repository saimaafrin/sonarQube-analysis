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

    # Initialize variables
    largest_index = -1
    is_ascending = False

    # Iterate over arr
    for index, element in enumerate(arr):
        # Check if current element is not greater than or equal to the
        # element preceding it
        if (index == 0) or (element <= arr[index - 1]):
            # Check if current element is greater than the element
            # preceding it
            if index != 0 and element > arr[index - 1]:
                # Set is_ascending to True
                is_ascending = True

            # Set largest_index to the current index
            largest_index = index

    # Check if the list is in ascending order
    if is_ascending:
        # Return the largest_index
        return largest_index

    # Otherwise return -1
    return -1
