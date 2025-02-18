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
    n = len(nums)
    if n == 1:
        return nums[0]
    min_sub_array = min(nums)
    sum_sub_array = sum(nums)
    for i in range(n - 1):
        if nums[i] < min_sub_array:
            min_sub_array = nums[i]
            sum_sub_array -= nums[i]
        else:
            sum_sub_array -= min_sub_array
            if sum_sub_array < min_sub_array:
                min_sub_array = sum_sub_array
    return min_sub_array
