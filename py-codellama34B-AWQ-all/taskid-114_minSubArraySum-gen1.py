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
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        if curr_sum - num < min_sum:
            min_sum = curr_sum - num
    return min_sum
