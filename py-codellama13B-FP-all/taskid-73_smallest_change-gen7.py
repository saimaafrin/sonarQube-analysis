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

    # We can use the fact that sum of first n numbers = n(n+1)/2,
    # and the sum of last n numbers = n(n+1)/2

    # Get the sum of first and last half of the array
    n = len(arr)
    arr_sum = sum(arr)
    first_half_sum = sum(arr[:n//2])
    last_half_sum = sum(arr[n//2:])

    # The difference in first and last half of the array should be
    # equal to the difference between their sum and total sum of array
    diff = abs((first_half_sum + last_half_sum) - arr_sum)

    # If the difference is even, we can make the array palindromic by
    # changing half of the difference
    if diff % 2 == 0:
        return diff // 2

    # If the difference is odd, we can make the array palindromic by
    # changing ceil(diff/2) number of elements
    return (diff // 2) + 1
