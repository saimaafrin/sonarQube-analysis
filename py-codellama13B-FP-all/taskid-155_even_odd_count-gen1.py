from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    count_even, count_odd = 0, 0
    if num < 0:
        num = num * -1

    while num > 0:
        last_digit = num % 10
        if last_digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        num = num // 10

    return (count_even, count_odd)
