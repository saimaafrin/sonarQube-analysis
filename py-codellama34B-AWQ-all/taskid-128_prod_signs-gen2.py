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

    # Initialize an empty array
    prod_arr: List[int] = []
    if not arr:
        return None
    # Iterate over the array
    for num in arr:
        if num == 0:
            prod_arr.append(0)
            continue
        # Calculate the product of all signs of each number in the array
        sign = 1 if num > 0 else -1
        # Calculate the magnitude of each number in the array
        magnitude = num if num > 0 else -num
        prod_arr.append(sign * magnitude)

    return sum(prod_arr)
