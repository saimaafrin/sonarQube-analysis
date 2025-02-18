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

    sum, start = 0, 0
    n = len(nums)
    for i in range(n):
        sum += nums[i]
        while sum >= nums[i]:
            sum -= nums[start]
            start += 1
        if sum < minSum or minSum == -1:
            minSum = sum
    return minSum
