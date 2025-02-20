from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    even_counter, odd_counter = 0, 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_counter += 1
        else:
            odd_counter += 1
    return even_counter, odd_counter
