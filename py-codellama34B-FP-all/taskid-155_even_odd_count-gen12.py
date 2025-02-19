from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    num_even, num_odd = 0, 0
    while num:
        last = num % 10
        if last % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
        num //= 10
    return num_even, num_odd
