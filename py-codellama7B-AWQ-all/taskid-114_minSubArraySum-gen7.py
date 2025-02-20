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

    cur_min = float('inf')
    cur_sum = 0
    for i in range(len(nums)):
        cur_sum += nums[i]
        if cur_sum < cur_min:
            cur_min = cur_sum
        elif cur_sum > cur_min:
            cur_sum = 0
    return cur_min
