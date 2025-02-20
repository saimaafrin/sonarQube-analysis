from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    even_digit_count = 0
    odd_digit_count = 0

    while num > 0:
        if num % 2 == 0:
            even_digit_count += 1
        else:
            odd_digit_count += 1
        num = num // 10

    return even_digit_count, odd_digit_count
