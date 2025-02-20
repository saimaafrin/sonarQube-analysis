from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    even, odd = 0, 0
    abs_num = abs(num)
    while abs_num > 0:
        if abs_num % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        abs_num //= 10
    return (even, odd)
