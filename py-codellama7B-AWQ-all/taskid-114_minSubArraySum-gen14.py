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

    # if not nums:
    #     return 0
    # return min(map(sum, zip(*[iter(nums)] * 2)))
    left, right, min_sum = 0, 1, float('inf')
    for right, num in enumerate(nums):
        min_sum = min(min_sum, sum(nums[left:right+1]))
    return min_sum
