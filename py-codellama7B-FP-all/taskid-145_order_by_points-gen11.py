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

    # sort by digit sum
    nums.sort(key=lambda x: sum(map(int, str(abs(x)))))
    # sort by index if sum of digits is the same
    for i in range(1, len(nums)):
        if sum(map(int, str(abs(nums[i])))) == \
                sum(map(int, str(abs(nums[i - 1])))):
            nums[i], nums[i - 1] = nums[i - 1], nums[i]

    return nums
