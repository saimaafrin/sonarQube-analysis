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

    even_digits = []
    for i in range(min(a, b), max(a, b) + 1):
        if i % 2 == 0:
            even_digits.append(i)
    return even_digits
