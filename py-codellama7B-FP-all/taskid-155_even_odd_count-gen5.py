from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    count_of_even = count_of_odd = 0
    while num > 0:
        if num % 10 % 2 == 0:
            count_of_even += 1
        else:
            count_of_odd += 1
        num //= 10
    return count_of_even, count_of_odd
