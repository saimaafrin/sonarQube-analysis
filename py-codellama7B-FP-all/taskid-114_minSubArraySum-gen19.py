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
    left = 0
    right = 0
    curr_sum = 0
    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum > 0:
            min_sum = min(min_sum, curr_sum)
            curr_sum -= nums[left]
            left += 1
    return min_sum
