from typing import List

def smallest_change(arr: List[int]) -> int:
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    >>> smallest_change([1, 2, 3, 5, 4, 7, 9, 6])
    4
    >>> smallest_change([1, 2, 3, 4, 3, 2, 2])
    1
    >>> smallest_change([1, 2, 3, 2, 1])
    0
    """

    # Get the length of the array
    n = len(arr)
    # The minimum number of elements to be changed
    count = 0

    # The center of the array.
    center = n // 2

    # This variable stores the minimum number of elements that need to be changed
    # to make the array palindromic.
    min_change = float('inf')

    # The maximum number of elements to be changed
    max_change = (n // 2) + 1

    # Loop through the elements of the array
    for i in range(n):
        # The index of the element
        index = i

        # Loop through the elements to the right of the element
        while index < n:
            # Check if the element is the center element
            if index == center:
                # The minimum number of elements to be changed
                # to make the array palindromic.
                min_change = min(min_change, count + 1)

                # The maximum number of elements to be changed
                max_change = min(max_change, count + 1)

                # Break out of the while loop
                break

            # Check if the element is the same
            if arr[i] == arr[index]:
                # Increase the number of elements to be changed
                count += 1

                # Increase the index of the element
                index += 1

                # Continue to the next iteration of the loop
                continue
            else:
                # Decrease the number of elements to be changed
                count -= 1

                # Increase the index of the element
                index += 1

    return min_change
