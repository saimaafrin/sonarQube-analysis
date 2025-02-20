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

    # O(n) time O(n) space
    # The idea is to maintain a running sum,
    # and keep updating the min value for each subarray.
    n = len(nums)
    min_sum = float('inf')
    curr_sum = 0

    for i in range(n):
        curr_sum += nums[i]
        min_sum = min(min_sum, curr_sum)
        curr_sum = max(curr_sum, 0)

    return min_sum
