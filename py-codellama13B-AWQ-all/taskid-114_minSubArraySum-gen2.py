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

    min_sum = float('inf')
    s = 0
    for i in range(len(nums)):
        s += nums[i]
        for j in range(i+1):
            if j == 0:
                min_sum = min(min_sum, s)
            else:
                min_sum = min(min_sum, s - nums[j-1])
    return min_sum
