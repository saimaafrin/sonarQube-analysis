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

    if len(arr) == 0:
        return None
    signs = [1] * len(arr)
    for i, x in enumerate(arr):
        if x < 0:
            signs[i] = -1
        elif x == 0:
            signs[i] = 0
    return sum(signs) * product(arr)
