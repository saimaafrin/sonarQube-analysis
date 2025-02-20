from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    return sum(map(lambda x: x % 2, str(num))), sum(map(lambda x: 1 - x % 2, str(num)))
