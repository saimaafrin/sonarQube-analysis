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
    curr_sum = 0
    for i in range(len(nums)):
        curr_sum += nums[i]
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return min_sum if min_sum != float('inf') else 0
