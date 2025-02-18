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

    # Sort the list of integers according to the sum of their digits
    # and keep the index for each item in the original list
    ordered_list = sorted(enumerate(nums), key=lambda x: sum(map(int, str(x[1]))))

    # Get the list of integers sorted by the sum of their digits
    # and reorder the original list based on the indices
    return [x[1] for x in ordered_list]
