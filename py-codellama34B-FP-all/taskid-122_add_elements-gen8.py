from typing import List

def add_elements(arr: List[int], k: int) -> int:
    """
    Given a non-empty array of integers arr and an integer k, return
    the sum of the elements with at most two digits from the first k elements of arr.

    Example:

    >>> add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4)
    24

    Constraints:
        1. 1 <= len(arr) <= 100
        2. 1 <= k <= len(arr)
    """


    arr.sort()
    # Initialize variables to keep track of the sum and
    # the number of digits in the current window.
    window_sum, num_digits = 0, 0
    for i in range(k):
        window_sum += arr[i]
        num_digits += len(str(arr[i]))

    # Initialize the result to be the current window sum.
    result = window_sum

    # Loop through the remaining elements and
    # update the window sum and the result.
    for i in range(k, len(arr)):
        # Add the next element to the window sum
        # and remove the first element of the window.
        window_sum += arr[i] - arr[i-k]
        # Remove the count of digits of the first element.
        num_digits -= len(str(arr[i-k]))
        # Add the count of digits of the next element.
        num_digits += len(str(arr[i]))

        # Update the result if the number of digits
        # in the current window is at most two.
        if num_digits <= 2:
            result = max(result, window_sum)

    return result
