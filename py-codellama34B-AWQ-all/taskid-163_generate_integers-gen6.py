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
    for num in range(a, b + 1):
        num_str = str(num)
        if "0" in num_str or "2" in num_str or "4" in num_str or "6" in num_str or "8" in num_str:
            even_digits.append(int(num_str))
    return even_digits
