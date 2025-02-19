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

    nums_index_sum = [(num, sum(map(int, str(num)))) for num in nums]
    nums_index_sum.sort(key=lambda x: x[1])
    return [num for num, _ in nums_index_sum]
