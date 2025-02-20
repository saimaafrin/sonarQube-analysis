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

    n = len(arr)
    # find the smallest odd index
    smallest_odd = None
    for i in range(n):
        if arr[i] % 2 == 1:
            smallest_odd = i
            break
    # if the smallest odd is None, then all elements are even
    # return the difference between the two middle elements
    if smallest_odd == None:
        return (arr[n // 2] - arr[n // 2 - 1]) % 10
    # if the smallest odd is not None, then we need to find the smallest even
    # index to the right of the smallest odd index
    smallest_even = None
    for i in range(smallest_odd + 1, n):
        if arr[i] % 2 == 0:
            smallest_even = i
            break
    # if the smallest even is None, then the smallest odd is the only element
    # that needs to be changed
    if smallest_even == None:
        return 1
    # otherwise, we need to find the index that is the largest element that
    # is smaller than the smallest odd and is even
    largest_smaller_even = None
    for i in range(smallest_odd - 1, -1, -1):
        if arr[i] % 2 == 0 and arr[i] < arr[smallest_odd]:
            largest_smaller_even = i
            break
    # if the largest smaller even is None, then the smallest odd needs to be changed
    if largest_smaller_even == None:
        return 1
    # otherwise, we need to change the largest smaller even and the smallest odd
    return 2
