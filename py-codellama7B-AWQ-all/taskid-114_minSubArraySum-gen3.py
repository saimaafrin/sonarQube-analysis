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

    n = len(nums)
    sum_ = sum(nums)
    min_sum = sum_
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            sub_sum = sum(nums[i - 1:j])
            if sub_sum < min_sum:
                min_sum = sub_sum
    return min_sum
