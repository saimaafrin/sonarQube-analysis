from typing import List

def maximum(arr: List[int], k: int) -> List[int]:
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.

    Example 1:

    >>> maximum([-3, -4, 5], 3)
    [-4, -3, 5]

    Example 2:

    >>> maximum([4, -4, 4], 2)
    [4, 4]

    Example 3:

    >>> maximum([-3, 2, 1, 2, -1, -2, 1], 1)
    [2]

    Note:
        1. The length of the array will be in the range of [1, 1000].
        2. The elements in the array will be in the range of [-1000, 1000].
        3. 0 <= k <= len(arr)
    """

    # Time: O(n log k)
    # Space: O(k)
    # Note: this is a general solution.
    # Note: the solution in the second if-block below can be faster in practice
    # if you know the maximum element is in the first half of the array.
    # In fact, if the maximum element is in the first half of the array, 
    # there's no need to sort the whole array. Just use the first k elements 
    # and sort them would give the correct answer. This is the common trick.
    # This is just a sample of how to reduce the time complexity.
    # If you want to have a better solution, you can use other sorting algorithms
    # like radix sort or counting sort.

    # solution one
    arr.sort()
    return arr[-k:]

    # solution two
    if k <= len(arr):
        arr.sort()
        return arr[-k:]
    else:
        arr.sort()
        return arr
