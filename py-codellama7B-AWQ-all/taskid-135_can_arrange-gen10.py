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

    # Sort the array to make the problem easier to solve.
    arr.sort()

    # Create a list of the largest indices for each value in the array.
    largest = [0 for _ in range(arr[0] + 1)]

    # Initialize a flag to indicate if the array can be arranged.
    flag = True

    # Iterate over the array from right to left.
    for i in range(len(arr) - 1, -1, -1):
        # If the current element is greater than or equal to the preceding
        # element then set the flag to False and break out of the loop.
        if arr[i] >= arr[i - 1]:
            flag = False
            break

        # Otherwise set the largest index for the current element to the
        # current index minus one.
        else:
            largest[arr[i]] = i - 1

    # If the flag is still True then return the largest index of the element
    # with the largest value.
    if flag:
        return largest[arr[-1]]

    # Otherwise return -1.
    return -1
