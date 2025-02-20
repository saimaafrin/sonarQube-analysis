from typing import List

def minSubArraySum(nums: List[int]) -> int:
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    >>> minSubArraySum([2, 3, 4, 1, 2, 4])
    1
    >>> minSubArraySum([-1, -2, -3])
    -6
    """

    minSum = float('inf')
    prefixSum = 0
    for num in nums:
        prefixSum += num
        minSum = min(minSum, prefixSum)
        if prefixSum < 0:
            prefixSum = 0
    return minSum
