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

    nums_sum = []
    for num in nums:
        sum_digits = 0
        while num > 0:
            sum_digits += num % 10
            num //= 10
        nums_sum.append(sum_digits)

    return [num for _, num in sorted(zip(nums_sum, nums))]
