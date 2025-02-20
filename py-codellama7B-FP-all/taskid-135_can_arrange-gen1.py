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

    def can_arrange_helper(arr: List[int], i: int) -> int:
        """Create a helper function which takes the current element and
        returns the largest index of an element which is not greater than or
        equal to the current element and is greater than the current element.
        """
        # Base case
        if i == len(arr):
            return -1

        # Recursive case
        j = i + 1
        while j < len(arr) and arr[j] <= arr[i]:
            j += 1

        if j == len(arr):
            return -1

        if arr[j] > arr[i]:
            return j

        # Recursive call
        return can_arrange_helper(arr, j)

    return can_arrange_helper(arr, 0)
