from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4])
    9
    >>> prod_signs([0, 1])
    0
    >>> prod_signs([])
    None
    """

    if not arr:
        return None

    # O(N) time | O(1) space
    # return sum(map(abs, arr)) * (-1) ** len([e for e in arr if e < 0])

    # O(N) time | O(1) space
    abs_sum = sum(map(abs, arr))
    neg_count = 0
    for num in arr:
        if num < 0:
            neg_count += 1
    return abs_sum * (-1) ** neg_count
