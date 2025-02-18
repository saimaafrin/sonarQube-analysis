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

    neg_count, pos_count, zero_count = 0, 0, 0
    for x in arr:
        if x < 0:
            neg_count += 1
        elif x > 0:
            pos_count += 1
        else:
            zero_count += 1

    if pos_count and neg_count:
        sign = -1
    elif zero_count:
        sign = 0
    else:
        sign = 1

    return sign * sum(arr)
