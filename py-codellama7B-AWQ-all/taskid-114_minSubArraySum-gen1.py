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

    # Check if nums is valid
    if not nums or len(nums) == 0:
        return 0

    # Find the minimum sum of any sub-array
    min_sum = sys.maxsize
    min_sum_i = 0
    min_sum_j = 0

    for i in range(len(nums)):
        curr_sum = 0

        for j in range(i, len(nums)):
            curr_sum += nums[j]

            if curr_sum < min_sum:
                min_sum = curr_sum
                min_sum_i = i
                min_sum_j = j

    return min(min_sum, minSubArraySum(nums[min_sum_i + 1 : min_sum_j + 1]))
