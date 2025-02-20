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

    """
    思路：
    - 不断的扫描nums，计算当前最小子数组和sum
    - 如果sum小于target，说明nums这个子数组和是足够小的，sum就是最小的
    - 如果sum大于target，说明nums这个子数组和是不够小的，sum是超出target的，因此要尝试向后扫描
    - 每次扫描nums，要计算出当前扫描到的数字sum
    """
    sum = 0
    target = 0
    for i in range(len(nums)):
        sum += nums[i]
        if sum < target:
            return sum
        if i + 1 < len(nums):
            target = sum - nums[i + 1]
        else:
            target = sum
    return sum
