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


    """
    Method 1: Two pointers approach

    First, sort the array in ascending order and find the
    first number that is greater than or equal to k.

    If the first number in the sorted array is greater than or equal
    to k, then the answer is 0.

    Otherwise, we iterate through the array and find the first number
    greater than or equal to k. If such a number is not found, then
    the answer is 0.

    Otherwise, we iterate through the array and find the first number
    that is greater than or equal to k. We count the number of elements
    that are greater than or equal to k.

    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    # Method 2: Two pointer approach

    # Sort the array in ascending order
    arr.sort()

    # Find the first number greater than or equal to k
    for i in range(k):
        if arr[i] >= k:
            break

    if i == k:
        return 0

    # Find the first number greater than or equal to k
    for j in range(i, len(arr)):
        if arr[j] >= k:
            break

    if j == len(arr):
        return 0

    # Count the number of elements greater than or equal to k
    count = 0
    for l in range(j, len(arr)):
        if arr[l] >= k:
            count += 1

    return count
