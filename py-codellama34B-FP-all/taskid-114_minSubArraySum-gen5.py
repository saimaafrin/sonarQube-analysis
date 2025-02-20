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

    # 初始化最小和为和最大值
    min_sum = sum(nums)
    # 累加和
    for i in range(1, len(nums)):
        nums[i] = nums[i] + nums[i-1]
        if min_sum > nums[i]:
            min_sum = nums[i]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if min_sum > nums[j] - nums[i]:
                min_sum = nums[j] - nums[i]

    return min_sum
