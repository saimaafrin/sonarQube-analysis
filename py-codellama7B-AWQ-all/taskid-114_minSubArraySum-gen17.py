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

    m = len(nums)
    n = len(nums)
    minSum = float('inf')
    for i in range(m):
        sum = 0
        for j in range(i, n):
            sum += nums[j]
            if sum < minSum:
                minSum = sum
    return minSum
