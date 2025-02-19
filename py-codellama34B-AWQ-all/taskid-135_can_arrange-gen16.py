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

    n = len(arr)
    if n < 2:
        return -1
    # We can use a dictionary to store the indices of the elements
    # so that we can easily look up the index of the element to check
    # if the array is sorted.
    indices = {element: i for i, element in enumerate(arr)}
    last_index = 0
    for i in range(1, n):
        if arr[i] < arr[last_index]:
            # If we find an element which is less than the last element
            # then we can swap the elements and update the last index.
            arr[indices[arr[i]]], arr[indices[arr[last_index]]] = \
                arr[indices[arr[last_index]]], arr[indices[arr[i]]]
            # Update the indices dictionary.
            indices[arr[i]] = indices[arr[last_index]]
            last_index = indices[arr[i]]
        else:
            # If the element is greater than or equal to the last element
            # then we update the last index to the current element.
            last_index = i
    # If the last element is equal to the largest element in the array
    # then we return the largest index.
    if arr[n - 1] == max(arr):
        return indices[max(arr)]
    return -1
