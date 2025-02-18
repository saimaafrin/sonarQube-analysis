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


    def get_points(num: int) -> int:
        points = 0
        while num != 0:
            points += abs(num % 10)
            num = num // 10
        return points

    # Sorting in-place with a custom key function
    nums.sort(key=get_points)
    return nums
