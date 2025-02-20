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
    for i in str(abs(num)):
        if int(i) % 2:
            odd += 1
        else:
            even += 1
    return even, odd
