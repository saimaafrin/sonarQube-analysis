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

    if a > b:
        a, b = b, a
    even_digits = []
    for i in range(a, b+1):
        digits = []
        for d in str(i):
            digits.append(int(d))
        if any(d % 2 == 0 for d in digits):
            even_digits.append(i)
    return even_digits
