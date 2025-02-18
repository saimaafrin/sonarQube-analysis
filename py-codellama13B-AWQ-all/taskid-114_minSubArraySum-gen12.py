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

    if len(nums) == 0:
        return 0
    
    min_so_far = nums[0]
    current_sum = 0
    for num in nums:
        current_sum += num
        if current_sum < min_so_far:
            min_so_far = current_sum
    return min_so_far
