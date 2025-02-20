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

    # 2 pointer solution
    # idea: try to find the smallest sub-array with sum >= 0
    # if we have a sum >= 0, we can return the sum
    # otherwise, update the sum and move the start pointer
    n = len(nums)
    start, end, sum_ = 0, 0, 0
    while end < n:
        sum_ += nums[end]
        end += 1
        while sum_ < 0:
            sum_ -= nums[start]
            start += 1
        if end - start == 1:
            return sum_
    return sum_
