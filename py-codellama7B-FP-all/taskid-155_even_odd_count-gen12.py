from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    str_num = str(abs(num))
    return len([i for i in str_num if int(i) % 2 == 0]), len([i for i in str_num if int(i) % 2 != 0])
