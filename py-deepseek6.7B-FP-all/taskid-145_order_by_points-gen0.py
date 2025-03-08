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


    def get_sum(n: int) -> int:
        if n < 0:
            n = -n
        return sum(map(int, str(n)))

    return sorted(nums, key=lambda x: (get_sum(x), nums.index(x)))
