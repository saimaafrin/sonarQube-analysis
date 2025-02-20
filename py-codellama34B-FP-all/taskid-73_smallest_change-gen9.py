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


    def is_palindromic(arr: List[int]) -> bool:
        """Checks if array is palindromic."""
        return arr == arr[::-1]

    n = len(arr)
    if n <= 1:
        return 0
    if n == 2:
        return 1

    count = 0
    while not is_palindromic(arr):
        if arr[0] != arr[-1]:
            if arr[0] > arr[-1]:
                arr[-1] = arr[0]
            else:
                arr[0] = arr[-1]
            count += 1
        arr = arr[1:-1]
        if not arr:
            return n

    return count
