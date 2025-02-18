from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    if a >= b:
        return []

    nums = []
    a, b = min(a, b), max(a, b)
    for num in range(a, b+1):
        if num % 2 == 0:
            nums.append(num)

    return nums
