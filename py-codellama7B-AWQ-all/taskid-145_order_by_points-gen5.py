from typing import List

def order_by_points(nums: List[int]) -> List[int]:
    """
    Write a function which sorts the given list of integers
    in ascending order according to the sum of their digits.
    Note: if there are several items with similar sum of their digits,
    order them based on their index in original list.

    For example:
    >>> order_by_points([1, 11, -1, -11, -12])
    [-1, -11, 1, -12, 11]
    >>> order_by_points([])
    []
    """

    # Sort by digits sum
    nums = sorted(nums, key=lambda x: sum_digits(x))

    # Sort by index if sum of digits is the same
    for i in range(1, len(nums)):
        if sum_digits(nums[i]) == sum_digits(nums[i - 1]):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums
