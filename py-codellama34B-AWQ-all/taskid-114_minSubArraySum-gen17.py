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


    max_so_far = max_ending_here = nums[0]
    min_ending_here = nums[0]
    min_so_far = nums[0]

    for i in range(1, len(nums)):
        # min_ending_here is the min of previous min and current value
        min_ending_here = min(nums[i], min_ending_here)
        max_ending_here = max(nums[i], max_ending_here)

        # max_so_far is the max of previous max and current max_ending_here
        max_so_far = max(max_so_far, max_ending_here)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far
