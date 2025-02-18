from typing import Tuple

def even_odd_count(num: int) -> Tuple[int, int]:
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
    >>> even_odd_count(-12)
    (1, 1)
    >>> even_odd_count(123)
    (1, 2)
    """

    digits = [int(x) for x in str(abs(num))]
    even_digits = []
    odd_digits = []
    for i in digits:
        if i % 2 == 0:
            even_digits.append(i)
        else:
            odd_digits.append(i)
    return (len(even_digits), len(odd_digits))
