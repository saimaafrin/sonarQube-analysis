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

    running_sum = 0
    min_sum = float('inf')

    for num in nums:
        running_sum += num
        min_sum = min(min_sum, running_sum)
        if running_sum < 0:
            running_sum = 0

    return min_sum
