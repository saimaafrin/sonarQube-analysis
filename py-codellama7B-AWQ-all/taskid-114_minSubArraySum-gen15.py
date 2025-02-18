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


    if not nums:
        return 0
    min_sum = float('inf')
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            min_sum = min(min_sum, cur_sum)
    return min_sum
