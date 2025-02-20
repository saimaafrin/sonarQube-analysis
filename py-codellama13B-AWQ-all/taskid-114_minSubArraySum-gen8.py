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

    # 初始化最小和和最小和索引
    minSum, minIdx = 0, 0
    # 累加
    for i in range(len(nums)):
        # 累加
        minSum += nums[i]
        # 比较是否小于最小和
        if minSum < minIdx:
            # 更新最小和
            minIdx = minSum
    # 返回最小和
    return minIdx
