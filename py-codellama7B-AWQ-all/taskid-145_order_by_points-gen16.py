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

    # --------------------------------------------------------------------------
    #                                Approach 1
    # --------------------------------------------------------------------------
    return sorted(nums, key=lambda x: (sum(str(x)), x))

    # --------------------------------------------------------------------------
    #                                Approach 2
    # --------------------------------------------------------------------------
    return sorted(nums, key=lambda x: (sum(map(int, list(str(x)))), x))

    # --------------------------------------------------------------------------
    #                                Approach 3
    # --------------------------------------------------------------------------
    nums.sort(key=lambda x: (sum(map(int, list(str(x)))), x))
    return nums

    # --------------------------------------------------------------------------
    #                                Approach 4
    # --------------------------------------------------------------------------
    return sorted(nums, key=lambda x: (sum(map(int, str(x))), x))

    # --------------------------------------------------------------------------
    #                                Approach 5
    # --------------------------------------------------------------------------
    return sorted(nums, key=lambda x: (sum(x), x))
