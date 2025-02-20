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


    # Step 1: Convert each item to digit sum tuple
    digit_sums = list(map(digit_sum, nums))

    # Step 2: Sort by digit sum
    sorted_indexes = sorted(range(len(digit_sums)), key=digit_sums.__getitem__)

    # Step 3: Reorder by original index
    return [nums[i] for i in sorted_indexes]
