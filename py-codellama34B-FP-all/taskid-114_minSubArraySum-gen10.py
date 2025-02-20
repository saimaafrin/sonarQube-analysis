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

    # init
    # max_sum = 0
    min_sum = float('inf')

    current_sum = 0
    # loop
    for n in nums:
        current_sum += n

        # update
        min_sum = min(min_sum, current_sum)

        # edge case
        if current_sum < 0:
            current_sum = 0
    return min_sum
