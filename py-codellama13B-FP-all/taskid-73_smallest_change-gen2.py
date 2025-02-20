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


    # Edge cases
    if len(arr) <= 1:
        return 0

    # O(n) time and space
    def min_changes(arr):
        n = len(arr)
        left_sums = [0] * n
        for i in range(1, n):
            left_sums[i] = left_sums[i - 1] + arr[i - 1]
        right_sums = [0] * n
        for i in range(n - 2, -1, -1):
            right_sums[i] = right_sums[i + 1] + arr[i + 1]
        # print(left_sums, right_sums)
        min_changes = float('inf')
        for i in range(n):
            # print(i, left_sums[i], right_sums[i])
            min_changes = min(min_changes, abs(left_sums[i] - right_sums[i]))
        return min_changes

    # O(n^2) time and space
    def min_changes2(arr):
        n = len(arr)
        min_changes = float('inf')
        for i in range(n):
            left_sum = 0
            for j in range(i):
                left_sum += arr[j]
            right_sum = 0
            for j in range(i + 1, n):
                right_sum += arr[j]
            min_changes = min(min_changes, abs(left_sum - right_sum))
        return min_changes

    return min_changes2(arr)
