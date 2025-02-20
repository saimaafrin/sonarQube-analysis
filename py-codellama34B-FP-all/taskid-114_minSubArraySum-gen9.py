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

    total = sum(nums)
    if total == 0:
        return 0

    min_sum = total + 1
    prefix_sum = 0

    for num in nums:
        prefix_sum += num
        if prefix_sum == total:
            return 1
        if min_sum > prefix_sum:
            min_sum = prefix_sum
    return min_sum
