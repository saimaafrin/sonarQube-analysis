from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    if num < 0:
        num = num * -1
    count_even = 0
    count_odd = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num //= 10
    return (count_even, count_odd)
