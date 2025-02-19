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

    # Calculate the product of signs
    signs_product = 1
    for i in arr:
        if i < 0:
            signs_product *= -1

    # Calculate sum of magnitude of integers
    magnitude_sum = 0
    for i in arr:
        magnitude_sum += abs(i)

    return signs_product * magnitude_sum
