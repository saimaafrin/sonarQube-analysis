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
    for char in str(num):
        if char in '02468':
            even += 1
        elif char in '13579':
            odd += 1
        else:
            raise ValueError('invalid digit')
    return even, odd
