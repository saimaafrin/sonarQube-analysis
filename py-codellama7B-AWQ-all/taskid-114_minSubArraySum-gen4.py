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

    min_sum = float("inf")
    left, right = 0, 0
    curr_sum = 0
    while right < len(nums):
        curr_sum += nums[right]
        right += 1
        while curr_sum >= nums[left]:
            curr_sum -= nums[left]
            left += 1
        min_sum = min(min_sum, curr_sum)
    return min_sum
