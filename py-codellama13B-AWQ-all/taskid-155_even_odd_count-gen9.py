from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    s = str(abs(num))
    return len([int(i) % 2 for i in s if i.isdigit() and int(i) % 2 == 0]), len([int(i) % 2 for i in s if i.isdigit() and int(i) % 2 == 1])
