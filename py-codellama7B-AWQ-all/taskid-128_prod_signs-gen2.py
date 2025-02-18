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

    sign = 1
    prod = 1
    for x in arr:
        if x == 0:
            return None
        if x < 0:
            sign *= -1
        elif x > 0:
            sign *= 1
        prod *= sign
    return prod
