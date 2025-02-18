from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    even_count = 0
    odd_count = 0
    while num > 0:
        digit = num % 10
        num //= 10
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
\end{code}
