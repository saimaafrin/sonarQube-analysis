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
    even, odd = 0, 0

    while num > 0:
        mod = num % 10
        if mod % 2 == 0:
            even += 1
        else:
            odd += 1
        num //= 10

    return (even, odd)
