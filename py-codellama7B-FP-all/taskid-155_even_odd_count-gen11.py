from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    num = abs(num)
    even_digits = odd_digits = 0
    while num:
        if num % 10 % 2 == 0:
            even_digits += 1
        else:
            odd_digits += 1
        num //= 10
    return even_digits, odd_digits
