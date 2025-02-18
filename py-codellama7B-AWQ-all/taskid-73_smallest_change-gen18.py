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
        arr_reversed = arr[::-1]
        return arr == arr_reversed

    def change_to_make_palindromic(arr: List[int]) -> int:
        min_changes = float('inf')
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] == arr[j]:
                    continue
                min_changes = min(min_changes, abs(arr[i] - arr[j]))
        return min_changes

    if is_palindromic(arr):
        return 0
    else:
        return change_to_make_palindromic(arr)
